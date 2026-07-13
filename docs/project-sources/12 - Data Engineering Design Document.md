# Data Engineering Design Document

**Project:** EVision Telangana  
**Official Project Title:** AI-Based EV Charging Infrastructure Planning and Decision Support System for Telangana

**Version:** 1.0  
**Status:** Draft  
**Last Updated:** July 2026

---

# Purpose

This document defines the complete data engineering pipeline for EVision Telangana.

It serves as the bridge between the approved Project Sources and the implementation phase by specifying how raw datasets are collected, validated, cleaned, transformed, integrated, and prepared for machine learning, database storage, analytics, backend APIs, and frontend visualization.

This document becomes the single source of truth for all data processing activities throughout the project.

---

# Objectives

The Data Engineering Design aims to:

- Standardize the complete data pipeline.
- Define all project datasets.
- Design the Master Dataset.
- Define preprocessing workflows.
- Define feature engineering.
- Ensure reproducibility.
- Support database implementation.
- Support ML implementation.
- Maintain data quality.

---

# Data Engineering Pipeline

```text
Official Raw Datasets
        │
        ▼
Data Validation
        │
        ▼
Data Cleaning
        │
        ▼
Data Standardization
        │
        ▼
Circle → District Mapping
        │
        ▼
Dataset Integration
        │
        ▼
Feature Engineering
        │
        ▼
Master Dataset
        │
        ├────────► Database
        ├────────► Machine Learning
        ├────────► Dashboard
        ├────────► Analytics
        └────────► AI Assistant
```

---

# Directory Structure

```text
data/
│
├── raw/
│   ├── consumption/
│   │   ├── tgspdcl/
│   │   └── tgnpdcl/
│   │
│   ├── charging_stations/
│   ├── demographics/
│   ├── transport/
│   ├── infrastructure/
│   ├── economy/
│   └── geography/
│
├── mappings/
│   └── circle_to_district.csv
│
├── interim/
│
├── processed/
│
├── external/
│
└── reports/
```

---

# Dataset Inventory

## 1. Electricity Consumption

### Source

- TGSPDCL
- TGNPDCL

### Frequency

Monthly

### Raw Format

Multiple CSV files

### Granularity

Circle

### Target Granularity

District

### Purpose

Historical EV charging demand.

---

## 2. Charging Stations

### Source

TGREDCO

### Format

CSV

### Granularity

Individual Station

### Target Granularity

District

### Purpose

Existing charging infrastructure.

---

## 3. District Boundaries

### Source

Official Telangana GeoJSON

### Format

GeoJSON

### Granularity

District

### Purpose

Interactive map visualization.

---

## 4. Population

### Source

Census

### Purpose

Demand normalization.

---

## 5. EV Registrations

### Source

Transport Department

### Purpose

Demand estimation.

---

## 6. Road Network

### Source

OpenStreetMap / Government

### Purpose

Accessibility analysis.

---

## 7. Economic Data

### Source

Government Reports

### Purpose

Decision support.

---

# Master Dataset Design

Each row represents:

> **One District during One Month**

Example:

| District   | Month | Year |
| ---------- | ----- | ---- |
| Hyderabad  | Jan   | 2023 |
| Hyderabad  | Feb   | 2023 |
| Karimnagar | Jan   | 2023 |

---

# Feature Groups

---

## Identity Features

| Column         | Type    | Source      |
| -------------- | ------- | ----------- |
| district_id    | Integer | Generated   |
| district_name  | String  | GeoJSON     |
| month          | Integer | Consumption |
| year           | Integer | Consumption |
| reporting_date | Date    | Generated   |

---

## Geographic Features

| Column             | Type    |
| ------------------ | ------- |
| latitude           | Float   |
| longitude          | Float   |
| district_area_sqkm | Float   |
| geometry           | GeoJSON |

---

## Demographic Features

| Column             | Type    |
| ------------------ | ------- |
| population         | Integer |
| population_density | Float   |
| urban_population   | Integer |
| rural_population   | Integer |
| urban_percentage   | Float   |

---

## Electricity Features

| Column          | Type    |
| --------------- | ------- |
| energy_units    | Float   |
| sanctioned_load | Float   |
| total_services  | Integer |
| billed_services | Integer |

---

## Charging Infrastructure Features

| Column                 | Type    |
| ---------------------- | ------- |
| charging_station_count | Integer |
| public_station_count   | Integer |
| private_station_count  | Integer |

---

## Transportation Features

| Column                      | Type    |
| --------------------------- | ------- |
| ev_registrations            | Integer |
| total_vehicle_registrations | Integer |

---

## Infrastructure Features

| Column             | Type    |
| ------------------ | ------- |
| road_length_km     | Float   |
| highway_length_km  | Float   |
| municipality_count | Integer |

---

## Economic Features

| Column                | Type    |
| --------------------- | ------- |
| district_gdp          | Float   |
| per_capita_income     | Float   |
| industrial_area_count | Integer |

---

## Engineered Features

| Column                       |
| ---------------------------- |
| stations_per_100k_population |
| stations_per_sqkm            |
| units_per_station            |
| units_per_capita             |
| utilization_ratio            |
| demand_growth_rate           |
| rolling_average_3m           |
| rolling_average_6m           |
| rolling_average_12m          |

---

## Machine Learning Outputs

| Column           |
| ---------------- |
| predicted_demand |
| cluster_id       |

---

## Decision Engine Outputs

| Column             |
| ------------------ |
| priority_score     |
| priority_level     |
| infrastructure_gap |
| recommendation     |

---

# Circle to District Mapping

Since electricity consumption data is collected **circle-wise**, every record must first be mapped to a district before integration.

Pipeline:

```text
Circle
      │
      ▼
Circle → District Mapping
      │
      ▼
District
```

Mapping file:

```text
circle_to_district.csv
```

Example:

| Circle        | District  |
| ------------- | --------- |
| BANJARA HILLS | Hyderabad |
| CHARMINAR     | Hyderabad |
| SAIFABAD      | Hyderabad |
| ADILABAD      | Adilabad  |

---

# Data Processing Pipeline

## Stage 1

Validate datasets.

Checks include:

- File exists
- Correct columns
- Correct encoding
- Correct data types

---

## Stage 2

Clean datasets.

Operations include:

- Remove duplicates
- Handle missing values
- Standardize text
- Trim whitespace

---

## Stage 3

Standardize schema.

Examples:

```
Circle → circle
Units → units
Load → load
```

---

## Stage 4

Map circles to districts.

---

## Stage 5

Merge TGSPDCL and TGNPDCL datasets.

---

## Stage 6

Aggregate by:

- District
- Month
- Year

---

## Stage 7

Merge auxiliary datasets.

- Population
- Charging Stations
- Roads
- EV Registrations
- Geography

---

## Stage 8

Generate engineered features.

---

## Stage 9

Generate Master Dataset.

---

# Intermediate Outputs

```text
processed/

01_consumption_combined.csv

02_circle_mapped.csv

03_district_monthly.csv

04_master_dataset.csv

05_ml_training_dataset.csv
```

---

# Feature Engineering Specification

Derived features include:

### Infrastructure

- Stations per 100k population
- Stations per sq. km

### Demand

- Monthly growth
- Rolling averages
- Demand trend

### Utilization

- Units per station
- Load per station
- Service utilization ratio

### Accessibility

- Road density
- Highway density

---

# Data Validation Rules

Each preprocessing stage performs validation.

## Schema Validation

- Required columns exist.
- Correct data types.

---

## Missing Values

- Report null values.
- Fill or remove according to rules.

---

## Duplicate Records

Duplicates removed before processing.

---

## Geographic Validation

Every district must exist in GeoJSON.

---

## Circle Mapping Validation

Every circle must map to exactly one district.

No unmapped circles are permitted.

---

## Aggregation Validation

Monthly totals before and after aggregation must match.

---

# Data Quality Report

Generated automatically after preprocessing.

Contents:

- Row counts
- Missing values
- Duplicate records
- Invalid districts
- Unmapped circles
- Processing summary

---

# Output Contracts

## Database Dataset

Contains normalized tables for:

- Districts
- Historical Demand
- Charging Stations
- Demographics
- Predictions
- Recommendations

---

## ML Dataset

Contains:

- Numerical features
- Engineered features
- Target variable

No geometry fields.

---

## Dashboard Dataset

Contains:

- Aggregated statistics
- KPIs
- Charts
- Map-ready information

---

## AI Assistant Dataset

Contains:

- District summaries
- Predictions
- Recommendations
- Analytics

Optimized for natural language responses.

---

# Data Dictionary

Each dataset column will be documented.

Example:

| Column                 | Description                        | Unit    | Source          | Nullable | Used By         |
| ---------------------- | ---------------------------------- | ------- | --------------- | -------- | --------------- |
| energy_units           | Monthly EV electricity consumption | kWh     | TGSPDCL/TGNPDCL | No       | ML, Dashboard   |
| charging_station_count | Existing charging stations         | Count   | TGREDCO         | No       | Dashboard       |
| population             | District population                | Persons | Census          | No       | ML              |
| predicted_demand       | Forecasted charging demand         | kWh     | ML              | No       | Dashboard       |
| priority_score         | Decision engine score              | Score   | Decision Engine | No       | Recommendations |

---

# Deliverables

This document defines the blueprint for producing:

- Clean datasets
- Standardized datasets
- Master dataset
- ML dataset
- Database dataset
- Dashboard dataset
- AI-ready dataset

These outputs will serve as the foundation for the remaining implementation phases, including database design, machine learning, backend development, frontend visualization, analytics, and the AI assistant.

---

# Version History

| Version | Date      | Description                              |
| ------- | --------- | ---------------------------------------- |
| 1.0     | July 2026 | Initial Data Engineering Design Document |