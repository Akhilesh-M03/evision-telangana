# Consumption Dataset Preprocessing Validation Report

Generated on: 2026-07-14 04:03:19

## Processing Summary

| Metric | Value |
| --- | --- |
| Total Discovered Files | 101 |
| Successfully Processed Files | 101 |
| Failed Files | 0 |
| Total Raw Rows Read | 15441 |
| Duplicate Rows Dropped | 64 |
| Final Output Rows | 15377 |



## Schema & Column Validation

Standardized schema columns verify:
- Source dataset matching `TG-SPDCL` or `TG-NPDCL`.
- Month and Year correctly parsed from path and filenames.
- Clean uppercase format for strings.
- Nullable `Int64` integer mapping for services.
- `float` numeric mapping for consumption units and load.

### Missing Values Count

| Column | Missing Count |
| --- | --- |
| source | 0 |
| year | 0 |
| month | 0 |
| reporting_month | 0 |
| circle | 0 |
| division | 0 |
| subdivision | 0 |
| section | 0 |
| area | 0 |
| cat_code | 0 |
| category | 0 |
| total_services | 0 |
| billed_services | 553 |
| units | 0 |
| load | 0 |

## Detailed File Inventory

| Source | Year | Month | File Name | Status | Rows Read | Error Message |
| --- | --- | --- | --- | --- | --- | --- |
| TG-NPDCL | 2023 | 1 | `1_JAN_2023.csv` | SUCCESS | 24 | - |
| TG-NPDCL | 2023 | 2 | `2_FEB_2023.csv` | SUCCESS | 28 | - |
| TG-NPDCL | 2023 | 3 | `3_MAR_2023.csv` | SUCCESS | 28 | - |
| TG-NPDCL | 2023 | 4 | `4_APR_2023.csv` | SUCCESS | 31 | - |
| TG-NPDCL | 2023 | 5 | `5_MAY_2023.csv` | SUCCESS | 31 | - |
| TG-NPDCL | 2023 | 6 | `6_JUN_2023.csv` | SUCCESS | 31 | - |
| TG-NPDCL | 2023 | 7 | `7_JUL_2023.csv` | SUCCESS | 32 | - |
| TG-NPDCL | 2023 | 8 | `8_AUG_2023.csv` | SUCCESS | 32 | - |
| TG-NPDCL | 2023 | 9 | `9_SEP_2023.csv` | SUCCESS | 33 | - |
| TG-NPDCL | 2023 | 10 | `10_OCT_2023.csv` | SUCCESS | 34 | - |
| TG-NPDCL | 2023 | 11 | `11_NOV_2023.csv` | SUCCESS | 35 | - |
| TG-NPDCL | 2023 | 12 | `12_DEC_2023.csv` | SUCCESS | 35 | - |
| TG-NPDCL | 2024 | 1 | `1_JAN_2024.csv` | SUCCESS | 36 | - |
| TG-NPDCL | 2024 | 2 | `2_FEB_2024.csv` | SUCCESS | 36 | - |
| TG-NPDCL | 2024 | 3 | `3_MAR_2024.csv` | SUCCESS | 37 | - |
| TG-NPDCL | 2024 | 4 | `4_APR_2024.csv` | SUCCESS | 37 | - |
| TG-NPDCL | 2024 | 5 | `5_MAY_2024.csv` | SUCCESS | 37 | - |
| TG-NPDCL | 2024 | 6 | `6_JUN_2024.csv` | SUCCESS | 25 | - |
| TG-NPDCL | 2024 | 7 | `7_JUL_2024.csv` | SUCCESS | 37 | - |
| TG-NPDCL | 2024 | 8 | `8_AUG_2024.csv` | SUCCESS | 38 | - |
| TG-NPDCL | 2024 | 9 | `9_SEP_2024.csv` | SUCCESS | 39 | - |
| TG-NPDCL | 2024 | 10 | `10_OCT_2024.csv` | SUCCESS | 39 | - |
| TG-NPDCL | 2024 | 11 | `11_NOV_2024.csv` | SUCCESS | 40 | - |
| TG-NPDCL | 2024 | 12 | `12_DEC_2024.csv` | SUCCESS | 43 | - |
| TG-NPDCL | 2025 | 1 | `1_JAN_2025.csv` | SUCCESS | 46 | - |
| TG-NPDCL | 2025 | 2 | `2_FEB_2025.csv` | SUCCESS | 50 | - |
| TG-NPDCL | 2025 | 3 | `3_MAR_2025.csv` | SUCCESS | 66 | - |
| TG-NPDCL | 2025 | 4 | `4_APR_2025.csv` | SUCCESS | 84 | - |
| TG-NPDCL | 2025 | 5 | `5_MAY_2025.csv` | SUCCESS | 93 | - |
| TG-NPDCL | 2025 | 6 | `6_JUN_2025.csv` | SUCCESS | 101 | - |
| TG-NPDCL | 2025 | 7 | `7_JUL_2025.csv` | SUCCESS | 110 | - |
| TG-NPDCL | 2025 | 8 | `8_AUG_2025.csv` | SUCCESS | 115 | - |
| TG-NPDCL | 2025 | 9 | `9_SEP_2025.csv` | SUCCESS | 119 | - |
| TG-NPDCL | 2025 | 10 | `10_OCT_2025.csv` | SUCCESS | 128 | - |
| TG-NPDCL | 2025 | 11 | `11_NOV_2025.csv` | SUCCESS | 140 | - |
| TG-NPDCL | 2025 | 12 | `12_DEC_2025.csv` | SUCCESS | 149 | - |
| TG-NPDCL | 2026 | 1 | `1_JAN_2026.csv` | SUCCESS | 160 | - |
| TG-NPDCL | 2026 | 2 | `2_FEB_2026.csv` | SUCCESS | 165 | - |
| TG-NPDCL | 2026 | 3 | `3_MAR_2026.csv` | SUCCESS | 168 | - |
| TG-NPDCL | 2026 | 4 | `4_APR_2026.csv` | SUCCESS | 173 | - |
| TG-NPDCL | 2026 | 5 | `5_MAY_2026.csv` | SUCCESS | 173 | - |
| TG-NPDCL | 2026 | 6 | `6_JUN_2026.csv` | SUCCESS | 178 | - |
| TG-SPDCL | 2021 | 6 | `06_Jun_2021.csv` | SUCCESS | 22 | - |
| TG-SPDCL | 2021 | 7 | `07_Jul_2021.csv` | SUCCESS | 24 | - |
| TG-SPDCL | 2021 | 8 | `08_Aug_2021.csv` | SUCCESS | 32 | - |
| TG-SPDCL | 2021 | 9 | `09_Sep_2021.csv` | SUCCESS | 35 | - |
| TG-SPDCL | 2021 | 10 | `10_Oct_2021.csv` | SUCCESS | 38 | - |
| TG-SPDCL | 2021 | 11 | `11_Nov_2021.csv` | SUCCESS | 40 | - |
| TG-SPDCL | 2021 | 12 | `12_Dec_2021.csv` | SUCCESS | 42 | - |
| TG-SPDCL | 2022 | 1 | `01_Jan_2022.csv` | SUCCESS | 46 | - |
| TG-SPDCL | 2022 | 2 | `02_Feb_2022.csv` | SUCCESS | 47 | - |
| TG-SPDCL | 2022 | 3 | `03_Mar_2022.csv` | SUCCESS | 50 | - |
| TG-SPDCL | 2022 | 4 | `04_Apr_2022.csv` | SUCCESS | 55 | - |
| TG-SPDCL | 2022 | 6 | `06_Jun_2022.csv` | SUCCESS | 67 | - |
| TG-SPDCL | 2022 | 7 | `07_Jul_2022.csv` | SUCCESS | 69 | - |
| TG-SPDCL | 2022 | 8 | `08_Aug_2022.csv` | SUCCESS | 75 | - |
| TG-SPDCL | 2022 | 9 | `09_Sep_2022.csv` | SUCCESS | 76 | - |
| TG-SPDCL | 2022 | 10 | `10_Oct_2022.csv` | SUCCESS | 77 | - |
| TG-SPDCL | 2022 | 11 | `11_Nov_2022.csv` | SUCCESS | 81 | - |
| TG-SPDCL | 2022 | 12 | `12_Dec_2022.csv` | SUCCESS | 85 | - |
| TG-SPDCL | 2023 | 1 | `01_Jan_2023.csv` | SUCCESS | 90 | - |
| TG-SPDCL | 2023 | 2 | `02_Feb_2023.csv` | SUCCESS | 92 | - |
| TG-SPDCL | 2023 | 3 | `03_Mar_2023.csv` | SUCCESS | 100 | - |
| TG-SPDCL | 2023 | 4 | `04_Apr_2023.csv` | SUCCESS | 108 | - |
| TG-SPDCL | 2023 | 5 | `05_May_2023.csv` | SUCCESS | 123 | - |
| TG-SPDCL | 2023 | 6 | `06_Jun_2023.csv` | SUCCESS | 128 | - |
| TG-SPDCL | 2023 | 7 | `07_Jul_2023.csv` | SUCCESS | 133 | - |
| TG-SPDCL | 2023 | 8 | `08_Aug_2023.csv` | SUCCESS | 145 | - |
| TG-SPDCL | 2023 | 9 | `09_Sep_2023.csv` | SUCCESS | 159 | - |
| TG-SPDCL | 2023 | 10 | `10_Oct_2023.csv` | SUCCESS | 169 | - |
| TG-SPDCL | 2023 | 11 | `11_Nov_2023.csv` | SUCCESS | 176 | - |
| TG-SPDCL | 2023 | 12 | `12_Dec_2023.csv` | SUCCESS | 186 | - |
| TG-SPDCL | 2024 | 1 | `01_Jan_2024.csv` | SUCCESS | 194 | - |
| TG-SPDCL | 2024 | 2 | `02_Feb_2024.csv` | SUCCESS | 198 | - |
| TG-SPDCL | 2024 | 3 | `03_Mar_2024.csv` | SUCCESS | 203 | - |
| TG-SPDCL | 2024 | 4 | `04_Apr_2024.csv` | SUCCESS | 209 | - |
| TG-SPDCL | 2024 | 5 | `05_May_2024.csv` | SUCCESS | 211 | - |
| TG-SPDCL | 2024 | 6 | `06_Jun_2024.csv` | SUCCESS | 215 | - |
| TG-SPDCL | 2024 | 7 | `07_Jul_2024.csv` | SUCCESS | 224 | - |
| TG-SPDCL | 2024 | 8 | `08_Aug_2024.csv` | SUCCESS | 226 | - |
| TG-SPDCL | 2024 | 9 | `09_Sep_2024.csv` | SUCCESS | 234 | - |
| TG-SPDCL | 2024 | 10 | `10_Oct_2024.csv` | SUCCESS | 241 | - |
| TG-SPDCL | 2024 | 11 | `11_Nov_2024.csv` | SUCCESS | 245 | - |
| TG-SPDCL | 2024 | 12 | `12_Dec_2024.csv` | SUCCESS | 254 | - |
| TG-SPDCL | 2025 | 1 | `01_Jan_2025.csv` | SUCCESS | 282 | - |
| TG-SPDCL | 2025 | 2 | `02_Feb_2025.csv` | SUCCESS | 301 | - |
| TG-SPDCL | 2025 | 3 | `03_Mar_2025.csv` | SUCCESS | 326 | - |
| TG-SPDCL | 2025 | 4 | `04_Apr_2025.csv` | SUCCESS | 366 | - |
| TG-SPDCL | 2025 | 5 | `05_May_2025.csv` | SUCCESS | 394 | - |
| TG-SPDCL | 2025 | 6 | `06_Jun_2025.csv` | SUCCESS | 413 | - |
| TG-SPDCL | 2025 | 7 | `07_Jul_2025.csv` | SUCCESS | 422 | - |
| TG-SPDCL | 2025 | 8 | `08_Aug_2025.csv` | SUCCESS | 495 | - |
| TG-SPDCL | 2025 | 10 | `10_Oct_2025.csv` | SUCCESS | 436 | - |
| TG-SPDCL | 2025 | 11 | `11_Nov_2025.csv` | SUCCESS | 442 | - |
| TG-SPDCL | 2025 | 12 | `12_Dec_2025.csv` | SUCCESS | 443 | - |
| TG-SPDCL | 2026 | 1 | `01_Jan_2026.csv` | SUCCESS | 452 | - |
| TG-SPDCL | 2026 | 2 | `02_Feb_2026.csv` | SUCCESS | 469 | - |
| TG-SPDCL | 2026 | 3 | `03_Mar_2026.csv` | SUCCESS | 476 | - |
| TG-SPDCL | 2026 | 4 | `04_Apr_2026.csv` | SUCCESS | 481 | - |
| TG-SPDCL | 2026 | 5 | `05_May_2026.csv` | SUCCESS | 485 | - |
| TG-SPDCL | 2026 | 6 | `06_Jun_2026.csv` | SUCCESS | 498 | - |

