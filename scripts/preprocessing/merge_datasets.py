"""
Dataset Integration module for EVision Telangana - Epic 7: Master Dataset V1.

This script integrates three preprocessed datasets into a single, validated master
dataset for use in downstream EV charging infrastructure planning and ML pipelines:

  1. district_monthly_consumption.csv  (primary / base table)
  2. charging_stations_clean.csv       (aggregated charging station counts)
  3. district_geography.csv            (latitude, longitude, area)

The script is idempotent: re-running it overwrites any previous outputs without
side effects.  It never writes to data/raw.

Outputs
-------
  data/interim/merged/master_dataset_v1.csv
  reports/master_dataset_report.md

Usage
-----
  python scripts/preprocessing/merge_datasets.py
  python scripts/preprocessing/merge_datasets.py --consumption data/interim/consumption/district_monthly_consumption.csv
"""

import argparse
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd

# ---------------------------------------------------------------------------
# Logger
# ---------------------------------------------------------------------------

logger = logging.getLogger("merge_datasets")


# ---------------------------------------------------------------------------
# Default paths  (all relative to project root)
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DEFAULT_CONSUMPTION_PATH = (
    PROJECT_ROOT / "data" / "interim" / "consumption" / "district_monthly_consumption.csv"
)
DEFAULT_CHARGING_PATH = (
    PROJECT_ROOT / "data" / "interim" / "charging_stations" / "charging_stations_clean.csv"
)
DEFAULT_GEOGRAPHY_PATH = (
    PROJECT_ROOT / "data" / "interim" / "geography" / "district_geography.csv"
)
DEFAULT_OUTPUT_PATH = (
    PROJECT_ROOT / "data" / "interim" / "merged" / "master_dataset_v1.csv"
)
DEFAULT_REPORT_PATH = PROJECT_ROOT / "reports" / "master_dataset_report.md"


# ---------------------------------------------------------------------------
# District name normalisation
# ---------------------------------------------------------------------------

# Mapping from consumption dataset district labels (upper-case) to the
# canonical district_name used in district_geography.csv.
#
# Only entries that do NOT resolve via a simple case-insensitive match are
# listed here.  This table was derived by cross-referencing the district_
# aggregation pipeline, the circle_to_district mapping, and the geography
# report.
CONSUMPTION_TO_CANONICAL: Dict[str, str] = {
    "ASIFABAD": "Kumuram Bheem Asifabad",
    "BHUPALAPALLY": "Jayashankar Bhupalpally",
    "GADWAL": "Jogulamba Gadwal",
    "JAGITYAL": "Jagtial",
    "MAHABOOBNAGAR": "Mahabubnagar",
    "MEDCHAL": "Medchal Malkajgiri",
    "PEDDAPALLY": "Peddapalli",
    "RAJANNA SIRICILLA": "Rajanna Sircilla",
    "RANGAREDDY": "Ranga Reddy",
    "YADADRI": "Yadadri Bhuvanagiri",
}

# Mapping from charging-station dataset district labels to canonical names.
# Only entries that do NOT resolve via a simple case-insensitive match.
CHARGING_TO_CANONICAL: Dict[str, str] = {
    "Jangoan": "Jangaon",
}

# Geometry-related column substrings to exclude when merging geography.
GEOMETRY_COLUMN_SUBSTRINGS: Tuple[str, ...] = (
    "geometry",
    "geom",
    "shape",
    "polygon",
    "wkt",
    "wkb",
)


# ---------------------------------------------------------------------------
# Logging helpers
# ---------------------------------------------------------------------------


def setup_logging(log_file: Optional[Path] = None) -> None:
    """
    Configure the logging system for console and optional file output.

    Args:
        log_file: Optional path to write log output.  Parent directories are
            created automatically.
    """
    # Reconfigure stdout to UTF-8 where supported (Python 3.7+ on Windows)
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except AttributeError:
        pass

    handlers: List[logging.Handler] = [logging.StreamHandler(sys.stdout)]
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(log_file, mode="w", encoding="utf-8"))

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=handlers,
        force=True,
    )


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------


def load_csv(path: Path, label: str) -> pd.DataFrame:
    """
    Load a CSV file into a DataFrame with error handling.

    Args:
        path:  Absolute or relative path to the CSV file.
        label: Human-readable label used in log messages.

    Returns:
        Loaded DataFrame.

    Raises:
        FileNotFoundError: If ``path`` does not exist.
        ValueError:        If the resulting DataFrame is empty.
    """
    if not path.exists():
        raise FileNotFoundError(f"[{label}] Input file not found: {path}")

    logger.info(f"[{label}] Loading from: {path}")
    df = pd.read_csv(path, low_memory=False)

    if df.empty:
        raise ValueError(f"[{label}] Loaded DataFrame is empty: {path}")

    logger.info(f"[{label}] Loaded {len(df):,} rows × {len(df.columns)} columns")
    return df


def ensure_output_dirs(paths: List[Path]) -> None:
    """
    Create parent directories for all given output file paths.

    Args:
        paths: List of output file Paths whose parent directories to create.
    """
    for p in paths:
        p.parent.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Ensured output directory: {p.parent}")


# ---------------------------------------------------------------------------
# District name normalisation
# ---------------------------------------------------------------------------


def _build_case_insensitive_lookup(canonical_names: List[str]) -> Dict[str, str]:
    """
    Build a upper-case keyed lookup from canonical geography district names.

    Args:
        canonical_names: List of official district names from district_geography.

    Returns:
        Dict mapping ``name.upper()`` → ``name`` for every canonical name.
    """
    return {name.upper(): name for name in canonical_names}


def normalise_district_column(
    df: pd.DataFrame,
    column: str,
    canonical_lookup: Dict[str, str],
    explicit_map: Dict[str, str],
    dataset_label: str,
) -> Tuple[pd.DataFrame, List[str]]:
    """
    Normalise a district column in ``df`` to canonical geography names.

    Resolution order:
      1. Apply ``explicit_map`` (upper-case key → canonical value).
      2. Apply case-insensitive lookup against geography canonical names.
      3. Leave unresolved values as-is and report them.

    Args:
        df:             Source DataFrame (mutated in-place copy).
        column:         Name of the district column to normalise.
        canonical_lookup: Mapping of ``upper(name)`` → canonical name.
        explicit_map:   Hard-coded overrides for known mismatches.
        dataset_label:  Label used in log messages.

    Returns:
        Tuple of (normalised DataFrame, list of unresolved district names).
    """
    df = df.copy()
    original_values = df[column].copy()

    explicit_upper = {k.upper(): v for k, v in explicit_map.items()}

    def _resolve(raw: str) -> str:
        upper = str(raw).strip().upper()
        if upper in explicit_upper:
            return explicit_upper[upper]
        if upper in canonical_lookup:
            return canonical_lookup[upper]
        return raw  # unresolved

    df[column] = df[column].apply(_resolve)

    # Identify still-unresolved values
    still_unresolved = [
        v for v in df[column].unique() if v.upper() not in canonical_lookup
    ]

    changed = original_values != df[column]
    n_changed = changed.sum()
    if n_changed:
        logger.info(
            f"[{dataset_label}] Normalised {n_changed:,} district values in '{column}'"
        )
    if still_unresolved:
        logger.warning(
            f"[{dataset_label}] {len(still_unresolved)} district(s) could not be "
            f"resolved to canonical geography names: {still_unresolved}"
        )

    return df, still_unresolved


# ---------------------------------------------------------------------------
# Dataset preparation
# ---------------------------------------------------------------------------


def prepare_consumption(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validate and lightly clean the consumption base table.

    Expected columns: district, year, month, reporting_month, units, load,
    total_services, billed_services, circle_count, division_count,
    subdivision_count.

    Args:
        df: Raw consumption DataFrame.

    Returns:
        Cleaned consumption DataFrame.

    Raises:
        ValueError: If required columns are missing.
    """
    required = [
        "district",
        "year",
        "month",
        "reporting_month",
        "units",
        "load",
        "total_services",
        "billed_services",
        "circle_count",
        "division_count",
        "subdivision_count",
    ]
    _assert_required_columns(df, required, "consumption")

    df = df.copy()

    # Strip whitespace from string columns
    df["district"] = df["district"].str.strip()
    df["reporting_month"] = df["reporting_month"].str.strip()

    logger.info(
        f"[consumption] {df['district'].nunique()} districts, "
        f"{df['reporting_month'].nunique()} reporting months"
    )
    return df


def prepare_charging_stations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate charging stations by district and return a count summary.

    Expected columns include: district.

    Args:
        df: Raw charging stations DataFrame.

    Returns:
        DataFrame with columns [district, charging_station_count].

    Raises:
        ValueError: If the 'district' column is missing.
    """
    _assert_required_columns(df, ["district"], "charging_stations")

    df = df.copy()
    df["district"] = df["district"].str.strip()

    agg = (
        df.groupby("district", sort=True)
        .size()
        .reset_index(name="charging_station_count")
    )

    logger.info(
        f"[charging_stations] Aggregated {len(df):,} records "
        f"into {len(agg)} district rows"
    )
    return agg


def prepare_geography(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extract and clean required geography fields, excluding geometry columns.

    Required source columns: district_name, centroid_latitude,
    centroid_longitude, area_sq_km.

    Args:
        df: Raw geography DataFrame.

    Returns:
        DataFrame with columns:
            [district_name, latitude, longitude, district_area_sqkm].

    Raises:
        ValueError: If required columns are missing.
    """
    required_source = ["district_name", "centroid_latitude", "centroid_longitude", "area_sq_km"]
    _assert_required_columns(df, required_source, "geography")

    df = df.copy()

    # Drop any geometry-like columns defensively
    geo_cols = [
        c for c in df.columns
        if any(sub in c.lower() for sub in GEOMETRY_COLUMN_SUBSTRINGS)
    ]
    if geo_cols:
        logger.info(f"[geography] Dropping geometry-related columns: {geo_cols}")
        df = df.drop(columns=geo_cols)

    # Select and rename only the required fields
    geo_slim = df[["district_name", "centroid_latitude", "centroid_longitude", "area_sq_km"]].rename(
        columns={
            "centroid_latitude": "latitude",
            "centroid_longitude": "longitude",
            "area_sq_km": "district_area_sqkm",
        }
    )

    geo_slim["district_name"] = geo_slim["district_name"].str.strip()

    logger.info(f"[geography] Prepared {len(geo_slim)} district geography records")
    return geo_slim


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------


def _assert_required_columns(df: pd.DataFrame, required: List[str], label: str) -> None:
    """
    Assert that all required columns exist in ``df``.

    Args:
        df:       DataFrame to check.
        required: List of column names that must be present.
        label:    Dataset label used in the error message.

    Raises:
        ValueError: If any required column is absent.
    """
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(
            f"[{label}] Missing required columns: {missing}.  "
            f"Available: {df.columns.tolist()}"
        )


def validate_district_coverage(
    consumption_districts: List[str],
    charging_districts: List[str],
    geography_districts: List[str],
) -> Dict[str, List[str]]:
    """
    Validate that districts in consumption and charging data exist in geography.

    Args:
        consumption_districts: District names from the (normalised) consumption table.
        charging_districts:    District names from the (normalised) charging table.
        geography_districts:   Canonical district names from geography.

    Returns:
        Dict with keys:
          'consumption_missing_from_geo' – consumption districts not in geography
          'charging_missing_from_geo'    – charging districts not in geography
          'geo_not_in_consumption'       – geography districts absent from consumption
    """
    geo_set = set(geography_districts)
    cons_set = set(consumption_districts)
    cs_set = set(charging_districts)

    result: Dict[str, List[str]] = {
        "consumption_missing_from_geo": sorted(cons_set - geo_set),
        "charging_missing_from_geo": sorted(cs_set - geo_set),
        "geo_not_in_consumption": sorted(geo_set - cons_set),
    }

    for key, districts in result.items():
        if districts:
            logger.warning(f"[validation] {key}: {districts}")
        else:
            logger.info(f"[validation] {key}: none (OK)")

    return result


def validate_master(df: pd.DataFrame) -> Dict[str, object]:
    """
    Run post-merge validation checks on the master dataset.

    Checks:
      - Duplicate rows (all columns)
      - Duplicate (district, reporting_month) pairs
      - Unexpected nulls per column

    Args:
        df: Merged master DataFrame.

    Returns:
        Dict summarising validation results.
    """
    stats: Dict[str, object] = {}

    # Duplicate full rows
    dup_full = int(df.duplicated().sum())
    stats["duplicate_full_rows"] = dup_full
    if dup_full:
        logger.warning(f"[master] {dup_full} fully duplicated rows found")
    else:
        logger.info("[master] No fully duplicated rows (OK)")

    # Duplicate business key
    dup_key = int(df.duplicated(subset=["district", "reporting_month"]).sum())
    stats["duplicate_key_rows"] = dup_key
    if dup_key:
        logger.warning(
            f"[master] {dup_key} duplicate (district, reporting_month) pairs found"
        )
    else:
        logger.info("[master] No duplicate (district, reporting_month) pairs (OK)")

    # Null counts per column
    null_counts: Dict[str, int] = {
        col: int(df[col].isna().sum()) for col in df.columns if df[col].isna().any()
    }
    stats["null_counts"] = null_counts
    if null_counts:
        logger.warning(f"[master] Columns with nulls: {null_counts}")
    else:
        logger.info("[master] No null values detected (OK)")

    return stats


# ---------------------------------------------------------------------------
# Merge pipeline
# ---------------------------------------------------------------------------


def merge_charging_stations(
    consumption: pd.DataFrame,
    charging_agg: pd.DataFrame,
) -> Tuple[pd.DataFrame, Dict[str, int]]:
    """
    Left-join charging station counts onto the consumption base table.

    Districts with no charging station present will receive 0 for
    ``charging_station_count``.

    Args:
        consumption:   Normalised consumption DataFrame.
        charging_agg:  Aggregated charging stations DataFrame
                       (columns: district, charging_station_count).

    Returns:
        Tuple of (merged DataFrame, join statistics dict).
    """
    before = len(consumption)
    merged = consumption.merge(
        charging_agg,
        on="district",
        how="left",
        validate="m:1",
    )
    after = len(merged)

    # Districts with no station → fill with 0
    n_zero = int(merged["charging_station_count"].isna().sum())
    merged["charging_station_count"] = (
        merged["charging_station_count"].fillna(0).astype(int)
    )

    stats = {
        "rows_before": before,
        "rows_after": after,
        "districts_with_no_station": n_zero // max(merged["reporting_month"].nunique(), 1),
    }

    if before != after:
        logger.error(
            f"[merge_charging] Row count changed: {before} → {after}. "
            "Check for 1:many relationship in charging_agg."
        )
    else:
        logger.info(
            f"[merge_charging] Left join successful: {after:,} rows retained. "
            f"{n_zero} rows filled with charging_station_count=0."
        )

    return merged, stats


def merge_geography(
    df: pd.DataFrame,
    geography: pd.DataFrame,
) -> Tuple[pd.DataFrame, Dict[str, int]]:
    """
    Left-join geographic fields (latitude, longitude, district_area_sqkm)
    onto the working DataFrame.

    Args:
        df:        Working DataFrame (consumption + charging counts).
        geography: Slim geography DataFrame
                   (columns: district_name, latitude, longitude, district_area_sqkm).

    Returns:
        Tuple of (merged DataFrame, join statistics dict).
    """
    before = len(df)
    merged = df.merge(
        geography.rename(columns={"district_name": "district"}),
        on="district",
        how="left",
        validate="m:1",
    )
    after = len(merged)

    n_null_lat = int(merged["latitude"].isna().sum())
    n_null_lon = int(merged["longitude"].isna().sum())
    n_null_area = int(merged["district_area_sqkm"].isna().sum())

    stats = {
        "rows_before": before,
        "rows_after": after,
        "null_latitude": n_null_lat,
        "null_longitude": n_null_lon,
        "null_area": n_null_area,
    }

    if before != after:
        logger.error(
            f"[merge_geography] Row count changed: {before} → {after}. "
            "Check for duplicates in geography table."
        )
    else:
        logger.info(
            f"[merge_geography] Left join successful: {after:,} rows retained."
        )

    if n_null_lat or n_null_lon or n_null_area:
        logger.warning(
            f"[merge_geography] Unmatched geography rows: "
            f"lat={n_null_lat}, lon={n_null_lon}, area={n_null_area}"
        )

    return merged, stats


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------


def build_report(
    master: pd.DataFrame,
    coverage: Dict[str, List[str]],
    validation: Dict[str, object],
    charging_join_stats: Dict[str, int],
    geography_join_stats: Dict[str, int],
    output_path: Path,
    report_path: Path,
) -> str:
    """
    Generate a Markdown report summarising the master dataset.

    Args:
        master:               Final merged master DataFrame.
        coverage:             District coverage validation results.
        validation:           Post-merge validation results.
        charging_join_stats:  Statistics from the charging station join.
        geography_join_stats: Statistics from the geography join.
        output_path:          Path where master_dataset_v1.csv was saved.
        report_path:          Path where this report will be saved.

    Returns:
        Rendered Markdown string.
    """
    now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    n_rows = len(master)
    n_districts = master["district"].nunique()
    n_months = master["reporting_month"].nunique()
    null_counts: Dict[str, int] = validation.get("null_counts", {})  # type: ignore[assignment]
    dup_full: int = validation.get("duplicate_full_rows", 0)  # type: ignore[assignment]
    dup_key: int = validation.get("duplicate_key_rows", 0)  # type: ignore[assignment]

    # ------------------------------------------------------------------ #
    # Section helpers
    # ------------------------------------------------------------------ #

    def _tick(condition: bool) -> str:
        return "✅ Pass" if condition else "❌ Fail"

    def _bullet_list(items: List[str], empty_msg: str = "_None_") -> str:
        if not items:
            return empty_msg
        return "\n".join(f"- `{i}`" for i in sorted(items))

    def _null_table(null_dict: Dict[str, int]) -> str:
        if not null_dict:
            return "_No null values detected._"
        rows = ["| Column | Null Count |", "| :--- | ---: |"]
        for col, cnt in sorted(null_dict.items()):
            rows.append(f"| `{col}` | {cnt:,} |")
        return "\n".join(rows)

    def _station_dist_table() -> str:
        tbl = (
            master.groupby("district")["charging_station_count"]
            .first()
            .sort_values(ascending=False)
            .reset_index()
        )
        rows = ["| District | Charging Stations |", "| :--- | ---: |"]
        for _, row in tbl.iterrows():
            rows.append(f"| {row['district']} | {int(row['charging_station_count'])} |")
        return "\n".join(rows)

    def _schema_table() -> str:
        rows = ["| Column | Dtype | Non-null Count |", "| :--- | :--- | ---: |"]
        for col in master.columns:
            rows.append(
                f"| `{col}` | `{master[col].dtype}` | {master[col].notna().sum():,} |"
            )
        return "\n".join(rows)

    def _geo_not_in_cons() -> str:
        districts = coverage.get("geo_not_in_consumption", [])
        if not districts:
            return "_None_"
        return "\n".join(f"- `{d}`" for d in sorted(districts))

    # ------------------------------------------------------------------ #
    # Render
    # ------------------------------------------------------------------ #
    lines = [
        "# EVision Telangana – Master Dataset V1 Report",
        "",
        f"_Generated: {now}_",
        "",
        "---",
        "",
        "## 1. Overview",
        "",
        "| Metric | Value |",
        "| :--- | ---: |",
        f"| **Total Rows** | {n_rows:,} |",
        f"| **Total Districts** | {n_districts} |",
        f"| **Reporting Months** | {n_months} |",
        f"| **Total Columns** | {len(master.columns)} |",
        f"| **Output Path** | `{output_path}` |",
        "",
        "---",
        "",
        "## 2. Schema",
        "",
        _schema_table(),
        "",
        "---",
        "",
        "## 3. District Coverage Validation",
        "",
        "### 3.1 Consumption Districts Not Found in Geography",
        "",
        _bullet_list(coverage.get("consumption_missing_from_geo", [])),
        "",
        "### 3.2 Charging Station Districts Not Found in Geography",
        "",
        _bullet_list(coverage.get("charging_missing_from_geo", [])),
        "",
        "### 3.3 Geography Districts Absent from Consumption",
        "",
        "> [!NOTE]",
        "> These geography districts have no consumption records.  This may indicate",
        "> newly created districts not yet in the consumption pipeline.",
        "",
        _geo_not_in_cons(),
        "",
        "---",
        "",
        "## 4. Join Statistics",
        "",
        "### 4.1 Charging Station Join",
        "",
        "| Metric | Value |",
        "| :--- | ---: |",
        f"| Rows Before Join | {charging_join_stats.get('rows_before', 'N/A'):,} |",
        f"| Rows After Join | {charging_join_stats.get('rows_after', 'N/A'):,} |",
        f"| Approx. Districts With Zero Stations | {charging_join_stats.get('districts_with_no_station', 'N/A')} |",
        "",
        "### 4.2 Geography Join",
        "",
        "| Metric | Value |",
        "| :--- | ---: |",
        f"| Rows Before Join | {geography_join_stats.get('rows_before', 'N/A'):,} |",
        f"| Rows After Join | {geography_join_stats.get('rows_after', 'N/A'):,} |",
        f"| Null Latitudes Post-Join | {geography_join_stats.get('null_latitude', 0)} |",
        f"| Null Longitudes Post-Join | {geography_join_stats.get('null_longitude', 0)} |",
        f"| Null Areas Post-Join | {geography_join_stats.get('null_area', 0)} |",
        "",
        "---",
        "",
        "## 5. Data Quality Validation",
        "",
        "| Check | Status |",
        "| :--- | :--- |",
        f"| No fully duplicated rows | {_tick(dup_full == 0)} |",
        f"| No duplicate (district, reporting_month) keys | {_tick(dup_key == 0)} |",
        f"| No unexpected nulls in non-optional columns | {_tick(not null_counts)} |",
        f"| All consumption districts resolved to geography | "
        f"{_tick(not coverage.get('consumption_missing_from_geo'))} |",
        f"| All charging districts resolved to geography | "
        f"{_tick(not coverage.get('charging_missing_from_geo'))} |",
        "",
        "### 5.1 Null Values by Column",
        "",
        _null_table(null_counts),
        "",
        "---",
        "",
        "## 6. Charging Station Distribution by District",
        "",
        _station_dist_table(),
        "",
        "---",
        "",
        "## 7. Dataset Summary Statistics",
        "",
        "| Column | Min | Max | Mean | Std |",
        "| :--- | ---: | ---: | ---: | ---: |",
    ]

    numeric_cols = master.select_dtypes(include="number").columns.tolist()
    for col in numeric_cols:
        s = master[col].dropna()
        if len(s) == 0:
            continue
        lines.append(
            f"| `{col}` | {s.min():.2f} | {s.max():.2f} | "
            f"{s.mean():.2f} | {s.std():.2f} |"
        )

    lines += [
        "",
        "---",
        "",
        "*Report generated automatically by `scripts/preprocessing/merge_datasets.py` "
        "on behalf of the EVision Telangana Preprocessing Pipeline.*",
        "",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        Parsed argument namespace.
    """
    parser = argparse.ArgumentParser(
        description="EVision Telangana – Epic 7: Merge datasets into Master Dataset V1.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--consumption",
        type=Path,
        default=DEFAULT_CONSUMPTION_PATH,
        help="Path to district_monthly_consumption.csv",
    )
    parser.add_argument(
        "--charging",
        type=Path,
        default=DEFAULT_CHARGING_PATH,
        help="Path to charging_stations_clean.csv",
    )
    parser.add_argument(
        "--geography",
        type=Path,
        default=DEFAULT_GEOGRAPHY_PATH,
        help="Path to district_geography.csv",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Path for master_dataset_v1.csv output",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=DEFAULT_REPORT_PATH,
        help="Path for master_dataset_report.md output",
    )
    parser.add_argument(
        "--log-file",
        type=Path,
        default=None,
        help="Optional path to write log output",
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------


def run(
    consumption_path: Path,
    charging_path: Path,
    geography_path: Path,
    output_path: Path,
    report_path: Path,
) -> pd.DataFrame:
    """
    Execute the full dataset integration pipeline.

    Steps:
      1. Load all three source datasets.
      2. Normalise district names to canonical geography names.
      3. Validate district coverage across datasets.
      4. Prepare and aggregate charging station data.
      5. Prepare geography (select, rename, exclude geometry).
      6. Merge charging station counts onto consumption (left join).
      7. Merge geography fields onto the result (left join).
      8. Run post-merge validation.
      9. Write master_dataset_v1.csv.
      10. Generate and write the Markdown report.

    Args:
        consumption_path: Path to district_monthly_consumption.csv.
        charging_path:    Path to charging_stations_clean.csv.
        geography_path:   Path to district_geography.csv.
        output_path:      Destination for master_dataset_v1.csv.
        report_path:      Destination for master_dataset_report.md.

    Returns:
        Final master DataFrame.
    """
    logger.info("=" * 70)
    logger.info("EVision Telangana – Epic 7: Dataset Integration (Master V1)")
    logger.info("=" * 70)

    # ------------------------------------------------------------------ #
    # Step 1 – Load raw sources
    # ------------------------------------------------------------------ #
    raw_consumption = load_csv(consumption_path, "consumption")
    raw_charging = load_csv(charging_path, "charging_stations")
    raw_geography = load_csv(geography_path, "geography")

    # ------------------------------------------------------------------ #
    # Step 2 – Build canonical lookup from geography
    # ------------------------------------------------------------------ #
    canonical_names: List[str] = raw_geography["district_name"].dropna().str.strip().tolist()
    canonical_lookup = _build_case_insensitive_lookup(canonical_names)

    # ------------------------------------------------------------------ #
    # Step 3 – Normalise district names
    # ------------------------------------------------------------------ #
    consumption, cons_unresolved = normalise_district_column(
        raw_consumption, "district", canonical_lookup, CONSUMPTION_TO_CANONICAL, "consumption"
    )
    charging_raw, cs_unresolved = normalise_district_column(
        raw_charging, "district", canonical_lookup, CHARGING_TO_CANONICAL, "charging_stations"
    )

    # ------------------------------------------------------------------ #
    # Step 4 – Prepare individual datasets
    # ------------------------------------------------------------------ #
    consumption = prepare_consumption(consumption)
    charging_agg = prepare_charging_stations(charging_raw)
    geography = prepare_geography(raw_geography)

    # ------------------------------------------------------------------ #
    # Step 5 – Validate district coverage
    # ------------------------------------------------------------------ #
    coverage = validate_district_coverage(
        consumption_districts=consumption["district"].unique().tolist(),
        charging_districts=charging_agg["district"].unique().tolist(),
        geography_districts=canonical_names,
    )

    # ------------------------------------------------------------------ #
    # Step 6 – Merge charging station counts onto consumption
    # ------------------------------------------------------------------ #
    master, charging_join_stats = merge_charging_stations(consumption, charging_agg)

    # ------------------------------------------------------------------ #
    # Step 7 – Merge geography
    # ------------------------------------------------------------------ #
    master, geography_join_stats = merge_geography(master, geography)

    # ------------------------------------------------------------------ #
    # Step 8 – Post-merge validation
    # ------------------------------------------------------------------ #
    validation = validate_master(master)

    # ------------------------------------------------------------------ #
    # Step 9 – Write output CSV
    # ------------------------------------------------------------------ #
    ensure_output_dirs([output_path, report_path])
    master.to_csv(output_path, index=False)
    logger.info(
        f"[output] Master dataset written: {output_path} "
        f"({len(master):,} rows × {len(master.columns)} columns)"
    )

    # ------------------------------------------------------------------ #
    # Step 10 – Write report
    # ------------------------------------------------------------------ #
    report_md = build_report(
        master=master,
        coverage=coverage,
        validation=validation,
        charging_join_stats=charging_join_stats,
        geography_join_stats=geography_join_stats,
        output_path=output_path,
        report_path=report_path,
    )
    report_path.write_text(report_md, encoding="utf-8")
    logger.info(f"[output] Report written: {report_path}")

    logger.info("=" * 70)
    logger.info("Pipeline complete.")
    logger.info("=" * 70)

    return master


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """Entry point for the merge pipeline."""
    args = parse_arguments()
    setup_logging(args.log_file)

    try:
        run(
            consumption_path=args.consumption,
            charging_path=args.charging,
            geography_path=args.geography,
            output_path=args.output,
            report_path=args.report,
        )
    except (FileNotFoundError, ValueError) as exc:
        logger.error(f"Pipeline aborted: {exc}")
        sys.exit(1)
    except Exception as exc:  # pylint: disable=broad-except
        logger.exception(f"Unexpected error: {exc}")
        sys.exit(2)


if __name__ == "__main__":
    main()
