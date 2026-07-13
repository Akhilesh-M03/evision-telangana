import pytest
import pandas as pd
from scripts.preprocess_charging_stations import (
    is_point_in_polygon,
    validate_schema,
    SCHEMA_MAP
)

def test_is_point_in_polygon():
    # Define a simple square polygon (exterior ring only, clockwise or counterclockwise)
    # Longitude from 0 to 10, Latitude from 0 to 10
    polygon = [
        [[0.0, 0.0], [10.0, 0.0], [10.0, 10.0], [0.0, 10.0], [0.0, 0.0]]
    ]
    
    # Point inside
    assert is_point_in_polygon(5.0, 5.0, polygon) is True
    
    # Point outside
    assert is_point_in_polygon(12.0, 5.0, polygon) is False
    assert is_point_in_polygon(5.0, -1.0, polygon) is False


def test_is_point_in_polygon_with_hole():
    # Square from 0 to 10, with a hole from 4 to 6
    polygon = [
        [[0.0, 0.0], [10.0, 0.0], [10.0, 10.0], [0.0, 10.0], [0.0, 0.0]],  # Exterior
        [[4.0, 4.0], [4.0, 6.0], [6.0, 6.0], [6.0, 4.0], [4.0, 4.0]]       # Interior Hole
    ]
    
    # Point inside the solid area
    assert is_point_in_polygon(2.0, 2.0, polygon) is True
    
    # Point inside the hole (should return False)
    assert is_point_in_polygon(5.0, 5.0, polygon) is False


def test_validate_schema_success():
    df = pd.DataFrame(columns=list(SCHEMA_MAP.keys()))
    # Should not raise exception
    validate_schema(df, list(SCHEMA_MAP.keys()))


def test_validate_schema_failure():
    df = pd.DataFrame(columns=["S.No.", "State"])
    with pytest.raises(ValueError) as excinfo:
        validate_schema(df, list(SCHEMA_MAP.keys()))
    assert "Missing expected columns in CSV" in str(excinfo.value)
