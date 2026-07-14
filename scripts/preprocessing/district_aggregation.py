"""
District Aggregation module for EVision Telangana electricity consumption dataset.

This script aggregates electricity consumption data from the circle level to the
district level, performs validations to ensure data integrity (comparing original
and aggregated totals), and writes a detailed execution report.
"""

import argparse
import logging
import math
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

# Setup logger
logger = logging.getLogger("district_aggregation")


def setup_logging(log_file: Optional[Path] = None) -> None:
    """
    Configure the logging system.

    Args:
        log_file: Optional path to save logs.
    """
    handlers: List[logging.Handler] = [logging.StreamHandler()]
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(log_file, mode="w", encoding="utf-8"))

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=handlers,
    )


def load_data(input_path: Path) -> pd.DataFrame:
    """
    Load circle-mapped consumption dataset.

    Args:
        input_path: Path to circle_mapped.csv file.

    Returns:
        DataFrame containing mapped consumption data.

    Raises:
        FileNotFoundError: If the input file does not exist.
    """
    if not input_path.exists():
        logger.error(f"Input file not found at: {input_path}")
        raise FileNotFoundError(f"Input file not found at: {input_path}")

    logger.info(f"Loading circle-mapped data from: {input_path}")
    df = pd.read_csv(input_path)
    return df


def aggregate_consumption(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate consumption data from circle level to district level.

    Group by:
      - district
      - year
      - month
      - reporting_month

    Aggregate:
      - units -> sum
      - load -> sum
      - total_services -> sum
      - billed_services -> sum

    Compute unique counts:
      - circle_count (number of unique circles)
      - division_count (number of unique divisions)
      - subdivision_count (number of unique subdivisions)

    Args:
        df: Input DataFrame with circle level data.

    Returns:
        Aggregated district-level monthly consumption DataFrame.
    """
    logger.info("Aggregating consumption data from circle level to district level...")
    agg_df = (
        df.groupby(["district", "year", "month", "reporting_month"], as_index=False)
        .agg(
            units=("units", "sum"),
            load=("load", "sum"),
            total_services=("total_services", "sum"),
            billed_services=("billed_services", "sum"),
            circle_count=("circle", "nunique"),
            division_count=("division", "nunique"),
            subdivision_count=("subdivision", "nunique"),
        )
    )

    # Sort output for consistency
    agg_df = agg_df.sort_values(
        by=["district", "year", "month", "reporting_month"]
    ).reset_index(drop=True)

    return agg_df


def validate_aggregation(
    original_df: pd.DataFrame, aggregated_df: pd.DataFrame
) -> Tuple[bool, Dict[str, Any]]:
    """
    Validate that aggregated totals match the original totals.

    Checks:
      1. Aggregated total units == original total units
      2. Aggregated total load == original total load
      3. Aggregated total_services == original total_services
      4. Aggregated billed_services == original billed_services

    Args:
        original_df: Original circle-level DataFrame.
        aggregated_df: Aggregated district-level DataFrame.

    Returns:
        Tuple of (is_valid, validation_results)
    """
    logger.info("Validating aggregated totals against original totals...")
    
    # Original sums (handling NaN values properly using skipna=True, which is default)
    orig_units = float(original_df["units"].sum())
    orig_load = float(original_df["load"].sum())
    orig_total_services = int(original_df["total_services"].sum())
    orig_billed_services = float(original_df["billed_services"].sum())

    # Aggregated sums
    agg_units = float(aggregated_df["units"].sum())
    agg_load = float(aggregated_df["load"].sum())
    agg_total_services = int(aggregated_df["total_services"].sum())
    agg_billed_services = float(aggregated_df["billed_services"].sum())

    # Tolerant float matching (rel_tol=1e-7 or absolute tolerance of 1e-3 for roundings)
    units_match = math.isclose(orig_units, agg_units, rel_tol=1e-7, abs_tol=1e-3)
    load_match = math.isclose(orig_load, agg_load, rel_tol=1e-7, abs_tol=1e-3)
    total_services_match = (orig_total_services == agg_total_services)
    billed_services_match = math.isclose(orig_billed_services, agg_billed_services, rel_tol=1e-7, abs_tol=1e-3)

    is_valid = units_match and load_match and total_services_match and billed_services_match

    results = {
        "units": {
            "original": orig_units,
            "aggregated": agg_units,
            "difference": orig_units - agg_units,
            "status": "PASSED" if units_match else "FAILED",
        },
        "load": {
            "original": orig_load,
            "aggregated": agg_load,
            "difference": orig_load - agg_load,
            "status": "PASSED" if load_match else "FAILED",
        },
        "total_services": {
            "original": orig_total_services,
            "aggregated": agg_total_services,
            "difference": orig_total_services - agg_total_services,
            "status": "PASSED" if total_services_match else "FAILED",
        },
        "billed_services": {
            "original": orig_billed_services,
            "aggregated": agg_billed_services,
            "difference": orig_billed_services - agg_billed_services,
            "status": "PASSED" if billed_services_match else "FAILED",
        },
    }

    return is_valid, results


def generate_report(
    report_path: Path,
    original_df: pd.DataFrame,
    aggregated_df: pd.DataFrame,
    validation_results: Dict[str, Any],
    is_valid: bool,
) -> None:
    """
    Generate markdown report for district aggregation.

    Args:
        report_path: Target path to write markdown report.
        original_df: Original DataFrame.
        aggregated_df: Aggregated DataFrame.
        validation_results: Results dictionary from validate_aggregation.
        is_valid: Boolean indicating whether validation passed.
    """
    report_path.parent.mkdir(parents=True, exist_ok=True)

    num_districts = int(aggregated_df["district"].nunique())
    num_reporting_months = int(aggregated_df["reporting_month"].nunique())
    total_agg_rows = len(aggregated_df)

    content = f"""# District Aggregation Report

This report summarizes the results and validations of the district-level aggregation of electricity consumption.

## Processing Summary

- **Number of Districts**: {num_districts}
- **Number of Reporting Months**: {num_reporting_months}
- **Total Aggregated Rows**: {total_agg_rows}
- **Original Rows**: {len(original_df)}
- **Status**: {"SUCCESS" if is_valid else "FAILED"}

## Validation Results

| Metric | Original Sum | Aggregated Sum | Difference | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Units (kWh)** | {validation_results['units']['original']:.4f} | {validation_results['units']['aggregated']:.4f} | {validation_results['units']['difference']:.4f} | {validation_results['units']['status']} |
| **Load (kW)** | {validation_results['load']['original']:.4f} | {validation_results['load']['aggregated']:.4f} | {validation_results['load']['difference']:.4f} | {validation_results['load']['status']} |
| **Total Services** | {validation_results['total_services']['original']} | {validation_results['total_services']['aggregated']} | {validation_results['total_services']['difference']} | {validation_results['total_services']['status']} |
| **Billed Services** | {validation_results['billed_services']['original']:.4f} | {validation_results['billed_services']['aggregated']:.4f} | {validation_results['billed_services']['difference']:.4f} | {validation_results['billed_services']['status']} |

## Aggregated Totals Summary

- **Total Electricity Consumed (Units)**: {validation_results['units']['aggregated']:,.2f} kWh
- **Total Connected Load**: {validation_results['load']['aggregated']:,.2f} kW
- **Total Services Registered**: {validation_results['total_services']['aggregated']:,}
- **Total Services Billed**: {validation_results['billed_services']['aggregated']:,.2f}
"""

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(content)

    logger.info(f"Aggregation report written to: {report_path}")


def parse_arguments() -> argparse.Namespace:
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="District Aggregation Pipeline for EVision Telangana"
    )
    parser.add_argument(
        "--input-file",
        type=Path,
        default=Path("data/interim/consumption/circle_mapped.csv"),
        help="Path to circle mapped consumption dataset.",
    )
    parser.add_argument(
        "--output-file",
        type=Path,
        default=Path("data/interim/consumption/district_monthly_consumption.csv"),
        help="Path to save aggregated district consumption CSV.",
    )
    parser.add_argument(
        "--report-file",
        type=Path,
        default=Path("reports/district_aggregation_report.md"),
        help="Path to save markdown aggregation report.",
    )
    parser.add_argument(
        "--log-file",
        type=Path,
        default=None,
        help="Path to write processing logs.",
    )
    return parser.parse_args()


def main() -> None:
    """
    Main execution pipeline.
    """
    args = parse_arguments()
    setup_logging(args.log_file)

    logger.info("Starting District Aggregation Process...")

    try:
        # 1. Load data
        original_df = load_data(args.input_file)

        # 2. Perform aggregation
        aggregated_df = aggregate_consumption(original_df)

        # 3. Validate
        is_valid, validation_results = validate_aggregation(original_df, aggregated_df)

        # 4. Generate report (always write report, even on validation failure)
        generate_report(args.report_file, original_df, aggregated_df, validation_results, is_valid)

        # Also write report to data/reports/ to conform with output directory constraints
        try:
            data_reports_path = Path("data/reports/district_aggregation_report.md")
            generate_report(data_reports_path, original_df, aggregated_df, validation_results, is_valid)
            logger.info(f"Report copy written to: {data_reports_path}")
        except Exception as report_err:
            logger.warning(f"Could not write copy to data/reports: {report_err}")

        # 5. Handle mismatch check
        if not is_valid:
            logger.error("Validation failed! Mismatch detected between original and aggregated totals.")
            raise ValueError(
                f"Validation failed: Aggregation totals do not match original totals. "
                f"Validation results: {validation_results}"
            )

        # 6. Save output if valid
        args.output_file.parent.mkdir(parents=True, exist_ok=True)
        aggregated_df.to_csv(args.output_file, index=False)
        logger.info(
            f"Successfully saved aggregated district consumption dataset to: {args.output_file} "
            f"({len(aggregated_df)} rows)"
        )

        logger.info("District Aggregation completed successfully.")

    except Exception as e:
        logger.exception("An error occurred during district aggregation:")
        raise e


if __name__ == "__main__":
    main()
