# EVision Telangana – Feature Engineering Report

_Generated: 2026-07-14 02:31:38 UTC_

---

## 1. Engineered Feature Count

| Metric | Value |
| :--- | ---: |
| **Source Columns (pass-through)** | 15 |
| **Engineered Features** | 28 |
| **Total Features in master_dataset.csv** | 43 |
| **Features in ml_training_dataset.csv** | 39 |

---

## 2. Feature Categories

| Category | Feature Count |
| :--- | ---: |
| Growth | 4 |
| Infrastructure | 4 |
| Rolling | 9 |
| Temporal | 7 |
| Utilization | 4 |

---

## 3. Validation Summary

**Status:** ✅ PASSED

### Errors

_No errors._

### Warnings

_No warnings._

---

## 4. NaN Value Summary by Column

> [!NOTE]
> NaN values in rolling and growth feature columns are expected and intentional.
> They arise from the first observation(s) in each district where no historical
> data exists.  Infrastructure and utilization NaNs arise from zero denominators.

| Column | NaN Count |
| :--- | ---: |
| `rolling_std_6m` | 186 |
| `rolling_max_6m` | 186 |
| `rolling_min_6m` | 186 |
| `monthly_growth_rate` | 98 |
| `rolling_std_3m` | 96 |
| `units_per_station` | 56 |
| `load_per_station` | 56 |
| `services_per_station` | 56 |
| `previous_month_units` | 32 |
| `previous_month_load` | 32 |
| `rolling_average_3m` | 32 |
| `rolling_average_6m` | 32 |
| `rolling_average_12m` | 32 |
| `monthly_load_growth` | 32 |
| `average_units_per_billed_service` | 12 |

---

## 5. Output Schema

### master_dataset.csv  (1245 rows × 43 columns)

| Column | Dtype | NaN Count |
| :--- | :--- | ---: |
| `district` | `object` | 0 |
| `year` | `int64` | 0 |
| `month` | `int64` | 0 |
| `reporting_month` | `object` | 0 |
| `units` | `float64` | 0 |
| `load` | `float64` | 0 |
| `total_services` | `int64` | 0 |
| `billed_services` | `float64` | 0 |
| `circle_count` | `int64` | 0 |
| `division_count` | `int64` | 0 |
| `subdivision_count` | `int64` | 0 |
| `charging_station_count` | `int64` | 0 |
| `latitude` | `float64` | 0 |
| `longitude` | `float64` | 0 |
| `district_area_sqkm` | `float64` | 0 |
| `quarter` | `int64` | 0 |
| `season` | `object` | 0 |
| `month_name` | `object` | 0 |
| `year_index` | `int64` | 0 |
| `month_of_year` | `int64` | 0 |
| `is_first_month` | `int64` | 0 |
| `is_last_month` | `int64` | 0 |
| `stations_per_sqkm` | `float64` | 0 |
| `units_per_station` | `float64` | 56 |
| `load_per_station` | `float64` | 56 |
| `services_per_station` | `float64` | 56 |
| `billed_service_ratio` | `float64` | 0 |
| `average_units_per_service` | `float64` | 0 |
| `average_load_per_service` | `float64` | 0 |
| `average_units_per_billed_service` | `float64` | 12 |
| `previous_month_units` | `float64` | 32 |
| `previous_month_load` | `float64` | 32 |
| `rolling_average_3m` | `float64` | 32 |
| `rolling_average_6m` | `float64` | 32 |
| `rolling_average_12m` | `float64` | 32 |
| `rolling_std_3m` | `float64` | 96 |
| `rolling_std_6m` | `float64` | 186 |
| `rolling_max_6m` | `float64` | 186 |
| `rolling_min_6m` | `float64` | 186 |
| `monthly_growth_rate` | `float64` | 98 |
| `monthly_load_growth` | `float64` | 32 |
| `cumulative_units` | `float64` | 0 |
| `cumulative_load` | `float64` | 0 |

---

## 6. Processing Statistics

| Metric | Value |
| :--- | ---: |
| **Input File** | `master_dataset_v1.csv` |
| **Total Rows** | 1,245 |
| **Total Districts** | 32 |
| **Date Range** | 2021-06 → 2026-06 |
| **Source Columns** | 15 |
| **Total Output Columns** | 43 |

---

## 7. Features Excluded from ML Training Dataset

The following **engineered** features are excluded from `ml_training_dataset.csv`
because they are string/categorical and require encoding before ML use,
or because they are purely descriptive.

| Feature | Category | Reason |
| :--- | :--- | :--- |
| `season` | Temporal | Telangana meteorological season: Summer (Mar-May), Monsoon (… |
| `month_name` | Temporal | Full English month name derived from the month number. |

### Source Columns Excluded from ML

| Feature | Reason |
| :--- | :--- |
| `district` | District name (canonical spelling from geography dataset). |
| `reporting_month` | Reporting period in YYYY-MM format. |

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
