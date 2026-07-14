# EVision Telangana – Data Consistency Report

_Generated: 2026-07-14 02:09:22 UTC_

> [!NOTE]
> This report validates the integrity of `master_dataset_v1.csv` against
> its upstream source datasets.  No source data is modified.

---

## 1. Overall Status

| Overall Consistency | **PASS** |
| :--- | :--- |

| Check Category | Status |
| :--- | :---: |
| Row count preserved | **Pass** |
| Numeric totals match | **Pass** |
| No duplicate keys | **Pass** |
| No geography nulls | **Pass** |
| No lookup duplicates | **Pass** |

---

## 2. Row Count Preservation

| Dataset | Row Count |
| :--- | ---: |
| `district_monthly_consumption.csv` | 1,245 |
| `master_dataset_v1.csv` | 1,245 |
| **Match** | **Pass** |

> [!NOTE]
> The master dataset is built with a left join from the consumption table.
> Row count must be exactly equal; any difference indicates a fan-out (m:many join).

---

## 3. Numeric Total Consistency

Verifies that column sums are identical before and after the merge.
Tolerance: `1e-4` (to accommodate floating-point representation).

| Column | Consumption Sum | Master Sum | Delta | Status |
| :--- | ---: | ---: | ---: | :---: |
| `units` | 29,788,661.0000 | 29,788,661.0000 | 0.000000 | **Pass** |
| `load` | 757,062.3120 | 757,062.3120 | 0.000000 | **Pass** |
| `total_services` | 18,855.0000 | 18,855.0000 | 0.000000 | **Pass** |
| `billed_services` | 17,924.0000 | 17,924.0000 | 0.000000 | **Pass** |

---

## 4. Key Uniqueness

| Check | Count | Status |
| :--- | ---: | :---: |
| Fully duplicated rows | 0 | **Pass** |
| Duplicate (district, reporting_month) keys | 0 | **Pass** |

---

## 5. Geographic Information Completeness

Checks that no rows in the master dataset have null values for geographic fields.

| Column | Null Count | Status |
| :--- | ---: | :---: |
| `latitude` | 0 | **Pass** |
| `longitude` | 0 | **Pass** |
| `district_area_sqkm` | 0 | **Pass** |

---

## 6. Lookup Table Duplicate Check

| Lookup Table | Duplicate Districts | Status |
| :--- | ---: | :---: |
| `district_geography.csv` (`district_name`) | 0 | **Pass** |
| `charging_stations_clean.csv` (aggregated by district) | 0 | **Pass** |

---

*Report generated automatically by `scripts/preprocessing/audit_master_dataset.py` on behalf of the EVision Telangana Preprocessing Pipeline.*
