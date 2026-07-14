"""
Rolling-window feature engineering for EVision Telangana – Epic 8.

All rolling features use **strictly historical data only** – i.e., the
computation at time *t* uses observations up to and including *t − 1* (lag
features) or *t − 1* through *t − k* (rolling windows).  This is enforced via
``pd.DataFrame.shift(1)`` before applying any window function, ensuring zero
data leakage.

Features generated (per district, sorted by reporting_month)
------------------------------------------------------------
previous_month_units    : Units consumed in the immediately preceding month.
previous_month_load     : Load in the immediately preceding month.
rolling_average_3m      : 3-month trailing mean of units (months t-3 to t-1).
rolling_average_6m      : 6-month trailing mean of units.
rolling_average_12m     : 12-month trailing mean of units.
rolling_std_3m          : 3-month trailing standard deviation of units.
rolling_std_6m          : 6-month trailing standard deviation of units.
rolling_max_6m          : 6-month trailing maximum of units.
rolling_min_6m          : 6-month trailing minimum of units.

NaN values appear naturally where insufficient history exists (e.g. the first
observation in a district will have NaN for all rolling features).  This is
intentional and expected; downstream ML pipelines may impute or mask as needed.

Design notes
------------
- The DataFrame **must** be sorted by (district, reporting_month) before
  calling :func:`add_rolling_features`.
- Window parameters are passed as named constants so they can be adjusted
  without touching the computation logic.
- ``min_periods=1`` is intentionally NOT used for rolling calculations to
  avoid producing deceptively precise statistics from a single data point.
  Instead ``min_periods`` is set to the full window size, producing NaN for
  partial windows.  The only exception is ``rolling_average_*``, for which
  ``min_periods=1`` is used to maximise coverage (documented below).
"""

import logging
from typing import List

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Window size constants
# ---------------------------------------------------------------------------

WINDOW_3M: int = 3
WINDOW_6M: int = 6
WINDOW_12M: int = 12


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def add_rolling_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add per-district lag and rolling-window features to the DataFrame.

    The function groups by ``district``, processes each group independently
    (preserving temporal ordering), and reassembles the result while
    retaining the original row index.

    Parameters
    ----------
    df : pd.DataFrame
        Must contain:

        - ``district``         (str) – district identifier
        - ``reporting_month``  (str, YYYY-MM) – chronological sort key
        - ``units``            (float) – monthly electricity units consumed
        - ``load``             (float) – monthly connected load

        The DataFrame **must** be sorted by (district, reporting_month)
        before this function is called.

    Returns
    -------
    pd.DataFrame
        Original DataFrame extended with:

        - ``previous_month_units``  float
        - ``previous_month_load``   float
        - ``rolling_average_3m``    float
        - ``rolling_average_6m``    float
        - ``rolling_average_12m``   float
        - ``rolling_std_3m``        float
        - ``rolling_std_6m``        float
        - ``rolling_max_6m``        float
        - ``rolling_min_6m``        float

    Raises
    ------
    KeyError
        If any required column is missing.
    """
    required = {"district", "reporting_month", "units", "load"}
    missing = required - set(df.columns)
    if missing:
        raise KeyError(f"Missing required columns for rolling features: {missing}")

    result = df.copy()

    # Initialise output columns as NaN (float64)
    rolling_cols: List[str] = [
        "previous_month_units",
        "previous_month_load",
        "rolling_average_3m",
        "rolling_average_6m",
        "rolling_average_12m",
        "rolling_std_3m",
        "rolling_std_6m",
        "rolling_max_6m",
        "rolling_min_6m",
    ]
    for col in rolling_cols:
        result[col] = np.nan

    # Process each district independently to prevent cross-district leakage
    for district, group_idx in result.groupby("district").groups.items():
        group = result.loc[group_idx].copy()

        # Verify temporal order within the group
        if not group["reporting_month"].is_monotonic_increasing:
            logger.warning(
                "District '%s' is not sorted by reporting_month within its group. "
                "Sorting now.", district
            )
            group = group.sort_values("reporting_month")

        units = group["units"].astype(float)
        load = group["load"].astype(float)

        # ---- Lag features (shift(1) = strictly historical) ----------------
        group["previous_month_units"] = units.shift(1)
        group["previous_month_load"] = load.shift(1)

        # ---- Shifted series for rolling windows ---------------------------
        # Shift by 1 so that rolling(window) at position t covers [t-w, t-1].
        units_shifted = units.shift(1)

        # Rolling averages – min_periods=1 so partial windows are still useful
        # for the first few observations where history is limited.
        group["rolling_average_3m"] = (
            units_shifted
            .rolling(window=WINDOW_3M, min_periods=1)
            .mean()
        )
        group["rolling_average_6m"] = (
            units_shifted
            .rolling(window=WINDOW_6M, min_periods=1)
            .mean()
        )
        group["rolling_average_12m"] = (
            units_shifted
            .rolling(window=WINDOW_12M, min_periods=1)
            .mean()
        )

        # Rolling std – require full window to avoid misleading single-point std
        group["rolling_std_3m"] = (
            units_shifted
            .rolling(window=WINDOW_3M, min_periods=WINDOW_3M)
            .std()
        )
        group["rolling_std_6m"] = (
            units_shifted
            .rolling(window=WINDOW_6M, min_periods=WINDOW_6M)
            .std()
        )

        # Rolling max / min – require full window for meaningful range statistics
        group["rolling_max_6m"] = (
            units_shifted
            .rolling(window=WINDOW_6M, min_periods=WINDOW_6M)
            .max()
        )
        group["rolling_min_6m"] = (
            units_shifted
            .rolling(window=WINDOW_6M, min_periods=WINDOW_6M)
            .min()
        )

        # Write back into the result DataFrame preserving original index
        result.loc[group_idx, rolling_cols] = group[rolling_cols].values

    nan_counts = result[rolling_cols].isna().sum()
    logger.info("Rolling features added. NaN counts: %s", nan_counts.to_dict())
    return result
