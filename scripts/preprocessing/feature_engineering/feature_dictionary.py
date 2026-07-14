"""
Feature dictionary for EVision Telangana – Epic 8.

Provides structured metadata (a *data dictionary*) for every engineered
feature.  Each entry is a :class:`FeatureEntry` dataclass describing the
feature's origin, formula, data type, and intended usage.

The dictionary serves three purposes:

1. **Documentation** – generated as ``data/processed/feature_dictionary.csv``
   so that analysts and ML engineers understand every column.

2. **ML column selection** – the ``used_by`` field controls which features are
   included in ``ml_training_dataset.csv``.  Features marked
   ``used_by="exclude"`` are descriptive or non-numeric and are dropped from
   the ML dataset.

3. **Extensibility** – future contributors add entries to :data:`FEATURE_ENTRIES`
   when introducing new feature modules.  No other file needs to change.

Schema of feature_dictionary.csv
----------------------------------
feature_name   : Exact column name in the output datasets.
category       : Feature group (temporal / infrastructure / utilization /
                 rolling / growth / source).
description    : Human-readable explanation of the feature.
formula        : Symbolic formula or rule used to derive the feature.
input_columns  : Comma-separated list of source columns used.
output_type    : Pandas dtype description (int, float, str/object).
used_by        : Comma-separated list of consumers (ml / analytics /
                 exclude).  "exclude" means NOT suitable for ML numerics.
"""

from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import List

import pandas as pd


# ---------------------------------------------------------------------------
# Dataclass
# ---------------------------------------------------------------------------


@dataclass
class FeatureEntry:
    """Metadata record for a single engineered feature."""

    feature_name: str
    category: str
    description: str
    formula: str
    input_columns: str        # comma-separated source column names
    output_type: str
    used_by: str              # comma-separated: ml, analytics, exclude


# ---------------------------------------------------------------------------
# Feature registry
# ---------------------------------------------------------------------------

FEATURE_ENTRIES: List[FeatureEntry] = [
    # ------------------------------------------------------------------
    # SOURCE COLUMNS (pass-through, not engineered)
    # ------------------------------------------------------------------
    FeatureEntry(
        feature_name="district",
        category="source",
        description="District name (canonical spelling from geography dataset).",
        formula="pass-through",
        input_columns="district",
        output_type="str",
        used_by="analytics, exclude",
    ),
    FeatureEntry(
        feature_name="year",
        category="source",
        description="Calendar year of the observation.",
        formula="pass-through",
        input_columns="year",
        output_type="int",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="month",
        category="source",
        description="Calendar month number (1–12).",
        formula="pass-through",
        input_columns="month",
        output_type="int",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="reporting_month",
        category="source",
        description="Reporting period in YYYY-MM format.",
        formula="pass-through",
        input_columns="reporting_month",
        output_type="str",
        used_by="analytics, exclude",
    ),
    FeatureEntry(
        feature_name="units",
        category="source",
        description="Total electricity units consumed in the district-month (MWh or kWh).",
        formula="pass-through",
        input_columns="units",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="load",
        category="source",
        description="Total connected load in the district-month (kVA or kW).",
        formula="pass-through",
        input_columns="load",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="total_services",
        category="source",
        description="Total number of electricity service connections in the district.",
        formula="pass-through",
        input_columns="total_services",
        output_type="int",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="billed_services",
        category="source",
        description="Number of service connections that received a bill in this month.",
        formula="pass-through",
        input_columns="billed_services",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="circle_count",
        category="source",
        description="Number of DISCOMS circles present in the district.",
        formula="pass-through",
        input_columns="circle_count",
        output_type="int",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="division_count",
        category="source",
        description="Number of DISCOMS divisions present in the district.",
        formula="pass-through",
        input_columns="division_count",
        output_type="int",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="subdivision_count",
        category="source",
        description="Number of DISCOMS subdivisions present in the district.",
        formula="pass-through",
        input_columns="subdivision_count",
        output_type="int",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="charging_station_count",
        category="source",
        description="Number of EV charging stations registered in the district.",
        formula="pass-through",
        input_columns="charging_station_count",
        output_type="int",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="latitude",
        category="source",
        description="Approximate latitude of the district centroid.",
        formula="pass-through",
        input_columns="latitude",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="longitude",
        category="source",
        description="Approximate longitude of the district centroid.",
        formula="pass-through",
        input_columns="longitude",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="district_area_sqkm",
        category="source",
        description="Geographic area of the district in square kilometres.",
        formula="pass-through",
        input_columns="district_area_sqkm",
        output_type="float",
        used_by="ml, analytics",
    ),
    # ------------------------------------------------------------------
    # TEMPORAL FEATURES
    # ------------------------------------------------------------------
    FeatureEntry(
        feature_name="quarter",
        category="temporal",
        description="Calendar quarter of the observation (Q1=Jan-Mar, Q2=Apr-Jun, "
                    "Q3=Jul-Sep, Q4=Oct-Dec).",
        formula="ceil(month / 3)",
        input_columns="month",
        output_type="int",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="season",
        category="temporal",
        description="Telangana meteorological season: Summer (Mar-May), Monsoon (Jun-Sep), "
                    "Post-Monsoon (Oct-Nov), Winter (Dec-Feb).",
        formula="lookup(month, season_map)",
        input_columns="month",
        output_type="str",
        used_by="analytics, exclude",
    ),
    FeatureEntry(
        feature_name="month_name",
        category="temporal",
        description="Full English month name derived from the month number.",
        formula="lookup(month, month_names)",
        input_columns="month",
        output_type="str",
        used_by="analytics, exclude",
    ),
    FeatureEntry(
        feature_name="year_index",
        category="temporal",
        description="Zero-based year index relative to the earliest year in the dataset. "
                    "Acts as a monotone linear time regressor.",
        formula="year - min(year)",
        input_columns="year",
        output_type="int",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="month_of_year",
        category="temporal",
        description="Month number (1–12), explicit alias of the source 'month' column for "
                    "clarity in feature selection.",
        formula="month",
        input_columns="month",
        output_type="int",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="is_first_month",
        category="temporal",
        description="Binary flag: 1 if this row is the earliest reporting_month for the "
                    "district, else 0.",
        formula="1 if reporting_month == min(reporting_month) per district else 0",
        input_columns="district, reporting_month",
        output_type="int",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="is_last_month",
        category="temporal",
        description="Binary flag: 1 if this row is the latest reporting_month for the "
                    "district, else 0.",
        formula="1 if reporting_month == max(reporting_month) per district else 0",
        input_columns="district, reporting_month",
        output_type="int",
        used_by="ml, analytics",
    ),
    # ------------------------------------------------------------------
    # INFRASTRUCTURE FEATURES
    # ------------------------------------------------------------------
    FeatureEntry(
        feature_name="stations_per_sqkm",
        category="infrastructure",
        description="EV charging station density: number of charging stations per square "
                    "kilometre of district area.",
        formula="charging_station_count / district_area_sqkm",
        input_columns="charging_station_count, district_area_sqkm",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="units_per_station",
        category="infrastructure",
        description="Electricity intensity per charging station: monthly units consumed "
                    "divided by number of charging stations. NaN if stations == 0.",
        formula="units / charging_station_count",
        input_columns="units, charging_station_count",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="load_per_station",
        category="infrastructure",
        description="Connected load per charging station (kVA/station). "
                    "NaN if stations == 0.",
        formula="load / charging_station_count",
        input_columns="load, charging_station_count",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="services_per_station",
        category="infrastructure",
        description="Number of service connections per charging station. "
                    "NaN if stations == 0.",
        formula="total_services / charging_station_count",
        input_columns="total_services, charging_station_count",
        output_type="float",
        used_by="ml, analytics",
    ),
    # ------------------------------------------------------------------
    # UTILIZATION FEATURES
    # ------------------------------------------------------------------
    FeatureEntry(
        feature_name="billed_service_ratio",
        category="utilization",
        description="Fraction of total services that were billed in the reporting month "
                    "(0–1). NaN if total_services == 0.",
        formula="billed_services / total_services",
        input_columns="billed_services, total_services",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="average_units_per_service",
        category="utilization",
        description="Average electricity units consumed per total service connection. "
                    "NaN if total_services == 0.",
        formula="units / total_services",
        input_columns="units, total_services",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="average_load_per_service",
        category="utilization",
        description="Average connected load per total service connection (kVA). "
                    "NaN if total_services == 0.",
        formula="load / total_services",
        input_columns="load, total_services",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="average_units_per_billed_service",
        category="utilization",
        description="Average electricity units consumed per *billed* service connection. "
                    "NaN if billed_services == 0.",
        formula="units / billed_services",
        input_columns="units, billed_services",
        output_type="float",
        used_by="ml, analytics",
    ),
    # ------------------------------------------------------------------
    # ROLLING FEATURES
    # ------------------------------------------------------------------
    FeatureEntry(
        feature_name="previous_month_units",
        category="rolling",
        description="Electricity units from the immediately preceding month for the same "
                    "district (lag-1). NaN for the first observation per district.",
        formula="units.shift(1) per district",
        input_columns="district, reporting_month, units",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="previous_month_load",
        category="rolling",
        description="Connected load from the immediately preceding month for the same "
                    "district (lag-1). NaN for the first observation per district.",
        formula="load.shift(1) per district",
        input_columns="district, reporting_month, load",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="rolling_average_3m",
        category="rolling",
        description="3-month trailing mean of units for the district, computed over the "
                    "3 months preceding the current month (t-3 to t-1). Historical only.",
        formula="mean(units.shift(1), window=3, min_periods=1) per district",
        input_columns="district, reporting_month, units",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="rolling_average_6m",
        category="rolling",
        description="6-month trailing mean of units for the district (t-6 to t-1). "
                    "Historical only.",
        formula="mean(units.shift(1), window=6, min_periods=1) per district",
        input_columns="district, reporting_month, units",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="rolling_average_12m",
        category="rolling",
        description="12-month trailing mean of units for the district (t-12 to t-1). "
                    "Historical only.",
        formula="mean(units.shift(1), window=12, min_periods=1) per district",
        input_columns="district, reporting_month, units",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="rolling_std_3m",
        category="rolling",
        description="3-month trailing standard deviation of units (t-3 to t-1). "
                    "NaN if fewer than 3 prior observations exist for the district.",
        formula="std(units.shift(1), window=3, min_periods=3) per district",
        input_columns="district, reporting_month, units",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="rolling_std_6m",
        category="rolling",
        description="6-month trailing standard deviation of units (t-6 to t-1). "
                    "NaN if fewer than 6 prior observations exist for the district.",
        formula="std(units.shift(1), window=6, min_periods=6) per district",
        input_columns="district, reporting_month, units",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="rolling_max_6m",
        category="rolling",
        description="6-month trailing maximum of units (t-6 to t-1). "
                    "NaN if fewer than 6 prior observations exist for the district.",
        formula="max(units.shift(1), window=6, min_periods=6) per district",
        input_columns="district, reporting_month, units",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="rolling_min_6m",
        category="rolling",
        description="6-month trailing minimum of units (t-6 to t-1). "
                    "NaN if fewer than 6 prior observations exist for the district.",
        formula="min(units.shift(1), window=6, min_periods=6) per district",
        input_columns="district, reporting_month, units",
        output_type="float",
        used_by="ml, analytics",
    ),
    # ------------------------------------------------------------------
    # GROWTH FEATURES
    # ------------------------------------------------------------------
    FeatureEntry(
        feature_name="monthly_growth_rate",
        category="growth",
        description="Month-on-month percentage change in electricity units for the "
                    "district: 100 × (units_t − units_{t-1}) / units_{t-1}. "
                    "NaN for the first observation or when previous month units == 0.",
        formula="100 * (units - units.shift(1)) / units.shift(1) per district",
        input_columns="district, reporting_month, units",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="monthly_load_growth",
        category="growth",
        description="Month-on-month percentage change in connected load for the district. "
                    "NaN for the first observation or when previous month load == 0.",
        formula="100 * (load - load.shift(1)) / load.shift(1) per district",
        input_columns="district, reporting_month, load",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="cumulative_units",
        category="growth",
        description="Running total of electricity units consumed by the district from "
                    "its first observation up to and including the current month.",
        formula="cumsum(units) per district",
        input_columns="district, reporting_month, units",
        output_type="float",
        used_by="ml, analytics",
    ),
    FeatureEntry(
        feature_name="cumulative_load",
        category="growth",
        description="Running total of connected load for the district from its first "
                    "observation up to and including the current month.",
        formula="cumsum(load) per district",
        input_columns="district, reporting_month, load",
        output_type="float",
        used_by="ml, analytics",
    ),
]


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def build_feature_dictionary() -> pd.DataFrame:
    """
    Convert the feature registry into a tidy DataFrame.

    Returns
    -------
    pd.DataFrame
        Columns: feature_name, category, description, formula,
                 input_columns, output_type, used_by.
    """
    records = [asdict(entry) for entry in FEATURE_ENTRIES]
    return pd.DataFrame(records)


def save_feature_dictionary(output_path: Path) -> pd.DataFrame:
    """
    Build the feature dictionary and write it to a CSV file.

    Parameters
    ----------
    output_path : Path
        Destination CSV path (including filename).

    Returns
    -------
    pd.DataFrame
        The dictionary DataFrame that was written.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df = build_feature_dictionary()
    df.to_csv(output_path, index=False, encoding="utf-8")
    return df


def get_ml_columns(df: pd.DataFrame) -> List[str]:
    """
    Return the list of column names that are suitable for ML training.

    A column is included if:
    - It exists in ``df``, AND
    - Its ``used_by`` field in the feature dictionary contains ``"ml"``, AND
    - Its ``output_type`` is numeric (``int`` or ``float``).

    Parameters
    ----------
    df : pd.DataFrame
        The fully feature-engineered dataset.

    Returns
    -------
    List[str]
        Ordered list of ML-ready column names.
    """
    ml_entries = [
        e for e in FEATURE_ENTRIES
        if "ml" in e.used_by and e.output_type in ("int", "float")
    ]
    available = set(df.columns)
    return [e.feature_name for e in ml_entries if e.feature_name in available]
