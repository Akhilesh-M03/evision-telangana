"""
Temporal feature engineering for EVision Telangana – Epic 8.

All features in this module are derived purely from the ``reporting_month``
(YYYY-MM) and ``year`` / ``month`` integer columns that are already present in
the master dataset.  No future information is used; every value is a deterministic
function of the calendar position of the observation.

Features generated
------------------
quarter         : Calendar quarter (1–4).
season          : Meteorological season for the Telangana context
                  (Summer / Monsoon / Post-Monsoon / Winter).
month_name      : Full English month name (January … December).
year_index      : 0-based index of the year relative to the first year in the
                  dataset.  Useful as a monotone time regressor.
month_of_year   : Alias for ``month`` (1–12); kept for explicitness.
is_first_month  : Binary flag – 1 if this is the first calendar month in the
                  dataset for the given district, else 0.
is_last_month   : Binary flag – 1 if this is the last calendar month in the
                  dataset for the given district, else 0.

Notes
-----
The DataFrame **must** be sorted by (district, reporting_month) before calling
:func:`add_temporal_features`.  The pipeline enforces this sort order upstream.
"""

import logging
from typing import List

import pandas as pd

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Internal constants
# ---------------------------------------------------------------------------

_MONTH_NAMES: List[str] = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

# Telangana meteorological seasons (month → season).
# Summer : March–May (hot & dry pre-monsoon)
# Monsoon : June–September
# Post-Monsoon : October–November
# Winter : December–February
_MONTH_TO_SEASON = {
    1: "Winter",
    2: "Winter",
    3: "Summer",
    4: "Summer",
    5: "Summer",
    6: "Monsoon",
    7: "Monsoon",
    8: "Monsoon",
    9: "Monsoon",
    10: "Post-Monsoon",
    11: "Post-Monsoon",
    12: "Winter",
}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def add_temporal_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Derive calendar and temporal index features from existing date columns.

    The function is **non-destructive**: it returns a new DataFrame that
    includes all original columns plus the derived temporal columns.

    Parameters
    ----------
    df : pd.DataFrame
        Must contain ``month`` (int 1–12) and ``year`` (int) columns.
        Must be pre-sorted by (district, reporting_month).

    Returns
    -------
    pd.DataFrame
        Original DataFrame with the following additional columns:

        - ``quarter``       int (1–4)
        - ``season``        str
        - ``month_name``    str
        - ``year_index``    int (0-based)
        - ``month_of_year`` int (1–12, alias for month)
        - ``is_first_month`` int (0 or 1)
        - ``is_last_month``  int (0 or 1)

    Raises
    ------
    KeyError
        If ``month`` or ``year`` columns are absent.
    ValueError
        If any month value falls outside 1–12.
    """
    if "month" not in df.columns or "year" not in df.columns:
        raise KeyError("DataFrame must contain 'month' and 'year' columns.")

    invalid_months = df["month"][~df["month"].between(1, 12)]
    if not invalid_months.empty:
        raise ValueError(
            f"Invalid month values detected: {sorted(invalid_months.unique())}"
        )

    result = df.copy()

    # --- quarter -------------------------------------------------------
    result["quarter"] = ((result["month"] - 1) // 3 + 1).astype(int)

    # --- season --------------------------------------------------------
    result["season"] = result["month"].map(_MONTH_TO_SEASON)

    # --- month_name ----------------------------------------------------
    result["month_name"] = result["month"].map(
        lambda m: _MONTH_NAMES[m - 1]
    )

    # --- year_index ----------------------------------------------------
    min_year = int(result["year"].min())
    result["year_index"] = (result["year"] - min_year).astype(int)

    # --- month_of_year -------------------------------------------------
    result["month_of_year"] = result["month"].astype(int)

    # --- is_first_month / is_last_month --------------------------------
    # First and last observation *per district* in chronological order.
    first_idx = result.groupby("district")["reporting_month"].transform("min")
    last_idx = result.groupby("district")["reporting_month"].transform("max")

    result["is_first_month"] = (result["reporting_month"] == first_idx).astype(int)
    result["is_last_month"] = (result["reporting_month"] == last_idx).astype(int)

    logger.info(
        "Temporal features added: quarter, season, month_name, year_index, "
        "month_of_year, is_first_month, is_last_month"
    )
    return result
