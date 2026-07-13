# Circle-to-District Mapping Report

This report summarizes the results and data quality of the Circle-to-District mapping stage.

## Mapping Metrics

| Metric | Value |
| :--- | :--- |
| **Total Circles** | 38 |
| **Mapped Circles** | 38 |
| **Unmapped Circles** | 0 |
| **Duplicate Mappings** | 0 |
| **Mapping Coverage** | 100.00% |

## Validation Checks Summary

- **Unique Mappings Check**: PASSED
  - *No circle should have duplicate definitions in the mapping file.*
- **Non-empty Mapped Districts Check**: PASSED
  - *All circles with status 'mapped' must have non-empty district values.*
- **Missing Mappings Check**: PASSED
  - *All circles in the consumption dataset should be successfully mapped to a district.*
