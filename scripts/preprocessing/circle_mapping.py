"""
Circle-to-District mapping module for EVision Telangana electricity consumption dataset.

This script performs validation checks on circle mapping configurations, maps circles in the combined
consumption dataset to their corresponding districts, and generates mapping reports.
"""

import argparse
import logging
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional
import pandas as pd

# Setup logger
logger = logging.getLogger("circle_mapping")


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


def load_data(
    consumption_path: Path, mapping_path: Path
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load consumption dataset and mapping file.

    Args:
        consumption_path: Path to consumption CSV file.
        mapping_path: Path to mapping CSV file.

    Returns:
        Tuple of (consumption_df, mapping_df)

    Raises:
        FileNotFoundError: If either file does not exist.
    """
    if not consumption_path.exists():
        logger.error(f"Consumption file not found at: {consumption_path}")
        raise FileNotFoundError(f"Consumption file not found at: {consumption_path}")
    if not mapping_path.exists():
        logger.error(f"Mapping file not found at: {mapping_path}")
        raise FileNotFoundError(f"Mapping file not found at: {mapping_path}")

    logger.info(f"Loading consumption data from: {consumption_path}")
    consumption_df = pd.read_csv(consumption_path)

    logger.info(f"Loading circle to district mapping from: {mapping_path}")
    mapping_df = pd.read_csv(mapping_path)

    return consumption_df, mapping_df


def validate_mapping_data(
    consumption_df: pd.DataFrame, mapping_df: pd.DataFrame
) -> Dict[str, Any]:
    """
    Validate circle mapping configurations and detect anomalies.

    Checks:
    - Every unique circle in the mapping file appears exactly once.
    - Every mapped district is non-empty.
    - Detect duplicate mappings.
    - Detect missing mappings in the consumption dataset.

    Args:
        consumption_df: Consumption DataFrame.
        mapping_df: Circle-to-District mapping DataFrame.

    Returns:
        A dictionary containing validation metrics and lists of anomalies.
    """
    # 1. Clean circle names for validation
    mapping_df_clean = mapping_df.copy()
    mapping_df_clean["circle_clean"] = (
        mapping_df_clean["circle"].astype(str).str.strip().str.upper()
    )
    mapping_df_clean["district_clean"] = (
        mapping_df_clean["district"].fillna("").astype(str).str.strip()
    )
    mapping_df_clean["status_clean"] = (
        mapping_df_clean["status"].fillna("").astype(str).str.strip().str.lower()
    )

    consumption_circles = (
        consumption_df["circle"].dropna().astype(str).str.strip().str.upper().unique()
    )

    # 2. Check for duplicate circle entries in mapping file
    duplicate_mappings = (
        mapping_df_clean[mapping_df_clean["circle_clean"].duplicated()]["circle_clean"]
        .unique()
        .tolist()
    )

    # 3. Check for empty district names for status='mapped'
    mapped_rows = mapping_df_clean[mapping_df_clean["status_clean"] == "mapped"]
    empty_district_rows = mapped_rows[mapped_rows["district_clean"] == ""]
    empty_district_circles = empty_district_rows["circle_clean"].unique().tolist()

    # 4. Check for missing mappings:
    # A circle in consumption is "missing" mapping if it is either:
    # - Not present in mapping file
    # - Present in mapping file but status is not 'mapped' or district is empty
    mapped_circles_set = set(
        mapped_rows[mapped_rows["district_clean"] != ""]["circle_clean"]
    )

    missing_mappings = []
    unmapped_circles = []

    for circle in consumption_circles:
        if circle not in mapped_circles_set:
            missing_mappings.append(circle)
            unmapped_circles.append(circle)

    # Total circles in consumption dataset
    total_circles = len(consumption_circles)
    mapped_circles_count = total_circles - len(unmapped_circles)
    coverage_pct = (
        (mapped_circles_count / total_circles) * 100.0 if total_circles > 0 else 0.0
    )

    validation_report = {
        "total_circles": total_circles,
        "mapped_circles": mapped_circles_count,
        "unmapped_circles": unmapped_circles,
        "duplicate_mappings": duplicate_mappings,
        "empty_district_circles": empty_district_circles,
        "mapping_coverage_pct": coverage_pct,
        "has_duplicates": len(duplicate_mappings) > 0,
        "has_empty_districts": len(empty_district_circles) > 0,
        "has_missing_mappings": len(missing_mappings) > 0,
    }

    # Log results
    logger.info("Validation metrics:")
    logger.info(f"  Total unique circles in consumption data: {total_circles}")
    logger.info(f"  Mapped circles: {mapped_circles_count}")
    logger.info(f"  Unmapped circles: {len(unmapped_circles)}")
    logger.info(f"  Mapping coverage: {coverage_pct:.2f}%")

    if duplicate_mappings:
        logger.warning(
            f"Duplicate circle definitions found in mapping: {duplicate_mappings}"
        )
    if empty_district_circles:
        logger.warning(
            f"Mapped circles with empty districts found: {empty_district_circles}"
        )
    if missing_mappings:
        logger.warning(
            f"Circles in consumption data missing valid district mappings: {missing_mappings}"
        )

    return validation_report


def map_circles_to_districts(
    consumption_df: pd.DataFrame, mapping_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Perform the mapping of circles to districts and insert the district column.

    Args:
        consumption_df: Consumption DataFrame.
        mapping_df: Circle-to-District mapping DataFrame.

    Returns:
        Mapped DataFrame with the 'district' column inserted right after 'circle'.
    """
    df_out = consumption_df.copy()

    # Standardize mapping keys for lookup
    mapping_df_clean = mapping_df.copy()
    mapping_df_clean["circle_clean"] = (
        mapping_df_clean["circle"].astype(str).str.strip().str.upper()
    )

    # We only map rows with status='mapped' and non-empty district
    mapped_only = mapping_df_clean[
        (
            mapping_df_clean["status"]
            .fillna("")
            .astype(str)
            .str.strip()
            .str.lower()
            == "mapped"
        )
        & (mapping_df_clean["district"].notna())
        & (mapping_df_clean["district"].astype(str).str.strip() != "")
    ]

    # Create mapping dictionary: circle_clean -> district
    lookup = dict(zip(mapped_only["circle_clean"], mapped_only["district"]))

    # Match ignoring case and leading/trailing whitespace
    circle_clean_series = df_out["circle"].astype(str).str.strip().str.upper()
    district_series = circle_clean_series.map(lookup)

    # Insert 'district' right after 'circle'
    if "district" in df_out.columns:
        logger.info("District column already exists, overwriting it.")
        df_out["district"] = district_series
    else:
        circle_idx = df_out.columns.get_loc("circle")
        df_out.insert(circle_idx + 1, "district", district_series)

    return df_out


def write_unmapped_circles(unmapped_circles: List[str], output_path: Path) -> None:
    """
    Generate reports/unmapped_circles.csv for any circles that could not be mapped.

    Args:
        unmapped_circles: List of unmapped circle names.
        output_path: Path to write the CSV.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(unmapped_circles, columns=["circle"])
    df.to_csv(output_path, index=False)
    logger.info(
        f"Unmapped circles report written to: {output_path} ({len(unmapped_circles)} rows)"
    )


def write_mapping_report(
    validation_report: Dict[str, Any], report_path: Path
) -> None:
    """
    Generate reports/circle_mapping_report.md.

    Args:
        validation_report: The validation metrics dictionary.
        report_path: Path to write the MD report.
    """
    report_path.parent.mkdir(parents=True, exist_ok=True)

    total = validation_report["total_circles"]
    mapped = validation_report["mapped_circles"]
    unmapped = len(validation_report["unmapped_circles"])
    duplicates = len(validation_report["duplicate_mappings"])
    coverage = validation_report["mapping_coverage_pct"]

    content = f"""# Circle-to-District Mapping Report

This report summarizes the results and data quality of the Circle-to-District mapping stage.

## Mapping Metrics

| Metric | Value |
| :--- | :--- |
| **Total Circles** | {total} |
| **Mapped Circles** | {mapped} |
| **Unmapped Circles** | {unmapped} |
| **Duplicate Mappings** | {duplicates} |
| **Mapping Coverage** | {coverage:.2f}% |

## Validation Checks Summary

- **Unique Mappings Check**: {"PASSED" if duplicates == 0 else "FAILED"}
  - *No circle should have duplicate definitions in the mapping file.*
- **Non-empty Mapped Districts Check**: {"PASSED" if not validation_report["has_empty_districts"] else "FAILED"}
  - *All circles with status 'mapped' must have non-empty district values.*
- **Missing Mappings Check**: {"PASSED" if unmapped == 0 else "WARNING (Unmapped Circles Found)"}
  - *All circles in the consumption dataset should be successfully mapped to a district.*

"""
    if unmapped > 0:
        content += "## Unmapped Circles List\n\n"
        for circle in validation_report["unmapped_circles"]:
            content += f"- {circle}\n"
        content += "\n"

    if duplicates > 0:
        content += "## Duplicate Circles in Mapping File\n\n"
        for circle in validation_report["duplicate_mappings"]:
            content += f"- {circle}\n"
        content += "\n"

    if validation_report["empty_district_circles"]:
        content += "## Circles Mapped to Empty Districts\n\n"
        for circle in validation_report["empty_district_circles"]:
            content += f"- {circle}\n"
        content += "\n"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

    logger.info(f"Mapping report written to: {report_path}")


def parse_arguments() -> argparse.Namespace:
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Circle-to-District Mapping Pipeline for EVision Telangana"
    )
    parser.add_argument(
        "--consumption-file",
        type=Path,
        default=Path("data/interim/consumption/consumption_combined.csv"),
        help="Path to combined consumption dataset.",
    )
    parser.add_argument(
        "--mapping-file",
        type=Path,
        default=Path("data/mappings/circle_to_district.csv"),
        help="Path to circle-to-district mapping CSV.",
    )
    parser.add_argument(
        "--output-file",
        type=Path,
        default=Path("data/interim/consumption/circle_mapped.csv"),
        help="Path to save mapped consumption dataset.",
    )
    parser.add_argument(
        "--unmapped-file",
        type=Path,
        default=Path("reports/unmapped_circles.csv"),
        help="Path to save unmapped circles CSV report.",
    )
    parser.add_argument(
        "--report-file",
        type=Path,
        default=Path("reports/circle_mapping_report.md"),
        help="Path to save markdown mapping report.",
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
    Main entry point for circle mapping.
    """
    args = parse_arguments()
    setup_logging(args.log_file)

    logger.info("Starting Circle-to-District Mapping Process...")

    try:
        # 1. Load datasets
        consumption_df, mapping_df = load_data(
            args.consumption_file, args.mapping_file
        )

        # 2. Validate mappings
        validation_report = validate_mapping_data(consumption_df, mapping_df)

        # 3. Perform mapping
        mapped_df = map_circles_to_districts(consumption_df, mapping_df)

        # 4. Save output dataset
        args.output_file.parent.mkdir(parents=True, exist_ok=True)
        mapped_df.to_csv(args.output_file, index=False)
        logger.info(
            f"Successfully saved mapped consumption dataset to: {args.output_file} ({len(mapped_df)} rows)"
        )

        # 5. Generate reports
        write_unmapped_circles(
            validation_report["unmapped_circles"], args.unmapped_file
        )
        write_mapping_report(validation_report, args.report_file)

        logger.info("Circle-to-District Mapping Process completed successfully.")

    except Exception as e:
        logger.exception("An error occurred during circle mapping:")
        raise e


if __name__ == "__main__":
    main()
