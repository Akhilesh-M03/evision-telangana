import logging
from datetime import datetime
from pathlib import Path

import pandas as pd
from sqlmodel import Session, select

from models.application_metadata import ApplicationMetadata
from models.charging_stations import ChargingStation
from models.district import District
from models.district_analytics import DistrictAnalytics
from models.district_prediction import DistrictPrediction
from models.district_recommendation import DistrictRecommendation
from models.historical_demand import HistoricalDemand

logger = logging.getLogger(__name__)

# Base path for interim data files relative to workspace root
BASE_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "interim"


def seed_districts(session: Session) -> dict[str, int]:
    """Seed districts from district_geography.csv.

    Args:
        session: The active database session.

    Returns:
        dict[str, int]: Mapping of lowercase district names to their primary key IDs.
    """
    csv_path = BASE_DATA_DIR / "geography" / "district_geography.csv"
    logger.info(f"Seeding districts from {csv_path}...")

    if not csv_path.exists():
        logger.error(f"District geography CSV not found at {csv_path}")
        raise FileNotFoundError(f"District geography CSV not found at {csv_path}")

    df = pd.read_csv(csv_path)
    if "district_name" not in df.columns:
        logger.error("Column 'district_name' not found in district geography CSV.")
        raise KeyError("Column 'district_name' not found in district geography CSV.")

    district_names = df["district_name"].dropna().unique().tolist()
    district_names = [name.strip() for name in district_names]
    district_names.sort()

    district_map = {}
    for name in district_names:
        existing = session.exec(
            select(District).where(District.district_name == name)
        ).first()
        if existing:
            db_district = existing
        else:
            db_district = District(district_name=name)
            session.add(db_district)
            session.flush()  # Flush to obtain the database-generated ID
        district_map[name.lower()] = db_district.id

    session.commit()
    logger.info(f"Successfully seeded {len(district_map)} districts.")
    return district_map


def seed_charging_stations(session: Session, district_map: dict[str, int]) -> None:
    """Seed charging station records from charging_stations_clean.csv.

    Args:
        session: The active database session.
        district_map: Mapping of lowercase district names to their IDs.
    """
    csv_path = BASE_DATA_DIR / "charging_stations" / "charging_stations_clean.csv"
    logger.info(f"Seeding charging stations from {csv_path}...")

    if not csv_path.exists():
        logger.error(f"Charging stations CSV not found at {csv_path}")
        raise FileNotFoundError(f"Charging stations CSV not found at {csv_path}")

    df = pd.read_csv(csv_path)
    station_count = 0

    for _, row in df.iterrows():
        raw_dist = row.get("district")
        if pd.isna(raw_dist):
            continue

        dist_name = str(raw_dist).strip().lower()
        district_id = district_map.get(dist_name)

        if not district_id:
            logger.warning(
                f"District '{raw_dist}' not found in district map. Skipping station '{row.get('station_name')}'."
            )
            continue

        station_name = str(row["station_name"]).strip() if not pd.isna(row.get("station_name")) else None
        org = str(row["owning_organisation"]).strip() if not pd.isna(row.get("owning_organisation")) else None
        addr = str(row["address"]).strip() if not pd.isna(row.get("address")) else None
        lat = float(row["latitude"]) if not pd.isna(row.get("latitude")) else None
        lon = float(row["longitude"]) if not pd.isna(row.get("longitude")) else None

        # Clean invalid coordinates to satisfy check constraints
        if lat is not None and (lat < -90 or lat > 90):
            lat = None
        if lon is not None and (lon < -180 or lon > 180):
            lon = None

        station = ChargingStation(
            district_id=district_id,
            station_name=station_name,
            organization=org,
            address=addr,
            latitude=lat,
            longitude=lon,
        )
        session.add(station)
        station_count += 1

    session.commit()
    logger.info(f"Successfully seeded {station_count} charging stations.")


def seed_historical_demand(session: Session, district_map: dict[str, int]) -> None:
    """Seed historical EV charging demand records.

    Args:
        session: The active database session.
        district_map: Mapping of lowercase district names to their IDs.
    """
    csv_path = BASE_DATA_DIR / "merged" / "master_dataset_v1.csv"
    logger.info(f"Seeding historical demand from {csv_path}...")

    if not csv_path.exists():
        logger.error(f"Historical consumption CSV not found at {csv_path}")
        raise FileNotFoundError(f"Historical consumption CSV not found at {csv_path}")

    df = pd.read_csv(csv_path)
    
    # Ensure no duplicates on composite key (district, reporting_month)
    df_clean = df.drop_duplicates(subset=["district", "reporting_month"])
    demand_count = 0

    for _, row in df_clean.iterrows():
        raw_dist = row.get("district")
        if pd.isna(raw_dist):
            continue

        dist_name = str(raw_dist).strip().lower()
        district_id = district_map.get(dist_name)

        if not district_id:
            logger.warning(
                f"District '{raw_dist}' not found in district map. Skipping demand record."
            )
            continue

        rep_month = str(row["reporting_month"]).strip()
        units = float(row["units"]) if not pd.isna(row.get("units")) else 0.0

        demand = HistoricalDemand(
            district_id=district_id,
            reporting_month=rep_month,
            demand_kwh=units,
        )
        session.add(demand)
        demand_count += 1

    session.commit()
    logger.info(f"Successfully seeded {demand_count} historical demand records.")


def seed_metadata(session: Session) -> None:
    """Seed application metadata key-values.

    Args:
        session: The active database session.
    """
    logger.info("Seeding application metadata...")

    meta_entries = [
        ("schema_version", "1.0.0"),
        ("initialized_at", datetime.utcnow().isoformat()),
        ("last_seeded_at", datetime.utcnow().isoformat()),
        ("dataset_version", "April 2024"),
    ]

    for key, val in meta_entries:
        existing = session.exec(
            select(ApplicationMetadata).where(ApplicationMetadata.metadata_key == key)
        ).first()
        if existing:
            existing.metadata_value = val
            existing.updated_at = datetime.utcnow()
            session.add(existing)
        else:
            meta = ApplicationMetadata(metadata_key=key, metadata_value=val)
            session.add(meta)

    session.commit()
    logger.info("Successfully seeded application metadata.")


def seed_all() -> None:
    """Clear existing tables and seed all reference datasets into the database."""
    # Ensure tables are initialized first
    from database.initialization import initialize_database
    initialize_database()

    from database.engine import engine

    with Session(engine) as session:
        logger.info("Clearing existing database tables before seeding...")
        try:
            # Delete child tables first to respect foreign key constraints
            session.query(DistrictRecommendation).delete()
            session.query(DistrictAnalytics).delete()
            session.query(DistrictPrediction).delete()
            session.query(HistoricalDemand).delete()
            session.query(ChargingStation).delete()
            session.query(ApplicationMetadata).delete()
            session.query(District).delete()
            session.commit()
            logger.info("Database tables cleared.")
        except Exception as e:
            session.rollback()
            logger.error(f"Error clearing database tables: {e}")
            raise e

        # Seed tables in dependency order
        try:
            district_map = seed_districts(session)
            seed_charging_stations(session, district_map)
            seed_historical_demand(session, district_map)
            seed_metadata(session)
            logger.info("Database seeding completed successfully.")
        except Exception as e:
            session.rollback()
            logger.error(f"Seeding failed: {e}")
            raise e
