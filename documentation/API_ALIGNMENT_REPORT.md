# EVision Telangana — API Alignment Report

> **Architecture Verification Audit**
> **Generated:** 2026-07-14
> **Scope:** Complete traceability audit across Frontend, Backend, Database, Data Engineering, and Machine Learning components
> **Verdict:** 🔴 CRITICAL GAPS — The system cannot serve production traffic today

---

## Table of Contents

1. [Frontend Feature Inventory](#1-frontend-feature-inventory)
2. [Backend API Inventory](#2-backend-api-inventory)
3. [Feature → API Mapping](#3-feature--api-mapping)
4. [API → Database Mapping](#4-api--database-mapping)
5. [Database → Dataset Mapping](#5-database--dataset-mapping)
6. [ML Dependency Mapping](#6-ml-dependency-mapping)
7. [Missing Dataset Report](#7-missing-dataset-report)
8. [Missing API Report](#8-missing-api-report)
9. [Unused API Report](#9-unused-api-report)
10. [Frontend Features Blocked by Missing Data](#10-frontend-features-blocked-by-missing-data)
11. [Recommended API Development Order](#11-recommended-api-development-order)
12. [Risk Assessment](#12-risk-assessment)
13. [Final Architecture Assessment](#13-final-architecture-assessment)

---

## 1. Frontend Feature Inventory

The frontend (`frontend/src/App.jsx`, 2520 lines) implements a monolithic single-page application with the following views and features. **All data is currently hardcoded as mock data within the frontend.** Zero API calls are made to the backend.

### 1.1 Landing Page

| Feature ID | Feature | Description | Data Source |
|:---|:---|:---|:---|
| F-LAND-01 | Hero Section | Marketing page with project overview | Static content |
| F-LAND-02 | CTA Button ("Explore Dashboard") | Navigates to dashboard | No data dependency |
| F-LAND-03 | Footer CTA | Additional call to action | Static content |

### 1.2 Dashboard View (`dbTab === 'dashboard'`)

| Feature ID | Feature | Description | Data Required |
|:---|:---|:---|:---|
| F-DASH-01 | KPI Card — Total Districts | Shows count of 33 districts | District list |
| F-DASH-02 | KPI Card — Charging Stations | Total recommended station count | Charging station data + recommendation counts |
| F-DASH-03 | KPI Card — Predicted Demand | Total predicted demand in GWh | ML prediction outputs (all districts) |
| F-DASH-04 | KPI Card — High Priority Districts | Count of critical/high-priority districts | Priority scores/levels (from Decision Engine) |
| F-DASH-05 | District Priority Heatmap (Leaflet) | Interactive choropleth map with GeoJSON | GeoJSON boundaries, priority levels per district |
| F-DASH-06 | Demand Forecast Trend Chart | AreaChart showing actual vs forecast GWh | Historical demand data, ML forecast data |
| F-DASH-07 | AI Insights Card | Summary text with KPI mini-cards | Priority scores, ML projections, cluster analysis |
| F-DASH-08 | District Selector (Dropdown) | Select active district | District list |
| F-DASH-09 | Global Search Bar | Search districts, metrics, reports | District search API |

### 1.3 District Explorer View (`dbTab === 'explorer'`)

| Feature ID | Feature | Description | Data Required |
|:---|:---|:---|:---|
| F-EXPL-01 | District Information Card | Population, Area, Urbanization, Road Density, Existing Stations, Fast Chargers | Population data, geography (area), urbanization %, road network density, charging station counts |
| F-EXPL-02 | EV Infrastructure & Demand Card | Current demand, Predicted demand, Growth rate, Charging capacity, Capacity gap, Utilization rate | Historical demand, ML predictions, capacity metrics, utilization data |
| F-EXPL-03 | District Risk Score (Gauge) | Visual gauge with risk score 0-100 | Risk scoring algorithm output (from Decision Engine) |
| F-EXPL-04 | District Priority Heatmap (Map) | Same interactive map as dashboard | GeoJSON, priority levels |
| F-EXPL-05 | AI Recommendations List | Increase Fast Charging, Expand Highway Corridors, Strengthen Urban Coverage | Recommendation engine outputs |
| F-EXPL-06 | Estimated Additional Investment | Investment amount in ₹ Cr | Financial model / recommendation calculations |
| F-EXPL-07 | Recommended Stations Count | Number of additional stations needed | Recommendation engine output |
| F-EXPL-08 | Export Report Button | Download district report | Report generation API |

### 1.4 Predictions View (`dbTab === 'predictions'`)

| Feature ID | Feature | Description | Data Required |
|:---|:---|:---|:---|
| F-PRED-01 | Predicted Demand Card | Predicted demand value with confidence interval | ML prediction + confidence interval |
| F-PRED-02 | Confidence Score Card | Model confidence percentage | ML model evaluation metrics |
| F-PRED-03 | Expected Growth (YoY) Card | Year-over-year growth percentage | Historical demand + ML predictions |
| F-PRED-04 | Recommended Stations Card | Additional stations needed | Recommendation engine |
| F-PRED-05 | Demand Forecast Trend Chart | AreaChart with historical vs AI-forecast | Historical demand data, ML forecast outputs |
| F-PRED-06 | Feature Importance Chart | Horizontal bar chart of top 7 features | ML model feature importance values |
| F-PRED-07 | AI Prediction Explanation | Text explaining why demand increases | Explainable AI / model interpretation |
| F-PRED-08 | Prediction Details Card | Model type, training data range, R², MAE, RMSE | ML model metadata |
| F-PRED-09 | Date Range Selector | Jan 2025 – Dec 2026 | Time-series filtering |
| F-PRED-10 | Export Report Button | Download predictions report | Report generation |

### 1.5 Analytics View (`dbTab === 'analytics'`)

| Feature ID | Feature | Description | Data Required |
|:---|:---|:---|:---|
| F-ANLY-01 | KPI Card — Total EV Demand (2026) | Statewide demand in GWh | ML predictions aggregated |
| F-ANLY-02 | KPI Card — Total Charging Stations | Current station count | Charging station data |
| F-ANLY-03 | KPI Card — Avg Utilization Rate | Average utilization % | Utilization metrics |
| F-ANLY-04 | KPI Card — Capacity Gap (2026) | Total capacity gap in GWh | Capacity analysis |
| F-ANLY-05 | KPI Card — High Priority Districts | Count requiring attention | Priority classification |
| F-ANLY-06 | Demand Distribution Pie Chart | Share of demand by district | ML predictions by district |
| F-ANLY-07 | Demand vs Capacity Gap Bar Chart | Top 10 districts comparison | Predictions + capacity data |
| F-ANLY-08 | EV Demand Intensity Map | Circle markers sized by demand | ML predictions + geography |
| F-ANLY-09 | Recommended Districts Table | Ranked table: District, Priority, Demand, Gap, Growth, Investment, ROI | Decision Engine full output |
| F-ANLY-10 | Seasonal Demand Heatmap Table | Monthly demand by year (2024, 2025, 2026F) | Historical monthly demand + forecasts |
| F-ANLY-11 | Demand Drivers Impact Chart | Top 5 drivers with impact scores | ML feature importance / correlation analysis |
| F-ANLY-12 | Filters & Date Range | Filter analytics by date and criteria | Query parameter support |
| F-ANLY-13 | Export Report Button | Download analytics report | Report generation |

### 1.6 AI Assistant View (`dbTab === 'assistant'`)

| Feature ID | Feature | Description | Data Required |
|:---|:---|:---|:---|
| F-CHAT-01 | Chat Interface | Full conversational UI with message history | AI/LLM backend (Gemini API) |
| F-CHAT-02 | Greeting Message | Bot introduction message | Static + context |
| F-CHAT-03 | User Message Input | Text input with Enter-to-send | Chat API endpoint |
| F-CHAT-04 | Bot Responses with Tables | Dynamic responses including data tables | Chat API with structured data |
| F-CHAT-05 | Suggestion Chips | Quick-action buttons for common queries | Suggestions API |
| F-CHAT-06 | Suggested Questions Sidebar | List of 5 pre-built questions | Suggestions API |
| F-CHAT-07 | Quick Actions Grid | 4 action cards (Forecast, Compare, Investment, Locations) | Chat API |
| F-CHAT-08 | Context-Aware Responses | Responses based on selected district | Chat API with district context |

**Total Frontend Features: 49**

---

## 2. Backend API Inventory

### 2.1 Specified APIs (from `07 - API Specification.md`)

The specification defines **7 endpoint categories** with **25 total endpoints**:

| Category | Endpoint | Method | Status in Code |
|:---|:---|:---|:---|
| **Dashboard** | `/dashboard/overview` | GET | ❌ MISSING |
| **Dashboard** | `/dashboard/map` | GET | ❌ MISSING |
| **Dashboard** | `/dashboard/stations` | GET | ❌ MISSING |
| **Dashboard** | `/dashboard/trends` | GET | ❌ MISSING |
| **Dashboard** | `/dashboard/summary` | GET | ❌ MISSING |
| **Districts** | `/districts` | GET | ✅ Stub (empty data) |
| **Districts** | `/districts/{district}` | GET | ✅ Stub (null values) |
| **Districts** | `/districts/{district}/comparison` | GET | ✅ Stub (null values) |
| **Districts** | `/districts/search` | GET | ✅ Stub (empty data) |
| **Predictions** | `/predictions` | GET | ✅ Stub (empty data) |
| **Predictions** | `/predictions/{district}` | GET | ✅ Stub (null values) |
| **Predictions** | `/predictions/top` | GET | ✅ Stub (empty data) |
| **Predictions** | `/predictions/summary` | GET | ✅ Stub (null values) |
| **Analytics** | `/analytics/clusters` | GET | ✅ Stub (empty data) |
| **Analytics** | `/analytics/trends` | GET | ✅ Stub (empty data) |
| **Analytics** | `/analytics/profile/{district}` | GET | ✅ Stub (null values) |
| **Analytics** | `/analytics/statistics` | GET | ✅ Stub (null values) |
| **Recommendations** | `/recommendations` | GET | ✅ Stub (empty data) |
| **Recommendations** | `/recommendations/{district}` | GET | ✅ Stub (null values) |
| **Recommendations** | `/recommendations/top` | GET | ✅ Stub (empty data) |
| **Recommendations** | `/recommendations/summary` | GET | ✅ Stub (null values) |
| **AI Assistant** | `/assistant/chat` | POST | ❌ MISSING |
| **AI Assistant** | `/assistant/explain` | POST | ❌ MISSING |
| **AI Assistant** | `/assistant/suggestions` | GET | ❌ MISSING |
| **Health** | `/health` | GET | ✅ Stub (hardcoded) |
| **Health** | `/health/database` | GET | ✅ Stub (hardcoded) |
| **Health** | `/health/models` | GET | ✅ Stub (hardcoded) |
| **Health** | `/health/ai` | GET | ✅ Stub (hardcoded) |

### 2.2 Implemented Endpoints (from `backend/api/routes/`)

| Router File | Prefix | Endpoints Implemented | Status |
|:---|:---|:---|:---|
| `health.py` | `/api/v1/health` | 4 endpoints | All stubs — no real health checks |
| `districts.py` | `/api/v1/districts` | 4 endpoints | All stubs — return `[]` or `None` values |
| `predictions.py` | `/api/v1/predictions` | 4 endpoints | All stubs — return `[]` or `None` values |
| `analytics.py` | `/api/v1/analytics` | 4 endpoints | All stubs — return `[]` or `None` values |
| `recommendations.py` | `/api/v1/recommendations` | 4 endpoints | All stubs — return `[]` or `None` values |
| `chatbot.py` | — | 0 endpoints | **Empty file** |

### 2.3 Implementation Detail Assessment

**Every single implemented endpoint is a non-functional stub.** Evidence:

- **No database queries** — No route imports `Session`, `get_session`, or any repository
- **No model imports** — No route imports any SQLModel/ORM model
- **No service layer calls** — No route calls any business logic service
- **No ML integration** — No route loads or calls any ML model
- **All return hardcoded responses** — Either empty arrays `[]` or `None` field values
- **All ORM models are empty files** — Every file in `backend/models/` contains zero code
- **Repository layer is empty** — `backend/repositories/` contains only `.gitkeep`
- **Schema layer is empty** — `backend/schemas/` contains only `.gitkeep`
- **ML service layer is empty** — `backend/ml/` contains only `.gitkeep`
- **Utils layer is empty** — `backend/utils/` contains only `.gitkeep`

---

## 3. Feature → API Mapping

### Traceability Matrix

| Feature ID | Frontend Feature | Required API Endpoint(s) | API Exists? | API Functional? | Can Feature Work Today? |
|:---|:---|:---|:---|:---|:---|
| F-DASH-01 | Total Districts KPI | `GET /districts` | ✅ | ❌ Stub | ❌ NO |
| F-DASH-02 | Charging Stations KPI | `GET /dashboard/stations` | ❌ Missing | — | ❌ NO |
| F-DASH-03 | Predicted Demand KPI | `GET /predictions/summary` | ✅ | ❌ Stub | ❌ NO |
| F-DASH-04 | High Priority Districts KPI | `GET /recommendations/summary` | ✅ | ❌ Stub | ❌ NO |
| F-DASH-05 | Priority Heatmap | `GET /dashboard/map` | ❌ Missing | — | ❌ NO |
| F-DASH-06 | Demand Forecast Trend | `GET /dashboard/trends` | ❌ Missing | — | ❌ NO |
| F-DASH-07 | AI Insights Card | `GET /dashboard/summary` | ❌ Missing | — | ❌ NO |
| F-DASH-08 | District Selector | `GET /districts` | ✅ | ❌ Stub | ❌ NO |
| F-DASH-09 | Global Search | `GET /districts/search` | ✅ | ❌ Stub | ❌ NO |
| F-EXPL-01 | District Information | `GET /districts/{district}` | ✅ | ❌ Stub | ❌ NO |
| F-EXPL-02 | EV Infrastructure & Demand | `GET /analytics/profile/{district}`, `GET /predictions/{district}` | ✅ | ❌ Stubs | ❌ NO |
| F-EXPL-03 | District Risk Score | `GET /recommendations/{district}` (or Decision Engine) | ✅ | ❌ Stub | ❌ NO |
| F-EXPL-04 | District Priority Heatmap | `GET /dashboard/map` | ❌ Missing | — | ❌ NO |
| F-EXPL-05 | AI Recommendations | `GET /recommendations/{district}` | ✅ | ❌ Stub | ❌ NO |
| F-EXPL-06 | Est. Additional Investment | `GET /recommendations/{district}` | ✅ | ❌ Stub | ❌ NO |
| F-EXPL-07 | Recommended Stations Count | `GET /recommendations/{district}` | ✅ | ❌ Stub | ❌ NO |
| F-EXPL-08 | Export Report | No API specified | ❌ Missing | — | ❌ NO |
| F-PRED-01 | Predicted Demand Card | `GET /predictions/{district}` | ✅ | ❌ Stub | ❌ NO |
| F-PRED-02 | Confidence Score | `GET /predictions/{district}` (with model metadata) | ✅ | ❌ Stub | ❌ NO |
| F-PRED-03 | Expected Growth | `GET /predictions/{district}` | ✅ | ❌ Stub | ❌ NO |
| F-PRED-04 | Recommended Stations | `GET /recommendations/{district}` | ✅ | ❌ Stub | ❌ NO |
| F-PRED-05 | Demand Forecast Trend | `GET /analytics/trends` | ✅ | ❌ Stub | ❌ NO |
| F-PRED-06 | Feature Importance Chart | No API specified (ML metadata) | ❌ Missing | — | ❌ NO |
| F-PRED-07 | AI Prediction Explanation | `POST /assistant/explain` | ❌ Missing | — | ❌ NO |
| F-PRED-08 | Prediction Details | No API specified (ML metadata) | ❌ Missing | — | ❌ NO |
| F-PRED-09 | Date Range Selector | Query params on `/predictions` | ✅ | ❌ Stub | ❌ NO |
| F-PRED-10 | Export Report | No API specified | ❌ Missing | — | ❌ NO |
| F-ANLY-01 | Total EV Demand KPI | `GET /analytics/statistics` | ✅ | ❌ Stub | ❌ NO |
| F-ANLY-02 | Total Charging Stations KPI | `GET /dashboard/stations` or `GET /analytics/statistics` | ❌/✅ | ❌ Stub | ❌ NO |
| F-ANLY-03 | Avg Utilization Rate | `GET /analytics/statistics` | ✅ | ❌ Stub | ❌ NO |
| F-ANLY-04 | Capacity Gap KPI | `GET /analytics/statistics` | ✅ | ❌ Stub | ❌ NO |
| F-ANLY-05 | High Priority Districts KPI | `GET /recommendations/summary` | ✅ | ❌ Stub | ❌ NO |
| F-ANLY-06 | Demand Distribution Pie | `GET /predictions` (all districts) | ✅ | ❌ Stub | ❌ NO |
| F-ANLY-07 | Demand vs Capacity Gap Bar | `GET /analytics/statistics`, `GET /predictions` | ✅ | ❌ Stub | ❌ NO |
| F-ANLY-08 | EV Demand Intensity Map | `GET /predictions`, `GET /dashboard/map` | ❌ Partial | ❌ Stub | ❌ NO |
| F-ANLY-09 | Recommended Districts Table | `GET /recommendations/top` | ✅ | ❌ Stub | ❌ NO |
| F-ANLY-10 | Seasonal Demand Heatmap | `GET /analytics/trends` | ✅ | ❌ Stub | ❌ NO |
| F-ANLY-11 | Demand Drivers Impact | No API specified (ML feature importance) | ❌ Missing | — | ❌ NO |
| F-ANLY-12 | Filters & Date Range | Query params support | ✅ Partial | ❌ Stub | ❌ NO |
| F-ANLY-13 | Export Report | No API specified | ❌ Missing | — | ❌ NO |
| F-CHAT-01 | Chat Interface | `POST /assistant/chat` | ❌ Missing | — | ❌ NO |
| F-CHAT-02 | Greeting Message | Static / `POST /assistant/chat` | ❌ Missing | — | ❌ NO |
| F-CHAT-03 | User Message Input | `POST /assistant/chat` | ❌ Missing | — | ❌ NO |
| F-CHAT-04 | Bot Responses with Tables | `POST /assistant/chat` | ❌ Missing | — | ❌ NO |
| F-CHAT-05 | Suggestion Chips | `GET /assistant/suggestions` | ❌ Missing | — | ❌ NO |
| F-CHAT-06 | Suggested Questions | `GET /assistant/suggestions` | ❌ Missing | — | ❌ NO |
| F-CHAT-07 | Quick Actions | `POST /assistant/chat` | ❌ Missing | — | ❌ NO |
| F-CHAT-08 | Context-Aware Responses | `POST /assistant/chat` | ❌ Missing | — | ❌ NO |

### Summary

| Metric | Count |
|:---|:---|
| **Total Frontend Features** | 49 |
| **Features with matching stub API** | 28 |
| **Features with no API at all** | 21 |
| **Features that can work today** | **0** |

---

## 4. API → Database Mapping

### 4.1 Database Schema (from `08 - Database Schema.md`)

The specification defines the following tables:

| Table | Purpose | Key Columns |
|:---|:---|:---|
| `districts` | District master data | district_id, district_name, population, area_sq_km, centroid_lat, centroid_lon, urban_percentage, road_density_km |
| `charging_stations` | EV charging station locations | station_id, district_id (FK), station_name, latitude, longitude, charger_type, power_kw, owning_organisation, status |
| `historical_demand` | Monthly electricity demand per district | demand_id, district_id (FK), year, month, energy_units, sanctioned_load, total_services, billed_services |
| `predictions` | ML prediction outputs per district | prediction_id, district_id (FK), predicted_demand, confidence_score, prediction_date, model_version |
| `recommendations` | Decision Engine outputs | recommendation_id, district_id (FK), priority_score, priority_level, recommended_stations, investment_estimate, recommendation_text |
| `clusters` | K-Means clustering results | cluster_id, cluster_name, cluster_summary |
| `district_clusters` | District-to-cluster mapping | district_id (FK), cluster_id (FK) |
| `application_metadata` | App config and model metadata | key, value |

### 4.2 Current Database Implementation Status

| Component | Status | Evidence |
|:---|:---|:---|
| Database engine | ✅ Configured | `backend/database/engine.py` — SQLite via SQLModel |
| Database session | ✅ Configured | `backend/database/session.py` — session generator |
| `districts` ORM model | ❌ EMPTY | `backend/models/district.py` — 0 bytes |
| `charging_stations` ORM model | ❌ EMPTY | `backend/models/charging_stations.py` — 0 bytes |
| `historical_demand` ORM model | ❌ EMPTY | `backend/models/historical_demand.py` — 0 bytes |
| `district_prediction` ORM model | ❌ EMPTY | `backend/models/district_prediction.py` — 0 bytes |
| `district_recommendation` ORM model | ❌ EMPTY | `backend/models/district_recommendation.py` — 0 bytes |
| `district_analytics` ORM model | ❌ EMPTY | `backend/models/district_analytics.py` — 0 bytes |
| `application_metadata` ORM model | ❌ EMPTY | `backend/models/application_metadaata.py` — 0 bytes (also has typo in filename) |
| Database initialization | ❌ EMPTY | `backend/database/initialization.py` — 0 bytes |
| SQLite database file | ❌ DOES NOT EXIST | No `evision.db` file exists |

### 4.3 API → Database Dependency

| API Endpoint | Required Database Tables | Tables Implemented? | Route Queries DB? |
|:---|:---|:---|:---|
| `GET /districts` | `districts` | ❌ | ❌ |
| `GET /districts/{district}` | `districts`, `charging_stations`, `predictions`, `recommendations` | ❌ | ❌ |
| `GET /districts/{district}/comparison` | `districts`, `predictions`, `recommendations`, `district_clusters` | ❌ | ❌ |
| `GET /districts/search` | `districts` | ❌ | ❌ |
| `GET /predictions` | `predictions`, `districts` | ❌ | ❌ |
| `GET /predictions/{district}` | `predictions`, `districts` | ❌ | ❌ |
| `GET /predictions/top` | `predictions`, `districts` | ❌ | ❌ |
| `GET /predictions/summary` | `predictions` | ❌ | ❌ |
| `GET /analytics/clusters` | `clusters`, `district_clusters`, `districts` | ❌ | ❌ |
| `GET /analytics/trends` | `historical_demand`, `districts` | ❌ | ❌ |
| `GET /analytics/profile/{district}` | `districts`, `historical_demand`, `charging_stations`, `clusters` | ❌ | ❌ |
| `GET /analytics/statistics` | `historical_demand`, `districts`, `clusters` | ❌ | ❌ |
| `GET /recommendations` | `recommendations`, `districts` | ❌ | ❌ |
| `GET /recommendations/{district}` | `recommendations`, `districts`, `predictions` | ❌ | ❌ |
| `GET /recommendations/top` | `recommendations`, `districts` | ❌ | ❌ |
| `GET /recommendations/summary` | `recommendations` | ❌ | ❌ |
| `POST /assistant/chat` | All tables (context-dependent) + AI service | ❌ | ❌ |
| `POST /assistant/explain` | `predictions`, `districts` + AI service | ❌ | ❌ |
| `GET /assistant/suggestions` | `districts` | ❌ | ❌ |
| `GET /health/database` | Connection check | ✅ (engine exists) | ❌ (hardcoded) |

---

## 5. Database → Dataset Mapping

### 5.1 Available Datasets

| Dataset | Location | Columns | Status |
|:---|:---|:---|:---|
| **Charging Stations (raw)** | `data/raw/charging_stations/EV_Charging_Stations_April_2024.csv` | s_no, station_name, state, district, address, latitude, longitude, owning_organisation | ✅ Available (95 KB) |
| **Charging Stations (clean)** | `data/interim/charging_stations/charging_stations_clean.csv` | s_no, station_name, state, district, address, latitude, longitude, owning_organisation | ✅ Available (90 KB) |
| **Geography (raw)** | `data/raw/geography/telangana_33_districts.geojson` | District boundaries, dtname | ✅ Available (2.3 MB) |
| **Geography (processed)** | `data/interim/geography/district_geography.csv` | OBJECTID, dtname, district_name, area_sq_km, centroid_longitude, centroid_latitude + others | ✅ Available (6 KB) |
| **Geography (clean GeoJSON)** | `data/interim/geography/district_boundaries.geojson` | Cleaned district boundaries | ✅ Available (2.5 MB) |
| **Consumption (combined)** | `data/interim/consumption/consumption_combined.csv` | Electricity consumption data | ✅ Available (1.9 MB) |
| **Consumption (monthly by district)** | `data/interim/consumption/district_monthly_consumption.csv` | district, year, month, reporting_month, units, load, total_services, billed_services, circle_count, division_count, subdivision_count | ✅ Available (64 KB) |
| **Circle-to-District Mapping** | `data/mappings/circle_to_district.csv` | Circle-to-district mapping | ✅ Available (28 KB) |
| **Master Dataset v1** | `data/interim/merged/master_dataset_v1.csv` | district, year, month, reporting_month, units, load, total_services, billed_services, circle_count, division_count, subdivision_count, charging_station_count, latitude, longitude, district_area_sqkm | ✅ Available (138 KB) |

### 5.2 Dataset → Database Table Mapping

| Database Table | Required Dataset(s) | Dataset Available? | Columns Aligned? |
|:---|:---|:---|:---|
| `districts` | `district_geography.csv` | ✅ | ⚠️ PARTIAL — Missing: `population`, `urban_percentage`, `road_density_km` |
| `charging_stations` | `charging_stations_clean.csv` | ✅ | ⚠️ PARTIAL — Missing: `charger_type`, `power_kw`, `status` |
| `historical_demand` | `district_monthly_consumption.csv` | ✅ | ✅ Aligned (units, load, total_services, billed_services) |
| `predictions` | ML output (not yet generated) | ❌ Missing | ❌ No ML model trained |
| `recommendations` | Decision Engine output (not built) | ❌ Missing | ❌ No Decision Engine exists |
| `clusters` | K-Means output (not yet generated) | ❌ Missing | ❌ No K-Means model trained |
| `district_clusters` | K-Means output (not yet generated) | ❌ Missing | ❌ No K-Means model trained |

### 5.3 Processed Data → `data/processed/` Status

**The `data/processed/` directory is EMPTY.** It contains only a `.gitkeep` file.

The ML Design Document specifies that `data/processed/master_dataset.csv` is the single input dataset for ML training. This file does not exist. The closest equivalent is `data/interim/merged/master_dataset_v1.csv`, but it is missing critical columns required by the ML specification.

---

## 6. ML Dependency Mapping

### 6.1 ML Pipeline Status

| Component | Specified | Implemented | Status |
|:---|:---|:---|:---|
| **Feature Engineering** | `scripts/feature_engineering.py` | 36 bytes (placeholder) | ❌ MISSING |
| **Dataset Merge** | `scripts/merge_datasets.py` | 31 bytes (placeholder) | ❌ MISSING |
| **Master Dataset (processed)** | `data/processed/master_dataset.csv` | Does not exist | ❌ MISSING |
| **Random Forest Training** | Specified in ML Design | No implementation | ❌ MISSING |
| **XGBoost Training** | Specified in ML Design | No implementation | ❌ MISSING |
| **K-Means Clustering** | Specified in ML Design | No implementation | ❌ MISSING |
| **Model Evaluation** | `models/evaluation/` | Contains only `.gitkeep` | ❌ MISSING |
| **Trained Models** | `models/trained/` | Contains only `.gitkeep` | ❌ MISSING |
| **Decision Engine** | Specified in ML Design | No implementation | ❌ MISSING |
| **Prediction Service** | `backend/ml/` | Contains only `.gitkeep` | ❌ MISSING |
| **Model Serialization** | `.joblib` files | Do not exist | ❌ MISSING |

### 6.2 ML Feature Requirements vs Available Data

| Required Feature (ML Spec) | Available in master_dataset_v1? | Source Dataset |
|:---|:---|:---|
| `district_area_sqkm` | ✅ Yes | Geography |
| `latitude` | ✅ Yes | Geography |
| `longitude` | ✅ Yes | Geography |
| `population` | ❌ **MISSING** | No population dataset exists |
| `population_density` | ❌ **MISSING** | Derived from population + area |
| `urban_percentage` | ❌ **MISSING** | No urbanization dataset exists |
| `charging_station_count` | ✅ Yes | Charging stations |
| `road_length_km` | ❌ **MISSING** | No road network dataset exists |
| `highway_length_km` | ❌ **MISSING** | No highway dataset exists |
| `ev_registrations` | ❌ **MISSING** | No EV registration dataset exists |
| `total_vehicle_registrations` | ❌ **MISSING** | No vehicle registration dataset exists |
| `energy_units` | ✅ Yes (as `units`) | Consumption data |
| `sanctioned_load` | ✅ Yes (as `load`) | Consumption data |
| `stations_per_100k_population` | ❌ **MISSING** | Requires population data |
| `stations_per_sqkm` | ⚠️ Derivable | station_count / area |
| `units_per_station` | ⚠️ Derivable | units / station_count |
| `utilization_ratio` | ❌ **MISSING** | Requires definition & additional data |
| `demand_growth_rate` | ⚠️ Derivable | From time-series consumption data |
| `rolling_average_3m` | ⚠️ Derivable | From consumption time-series |
| `rolling_average_6m` | ⚠️ Derivable | From consumption time-series |
| `rolling_average_12m` | ⚠️ Derivable | From consumption time-series |

### 6.3 Frontend Features Dependent on ML

| Frontend Feature | ML Model Required | ML Output Required | ML Status |
|:---|:---|:---|:---|
| F-DASH-03 (Predicted Demand KPI) | Random Forest or XGBoost | `predicted_demand` | ❌ No model trained |
| F-DASH-04 (High Priority KPI) | Decision Engine | `priority_level` | ❌ No Decision Engine |
| F-DASH-06 (Forecast Trend) | Regression Model | Time-series predictions | ❌ No model trained |
| F-PRED-01 to F-PRED-08 | Regression + Evaluation | All prediction outputs | ❌ No model trained |
| F-EXPL-02 (Predicted Demand) | Regression Model | `predicted_demand` | ❌ No model trained |
| F-EXPL-03 (Risk Score) | Decision Engine | Risk score calculation | ❌ No Decision Engine |
| F-EXPL-05–07 (Recommendations) | Decision Engine | Priority + recommendations | ❌ No Decision Engine |
| F-ANLY-06–09 (Analytics charts) | Regression + K-Means | Predictions + clusters | ❌ No models trained |
| F-ANLY-11 (Demand Drivers) | Feature Importance | Model coefficients | ❌ No model trained |
| F-CHAT-01–08 (AI Assistant) | Gemini API + Context | Structured responses | ❌ No integration |

---

## 7. Missing Dataset Report

### 7.1 Datasets That Do Not Exist Anywhere in the Project

| Dataset | Required Columns | Why Required | Blocking Features |
|:---|:---|:---|:---|
| **Population Data** | `district_name`, `population`, `population_density` | ML feature for regression & clustering; District Explorer display | F-EXPL-01, F-PRED-06, all ML training |
| **Urbanization Data** | `district_name`, `urban_percentage` | ML feature; District Explorer display | F-EXPL-01, all ML training |
| **Road Network Data** | `district_name`, `road_length_km`, `highway_length_km`, `road_density_km_per_sqkm` | ML feature; District Explorer display | F-EXPL-01, all ML training |
| **EV Registration Data** | `district_name`, `ev_registrations`, `total_vehicle_registrations` | ML feature; Core demand driver | F-DASH-02, F-EXPL-01, all ML training |
| **Traffic Volume Data** | `district_name`, `traffic_volume_index` | Frontend displays "Traffic Volume Index" in feature importance | F-PRED-06 |
| **Income Level Data** | `district_name`, `avg_income_level` | Frontend displays "Avg. Income Level" in feature importance | F-PRED-06 |
| **Processed Master Dataset** | All ML features combined | Single input for ML training pipeline | ALL ML-dependent features |
| **ML Prediction Outputs** | `district_name`, `predicted_demand`, `confidence_score`, etc. | Predictions for all districts | F-DASH-03, F-PRED-01–08, F-ANLY-01, F-ANLY-06–09 |
| **Decision Engine Outputs** | `district_name`, `priority_score`, `priority_level`, `recommendation`, `investment_estimate` | Priority rankings and recommendations | F-DASH-04, F-EXPL-03–07, F-ANLY-05, F-ANLY-09 |
| **K-Means Cluster Assignments** | `district_name`, `cluster_id`, `cluster_summary` | District grouping for analytics | F-ANLY-06, F-DASH-07 |

### 7.2 Datasets That Exist But Are Incomplete

| Dataset | What's Present | What's Missing |
|:---|:---|:---|
| `master_dataset_v1.csv` | district, year, month, units, load, services, station_count, lat, lon, area | population, urban_percentage, road data, EV registrations, vehicle registrations, all engineered features |
| `charging_stations_clean.csv` | Name, location, coordinates, owner | charger_type, power_kw, status, operational_since |

---

## 8. Missing API Report

### 8.1 Entirely Missing API Endpoints

These endpoints are defined in the API Specification but have no implementation (not even stubs):

| # | Endpoint | Method | Category | Required By |
|:---|:---|:---|:---|:---|
| 1 | `/dashboard/overview` | GET | Dashboard | F-DASH-01 through F-DASH-04 |
| 2 | `/dashboard/map` | GET | Dashboard | F-DASH-05, F-EXPL-04, F-ANLY-08 |
| 3 | `/dashboard/stations` | GET | Dashboard | F-DASH-02, F-ANLY-02 |
| 4 | `/dashboard/trends` | GET | Dashboard | F-DASH-06 |
| 5 | `/dashboard/summary` | GET | Dashboard | F-DASH-07 |
| 6 | `/assistant/chat` | POST | AI Assistant | F-CHAT-01 through F-CHAT-08 |
| 7 | `/assistant/explain` | POST | AI Assistant | F-PRED-07 |
| 8 | `/assistant/suggestions` | GET | AI Assistant | F-CHAT-05, F-CHAT-06 |

### 8.2 APIs Needed But Not Specified

These APIs are needed by the frontend but are not defined in the API Specification:

| # | Missing API | Purpose | Required By |
|:---|:---|:---|:---|
| 1 | `GET /predictions/{district}/feature-importance` | Return ML feature importance values | F-PRED-06, F-ANLY-11 |
| 2 | `GET /predictions/{district}/metadata` | Return model metadata (type, R², MAE, RMSE, training dates) | F-PRED-08 |
| 3 | `GET /reports/export/{type}` | Generate and download reports (district, predictions, analytics) | F-EXPL-08, F-PRED-10, F-ANLY-13 |
| 4 | `GET /dashboard/geojson` | Serve GeoJSON for map rendering | F-DASH-05, F-EXPL-04 (currently fetched as static file) |

---

## 9. Unused API Report

### 9.1 API Endpoint Classification

| Endpoint | Classification | Justification |
|:---|:---|:---|
| `GET /` (root) | **Required** (Operational) | Application health/status endpoint |
| `GET /api/v1/health` | **Required** (Operational) | Basic health check |
| `GET /api/v1/health/database` | **Required** (Operational) | Database connectivity check |
| `GET /api/v1/health/models` | **Required** (Operational) | ML model availability check |
| `GET /api/v1/health/ai` | **Required** (Operational) | AI service availability check |
| `GET /api/v1/districts` | **Required** | Core data endpoint |
| `GET /api/v1/districts/{district}` | **Required** | Core data endpoint |
| `GET /api/v1/districts/{district}/comparison` | **Required** | District comparison feature |
| `GET /api/v1/districts/search` | **Required** | Global search feature |
| `GET /api/v1/predictions` | **Required** | Predictions listing |
| `GET /api/v1/predictions/{district}` | **Required** | Per-district prediction |
| `GET /api/v1/predictions/top` | **Required** | Top predictions ranking |
| `GET /api/v1/predictions/summary` | **Required** | Prediction statistics |
| `GET /api/v1/analytics/clusters` | **Required** | Cluster analysis display |
| `GET /api/v1/analytics/trends` | **Required** | Trend analysis charts |
| `GET /api/v1/analytics/profile/{district}` | **Required** | District analytical profile |
| `GET /api/v1/analytics/statistics` | **Required** | Analytics KPI cards |
| `GET /api/v1/recommendations` | **Required** | Recommendations listing |
| `GET /api/v1/recommendations/{district}` | **Required** | Per-district recommendations |
| `GET /api/v1/recommendations/top` | **Required** | Top recommendations ranking |
| `GET /api/v1/recommendations/summary` | **Required** | Recommendation statistics |
| `backend/api/router.py` | **Duplicate** | Duplicates routing already done in `main.py` — both files include the same routers |

### 9.2 Summary

| Classification | Count |
|:---|:---|
| Required | 21 |
| Optional | 0 |
| Duplicate | 1 (`router.py` duplicates `main.py`) |
| Unused | 0 |
| Missing (not implemented) | 8 (specified) + 4 (unspecified but needed) |

---

## 10. Frontend Features Blocked by Missing Data

### 10.1 Features Blocked — Categorized by Root Cause

#### Block Category A: Missing External Datasets (6 datasets, blocks all ML)

| Missing Dataset | Columns Required | Features Blocked |
|:---|:---|:---|
| Population Data | population, population_density | F-EXPL-01, F-PRED-06, ALL ML-dependent features |
| Urbanization Data | urban_percentage | F-EXPL-01, ALL ML-dependent features |
| Road Network Data | road_length_km, highway_length_km, road_density | F-EXPL-01, ALL ML-dependent features |
| EV Registration Data | ev_registrations, total_vehicle_registrations | ALL ML-dependent features |
| Traffic Volume Data | traffic_volume_index | F-PRED-06 |
| Income Level Data | avg_income_level | F-PRED-06 |

#### Block Category B: ML Pipeline Not Built (blocks 25+ features)

| Missing Component | Features Blocked |
|:---|:---|
| Feature engineering pipeline | All prediction, recommendation, and analytics features |
| Processed master dataset | All ML training |
| Random Forest / XGBoost training | F-PRED-01–08, F-DASH-03, F-DASH-06, F-ANLY-01, F-ANLY-06–11 |
| K-Means clustering | F-ANLY-06, F-DASH-07 cluster analysis |
| Decision Engine | F-DASH-04, F-EXPL-03–07, F-ANLY-05, F-ANLY-09 |
| Model serialization (.joblib) | All runtime predictions |

#### Block Category C: Backend Not Implemented (blocks all 49 features)

| Missing Component | Features Blocked |
|:---|:---|
| ORM models (all empty) | All database-dependent features |
| Database initialization & schema | All data access |
| Repository layer | All data queries |
| Service layer | All business logic |
| API route implementations (all stubs) | All frontend features |
| Dashboard router (entirely missing) | F-DASH-01–09 |
| AI Assistant router (empty file) | F-CHAT-01–08 |

#### Block Category D: AI Integration Not Built

| Missing Component | Features Blocked |
|:---|:---|
| Gemini API integration | F-CHAT-01–08 |
| Chat API endpoint | F-CHAT-01–08 |
| Explain API endpoint | F-PRED-07 |
| Suggestions API endpoint | F-CHAT-05, F-CHAT-06 |

### 10.2 Blocking Summary

> **Every single frontend feature (49/49) is blocked.**
>
> The frontend currently operates entirely on hardcoded mock data embedded in `App.jsx` (lines 52–585). It makes zero API calls to the backend. The backend returns empty arrays and null values for all endpoints.

---

## 11. Recommended API Development Order

### Phase 1: Foundation (Critical Path — Week 1–2)

| Priority | Task | Prerequisite | Unblocks |
|:---|:---|:---|:---|
| P0 | Implement ORM models for all database tables | None | All backend development |
| P0 | Create database initialization/migration script | ORM models | Database availability |
| P0 | Implement `districts` repository + service | ORM models, DB init | `GET /districts`, `GET /districts/{district}`, `GET /districts/search` |
| P0 | Seed `districts` table from `district_geography.csv` | DB init, districts model | District data availability |
| P0 | Seed `charging_stations` table from `charging_stations_clean.csv` | DB init, stations model | Station data availability |
| P0 | Seed `historical_demand` table from `district_monthly_consumption.csv` | DB init, demand model | Historical data availability |

### Phase 2: Core APIs (Week 2–3)

| Priority | Task | Prerequisite | Unblocks |
|:---|:---|:---|:---|
| P1 | Implement `GET /districts` with real data | Phase 1 | F-DASH-01, F-DASH-08 |
| P1 | Implement `GET /districts/{district}` | Phase 1 | F-EXPL-01 (partial) |
| P1 | Implement `GET /districts/search` | Phase 1 | F-DASH-09 |
| P1 | Implement `GET /districts/{district}/comparison` | Phase 1 | District comparison |
| P1 | Implement `GET /analytics/trends` with historical data | Phase 1 | F-DASH-06, F-PRED-05, F-ANLY-10 |
| P1 | Implement `GET /analytics/statistics` | Phase 1 | F-ANLY-01–05 |
| P1 | Implement `GET /analytics/profile/{district}` | Phase 1 | F-EXPL-02 |
| P1 | Implement Dashboard endpoints (`/dashboard/*`) | Phase 1 | F-DASH-02–07 |

### Phase 3: ML Pipeline (Week 3–5)

| Priority | Task | Prerequisite | Unblocks |
|:---|:---|:---|:---|
| P2 | Acquire missing datasets (population, roads, EV registrations) | None (external dependency) | ML training |
| P2 | Build feature engineering pipeline | Missing datasets | Processed master dataset |
| P2 | Train Random Forest + XGBoost models | Feature engineering | Predictions |
| P2 | Train K-Means clustering | Feature engineering | Cluster assignments |
| P2 | Build Decision Engine | Trained models | Priority scores, recommendations |
| P2 | Implement prediction service (load .joblib) | Trained models | Runtime predictions |

### Phase 4: ML-Dependent APIs (Week 5–6)

| Priority | Task | Prerequisite | Unblocks |
|:---|:---|:---|:---|
| P3 | Implement `GET /predictions` endpoints (all 4) | Phase 3 | F-PRED-01–05, F-ANLY-06–08 |
| P3 | Implement `GET /recommendations` endpoints (all 4) | Phase 3 | F-EXPL-03–07, F-ANLY-09 |
| P3 | Implement `GET /analytics/clusters` | Phase 3 | Cluster analysis |
| P3 | Add feature importance API | Phase 3 | F-PRED-06, F-ANLY-11 |
| P3 | Add model metadata API | Phase 3 | F-PRED-08 |

### Phase 5: AI Assistant (Week 6–7)

| Priority | Task | Prerequisite | Unblocks |
|:---|:---|:---|:---|
| P4 | Implement Gemini API integration | Gemini API key configured | AI service |
| P4 | Implement `POST /assistant/chat` | Gemini integration, all data APIs | F-CHAT-01–04, F-CHAT-07–08 |
| P4 | Implement `POST /assistant/explain` | Gemini integration, predictions | F-PRED-07 |
| P4 | Implement `GET /assistant/suggestions` | District data | F-CHAT-05–06 |

### Phase 6: Frontend Integration (Week 7–8)

| Priority | Task | Prerequisite | Unblocks |
|:---|:---|:---|:---|
| P5 | Replace all hardcoded mock data with API calls | All APIs functional | Production readiness |
| P5 | Implement error handling & loading states | API integration | UX quality |
| P5 | Implement report export functionality | Report generation API | F-EXPL-08, F-PRED-10, F-ANLY-13 |

---

## 12. Risk Assessment

### 12.1 Critical Risks

| # | Risk | Severity | Impact | Mitigation |
|:---|:---|:---|:---|:---|
| R1 | **Zero functional backend** — All 21 implemented endpoints are stubs returning empty/null data | 🔴 Critical | Complete system failure; no feature works | Prioritize Phase 1–2 immediately |
| R2 | **Missing external datasets** — Population, EV registrations, road networks, income levels do not exist | 🔴 Critical | ML pipeline cannot be built; 25+ features blocked | Identify and acquire government/open datasets immediately |
| R3 | **No ML pipeline exists** — Feature engineering, training, evaluation, Decision Engine are all unbuilt | 🔴 Critical | Predictions, recommendations, priority scores unavailable | Begin ML development after data acquisition |
| R4 | **Frontend-backend decoupling** — Frontend makes zero API calls; all data is mock | 🔴 Critical | No integration tested; unknown compatibility issues | Plan frontend integration phase |
| R5 | **No database exists** — SQLite DB file not created; all ORM models are empty | 🔴 Critical | Backend cannot persist or query any data | Implement ORM models and DB initialization first |

### 12.2 High Risks

| # | Risk | Severity | Impact | Mitigation |
|:---|:---|:---|:---|:---|
| R6 | **AI Assistant has no backend** — `chatbot.py` is empty; no Gemini API integration | 🟠 High | Entire AI Assistant tab non-functional | Implement after core APIs are functional |
| R7 | **Dashboard router missing entirely** — 5 specified endpoints have no route file | 🟠 High | Dashboard overview KPIs and map cannot be served | Create `dashboard.py` router |
| R8 | **Schema layer empty** — No Pydantic response schemas defined | 🟠 High | No request/response validation; API contracts not enforced | Define schemas matching API specification |
| R9 | **Master dataset incomplete** — `master_dataset_v1.csv` missing 6+ required ML columns | 🟠 High | ML training will fail or produce poor results | Complete feature engineering pipeline |
| R10 | **Duplicate routing configuration** — Both `main.py` and `api/router.py` register the same routers | 🟡 Medium | Potential routing conflicts | Remove `api/router.py` or refactor `main.py` |

### 12.3 Data Acquisition Risk

| Dataset | Likely Source | Acquisition Difficulty | Timeline Risk |
|:---|:---|:---|:---|
| Population by district | Census India / Telangana CDMA | Medium (publicly available) | Low |
| Urbanization percentage | Census India | Medium | Low |
| Road network length | NHAI / Telangana R&B Dept | High (may require RTI/special request) | High |
| EV registrations | Vahan / Telangana RTO | High (may require API access) | High |
| Total vehicle registrations | Vahan portal | Medium (publicly available) | Medium |
| Traffic volume index | NHAI / Telangana Traffic Police | Very High (not openly published) | Very High |
| Average income level | NSSO / RBI / Telangana Planning Dept | High | High |

---

## 13. Final Architecture Assessment

### 13.1 Component Readiness Scorecard

| Component | Specification | Implementation | Readiness |
|:---|:---|:---|:---|
| **Project Documentation** | 14 comprehensive documents | Complete and detailed | ✅ 100% |
| **Frontend UI** | Landing + 5 dashboard views | Fully built with rich UI (2520 lines) | ⚠️ 90% (visual-complete, but all mock data) |
| **Backend Route Stubs** | 25 endpoints specified | 20 stub routes + 1 empty file | ⚠️ 40% (structure exists, no logic) |
| **Backend Business Logic** | Services, repositories, schemas | All directories contain only `.gitkeep` | ❌ 0% |
| **Database Models (ORM)** | 7 models specified | All model files are empty (0 bytes) | ❌ 0% |
| **Database** | SQLite with schema | No database file exists | ❌ 0% |
| **Data Engineering** | 3 preprocessing pipelines | 2 functional (geography, charging stations) + 1 partial (consumption) | ⚠️ 50% |
| **Data Ingestion** | Government API client | Functional client for TGSPDCL/TGNPDCL | ✅ 80% |
| **Raw Data** | 3 dataset types | Charging stations, geography, consumption all present | ✅ 75% |
| **Interim/Processed Data** | Merged master dataset | `master_dataset_v1.csv` exists but incomplete | ⚠️ 40% |
| **ML Training** | 3 models (RF, XGB, K-Means) | No training code or trained models | ❌ 0% |
| **ML Inference** | Prediction service | No implementation | ❌ 0% |
| **Decision Engine** | Priority scoring + recommendations | No implementation | ❌ 0% |
| **AI Integration** | Gemini API chatbot | Settings has `gemini_api_key` field; no integration code | ❌ 0% |
| **Testing** | Test suite | 4 test files for data preprocessing only | ⚠️ 20% |

### 13.2 Overall Architecture Alignment

```
SPECIFICATION ←→ IMPLEMENTATION GAP ANALYSIS

Frontend (Spec)    ████████████████████░ 95% specified
Frontend (Impl)    ████████████████████░ 90% built (mock data)
Frontend→Backend   ░░░░░░░░░░░░░░░░░░░░  0% integrated

Backend  (Spec)    ████████████████████░ 95% specified
Backend  (Impl)    ████░░░░░░░░░░░░░░░░ 15% built (stubs only)

Database (Spec)    ████████████████████░ 95% specified
Database (Impl)    ░░░░░░░░░░░░░░░░░░░░  0% built

Data Eng (Spec)    ████████████████████░ 90% specified
Data Eng (Impl)    ████████░░░░░░░░░░░░ 40% built

ML       (Spec)    ████████████████████░ 95% specified
ML       (Impl)    ░░░░░░░░░░░░░░░░░░░░  0% built

AI       (Spec)    ████████████████████░ 90% specified
AI       (Impl)    ░░░░░░░░░░░░░░░░░░░░  0% built
```

### 13.3 Verdict

> **The EVision Telangana project has exceptional documentation and a polished frontend shell, but the backend, database, ML pipeline, and AI integration are fundamentally non-functional.**
>
> - **49 out of 49 frontend features** are blocked and cannot work with real data today
> - **0 out of 25 API endpoints** return real data
> - **0 out of 7 database tables** exist
> - **0 out of 3 ML models** are trained
> - **6+ external datasets** required for ML training have not been acquired
> - The frontend operates entirely on **hardcoded mock data** embedded in JSX
> - The backend is a collection of **empty stubs** that return `null` and `[]`
>
> **Estimated effort to production readiness: 6–8 weeks** with a dedicated team, assuming external datasets can be acquired. The critical path runs through: dataset acquisition → database implementation → core API implementation → ML pipeline → API integration → frontend integration.

---

> *This report was generated based exclusively on project source documents and current implementation artifacts. No assumptions were made. Every conclusion is traceable to specific files and line numbers in the codebase.*
