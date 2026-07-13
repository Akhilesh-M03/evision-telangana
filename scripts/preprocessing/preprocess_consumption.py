"""
Preprocessing module for EVision Telangana electricity consumption datasets.

This script recursively discovers monthly consumption CSV files from TG-SPDCL and TG-NPDCL,
extracts metadata from file paths, standardizes column headers and data types,
aggregates the data, performs validation, and generates a validation report.

The script is designed to be idempotent and handles malformed files gracefully.
"""

import argparse
from datetime import datetime
import logging
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional
import pandas as pd

# Setup Logger
logger = logging.getLogger("preprocess_consumption")


def setup_logging(log_file: Optional[Path] = None) -> None:
    """
    Configure the logging system for console and optional file logging.

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


# Standardized Target Columns
REQUIRED_COLUMNS = [
    "source",
    "year",
    "month",
    "reporting_month",
    "circle",
    "division",
    "subdivision",
    "section",
    "area",
    "cat_code",
    "category",
    "total_services",
    "billed_services",
    "units",
    "load",
]

# Raw header to standardized column mapping (ignoring case, spaces, and underscores)
COLUMN_MAPPING = {
    "circle": "circle",
    "division": "division",
    "subdivision": "subdivision",
    "section": "section",
    "area": "area",
    "catcode": "cat_code",
    "catdesc": "category",
    "totservices": "total_services",
    "billdservices": "billed_services",
    "billedservices": "billed_services",
    "units": "units",
    "load": "load",
}


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments for the preprocessing pipeline.

    Returns:
        argparse.Namespace containing paths for inputs and outputs.
    """
    parser = argparse.ArgumentParser(
        description="Preprocess electricity consumption datasets for EVision Telangana."
    )
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=Path("data/raw/consumption"),
        help="Directory containing raw TG-SPDCL and TG-NPDCL CSV files.",
    )
    parser.add_argument(
        "--interim-dir",
        type=Path,
        default=Path("data/interim/consumption"),
        help="Directory to write preprocessed interim datasets.",
    )
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=Path("reports"),
        help="Directory to write processing validation reports.",
    )
    parser.add_argument(
        "--log-file",
        type=Path,
        default=None,
        help="Path to write processing logs.",
    )
    return parser.parse_args()


def discover_files(raw_dir: Path) -> List[Path]:
    """
    Recursively discover all CSV files under TG-SPDCL and TG-NPDCL.

    Args:
        raw_dir: Path to raw consumption directory.

    Returns:
        List of pathlib.Path objects of discovered CSV files.
    """
    if not raw_dir.exists():
        logger.error(f"Raw data directory does not exist: {raw_dir}")
        return []

    # Discover CSV files recursively
    files = sorted(list(raw_dir.rglob("*.csv")))
    logger.info(f"Discovered {len(files)} CSV files under {raw_dir}")
    return files


def extract_metadata(file_path: Path) -> Tuple[str, int, int, str]:
    """
    Extract source, year, month, and reporting_month from file path and filename.

    Path format expected: .../source/year/filename.csv
    Filename format expected: <month_num>_<month_name>_<year>.csv (e.g. 06_Jun_2021.csv or 2_FEB_2024.csv)

    Args:
        file_path: Path to the CSV file.

    Returns:
        A tuple of (source, year, month, reporting_month).

    Raises:
        ValueError: If metadata extraction fails due to unexpected path or naming convention.
    """
    # 1. Extract source (must be TG-SPDCL or TG-NPDCL)
    source = ""
    for parent in file_path.parents:
        if parent.name in ["TG-SPDCL", "TG-NPDCL"]:
            source = parent.name
            break

    if not source:
        raise ValueError(f"Could not determine source (TG-SPDCL/TG-NPDCL) from path: {file_path}")

    # 2. Extract year from path folder name or filename
    try:
        year = int(file_path.parent.name)
    except ValueError:
        raise ValueError(f"Could not parse year from parent directory name: {file_path.parent.name}")

    # 3. Extract month number from filename stem
    stem_parts = file_path.stem.split("_")
    if not stem_parts:
        raise ValueError(f"Filename does not follow '<month_num>_<name>' format: {file_path.name}")

    try:
        month = int(stem_parts[0])
    except ValueError:
        raise ValueError(f"First component of filename is not an integer month: {stem_parts[0]}")

    if not (1 <= month <= 12):
        raise ValueError(f"Month number {month} out of valid range (1-12) in file: {file_path.name}")

    # 4. Generate reporting month in YYYY-MM format
    reporting_month = f"{year:04d}-{month:02d}"

    return source, year, month, reporting_month


def normalize_and_clean(
    df: pd.DataFrame, source: str, year: int, month: int, reporting_month: str
) -> pd.DataFrame:
    """
    Standardize the columns and clean datatypes for a single file's DataFrame.

    Args:
        df: Raw DataFrame read from a CSV.
        source: Extracted source name.
        year: Extracted year.
        month: Extracted month number.
        reporting_month: Extracted reporting month string.

    Returns:
        A cleaned, standardized DataFrame matching target schema.
    """
    cleaned_df = df.copy()

    # 1. Standardize column names using case-insensitive mapping
    mapped_columns = []
    for col in cleaned_df.columns:
        col_clean = str(col).lower().replace("_", "").replace(" ", "").strip()
        mapped = COLUMN_MAPPING.get(col_clean, col_clean)
        mapped_columns.append(mapped)

    cleaned_df.columns = mapped_columns

    # 2. Add metadata columns
    cleaned_df["source"] = source
    cleaned_df["year"] = year
    cleaned_df["month"] = month
    cleaned_df["reporting_month"] = reporting_month

    # 3. Ensure all REQUIRED_COLUMNS exist
    for col in REQUIRED_COLUMNS:
        if col not in cleaned_df.columns:
            logger.warning(f"Required column '{col}' missing. Adding it with NaN values.")
            cleaned_df[col] = pd.NA

    # 4. Filter to target columns and preserve ordering
    cleaned_df = cleaned_df[REQUIRED_COLUMNS]

    # 5. Clean string/categorical columns (uppercase, stripped, NaNs handled)
    string_cols = ["circle", "division", "subdivision", "section", "area", "category"]
    for col in string_cols:
        cleaned_df[col] = (
            cleaned_df[col]
            .fillna("")
            .astype(str)
            .str.strip()
            .str.upper()
        )

    # 6. Clean numeric columns
    # Integer columns (using nullable Int64 to preserve NaNs without converting to float)
    int_cols = ["cat_code", "total_services", "billed_services"]
    for col in int_cols:
        cleaned_df[col] = pd.to_numeric(cleaned_df[col], errors="coerce").astype("Int64")

    # Float columns
    float_cols = ["units", "load"]
    for col in float_cols:
        cleaned_df[col] = pd.to_numeric(cleaned_df[col], errors="coerce").astype(float)

    return cleaned_df


def generate_validation_report(
    report_path: Path,
    inventory: List[Dict[str, Any]],
    combined_df: pd.DataFrame,
    duplicates_dropped: int,
) -> None:
    """
    Generate a markdown validation report summarizing the preprocessing run.

    Args:
        report_path: Path where the report will be written.
        inventory: Metadata and status record for each discovered file.
        combined_df: The final aggregated, deduplicated DataFrame.
        duplicates_dropped: Number of duplicate rows removed.
    """
    total_files = len(inventory)
    successful_files = sum(1 for f in inventory if f["status"] == "SUCCESS")
    failed_files = total_files - successful_files

    total_raw_rows = sum(f["row_count"] for f in inventory if f["status"] == "SUCCESS")
    final_rows = len(combined_df)

    # Missing value statistics
    missing_counts = combined_df.isnull().sum()
    missing_table = "\n".join(
        [f"| {col} | {missing_counts[col]} |" for col in REQUIRED_COLUMNS]
    )

    # Failed files summary
    failed_section = ""
    if failed_files > 0:
        failed_section = "\n### Failed Files\n\n| File Path | Error Message |\n| --- | --- |\n"
        for item in inventory:
            if item["status"] == "FAILED":
                failed_section += f"| `{item['file_path']}` | {item['error_message']} |\n"

    # Processing inventory table (detailed file breakdown)
    inventory_table = ""
    for item in sorted(inventory, key=lambda x: (x["source"], x["year"], x["month"])):
        inventory_table += (
            f"| {item['source']} | {item['year']} | {item['month']} | "
            f"`{Path(item['file_path']).name}` | {item['status']} | {item['row_count']} | "
            f"{item['error_message'] or '-'} |\n"
        )

    # Build full report
    report_content = f"""# Consumption Dataset Preprocessing Validation Report

Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Processing Summary

| Metric | Value |
| --- | --- |
| Total Discovered Files | {total_files} |
| Successfully Processed Files | {successful_files} |
| Failed Files | {failed_files} |
| Total Raw Rows Read | {total_raw_rows} |
| Duplicate Rows Dropped | {duplicates_dropped} |
| Final Output Rows | {final_rows} |

{failed_section}

## Schema & Column Validation

Standardized schema columns verify:
- Source dataset matching `TG-SPDCL` or `TG-NPDCL`.
- Month and Year correctly parsed from path and filenames.
- Clean uppercase format for strings.
- Nullable `Int64` integer mapping for services.
- `float` numeric mapping for consumption units and load.

### Missing Values Count

| Column | Missing Count |
| --- | --- |
{missing_table}

## Detailed File Inventory

| Source | Year | Month | File Name | Status | Rows Read | Error Message |
| --- | --- | --- | --- | --- | --- | --- |
{inventory_table}
"""

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_content, encoding="utf-8")
    logger.info(f"Validation report written to: {report_path}")


def main() -> None:
    """
    Main orchestration function for the preprocessing pipeline.
    """
    args = parse_arguments()
    setup_logging(args.log_file)

    logger.info("Starting EVision Telangana Consumption Preprocessing Pipeline")

    # 1. Discover CSV files
    discovered_files = discover_files(args.raw_dir)
    if not discovered_files:
        logger.warning("No CSV files discovered. Exiting pipeline.")
        return

    inventory: List[Dict[str, Any]] = []
    dataframes: List[pd.DataFrame] = []

    # 2. Process each file
    for file_path in discovered_files:
        try:
            relative_path = file_path.resolve().relative_to(Path.cwd().resolve()).as_posix()
        except ValueError:
            relative_path = file_path.as_posix()
        record: Dict[str, Any] = {
            "file_path": relative_path,
            "source": "",
            "year": 0,
            "month": 0,
            "reporting_month": "",
            "status": "PENDING",
            "row_count": 0,
            "error_message": "",
        }

        try:
            # Extract metadata
            source, year, month, reporting_month = extract_metadata(file_path)
            record.update(
                {
                    "source": source,
                    "year": year,
                    "month": month,
                    "reporting_month": reporting_month,
                }
            )

            # Read CSV safely
            # Empty rows or bad formatting will be handled gracefully
            try:
                df = pd.read_csv(file_path, keep_default_na=True)
            except Exception as read_err:
                raise ValueError(f"CSV read error: {read_err}")

            if df.empty:
                raise ValueError("File is empty (contains no rows).")

            # Clean and normalize columns
            cleaned_df = normalize_and_clean(df, source, year, month, reporting_month)

            dataframes.append(cleaned_df)
            record.update({"status": "SUCCESS", "row_count": len(cleaned_df)})
            logger.info(
                f"Successfully preprocessed {relative_path} ({len(cleaned_df)} rows)"
            )

        except Exception as err:
            error_msg = str(err)
            record.update({"status": "FAILED", "error_message": error_msg})
            logger.error(f"Failed to preprocess {relative_path}: {error_msg}")

        inventory.append(record)

    # 3. Create outputs directories
    args.interim_dir.mkdir(parents=True, exist_ok=True)
    args.reports_dir.mkdir(parents=True, exist_ok=True)

    # 4. Save file inventory
    inventory_df = pd.DataFrame(inventory)
    inventory_path = args.interim_dir / "consumption_inventory.csv"
    inventory_df.to_csv(inventory_path, index=False)
    logger.info(f"File inventory written to: {inventory_path}")

    # 5. Aggregate and deduplicate combined dataset
    if dataframes:
        combined_df = pd.concat(dataframes, ignore_index=True)
        raw_combined_rows = len(combined_df)

        # Check for duplicates
        duplicates_dropped = int(combined_df.duplicated().sum())
        if duplicates_dropped > 0:
            logger.info(f"Found {duplicates_dropped} duplicate rows. Dropping them.")
            combined_df = combined_df.drop_duplicates()

        # Save combined dataset
        combined_path = args.interim_dir / "consumption_combined.csv"
        combined_df.to_csv(combined_path, index=False)
        logger.info(
            f"Combined dataset saved to: {combined_path} "
            f"({len(combined_df)} rows, dropped {duplicates_dropped} duplicates)"
        )

        # 6. Generate validation report
        report_path = args.reports_dir / "consumption_validation_report.md"
        generate_validation_report(
            report_path, inventory, combined_df, duplicates_dropped
        )
    else:
        logger.error("No dataframes were successfully processed. Skipping aggregation.")

    logger.info("EVision Telangana Consumption Preprocessing Pipeline Completed")


if __name__ == "__main__":
    main()
