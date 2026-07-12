- [Data Contracts](#data-contracts)
- [Purpose](#purpose)
- [Relationship to Other Project Documents](#relationship-to-other-project-documents)
- [Data Contract Objectives](#data-contract-objectives)
  - [1. Single Source of Truth](#1-single-source-of-truth)
  - [2. Consistent Data Exchange](#2-consistent-data-exchange)
  - [3. Parallel Development](#3-parallel-development)
  - [4. Data Integrity](#4-data-integrity)
  - [5. Reproducibility](#5-reproducibility)
  - [6. Maintainability](#6-maintainability)
- [Data Contract Design Principles](#data-contract-design-principles)
  - [Immutable Raw Data](#immutable-raw-data)
  - [Generated Processed Data](#generated-processed-data)
  - [Standardized Naming](#standardized-naming)
  - [Explicit Ownership](#explicit-ownership)
  - [Version Awareness](#version-awareness)
  - [Separation of Runtime and Training Data](#separation-of-runtime-and-training-data)
- [Data Flow Overview](#data-flow-overview)
- [Repository Data Locations](#repository-data-locations)
  - [3. External Supporting Data](#3-external-supporting-data)
  - [4. Generated Machine Learning Artifacts](#4-generated-machine-learning-artifacts)
- [Raw Dataset Contracts](#raw-dataset-contracts)
- [TGSPDCL EV Charging Station Consumption Dataset](#tgspdcl-ev-charging-station-consumption-dataset)
  - [Purpose](#purpose-1)
  - [Dataset Owner](#dataset-owner)
  - [Repository Location](#repository-location)
  - [File Format](#file-format)
  - [Naming Convention](#naming-convention)
  - [Consumed By](#consumed-by)
  - [Generated Outputs](#generated-outputs)
  - [Required Columns](#required-columns)
  - [Optional Columns](#optional-columns)
  - [Validation Rules](#validation-rules)
- [TGNPDCL EV Charging Station Consumption Dataset](#tgnpdcl-ev-charging-station-consumption-dataset)
  - [Purpose](#purpose-2)
  - [Dataset Owner](#dataset-owner-1)
  - [Repository Location](#repository-location-1)
  - [File Format](#file-format-1)
  - [Naming Convention](#naming-convention-1)
  - [Consumed By](#consumed-by-1)
  - [Generated Outputs](#generated-outputs-1)
  - [Required Columns](#required-columns-1)
  - [Optional Columns](#optional-columns-1)
  - [Validation Rules](#validation-rules-1)
- [TGREDCO Charging Station Dataset](#tgredco-charging-station-dataset)
  - [Purpose](#purpose-3)
  - [Dataset Owner](#dataset-owner-2)
  - [Repository Location](#repository-location-2)
  - [File Format](#file-format-2)
  - [Naming Convention](#naming-convention-2)
  - [Consumed By](#consumed-by-2)
  - [Generated Outputs](#generated-outputs-2)
  - [Required Columns](#required-columns-2)
  - [Optional Columns](#optional-columns-2)
  - [Validation Rules](#validation-rules-2)
  - [File Format](#file-format-3)
  - [Naming Convention](#naming-convention-3)
  - [Consumed By](#consumed-by-3)
  - [Required Properties](#required-properties)
  - [Optional Properties](#optional-properties)
  - [Validation Rules](#validation-rules-3)
- [Processed Dataset Contracts](#processed-dataset-contracts)
- [Clean Consumption Dataset](#clean-consumption-dataset)
  - [Purpose](#purpose-4)
  - [Dataset Owner](#dataset-owner-3)
  - [Repository Location](#repository-location-3)
  - [File Format](#file-format-4)
  - [Naming Convention](#naming-convention-4)
  - [Input Sources](#input-sources)
  - [Consumed By](#consumed-by-4)
  - [Required Columns](#required-columns-3)
  - [Optional Columns](#optional-columns-3)
  - [Validation Rules](#validation-rules-4)
- [Integrated Consumption Dataset](#integrated-consumption-dataset)
  - [Purpose](#purpose-5)
  - [Dataset Owner](#dataset-owner-4)
  - [Repository Location](#repository-location-4)
  - [File Format](#file-format-5)
  - [Naming Convention](#naming-convention-5)
  - [Input Sources](#input-sources-1)
  - [Consumed By](#consumed-by-5)
  - [Required Columns](#required-columns-4)
  - [Validation Rules](#validation-rules-5)
- [Master Dataset](#master-dataset)
  - [Purpose](#purpose-6)
  - [Dataset Owner](#dataset-owner-5)
  - [Repository Location](#repository-location-5)
  - [File Format](#file-format-6)
  - [Naming Convention](#naming-convention-6)
  - [Input Sources](#input-sources-2)
  - [Consumed By](#consumed-by-6)
  - [Required Columns](#required-columns-5)
  - [Optional Columns](#optional-columns-4)
  - [Validation Rules](#validation-rules-6)
- [Feature Engineering Contract](#feature-engineering-contract)
  - [Input Dataset](#input-dataset)
  - [Output Dataset](#output-dataset)
  - [Dataset Owner](#dataset-owner-6)
  - [Repository Location](#repository-location-6)
  - [Consumed By](#consumed-by-7)
  - [Required Base Columns](#required-base-columns)
  - [Generated Features](#generated-features)
  - [Feature Types](#feature-types)
  - [Feature Validation Rules](#feature-validation-rules)
- [Machine Learning Training Dataset Contract](#machine-learning-training-dataset-contract)
  - [Dataset Owner](#dataset-owner-7)
  - [Repository Location](#repository-location-7)
  - [File Format](#file-format-7)
  - [Naming Convention](#naming-convention-7)
  - [Produced By](#produced-by)
  - [Consumed By](#consumed-by-8)
  - [Required Columns](#required-columns-6)
  - [Target Variable](#target-variable)
  - [Dataset Split](#dataset-split)
  - [Validation Rules](#validation-rules-7)
- [Prediction Output Contract](#prediction-output-contract)
  - [Dataset Owner](#dataset-owner-8)
  - [Repository Location](#repository-location-8)
  - [File Format](#file-format-8)
  - [Naming Convention](#naming-convention-8)
  - [Produced By](#produced-by-1)
  - [Consumed By](#consumed-by-9)
  - [Required Columns](#required-columns-7)
  - [Optional Columns](#optional-columns-5)
  - [Validation Rules](#validation-rules-8)
- [Clustering Output Contract](#clustering-output-contract)
  - [Dataset Owner](#dataset-owner-9)
  - [Repository Location](#repository-location-9)
  - [File Format](#file-format-9)
  - [Naming Convention](#naming-convention-9)
  - [Produced By](#produced-by-2)
  - [Consumed By](#consumed-by-10)
  - [Required Columns](#required-columns-8)
  - [Optional Columns](#optional-columns-6)
  - [Validation Rules](#validation-rules-9)
- [Decision Engine Dataset Contract](#decision-engine-dataset-contract)
  - [Dataset Owner](#dataset-owner-10)
  - [Repository Location](#repository-location-10)
  - [Input Datasets](#input-datasets)
  - [Output Dataset](#output-dataset-1)
  - [Consumed By](#consumed-by-11)
  - [Required Columns](#required-columns-9)
  - [Optional Columns](#optional-columns-7)
  - [Validation Rules](#validation-rules-10)
- [GeoJSON Contract](#geojson-contract)
  - [Dataset Owner](#dataset-owner-11)
  - [Repository Location](#repository-location-11)
  - [File Format](#file-format-10)
  - [Naming Convention](#naming-convention-10)
  - [Coordinate Reference System](#coordinate-reference-system)
  - [Required Properties](#required-properties-1)
  - [Geometry Types](#geometry-types)
  - [Validation Rules](#validation-rules-11)
- [Joblib Model Contracts](#joblib-model-contracts)
- [Regression Model Contract](#regression-model-contract)
  - [Purpose](#purpose-7)
  - [Repository Location](#repository-location-12)
  - [File Format](#file-format-11)
  - [Naming Convention](#naming-convention-11)
  - [Produced By](#produced-by-3)
  - [Consumed By](#consumed-by-12)
  - [Artifact Contents](#artifact-contents)
  - [Validation Rules](#validation-rules-12)
- [K-Means Model Contract](#k-means-model-contract)
  - [Purpose](#purpose-8)
  - [Repository Location](#repository-location-13)
  - [File Format](#file-format-12)
  - [Naming Convention](#naming-convention-12)
  - [Produced By](#produced-by-4)
  - [Consumed By](#consumed-by-13)
  - [Artifact Contents](#artifact-contents-1)
  - [Validation Rules](#validation-rules-13)
- [Model Versioning](#model-versioning)
- [Data Ownership Matrix](#data-ownership-matrix)
- [File Naming Conventions](#file-naming-conventions)
  - [General Rules](#general-rules)
  - [Raw Datasets](#raw-datasets)
  - [Processed Datasets](#processed-datasets)
  - [Geographic Files](#geographic-files)
  - [Machine Learning Models](#machine-learning-models)
  - [Evaluation Artifacts](#evaluation-artifacts)
- [Column Naming Conventions](#column-naming-conventions)
  - [General Rules](#general-rules-1)
  - [Identifier Columns](#identifier-columns)
  - [Numeric Columns](#numeric-columns)
  - [Timestamp Columns](#timestamp-columns)
- [Standard Data Types](#standard-data-types)
- [Missing Value Policy](#missing-value-policy)
  - [Required Fields](#required-fields)
  - [Optional Fields](#optional-fields)
  - [Engineered Features](#engineered-features)
- [Validation Rules](#validation-rules-14)
  - [Structural Validation](#structural-validation)
  - [Content Validation](#content-validation)
  - [Referential Validation](#referential-validation)
  - [Geographic Validation](#geographic-validation)
  - [Machine Learning Validation](#machine-learning-validation)
- [Data Quality Expectations](#data-quality-expectations)
  - [Completeness](#completeness)
  - [Consistency](#consistency)
  - [Accuracy](#accuracy)
  - [Uniqueness](#uniqueness)
  - [Validity](#validity)
  - [Reproducibility](#reproducibility)
- [Versioning Strategy](#versioning-strategy)
  - [Raw Datasets](#raw-datasets-1)
  - [Processed Datasets](#processed-datasets-1)
  - [Machine Learning Models](#machine-learning-models-1)
  - [Recommendation Outputs](#recommendation-outputs)
  - [Database Initialization](#database-initialization)
- [Dataset Lifecycle](#dataset-lifecycle)
  - [Stage 1 — Raw Data Acquisition](#stage-1--raw-data-acquisition)
  - [Stage 2 — Data Preprocessing](#stage-2--data-preprocessing)
  - [Stage 3 — Feature Engineering](#stage-3--feature-engineering)
  - [Stage 4 — Machine Learning](#stage-4--machine-learning)
  - [Stage 5 — Prediction Generation](#stage-5--prediction-generation)
  - [Stage 6 — Analytics Generation](#stage-6--analytics-generation)
  - [Stage 7 — Decision Engine](#stage-7--decision-engine)
  - [Stage 8 — Database Initialization](#stage-8--database-initialization)
  - [Stage 9 — Application Runtime](#stage-9--application-runtime)
- [Data Lineage](#data-lineage)
- [Contract Change Management](#contract-change-management)
  - [Permitted Changes](#permitted-changes)
  - [Restricted Changes](#restricted-changes)
  - [Impact Assessment](#impact-assessment)
- [Governance](#governance)
- [Conclusion](#conclusion)


# Data Contracts

**Project:** EVision Telangana  
**Official Project Title:** AI-Based EV Charging Infrastructure Planning and Decision Support System for Telangana

**Version:** 1.0  
**Status:** Frozen  
**Last Updated:** July 2026

---

# Purpose

This document defines the approved data contracts for EVision Telangana.

It specifies every dataset, generated artifact, machine learning input, machine learning output, and data exchange format used throughout the project lifecycle.

The Data Contracts document serves as the implementation agreement between the Data Processing Pipeline, Machine Learning Pipeline, Database Layer, Backend Services, Frontend Application, and AI Assistant.

This document intentionally defines **how data is exchanged between project modules** rather than how algorithms or business logic are implemented.

It serves as the authoritative reference for all project datasets and machine learning artifacts throughout development.

---

# Relationship to Other Project Documents

The Data Contracts document complements the existing project documentation by defining the structure, ownership, validation rules, and lifecycle of all datasets exchanged between project components.

| Document                           | Purpose                                                                                      |
| ---------------------------------- | -------------------------------------------------------------------------------------------- |
| Final Project Scope                | Defines approved datasets and project boundaries.                                            |
| Master Roadmap                     | Defines implementation phases and execution workflow.                                        |
| Final Tech Stack                   | Defines approved technologies used for processing and storage.                               |
| System Architecture                | Defines how data flows through the system.                                                   |
| Repository Structure               | Defines where datasets and artifacts are stored.                                             |
| Git Workflow                       | Defines collaboration practices for data-related changes.                                    |
| API Specification                  | Defines runtime data exchanged through REST APIs.                                            |
| Database Schema                    | Defines runtime persistence within SQLite.                                                   |
| **Data Contracts (This Document)** | Defines datasets, machine learning artifacts, file formats, validation rules, and ownership. |

This document does not introduce new datasets or project scope.

Instead, it formalizes the structure and contracts governing data exchanged between all project modules.

---

# Data Contract Objectives

The approved data contracts have been designed around several primary objectives.

## 1. Single Source of Truth

Each dataset has one authoritative source.

---

## 2. Consistent Data Exchange

Every project module exchanges data using standardized formats.

---

## 3. Parallel Development

Frontend, backend, machine learning, and data engineering can be developed independently using agreed data structures.

---

## 4. Data Integrity

Validation rules ensure datasets remain complete and internally consistent.

---

## 5. Reproducibility

Identical raw datasets should always produce identical processed outputs.

---

## 6. Maintainability

Dataset organization remains predictable and scalable throughout the project lifecycle.

---

# Data Contract Design Principles

The project follows several guiding principles.

---

## Immutable Raw Data

Raw datasets are never modified directly.

---

## Generated Processed Data

Processed datasets are generated programmatically through the preprocessing pipeline.

---

## Standardized Naming

All files and columns follow consistent naming conventions.

---

## Explicit Ownership

Every dataset has one owning component.

---

## Version Awareness

Generated datasets and model artifacts should include version information where applicable.

---

## Separation of Runtime and Training Data

Training datasets remain separate from runtime database contents.

---

# Data Flow Overview

The complete project data flow is summarized below.

```text
Official Raw Datasets
        │
        ▼
Data Preprocessing Pipeline
        │
        ▼
Processed Datasets
        │
        ├─────────────► Machine Learning Training
        │                     │
        │                     ▼
        │              Trained Models (.joblib)
        │                     │
        │                     ▼
        ├─────────────► Prediction Outputs
        │
        ├─────────────► Clustering Outputs
        │
        ▼
Decision Engine
        │
        ▼
Recommendation Outputs
        │
        ▼
SQLite Database
        │
        ▼
Backend APIs
        │
        ▼
Frontend Dashboard
                │
                ▼
         AI Assistant
```

---

# Repository Data Locations

| Repository Directory | Purpose                                   |
| -------------------- | ----------------------------------------- |
| `data/raw/`          | Official raw datasets                     |
| `data/processed/`    | Generated processed datasets              |
| `data/external/`     | Supporting GeoJSON and reference datasets |
| `models/`            | Serialized machine learning models        |
| `models/evaluation/` | Model evaluation outputs                  |

---

````

# Dataset Categories

The EVision Telangana project organizes all project data into four primary categories.

Each category has a distinct purpose, ownership, lifecycle, and storage location.

---

## 1. Raw Datasets

Raw datasets are the official source datasets collected from external organizations.

Characteristics:

- Original source data
- Never modified directly
- Read-only throughout the project
- Stored in `data/raw/`

Primary datasets include:

- TGSPDCL EV Charging Station Consumption
- TGNPDCL EV Charging Station Consumption
- TGREDCO Charging Station Details

These datasets serve as the authoritative inputs for the Data Processing Pipeline.

---

## 2. Processed Datasets

Processed datasets are generated by the preprocessing pipeline.

Characteristics:

- Cleaned
- Standardized
- Integrated
- Ready for machine learning and application use

Stored in:

```text
data/processed/
````

Typical processed datasets include:

- Clean consumption dataset
- Integrated consumption dataset
- Master dataset

Processed datasets may be regenerated whenever preprocessing is executed.

---

## 3. External Supporting Data

Supporting datasets provide geographic and reference information required by the application.

These datasets are not generated by the preprocessing pipeline.

Stored in:

```text
data/external/
```

Typical examples include:

- Telangana district boundaries (GeoJSON)

Supporting datasets are used primarily by:

- Interactive maps
- Geographic visualization
- Spatial analysis

---

## 4. Generated Machine Learning Artifacts

Machine learning produces several generated artifacts during model training.

These artifacts are not manually edited.

Stored in:

```text
models/
```

Typical artifacts include:

- Selected regression model (`best_regression.joblib`)
- Selected clustering model (`kmeans.joblib`)
- Evaluation summaries

Generated artifacts may be replaced whenever models are retrained.

---

# Raw Dataset Contracts

The following sections define the approved contracts for every official source dataset used within EVision Telangana.

These datasets remain the authoritative source of project data and must never be modified directly.

Any corrections, cleaning, or feature engineering should produce new processed datasets rather than altering the original files.

---

# TGSPDCL EV Charging Station Consumption Dataset

## Purpose

Provides historical electricity consumption records for EV charging stations operated under TGSPDCL.

The dataset contributes historical charging demand information for the Machine Learning Pipeline and dashboard analytics.

---

## Dataset Owner

Data Processing Pipeline

---

## Repository Location

```text
data/raw/
```

---

## File Format

```text
CSV
```

---

## Naming Convention

```text
tgspdcl_ev_consumption.csv
```

---

## Consumed By

- Data Preprocessing Pipeline

---

## Generated Outputs

- Clean Consumption Dataset
- Integrated Consumption Dataset
- Master Dataset

---

## Required Columns

The exact source column names may vary depending on the official dataset release.

The preprocessing pipeline shall normalize them into the approved project schema.

Minimum required information includes:

| Logical Field           | Data Type | Required |
| ----------------------- | --------- | -------- |
| District                | String    | Yes      |
| Reporting Month         | String    | Yes      |
| Electricity Consumption | Numeric   | Yes      |

---

## Optional Columns

Examples may include:

- Division
- Circle
- Station Identifier
- Remarks

Optional columns may be ignored if not required by the approved project scope.

---

## Validation Rules

The preprocessing pipeline shall verify:

- Required columns exist.
- District names are not empty.
- Reporting period is valid.
- Consumption values are numeric.
- Duplicate records are identified.
- Missing required values are reported.

---

# TGNPDCL EV Charging Station Consumption Dataset

## Purpose

Provides historical electricity consumption records for EV charging stations operated under TGNPDCL.

Combined with TGSPDCL data, it forms the statewide historical charging demand dataset.

---

## Dataset Owner

Data Processing Pipeline

---

## Repository Location

```text
data/raw/
```

---

## File Format

```text
CSV
```

---

## Naming Convention

```text
tgnpdcl_ev_consumption.csv
```

---

## Consumed By

- Data Preprocessing Pipeline

---

## Generated Outputs

- Clean Consumption Dataset
- Integrated Consumption Dataset
- Master Dataset

---

## Required Columns

| Logical Field           | Data Type | Required |
| ----------------------- | --------- | -------- |
| District                | String    | Yes      |
| Reporting Month         | String    | Yes      |
| Electricity Consumption | Numeric   | Yes      |

---

## Optional Columns

Examples include:

- Division
- Circle
- Station Identifier
- Remarks

---

## Validation Rules

The preprocessing pipeline shall verify:

- Required columns exist.
- District names are valid.
- Reporting periods are valid.
- Consumption values are numeric.
- Duplicate observations are detected.

---

# TGREDCO Charging Station Dataset

## Purpose

Provides information about existing EV charging stations across Telangana.

This dataset supplies infrastructure information used by the dashboard, database, recommendation engine, and AI Assistant.

---

## Dataset Owner

Data Processing Pipeline

---

## Repository Location

```text
data/raw/
```

---

## File Format

```text
CSV
```

---

## Naming Convention

```text
tgredco_charging_stations.csv
```

---

## Consumed By

- Data Preprocessing Pipeline

---

## Generated Outputs

- Master Dataset
- SQLite Charging Station Table

---

## Required Columns

| Logical Field | Data Type | Required |
| ------------- | --------- | -------- |
| District      | String    | Yes      |
| Station Name  | String    | No       |
| Latitude      | Decimal   | No       |
| Longitude     | Decimal   | No       |
| Organization  | String    | No       |

---

## Optional Columns

Examples include:

- Address
- Contact Information
- Additional Remarks

---

## Validation Rules

The preprocessing pipeline shall verify:

- District values are present.
- Coordinates, when available, are numeric.
- Latitude ranges between -90 and 90.
- Longitude ranges between -180 and 180.
- Duplicate station records are identified.

````

# External Supporting Dataset Contracts

Supporting datasets provide geographic reference information required for visualization and spatial analysis.

Unlike the primary datasets, these files are not processed into historical demand records.

They are used primarily for map rendering and geographic context.

---

# Telangana District Boundary GeoJSON

## Purpose

Provides the official district boundaries required for rendering the interactive Telangana map.

This dataset is used exclusively for geographic visualization and does not contribute to machine learning model training.

---

## Dataset Owner

Data Processing Pipeline

---

## Repository Location

```text
data/external/
````

---

## File Format

```text
GeoJSON
```

---

## Naming Convention

```text
telangana_district_boundaries.geojson
```

---

## Consumed By

- Backend Map Services
- Frontend Interactive Map
- Dashboard Visualizations

---

## Required Properties

Each GeoJSON feature shall contain the following minimum properties.

| Property | Data Type              | Required |
| -------- | ---------------------- | -------- |
| district | String                 | Yes      |
| geometry | Polygon / MultiPolygon | Yes      |

---

## Optional Properties

Examples include:

- District Code
- Area
- Metadata

These properties are optional and are not required by the approved MVP.

---

## Validation Rules

The dataset shall satisfy the following requirements.

- Valid GeoJSON syntax.
- Valid polygon or multipolygon geometry.
- Every district appears only once.
- District names match the standardized processed dataset.
- No invalid or self-intersecting geometries.

---

# Processed Dataset Contracts

Processed datasets are generated programmatically by the Data Processing Pipeline.

They provide standardized, validated, and application-ready data for machine learning, database initialization, analytics, and visualization.

Processed datasets should never be edited manually.

If preprocessing logic changes, the datasets should be regenerated rather than modified.

---

# Clean Consumption Dataset

## Purpose

Stores cleaned historical electricity consumption records after validation and standardization.

This dataset removes inconsistencies from the official source datasets while preserving the original observations.

---

## Dataset Owner

Data Processing Pipeline

---

## Repository Location

```text
data/processed/
```

---

## File Format

```text
CSV
```

---

## Naming Convention

```text
clean_consumption_dataset.csv
```

---

## Input Sources

- TGSPDCL Consumption Dataset
- TGNPDCL Consumption Dataset

---

## Consumed By

- Integrated Dataset Generation
- Exploratory Data Analysis
- Feature Engineering

---

## Required Columns

| Column          | Data Type |
| --------------- | --------- |
| district        | String    |
| reporting_month | String    |
| demand_kwh      | Decimal   |

---

## Optional Columns

Examples include:

- source_dataset
- remarks

---

## Validation Rules

The preprocessing pipeline shall ensure:

- Required columns exist.
- District names are standardized.
- Reporting month follows YYYY-MM format.
- Consumption values are numeric.
- Duplicate observations are removed.
- Missing required values are handled according to preprocessing rules.

---

# Integrated Consumption Dataset

## Purpose

Combines TGSPDCL and TGNPDCL consumption data into a unified statewide dataset.

This dataset serves as the primary historical demand dataset prior to feature engineering.

---

## Dataset Owner

Data Processing Pipeline

---

## Repository Location

```text
data/processed/
```

---

## File Format

```text
CSV
```

---

## Naming Convention

```text
integrated_consumption_dataset.csv
```

---

## Input Sources

- Clean Consumption Dataset

---

## Consumed By

- Feature Engineering
- Machine Learning Training
- Database Initialization

---

## Required Columns

| Column          | Data Type |
| --------------- | --------- |
| district        | String    |
| reporting_month | String    |
| demand_kwh      | Decimal   |

---

## Validation Rules

The preprocessing pipeline shall verify:

- District names remain unique per reporting month.
- No duplicate district-month combinations exist.
- Required values are complete.
- Dataset remains deterministic for identical inputs.

---

# Master Dataset

## Purpose

Provides the finalized dataset used throughout the remainder of the project.

The Master Dataset combines processed historical demand data with charging station information required by downstream project components.

It serves as the primary input for machine learning, database population, analytics generation, and the Decision Engine.

---

## Dataset Owner

Data Processing Pipeline

---

## Repository Location

```text
data/processed/
```

---

## File Format

```text
CSV
```

---

## Naming Convention

```text
master_dataset.csv
```

---

## Input Sources

- Integrated Consumption Dataset
- TGREDCO Charging Station Dataset

---

## Consumed By

- Machine Learning Pipeline
- Database Initialization
- Analytics Engine
- Decision Engine

---

## Required Columns

| Column                 | Data Type |
| ---------------------- | --------- |
| district               | String    |
| reporting_month        | String    |
| demand_kwh             | Decimal   |
| charging_station_count | Integer   |

---

## Optional Columns

Additional engineered attributes generated during preprocessing may also be included.

These columns remain implementation-dependent provided they do not alter the approved project scope.

---

## Validation Rules

The preprocessing pipeline shall ensure:

- Every district is standardized.
- Required columns are complete.
- Numeric values contain valid data.
- Duplicate records are eliminated.
- Charging station counts are non-negative.
- Dataset remains reproducible from identical raw inputs.

# Feature Engineering Contract

Feature engineering transforms the Master Dataset into a machine learning-ready dataset.

The process generates derived features that improve model performance while preserving reproducibility.

Feature engineering is performed entirely by the Data Processing Pipeline.

The generated dataset should never be edited manually.

---

## Input Dataset

```text
master_dataset.csv
```

---

## Output Dataset

```text
ml_training_dataset.csv
```

---

## Dataset Owner

Machine Learning Pipeline

---

## Repository Location

```text
data/processed/
```

---

## Consumed By

- Regression Model Training
- Clustering Model Training

---

## Required Base Columns

The following columns originate from the Master Dataset and must be preserved.

| Column                 | Data Type |
| ---------------------- | --------- |
| district               | String    |
| reporting_month        | String    |
| demand_kwh             | Decimal   |
| charging_station_count | Integer   |

---

## Generated Features

The exact engineered features remain implementation-dependent.

Typical feature categories include:

- Time-based features
- Historical demand summaries
- Infrastructure-related features
- Normalized numerical features

The approved project does not prescribe a specific feature engineering methodology.

---

## Feature Types

Generated features may include:

| Feature Type          | Purpose                       |
| --------------------- | ----------------------------- |
| Numerical             | Regression model input        |
| Categorical (encoded) | Machine learning input        |
| Derived statistics    | Improve predictive capability |

---

## Feature Validation Rules

Generated features shall satisfy the following requirements.

- No duplicate columns.
- Numeric features contain valid numeric values.
- Missing values are handled before training.
- Feature names use snake_case.
- Dataset remains reproducible from identical inputs.

---

# Machine Learning Training Dataset Contract

The Machine Learning Training Dataset serves as the authoritative input for all machine learning model training.

It is produced after preprocessing and feature engineering have been completed.

---

## Dataset Owner

Machine Learning Pipeline

---

## Repository Location

```text
data/processed/
```

---

## File Format

```text
CSV
```

---

## Naming Convention

```text
ml_training_dataset.csv
```

---

## Produced By

Feature Engineering Pipeline

---

## Consumed By

- Regression Model Training
- K-Means Clustering Training

---

## Required Columns

The final training dataset shall contain:

| Category            | Required |
| ------------------- | -------- |
| District Identifier | Yes      |
| Historical Demand   | Yes      |
| Engineered Features | Yes      |

The exact feature columns remain implementation-dependent.

---

## Target Variable

The regression model predicts:

```text
demand_kwh
```

No target variable is required for clustering.

---

## Dataset Split

The training pipeline is responsible for creating appropriate training and testing datasets.

Typical split responsibilities include:

- Training subset
- Testing subset

The exact split ratio is implementation-dependent.

---

## Validation Rules

Before model training begins, the training dataset shall satisfy the following requirements.

- No missing target values.
- Required features are present.
- Numeric features contain valid values.
- Duplicate observations are removed.
- Invalid districts are excluded.
- Dataset passes preprocessing validation.

---

# Prediction Output Contract

Prediction outputs are generated by the approved regression model.

These outputs represent finalized forecast values used throughout the application.

Prediction outputs are generated automatically and should never be edited manually.

---

## Dataset Owner

Machine Learning Pipeline

---

## Repository Location

```text
data/processed/
```

---

## File Format

```text
CSV
```

---

## Naming Convention

```text
prediction_outputs.csv
```

---

## Produced By

Selected Regression Model

---

## Consumed By

- Decision Engine
- SQLite Database
- Backend APIs
- Dashboard
- AI Assistant

---

## Required Columns

| Column           | Data Type |
| ---------------- | --------- |
| district         | String    |
| predicted_demand | Decimal   |

---

## Optional Columns

Examples include:

- forecast_period
- model_version
- generated_at

---

## Validation Rules

Prediction outputs shall satisfy the following requirements.

- Every district appears only once per forecasting period.
- Predicted values are numeric.
- Predicted values are non-negative.
- District names match the standardized master dataset.
- No duplicate prediction records exist.

---

# Clustering Output Contract

Clustering outputs are generated by the approved K-Means model.

These outputs provide analytical groupings used for visualization and district profiling.

Cluster identifiers are analytical labels only.

They are not rankings.

---

## Dataset Owner

Machine Learning Pipeline

---

## Repository Location

```text
data/processed/
```

---

## File Format

```text
CSV
```

---

## Naming Convention

```text
cluster_outputs.csv
```

---

## Produced By

Selected K-Means Model

---

## Consumed By

- Analytics Engine
- SQLite Database
- Dashboard
- AI Assistant

---

## Required Columns

| Column     | Data Type |
| ---------- | --------- |
| district   | String    |
| cluster_id | Integer   |

---

## Optional Columns

Examples include:

- generated_at
- model_version

---

## Validation Rules

The clustering output shall satisfy the following requirements.

- Every district belongs to exactly one cluster.
- Cluster identifiers are integers.
- District names are standardized.
- No duplicate district records exist.
- Cluster assignments remain reproducible for identical model artifacts.

# Decision Engine Dataset Contract

The Decision Engine consumes processed analytical outputs and machine learning predictions to generate the final district recommendations.

It represents the final stage of the project's data pipeline before application runtime.

The Decision Engine produces finalized recommendation outputs only.

Its internal scoring methodology remains implementation-dependent.

---

## Dataset Owner

Decision Engine

---

## Repository Location

```text
data/processed/
```

---

## Input Datasets

The Decision Engine consumes the following datasets.

| Dataset                  | Purpose                                   |
| ------------------------ | ----------------------------------------- |
| `master_dataset.csv`     | Historical and infrastructure information |
| `prediction_outputs.csv` | Forecasted charging demand                |
| `cluster_outputs.csv`    | District analytical grouping              |

---

## Output Dataset

```text
recommendation_outputs.csv
```

---

## Consumed By

- SQLite Database
- Backend Services
- Recommendation API
- Dashboard
- AI Assistant

---

## Required Columns

| Column         | Data Type |
| -------------- | --------- |
| district       | String    |
| priority_score | Decimal   |
| priority_level | String    |
| district_rank  | Integer   |

---

## Optional Columns

Examples include:

- generated_at
- recommendation_version

---

## Validation Rules

Recommendation outputs shall satisfy the following requirements.

- Every district appears exactly once.
- District rankings are unique.
- Priority scores are numeric.
- Priority scores are non-negative.
- Priority levels follow the approved recommendation categories.
- District names match the standardized master dataset.

---

# GeoJSON Contract

GeoJSON files provide geographic information used for rendering interactive district maps.

They are visualization resources only and are not used during machine learning model training.

---

## Dataset Owner

Data Processing Pipeline

---

## Repository Location

```text
data/external/
```

---

## File Format

```text
GeoJSON
```

---

## Naming Convention

```text
telangana_district_boundaries.geojson
```

---

## Coordinate Reference System

The dataset shall use the standard WGS84 geographic coordinate reference system.

---

## Required Properties

Each feature shall contain:

| Property | Required |
| -------- | -------- |
| district | Yes      |
| geometry | Yes      |

---

## Geometry Types

Supported geometry types include:

- Polygon
- MultiPolygon

---

## Validation Rules

The GeoJSON dataset shall satisfy the following requirements.

- Valid GeoJSON syntax.
- Valid polygon geometry.
- One feature per district.
- District names match the standardized processed datasets.
- No duplicate district features.
- No invalid coordinates.

---

# Joblib Model Contracts

Machine learning models are serialized after training and stored as Joblib artifacts.

These artifacts are loaded during backend startup and remain read-only during normal application execution.

---

# Regression Model Contract

## Purpose

Stores the selected regression model used to generate charging demand predictions.

---

## Repository Location

```text
models/
```

---

## File Format

```text
Joblib
```

---

## Naming Convention

```text
best_regression.joblib
```

---

## Produced By

Machine Learning Pipeline

---

## Consumed By

- Backend Prediction Service
- Prediction API
- Decision Engine

---

## Artifact Contents

The serialized artifact contains:

- Trained regression model
- Model parameters
- Learned weights

Implementation-specific metadata may also be stored where supported.

---

## Validation Rules

The regression artifact shall satisfy the following requirements.

- Successfully loads using Joblib.
- Compatible with the approved runtime environment.
- Produces deterministic predictions for identical inputs.
- Corresponds to the approved feature set.

---

# K-Means Model Contract

## Purpose

Stores the trained clustering model used for district profiling.

---

## Repository Location

```text
models/
```

---

## File Format

```text
Joblib
```

---

## Naming Convention

```text
kmeans.joblib
```

---

## Produced By

Machine Learning Pipeline

---

## Consumed By

- Analytics Engine
- Backend Analytics Service

---

## Artifact Contents

The serialized artifact contains:

- Trained K-Means model
- Cluster centroids
- Learned clustering parameters

---

## Validation Rules

The clustering artifact shall satisfy the following requirements.

- Successfully loads using Joblib.
- Compatible with the approved runtime environment.
- Produces deterministic cluster assignments for identical inputs.
- Corresponds to the approved training dataset.

---

# Model Versioning

Machine learning artifacts should include version information whenever models are retrained.

Recommended version information includes:

- Model version
- Training timestamp
- Dataset version
- Training pipeline version

Version information supports reproducibility while remaining independent of application runtime.

# Data Ownership Matrix

Every dataset and generated artifact has a single authoritative owner.

Ownership defines which project component is responsible for creating, maintaining, validating, and updating the dataset.

Other project modules consume the data but must not modify it directly.

---

| Dataset / Artifact                  | Owner                     | Primary Consumers                        |
| ----------------------------------- | ------------------------- | ---------------------------------------- |
| TGSPDCL Consumption Dataset         | Data Processing Pipeline  | Data Preprocessing                       |
| TGNPDCL Consumption Dataset         | Data Processing Pipeline  | Data Preprocessing                       |
| TGREDCO Charging Station Dataset    | Data Processing Pipeline  | Data Preprocessing                       |
| Telangana District Boundary GeoJSON | Data Processing Pipeline  | Backend Map Services, Frontend           |
| Clean Consumption Dataset           | Data Processing Pipeline  | Feature Engineering                      |
| Integrated Consumption Dataset      | Data Processing Pipeline  | Feature Engineering                      |
| Master Dataset                      | Data Processing Pipeline  | ML Pipeline, Database Initialization     |
| ML Training Dataset                 | Machine Learning Pipeline | Regression Training, Clustering Training |
| Prediction Outputs                  | Machine Learning Pipeline | Decision Engine, Backend                 |
| Clustering Outputs                  | Machine Learning Pipeline | Analytics Engine                         |
| Recommendation Outputs              | Decision Engine           | Database, Backend APIs                   |
| Regression Model Artifact           | Machine Learning Pipeline | Backend Prediction Service               |
| K-Means Model Artifact              | Machine Learning Pipeline | Backend Analytics Service                |

No dataset should have multiple owners.

---

# File Naming Conventions

Every dataset and generated artifact shall follow consistent naming conventions.

---

## General Rules

Dataset filenames shall:

- Use lowercase letters.
- Use snake_case.
- Avoid spaces.
- Use descriptive names.
- Include the appropriate file extension.

---

## Raw Datasets

Examples:

```text
tgspdcl_ev_consumption.csv

tgnpdcl_ev_consumption.csv

tgredco_charging_stations.csv
```

---

## Processed Datasets

Examples:

```text
clean_consumption_dataset.csv

integrated_consumption_dataset.csv

master_dataset.csv

ml_training_dataset.csv

prediction_outputs.csv

cluster_outputs.csv

recommendation_outputs.csv
```

---

## Geographic Files

Examples:

```text
telangana_district_boundaries.geojson
```

---

## Machine Learning Models

Examples:

```text
best_regression.joblib

kmeans.joblib
```

---

## Evaluation Artifacts

Examples:

```text
model_evaluation_report.json

feature_importance.csv
```

Evaluation artifact names should clearly describe their contents.

---

# Column Naming Conventions

Every processed dataset shall use consistent column names.

---

## General Rules

Column names shall:

- Use lowercase letters.
- Use snake_case.
- Avoid abbreviations.
- Clearly describe the stored value.

Examples:

```text
district

reporting_month

demand_kwh

charging_station_count

predicted_demand

priority_score

cluster_id
```

---

## Identifier Columns

Identifiers should use descriptive names.

Examples:

```text
district

cluster_id
```

---

## Numeric Columns

Examples:

```text
demand_kwh

predicted_demand

priority_score

district_rank
```

---

## Timestamp Columns

Examples:

```text
generated_at

created_at

updated_at
```

Timestamp fields should use ISO 8601 format whenever stored as text.

---

# Standard Data Types

Processed datasets shall use consistent logical data types.

| Data Type | Typical Usage                         |
| --------- | ------------------------------------- |
| String    | District names, labels, categories    |
| Integer   | Counts, rankings, cluster identifiers |
| Decimal   | Demand values, scores, coordinates    |
| Boolean   | Validation flags (if required)        |
| Datetime  | Generated timestamps                  |

These logical types remain implementation-independent.

---

# Missing Value Policy

Missing values shall be handled consistently throughout the preprocessing pipeline.

---

## Required Fields

Missing values are not permitted for required fields.

Examples include:

- district
- reporting_month
- demand_kwh

Records violating these requirements should be handled according to preprocessing rules before downstream processing.

---

## Optional Fields

Optional fields may contain missing values.

Examples include:

- station_name
- organization
- address
- latitude
- longitude

Missing optional values should not prevent dataset generation.

---

## Engineered Features

Machine learning feature columns shall not contain missing values before model training.

Any missing values shall be addressed during preprocessing.

---

# Validation Rules

Every generated dataset shall pass validation before being consumed by downstream modules.

---

## Structural Validation

Validation shall verify:

- Expected file exists.
- Expected columns exist.
- Correct file format.
- Valid encoding.
- Correct delimiter.

---

## Content Validation

Validation shall verify:

- Required fields are complete.
- Numeric values are valid.
- District names are standardized.
- No unexpected duplicate records exist.
- Invalid values are identified.

---

## Referential Validation

Where relationships exist:

- District names shall match the approved standardized district list.
- Generated datasets shall reference valid districts only.

---

## Geographic Validation

GeoJSON datasets shall verify:

- Valid geometry.
- One feature per district.
- Matching district names.

---

## Machine Learning Validation

Training datasets shall verify:

- Required features exist.
- Target variable exists.
- No missing required values.
- Compatible with approved model pipeline.

---

# Data Quality Expectations

Every processed dataset should satisfy the project's quality standards before downstream consumption.

---

## Completeness

Required fields shall be populated.

---

## Consistency

District names, timestamps, and categorical values shall remain standardized across every dataset.

---

## Accuracy

Processed values should accurately represent the official source datasets after preprocessing.

---

## Uniqueness

Duplicate records should be eliminated unless explicitly required.

---

## Validity

Numeric values, dates, and coordinates shall remain within acceptable ranges.

---

## Reproducibility

Executing the preprocessing pipeline using identical raw datasets shall always produce identical processed outputs.

# Versioning Strategy

Versioning ensures that datasets, generated artifacts, and machine learning models remain reproducible and traceable throughout the project lifecycle.

Only generated datasets and artifacts should be versioned.

Official raw datasets remain the authoritative source and should not be modified.

---

## Raw Datasets

Raw datasets retain their original filenames provided by the official data source.

If updated source datasets are obtained, they should be stored as separate files rather than overwriting previous versions.

---

## Processed Datasets

Processed datasets should always be regenerated from the corresponding raw datasets.

Version identifiers may be recorded through:

- Dataset generation timestamp
- Processing pipeline version
- Application metadata

The approved repository stores only the latest generated datasets required for application execution.

---

## Machine Learning Models

Serialized machine learning artifacts should include version information whenever retraining occurs.

Typical version metadata may include:

- Model version
- Dataset version
- Training timestamp
- Pipeline version

Version information supports reproducibility without affecting runtime APIs.

---

## Recommendation Outputs

Recommendation outputs should correspond to the latest prediction and analytics generation cycle.

Whenever predictions are regenerated, recommendation outputs should also be regenerated to maintain consistency.

---

## Database Initialization

SQLite runtime data should always originate from the latest approved processed datasets.

The database should not become an independent source of truth.

---

# Dataset Lifecycle

Every dataset follows a predictable lifecycle from acquisition to application runtime.

---

## Stage 1 — Raw Data Acquisition

Official datasets are collected from the approved organizations.

Outputs:

- TGSPDCL Consumption Dataset
- TGNPDCL Consumption Dataset
- TGREDCO Charging Station Dataset

---

## Stage 2 — Data Preprocessing

The preprocessing pipeline performs:

- Cleaning
- Standardization
- Validation
- Integration

Outputs:

- Clean Consumption Dataset
- Integrated Consumption Dataset
- Master Dataset

---

## Stage 3 — Feature Engineering

The Machine Learning Pipeline generates engineered features suitable for model training.

Output:

```text
ml_training_dataset.csv
```

---

## Stage 4 — Machine Learning

The training pipeline generates:

- Regression model
- K-Means clustering model

Outputs:

```text
best_regression.joblib

kmeans.joblib
```

---

## Stage 5 — Prediction Generation

The regression model generates charging demand forecasts.

Output:

```text
prediction_outputs.csv
```

---

## Stage 6 — Analytics Generation

The clustering model generates district analytical groupings.

Output:

```text
cluster_outputs.csv
```

---

## Stage 7 — Decision Engine

The Decision Engine combines processed information into final recommendations.

Output:

```text
recommendation_outputs.csv
```

---

## Stage 8 — Database Initialization

Processed datasets are imported into SQLite.

The backend uses SQLite as its runtime data source.

---

## Stage 9 — Application Runtime

During normal execution:

- Backend services query SQLite.
- Prediction and recommendation results are served through REST APIs.
- The frontend consumes standardized API responses.
- The AI Assistant receives processed application context prepared by the backend.

---

# Data Lineage

The following diagram summarizes the lineage of every major project dataset.

```text
TGSPDCL Consumption ─────────────┐
                                 │
TGNPDCL Consumption ─────────────┼────► Clean Dataset
                                 │
TGREDCO Stations ────────────────┘
                                        │
                                        ▼
                             Integrated Dataset
                                        │
                                        ▼
                                Master Dataset
                                        │
                      ┌─────────────────┴─────────────────┐
                      ▼                                   ▼
           Feature Engineering                 Database Initialization
                      │
                      ▼
          ML Training Dataset
               │           │
               ▼           ▼
      Regression Model   K-Means Model
               │           │
               ▼           ▼
     Prediction Outputs  Cluster Outputs
               └───────────┬───────────┘
                           ▼
                   Decision Engine
                           ▼
              Recommendation Outputs
                           ▼
                     SQLite Database
                           ▼
                     Backend Services
                           ▼
        Frontend Dashboard & AI Assistant
```

---

# Contract Change Management

Data contracts are intended to remain stable throughout implementation.

Changes should occur only when necessary and must remain consistent with the approved project documentation.

---

## Permitted Changes

Data contract modifications may be made when:

- Required by verified implementation constraints.
- Required to correct inconsistencies.
- Required by the project supervisor.
- Required to improve maintainability without expanding project scope.

---

## Restricted Changes

The following changes are not permitted without formal project approval:

- Introducing new datasets.
- Removing approved datasets.
- Changing standardized column names.
- Changing approved file formats.
- Altering machine learning artifact responsibilities.
- Expanding project scope.

---

## Impact Assessment

Before modifying a data contract, the following project documents should be reviewed for consistency:

- System Architecture
- Repository Structure
- API Specification
- Database Schema

Any approved modification should preserve compatibility across all implementation modules.

---

# Governance

This document defines the approved data contracts for EVision Telangana.

Every project module shall exchange data using the datasets, file formats, naming conventions, validation rules, and ownership responsibilities defined herein.

Data contract modifications should only be made when:

- Required by verified implementation constraints,
- Required to resolve data consistency issues,
- Required by the project supervisor,
- Required to improve maintainability without altering the approved project scope.

Changes must remain fully aligned with the approved Project Scope, Master Roadmap, Final Tech Stack, System Architecture, Repository Structure, Git Workflow, API Specification, and Database Schema.

---

# Conclusion

The Data Contracts document establishes a consistent, implementation-independent framework for managing every dataset, generated artifact, and machine learning input/output within EVision Telangana.

By defining standardized dataset structures, ownership, naming conventions, validation rules, versioning practices, and data lineage, the document enables reliable collaboration between the Data Processing Pipeline, Machine Learning Pipeline, Decision Engine, Database Layer, Backend Services, Frontend Application, and AI Assistant.

Together with the Repository Structure, API Specification, and Database Schema, these contracts provide a single source of truth for all data exchanged throughout the project lifecycle while ensuring reproducibility, maintainability, and consistency across the entire system.
