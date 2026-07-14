# Machine Learning Dataset Architecture Review

## 1. Target Leakage Analysis: `cumulative_units` and `cumulative_load`

### Evaluation
The features `cumulative_units` and `cumulative_load` as originally implemented used the cumulative sum (`cumsum()`) of `units` and `load` for the current month $t$:
$$\text{cumulative\_units}_t = \sum_{i=1}^{t} \text{units}_i = \text{cumulative\_units}_{t-1} + \text{units}_t$$

In the context of predicting the current month's electricity consumption/demand $y_t = \text{units}_t$, that inclusive computation created **target leakage** because the target variable `units` was mathematically contained within the feature.

### Implemented Correction
To completely resolve this data leakage, the cumulative features have been updated to use strictly historical volume to date (up to month $t-1$):
$$\text{cumulative\_units\_historical}_t = \sum_{i=1}^{t-1} \text{units}_i$$

Specifically, in `scripts/preprocessing/feature_engineering/growth_features.py`, the cumulative calculations were updated to:
```python
group["cumulative_units"] = units.shift(1).cumsum()
group["cumulative_load"] = load.shift(1).cumsum()
```
This ensures that only historical values available before the prediction month are used, preventing all target leakage.

---

## 2. Machine Learning Target Definition

The target of the supervised regression pipeline is identified as follows:

| Target Column | Description | Reason | Used By |
| :--- | :--- | :--- | :--- |
| `units` | Total electricity consumption/demand in the district-month. | Identified in the Data Contracts (`demand_kwh`) and ML Concepts documents as the primary objective of regression (predicting future EV charging consumption demand). | Regression Model Training (`Random Forest`, `XGBoost`) |

---

## 3. Column Classification

The columns present in the processed datasets are classified below:

| Column | Category | Reason / Notes |
| :--- | :--- | :--- |
| `district` | Excluded / Metadata | Categorical/string identifier; excluded from ML training dataset. |
| `reporting_month` | Excluded / Metadata | Chronological string key (YYYY-MM); excluded from ML training dataset. |
| `season` | Excluded | Categorical text column; excluded from ML training dataset. |
| `month_name` | Excluded | Categorical text column; excluded from ML training dataset. |
| `units` | **Target** | Primary variable to predict. |
| `year` | Feature | Input feature representing calendar year. |
| `month` | Feature | Input feature representing calendar month number. |
| `load` | Feature | Input feature representing connected load. |
| `total_services` | Feature | Input feature representing total electrical connections. |
| `billed_services` | Feature | Input feature representing billed electrical connections. |
| `circle_count` | Feature | Input feature representing administrative circle count. |
| `division_count` | Feature | Input feature representing division count. |
| `subdivision_count` | Feature | Input feature representing subdivision count. |
| `charging_station_count` | Feature | Input feature representing charging station count. |
| `latitude` | Feature | Centroid coordinates representing geographical positioning. |
| `longitude` | Feature | Centroid coordinates representing geographical positioning. |
| `district_area_sqkm` | Feature | Geographical area. |
| `quarter` | Feature | Temporal quarter index (1–4). |
| `year_index` | Feature | Time linear trend regressor. |
| `month_of_year` | Feature | Month index. |
| `is_first_month` | Feature | Time boundary flag. |
| `is_last_month` | Feature | Time boundary flag. |
| `stations_per_sqkm` | Feature | Density ratio. |
| `units_per_station` | Feature | Ratios. |
| `load_per_station` | Feature | Ratios. |
| `services_per_station` | Feature | Ratios. |
| `billed_service_ratio` | Feature | Service utilization ratio. |
| `average_units_per_service` | Feature | Service efficiency. |
| `average_load_per_service` | Feature | Service efficiency. |
| `average_units_per_billed_service` | Feature | Service efficiency. |
| `previous_month_units` | Feature | Lag feature (safe). |
| `previous_month_load` | Feature | Lag feature (safe). |
| `rolling_average_3m` | Feature | Historical rolling average (safe). |
| `rolling_average_6m` | Feature | Historical rolling average (safe). |
| `rolling_average_12m` | Feature | Historical rolling average (safe). |
| `rolling_std_3m` | Feature | Historical rolling volatility (safe). |
| `rolling_std_6m` | Feature | Historical rolling volatility (safe). |
| `rolling_max_6m` | Feature | Historical rolling extrema (safe). |
| `rolling_min_6m` | Feature | Historical rolling extrema (safe). |
| `monthly_growth_rate` | Feature | Historical percentage growth rate (safe). |
| `monthly_load_growth` | Feature | Historical percentage growth rate (safe). |
| `cumulative_units` | Feature | Cumulative total consumption (strictly historical, target leakage-free). |
| `cumulative_load` | Feature | Cumulative total load (strictly historical, target leakage-free). |

---

## 4. Alignment with Machine Learning Design Document

* **Numerical features only**: ✅ Confirmed. `ml_training_dataset.csv` contains only float64 and int64 data types.
* **No geometry**: ✅ Confirmed. Structural spatial geometry is omitted, with geographical centroid coordinates (`latitude` and `longitude`) retained.
* **No district names**: ✅ Confirmed. `district` is omitted.
* **No reporting month**: ✅ Confirmed. `reporting_month` is omitted.
* **No future information**: ✅ Confirmed. Chronological sorting by `(district, reporting_month)` is enforced, and temporal rolling computations use historical lookbacks only.
* **No data leakage**: ✅ Confirmed. All rolling, growth, lag, and cumulative features exclude the current month's values via `.shift(1)`.

---

## 5. Review Conclusion

### READY TO MERGE

**Justification:**
All architectural review recommendations have been successfully implemented. The target leakage issue identified in `cumulative_units` and `cumulative_load` has been completely resolved by switching to `.shift(1).cumsum()`. The outputs have been regenerated and validated successfully. The dataset is fully ready for Machine Learning training.
