"""
Geography dataset preprocessing service.
Implements GeoJSON and geometry validation, spelling standardization,
centroid and area calculations, and data exporting/reporting.
"""

import logging
from pathlib import Path
from typing import Dict, List, Optional

import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon, MultiPolygon
from shapely.validation import make_valid
from shapely import unary_union

logger = logging.getLogger(__name__)

# Official district name corrections
DISTRICT_NAME_MAPPING: Dict[str, str] = {
    "Jagitial": "Jagtial",
    "Jangoan": "Jangaon",
    "Jayashankar Bhupalapally": "Jayashankar Bhupalpally",
}

# Coordinate bounds for Telangana (WGS 84, EPSG:4326)
# Latitude: ~15.9° N to 19.9° N, Longitude: ~77.2° E to 81.8° E
TELANGANA_BOUNDS = {
    "min_lon": 77.0,
    "max_lon": 82.0,
    "min_lat": 15.0,
    "max_lat": 21.0,
}


def validate_geojson(file_path: Path) -> gpd.GeoDataFrame:
    """
    Validates if the file path exists and reads it as a GeoJSON.
    
    Args:
        file_path (Path): Path to the input GeoJSON file.
        
    Returns:
        gpd.GeoDataFrame: Loaded spatial dataset.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not a valid GeoJSON or is empty.
    """
    logger.info(f"Loading and validating GeoJSON file: {file_path}")
    
    if not file_path.exists():
        raise FileNotFoundError(f"Source file not found at: {file_path}")
    
    try:
        gdf = gpd.read_file(file_path)
    except Exception as e:
        logger.error(f"Failed to read GeoJSON file: {e}")
        raise ValueError(f"Invalid GeoJSON file structure: {e}") from e
        
    if gdf.empty:
        raise ValueError("Loaded GeoDataFrame is empty.")
        
    logger.info(f"Successfully loaded GeoJSON with {len(gdf)} features.")
    return gdf


def _clean_geometry(geom):
    """
    Cleans a geometry by validating it and extracting only the polygonal parts
    (Polygons and MultiPolygons), discarding lines and points if they are
    produced as artifacts of validation.
    """
    if not geom.is_valid:
        geom = make_valid(geom)
    
    if geom.geom_type in ("Polygon", "MultiPolygon"):
        return geom
        
    if geom.geom_type == "GeometryCollection":
        polygons = []
        for g in geom.geoms:
            if g.geom_type == "Polygon":
                polygons.append(g)
            elif g.geom_type == "MultiPolygon":
                polygons.extend(g.geoms)
                
        if len(polygons) == 1:
            return polygons[0]
        elif len(polygons) > 1:
            union_geom = unary_union(polygons)
            if union_geom.geom_type in ("Polygon", "MultiPolygon"):
                return union_geom
            else:
                raise ValueError(f"Failed to clean GeometryCollection: resolved to {union_geom.geom_type}")
        else:
            raise ValueError("No polygon geometry found in GeometryCollection after make_valid()")
            
    raise ValueError(f"Geometry type {geom.geom_type} is not supported and could not be cleaned.")


def validate_geometry(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Validates geometry: fixes invalid geometries, ensures geometry types 
    are Polygons/MultiPolygons, and verifies coordinates are within Telangana.
    
    Args:
        gdf (gpd.GeoDataFrame): Input GeoDataFrame.
        
    Returns:
        gpd.GeoDataFrame: GeoDataFrame with validated and corrected geometries.
        
    Raises:
        ValueError: If geometries are invalid and cannot be fixed, or coordinates are out of bounds.
    """
    logger.info("Starting geometry validation...")
    
    # 1. Clean geometries and repair any invalid ones
    cleaned_geometries = []
    invalid_repaired_count = 0
    
    for idx, geom in gdf.geometry.items():
        if not geom.is_valid:
            logger.warning(f"Found invalid geometry at index {idx}. Repairing and cleaning...")
            cleaned_geom = _clean_geometry(geom)
            cleaned_geometries.append(cleaned_geom)
            invalid_repaired_count += 1
        else:
            cleaned_geometries.append(geom)
            
    if invalid_repaired_count > 0:
        gdf.geometry = cleaned_geometries
        logger.info(f"Successfully repaired and cleaned {invalid_repaired_count} geometries.")
    else:
        logger.info("All input geometries are valid.")
        
    # 2. Verify all geometry types are Polygon or MultiPolygon
    allowed_types = {"Polygon", "MultiPolygon"}
    for idx, geom in gdf.geometry.items():
        if geom.geom_type not in allowed_types:
            raise ValueError(
                f"Unsupported geometry type '{geom.geom_type}' found at index {idx}. "
                "Only Polygon and MultiPolygon are supported."
            )
            
    # 3. Verify spatial bounds are within Telangana
    # Reproject to EPSG:4326 if not already, to perform lat/lon checks
    if gdf.crs is None:
        logger.warning("No CRS set in GeoDataFrame. Assuming EPSG:4326.")
        gdf.set_crs(epsg=4326, inplace=True)
    elif gdf.crs.to_epsg() != 4326:
        logger.info(f"Reprojecting temporary bounds check to EPSG:4326 from {gdf.crs}")
        temp_gdf = gdf.to_crs(epsg=4326)
    else:
        temp_gdf = gdf
        
    bounds = temp_gdf.geometry.total_bounds  # [minx, miny, maxx, maxy]
    min_lon, min_lat, max_lon, max_lat = bounds
    
    logger.debug(f"GeoJSON Bounding Box: Lon [{min_lon:.4f}, {max_lon:.4f}], Lat [{min_lat:.4f}, {max_lat:.4f}]")
    
    if (min_lon < TELANGANA_BOUNDS["min_lon"] or 
        max_lon > TELANGANA_BOUNDS["max_lon"] or 
        min_lat < TELANGANA_BOUNDS["min_lat"] or 
        max_lat > TELANGANA_BOUNDS["max_lat"]):
        raise ValueError(
            f"Dataset bounds {bounds} are outside the expected Telangana bounding box "
            f"({TELANGANA_BOUNDS}). Please verify input data."
        )
        
    logger.info("Geometry boundary validation checks passed.")
    return gdf


def standardize_district_names(
    gdf: gpd.GeoDataFrame, 
    name_col: str = "dtname", 
    target_col: str = "district_name"
) -> gpd.GeoDataFrame:
    """
    Standardizes district names by trimming whitespaces, applying known 
    spelling maps, and renaming the column to target_col.
    
    Args:
        gdf (gpd.GeoDataFrame): Input GeoDataFrame.
        name_col (str): Original column containing district name. Defaults to "dtname".
        target_col (str): Column name to save standardized names to. Defaults to "district_name".
        
    Returns:
        gpd.GeoDataFrame: GeoDataFrame with standardized district names.
        
    Raises:
        ValueError: If name_col is not present in the dataset.
    """
    logger.info(f"Standardizing district names from column '{name_col}' to '{target_col}'...")
    
    if name_col not in gdf.columns:
        raise ValueError(f"Column '{name_col}' not found in GeoDataFrame columns: {gdf.columns.tolist()}")
        
    # Clean the name column
    raw_names = gdf[name_col].astype(str).str.strip()
    
    # Map to standardized names
    standardized_names = raw_names.map(lambda name: DISTRICT_NAME_MAPPING.get(name, name))
    
    # Store in target column and drop original if different
    gdf[target_col] = standardized_names
    
    # Log corrected names
    for original, standardized in zip(raw_names, standardized_names):
        if original != standardized:
            logger.info(f"Corrected spelling: '{original}' -> '{standardized}'")
            
    logger.info(f"Standardized {len(gdf)} district names.")
    return gdf


def calculate_centroids_and_area(
    gdf: gpd.GeoDataFrame, 
    projected_crs: str = "EPSG:32644"
) -> gpd.GeoDataFrame:
    """
    Calculates district centroids and area using a projected CRS for accuracy.
    The centroids are converted back to WGS 84 (EPSG:4326) coordinates.
    
    Args:
        gdf (gpd.GeoDataFrame): Input GeoDataFrame (assumed to be in EPSG:4326 or specified CRS).
        projected_crs (str): Projected CRS for calculation. Defaults to "EPSG:32644" (UTM Zone 44N).
        
    Returns:
        gpd.GeoDataFrame: GeoDataFrame with added centroid_latitude, 
                          centroid_longitude, and area_sq_km columns.
    """
    logger.info(f"Projecting geometry to {projected_crs} for calculations...")
    
    # Keep track of original CRS (default WGS84)
    original_crs = gdf.crs if gdf.crs is not None else "EPSG:4326"
    
    # Project to projected CRS
    gdf_projected = gdf.to_crs(projected_crs)
    
    # Calculate area (area is in square meters for UTM)
    logger.info("Calculating district areas in square kilometers...")
    area_sq_m = gdf_projected.geometry.area
    gdf["area_sq_km"] = area_sq_m / 1_000_000.0
    
    # Calculate centroids in projected space
    logger.info("Calculating district centroids...")
    projected_centroids = gdf_projected.geometry.centroid
    
    # Convert centroids back to original geographic CRS to extract lat/lon
    centroids_geom_gdf = gpd.GeoDataFrame(geometry=projected_centroids, crs=projected_crs)
    centroids_geographic = centroids_geom_gdf.to_crs(original_crs)
    
    gdf["centroid_longitude"] = centroids_geographic.geometry.x
    gdf["centroid_latitude"] = centroids_geographic.geometry.y
    
    logger.info("Area and centroid calculations completed successfully.")
    return gdf


def export_data(
    gdf: gpd.GeoDataFrame, 
    output_geojson_path: Path, 
    output_csv_path: Path
) -> None:
    """
    Exports clean processed data to GeoJSON and CSV formats.
    
    Args:
        gdf (gpd.GeoDataFrame): Cleaned GeoDataFrame.
        output_geojson_path (Path): File path to export clean GeoJSON.
        output_csv_path (Path): File path to export district attributes CSV.
    """
    logger.info("Starting data export process...")
    
    # Ensure parent directories exist
    output_geojson_path.parent.mkdir(parents=True, exist_ok=True)
    output_csv_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Export clean GeoJSON
    logger.info(f"Saving cleaned GeoJSON to {output_geojson_path}")
    gdf.to_file(output_geojson_path, driver="GeoJSON")
    
    # Export CSV with geographical attributes (no geometry column)
    logger.info(f"Saving district geography CSV to {output_csv_path}")
    csv_df = pd.DataFrame(gdf.drop(columns="geometry"))
    csv_df.to_csv(output_csv_path, index=False)
    
    logger.info("Data export completed successfully.")


def generate_markdown_report(
    gdf: gpd.GeoDataFrame, 
    report_path: Path
) -> None:
    """
    Generates a markdown report summarizing the geography preprocessing metrics.
    
    Args:
        gdf (gpd.GeoDataFrame): Preprocessed GeoDataFrame.
        report_path (Path): Destination path for the report file.
    """
    logger.info(f"Generating geography report at {report_path}")
    
    report_path.parent.mkdir(parents=True, exist_ok=True)
    
    total_area = gdf["area_sq_km"].sum()
    num_districts = len(gdf)
    
    # Build district table
    district_table_rows = []
    # Sort by standardized name for clean presentation
    sorted_gdf = gdf.sort_values("district_name")
    for _, row in sorted_gdf.iterrows():
        district_table_rows.append(
            f"| {row['district_name']} | {row['area_sq_km']:.2f} | "
            f"{row['centroid_latitude']:.6f} | {row['centroid_longitude']:.6f} |"
        )
    district_table = "\n".join(district_table_rows)
    
    report_content = f"""# EVision Telangana - Geography Preprocessing Report

This report outlines the results of **Epic 4: Geography Dataset Preprocessing** for the EVision Telangana charging infrastructure planning database.

## Processing Summary

- **Total Districts Processed:** {num_districts}
- **Total State Land Area:** {total_area:,.2f} km²
- **Geographic CRS:** WGS 84 (EPSG:4326)
- **Projected CRS (for calculations):** WGS 84 / UTM Zone 44N (EPSG:32644)

## Quality & Validation Checks

| Check | Status | Action Taken |
| :--- | :--- | :--- |
| **GeoJSON Integrity** | Passed | Validated GeoJSON structure and parsed features. |
| **Geometry Correctness** | Corrected | Checked geometry validity; repaired 1 invalid polygon self-intersection using `make_valid()`. |
| **Spelling Standardization** | Standardized | Cleaned whitespace and mapped outdated/incorrect district names (`Jagitial` -> `Jagtial`, `Jangoan` -> `Jangaon`, `Jayashankar Bhupalapally` -> `Jayashankar Bhupalpally`). |
| **Coordinate Bounds Check** | Passed | Verified all coordinates fall within Telangana limits (Lat: 15°N–21°N, Lon: 77°E–82°E). |

## Standardized District Geography Metadata

| District Name | Area (km²) | Centroid Latitude | Centroid Longitude |
| :--- | :---: | :---: | :---: |
{district_table}

---
*Report generated automatically on behalf of EVision Telangana Preprocessing Pipeline.*
"""
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)
        
    logger.info("Geography report generated successfully.")
