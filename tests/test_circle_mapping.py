import pytest
import pandas as pd
from pathlib import Path
from scripts.preprocessing.circle_mapping import (
    load_data,
    validate_mapping_data,
    map_circles_to_districts,
    write_unmapped_circles,
    write_mapping_report,
)


def test_validate_mapping_data_basic():
    # Setup mock dataframes
    consumption_df = pd.DataFrame(
        {
            "circle": [
                "HYDERABAD CENTRAL",
                "SECUNDERABAD",
                "ADILABAD",
                "HYDERABAD CENTRAL",
            ]
        }
    )
    mapping_df = pd.DataFrame(
        {
            "circle": ["HYDERABAD CENTRAL", "SECUNDERABAD", "ADILABAD"],
            "district": ["Hyderabad", "Hyderabad", "Adilabad"],
            "status": ["mapped", "mapped", "mapped"],
        }
    )

    report = validate_mapping_data(consumption_df, mapping_df)

    assert report["total_circles"] == 3
    assert report["mapped_circles"] == 3
    assert len(report["unmapped_circles"]) == 0
    assert len(report["duplicate_mappings"]) == 0
    assert report["mapping_coverage_pct"] == 100.0
    assert report["has_duplicates"] is False
    assert report["has_empty_districts"] is False
    assert report["has_missing_mappings"] is False


def test_validate_mapping_data_with_issues():
    # Setup mock dataframes with duplicate mapping, unmapped circles, empty districts
    consumption_df = pd.DataFrame(
        {
            "circle": [
                "HYDERABAD CENTRAL",
                "SECUNDERABAD",
                "ADILABAD",
                "UNKNOWN_CIRCLE",
            ]
        }
    )
    # 'SECUNDERABAD' is duplicated, 'ADILABAD' has empty district, 'UNKNOWN_CIRCLE' is missing from mapping
    mapping_df = pd.DataFrame(
        {
            "circle": ["HYDERABAD CENTRAL", "SECUNDERABAD", "SECUNDERABAD", "ADILABAD"],
            "district": ["Hyderabad", "Hyderabad", "Hyderabad", ""],
            "status": ["mapped", "mapped", "mapped", "mapped"],
        }
    )

    report = validate_mapping_data(consumption_df, mapping_df)

    assert report["total_circles"] == 4
    # Only HYDERABAD CENTRAL and SECUNDERABAD are successfully mapped to non-empty district
    assert report["mapped_circles"] == 2
    # UNKNOWN_CIRCLE and ADILABAD are unmapped
    assert set(report["unmapped_circles"]) == {"UNKNOWN_CIRCLE", "ADILABAD"}
    assert report["duplicate_mappings"] == ["SECUNDERABAD"]
    assert report["empty_district_circles"] == ["ADILABAD"]
    assert report["mapping_coverage_pct"] == 50.0
    assert report["has_duplicates"] is True
    assert report["has_empty_districts"] is True
    assert report["has_missing_mappings"] is True


def test_map_circles_to_districts():
    consumption_df = pd.DataFrame(
        {
            "circle": ["HYDERABAD CENTRAL", "SECUNDERABAD", "ADILABAD"],
            "value": [10, 20, 30],
        }
    )
    mapping_df = pd.DataFrame(
        {
            "circle": ["HYDERABAD CENTRAL", "SECUNDERABAD", "ADILABAD"],
            "district": ["Hyderabad", "Hyderabad", "Adilabad"],
            "status": ["mapped", "mapped", "mapped"],
        }
    )

    mapped_df = map_circles_to_districts(consumption_df, mapping_df)

    # Check column order: 'district' must be right after 'circle'
    columns = list(mapped_df.columns)
    assert columns[columns.index("circle") + 1] == "district"

    # Check values
    expected_districts = ["Hyderabad", "Hyderabad", "Adilabad"]
    assert list(mapped_df["district"]) == expected_districts


def test_write_unmapped_circles(tmp_path):
    output_file = tmp_path / "unmapped.csv"
    unmapped_circles = ["CIRCLE_A", "CIRCLE_B"]

    write_unmapped_circles(unmapped_circles, output_file)

    assert output_file.exists()
    df = pd.read_csv(output_file)
    assert list(df["circle"]) == unmapped_circles


def test_write_mapping_report(tmp_path):
    report_file = tmp_path / "report.md"
    report_data = {
        "total_circles": 5,
        "mapped_circles": 4,
        "unmapped_circles": ["CIRCLE_X"],
        "duplicate_mappings": ["CIRCLE_Y"],
        "empty_district_circles": ["CIRCLE_Z"],
        "mapping_coverage_pct": 80.0,
        "has_duplicates": True,
        "has_empty_districts": True,
        "has_missing_mappings": True,
    }

    write_mapping_report(report_data, report_file)

    assert report_file.exists()
    content = report_file.read_text(encoding="utf-8")
    assert "**Total Circles** | 5" in content
    assert "**Mapped Circles** | 4" in content
    assert "**Unmapped Circles** | 1" in content
    assert "**Duplicate Mappings** | 1" in content
    assert "**Mapping Coverage** | 80.00%" in content
    assert "CIRCLE_X" in content
    assert "CIRCLE_Y" in content
    assert "CIRCLE_Z" in content


def test_load_data_missing_files():
    with pytest.raises(FileNotFoundError):
        load_data(Path("does_not_exist_1.csv"), Path("does_not_exist_2.csv"))
