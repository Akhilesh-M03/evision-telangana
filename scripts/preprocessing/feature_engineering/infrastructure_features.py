"""
Infrastructure feature engineering for EVision Telangana – Epic 8.

Computes density and per-station ratios that express how EV-charging
infrastructure is distributed relative to the geographic footprint of a
district and to its electricity consumption.

Features generated
------------------
stations_per_sqkm   : Charging station density (stations / km²).
units_per_station   : Average electricity units consumed per charging station.
load_per_station    : Average connected load (kVA/kW) per charging station.
services_per_station: Average number of services (connections) per charging
                      station.

All divide-by-zero cases are handled by returning ``NaN`` via
``pandas.NA``-compatible safe division.  No sentinel values (e.g. 0 or −1)
are introduced because downstream validation and ML pipelines can reason
about ``NaN`` explicitly.

Notes
-----
These features are computed row-wise; no temporal ordering or grouping is
required.  However, the DataFrame should already be sorted by
(district, reporting_month) for consistency with upstream stages.
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
        Dividend series (float or int).
    denominator : pd.Series
        Divisor series (float or int).

    Returns
    -------
    pd.Series
        Float series with NaN where ``denominator == 0`` or the result is
        infinite.
    """
    with np.errstate(divide="ignore", invalid="ignore"):
        result = np.where(
            denominator == 0,
            np.nan,
            numerator / denominator,
        )
    series = pd.Series(result, index=numerator.index, dtype=float)
    # Belt-and-suspenders: replace any stray infinities
    series = series.replace([np.inf, -np.inf], np.nan)
    return series


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def add_infrastructure_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute EV infrastructure density and per-station capacity features.

    Parameters
    ----------
    df : pd.DataFrame
        Must contain the following columns:

        - ``charging_station_count`` (numeric) – number of charging stations
        - ``district_area_sqkm``     (numeric) – district area in km²
        - ``units``                  (numeric) – monthly electricity units
        - ``load``                   (numeric) – monthly connected load
        - ``total_services``         (numeric) – total electricity services

    Returns
    -------
    pd.DataFrame
        Original DataFrame with the following additional columns:

        - ``stations_per_sqkm``    float – charging station density
        - ``units_per_station``    float – electricity intensity per station
        - ``load_per_station``     float – load intensity per station
        - ``services_per_station`` float – services per station

    Raises
    ------
    KeyError
        If any required source column is missing.
    """
    required = {
        "charging_station_count",
        "district_area_sqkm",
        "units",
        "load",
        "total_services",
    }
    missing = required - set(df.columns)
    if missing:
        raise KeyError(f"Missing required columns for infrastructure features: {missing}")

    result = df.copy()

    stations = result["charging_station_count"].astype(float)
    area = result["district_area_sqkm"].astype(float)
    units = result["units"].astype(float)
    load = result["load"].astype(float)
    services = result["total_services"].astype(float)

    result["stations_per_sqkm"] = _safe_divide(stations, area)
    result["units_per_station"] = _safe_divide(units, stations)
    result["load_per_station"] = _safe_divide(load, stations)
    result["services_per_station"] = _safe_divide(services, stations)

    _log_zero_station_rows(result, stations)

    logger.info(
        "Infrastructure features added: stations_per_sqkm, units_per_station, "
        "load_per_station, services_per_station"
    )
    return result


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _log_zero_station_rows(df: pd.DataFrame, stations: pd.Series) -> None:
    """Emit a warning for rows where charging_station_count is zero."""
    zero_mask = stations == 0
    n_zero = int(zero_mask.sum())
    if n_zero > 0:
        affected_districts = sorted(df.loc[zero_mask, "district"].unique())
        logger.warning(
            "%d row(s) have zero charging stations; per-station ratios will be NaN "
            "for those rows.  Affected districts: %s",
            n_zero,
            affected_districts,
        )
