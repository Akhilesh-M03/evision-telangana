"""
Utilization feature engineering for EVision Telangana – Epic 8.

Generates ratios that describe how efficiently electricity services are
utilized within each district-month record.

Features generated
------------------
billed_service_ratio        : Fraction of services that were actually billed
                              (billed_services / total_services).
average_units_per_service   : Electricity units per total service
                              (units / total_services).
average_load_per_service    : Load per total service
                              (load / total_services).
average_units_per_billed_service : Electricity units per *billed* service
                              (units / billed_services).

All divide-by-zero cases produce NaN via safe division.  No sentinel values
are introduced.

Notes
-----
These are row-wise, stateless features.  The input DataFrame is assumed to
be pre-sorted by (district, reporting_month) for consistency.
"""

import logging

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _safe_divide(numerator: pd.Series, denominator: pd.Series) -> pd.Series:
    """
    Element-wise division that replaces division-by-zero and ±inf with NaN.

    Parameters
    ----------
    numerator : pd.Series
    denominator : pd.Series

    Returns
    -------
    pd.Series (float)
    """
    with np.errstate(divide="ignore", invalid="ignore"):
        result = np.where(
            denominator == 0,
            np.nan,
            numerator / denominator,
        )
    series = pd.Series(result, index=numerator.index, dtype=float)
    return series.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def add_utilization_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute service utilization and efficiency ratio features.

    Parameters
    ----------
    df : pd.DataFrame
        Must contain:

        - ``units``            (numeric) – monthly electricity units consumed
        - ``load``             (numeric) – monthly connected load (kVA/kW)
        - ``total_services``   (numeric) – total number of service connections
        - ``billed_services``  (numeric) – number of billed service connections

    Returns
    -------
    pd.DataFrame
        Original DataFrame extended with:

        - ``billed_service_ratio``            float ∈ [0, 1]
        - ``average_units_per_service``       float ≥ 0
        - ``average_load_per_service``        float ≥ 0
        - ``average_units_per_billed_service`` float ≥ 0

    Raises
    ------
    KeyError
        If any required source column is missing.
    """
    required = {"units", "load", "total_services", "billed_services"}
    missing = required - set(df.columns)
    if missing:
        raise KeyError(f"Missing required columns for utilization features: {missing}")

    result = df.copy()

    units = result["units"].astype(float)
    load = result["load"].astype(float)
    total = result["total_services"].astype(float)
    billed = result["billed_services"].astype(float)

    result["billed_service_ratio"] = _safe_divide(billed, total)
    result["average_units_per_service"] = _safe_divide(units, total)
    result["average_load_per_service"] = _safe_divide(load, total)
    result["average_units_per_billed_service"] = _safe_divide(units, billed)

    _warn_zero_services(result, total, billed)

    logger.info(
        "Utilization features added: billed_service_ratio, "
        "average_units_per_service, average_load_per_service, "
        "average_units_per_billed_service"
    )
    return result


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _warn_zero_services(
    df: pd.DataFrame,
    total: pd.Series,
    billed: pd.Series,
) -> None:
    """Emit warnings for rows where services denominators are zero."""
    zero_total = int((total == 0).sum())
    zero_billed = int((billed == 0).sum())
    if zero_total > 0:
        logger.warning(
            "%d row(s) have total_services == 0; per-service ratios will be NaN.",
            zero_total,
        )
    if zero_billed > 0:
        logger.warning(
            "%d row(s) have billed_services == 0; "
            "average_units_per_billed_service will be NaN.",
            zero_billed,
        )
