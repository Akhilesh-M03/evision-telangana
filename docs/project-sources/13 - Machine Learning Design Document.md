# Machine Learning Design Document

**Project:** EVision Telangana  
**Official Project Title:** AI-Based EV Charging Infrastructure Planning and Decision Support System for Telangana

**Version:** 1.0  
**Status:** Draft  
**Last Updated:** July 2026

---

# Purpose

This document defines the complete Machine Learning design for EVision Telangana.

It specifies how machine learning is implemented within the system, including dataset preparation, feature engineering, model training, evaluation, clustering, model deployment, prediction workflow, explainability, and integration with the Decision Engine.

This document serves as the implementation blueprint for the Machine Learning Pipeline and bridges the gap between the approved ML Concepts document and the actual source code.

---

# Relationship to Other Project Documents

This document complements the existing Project Sources by defining the implementation details of the Machine Learning Pipeline.

| Document                                             | Purpose                                         |
| ---------------------------------------------------- | ----------------------------------------------- |
| Final Project Scope                                  | Defines project objectives and deliverables     |
| Master Roadmap                                       | Defines implementation phases                   |
| Final Tech Stack                                     | Defines approved ML libraries and technologies  |
| System Architecture                                  | Defines the role of the ML Engine               |
| Repository Structure                                 | Defines ML project organization                 |
| Database Schema                                      | Defines storage of prediction outputs           |
| Data Contracts                                       | Defines datasets and ML artifacts               |
| Coding Standards                                     | Defines implementation conventions              |
| ML Concepts                                          | Explains machine learning theory                |
| **Machine Learning Design Document (This Document)** | Defines the complete ML implementation workflow |

This document focuses on **how machine learning is implemented**, while remaining consistent with all approved Project Sources.

---

# Objectives

The Machine Learning Design aims to:

- Standardize the complete ML workflow.
- Define the regression pipeline.
- Define the clustering pipeline.
- Define feature engineering requirements.
- Define model evaluation.
- Define deployment strategy.
- Define explainability.
- Support backend integration.
- Support Decision Engine implementation.
- Ensure reproducibility.

---

# Machine Learning Pipeline

```text
Master Dataset
        │
        ▼
Feature Engineering
        │
        ▼
ML Training Dataset
        │
        ▼
Train-Test Split
        │
        ▼
Regression Training
        │
        ├─────────────► Random Forest
        │
        └─────────────► XGBoost
                    │
                    ▼
             Model Evaluation
                    │
                    ▼
            Best Model Selection
                    │
                    ▼
           Model Serialization
                    │
                    ▼
          Backend Prediction Service
                    │
                    ▼
             Decision Engine
                    │
                    ▼
 Dashboard • APIs • AI Assistant
```

---

# ML Pipeline Components

The Machine Learning Pipeline consists of six major stages:

1. Dataset Preparation
2. Feature Engineering
3. Regression Model Training
4. Clustering
5. Model Evaluation
6. Deployment

Each stage operates independently and produces deterministic outputs.

---

# Input Dataset

The Machine Learning Pipeline consumes:

```text
data/processed/master_dataset.csv
```

This dataset is generated entirely by the Data Engineering Pipeline.

No raw datasets are used directly during model training.

---

# Output Artifacts

The Machine Learning Pipeline generates:

```text
models/

best_regression.joblib

kmeans.joblib

feature_columns.json

model_metadata.json

evaluation_report.json
```

These artifacts are consumed by the Backend Prediction Service.

---

# Feature Categories

The training dataset consists of multiple feature groups.

---

## Geographic Features

Examples include:

- district_area_sqkm
- latitude
- longitude

---

## Demographic Features

Examples include:

- population
- population_density
- urban_percentage

---

## Infrastructure Features

Examples include:

- charging_station_count
- road_length_km
- highway_length_km

---

## Transportation Features

Examples include:

- ev_registrations
- total_vehicle_registrations

---

## Electricity Features

Examples include:

- energy_units
- sanctioned_load

---

## Engineered Features

Examples include:

- stations_per_100k_population
- stations_per_sqkm
- units_per_station
- utilization_ratio
- demand_growth_rate
- rolling_average_3m
- rolling_average_6m
- rolling_average_12m

---

# Feature Selection

Only numerical features required by the regression models are included.

The following fields are excluded:

- district_name
- geometry
- recommendation
- priority_level
- cluster_name

Categorical features are encoded before training where required.

---

# Target Variable

The regression models predict:

```text
predicted_demand
```

This represents the estimated future EV charging demand for a district.

---

# Data Preprocessing

Before training, the following preprocessing steps are applied.

## Missing Values

- Numerical features are imputed.
- Invalid rows are removed.

---

## Duplicate Records

Duplicate observations are removed.

---

## Encoding

Categorical variables are encoded where necessary.

---

## Scaling

Tree-based models generally do not require feature scaling.

Scaling remains optional for future models.

---

# Train-Test Split

The processed dataset is divided into:

```text
80% Training

20% Testing
```

A fixed random seed is used to ensure reproducibility.

---

# Regression Models

The project evaluates two approved regression algorithms.

---

## Random Forest Regressor

Purpose:

Provide a strong baseline regression model.

Advantages:

- Robust
- Stable
- Feature Importance
- Low overfitting

---

## XGBoost Regressor

Purpose:

Provide an optimized boosting-based regression model.

Advantages:

- Higher accuracy
- Better handling of nonlinear relationships
- Built-in regularization

---

# Hyperparameter Tuning

The following parameters may be tuned.

Random Forest

- n_estimators
- max_depth
- min_samples_split
- min_samples_leaf

XGBoost

- learning_rate
- max_depth
- n_estimators
- subsample
- colsample_bytree

Grid Search or Random Search may be used.

---

# Model Evaluation

Models are evaluated using:

- RMSE
- MAE
- R² Score

Evaluation uses the testing dataset only.

---

# Model Selection

The production model is selected according to:

- Lowest RMSE
- Lowest MAE
- Highest R² Score

Only one regression model is deployed.

---

# Feature Importance

Both approved regression models provide feature importance values.

These values are used to:

- Interpret predictions
- Support dashboard insights
- Generate AI explanations

---

# Clustering Pipeline

The project also performs district clustering.

Pipeline:

```text
Master Dataset
        │
        ▼
Feature Selection
        │
        ▼
Normalization
        │
        ▼
K-Means Clustering
        │
        ▼
Cluster Labels
        │
        ▼
Analytics Engine
```

---

# Clustering Features

Typical clustering features include:

- charging_station_count
- energy_units
- population
- ev_registrations
- utilization_ratio

---

# Number of Clusters

The optimal number of clusters is determined using:

- Elbow Method
- Silhouette Score

---

# Clustering Outputs

Generated outputs include:

- cluster_id
- cluster_summary
- cluster_statistics

These outputs support dashboard visualization and district profiling.

---

# Model Serialization

After evaluation, the selected models are saved.

Example:

```text
models/

best_regression.joblib

kmeans.joblib
```

Supporting metadata is also stored.

---

# Prediction Workflow

```text
API Request
        │
        ▼
Load Model
        │
        ▼
Prepare Features
        │
        ▼
Generate Prediction
        │
        ▼
Return Prediction
```

The backend never retrains models during runtime.

---

# Explainable AI

Prediction outputs are supplemented with feature-based explanations.

Example:

```text
Predicted Demand:

4,250 kWh

Key Contributing Factors

• High EV registrations

• Low charging station availability

• Increasing historical demand

• High utilization ratio
```

These explanations support both the dashboard and AI Assistant.

---

# Decision Engine Integration

Machine Learning outputs are combined with additional information.

Inputs include:

- Predicted demand
- Charging station count
- Population
- EV registrations
- Cluster assignment
- Infrastructure metrics

These inputs are used to calculate:

- Priority Score
- Priority Level
- District Ranking
- Recommendation

---

# Model Versioning

Every trained model includes metadata such as:

- Model Version
- Training Date
- Dataset Version
- Algorithm
- Evaluation Metrics

This ensures reproducibility and traceability.

---

# Validation Rules

Before deployment, the Machine Learning Pipeline shall verify:

- Required features exist.
- No missing target values.
- Numeric features are valid.
- Models satisfy evaluation thresholds.
- Serialized artifacts load successfully.
- Predictions are reproducible.

---

# Future Enhancements

Potential future improvements include:

- Time-series forecasting models
- AutoML experimentation
- SHAP-based explainability
- Spatial regression
- Deep learning models
- Automated retraining pipeline

These enhancements remain outside the approved MVP but are compatible with the current architecture.

---

# Conclusion

The Machine Learning Design Document serves as the implementation blueprint for the EVision Telangana Machine Learning Pipeline.

It standardizes model development, evaluation, deployment, and integration with the backend, Decision Engine, dashboard, and AI Assistant while ensuring consistency, reproducibility, and maintainability throughout the project lifecycle.