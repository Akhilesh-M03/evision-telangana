"""
Growth feature engineering for EVision Telangana – Epic 8.

Computes month-on-month growth rates and cumulative aggregates per district.
All growth features use **strictly historical data** (t − 1 or earlier),
preventing any form of data leakage.

Features generated (per district, sorted by reporting_month)
------------------------------------------------------------
monthly_growth_rate  : Percentage change in ``units`` from the previous month:
                       100 × (units_t − units_{t-1}) / units_{t-1}.
                       NaN if previous month is missing or zero.
                       Clamped to avoid ±inf (see implementation notes below).
monthly_load_growth  : Percentage change in ``load`` from the previous month.
                       Same conventions as monthly_growth_rate.
cumulative_units     : Running total of ``units`` for the district, up to
                       and including month *t-1* (historical cumulative sum).
cumulative_load      : Running total of ``load`` for the district, same logic.

Implementation notes
--------------------
- ``monthly_growth_rate`` and ``monthly_load_growth`` use ``shift(1)``
  on the current group to reference the immediately preceding observation.
- Infinite growth rates (caused by 0 → non-zero transitions) are replaced
  with NaN to prevent downstream model instability.
- Negative growth rates are valid (e.g. consumption declined).
- Cumulative sums are strictly historical (using shift(1).cumsum()) and
  are therefore suitable as "total volume to date" features without target leakage.
"""

import logging

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _safe_pct_change(series: pd.Series) -> pd.Series:
    """
    Compute percentage change from the previous element without ±inf.

    Parameters
    ----------
    series : pd.Series (float)
        Values to compute percentage change for, within a single district's
        sorted time series.

    Returns
    -------
    pd.Series (float)
        100 × (x_t − x_{t-1}) / x_{t-1}, with NaN where the denominator is
        zero or the previous value is missing, and ±inf replaced by NaN.
    """
    prev = series.shift(1).astype(float)
    with np.errstate(divide="ignore", invalid="ignore"):
        pct = np.where(
            (prev == 0) | prev.isna(),
            np.nan,
            100.0 * (series.astype(float) - prev) / prev,
        )
    result = pd.Series(pct, index=series.index, dtype=float)
    return result.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def add_growth_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add per-district growth rate and cumulative sum features.

    Parameters
    ----------
    df : pd.DataFrame
        Must contain:

        - ``district``        (str)   – district identifier
        - ``reporting_month`` (str, YYYY-MM) – chronological sort key
        - ``units``           (float) – monthly electricity units consumed
        - ``load``            (float) – monthly connected load

        The DataFrame **must** be sorted by (district, reporting_month).

    Returns
    -------
    pd.DataFrame
        Original DataFrame extended with:

        - ``monthly_growth_rate`` float  (%, NaN-safe)
        - ``monthly_load_growth`` float  (%, NaN-safe)
        - ``cumulative_units``    float
        - ``cumulative_load``     float

    Raises
    ------
    KeyError
        If any required column is missing.
    """
    required = {"district", "reporting_month", "units", "load"}
    missing = required - set(df.columns)
    if missing:
        raise KeyError(f"Missing required columns for growth features: {missing}")

    result = df.copy()

    growth_cols = [
        "monthly_growth_rate",
        "monthly_load_growth",
        "cumulative_units",
        "cumulative_load",
    ]
    for col in growth_cols:
        result[col] = np.nan

    for district, group_idx in result.groupby("district").groups.items():
        group = result.loc[group_idx].copy()

        if not group["reporting_month"].is_monotonic_increasing:
            logger.warning(
                "District '%s': reporting_month not monotone within group; sorting.",
                district,
            )
            group = group.sort_values("reporting_month")

        units = group["units"].astype(float)
        load = group["load"].astype(float)

        group["monthly_growth_rate"] = _safe_pct_change(units)
        group["monthly_load_growth"] = _safe_pct_change(load)
        group["cumulative_units"] = units.shift(1).cumsum()
        group["cumulative_load"] = load.shift(1).cumsum()

        result.loc[group_idx, growth_cols] = group[growth_cols].values

    # Sanity check: no inf values should remain
    for col in ["monthly_growth_rate", "monthly_load_growth"]:
        n_inf = int(np.isinf(result[col].fillna(0)).sum())
        if n_inf > 0:
            logger.error(
                "Column '%s' still contains %d infinite value(s) after safe division. "
                "Replacing with NaN.", col, n_inf
            )
            result[col] = result[col].replace([np.inf, -np.inf], np.nan)

    logger.info(
        "Growth features added: monthly_growth_rate, monthly_load_growth, "
        "cumulative_units, cumulative_load"
    )
    return result
