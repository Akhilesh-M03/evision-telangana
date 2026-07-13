"""
Unit tests for the geography dataset preprocessing service.
"""

import sys
from pathlib import Path
import pytest
import geopandas as gpd
from shapely.geometry import Polygon, Point, MultiPolygon
import pandas as pd

# Add project root to python path for backend imports
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


@pytest.fixture
def sample_valid_gdf() -> gpd.GeoDataFrame:
    """
    Creates a sample GeoDataFrame containing a valid polygon inside Telangana bounds.
    """
    # Telangana bounding box is Lon: 77 to 82, Lat: 15 to 21
    # Let's create a district polygon around Hyderabad/Secunderabad area (roughly Lon 78.4, Lat 17.4)
    poly = Polygon([
        (78.3, 17.3),
        (78.5, 17.3),
        (78.5, 17.5),
        (78.3, 17.5),
        (78.3, 17.3)
    ])
    gdf = gpd.GeoDataFrame(
        {"dtname": ["Hyderabad"], "stname": ["TELANGANA"]},
        geometry=[poly],
        crs="EPSG:4326"
    )
    return gdf


@pytest.fixture
def sample_invalid_geometry_gdf() -> gpd.GeoDataFrame:
    """
    Creates a GeoDataFrame containing a self-intersecting (invalid) polygon.
    """
    # Self-intersecting polygon (hourglass shape)
    poly = Polygon([(78.3, 17.3), (78.5, 17.5), (78.3, 17.5), (78.5, 17.3), (78.3, 17.3)])
    gdf = gpd.GeoDataFrame(
        {"dtname": ["Jagitial"]},
        geometry=[poly],
        crs="EPSG:4326"
    )
    return gdf


def test_validate_geojson_missing_file():
    """
    Test that validate_geojson raises FileNotFoundError for missing paths.
    """
    with pytest.raises(FileNotFoundError):
        validate_geojson(Path("non_existent_file.geojson"))


def test_validate_geometry_valid(sample_valid_gdf):
    """
    Test that validate_geometry passes for a valid GeoDataFrame.
    """
    validated_gdf = validate_geometry(sample_valid_gdf)
    assert validated_gdf is not None
    assert len(validated_gdf) == 1
    assert validated_gdf.iloc[0]["dtname"] == "Hyderabad"


def test_validate_geometry_invalid_fixed(sample_invalid_geometry_gdf):
    """
    Test that validate_geometry repairs invalid self-intersecting geometries.
    """
    # Check that input is indeed invalid originally
    assert not sample_invalid_geometry_gdf.geometry.iloc[0].is_valid
    
    # Run through validation (should repair it)
    validated_gdf = validate_geometry(sample_invalid_geometry_gdf)
    assert validated_gdf.geometry.iloc[0].is_valid


def test_validate_geometry_unsupported_type():
    """
    Test that validate_geometry raises ValueError for unsupported geometry types (e.g. Point).
    """
    point_gdf = gpd.GeoDataFrame(
        {"dtname": ["PointDistrict"]},
        geometry=[Point(78.4, 17.4)],
        crs="EPSG:4326"
    )
    with pytest.raises(ValueError, match="Unsupported geometry type"):
        validate_geometry(point_gdf)


def test_validate_geometry_out_of_bounds(sample_valid_gdf):
    """
    Test that validate_geometry raises ValueError for coordinates outside Telangana.
    """
    # Polygon in USA (outside Telangana)
    usa_poly = Polygon([(-100.0, 40.0), (-99.0, 40.0), (-99.0, 41.0), (-100.0, 41.0), (-100.0, 40.0)])
    out_of_bounds_gdf = gpd.GeoDataFrame(
        {"dtname": ["OutDistrict"]},
        geometry=[usa_poly],
        crs="EPSG:4326"
    )
    with pytest.raises(ValueError, match="outside the expected Telangana bounding box"):
        validate_geometry(out_of_bounds_gdf)


def test_standardize_district_names(sample_valid_gdf):
    """
    Test name standardization dictionary and whitespace trimming.
    """
    # Test specific spelling mapping
    gdf = gpd.GeoDataFrame(
        {"dtname": [" Jagitial ", "Jangoan", "Jayashankar Bhupalapally"]},
        geometry=[sample_valid_gdf.geometry.iloc[0]] * 3,
        crs="EPSG:4326"
    )
    standardized = standardize_district_names(gdf)
    
    # Assert renamed column exist
    assert "district_name" in standardized.columns
    # Assert values mapped correctly and trimmed
    assert standardized.iloc[0]["district_name"] == "Jagtial"
    assert standardized.iloc[1]["district_name"] == "Jangaon"
    assert standardized.iloc[2]["district_name"] == "Jayashankar Bhupalpally"


def test_standardize_district_names_missing_column(sample_valid_gdf):
    """
    Test that standardize_district_names raises ValueError if original name column is missing.
    """
    gdf = sample_valid_gdf.drop(columns="dtname")
    with pytest.raises(ValueError, match="Column 'dtname' not found"):
        standardize_district_names(gdf, name_col="dtname")


def test_calculate_centroids_and_area(sample_valid_gdf):
    """
    Test area and centroid calculation functionality.
    """
    res = calculate_centroids_and_area(sample_valid_gdf)
    
    assert "area_sq_km" in res.columns
    assert "centroid_latitude" in res.columns
    assert "centroid_longitude" in res.columns
    
    # Hyd bounds: Lon 78.3 to 78.5, Lat 17.3 to 17.5. Centroid should be around 78.4, 17.4
    assert pytest.approx(res.iloc[0]["centroid_longitude"], abs=0.01) == 78.4
    assert pytest.approx(res.iloc[0]["centroid_latitude"], abs=0.01) == 17.4
    # Area of ~0.2 x ~0.2 degrees at 17 deg latitude is around 480-490 sq km
    assert res.iloc[0]["area_sq_km"] > 0
    assert res.iloc[0]["area_sq_km"] < 1000


def test_export_data_and_report(sample_valid_gdf, tmp_path):
    """
    Test exporting GeoJSON, CSV, and markdown reports.
    """
    # Preprocess
    gdf = validate_geometry(sample_valid_gdf)
    gdf = standardize_district_names(gdf)
    gdf = calculate_centroids_and_area(gdf)
    
    out_geojson = tmp_path / "district_boundaries.geojson"
    out_csv = tmp_path / "district_geography.csv"
    out_report = tmp_path / "geography_report.md"
    
    # Export files
    export_data(gdf, out_geojson, out_csv)
    generate_markdown_report(gdf, out_report)
    
    # Assert files exist
    assert out_geojson.exists()
    assert out_csv.exists()
    assert out_report.exists()
    
    # Load back and verify values
    loaded_csv = pd.read_csv(out_csv)
    assert len(loaded_csv) == 1
    assert loaded_csv.iloc[0]["district_name"] == "Hyderabad"
    assert loaded_csv.iloc[0]["area_sq_km"] > 0
    assert loaded_csv.iloc[0]["centroid_longitude"] == gdf.iloc[0]["centroid_longitude"]
    
    # Verify report content
    with open(out_report, "r", encoding="utf-8") as f:
        content = f.read()
        assert "EVision Telangana - Geography Preprocessing Report" in content
        assert "Hyderabad" in content
