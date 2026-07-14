# EVision Telangana — Traceability Matrix

This document provides a complete mapping of the EVision Telangana system from Frontend Features through Backend Endpoints, Database Tables, Dataset Columns, and Machine Learning (ML) dependencies to their current integration and readiness status.

---

## 1. Traceability Mapping

| Frontend Feature | Backend Endpoint | Database Tables | Dataset Columns | ML Output | Status |
|:---|:---|:---|:---|:---|:---|
| **F-DASH-01**<br>Total Districts KPI | `GET /api/v1/districts` | `districts` | `district_geography.csv` → `district_name` | None | 🔴 **Blocked**<br>- Endpoint is a non-functional stub (returns `[]`) |
| **F-DASH-02**<br>Charging Stations KPI | `GET /api/v1/dashboard/stations` | `charging_stations` | `charging_stations_clean.csv` → `owning_organisation` | None | 🔴 **Blocked**<br>- Dashboard router is missing entirely in backend |
| **F-DASH-03**<br>Predicted Demand KPI | `GET /api/v1/predictions/summary` | `district_predictions` | None (ML generated) | Regression → `predicted_demand` | 🔴 **Blocked**<br>- Endpoint is a stub (returns `None`) |
| **F-DASH-04**<br>High Priority Districts KPI | `GET /api/v1/recommendations/summary` | `district_recommendations` | None (ML generated) | Decision Engine → `priority_level` | 🔴 **Blocked**<br>- Endpoint is a stub (returns `None`) |
| **F-DASH-05**<br>District Priority Heatmap | `GET /api/v1/dashboard/map` | `district_recommendations` | `district_geography.csv` → `centroid_latitude`, `centroid_longitude` | Decision Engine → `priority_score` | 🔴 **Blocked**<br>- Dashboard router is missing entirely in backend |
| **F-DASH-06**<br>Demand Forecast Trend Chart | `GET /api/v1/dashboard/trends` | `historical_demand`, `district_predictions` | `district_monthly_consumption.csv` → `reporting_month`, `units` | Regression → `predicted_demand` | 🔴 **Blocked**<br>- Dashboard router is missing entirely in backend |
| **F-DASH-07**<br>AI Insights Card | `GET /api/v1/dashboard/summary` | `district_analytics`, `district_recommendations` | None (ML generated) | Decision Engine + Clustering | 🔴 **Blocked**<br>- Dashboard router is missing entirely in backend |
| **F-DASH-08**<br>District Selector (Dropdown) | `GET /api/v1/districts` | `districts` | `district_geography.csv` → `district_name` | None | 🔴 **Blocked**<br>- Endpoint is a non-functional stub (returns `[]`) |
| **F-DASH-09**<br>Global Search Bar | `GET /api/v1/districts/search` | `districts` | `district_geography.csv` → `district_name` | None | 🔴 **Blocked**<br>- Endpoint is a non-functional stub (returns `[]`) |
| **F-EXPL-01**<br>District Information Card | `GET /api/v1/districts/{district}` | `districts` | `district_geography.csv` → `area_sq_km`, `centroid_latitude`, `centroid_longitude` | None | 🔴 **Blocked**<br>- Endpoint is a stub (returns `None` values) |
| **F-EXPL-02**<br>EV Infrastructure & Demand Card | `GET /api/v1/analytics/profile/{district}`, `GET /api/v1/predictions/{district}` | `historical_demand`, `district_predictions` | `district_monthly_consumption.csv` → `units` | Regression → `predicted_demand` | 🔴 **Blocked**<br>- Both endpoints are non-functional stubs |
| **F-EXPL-03**<br>District Risk Score (Gauge) | `GET /api/v1/recommendations/{district}` | `district_recommendations` | None (ML generated) | Decision Engine → `priority_score` | 🔴 **Blocked**<br>- Endpoint is a stub (returns `None` values) |
| **F-EXPL-04**<br>District Priority Heatmap (Map) | `GET /api/v1/dashboard/map` | `district_recommendations` | `district_geography.csv` → `centroid_latitude`, `centroid_longitude` | Decision Engine → `priority_score` | 🔴 **Blocked**<br>- Dashboard router is missing entirely in backend |
| **F-EXPL-05**<br>AI Recommendations List | `GET /api/v1/recommendations/{district}` | `district_recommendations` | None (ML generated) | Decision Engine → `recommendation` | 🔴 **Blocked**<br>- Endpoint is a stub (returns `None` values) |
| **F-EXPL-06**<br>Estimated Additional Investment | `GET /api/v1/recommendations/{district}` | `district_recommendations` | None (ML generated) | Decision Engine → `investment_estimate` | 🔴 **Blocked**<br>- Endpoint is a stub (returns `None` values) |
| **F-EXPL-07**<br>Recommended Stations Count | `GET /api/v1/recommendations/{district}` | `district_recommendations` | None (ML generated) | Decision Engine → `recommended_stations` | 🔴 **Blocked**<br>- Endpoint is a stub (returns `None` values) |
| **F-EXPL-08**<br>Export Report Button | None Specified | None | None | None | 🔴 **Blocked**<br>- API is not defined in API Specification |
| **F-PRED-01**<br>Predicted Demand Card | `GET /api/v1/predictions/{district}` | `district_predictions` | None (ML generated) | Regression → `predicted_demand` | 🔴 **Blocked**<br>- Endpoint is a stub (returns `None` values) |
| **F-PRED-02**<br>Confidence Score Card | `GET /api/v1/predictions/{district}` | `district_predictions` | None (ML generated) | Regression → `confidence_score` | 🔴 **Blocked**<br>- Endpoint is a stub (returns `None` values) |
| **F-PRED-03**<br>Expected Growth (YoY) Card | `GET /api/v1/predictions/{district}` | `district_predictions` | None (ML generated) | Regression → `predicted_demand` | 🔴 **Blocked**<br>- Endpoint is a stub (returns `None` values) |
| **F-PRED-04**<br>Recommended Stations Card | `GET /api/v1/recommendations/{district}` | `district_recommendations` | None (ML generated) | Decision Engine → `recommended_stations` | 🔴 **Blocked**<br>- Endpoint is a stub (returns `None` values) |
| **F-PRED-05**<br>Demand Forecast Trend Chart | `GET /api/v1/analytics/trends` | `historical_demand`, `district_predictions` | `district_monthly_consumption.csv` → `reporting_month`, `units` | Regression → `predicted_demand` | 🔴 **Blocked**<br>- Endpoint is a non-functional stub |
| **F-PRED-06**<br>Feature Importance Chart | None Specified | `application_metadata` | None (ML generated) | Regression → Feature Importance | 🔴 **Blocked**<br>- API is not defined in API Specification |
| **F-PRED-07**<br>AI Prediction Explanation | `POST /api/v1/assistant/explain` | `district_predictions` | None (ML generated) | Explainable AI → explanation text | 🔴 **Blocked**<br>- AI Assistant router is missing entirely (empty file) |
| **F-PRED-08**<br>Prediction Details Card | None Specified | `application_metadata` | None (ML generated) | Regression → Model metadata | 🔴 **Blocked**<br>- API is not defined in API Specification |
| **F-PRED-09**<br>Date Range Selector | `GET /api/v1/predictions` (with query parameters) | `district_predictions` | None (ML generated) | Regression → time-series predictions | 🔴 **Blocked**<br>- Endpoint is a non-functional stub |
| **F-PRED-10**<br>Export Report Button | None Specified | None | None | None | 🔴 **Blocked**<br>- API is not defined in API Specification |
| **F-ANLY-01**<br>Total EV Demand KPI (2026) | `GET /api/v1/analytics/statistics` | `district_predictions` | None (ML generated) | Regression → `predicted_demand` | 🔴 **Blocked**<br>- Endpoint is a stub (returns `None` values) |
| **F-ANLY-02**<br>Total Charging Stations KPI | `GET /api/v1/dashboard/stations` or `GET /api/v1/analytics/statistics` | `charging_stations` | `charging_stations_clean.csv` → count | None | 🔴 **Blocked**<br>- Dashboard router missing; analytics statistics endpoint is stub |
| **F-ANLY-03**<br>Average Utilization Rate | `GET /api/v1/analytics/statistics` | `district_analytics` | None (ML generated) | Clustering/Analytics → `utilization_ratio` | 🔴 **Blocked**<br>- Endpoint is a stub (returns `None` values) |
| **F-ANLY-04**<br>Capacity Gap KPI | `GET /api/v1/analytics/statistics` | `district_analytics` | None (ML generated) | Decision Engine → `infrastructure_gap` | 🔴 **Blocked**<br>- Endpoint is a stub (returns `None` values) |
| **F-ANLY-05**<br>High Priority Districts KPI | `GET /api/v1/recommendations/summary` | `district_recommendations` | None (ML generated) | Decision Engine → priority classifications | 🔴 **Blocked**<br>- Endpoint is a stub (returns `None` values) |
| **F-ANLY-06**<br>Demand Distribution Pie Chart | `GET /api/v1/predictions` | `district_predictions` | None (ML generated) | Regression → `predicted_demand` | 🔴 **Blocked**<br>- Endpoint is a non-functional stub |
| **F-ANLY-07**<br>Demand vs Capacity Gap Bar Chart | `GET /api/v1/predictions`, `GET /api/v1/analytics/statistics` | `district_predictions`, `district_analytics` | None (ML generated) | Regression + Decision Engine | 🔴 **Blocked**<br>- Both endpoints are non-functional stubs |
| **F-ANLY-08**<br>EV Demand Intensity Map | `GET /api/v1/predictions`, `GET /api/v1/dashboard/map` | `district_predictions`, `district_recommendations` | `district_geography.csv` → centroid coordinates | Regression + Decision Engine | 🔴 **Blocked**<br>- Both endpoints are missing or stubs |
| **F-ANLY-09**<br>Recommended Districts Table | `GET /api/v1/recommendations/top` | `district_recommendations` | None (ML generated) | Decision Engine → rankings, investment | 🔴 **Blocked**<br>- Endpoint is a non-functional stub |
| **F-ANLY-10**<br>Seasonal Demand Heatmap Table | `GET /api/v1/analytics/trends` | `historical_demand`, `district_predictions` | `district_monthly_consumption.csv` → `units` | Regression → seasonal forecast | 🔴 **Blocked**<br>- Endpoint is a non-functional stub |
| **F-ANLY-11**<br>Demand Drivers Impact Chart | None Specified | `application_metadata` | None (ML generated) | Regression → Feature Importance | 🔴 **Blocked**<br>- API is not defined in API Specification |
| **F-ANLY-12**<br>Filters & Date Range | Query parameters on `/api/v1/analytics/*` | Multiple tables | Multiple columns | Multiple models | 🔴 **Blocked**<br>- Stubs do not process query parameters |
| **F-ANLY-13**<br>Export Report Button | None Specified | None | None | None | 🔴 **Blocked**<br>- API is not defined in API Specification |
| **F-CHAT-01**<br>Chat Interface | `POST /api/v1/assistant/chat` | All tables | All columns | Gemini AI + Context Orchestration | 🔴 **Blocked**<br>- AI Assistant router is missing entirely (empty file) |
| **F-CHAT-02**<br>Greeting Message | Static / `POST /api/v1/assistant/chat` | None | None | None | 🔴 **Blocked**<br>- AI Assistant router is missing entirely (empty file) |
| **F-CHAT-03**<br>User Message Input | `POST /api/v1/assistant/chat` | All tables | All columns | Gemini AI + Context Orchestration | 🔴 **Blocked**<br>- AI Assistant router is missing entirely (empty file) |
| **F-CHAT-04**<br>Bot Responses with Tables | `POST /api/v1/assistant/chat` | All tables | All columns | Gemini AI + Structured context | 🔴 **Blocked**<br>- AI Assistant router is missing entirely (empty file) |
| **F-CHAT-05**<br>Suggestion Chips | `GET /api/v1/assistant/suggestions` | `districts` | `district_geography.csv` → `district_name` | None | 🔴 **Blocked**<br>- AI Assistant router is missing entirely (empty file) |
| **F-CHAT-06**<br>Suggested Questions Sidebar | `GET /api/v1/assistant/suggestions` | `districts` | `district_geography.csv` → `district_name` | None | 🔴 **Blocked**<br>- AI Assistant router is missing entirely (empty file) |
| **F-CHAT-07**<br>Quick Actions Grid | `POST /api/v1/assistant/chat` | All tables | All columns | Gemini AI + Context Orchestration | 🔴 **Blocked**<br>- AI Assistant router is missing entirely (empty file) |
| **F-CHAT-08**<br>Context-Aware Responses | `POST /api/v1/assistant/chat` | All tables | All columns | Gemini AI + Selected district context | 🔴 **Blocked**<br>- AI Assistant router is missing entirely (empty file) |

---

## 2. Gap Explanations & Notes

1. **Table Names in Code vs Spec**: 
   - The specifications call for `districts`, `charging_stations`, `historical_demand`, `district_predictions`, `district_analytics`, `district_recommendations`, and `application_metadata` as the model files.
   - In the actual files, there are empty files matching these naming conventions under `backend/models/`.
   - However, the actual SQLite database is never initialized and the tables are 0-byte placeholders.

2. **Missing Datasets**: 
   - Demographics (population, urban percentage), transport (EV registrations, total vehicles), infrastructure (road network, highways), and economy are required as ML inputs but do not exist in the `data/` directory. 
   - This makes it impossible to train the regression models or generate the predictions required for the dashboard.

3. **Stubs Everywhere**: 
   - All implemented routes under `backend/api/routes/` are empty FastAPI skeletons that do not query any database, do not load any joblib models, and do not connect to any AI assistant services.
