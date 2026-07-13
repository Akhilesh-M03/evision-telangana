"""Preprocess charging stations data for EVision Telangana.

This script performs the following tasks:
- Loads raw charging station CSV and Telangana districts GeoJSON data.
- Validates the data schema.
- Standardizes column names to snake_case.
- Trims whitespace and normalizes text fields.
- Validates coordinates and filters out records with invalid or out-of-bounds coordinates.
- Standardizes district names using a Point-in-Polygon (PIP) check against the GeoJSON boundaries.
- Removes duplicate charging stations.
- Produces summary statistics.
- Outputs the cleaned data to an interim CSV and generates a markdown report.
"""

import json
import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

# Define paths relative to workspace root
WORKSPACE_DIR = Path(__file__).resolve().parents[1]
DEFAULT_CSV_PATH = WORKSPACE_DIR / "data" / "raw" / "charging_stations" / "EV_Charging_Stations_April_2024.csv"
DEFAULT_GEOJSON_PATH = WORKSPACE_DIR / "data" / "raw" / "geography" / "telangana_33_districts.geojson"
DEFAULT_OUT_CSV_PATH = WORKSPACE_DIR / "data" / "interim" / "charging_stations" / "charging_stations_clean.csv"
DEFAULT_REPORT_PATH = WORKSPACE_DIR / "report" / "charging_station_report.md"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(WORKSPACE_DIR / "scripts" / "preprocess_charging_stations.log", mode="w", encoding="utf-8")
    ]
)
logger = logging.getLogger(__name__)

# Expected input schema mapping (original column to standardized column)
SCHEMA_MAP: Dict[str, str] = {
    "S.No.": "s_no",
    "Name of the EV Charging Station (Private / Public Charging Infra)": "station_name",
    "State": "state",
    "District": "district",
    "Address": "address",
    "Latitude": "latitude",
    "Longitude": "longitude",
    "Name of the Owning Organisation/ Person": "owning_organisation"
}


def load_geojson(path: Path) -> Dict[str, Any]:
    """Load and parse the GeoJSON file containing district boundaries.

    Args:
        path: Path to the GeoJSON file.

    Returns:
        Dict representation of the GeoJSON data.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    logger.info(f"Loading GeoJSON from {path}")
    if not path.exists():
        logger.error(f"GeoJSON file not found at {path}")
        raise FileNotFoundError(f"GeoJSON file not found at {path}")
    
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_csv(path: Path) -> pd.DataFrame:
    """Load the raw EV Charging Stations CSV file.

    Args:
        path: Path to the CSV file.

    Returns:
        pd.DataFrame containing the raw data.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    logger.info(f"Loading CSV from {path}")
    if not path.exists():
        logger.error(f"CSV file not found at {path}")
        raise FileNotFoundError(f"CSV file not found at {path}")
    
    return pd.read_csv(path)


def validate_schema(df: pd.DataFrame, expected_columns: List[str]) -> None:
    """Validate that the loaded DataFrame has all expected columns.

    Args:
        df: DataFrame to validate.
        expected_columns: List of expected column names.

    Raises:
        ValueError: If any expected columns are missing.
    """
    missing_cols = [col for col in expected_columns if col not in df.columns]
    if missing_cols:
        logger.error(f"Schema validation failed. Missing columns: {missing_cols}")
        raise ValueError(f"Missing expected columns in CSV: {missing_cols}")
    logger.info("Schema validation passed.")


def is_point_in_polygon(x: float, y: float, polygon: List[List[List[float]]]) -> bool:
    """Determine if a point (x, y) lies inside a polygon using the Ray-Casting algorithm.

    Here, x represents longitude and y represents latitude.

    Args:
        x: Longitude of the point.
        y: Latitude of the point.
        polygon: Polygon coordinates as a list of lists of [lon, lat] points (from GeoJSON).

    Returns:
        True if the point is inside the polygon (exterior ring and not inside any interior holes), False otherwise.
    """
    def check_ring(px: float, py: float, ring: List[List[float]]) -> bool:
        inside = False
        n = len(ring)
        if n < 3:
            return False
        p1x, p1y = ring[0]
        for i in range(n + 1):
            p2x, p2y = ring[i % n]
            if py > min(p1y, p2y):
                if py <= max(p1y, p2y):
                    if px <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (py - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or px <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    # polygon[0] is the exterior ring
    if not check_ring(x, y, polygon[0]):
        return False
        
    # Check interior rings (holes), if any exist
    for hole in polygon[1:]:
        if check_ring(x, y, hole):
            return False
            
    return True


def get_district_for_point(lon: float, lat: float, geojson_data: Dict[str, Any]) -> Optional[str]:
    """Find the standardized Telangana district name containing the given coordinates.

    Args:
        lon: Longitude of the point.
        lat: Latitude of the point.
        geojson_data: The loaded GeoJSON district boundary data.

    Returns:
        Standardized district name if found, None otherwise.
    """
    for feature in geojson_data.get("features", []):
        district_name = feature["properties"]["dtname"]
        geom = feature.get("geometry", {})
        geom_type = geom.get("type")
        coords = geom.get("coordinates", [])
        
        if geom_type == "Polygon":
            if is_point_in_polygon(lon, lat, coords):
                return district_name
        elif geom_type == "MultiPolygon":
            # MultiPolygon is a list of polygons
            for poly in coords:
                if is_point_in_polygon(lon, lat, poly):
                    return district_name
    return None


def get_geojson_bounding_box(geojson_data: Dict[str, Any]) -> Tuple[float, float, float, float]:
    """Calculate the global bounding box of all polygons in the GeoJSON.

    Args:
        geojson_data: Loaded GeoJSON data.

    Returns:
        A tuple of (min_lon, max_lon, min_lat, max_lat).
    """
    min_lon, max_lon = 180.0, -180.0
    min_lat, max_lat = 90.0, -90.0
    
    for feature in geojson_data.get("features", []):
        geom = feature.get("geometry", {})
        geom_type = geom.get("type")
        coords = geom.get("coordinates", [])
        
        def process_ring(ring: List[List[float]]) -> None:
            nonlocal min_lon, max_lon, min_lat, max_lat
            for pt in ring:
                lon, lat = pt
                if lon < min_lon: min_lon = lon
                if lon > max_lon: max_lon = lon
                if lat < min_lat: min_lat = lat
                if lat > max_lat: max_lat = lat

        if geom_type == "Polygon":
            for ring in coords:
                process_ring(ring)
        elif geom_type == "MultiPolygon":
            for poly in coords:
                for ring in poly:
                    process_ring(ring)
                    
    return min_lon, max_lon, min_lat, max_lat


def parse_coordinate(val: Any) -> Optional[float]:
    """Parse a coordinate string in various formats to decimal degrees.

    Args:
        val: Input coordinate value.

    Returns:
        Decimal degrees float if successfully parsed, None otherwise.
    """
    if pd.isna(val):
        return None
        
    s = str(val).strip()
    if not s:
        return None
        
    # Clean trailing characters and spaces
    s = s.rstrip(",'\"")
    s = s.replace(" ", "")
    
    # Check for hemisphere suffix at the very end
    hemi = None
    if s and s[-1].upper() in ["N", "S", "E", "W"]:
        hemi = s[-1].upper()
        s = s[:-1].rstrip(",'\"")
        
    # Try simple float conversion first
    try:
        val_float = float(s)
        if hemi in ["S", "W"]:
            val_float = -val_float
        return val_float
    except ValueError:
        pass
        
    # Check for multiple dots format (e.g. DD.MMSS.S)
    if s.count(".") >= 2:
        parts = s.split(".")
        if len(parts) >= 3:
            try:
                deg = float(parts[0])
                mmss = parts[1]
                frac_sec = parts[2]
                if len(mmss) == 4 and mmss.isdigit():
                    min_val = float(mmss[:2])
                    sec_val = float(mmss[2:]) + float(f"0.{frac_sec}")
                    decimal = deg + (min_val / 60.0) + (sec_val / 3600.0)
                    if hemi in ["S", "W"]:
                        decimal = -decimal
                    return decimal
            except (ValueError, IndexError):
                pass

    # DMS / DDM parser using generalized pattern (degrees, non-digits, minutes, non-digits, optional seconds, optional hemisphere)
    pattern = r"^(\d+)\D+(\d+(?:\.\d+)?)(?:\D+(\d+(?:\.\d+)?))?\D*$"
    match = re.match(pattern, s)
    if match:
        try:
            deg = float(match.group(1))
            min_str = match.group(2)
            sec_str = match.group(3)
            
            if len(min_str) == 4 and min_str.isdigit():
                min_val = float(min_str[:2])
                sec_val = float(min_str[2:])
                if sec_str:
                    sec_val += float(f"0.{sec_str}")
            else:
                min_val = float(min_str)
                sec_val = float(sec_str) if sec_str else 0.0
                
            decimal = deg + (min_val / 60.0) + (sec_val / 3600.0)
            if hemi in ["S", "W"]:
                decimal = -decimal
            return decimal
        except ValueError:
            pass

    return None


def preprocess_charging_stations(
    csv_path: Path, 
    geojson_path: Path
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Execute the full preprocessing pipeline.

    Args:
        csv_path: Path to the input CSV file.
        geojson_path: Path to the input GeoJSON file.

    Returns:
        A tuple of (preprocessed DataFrame, summary statistics dictionary).
    """
    # 1. Load Datasets
    raw_df = load_csv(csv_path)
    geojson_data = load_geojson(geojson_path)
    
    total_raw_rows = len(raw_df)
    logger.info(f"Loaded {total_raw_rows} raw records.")
    
    # 2. Schema Validation
    validate_schema(raw_df, list(SCHEMA_MAP.keys()))
    
    # 3. Standardize Columns
    df = raw_df.rename(columns=SCHEMA_MAP)[list(SCHEMA_MAP.values())]
    
    # 4. Trim Whitespace and Normalize String Fields
    string_cols = ["station_name", "state", "district", "address", "owning_organisation"]
    for col in string_cols:
        df[col] = df[col].fillna("").astype(str).str.strip().str.replace(r"\s+", " ", regex=True)
        
    # 5. Parse and Validate Coordinates using robust parsing helper
    df["latitude"] = df["latitude"].apply(parse_coordinate)
    df["longitude"] = df["longitude"].apply(parse_coordinate)
    
    # Remove rows with null/NaN coordinates
    missing_coords_mask = df["latitude"].isna() | df["longitude"].isna()
    missing_coords_count = missing_coords_mask.sum()
    if missing_coords_count > 0:
        logger.warning(f"Removing {missing_coords_count} records due to missing or invalid numeric coordinates.")
    
    df_valid_coords = df[~missing_coords_mask].copy()
    
    # Check bounding box first for optimization, then Point-in-Polygon
    min_lon, max_lon, min_lat, max_lat = get_geojson_bounding_box(geojson_data)
    logger.info(f"Telangana Bounding Box: Longitude [{min_lon:.4f}, {max_lon:.4f}], Latitude [{min_lat:.4f}, {max_lat:.4f}]")
    
    pip_districts: List[Optional[str]] = []
    outside_count = 0
    
    for idx, row in df_valid_coords.iterrows():
        lat = row["latitude"]
        lon = row["longitude"]
        
        # Fast bounding box check
        if not (min_lon <= lon <= max_lon and min_lat <= lat <= max_lat):
            pip_districts.append(None)
            outside_count += 1
            continue
            
        # Detailed Point-in-Polygon check
        dist_name = get_district_for_point(lon, lat, geojson_data)
        if dist_name is None:
            outside_count += 1
        pip_districts.append(dist_name)
        
    df_valid_coords["pip_district"] = pip_districts
    
    # Keep track of records that fall outside Telangana boundaries
    outside_mask = df_valid_coords["pip_district"].isna()
    if outside_count > 0:
        logger.warning(f"Removing {outside_count} records with coordinates outside Telangana's district boundaries.")
        
    df_telangana = df_valid_coords[~outside_mask].copy()
    
    # Standardize district names and document mismatches
    original_districts = df_telangana["district"].tolist()
    standardized_districts = df_telangana["pip_district"].tolist()
    
    mismatches: List[Tuple[str, str, str]] = []
    for s_no, orig, std, name in zip(df_telangana["s_no"], original_districts, standardized_districts, df_telangana["station_name"]):
        if orig.strip().lower() != std.strip().lower():
            mismatches.append((str(s_no), name, f"'{orig}' -> '{std}'"))
            
    df_telangana["district"] = standardized_districts
    df_telangana = df_telangana.drop(columns=["pip_district"])
    
    # Standardize State name
    df_telangana["state"] = "Telangana"
    
    # 6. Remove Duplicate Stations
    # Define duplicates based on name/coordinates and name/address
    initial_clean_count = len(df_telangana)
    
    # Drop duplicates where name and coordinates are identical
    df_clean = df_telangana.drop_duplicates(subset=["station_name", "latitude", "longitude"], keep="first")
    dupes_removed_coords = initial_clean_count - len(df_clean)
    
    # Drop duplicates where name and address are identical
    final_clean_count_before_addr = len(df_clean)
    df_clean = df_clean.drop_duplicates(subset=["station_name", "address"], keep="first")
    dupes_removed_address = final_clean_count_before_addr - len(df_clean)
    
    total_duplicates_removed = dupes_removed_coords + dupes_removed_address
    logger.info(f"Removed {total_duplicates_removed} duplicate records (Coords: {dupes_removed_coords}, Address: {dupes_removed_address}).")
    
    # Reset serial numbers sequentially for the cleaned dataset
    df_clean = df_clean.copy()
    df_clean["s_no"] = range(1, len(df_clean) + 1)
    
    # 7. Compile Statistics
    stats: Dict[str, Any] = {
        "total_raw_records": total_raw_rows,
        "missing_coords_removed": int(missing_coords_count),
        "outside_telangana_removed": int(outside_count),
        "duplicates_removed": int(total_duplicates_removed),
        "final_clean_records": len(df_clean),
        "mismatches": mismatches,
        "district_distribution": df_clean["district"].value_counts().to_dict(),
        "owner_distribution": df_clean["owning_organisation"].value_counts().to_dict(),
        "lat_range": (float(df_clean["latitude"].min()), float(df_clean["latitude"].max())),
        "lon_range": (float(df_clean["longitude"].min()), float(df_clean["longitude"].max()))
    }
    
    return df_clean, stats


def generate_report(stats: Dict[str, Any], output_path: Path) -> None:
    """Generate a markdown report summarizing the cleaning process and results.

    Args:
        stats: Statistics compiled during preprocessing.
        output_path: Path where the report should be saved.
    """
    logger.info(f"Generating summary report at {output_path}")
    
    # Make parent directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    mismatches_content = ""
    if stats["mismatches"]:
        mismatches_content += "| S.No. | Station Name | District Mismatch |\n"
        mismatches_content += "|---|---|---|\n"
        for s_no, name, mismatch in stats["mismatches"][:50]:  # Show first 50
            mismatches_content += f"| {s_no} | {name} | {mismatch} |\n"
        if len(stats["mismatches"]) > 50:
            mismatches_content += f"| ... | and {len(stats['mismatches']) - 50} more mismatches | |\n"
    else:
        mismatches_content = "No district name mismatches identified."

    district_table = "| District | Cleaned Station Count |\n|---|---|\n"
    for dist, count in sorted(stats["district_distribution"].items(), key=lambda x: x[1], reverse=True):
        district_table += f"| {dist} | {count} |\n"

    owner_table = "| Owning Organisation / Person | Count |\n|---|---|\n"
    for owner, count in sorted(stats["owner_distribution"].items(), key=lambda x: x[1], reverse=True)[:20]:
        owner_table += f"| {owner} | {count} |\n"
    if len(stats["owner_distribution"]) > 20:
        owner_table += f"| ... | and {len(stats['owner_distribution']) - 20} more organizations |\n"

    report_md = f"""# EV Charging Stations Preprocessing Report

This report summarizes the data cleaning, schema validation, coordinate check, and spatial classification of charging stations for the EVision Telangana planning support system.

## 1. Executive Summary

- **Total Raw Records Loaded**: {stats["total_raw_records"]}
- **Records Removed due to Missing/Invalid Coordinates**: {stats["missing_coords_removed"]}
- **Records Removed due to Coordinates Outside Telangana Boundary**: {stats["outside_telangana_removed"]}
- **Duplicate Records Removed**: {stats["duplicates_removed"]}
- **Cleaned Records Retained**: {stats["final_clean_records"]}

## 2. Spatial and Coordinate Checks

Coordinates were validated spatially against Telangana's 33 districts boundaries defined in `telangana_33_districts.geojson`.
- **Bounding Box of Telangana**:
  - Latitude: [{stats["lat_range"][0]:.6f}, {stats["lat_range"][1]:.6f}]
  - Longitude: [{stats["lon_range"][0]:.6f}, {stats["lon_range"][1]:.6f}]

### District Name Typos & Spatial Mismatches Resolved ({len(stats["mismatches"])})

The following table lists samples of station district mismatches corrected by assigning standard district names from spatial polygons:

{mismatches_content}

## 3. District-Wise Station Distribution

The cleaned station distribution across Telangana's 33 standardized districts:

{district_table}

## 4. Owner Distribution (Top 20)

Cleaned stations breakdown by owning organization or person:

{owner_table}
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report_md)


def main() -> None:
    """Main execution function for the preprocessing script."""
    logger.info("Starting Charging Station Preprocessing pipeline.")
    
    try:
        df_clean, stats = preprocess_charging_stations(DEFAULT_CSV_PATH, DEFAULT_GEOJSON_PATH)
        
        # Create output directories if they do not exist
        DEFAULT_OUT_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
        
        # Save preprocessed dataset
        logger.info(f"Saving cleaned dataset to {DEFAULT_OUT_CSV_PATH}")
        df_clean.to_csv(DEFAULT_OUT_CSV_PATH, index=False)
        
        # Save summary report in report/ (singular)
        generate_report(stats, DEFAULT_REPORT_PATH)
        
        # Also copy report to reports/ (plural) if required
        reports_plural_path = WORKSPACE_DIR / "reports" / "charging_station_report.md"
        generate_report(stats, reports_plural_path)
        
        # Also copy to data/reports/ as allowed in write directories
        data_reports_path = WORKSPACE_DIR / "data" / "reports" / "charging_station_report.md"
        generate_report(stats, data_reports_path)
        
        logger.info("Charging Station Preprocessing pipeline completed successfully.")
        
    except Exception as e:
        logger.exception(f"Preprocessing pipeline failed: {e}")
        raise


if __name__ == "__main__":
    main()
