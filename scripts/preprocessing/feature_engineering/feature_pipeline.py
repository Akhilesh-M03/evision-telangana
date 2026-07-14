"""
Feature Engineering Pipeline for EVision Telangana – Epic 8.

Orchestrates the complete feature-engineering workflow:

1. Load master dataset (READ-ONLY source).
2. Sort by (district, reporting_month) – mandatory for leakage prevention.
3. Apply each feature module in order:
   a. Temporal features
   b. Infrastructure features
   c. Utilization features
   d. Rolling features
   e. Growth features
4. Validate the resulting dataset.
5. Write output artefacts:
   - data/processed/master_dataset.csv
   - data/processed/ml_training_dataset.csv
   - data/processed/feature_dictionary.csv
   - reports/feature_engineering_report.md
6. Emit structured logging throughout.

Usage
-----
    python scripts/preprocessing/feature_engineering/feature_pipeline.py
    python scripts/preprocessing/feature_engineering/feature_pipeline.py \\
        --input  data/interim/merged/master_dataset_v1.csv \\
        --output-dir data/processed \\
        --reports-dir reports

The script is idempotent: re-running overwrites all output files safely.
"""

import argparse
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Internal module imports  (use absolute-style imports so the script can be
# run both as  ``python feature_pipeline.py``  and as a module inside the
# package)
# ---------------------------------------------------------------------------

try:
    from .temporal_features import add_temporal_features
    from .infrastructure_features import add_infrastructure_features
    from .utilization_features import add_utilization_features
    from .rolling_features import add_rolling_features
    from .growth_features import add_growth_features
    from .validation import validate_features, ValidationResult
    from .feature_dictionary import (
        FEATURE_ENTRIES,
        build_feature_dictionary,
        save_feature_dictionary,
        get_ml_columns,
    )
except ImportError:
    # Fallback for direct execution: insert parent dirs into sys.path
    _HERE = Path(__file__).resolve().parent
    sys.path.insert(0, str(_HERE))
    from temporal_features import add_temporal_features
    from infrastructure_features import add_infrastructure_features
    from utilization_features import add_utilization_features
    from rolling_features import add_rolling_features
    from growth_features import add_growth_features
    from validation import validate_features, ValidationResult
    from feature_dictionary import (
        FEATURE_ENTRIES,
        build_feature_dictionary,
        save_feature_dictionary,
        get_ml_columns,
    )


# ---------------------------------------------------------------------------
# Logger
# ---------------------------------------------------------------------------

logger = logging.getLogger("feature_pipeline")

# ---------------------------------------------------------------------------
# Default paths  (all resolved relative to project root)
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[3]

DEFAULT_INPUT_PATH = (
    PROJECT_ROOT / "data" / "interim" / "merged" / "master_dataset_v1.csv"
)
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
DEFAULT_REPORTS_DIR = PROJECT_ROOT / "reports"


# ---------------------------------------------------------------------------
# Setup logging
# ---------------------------------------------------------------------------


def setup_logging(log_file: Optional[Path] = None) -> None:
    """
    Configure console and optional file logging.

    Parameters
    ----------
    log_file : Path, optional
        If provided, log output is written to this file in addition to
        the console.
    """
    handlers = [logging.StreamHandler()]
    if log_file is not None:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(log_file, mode="w", encoding="utf-8"))

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=handlers,
    )


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments for the feature engineering pipeline.

    Returns
    -------
    argparse.Namespace
        Parsed arguments with resolved Path objects.
    """
    parser = argparse.ArgumentParser(
        description="EVision Telangana – Feature Engineering Pipeline (Epic 8)."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help="Path to the master dataset CSV (read-only source).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for processed output datasets.",
    )
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=DEFAULT_REPORTS_DIR,
        help="Directory for feature engineering report.",
    )
    parser.add_argument(
        "--log-file",
        type=Path,
        default=None,
        help="Optional path to write pipeline logs.",
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Pipeline stages
# ---------------------------------------------------------------------------


def load_master_dataset(input_path: Path) -> pd.DataFrame:
    """
    Load the master dataset from CSV.

    The file is treated as READ-ONLY; no modifications are made to it.

    Parameters
    ----------
    input_path : Path
        Path to master_dataset_v1.csv.

    Returns
    -------
    pd.DataFrame
        Raw master dataset.

    Raises
    ------
    FileNotFoundError
        If the input path does not exist.
    """
    if not input_path.exists():
        raise FileNotFoundError(
            f"Master dataset not found: {input_path}\n"
            "Ensure the preprocessing pipeline has been run first."
        )
    df = pd.read_csv(input_path, dtype={"reporting_month": str})
    logger.info(
        "Loaded master dataset: %d rows × %d columns from %s",
        len(df),
        len(df.columns),
        input_path,
    )
    return df


def sort_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sort the dataset by (district, reporting_month) – mandatory pre-condition.

    Sorting must happen **before** any rolling or growth feature is computed
    to ensure temporal ordering is preserved per district and data leakage
    cannot occur.

    Parameters
    ----------
    df : pd.DataFrame
        Unsorted or partially sorted master dataset.

    Returns
    -------
    pd.DataFrame
        Sorted copy with reset index.
    """
    sorted_df = df.sort_values(
        by=["district", "reporting_month"],
        ascending=True,
        kind="mergesort",  # stable sort preserves secondary ordering
    ).reset_index(drop=True)
    logger.info(
        "Dataset sorted by (district, reporting_month). "
        "First row: district=%s, month=%s; Last row: district=%s, month=%s",
        sorted_df.iloc[0]["district"],
        sorted_df.iloc[0]["reporting_month"],
        sorted_df.iloc[-1]["district"],
        sorted_df.iloc[-1]["reporting_month"],
    )
    return sorted_df


def apply_all_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply every feature engineering module in sequence.

    The order matters:

    1. Temporal  – calendar features (stateless, per-row).
    2. Infrastructure – density ratios (stateless, per-row).
    3. Utilization – service ratios (stateless, per-row).
    4. Rolling  – lag and window features (stateful, per-district).
    5. Growth   – growth rates and cumulative sums (stateful, per-district).

    Parameters
    ----------
    df : pd.DataFrame
        Sorted master dataset.

    Returns
    -------
    pd.DataFrame
        Fully feature-engineered dataset.
    """
    logger.info("=== Stage 1/5: Temporal features ===")
    df = add_temporal_features(df)

    logger.info("=== Stage 2/5: Infrastructure features ===")
    df = add_infrastructure_features(df)

    logger.info("=== Stage 3/5: Utilization features ===")
    df = add_utilization_features(df)

    logger.info("=== Stage 4/5: Rolling features ===")
    df = add_rolling_features(df)

    logger.info("=== Stage 5/5: Growth features ===")
    df = add_growth_features(df)

    n_original = 15  # columns in master_dataset_v1
    n_engineered = len(df.columns) - n_original
    logger.info(
        "Feature engineering complete: %d source columns + %d engineered features = %d total columns.",
        n_original,
        n_engineered,
        len(df.columns),
    )
    return df


def save_master_dataset(df: pd.DataFrame, output_dir: Path) -> Path:
    """
    Save the full feature-engineered dataset as master_dataset.csv.

    Parameters
    ----------
    df : pd.DataFrame
        Fully feature-engineered dataset.
    output_dir : Path
        Output directory.

    Returns
    -------
    Path
        Absolute path where the file was written.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / "master_dataset.csv"
    df.to_csv(out_path, index=False, encoding="utf-8")
    logger.info("master_dataset.csv written: %d rows × %d columns → %s", len(df), len(df.columns), out_path)
    return out_path


def save_ml_dataset(df: pd.DataFrame, output_dir: Path) -> Path:
    """
    Select ML-suitable columns and write ml_training_dataset.csv.

    Excluded columns include:
    - Non-numeric descriptive columns (district_name, month_name, season,
      reporting_month, geometry if present).
    - Any column whose feature dictionary entry marks it as ``exclude``.

    Parameters
    ----------
    df : pd.DataFrame
        Fully feature-engineered dataset.
    output_dir : Path
        Output directory.

    Returns
    -------
    Path
        Absolute path where the file was written.
    """
    ml_cols = get_ml_columns(df)

    # Ensure district column is NOT in ml columns (it's a string key)
    ml_cols = [c for c in ml_cols if c != "district"]

    ml_df = df[ml_cols].copy()
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / "ml_training_dataset.csv"
    ml_df.to_csv(out_path, index=False, encoding="utf-8")
    logger.info(
        "ml_training_dataset.csv written: %d rows × %d columns → %s",
        len(ml_df),
        len(ml_df.columns),
        out_path,
    )
    return out_path


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------


def generate_report(
    df: pd.DataFrame,
    val_result: ValidationResult,
    output_dir: Path,
    reports_dir: Path,
    input_path: Path,
) -> Path:
    """
    Write the feature engineering report to Markdown.

    Parameters
    ----------
    df : pd.DataFrame
        Fully feature-engineered dataset.
    val_result : ValidationResult
        Validation outcome.
    output_dir : Path
        Directory containing output CSV files.
    reports_dir : Path
        Directory where the report should be written.
    input_path : Path
        Path to the source master dataset (for provenance).

    Returns
    -------
    Path
        Absolute path of the written report.
    """
    generated_at = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    # --- Feature count breakdown per category ---------------------------
    category_counts: dict = {}
    for e in FEATURE_ENTRIES:
        if e.category == "source":
            continue
        category_counts[e.category] = category_counts.get(e.category, 0) + 1

    total_engineered = sum(category_counts.values())
    total_source = sum(1 for e in FEATURE_ENTRIES if e.category == "source")
    total_features = len(FEATURE_ENTRIES)

    cat_table_rows = "\n".join(
        f"| {cat.title()} | {cnt} |"
        for cat, cnt in sorted(category_counts.items())
    )

    # --- ML columns vs excluded -----------------------------------------
    ml_cols = [c for c in get_ml_columns(df) if c != "district"]
    excluded_entries = [e for e in FEATURE_ENTRIES if "exclude" in e.used_by and e.category != "source"]
    excluded_source = [e for e in FEATURE_ENTRIES if "exclude" in e.used_by and e.category == "source"]
    ml_cols_table = "\n".join(f"| `{c}` |" for c in ml_cols)
    excluded_table = "\n".join(
        f"| `{e.feature_name}` | {e.category.title()} | {e.description[:60]}… |"
        if len(e.description) > 60
        else f"| `{e.feature_name}` | {e.category.title()} | {e.description} |"
        for e in excluded_entries
    )
    excluded_src_table = "\n".join(
        f"| `{e.feature_name}` | {e.description[:60]}… |"
        if len(e.description) > 60
        else f"| `{e.feature_name}` | {e.description} |"
        for e in excluded_source
    )

    # --- Validation summary ---------------------------------------------
    val_status = "✅ PASSED" if val_result.passed else "❌ FAILED"
    errors_md = (
        "\n".join(f"- ❌ {e}" for e in val_result.errors)
        if val_result.errors
        else "_No errors._"
    )
    warnings_md = (
        "\n".join(f"- ⚠️ {w}" for w in val_result.warnings)
        if val_result.warnings
        else "_No warnings._"
    )

    # --- NaN summary by column ------------------------------------------
    nan_by_col = val_result.info.get("nan_by_column", {})
    nan_table = "\n".join(
        f"| `{col}` | {cnt} |"
        for col, cnt in sorted(nan_by_col.items(), key=lambda x: -x[1])
    ) if nan_by_col else "| _No NaN values_ | 0 |"

    # --- Output schema --------------------------------------------------
    schema_rows = []
    for col in df.columns:
        dtype = str(df[col].dtype)
        n_nan = int(df[col].isna().sum())
        schema_rows.append(f"| `{col}` | `{dtype}` | {n_nan} |")
    schema_table = "\n".join(schema_rows)

    # --- Processing statistics ------------------------------------------
    n_rows = len(df)
    n_districts = df["district"].nunique()
    n_cols = len(df.columns)
    date_min = df["reporting_month"].min()
    date_max = df["reporting_month"].max()

    report = f"""# EVision Telangana – Feature Engineering Report

_Generated: {generated_at}_

---

## 1. Engineered Feature Count

| Metric | Value |
| :--- | ---: |
| **Source Columns (pass-through)** | {total_source} |
| **Engineered Features** | {total_engineered} |
| **Total Features in master_dataset.csv** | {total_features} |
| **Features in ml_training_dataset.csv** | {len(ml_cols)} |

---

## 2. Feature Categories

| Category | Feature Count |
| :--- | ---: |
{cat_table_rows}

---

## 3. Validation Summary

**Status:** {val_status}

### Errors

{errors_md}

### Warnings

{warnings_md}

---

## 4. NaN Value Summary by Column

> [!NOTE]
> NaN values in rolling and growth feature columns are expected and intentional.
> They arise from the first observation(s) in each district where no historical
> data exists.  Infrastructure and utilization NaNs arise from zero denominators.

| Column | NaN Count |
| :--- | ---: |
{nan_table}

---

## 5. Output Schema

### master_dataset.csv  ({n_rows} rows × {n_cols} columns)

| Column | Dtype | NaN Count |
| :--- | :--- | ---: |
{schema_table}

---

## 6. Processing Statistics

| Metric | Value |
| :--- | ---: |
| **Input File** | `{input_path.name}` |
| **Total Rows** | {n_rows:,} |
| **Total Districts** | {n_districts} |
| **Date Range** | {date_min} → {date_max} |
| **Source Columns** | {total_source} |
| **Total Output Columns** | {n_cols} |

---

## 7. Features Excluded from ML Training Dataset

The following **engineered** features are excluded from `ml_training_dataset.csv`
because they are string/categorical and require encoding before ML use,
or because they are purely descriptive.

| Feature | Category | Reason |
| :--- | :--- | :--- |
{excluded_table}

### Source Columns Excluded from ML

| Feature | Reason |
| :--- | :--- |
{excluded_src_table}

---

## 8. Features Reserved for Future Datasets

The feature engineering package is designed to be extended.  The following
feature groups are planned but **not yet implemented**, pending additional data
sources:

| Future Feature Group | Required Dataset | Status |
| :--- | :--- | :--- |
| Population density features | Population census data | 🔜 Planned |
| EV registration density | EV registration records | 🔜 Planned |
| Road network features | Road network GIS data | 🔜 Planned |
| Economic indicators | GDP / income data | 🔜 Planned |
| Weather/climate features | Historical weather data | 🔜 Planned |
| Demographic features | Demographics data | 🔜 Planned |

To add a new feature module, create a new file in
`scripts/preprocessing/feature_engineering/` following the existing module
conventions, then add it to the `apply_all_features()` function in
`feature_pipeline.py`.

---

## 9. Data Leakage Prevention Summary

| Mechanism | Detail |
| :--- | :--- |
| **Pre-sort requirement** | Dataset sorted by `(district, reporting_month)` before any rolling/growth computation. |
| **Lag via shift(1)** | All rolling window features are applied to `units.shift(1)` – the current month is excluded from its own rolling statistics. |
| **Per-district groupby** | Rolling and growth computations are performed inside `groupby("district")` to prevent cross-district leakage. |
| **No global statistics** | No feature uses global means, medians, or statistics from the full dataset that would include future rows. |
| **Temporal flags** | `is_first_month` / `is_last_month` are boolean position flags derived only from the sorted dataset structure. |
| **No target encoding** | No feature is derived from a future target variable. |
| **Cumulative sums** | `cumulative_units` / `cumulative_load` include the current month (t-inclusive), which is appropriate for "total to date" features but is noted as potentially leaky if used as a predictor of the same month's consumption. |

---

*Report generated automatically by `scripts/preprocessing/feature_engineering/feature_pipeline.py`.*
"""

    reports_dir.mkdir(parents=True, exist_ok=True)
    report_path = reports_dir / "feature_engineering_report.md"
    report_path.write_text(report, encoding="utf-8")
    logger.info("Feature engineering report written to: %s", report_path)
    return report_path


# ---------------------------------------------------------------------------
# Main pipeline entry point
# ---------------------------------------------------------------------------


def run_pipeline(
    input_path: Optional[Path] = None,
    output_dir: Optional[Path] = None,
    reports_dir: Optional[Path] = None,
) -> None:
    """
    Execute the complete feature engineering pipeline.

    This function is the primary programmatic entry point.  It can be called
    from other scripts or from the CLI via ``__main__``.

    Parameters
    ----------
    input_path : Path, optional
        Source master dataset.  Defaults to
        ``data/interim/merged/master_dataset_v1.csv``.
    output_dir : Path, optional
        Output directory for processed datasets.  Defaults to
        ``data/processed``.
    reports_dir : Path, optional
        Output directory for the report.  Defaults to ``reports``.

    Raises
    ------
    FileNotFoundError
        If the master dataset does not exist.
    SystemExit
        If validation errors are found (exit code 1).
    """
    input_path = input_path or DEFAULT_INPUT_PATH
    output_dir = output_dir or DEFAULT_OUTPUT_DIR
    reports_dir = reports_dir or DEFAULT_REPORTS_DIR

    logger.info("=" * 70)
    logger.info("EVision Telangana – Feature Engineering Pipeline (Epic 8)")
    logger.info("=" * 70)
    logger.info("Input  : %s", input_path)
    logger.info("Output : %s", output_dir)
    logger.info("Reports: %s", reports_dir)

    # 1. Load
    df = load_master_dataset(input_path)

    # 2. Sort (MANDATORY before rolling/growth)
    df = sort_dataset(df)

    # 3. Apply all feature groups
    df = apply_all_features(df)

    # 4. Validate
    logger.info("=== Validation ===")
    val_result = validate_features(df)

    # 5. Save outputs
    logger.info("=== Saving outputs ===")
    save_master_dataset(df, output_dir)
    save_ml_dataset(df, output_dir)
    save_feature_dictionary(output_dir / "feature_dictionary.csv")

    # 6. Generate report
    generate_report(df, val_result, output_dir, reports_dir, input_path)

    logger.info("=" * 70)
    logger.info("Pipeline completed successfully.")
    logger.info(
        "Outputs:\n"
        "  %s/master_dataset.csv\n"
        "  %s/ml_training_dataset.csv\n"
        "  %s/feature_dictionary.csv\n"
        "  %s/feature_engineering_report.md",
        output_dir,
        output_dir,
        output_dir,
        reports_dir,
    )

    if not val_result.passed:
        logger.error(
            "Validation FAILED with %d error(s). Review the report before using outputs.",
            len(val_result.errors),
        )
        sys.exit(1)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """CLI entry point when the script is executed directly."""
    args = parse_arguments()
    setup_logging(args.log_file)
    run_pipeline(
        input_path=args.input,
        output_dir=args.output_dir,
        reports_dir=args.reports_dir,
    )


if __name__ == "__main__":
    main()
