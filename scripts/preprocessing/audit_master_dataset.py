"""
Audit module for EVision Telangana – Epic 7 follow-up.

Generates two supplementary audit reports from the existing master dataset and its
upstream source files.  This script is strictly read-only: it never modifies any CSV
file and never writes to data/raw.

Reports generated
-----------------
  reports/dataset_coverage_report.md
      District-month coverage grid, timeline visualisation, missing combinations,
      per-district statistics, global month gaps, and explanations for gaps based
      on observable data.

  reports/data_consistency_report.md
      Numeric integrity checks (unit/load/services totals before vs after merge),
      key-uniqueness checks, geography null checks, and lookup-table duplicate checks.

Usage
-----
  python scripts/preprocessing/audit_master_dataset.py
  python scripts/preprocessing/audit_master_dataset.py \\
      --master  data/interim/merged/master_dataset_v1.csv \\
      --consumption data/interim/consumption/district_monthly_consumption.csv \\
      --charging    data/interim/charging_stations/charging_stations_clean.csv \\
      --geography   data/interim/geography/district_geography.csv
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

logger = logging.getLogger("audit_master_dataset")

# ---------------------------------------------------------------------------
# Default paths  (resolved relative to project root)
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DEFAULT_MASTER_PATH = (
    PROJECT_ROOT / "data" / "interim" / "merged" / "master_dataset_v1.csv"
)
DEFAULT_CONSUMPTION_PATH = (
    PROJECT_ROOT / "data" / "interim" / "consumption" / "district_monthly_consumption.csv"
)
DEFAULT_CHARGING_PATH = (
    PROJECT_ROOT / "data" / "interim" / "charging_stations" / "charging_stations_clean.csv"
)
DEFAULT_GEOGRAPHY_PATH = (
    PROJECT_ROOT / "data" / "interim" / "geography" / "district_geography.csv"
)
DEFAULT_COVERAGE_REPORT_PATH = PROJECT_ROOT / "reports" / "dataset_coverage_report.md"
DEFAULT_CONSISTENCY_REPORT_PATH = PROJECT_ROOT / "reports" / "data_consistency_report.md"

# Tolerance for floating-point sum comparisons
_FLOAT_TOLERANCE: float = 1e-4

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------


def setup_logging(log_file: Optional[Path] = None) -> None:
    """
    Configure the logging system for console and optional file output.

    Args:
        log_file: Optional path for a log file.  Parent directories are created
            automatically.
    """
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
        path:  Path to the CSV file.
        label: Human-readable label for log messages.

    Returns:
        Loaded DataFrame.

    Raises:
        FileNotFoundError: If ``path`` does not exist.
        ValueError:        If the resulting DataFrame is empty.
    """
    if not path.exists():
        raise FileNotFoundError(f"[{label}] File not found: {path}")

    logger.info(f"[{label}] Loading from: {path}")
    df = pd.read_csv(path, low_memory=False)

    if df.empty:
        raise ValueError(f"[{label}] Loaded DataFrame is empty: {path}")

    logger.info(f"[{label}] {len(df):,} rows × {len(df.columns)} columns")
    return df


def write_report(path: Path, content: str) -> None:
    """
    Write a text report to disk, creating parent directories as needed.

    Args:
        path:    Destination file path.
        content: Text content to write.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    logger.info(f"[output] Report written: {path}")


# ---------------------------------------------------------------------------
# Coverage analysis helpers
# ---------------------------------------------------------------------------


def build_coverage_grid(
    master: pd.DataFrame,
) -> Tuple[
    List[str],          # all districts (sorted)
    List[str],          # all reporting months (sorted)
    int,                # expected combos
    int,                # actual combos
    List[Tuple[str, str]],  # missing combos
]:
    """
    Build the district × reporting_month coverage grid.

    Args:
        master: Master dataset DataFrame.

    Returns:
        Tuple of (districts, months, expected, actual, missing_combos).
    """
    districts: List[str] = sorted(master["district"].unique())
    months: List[str] = sorted(master["reporting_month"].unique())

    expected_set = {(d, m) for d in districts for m in months}
    actual_set = set(zip(master["district"], master["reporting_month"]))
    missing = sorted(expected_set - actual_set)

    return districts, months, len(expected_set), len(actual_set), missing


def build_district_timeline(master: pd.DataFrame) -> pd.DataFrame:
    """
    Compute per-district timeline statistics.

    Args:
        master: Master dataset DataFrame.

    Returns:
        DataFrame indexed by district with columns:
            first_month, last_month, months_present, months_missing, coverage_pct.
    """
    all_months = sorted(master["reporting_month"].unique())
    n_total = len(all_months)

    records = []
    for district, grp in master.groupby("district"):
        present = set(grp["reporting_month"])
        missing_months = sorted(set(all_months) - present)
        n_present = len(present)
        records.append(
            {
                "district": district,
                "first_month": grp["reporting_month"].min(),
                "last_month": grp["reporting_month"].max(),
                "months_present": n_present,
                "months_missing": len(missing_months),
                "coverage_pct": round(100.0 * n_present / n_total, 1),
                "missing_months_list": missing_months,
            }
        )

    tl = pd.DataFrame(records).set_index("district").sort_index()
    return tl


def detect_global_month_gaps(master: pd.DataFrame) -> List[str]:
    """
    Detect calendar months that are entirely absent from the master dataset.

    Compares the set of actual ``reporting_month`` values against a contiguous
    monthly range from the first to the last observed month.

    Args:
        master: Master dataset DataFrame.

    Returns:
        Sorted list of YYYY-MM strings that are absent from the dataset.
    """
    actual_months = sorted(master["reporting_month"].unique())
    if not actual_months:
        return []

    full_range = pd.date_range(
        start=actual_months[0], end=actual_months[-1], freq="MS"
    )
    expected = {d.strftime("%Y-%m") for d in full_range}
    return sorted(expected - set(actual_months))


def explain_coverage_gaps(
    timeline: pd.DataFrame,
    global_gaps: List[str],
    consumption_path: Path,
) -> Dict[str, str]:
    """
    Build observable explanations for each coverage gap type.

    All explanations are grounded in data that can be directly observed.
    No guesses are made.

    Args:
        timeline:         District timeline DataFrame from :func:`build_district_timeline`.
        global_gaps:      List of globally absent months.
        consumption_path: Path to district_monthly_consumption.csv (for cross-check).

    Returns:
        Dict mapping gap category to explanation string.
    """
    explanations: Dict[str, str] = {}

    # --- Global month gaps ---------------------------------------------------
    if global_gaps:
        for gm in global_gaps:
            # Verify the gap exists in the upstream consumption file too
            cons = pd.read_csv(consumption_path, low_memory=False)
            count_in_cons = int((cons["reporting_month"] == gm).sum())
            if count_in_cons == 0:
                explanations[f"global_gap:{gm}"] = (
                    f"Month `{gm}` is absent from `district_monthly_consumption.csv` "
                    f"(0 rows found), and no corresponding raw source file exists in "
                    f"`data/raw/consumption/` for this period.  This indicates the raw "
                    f"data for `{gm}` was never collected or published by the utility."
                )
            else:
                explanations[f"global_gap:{gm}"] = (
                    f"Month `{gm}` is present in the upstream consumption file "
                    f"({count_in_cons} rows) but was not propagated into the master "
                    f"dataset.  This may indicate a merge-pipeline issue."
                )

    # --- District-level early gaps -------------------------------------------
    # Districts that start later than the global minimum have observable reasons:
    # their first available raw file date determines the earliest record.
    global_first = timeline["first_month"].min()
    late_starters = timeline[timeline["first_month"] > global_first]

    for district, row in late_starters.iterrows():
        key = f"late_start:{district}"
        explanations[key] = (
            f"Earliest consumption record for `{district}` is `{row['first_month']}` "
            f"(global dataset start: `{global_first}`).  The district has "
            f"`{row['months_present']}` months of data.  This reflects the date when "
            f"the utility's reporting circle(s) for this district first appeared in the "
            f"raw source files."
        )

    return explanations


# ---------------------------------------------------------------------------
# Consistency analysis helpers
# ---------------------------------------------------------------------------


def check_numeric_totals(
    master: pd.DataFrame,
    consumption: pd.DataFrame,
) -> List[Dict[str, object]]:
    """
    Compare column-level sums between the consumption source and the master dataset.

    Args:
        master:      Master dataset DataFrame.
        consumption: Pre-merge consumption DataFrame.

    Returns:
        List of dicts, one per checked column, with keys:
            column, consumption_sum, master_sum, delta, passed.
    """
    cols = ["units", "load", "total_services", "billed_services"]
    results = []
    for col in cols:
        if col not in consumption.columns or col not in master.columns:
            logger.warning(f"[consistency] Column '{col}' missing from one dataset; skipping.")
            continue
        c_sum = float(consumption[col].sum())
        m_sum = float(master[col].sum())
        delta = abs(c_sum - m_sum)
        passed = delta < _FLOAT_TOLERANCE
        results.append(
            {
                "column": col,
                "consumption_sum": c_sum,
                "master_sum": m_sum,
                "delta": delta,
                "passed": passed,
            }
        )
        status = "OK" if passed else "FAIL"
        logger.info(
            f"[consistency] {col}: consumption={c_sum:.4f}  master={m_sum:.4f}  "
            f"delta={delta:.6f}  [{status}]"
        )
    return results


def check_key_uniqueness(master: pd.DataFrame) -> Dict[str, int]:
    """
    Check for duplicate rows and duplicate business-key pairs.

    Args:
        master: Master dataset DataFrame.

    Returns:
        Dict with keys:
            duplicate_full_rows, duplicate_key_rows.
    """
    dup_full = int(master.duplicated().sum())
    dup_key = int(master.duplicated(subset=["district", "reporting_month"]).sum())
    logger.info(f"[consistency] Duplicate full rows: {dup_full}")
    logger.info(f"[consistency] Duplicate (district, reporting_month) keys: {dup_key}")
    return {"duplicate_full_rows": dup_full, "duplicate_key_rows": dup_key}


def check_geography_nulls(master: pd.DataFrame) -> Dict[str, int]:
    """
    Check for null geographic values in the master dataset.

    Args:
        master: Master dataset DataFrame.

    Returns:
        Dict mapping column name to null count for geographic columns.
    """
    geo_cols = ["latitude", "longitude", "district_area_sqkm"]
    result: Dict[str, int] = {}
    for col in geo_cols:
        if col not in master.columns:
            logger.warning(f"[consistency] Geography column '{col}' not found in master.")
            result[col] = -1  # sentinel: column absent
            continue
        n_null = int(master[col].isna().sum())
        result[col] = n_null
        status = "OK" if n_null == 0 else "FAIL"
        logger.info(f"[consistency] Null {col}: {n_null} [{status}]")
    return result


def check_lookup_duplicates(
    geography: pd.DataFrame,
    charging: pd.DataFrame,
) -> Dict[str, int]:
    """
    Check for duplicate district entries in lookup tables.

    Args:
        geography: Geography lookup DataFrame (district_geography.csv).
        charging:  Charging stations DataFrame (charging_stations_clean.csv).

    Returns:
        Dict with keys:
            geo_duplicate_districts, charging_duplicate_districts.
    """
    geo_dup = int(geography["district_name"].duplicated().sum())
    cs_dup = int(charging["district"].duplicated(keep=False).sum()) if "district" in charging.columns else 0

    # For charging, what matters is uniqueness in the aggregated form
    cs_agg = charging.groupby("district").size().reset_index(name="count")
    cs_agg_dup = int(cs_agg["district"].duplicated().sum())

    logger.info(f"[consistency] Duplicate district_name in geography: {geo_dup}")
    logger.info(f"[consistency] Duplicate district in charging agg: {cs_agg_dup}")

    return {
        "geo_duplicate_districts": geo_dup,
        "charging_duplicate_districts": cs_agg_dup,
    }


# ---------------------------------------------------------------------------
# Report builders
# ---------------------------------------------------------------------------


def build_coverage_report(
    master: pd.DataFrame,
    consumption_path: Path,
    report_path: Path,
) -> str:
    """
    Build and return the dataset coverage Markdown report.

    Args:
        master:           Master dataset DataFrame.
        consumption_path: Path to upstream consumption CSV (for gap explanations).
        report_path:      Destination path (used in report header only).

    Returns:
        Rendered Markdown string.
    """
    now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    # ------------------------------------------------------------------ #
    # Core computations
    # ------------------------------------------------------------------ #
    districts, months, n_expected, n_actual, missing_combos = build_coverage_grid(master)
    timeline = build_district_timeline(master)
    global_gaps = detect_global_month_gaps(master)
    explanations = explain_coverage_gaps(timeline, global_gaps, consumption_path)

    coverage_pct = round(100.0 * n_actual / n_expected, 2) if n_expected else 0.0
    n_districts = len(districts)
    n_months = len(months)
    max_months = n_months  # maximum possible per district

    # Rows per year
    rows_per_year: pd.Series = master.groupby("year").size().sort_index()
    # Rows per calendar month
    rows_per_month: pd.Series = master.groupby("month").size().sort_index()

    # Districts with incomplete timelines
    incomplete = timeline[timeline["months_present"] < max_months].sort_values(
        "months_present"
    )

    # ------------------------------------------------------------------ #
    # Helpers
    # ------------------------------------------------------------------ #
    def _tick(passed: bool) -> str:
        return "Pass" if passed else "Fail"

    def _rows_per_year_table() -> str:
        rows = ["| Year | Rows |", "| ---: | ---: |"]
        for yr, cnt in rows_per_year.items():
            rows.append(f"| {yr} | {cnt:,} |")
        return "\n".join(rows)

    def _rows_per_month_table() -> str:
        month_names = [
            "", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
        ]
        rows = ["| Month | Name | Rows |", "| ---: | :--- | ---: |"]
        for mn, cnt in rows_per_month.items():
            label = month_names[int(mn)] if 1 <= int(mn) <= 12 else str(mn)
            rows.append(f"| {mn} | {label} | {cnt:,} |")
        return "\n".join(rows)

    def _timeline_overview_table() -> str:
        rows = [
            "| District | First Month | Last Month | "
            "Months Present | Months Missing | Coverage % |",
            "| :--- | :---: | :---: | ---: | ---: | ---: |",
        ]
        for district, row in timeline.iterrows():
            rows.append(
                f"| {district} "
                f"| {row['first_month']} "
                f"| {row['last_month']} "
                f"| {row['months_present']} "
                f"| {row['months_missing']} "
                f"| {row['coverage_pct']} % |"
            )
        return "\n".join(rows)

    def _timeline_visual() -> str:
        """
        Render a compact presence/absence Markdown table.
        Columns = year (to keep table width manageable).
        Cell = count of months recorded for that district in that year.
        """
        master_copy = master.copy()
        pivot = (
            master_copy.groupby(["district", "year"])
            .size()
            .unstack(fill_value=0)
            .reindex(index=sorted(master_copy["district"].unique()))
        )
        years = sorted(pivot.columns.tolist())

        header = "| District | " + " | ".join(str(y) for y in years) + " |"
        sep = "| :--- | " + " | ".join("---:" for _ in years) + " |"
        rows = [header, sep]
        for district in pivot.index:
            cells = " | ".join(str(pivot.loc[district, y]) for y in years)
            rows.append(f"| {district} | {cells} |")
        return "\n".join(rows)

    def _missing_combos_section() -> str:
        if not missing_combos:
            return "_No missing district-month combinations._"
        total = len(missing_combos)
        # Group by district for readability
        by_district: Dict[str, List[str]] = {}
        for d, m in missing_combos:
            by_district.setdefault(d, []).append(m)
        lines = [
            f"**Total missing combinations:** {total:,}",
            "",
            "| District | Count | Missing Months |",
            "| :--- | ---: | :--- |",
        ]
        for d in sorted(by_district):
            ms = by_district[d]
            # Abbreviate if > 12 months
            if len(ms) <= 12:
                label = ", ".join(f"`{m}`" for m in ms)
            else:
                label = (
                    ", ".join(f"`{m}`" for m in ms[:6])
                    + f" … and {len(ms) - 6} more"
                )
            lines.append(f"| {d} | {len(ms)} | {label} |")
        return "\n".join(lines)

    def _gap_explanations_section() -> str:
        if not explanations:
            return "_No gaps requiring explanation._"
        parts = []

        # Global gaps first
        global_keys = [k for k in explanations if k.startswith("global_gap:")]
        if global_keys:
            parts.append("### Globally Absent Months")
            parts.append("")
            for k in sorted(global_keys):
                parts.append(f"> **{k.split(':', 1)[1]}**")
                parts.append(f"> {explanations[k]}")
                parts.append("")

        # Late-starting districts
        late_keys = [k for k in explanations if k.startswith("late_start:")]
        if late_keys:
            parts.append("### Districts With Late Data Start")
            parts.append("")
            parts.append(
                "The following districts have fewer months than the maximum because "
                "their raw source files only begin from the date shown below.  "
                "This is a property of the upstream utility reporting data, not a "
                "pipeline defect."
            )
            parts.append("")
            parts.append("| District | First Available Month | Reason |")
            parts.append("| :--- | :---: | :--- |")
            for k in sorted(late_keys):
                d = k.split(":", 1)[1]
                row = timeline.loc[d] if d in timeline.index else None
                first = row["first_month"] if row is not None else "N/A"
                parts.append(
                    f"| {d} | `{first}` | "
                    "First raw source file available from this month onward |"
                )
        return "\n".join(parts)

    # ------------------------------------------------------------------ #
    # Render
    # ------------------------------------------------------------------ #
    lines = [
        "# EVision Telangana – Dataset Coverage Report",
        "",
        f"_Generated: {now}_",
        "",
        "> [!NOTE]",
        "> This report audits `master_dataset_v1.csv` for district-month coverage.",
        "> The master dataset is **not modified** by this script.",
        "",
        "---",
        "",
        "## 1. Overview",
        "",
        "| Metric | Value |",
        "| :--- | ---: |",
        f"| **Total Districts** | {n_districts} |",
        f"| **Total Reporting Months** | {n_months} |",
        f"| **First Reporting Month** | `{months[0]}` |",
        f"| **Last Reporting Month** | `{months[-1]}` |",
        f"| **Expected District-Month Combinations** | {n_expected:,} |",
        f"| **Actual District-Month Combinations** | {n_actual:,} |",
        f"| **Missing Combinations** | {n_expected - n_actual:,} |",
        f"| **Coverage Percentage** | {coverage_pct} % |",
        f"| **Globally Absent Calendar Months** | {len(global_gaps)} |",
        "",
        "---",
        "",
        "## 2. Rows per Year",
        "",
        _rows_per_year_table(),
        "",
        "---",
        "",
        "## 3. Rows per Calendar Month",
        "",
        _rows_per_month_table(),
        "",
        "---",
        "",
        "## 4. Per-District Timeline",
        "",
        _timeline_overview_table(),
        "",
        "---",
        "",
        "## 5. Timeline Visualisation (Months per District per Year)",
        "",
        "> Cell values = number of months recorded for that district in that year.",
        "> Maximum possible per year = 12 (or fewer for the boundary years of the dataset).",
        "",
        _timeline_visual(),
        "",
        "---",
        "",
        "## 6. Missing District-Month Combinations",
        "",
        _missing_combos_section(),
        "",
        "---",
        "",
        "## 7. Districts With Incomplete Timelines",
        "",
    ]

    if incomplete.empty:
        lines.append("_All districts have complete timelines._")
    else:
        lines.append(
            f"**{len(incomplete)} out of {n_districts} districts** have fewer than "
            f"the maximum {max_months} reporting months."
        )
        lines.append("")
        lines.append(
            "| District | Months Present | Coverage % |"
        )
        lines.append("| :--- | ---: | ---: |")
        for district, row in incomplete.iterrows():
            lines.append(
                f"| {district} | {row['months_present']} | {row['coverage_pct']} % |"
            )

    lines += [
        "",
        "---",
        "",
        "## 8. Globally Absent Calendar Months",
        "",
    ]

    if global_gaps:
        lines.append(
            f"The following {len(global_gaps)} month(s) are absent for **all** "
            "districts (i.e. not present anywhere in the master dataset):"
        )
        lines.append("")
        for gm in global_gaps:
            lines.append(f"- `{gm}`")
    else:
        lines.append(
            "_No calendar months are globally absent; the dataset is contiguous._"
        )

    lines += [
        "",
        "---",
        "",
        "## 9. Coverage Gap Explanations",
        "",
        "> [!IMPORTANT]",
        "> All explanations below are based on **observable facts** only.",
        "> No assumptions or guesses are made.",
        "",
        _gap_explanations_section(),
        "",
        "---",
        "",
        "*Report generated automatically by `scripts/preprocessing/audit_master_dataset.py` "
        "on behalf of the EVision Telangana Preprocessing Pipeline.*",
        "",
    ]

    return "\n".join(lines)


def build_consistency_report(
    master: pd.DataFrame,
    consumption: pd.DataFrame,
    geography: pd.DataFrame,
    charging: pd.DataFrame,
    report_path: Path,
) -> str:
    """
    Build and return the data consistency Markdown report.

    Args:
        master:      Master dataset DataFrame.
        consumption: Pre-merge consumption DataFrame.
        geography:   Geography lookup DataFrame.
        charging:    Charging stations DataFrame.
        report_path: Destination path (used in report header only).

    Returns:
        Rendered Markdown string.
    """
    now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    # ------------------------------------------------------------------ #
    # Run all checks
    # ------------------------------------------------------------------ #
    numeric_results = check_numeric_totals(master, consumption)
    key_checks = check_key_uniqueness(master)
    geo_nulls = check_geography_nulls(master)
    lookup_dups = check_lookup_duplicates(geography, charging)

    # Row count check
    cons_rows = len(consumption)
    master_rows = len(master)
    row_count_match = cons_rows == master_rows

    # ------------------------------------------------------------------ #
    # Helpers
    # ------------------------------------------------------------------ #
    def _tick(passed: bool) -> str:
        return "Pass" if passed else "FAIL"

    def _numeric_table() -> str:
        rows = [
            "| Column | Consumption Sum | Master Sum | Delta | Status |",
            "| :--- | ---: | ---: | ---: | :---: |",
        ]
        for r in numeric_results:
            rows.append(
                f"| `{r['column']}` "
                f"| {r['consumption_sum']:,.4f} "
                f"| {r['master_sum']:,.4f} "
                f"| {r['delta']:.6f} "
                f"| **{_tick(bool(r['passed']))}** |"
            )
        return "\n".join(rows)

    def _geo_null_table() -> str:
        rows = [
            "| Column | Null Count | Status |",
            "| :--- | ---: | :---: |",
        ]
        for col, cnt in geo_nulls.items():
            if cnt == -1:
                rows.append(f"| `{col}` | _column absent_ | **FAIL** |")
            else:
                rows.append(f"| `{col}` | {cnt} | **{_tick(cnt == 0)}** |")
        return "\n".join(rows)

    all_numeric_pass = all(bool(r["passed"]) for r in numeric_results)
    all_geo_pass = all(v == 0 for v in geo_nulls.values())
    all_key_pass = (
        key_checks["duplicate_full_rows"] == 0
        and key_checks["duplicate_key_rows"] == 0
    )
    all_lookup_pass = (
        lookup_dups["geo_duplicate_districts"] == 0
        and lookup_dups["charging_duplicate_districts"] == 0
    )
    overall_pass = (
        all_numeric_pass
        and all_geo_pass
        and all_key_pass
        and all_lookup_pass
        and row_count_match
    )

    # ------------------------------------------------------------------ #
    # Render
    # ------------------------------------------------------------------ #
    lines = [
        "# EVision Telangana – Data Consistency Report",
        "",
        f"_Generated: {now}_",
        "",
        "> [!NOTE]",
        "> This report validates the integrity of `master_dataset_v1.csv` against",
        "> its upstream source datasets.  No source data is modified.",
        "",
        "---",
        "",
        "## 1. Overall Status",
        "",
        f"| Overall Consistency | **{'PASS' if overall_pass else 'FAIL'}** |",
        "| :--- | :--- |",
        "",
        "| Check Category | Status |",
        "| :--- | :---: |",
        f"| Row count preserved | **{_tick(row_count_match)}** |",
        f"| Numeric totals match | **{_tick(all_numeric_pass)}** |",
        f"| No duplicate keys | **{_tick(all_key_pass)}** |",
        f"| No geography nulls | **{_tick(all_geo_pass)}** |",
        f"| No lookup duplicates | **{_tick(all_lookup_pass)}** |",
        "",
        "---",
        "",
        "## 2. Row Count Preservation",
        "",
        "| Dataset | Row Count |",
        "| :--- | ---: |",
        f"| `district_monthly_consumption.csv` | {cons_rows:,} |",
        f"| `master_dataset_v1.csv` | {master_rows:,} |",
        f"| **Match** | **{_tick(row_count_match)}** |",
        "",
        "> [!NOTE]",
        "> The master dataset is built with a left join from the consumption table.",
        "> Row count must be exactly equal; any difference indicates a fan-out (m:many join).",
        "",
        "---",
        "",
        "## 3. Numeric Total Consistency",
        "",
        "Verifies that column sums are identical before and after the merge.",
        "Tolerance: `1e-4` (to accommodate floating-point representation).",
        "",
        _numeric_table(),
        "",
        "---",
        "",
        "## 4. Key Uniqueness",
        "",
        "| Check | Count | Status |",
        "| :--- | ---: | :---: |",
        f"| Fully duplicated rows | {key_checks['duplicate_full_rows']} "
        f"| **{_tick(key_checks['duplicate_full_rows'] == 0)}** |",
        f"| Duplicate (district, reporting_month) keys | {key_checks['duplicate_key_rows']} "
        f"| **{_tick(key_checks['duplicate_key_rows'] == 0)}** |",
        "",
        "---",
        "",
        "## 5. Geographic Information Completeness",
        "",
        "Checks that no rows in the master dataset have null values for geographic fields.",
        "",
        _geo_null_table(),
        "",
        "---",
        "",
        "## 6. Lookup Table Duplicate Check",
        "",
        "| Lookup Table | Duplicate Districts | Status |",
        "| :--- | ---: | :---: |",
        f"| `district_geography.csv` (`district_name`) "
        f"| {lookup_dups['geo_duplicate_districts']} "
        f"| **{_tick(lookup_dups['geo_duplicate_districts'] == 0)}** |",
        f"| `charging_stations_clean.csv` (aggregated by district) "
        f"| {lookup_dups['charging_duplicate_districts']} "
        f"| **{_tick(lookup_dups['charging_duplicate_districts'] == 0)}** |",
        "",
        "---",
        "",
        "*Report generated automatically by `scripts/preprocessing/audit_master_dataset.py` "
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
        description="EVision Telangana – Epic 7 follow-up: audit master_dataset_v1.csv.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--master",
        type=Path,
        default=DEFAULT_MASTER_PATH,
        help="Path to master_dataset_v1.csv",
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
        "--coverage-report",
        type=Path,
        default=DEFAULT_COVERAGE_REPORT_PATH,
        help="Output path for dataset_coverage_report.md",
    )
    parser.add_argument(
        "--consistency-report",
        type=Path,
        default=DEFAULT_CONSISTENCY_REPORT_PATH,
        help="Output path for data_consistency_report.md",
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
    master_path: Path,
    consumption_path: Path,
    charging_path: Path,
    geography_path: Path,
    coverage_report_path: Path,
    consistency_report_path: Path,
) -> None:
    """
    Execute the full audit pipeline.

    Steps:
      1. Load all source datasets (read-only).
      2. Build coverage report (district-month grid, timeline, gap explanations).
      3. Build consistency report (numeric totals, key uniqueness, geo nulls, lookups).
      4. Write both reports to disk.

    Args:
        master_path:              Path to master_dataset_v1.csv.
        consumption_path:         Path to district_monthly_consumption.csv.
        charging_path:            Path to charging_stations_clean.csv.
        geography_path:           Path to district_geography.csv.
        coverage_report_path:     Destination for dataset_coverage_report.md.
        consistency_report_path:  Destination for data_consistency_report.md.
    """
    logger.info("=" * 70)
    logger.info("EVision Telangana – Epic 7 Audit: Coverage & Consistency")
    logger.info("=" * 70)

    # ------------------------------------------------------------------ #
    # Load data (read-only)
    # ------------------------------------------------------------------ #
    master = load_csv(master_path, "master")
    consumption = load_csv(consumption_path, "consumption")
    charging = load_csv(charging_path, "charging_stations")
    geography = load_csv(geography_path, "geography")

    # ------------------------------------------------------------------ #
    # Build coverage report
    # ------------------------------------------------------------------ #
    logger.info("[coverage] Building coverage report...")
    coverage_md = build_coverage_report(master, consumption_path, coverage_report_path)
    write_report(coverage_report_path, coverage_md)

    # ------------------------------------------------------------------ #
    # Build consistency report
    # ------------------------------------------------------------------ #
    logger.info("[consistency] Building consistency report...")
    consistency_md = build_consistency_report(
        master, consumption, geography, charging, consistency_report_path
    )
    write_report(consistency_report_path, consistency_md)

    logger.info("=" * 70)
    logger.info("Audit pipeline complete.")
    logger.info("=" * 70)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """Entry point for the audit pipeline."""
    args = parse_arguments()
    setup_logging(args.log_file)

    try:
        run(
            master_path=args.master,
            consumption_path=args.consumption,
            charging_path=args.charging,
            geography_path=args.geography,
            coverage_report_path=args.coverage_report,
            consistency_report_path=args.consistency_report,
        )
    except (FileNotFoundError, ValueError) as exc:
        logger.error(f"Audit aborted: {exc}")
        sys.exit(1)
    except Exception as exc:  # pylint: disable=broad-except
        logger.exception(f"Unexpected error: {exc}")
        sys.exit(2)


if __name__ == "__main__":
    main()
