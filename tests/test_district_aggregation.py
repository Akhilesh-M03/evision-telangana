import pytest
import pandas as pd
import math
from pathlib import Path
from scripts.preprocessing.district_aggregation import (
    load_data,
    aggregate_consumption,
    validate_aggregation,
    generate_report,
)


def test_aggregate_consumption():
    # Setup mock dataframe representing circle_mapped.csv
    mock_df = pd.DataFrame(
        {
            "district": ["ADILABAD", "ADILABAD", "ADILABAD", "NIZAMABAD"],
            "year": [2023, 2023, 2023, 2023],
            "month": [1, 1, 1, 1],
            "reporting_month": ["2023-01", "2023-01", "2023-01", "2023-01"],
            "circle": ["Circle A", "Circle A", "Circle B", "Circle C"],
            "division": ["Div A1", "Div A1", "Div B1", "Div C1"],
            "subdivision": ["Sub A1", "Sub A2", "Sub B1", "Sub C1"],
            "units": [100.0, 150.0, 200.0, 300.0],
            "load": [50.0, 75.0, 100.0, 150.0],
            "total_services": [10, 15, 20, 30],
            "billed_services": [8.0, 12.0, 18.0, 25.0],
            "source": ["TG-NPDCL", "TG-NPDCL", "TG-NPDCL", "TG-NPDCL"],
            "section": ["Sec A", "Sec B", "Sec C", "Sec D"],
            "area": ["Area A", "Area B", "Area C", "Area D"],
            "category": ["LT-I", "LT-I", "LT-I", "LT-I"],
        }
    )

    agg_df = aggregate_consumption(mock_df)

    assert len(agg_df) == 2

    # Check ADILABAD aggregation
    adil_row = agg_df[agg_df["district"] == "ADILABAD"].iloc[0]
    assert adil_row["units"] == 450.0
    assert adil_row["load"] == 225.0
    assert adil_row["total_services"] == 45
    assert adil_row["billed_services"] == 38.0
    # 2 unique circles: "Circle A", "Circle B"
    assert adil_row["circle_count"] == 2
    # 2 unique divisions: "Div A1", "Div B1"
    assert adil_row["division_count"] == 2
    # 3 unique subdivisions: "Sub A1", "Sub A2", "Sub B1"
    assert adil_row["subdivision_count"] == 3

    # Check NIZAMABAD aggregation
    niz_row = agg_df[agg_df["district"] == "NIZAMABAD"].iloc[0]
    assert niz_row["units"] == 300.0
    assert niz_row["load"] == 150.0
    assert niz_row["total_services"] == 30
    assert niz_row["billed_services"] == 25.0
    assert niz_row["circle_count"] == 1
    assert niz_row["division_count"] == 1
    assert niz_row["subdivision_count"] == 1


def test_validate_aggregation_success():
    orig_df = pd.DataFrame(
        {
            "units": [10.0, 20.0],
            "load": [5.0, 5.0],
            "total_services": [1, 2],
            "billed_services": [1.0, 2.0],
        }
    )
    agg_df = pd.DataFrame(
        {
            "units": [30.0],
            "load": [10.0],
            "total_services": [3],
            "billed_services": [3.0],
        }
    )

    is_valid, results = validate_aggregation(orig_df, agg_df)
    assert is_valid is True
    assert results["units"]["status"] == "PASSED"
    assert results["load"]["status"] == "PASSED"
    assert results["total_services"]["status"] == "PASSED"
    assert results["billed_services"]["status"] == "PASSED"


def test_validate_aggregation_failure():
    orig_df = pd.DataFrame(
        {
            "units": [10.0, 20.0],
            "load": [5.0, 5.0],
            "total_services": [1, 2],
            "billed_services": [1.0, 2.0],
        }
    )
    # Mismatch in units
    agg_df = pd.DataFrame(
        {
            "units": [35.0],
            "load": [10.0],
            "total_services": [3],
            "billed_services": [3.0],
        }
    )

    is_valid, results = validate_aggregation(orig_df, agg_df)
    assert is_valid is False
    assert results["units"]["status"] == "FAILED"
    assert results["load"]["status"] == "PASSED"


def test_generate_report(tmp_path):
    orig_df = pd.DataFrame(
        {
            "district": ["A", "B"],
            "year": [2023, 2023],
            "month": [1, 1],
            "reporting_month": ["2023-01", "2023-01"],
            "units": [10.0, 20.0],
            "load": [5.0, 5.0],
            "total_services": [1, 2],
            "billed_services": [1.0, 2.0],
        }
    )
    agg_df = pd.DataFrame(
        {
            "district": ["A", "B"],
            "year": [2023, 2023],
            "month": [1, 1],
            "reporting_month": ["2023-01", "2023-01"],
            "units": [10.0, 20.0],
            "load": [5.0, 5.0],
            "total_services": [1, 2],
            "billed_services": [1.0, 2.0],
        }
    )
    is_valid, results = validate_aggregation(orig_df, agg_df)
    report_file = tmp_path / "district_aggregation_report.md"

    generate_report(report_file, orig_df, agg_df, results, is_valid)

    assert report_file.exists()
    content = report_file.read_text(encoding="utf-8")
    assert "# District Aggregation Report" in content
    assert "## Processing Summary" in content
    assert "## Validation Results" in content
    assert "PASSED" in content


def test_load_data_missing_file():
    with pytest.raises(FileNotFoundError):
        load_data(Path("non_existent_file_path_123.csv"))
