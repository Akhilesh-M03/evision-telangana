# EVision Telangana – Master Dataset V1 Report

_Generated: 2026-07-14 01:13:53 UTC_

---

## 1. Overview

| Metric | Value |
| :--- | ---: |
| **Total Rows** | 1,245 |
| **Total Districts** | 32 |
| **Reporting Months** | 60 |
| **Total Columns** | 15 |
| **Output Path** | `D:\codes\projects\merge-datasets\data\interim\merged\master_dataset_v1.csv` |

---

## 2. Schema

| Column | Dtype | Non-null Count |
| :--- | :--- | ---: |
| `district` | `object` | 1,245 |
| `year` | `int64` | 1,245 |
| `month` | `int64` | 1,245 |
| `reporting_month` | `object` | 1,245 |
| `units` | `float64` | 1,245 |
| `load` | `float64` | 1,245 |
| `total_services` | `int64` | 1,245 |
| `billed_services` | `float64` | 1,245 |
| `circle_count` | `int64` | 1,245 |
| `division_count` | `int64` | 1,245 |
| `subdivision_count` | `int64` | 1,245 |
| `charging_station_count` | `int64` | 1,245 |
| `latitude` | `float64` | 1,245 |
| `longitude` | `float64` | 1,245 |
| `district_area_sqkm` | `float64` | 1,245 |

---

## 3. District Coverage Validation

### 3.1 Consumption Districts Not Found in Geography

_None_

### 3.2 Charging Station Districts Not Found in Geography

_None_

### 3.3 Geography Districts Absent from Consumption

> [!NOTE]
> These geography districts have no consumption records.  This may indicate
> newly created districts not yet in the consumption pipeline.

- `Narayanpet`

---

## 4. Join Statistics

### 4.1 Charging Station Join

| Metric | Value |
| :--- | ---: |
| Rows Before Join | 1,245 |
| Rows After Join | 1,245 |
| Approx. Districts With Zero Stations | 0 |

### 4.2 Geography Join

| Metric | Value |
| :--- | ---: |
| Rows Before Join | 1,245 |
| Rows After Join | 1,245 |
| Null Latitudes Post-Join | 0 |
| Null Longitudes Post-Join | 0 |
| Null Areas Post-Join | 0 |

---

## 5. Data Quality Validation

| Check | Status |
| :--- | :--- |
| No fully duplicated rows | ✅ Pass |
| No duplicate (district, reporting_month) keys | ✅ Pass |
| No unexpected nulls in non-optional columns | ✅ Pass |
| All consumption districts resolved to geography | ✅ Pass |
| All charging districts resolved to geography | ✅ Pass |

### 5.1 Null Values by Column

_No null values detected._

---

## 6. Charging Station Distribution by District

| District | Charging Stations |
| :--- | ---: |
| Ranga Reddy | 129 |
| Medchal Malkajgiri | 111 |
| Hyderabad | 101 |
| Nalgonda | 19 |
| Sangareddy | 18 |
| Suryapet | 14 |
| Mahabubnagar | 13 |
| Hanumakonda | 13 |
| Yadadri Bhuvanagiri | 11 |
| Nizamabad | 10 |
| Kamareddy | 8 |
| Karimnagar | 7 |
| Wanaparthy | 5 |
| Khammam | 5 |
| Bhadradri Kothagudem | 5 |
| Medak | 5 |
| Nagarkurnool | 4 |
| Siddipet | 4 |
| Mahabubabad | 4 |
| Vikarabad | 3 |
| Jogulamba Gadwal | 3 |
| Mancherial | 3 |
| Adilabad | 3 |
| Peddapalli | 3 |
| Warangal | 3 |
| Rajanna Sircilla | 2 |
| Jangaon | 2 |
| Kumuram Bheem Asifabad | 1 |
| Nirmal | 1 |
| Mulugu | 1 |
| Jagtial | 0 |
| Jayashankar Bhupalpally | 0 |

---

## 7. Dataset Summary Statistics

| Column | Min | Max | Mean | Std |
| :--- | ---: | ---: | ---: | ---: |
| `year` | 2021.00 | 2026.00 | 2024.10 | 1.29 |
| `month` | 1.00 | 12.00 | 6.24 | 3.46 |
| `units` | 0.00 | 1653178.00 | 23926.64 | 105143.13 |
| `load` | 1.50 | 30075.00 | 608.08 | 1527.52 |
| `total_services` | 1.00 | 273.00 | 15.14 | 31.67 |
| `billed_services` | 0.00 | 255.00 | 14.40 | 30.05 |
| `circle_count` | 1.00 | 6.00 | 1.28 | 1.07 |
| `division_count` | 1.00 | 17.00 | 2.66 | 3.02 |
| `subdivision_count` | 1.00 | 44.00 | 4.86 | 6.70 |
| `charging_station_count` | 0.00 | 129.00 | 22.36 | 37.79 |
| `latitude` | 16.07 | 19.52 | 17.76 | 0.84 |
| `longitude` | 77.75 | 80.72 | 78.93 | 0.78 |
| `district_area_sqkm` | 191.62 | 7204.00 | 3448.66 | 1653.67 |

---

*Report generated automatically by `scripts/preprocessing/merge_datasets.py` on behalf of the EVision Telangana Preprocessing Pipeline.*
