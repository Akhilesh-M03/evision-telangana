import logging
import sys
from datetime import datetime
from pathlib import Path

# Add backend directory to sys.path to resolve imports correctly
BACKEND_DIR = Path(__file__).resolve().parents[1]
if str(BACKEND_DIR) not in sys.path:
    sys.path.append(str(BACKEND_DIR))

from sqlmodel import Session, select

from core.settings import settings
from database.engine import engine
from database.initialization import initialize_database
from database.seed import seed_all
from models.application_metadata import ApplicationMetadata
from models.charging_stations import ChargingStation
from models.district import District
from models.district_analytics import DistrictAnalytics
from models.district_prediction import DistrictPrediction
from models.district_recommendation import DistrictRecommendation
from models.historical_demand import HistoricalDemand

# Configure logging to stdout
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)


def run_verification() -> bool:
    """Run verification checks on the database schema, seeding, and relationships.

    Returns:
        bool: True if verification passes, False otherwise.
    """
    logger.info("Starting database verification...")
    logger.info(f"Database URL configured: {settings.database_url}")

    # 1. Initialize and Seed
    try:
        initialize_database()
        seed_all()
    except Exception as e:
        logger.error(f"Initialization or Seeding failed: {e}")
        return False

    # 2. Check table records and counts
    with Session(engine) as session:
        # Check districts
        districts = session.exec(select(District)).all()
        logger.info(f"Found {len(districts)} districts in database.")
        if len(districts) != 33:
            logger.error(f"Expected 33 districts, found {len(districts)}.")
            return False

        # Check charging stations
        stations = session.exec(select(ChargingStation)).all()
        logger.info(f"Found {len(stations)} charging stations in database.")
        if len(stations) == 0:
            logger.error("Expected at least one charging station, found 0.")
            return False

        # Check historical demand
        demand_records = session.exec(select(HistoricalDemand)).all()
        logger.info(f"Found {len(demand_records)} historical demand records in database.")
        if len(demand_records) == 0:
            logger.error("Expected historical demand records, found 0.")
            return False

        # Check metadata
        metadata = session.exec(select(ApplicationMetadata)).all()
        logger.info(f"Found {len(metadata)} metadata keys.")
        for item in metadata:
            logger.info(f"  Metadata Key: {item.metadata_key} -> {item.metadata_value}")

        # 3. Verify Relationships
        # Retrieve Adilabad and verify charging stations
        adilabad = session.exec(select(District).where(District.district_name == "Adilabad")).first()
        if not adilabad:
            logger.error("Adilabad district not found in database.")
            return False

        logger.info(f"Retrieved district '{adilabad.district_name}' with ID: {adilabad.id}")
        
        # Test One-to-Many Relationship: District -> ChargingStation
        logger.info(f"Adilabad charging stations count: {len(adilabad.charging_stations)}")
        for station in adilabad.charging_stations[:3]:
            logger.info(f"  Station: {station.station_name} | Org: {station.organization}")

        # Test One-to-Many Relationship: District -> HistoricalDemand
        logger.info(f"Adilabad historical demand records: {len(adilabad.historical_demand)}")
        for record in adilabad.historical_demand[:3]:
            logger.info(f"  Month: {record.reporting_month} | Demand (kWh): {record.demand_kwh}")

        # 4. Verify Predictions, Analytics, and Recommendations insertion and constraints
        logger.info("Verifying District Prediction, Analytics, and Recommendation entities...")
        try:
            # Create a prediction record
            prediction = DistrictPrediction(
                district_id=adilabad.id,
                forecast_period="2024-05",
                predicted_demand=12500.5,
                model_version="v1.0",
                generated_at=datetime.utcnow()
            )
            session.add(prediction)

            # Create an analytics record
            analytics = DistrictAnalytics(
                district_id=adilabad.id,
                cluster_id=2,
                historical_average_demand=9500.2,
                trend_label="High Growth",
                generated_at=datetime.utcnow()
            )
            session.add(analytics)

            # Create a recommendation record
            recommendation = DistrictRecommendation(
                district_id=adilabad.id,
                priority_score=85.5,
                priority_level="High",
                district_rank=3,
                generated_at=datetime.utcnow()
            )
            session.add(recommendation)
            session.commit()

            logger.info("Successfully saved Prediction, Analytics, and Recommendation records.")
        except Exception as e:
            session.rollback()
            logger.error(f"Failed to insert ML/Analytics/Decision records: {e}")
            return False

        # Verify relationships of newly added records
        session.refresh(adilabad)
        
        # District -> Predictions
        if not adilabad.predictions:
            logger.error("District predictions relationship returned empty.")
            return False
        logger.info(f"Verified district predictions relationship: {adilabad.predictions[0].predicted_demand}")

        # District -> Analytics (One-to-One)
        if not adilabad.analytics:
            logger.error("District analytics relationship returned empty.")
            return False
        logger.info(f"Verified district analytics relationship: cluster_id={adilabad.analytics.cluster_id}, trend={adilabad.analytics.trend_label}")

        # District -> Recommendation (One-to-One)
        if not adilabad.recommendation:
            logger.error("District recommendation relationship returned empty.")
            return False
        logger.info(f"Verified district recommendation relationship: priority_score={adilabad.recommendation.priority_score}, rank={adilabad.recommendation.district_rank}")

        # Test Check Constraint on DistrictRecommendation priority_score (should fail if < 0)
        try:
            invalid_recommendation = DistrictRecommendation(
                district_id=adilabad.id,
                priority_score=-1.0,  # Invalid
                priority_level="Low",
                district_rank=34,
                generated_at=datetime.utcnow()
            )
            session.add(invalid_recommendation)
            session.commit()
            logger.error("Constraint check failed: inserted recommendation with negative priority_score.")
            return False
        except Exception:
            session.rollback()
            logger.info("Verified: priority_score >= 0 check constraint behaves correctly (rejected negative values).")

        # Test Check Constraint on DistrictRecommendation district_rank (should fail if <= 0)
        try:
            invalid_rank = DistrictRecommendation(
                district_id=adilabad.id,
                priority_score=10.0,
                priority_level="Low",
                district_rank=0,  # Invalid (rank must be > 0)
                generated_at=datetime.utcnow()
            )
            session.add(invalid_rank)
            session.commit()
            logger.error("Constraint check failed: inserted recommendation with rank <= 0.")
            return False
        except Exception:
            session.rollback()
            logger.info("Verified: district_rank > 0 check constraint behaves correctly (rejected rank <= 0).")

        # Test Unique Constraint on District district_name
        try:
            duplicate_district = District(district_name="Adilabad")
            session.add(duplicate_district)
            session.commit()
            logger.error("Constraint check failed: inserted duplicate district name.")
            return False
        except Exception:
            session.rollback()
            logger.info("Verified: district_name unique constraint behaves correctly (rejected duplicate name).")

        # Test Unique Constraint on HistoricalDemand (district_id, reporting_month)
        try:
            duplicate_demand = HistoricalDemand(
                district_id=adilabad.id,
                reporting_month=adilabad.historical_demand[0].reporting_month,
                demand_kwh=100.0
            )
            session.add(duplicate_demand)
            session.commit()
            logger.error("Constraint check failed: inserted duplicate historical demand for same month.")
            return False
        except Exception:
            session.rollback()
            logger.info("Verified: composite unique constraint (district_id, reporting_month) behaves correctly.")

    logger.info("All verification checks completed successfully.")
    return True


if __name__ == "__main__":
    success = run_verification()
    if success:
        logger.info("Database verification PASSED.")
        sys.exit(0)
    else:
        logger.error("Database verification FAILED.")
        sys.exit(1)
