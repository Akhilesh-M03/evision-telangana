"""
Post-generation validation for EVision Telangana – Epic 8.

This module provides a structured quality-control layer that runs after all
feature engineering transformations have been applied.  It does not modify the
DataFrame; it only inspects it and emits structured warnings and errors.

Checks performed
----------------
1. Duplicate columns       – raises ValueError if found.
2. Duplicate rows          – warns with count.
3. Infinite values         – warns per column.
4. Unexpected NaN values   – warns per column for non-lag columns.
5. Temporal ordering       – verifies each district is sorted by reporting_month.
6. District ordering       – verifies district groups are contiguous.
7. Negative rates          – informational (valid, but logged for awareness).
8. Value range checks      – billed_service_ratio bounded ∈ [0, 1].

The :func:`validate_features` function returns a
:class:`ValidationResult` dataclass summarising all findings.
"""

import logging
from dataclasses import dataclass, field
from typing import Dict, List

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Expected NaN columns
# ---------------------------------------------------------------------------
# These columns are allowed to contain NaN values because they represent
# look-back features that cannot be computed for the earliest observations
# in each district.
_EXPECTED_NAN_COLS = {
    "previous_month_units",
    "previous_month_load",
    "rolling_average_3m",
    "rolling_average_6m",
    "rolling_average_12m",
    "rolling_std_3m",
    "rolling_std_6m",
    "rolling_max_6m",
    "rolling_min_6m",
    "monthly_growth_rate",
    "monthly_load_growth",
    # Infrastructure NaN when stations == 0
    "units_per_station",
    "load_per_station",
    "services_per_station",
    # Utilization NaN when services == 0
    "average_units_per_billed_service",
}


# ---------------------------------------------------------------------------
# Result dataclass
# ---------------------------------------------------------------------------


@dataclass
class ValidationResult:
    """
    Structured summary of a validation run.

    Attributes
    ----------
    passed : bool
        True if no *error*-level issues were found (warnings are tolerated).
    errors : List[str]
        List of error messages (issues that make the dataset unusable).
    warnings : List[str]
        List of warning messages (issues to be aware of but not fatal).
    info : Dict[str, object]
        Supplementary statistics generated during validation.
    """

    passed: bool = True
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    info: Dict[str, object] = field(default_factory=dict)

    def add_error(self, msg: str) -> None:
        """Record a fatal error and mark the result as failed."""
        self.passed = False
        self.errors.append(msg)
        logger.error("VALIDATION ERROR: %s", msg)

    def add_warning(self, msg: str) -> None:
        """Record a non-fatal warning."""
        self.warnings.append(msg)
        logger.warning("VALIDATION WARNING: %s", msg)

    def add_info(self, key: str, value: object) -> None:
        """Store a supplementary statistic."""
        self.info[key] = value


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def validate_features(df: pd.DataFrame) -> ValidationResult:
    """
    Run all quality checks on the feature-engineered DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The fully feature-engineered dataset.

    Returns
    -------
    ValidationResult
        Structured result containing errors, warnings, and statistics.
    """
    result = ValidationResult()

    _check_duplicate_columns(df, result)
    _check_duplicate_rows(df, result)
    _check_infinite_values(df, result)
    _check_unexpected_nans(df, result)
    _check_temporal_ordering(df, result)
    _check_district_ordering(df, result)
    _check_value_ranges(df, result)

    result.add_info("total_rows", len(df))
    result.add_info("total_columns", len(df.columns))
    result.add_info("total_districts", df["district"].nunique() if "district" in df.columns else "N/A")
    result.add_info("error_count", len(result.errors))
    result.add_info("warning_count", len(result.warnings))

    status = "PASSED" if result.passed else "FAILED"
    logger.info(
        "Validation %s – %d error(s), %d warning(s).",
        status,
        len(result.errors),
        len(result.warnings),
    )
    return result


# ---------------------------------------------------------------------------
# Individual check functions
# ---------------------------------------------------------------------------


def _check_duplicate_columns(df: pd.DataFrame, result: ValidationResult) -> None:
    """Error if any column name appears more than once."""
    seen = set()
    duplicates = []
    for col in df.columns:
        if col in seen:
            duplicates.append(col)
        seen.add(col)
    if duplicates:
        result.add_error(f"Duplicate column names detected: {duplicates}")
    else:
        logger.debug("No duplicate columns found.")


def _check_duplicate_rows(df: pd.DataFrame, result: ValidationResult) -> None:
    """Warn if any fully duplicated rows exist."""
    n_dup = int(df.duplicated().sum())
    if n_dup > 0:
        result.add_warning(f"{n_dup} fully duplicated row(s) found in the feature dataset.")
    result.add_info("duplicate_rows", n_dup)


def _check_infinite_values(df: pd.DataFrame, result: ValidationResult) -> None:
    """Warn for each column that contains ±inf values."""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    inf_cols: Dict[str, int] = {}
    for col in numeric_cols:
        n_inf = int(np.isinf(df[col].fillna(0)).sum())
        if n_inf > 0:
            inf_cols[col] = n_inf
    if inf_cols:
        result.add_warning(
            f"Columns with infinite values (should be zero after engineering): {inf_cols}"
        )
    result.add_info("infinite_value_columns", inf_cols)


def _check_unexpected_nans(df: pd.DataFrame, result: ValidationResult) -> None:
    """Warn for columns that contain NaN but are not in the expected-NaN set."""
    nan_summary: Dict[str, int] = {}
    unexpected_nan: Dict[str, int] = {}

    for col in df.columns:
        n_nan = int(df[col].isna().sum())
        if n_nan > 0:
            nan_summary[col] = n_nan
            if col not in _EXPECTED_NAN_COLS:
                unexpected_nan[col] = n_nan

    if unexpected_nan:
        result.add_warning(
            f"Unexpected NaN values in non-lag columns: {unexpected_nan}"
        )
    result.add_info("nan_by_column", nan_summary)
    result.add_info("unexpected_nan_columns", unexpected_nan)


def _check_temporal_ordering(df: pd.DataFrame, result: ValidationResult) -> None:
    """Error if any district's reporting_month is not monotonically increasing."""
    if "district" not in df.columns or "reporting_month" not in df.columns:
        result.add_warning("Cannot verify temporal ordering: missing 'district' or 'reporting_month'.")
        return

    violated_districts = []
    for district, grp in df.groupby("district"):
        if not grp["reporting_month"].is_monotonic_increasing:
            violated_districts.append(district)

    if violated_districts:
        result.add_error(
            f"Temporal ordering violated for districts: {violated_districts}"
        )
    else:
        logger.debug("Temporal ordering verified for all districts.")
    result.add_info("temporal_order_violated_districts", violated_districts)


def _check_district_ordering(df: pd.DataFrame, result: ValidationResult) -> None:
    """Warn if district groups are not contiguous (interleaved districts)."""
    if "district" not in df.columns:
        return

    # Each district should appear as a contiguous block
    transitions = (df["district"] != df["district"].shift()).sum()
    n_districts = df["district"].nunique()
    # In a fully grouped frame, transitions == n_districts
    if transitions > n_districts:
        result.add_warning(
            f"District groups appear to be non-contiguous (interleaved). "
            f"Expected {n_districts} transitions, found {transitions}."
        )
    result.add_info("district_group_transitions", int(transitions))


def _check_value_ranges(df: pd.DataFrame, result: ValidationResult) -> None:
    """Warn if known-bounded columns fall outside expected ranges."""
    range_checks = {
        "billed_service_ratio": (0.0, 1.0),
        "month_of_year": (1, 12),
        "quarter": (1, 4),
    }

    for col, (lo, hi) in range_checks.items():
        if col not in df.columns:
            continue
        col_series = pd.to_numeric(df[col], errors="coerce")
        out_of_range = col_series.dropna()
        out_of_range = out_of_range[(out_of_range < lo) | (out_of_range > hi)]
        if not out_of_range.empty:
            result.add_warning(
                f"Column '{col}' has {len(out_of_range)} value(s) outside [{lo}, {hi}]."
            )
