"""
Preprocess GeoJSON data.
Entry point script that loads the raw Telangana district geography dataset,
runs validation and calculations, and exports the cleaned datasets and report.
"""

import logging
import sys
from pathlib import Path

# Ensure project root is in the Python path for backend imports
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from backend.services.geography_processor import (
    validate_geojson,
    validate_geometry,
    standardize_district_names,
    calculate_centroids_and_area,
    export_data,
    generate_markdown_report,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(project_root / "geography_preprocessing.log", encoding="utf-8"),
    ]
)
logger = logging.getLogger("preprocess_geojson")


def main() -> None:
    """
    Main execution pipeline for Geography Dataset Preprocessing.
    """
    logger.info("Starting Geography Preprocessing Pipeline...")
    
    # 1. Define paths using pathlib
    input_path = project_root / "data" / "raw" / "geography" / "telangana_33_districts.geojson"
    output_geojson_path = project_root / "data" / "interim" / "geography" / "district_boundaries.geojson"
    output_csv_path = project_root / "data" / "interim" / "geography" / "district_geography.csv"
    report_path = project_root / "reports" / "geography_report.md"
    
    try:
        # 2. Validate GeoJSON structure
        gdf = validate_geojson(input_path)
        
        # 3. Validate & repair geometries, perform coordinate boundary checks
        gdf = validate_geometry(gdf)
        
        # 4. Standardize district names
        gdf = standardize_district_names(gdf)
        
        # 5. Generate centroids and calculate area
        gdf = calculate_centroids_and_area(gdf)
        
        # 6. Export results
        export_data(gdf, output_geojson_path, output_csv_path)
        
        # 7. Generate report
        generate_markdown_report(gdf, report_path)
        
        logger.info("Geography Preprocessing Pipeline completed successfully.")
        
    except Exception as e:
        logger.exception("An error occurred during geography preprocessing:")
        sys.exit(1)


if __name__ == "__main__":
    main()
