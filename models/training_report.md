# ML Training Report

## Overview
This report documents the results of training the EV charging demand forecasting model. Based on architectural review, the model is designed to forecast **next month's demand** (Option B).

## Dataset Changes
- **Target Definition:** `target = units.shift(-1)` per district.
- **Rows Removed:** The final observation for each of the 32 districts was dropped due to missing shifted targets.
- **Data Split:** A chronological split (80% train, 20% test) was used instead of random shuffling to prevent temporal data leakage.

## Model Comparison
| Model | RMSE | MAE | R² |
|---|---|---|---|
| RandomForest | 108065.98 | 24006.99 | 0.7262 |
| XGBoost | 103990.55 | 22939.12 | 0.7464 |

## Recommendation
**XGBoost** achieved the lowest RMSE and is recommended as the production model.
