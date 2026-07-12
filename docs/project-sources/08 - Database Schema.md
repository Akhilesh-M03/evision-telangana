- [Database Schema](#database-schema)
- [Purpose](#purpose)
- [Relationship to Other Project Documents](#relationship-to-other-project-documents)
- [Database Objectives](#database-objectives)
  - [1. Centralized Application Data](#1-centralized-application-data)
  - [2. Support Backend Services](#2-support-backend-services)
  - [3. Separation of Runtime and Training Data](#3-separation-of-runtime-and-training-data)
  - [4. Maintain Simplicity](#4-maintain-simplicity)
  - [5. Future Portability](#5-future-portability)
  - [6. Clear Ownership](#6-clear-ownership)
- [Database Design Principles](#database-design-principles)
  - [Normalized Design](#normalized-design)
  - [Single Source of Truth](#single-source-of-truth)
  - [Stable Primary Keys](#stable-primary-keys)
  - [Foreign Key Integrity](#foreign-key-integrity)
  - [Read-Optimized Design](#read-optimized-design)
  - [Runtime Storage Only](#runtime-storage-only)
- [Database Responsibilities](#database-responsibilities)
- [Database Technology](#database-technology)
- [Database Scope](#database-scope)
- [Table Definitions](#table-definitions)
- [districts](#districts)
  - [Purpose](#purpose-1)
  - [Columns](#columns)
  - [Primary Key](#primary-key)
  - [Foreign Keys](#foreign-keys)
  - [Notes](#notes)
- [charging\_stations](#charging_stations)
  - [Purpose](#purpose-2)
  - [Columns](#columns-1)
  - [Primary Key](#primary-key-1)
  - [Foreign Keys](#foreign-keys-1)
  - [Notes](#notes-1)
- [historical\_demand](#historical_demand)
  - [Purpose](#purpose-3)
  - [Columns](#columns-2)
  - [Primary Key](#primary-key-2)
  - [Foreign Keys](#foreign-keys-2)
  - [Notes](#notes-2)
- [district\_predictions](#district_predictions)
  - [Purpose](#purpose-4)
  - [Columns](#columns-3)
  - [Primary Key](#primary-key-3)
  - [Foreign Keys](#foreign-keys-3)
  - [Notes](#notes-3)
- [district\_analytics](#district_analytics)
  - [Purpose](#purpose-5)
  - [Columns](#columns-4)
  - [Primary Key](#primary-key-4)
  - [Foreign Keys](#foreign-keys-4)
  - [Notes](#notes-4)
- [district\_recommendations](#district_recommendations)
  - [Purpose](#purpose-6)
  - [Columns](#columns-5)
  - [Primary Key](#primary-key-5)
  - [Foreign Keys](#foreign-keys-5)
  - [Notes](#notes-5)
- [application\_metadata](#application_metadata)
  - [Purpose](#purpose-7)
  - [Columns](#columns-6)
  - [Primary Key](#primary-key-6)
  - [Foreign Keys](#foreign-keys-6)
  - [Notes](#notes-6)
- [Table Relationships](#table-relationships)
  - [Relationship Summary](#relationship-summary)
  - [Relationship Details](#relationship-details)
    - [districts → charging\_stations](#districts--charging_stations)
    - [districts → historical\_demand](#districts--historical_demand)
    - [districts → district\_predictions](#districts--district_predictions)
    - [districts → district\_analytics](#districts--district_analytics)
    - [districts → district\_recommendations](#districts--district_recommendations)
- [SQLModel Mapping Guidelines](#sqlmodel-mapping-guidelines)
  - [One Model Per Table](#one-model-per-table)
  - [Separation of Database Models and API Schemas](#separation-of-database-models-and-api-schemas)
  - [Relationships](#relationships)
  - [Validation](#validation)
  - [Default Values](#default-values)
- [SQLite Data Types](#sqlite-data-types)
- [Primary Key Strategy](#primary-key-strategy)
- [Foreign Key Strategy](#foreign-key-strategy)
- [Indexing Strategy](#indexing-strategy)
- [Naming Conventions](#naming-conventions)
  - [Table Names](#table-names)
  - [Column Names](#column-names)
  - [Primary Keys](#primary-keys)
  - [Foreign Keys](#foreign-keys-7)
  - [Timestamp Columns](#timestamp-columns)
- [Data Ownership](#data-ownership)
- [Data Lifecycle](#data-lifecycle)
  - [Stage 1 — Data Processing](#stage-1--data-processing)
  - [Stage 2 — Database Initialization](#stage-2--database-initialization)
  - [Stage 3 — Machine Learning](#stage-3--machine-learning)
  - [Stage 4 — Analytics](#stage-4--analytics)
  - [Stage 5 — Decision Support](#stage-5--decision-support)
  - [Stage 6 — Application Runtime](#stage-6--application-runtime)
- [Initialization Workflow](#initialization-workflow)
- [Migration Strategy](#migration-strategy)
- [PostgreSQL Compatibility](#postgresql-compatibility)
  - [Standard SQL Naming](#standard-sql-naming)
  - [Surrogate Integer Keys](#surrogate-integer-keys)
  - [Explicit Foreign Keys](#explicit-foreign-keys)
  - [Standard Data Types](#standard-data-types)
  - [Avoid SQLite-Specific Features](#avoid-sqlite-specific-features)
  - [ORM-Based Access](#orm-based-access)
  - [Expected Migration Impact](#expected-migration-impact)
- [Performance Considerations](#performance-considerations)
  - [Read-Optimized Design](#read-optimized-design-1)
  - [Small Dataset Assumption](#small-dataset-assumption)
  - [Indexed Queries](#indexed-queries)
  - [Efficient Relationships](#efficient-relationships)
  - [Cached Runtime Objects](#cached-runtime-objects)
- [Data Integrity Rules](#data-integrity-rules)
  - [District Consistency](#district-consistency)
  - [Unique District Names](#unique-district-names)
  - [Historical Demand Consistency](#historical-demand-consistency)
  - [Prediction Consistency](#prediction-consistency)
  - [Recommendation Consistency](#recommendation-consistency)
  - [Metadata Consistency](#metadata-consistency)
- [Constraints](#constraints)
  - [NOT NULL Constraints](#not-null-constraints)
  - [UNIQUE Constraints](#unique-constraints)
  - [Foreign Key Constraints](#foreign-key-constraints)
  - [Check Constraints](#check-constraints)
- [Future Database Extensions](#future-database-extensions)
- [Database Governance](#database-governance)
- [Conclusion](#conclusion)


# Database Schema

**Project:** EVision Telangana  
**Official Project Title:** AI-Based EV Charging Infrastructure Planning and Decision Support System for Telangana

**Version:** 1.0  
**Status:** Frozen  
**Last Updated:** July 2026

---

# Purpose

This document defines the approved logical database schema for EVision Telangana.

It specifies the SQLite database structure used by the backend application, including logical entities, tables, relationships, keys, indexing strategy, naming conventions, SQLModel mapping guidelines, and future migration considerations.

The Database Schema serves as the implementation contract between the backend services and the application's persistent data storage.

This document intentionally defines **what data is stored** rather than **how it is processed**.

Machine learning algorithms, preprocessing pipelines, Decision Engine logic, and API behavior are defined in their respective Project Sources.

This document serves as the authoritative reference for all database-related implementation throughout the project lifecycle.

---

# Relationship to Other Project Documents

The Database Schema complements the existing project documentation by defining the logical data model used by the application.

| Document                            | Purpose                                                                      |
| ----------------------------------- | ---------------------------------------------------------------------------- |
| Final Project Scope                 | Defines project objectives, datasets, deliverables, and scope boundaries.    |
| Master Roadmap                      | Defines implementation phases and development workflow.                      |
| Final Tech Stack                    | Defines approved technologies including SQLite and SQLModel.                 |
| System Architecture                 | Defines the role of the database within the overall architecture.            |
| Repository Structure                | Defines the location of database-related source files.                       |
| Git Workflow                        | Defines collaborative development practices.                                 |
| API Specification                   | Defines how the frontend interacts with backend data.                        |
| **Database Schema (This Document)** | Defines logical database entities, relationships, and persistence structure. |

This document does not introduce new application functionality or expand the approved project scope.

Instead, it formalizes the logical data model used by the backend application.

---

# Database Objectives

The database has been designed around several primary objectives.

## 1. Centralized Application Data

Provide a single source of truth for processed application data used during runtime.

---

## 2. Support Backend Services

Provide efficient data storage for dashboard visualization, analytics, recommendations, and AI explanations.

---

## 3. Separation of Runtime and Training Data

Support application runtime without storing machine learning training artifacts or intermediate preprocessing outputs.

---

## 4. Maintain Simplicity

Use a lightweight relational schema appropriate for the approved MVP.

---

## 5. Future Portability

Remain compatible with future migration to PostgreSQL with minimal structural changes.

---

## 6. Clear Ownership

Assign every logical entity to a single authoritative table.

---

# Database Design Principles

The database follows several guiding principles.

---

## Normalized Design

Data should be organized to minimize redundancy while maintaining implementation simplicity.

---

## Single Source of Truth

Each logical entity is stored in exactly one primary table.

---

## Stable Primary Keys

Every table uses stable primary keys that uniquely identify records.

---

## Foreign Key Integrity

Relationships between entities should be enforced through foreign keys whenever appropriate.

---

## Read-Optimized Design

The database primarily supports read operations for dashboard visualization and decision support.

---

## Runtime Storage Only

Only application runtime data is stored within SQLite.

Training datasets, notebooks, intermediate preprocessing outputs, and machine learning artifacts remain external.

---

# Database Responsibilities

The database is responsible for storing:

- District information
- Charging station metadata
- Historical charging demand
- Prediction results
- Analytical summaries
- Recommendation outputs
- Application metadata

The database is **not** responsible for storing:

- Raw datasets
- Machine learning training data
- Joblib model files
- Feature engineering pipelines
- Evaluation metrics
- Notebook outputs

---

# Database Technology

| Component          | Technology                |
| ------------------ | ------------------------- |
| Database Engine    | SQLite                    |
| ORM                | SQLModel                  |
| Query Language     | SQL                       |
| Connection Library | SQLAlchemy (via SQLModel) |

SQLite is sufficient for the approved MVP while maintaining compatibility with future PostgreSQL migration.

---

# Database Scope

The logical database stores only processed runtime information required by the backend application.

Data is populated during database initialization using processed datasets generated by the Data Processing Pipeline.

Machine learning models are loaded separately from the `models/` directory and are never stored within the database.

---

````

# Logical Data Model Overview

The EVision Telangana database follows a simple relational design centered around districts.

Most application data is associated with a district, allowing the backend to efficiently retrieve information for dashboard visualization, analytics, recommendations, and AI explanations.

The logical model separates independent entities while minimizing data duplication.

The database consists of the following logical entities:

| Entity | Purpose |
|---------|---------|
| District | Master list of Telangana districts |
| Charging Station | Existing charging infrastructure |
| Historical Demand | Historical EV charging electricity consumption |
| District Prediction | Future demand predictions generated by the ML model |
| District Analytics | Analytical summaries and clustering results |
| District Recommendation | Decision Engine outputs and District Priority Scores |
| Application Metadata | Application-level configuration and metadata |

The District entity serves as the central reference point for nearly every other table.

---

# Entity Overview

---

## 1. District

Purpose:

Stores the master list of Telangana districts used throughout the application.

Responsibilities:

- Official district names
- Geographic reference information
- Stable identifiers

Referenced by:

- Charging Stations
- Historical Demand
- Predictions
- Analytics
- Recommendations

---

## 2. Charging Station

Purpose:

Stores existing EV charging station information imported from the processed TGREDCO dataset.

Responsibilities:

- Station location
- District association
- Geographic coordinates
- Owning organization

Supports:

- Interactive maps
- Infrastructure visualization
- Station counts
- Infrastructure gap analysis

---

## 3. Historical Demand

Purpose:

Stores processed historical electricity consumption records used for visualization and analytics.

Responsibilities:

- Monthly demand values
- Reporting period
- District association

Supports:

- Historical trend charts
- District statistics
- AI explanations

The table stores processed historical observations only.

It is **not** used for model training during application runtime.

---

## 4. District Prediction

Purpose:

Stores prediction outputs generated by the selected regression model.

Responsibilities:

- Predicted charging demand
- Prediction timestamp
- Forecast period

Supports:

- Dashboard
- Predictions API
- Recommendation Engine
- AI Assistant

Prediction results may be regenerated whenever the model is retrained.

---

## 5. District Analytics

Purpose:

Stores processed analytical outputs generated by the Analytics Engine.

Responsibilities:

- Cluster assignments
- Historical averages
- Trend labels
- Summary statistics

Supports:

- Dashboard analytics
- District profiles
- Cluster visualization
- AI explanations

---

## 6. District Recommendation

Purpose:

Stores the final outputs produced by the Decision Engine.

Responsibilities:

- District Priority Score
- Priority category
- District ranking

Supports:

- Recommendation dashboard
- District comparison
- AI explanations

The exact computation of the District Priority Score remains implementation-dependent.

Only the finalized outputs are stored.

---

## 7. Application Metadata

Purpose:

Stores small amounts of application-level metadata required by the backend.

Typical examples include:

- Dataset generation timestamp
- Database initialization version
- Latest processed reporting month

This table is intentionally lightweight.

It is not intended to replace application configuration managed through environment variables.

---

# Entity Relationship Diagram (Logical)

The following diagram illustrates the logical relationships between the primary database entities.

```text
                    +----------------------+
                    |      District        |
                    +----------+-----------+
                               |
        +-----------+----------+----------+-----------+-----------+
        |           |                     |           |           |
        ▼           ▼                     ▼           ▼           ▼
+---------------+ +----------------+ +----------------+ +----------------+ +----------------------+
| Charging      | | Historical     | | District       | | District       | | District             |
| Stations      | | Demand         | | Prediction     | | Analytics      | | Recommendation       |
+---------------+ +----------------+ +----------------+ +----------------+ +----------------------+

                     +----------------------+
                     | Application Metadata |
                     +----------------------+
````

The database intentionally uses a straightforward relational structure.

Most entities reference the District table through foreign keys, allowing consistent district-based querying while keeping the schema easy to understand and maintain.

# Table Definitions

---

# districts

## Purpose

Stores the master list of Telangana districts used throughout the application.

This table serves as the parent entity for nearly every other logical table.

---

## Columns

| Column        | Data Type | Nullable | Description                 |
| ------------- | --------- | -------- | --------------------------- |
| id            | INTEGER   | No       | Primary key                 |
| district_name | TEXT      | No       | Official district name      |
| created_at    | DATETIME  | No       | Record creation timestamp   |
| updated_at    | DATETIME  | No       | Last modification timestamp |

---

## Primary Key

- `id`

---

## Foreign Keys

None.

---

## Notes

- District names should remain unique.
- Names should match the standardized names produced by the Data Processing Pipeline.

---

# charging_stations

## Purpose

Stores processed charging station metadata imported from the TGREDCO charging station dataset.

---

## Columns

| Column       | Data Type | Nullable | Description                        |
| ------------ | --------- | -------- | ---------------------------------- |
| id           | INTEGER   | No       | Primary key                        |
| district_id  | INTEGER   | No       | Reference to district              |
| station_name | TEXT      | Yes      | Charging station name if available |
| organization | TEXT      | Yes      | Owning organization                |
| address      | TEXT      | Yes      | Station address                    |
| latitude     | REAL      | Yes      | Geographic latitude                |
| longitude    | REAL      | Yes      | Geographic longitude               |
| created_at   | DATETIME  | No       | Record creation timestamp          |

---

## Primary Key

- `id`

---

## Foreign Keys

- `district_id → districts.id`

---

## Notes

- Geographic coordinates should use decimal degrees.
- Missing optional station fields may remain NULL.

---

# historical_demand

## Purpose

Stores processed historical charging demand used by the application.

---

## Columns

| Column          | Data Type | Nullable | Description               |
| --------------- | --------- | -------- | ------------------------- |
| id              | INTEGER   | No       | Primary key               |
| district_id     | INTEGER   | No       | Reference to district     |
| reporting_month | TEXT      | No       | Month in YYYY-MM format   |
| demand_kwh      | REAL      | No       | Electricity consumption   |
| created_at      | DATETIME  | No       | Record creation timestamp |

---

## Primary Key

- `id`

---

## Foreign Keys

- `district_id → districts.id`

---

## Notes

- One record represents one district for one reporting month.
- Duplicate district-month combinations should not exist.

---

# district_predictions

## Purpose

Stores prediction outputs generated by the selected regression model.

---

## Columns

| Column           | Data Type | Nullable | Description               |
| ---------------- | --------- | -------- | ------------------------- |
| id               | INTEGER   | No       | Primary key               |
| district_id      | INTEGER   | No       | Reference to district     |
| forecast_period  | TEXT      | No       | Forecast period           |
| predicted_demand | REAL      | No       | Predicted charging demand |
| model_version    | TEXT      | Yes      | Model version identifier  |
| generated_at     | DATETIME  | No       | Prediction timestamp      |

---

## Primary Key

- `id`

---

## Foreign Keys

- `district_id → districts.id`

---

## Notes

- Existing predictions may be replaced whenever models are retrained.
- Only finalized prediction outputs are stored.

---

# district_analytics

## Purpose

Stores processed analytical information generated by the Analytics Engine.

---

## Columns

| Column                    | Data Type | Nullable | Description               |
| ------------------------- | --------- | -------- | ------------------------- |
| id                        | INTEGER   | No       | Primary key               |
| district_id               | INTEGER   | No       | Reference to district     |
| cluster_id                | INTEGER   | No       | Assigned cluster          |
| historical_average_demand | REAL      | Yes      | Average historical demand |
| trend_label               | TEXT      | Yes      | Trend classification      |
| generated_at              | DATETIME  | No       | Analysis timestamp        |

---

## Primary Key

- `id`

---

## Foreign Keys

- `district_id → districts.id`

---

## Notes

- Cluster identifiers are analytical labels only.
- This table stores processed summaries rather than raw analytical calculations.

---

# district_recommendations

## Purpose

Stores finalized recommendation outputs produced by the Decision Engine.

---

## Columns

| Column         | Data Type | Nullable | Description              |
| -------------- | --------- | -------- | ------------------------ |
| id             | INTEGER   | No       | Primary key              |
| district_id    | INTEGER   | No       | Reference to district    |
| priority_score | REAL      | No       | District Priority Score  |
| priority_level | TEXT      | No       | Recommendation category  |
| district_rank  | INTEGER   | No       | Relative ranking         |
| generated_at   | DATETIME  | No       | Recommendation timestamp |

---

## Primary Key

- `id`

---

## Foreign Keys

- `district_id → districts.id`

---

## Notes

- The exact computation of `priority_score` is intentionally implementation-dependent.
- Only finalized outputs are persisted.

---

# application_metadata

## Purpose

Stores lightweight application metadata required during runtime.

---

## Columns

| Column         | Data Type | Nullable | Description           |
| -------------- | --------- | -------- | --------------------- |
| id             | INTEGER   | No       | Primary key           |
| metadata_key   | TEXT      | No       | Metadata identifier   |
| metadata_value | TEXT      | No       | Metadata value        |
| updated_at     | DATETIME  | No       | Last update timestamp |

---

## Primary Key

- `id`

---

## Foreign Keys

None.

---

## Notes

Typical metadata values may include:

- Database schema version
- Latest reporting month
- Dataset generation timestamp
- Database initialization timestamp

Application configuration remains outside the database and should continue to be managed through environment variables.

# Table Relationships

The database follows a straightforward relational structure centered around the `districts` table.

Every operational table references a district, allowing the backend to efficiently retrieve related information while maintaining data integrity.

---

## Relationship Summary

| Parent Table | Child Table              | Relationship                  |
| ------------ | ------------------------ | ----------------------------- |
| districts    | charging_stations        | One-to-Many                   |
| districts    | historical_demand        | One-to-Many                   |
| districts    | district_predictions     | One-to-Many                   |
| districts    | district_analytics       | One-to-One (Current Snapshot) |
| districts    | district_recommendations | One-to-One (Current Snapshot) |

The `application_metadata` table is independent and has no foreign key relationships.

---

## Relationship Details

### districts → charging_stations

Relationship Type:

**One-to-Many**

A district may contain multiple charging stations.

Each charging station belongs to exactly one district.

---

### districts → historical_demand

Relationship Type:

**One-to-Many**

Each district contains multiple historical monthly demand records.

Each historical demand record belongs to one district.

---

### districts → district_predictions

Relationship Type:

**One-to-Many**

Prediction records may be regenerated after future model retraining.

Although the MVP typically stores the latest prediction, the schema allows multiple prediction records if future forecasting periods are introduced.

---

### districts → district_analytics

Relationship Type:

**One-to-One (Current Snapshot)**

Each district has one current analytical summary.

When analytics are regenerated, the existing record may be updated or replaced.

---

### districts → district_recommendations

Relationship Type:

**One-to-One (Current Snapshot)**

Each district has one current recommendation generated by the Decision Engine.

Future recalculations update the existing recommendation.

---

# SQLModel Mapping Guidelines

The backend uses SQLModel as the ORM layer.

Each logical table should be represented by one SQLModel class.

---

## One Model Per Table

Each database table maps directly to a corresponding SQLModel model.

Examples include:

| Database Table           | SQLModel Class           |
| ------------------------ | ------------------------ |
| districts                | `District`               |
| charging_stations        | `ChargingStation`        |
| historical_demand        | `HistoricalDemand`       |
| district_predictions     | `DistrictPrediction`     |
| district_analytics       | `DistrictAnalytics`      |
| district_recommendations | `DistrictRecommendation` |
| application_metadata     | `ApplicationMetadata`    |

---

## Separation of Database Models and API Schemas

Database models should represent persistent entities only.

API request and response schemas should remain separate and be defined within the `schemas/` package.

This separation prevents API contracts from becoming tightly coupled to database implementation.

---

## Relationships

SQLModel relationships should mirror the logical relationships defined in this document.

Examples include:

- District → Charging Stations
- District → Historical Demand
- District → Prediction
- District → Analytics
- District → Recommendation

Relationship loading strategy may be selected during implementation based on performance requirements.

---

## Validation

SQLModel field validation should enforce:

- Required fields
- Appropriate data types
- Nullable constraints
- Maximum string lengths where applicable

Business validation remains within the Service Layer rather than the database model itself.

---

## Default Values

Timestamp fields such as `created_at`, `updated_at`, and `generated_at` should use backend-generated defaults.

Application logic should manage automatic timestamp updates where appropriate.

---

# SQLite Data Types

The database uses SQLite data types compatible with SQLModel.

| SQLite Type | Typical Usage                                                 |
| ----------- | ------------------------------------------------------------- |
| INTEGER     | Primary keys, foreign keys, rankings, cluster identifiers     |
| REAL        | Demand values, scores, coordinates                            |
| TEXT        | District names, labels, metadata values                       |
| DATETIME    | Creation timestamps, update timestamps, generation timestamps |

SQLite's flexible typing is sufficient for the approved MVP while remaining portable to PostgreSQL.

---

# Primary Key Strategy

Every table uses a single-column surrogate primary key.

Characteristics:

- INTEGER
- Auto-incrementing
- Immutable
- Never reused

Using surrogate keys simplifies foreign key relationships and future schema evolution.

---

# Foreign Key Strategy

Foreign keys enforce referential integrity across district-related tables.

The following foreign keys are defined:

| Child Table              | Foreign Key | Parent Table |
| ------------------------ | ----------- | ------------ |
| charging_stations        | district_id | districts    |
| historical_demand        | district_id | districts    |
| district_predictions     | district_id | districts    |
| district_analytics       | district_id | districts    |
| district_recommendations | district_id | districts    |

All district references should point to an existing district record.

Deleting a district should not normally occur during application runtime.

Accordingly, cascade delete behavior is not required for the approved MVP.

---

# Indexing Strategy

Indexes improve query performance for common dashboard and API operations.

The following indexes are recommended.

| Table                    | Indexed Column(s) | Purpose                       |
| ------------------------ | ----------------- | ----------------------------- |
| districts                | district_name     | Fast district lookup          |
| charging_stations        | district_id       | Retrieve stations by district |
| historical_demand        | district_id       | Historical trend queries      |
| historical_demand        | reporting_month   | Time-series queries           |
| district_predictions     | district_id       | Prediction retrieval          |
| district_analytics       | district_id       | Analytics retrieval           |
| district_recommendations | district_id       | Recommendation retrieval      |
| application_metadata     | metadata_key      | Metadata lookup               |

Additional indexes may be introduced during implementation if profiling identifies performance bottlenecks.

The approved MVP dataset size is expected to perform efficiently with this indexing strategy.

# Naming Conventions

The database follows consistent naming conventions to improve readability, maintainability, and compatibility with SQLModel and future PostgreSQL migration.

---

## Table Names

Table names should:

- Use lowercase letters
- Use snake_case
- Use plural nouns
- Avoid abbreviations where practical

Examples:

```text
districts
charging_stations
historical_demand
district_predictions
district_analytics
district_recommendations
application_metadata
```

---

## Column Names

Column names should:

- Use lowercase letters
- Use snake_case
- Be descriptive
- Avoid unnecessary abbreviations

Examples:

```text
district_name
priority_score
historical_average_demand
generated_at
reporting_month
```

---

## Primary Keys

Primary keys should always use:

```text
id
```

This convention remains consistent across every table.

---

## Foreign Keys

Foreign key columns should use:

```text
<parent_table>_id
```

Examples:

```text
district_id
```

This naming convention clearly communicates relationships while remaining ORM-friendly.

---

## Timestamp Columns

Timestamp fields should use standardized names.

| Purpose             | Column Name  |
| ------------------- | ------------ |
| Record creation     | created_at   |
| Record modification | updated_at   |
| Generated output    | generated_at |

Using consistent timestamp names simplifies backend implementation and auditing.

---

# Data Ownership

Each logical entity has a single authoritative owner.

This prevents duplication and ensures consistent data throughout the application.

| Data                         | Owning Table             |
| ---------------------------- | ------------------------ |
| District information         | districts                |
| Charging station information | charging_stations        |
| Historical demand            | historical_demand        |
| Prediction outputs           | district_predictions     |
| Analytical summaries         | district_analytics       |
| Recommendation outputs       | district_recommendations |
| Application metadata         | application_metadata     |

No logical entity should be duplicated across multiple tables unless required for denormalized reporting in future versions.

---

# Data Lifecycle

The database supports the runtime lifecycle of processed application data.

The overall lifecycle consists of several stages.

---

## Stage 1 — Data Processing

Official datasets are cleaned, validated, standardized, and merged by the Data Processing Pipeline.

Outputs include processed datasets ready for application use.

---

## Stage 2 — Database Initialization

Processed datasets are imported into the SQLite database.

Tables are populated with:

- District records
- Charging stations
- Historical demand
- Application metadata

This initialization occurs before normal application execution.

---

## Stage 3 — Machine Learning

Machine learning models consume processed datasets outside the database.

Training datasets remain external.

Prediction outputs generated by the selected regression model are then written into the appropriate database tables.

---

## Stage 4 — Analytics

The Analytics Engine computes:

- Cluster assignments
- Historical summaries
- Trend labels

The resulting analytical outputs are stored within the database.

---

## Stage 5 — Decision Support

The Decision Engine generates:

- District Priority Scores
- Rankings
- Recommendation levels

Only finalized outputs are persisted.

---

## Stage 6 — Application Runtime

During application execution, the backend performs primarily read operations against the database.

Typical runtime operations include:

- Dashboard queries
- District lookup
- Recommendation retrieval
- Analytics retrieval
- AI context preparation

The application does not continuously modify historical records during normal execution.

---

# Initialization Workflow

The database should be initialized during backend setup using the following workflow.

```text
Processed Datasets
        │
        ▼
Create SQLite Database
        │
        ▼
Create Tables
        │
        ▼
Populate District Table
        │
        ▼
Populate Charging Stations
        │
        ▼
Populate Historical Demand
        │
        ▼
Load Prediction Outputs
        │
        ▼
Load Analytics
        │
        ▼
Load Recommendations
        │
        ▼
Insert Application Metadata
```

Database initialization should be deterministic.

Running the initialization process with identical processed datasets should produce identical database contents.

---

# Migration Strategy

The approved MVP uses SQLite for simplicity.

Database migrations should remain lightweight and manageable.

Recommended migration principles include:

- Preserve existing data whenever practical.
- Apply incremental schema changes.
- Version schema changes.
- Test migrations before deployment.
- Avoid destructive changes unless necessary.

The project may use SQLModel metadata creation during early development.

Formal migration tooling (such as Alembic) is intentionally outside the MVP scope.

---

# PostgreSQL Compatibility

Although SQLite is the approved database for the MVP, the schema has been designed for straightforward migration to PostgreSQL.

The following practices support future portability.

---

## Standard SQL Naming

Avoid SQLite-specific naming conventions.

Use generic SQL-compatible table and column names.

---

## Surrogate Integer Keys

Use integer primary keys rather than SQLite row identifiers.

---

## Explicit Foreign Keys

Relationships should be declared explicitly rather than relying on application logic.

---

## Standard Data Types

Use SQLModel field definitions that map cleanly to PostgreSQL equivalents.

---

## Avoid SQLite-Specific Features

The schema should avoid dependence on SQLite-only behavior wherever practical.

---

## ORM-Based Access

The backend interacts with the database exclusively through SQLModel.

Using an ORM minimizes the effort required to migrate database engines in the future.

---

## Expected Migration Impact

If PostgreSQL is adopted in a future version, the following components should require minimal changes:

- SQLModel models
- Repository layer
- Service layer
- REST API
- Frontend application

Only the database connection configuration and migration scripts should require significant modification.

# Performance Considerations

The approved database schema is designed for a lightweight academic decision support system with a relatively small dataset.

The primary optimization goal is fast read performance for dashboard visualization and API responses rather than high-volume transactional processing.

---

## Read-Optimized Design

Most application operations retrieve information rather than modify it.

Typical read operations include:

- Dashboard summaries
- District details
- Historical trends
- Prediction retrieval
- Recommendation retrieval
- AI context preparation

Accordingly, the schema favors efficient read access while keeping update operations simple.

---

## Small Dataset Assumption

The approved MVP stores information for:

- 33 Telangana districts
- Existing charging stations
- Historical charging demand records
- Prediction outputs
- Analytical summaries
- Recommendation results

This dataset size is well within SQLite's capabilities.

No database sharding, partitioning, or distributed storage is required.

---

## Indexed Queries

Indexes should be created only for frequently queried columns.

Excessive indexing is discouraged because it increases storage requirements and write overhead without providing measurable benefit for the approved dataset size.

---

## Efficient Relationships

The schema avoids deeply nested relationships.

Most application queries require only one or two joins centered around the `districts` table.

This simplifies query execution and improves maintainability.

---

## Cached Runtime Objects

Machine learning models should be loaded into application memory during backend startup.

Prediction requests should not repeatedly load serialized model artifacts from disk.

Similarly, frequently accessed application metadata may be cached in memory after initial retrieval.

---

# Data Integrity Rules

The database should maintain consistent, reliable, and valid data throughout the application lifecycle.

The following rules apply across all tables.

---

## District Consistency

Every district referenced by child tables must exist within the `districts` table.

Orphaned foreign key references should never occur.

---

## Unique District Names

Each district should appear only once within the `districts` table.

Duplicate district names are not permitted.

---

## Historical Demand Consistency

Each historical demand record should represent one district for one reporting period.

Duplicate district-month combinations should not exist.

---

## Prediction Consistency

Prediction records should correspond only to valid districts.

If prediction outputs are regenerated, older records should be replaced or updated according to the application's data refresh strategy.

---

## Recommendation Consistency

Recommendation records should reference valid prediction and analytical outputs generated during the same processing cycle.

The backend is responsible for maintaining this consistency during database updates.

---

## Metadata Consistency

Metadata keys should remain unique.

Each metadata entry should represent a single application property.

---

# Constraints

The following logical constraints should be enforced where appropriate.

---

## NOT NULL Constraints

The following fields should always contain values.

Examples include:

- Primary keys
- Foreign keys
- District names
- Reporting periods
- Prediction values
- Priority scores
- Timestamp fields

---

## UNIQUE Constraints

Recommended unique constraints include:

| Table                | Column(s)                    |
| -------------------- | ---------------------------- |
| districts            | district_name                |
| historical_demand    | district_id, reporting_month |
| application_metadata | metadata_key                 |

These constraints prevent accidental duplication of critical application data.

---

## Foreign Key Constraints

Foreign key relationships should be enforced for all district-related tables.

This ensures that child records cannot reference non-existent districts.

---

## Check Constraints

Where supported by the implementation, logical validation rules may include:

- Latitude values between -90 and 90
- Longitude values between -180 and 180
- Priority scores greater than or equal to zero
- District rankings greater than zero

These constraints provide an additional layer of data validation.

---

# Future Database Extensions

The database has been intentionally designed to support future enhancements without requiring major structural changes.

Potential future additions include:

- User authentication tables
- Saved dashboard preferences
- Multiple prediction versions
- Multi-year forecasting results
- Scenario analysis
- Infrastructure planning projects
- Feedback collection
- Audit logging
- AI conversation history
- Scheduled data refresh records

Future extensions should build upon the existing relational model rather than introducing parallel or duplicate data structures.

---

# Database Governance

This document defines the approved logical database schema for EVision Telangana.

All database implementation should conform to the entities, relationships, naming conventions, and integrity rules defined herein.

Schema modifications should only be made when:

- Required by verified implementation constraints,
- Required to resolve data consistency issues,
- Required by the project supervisor,
- Required to improve maintainability without altering approved functionality, or
- Required for future approved project enhancements.

Database changes must remain consistent with the approved Project Scope, Master Roadmap, Final Tech Stack, System Architecture, Repository Structure, Git Workflow, and API Specification.

---

# Conclusion

The Database Schema establishes a simple, consistent, and maintainable relational data model for EVision Telangana.

By organizing district information, charging station metadata, historical demand records, prediction outputs, analytical summaries, recommendation results, and application metadata into well-defined relational tables, the schema provides a reliable foundation for backend services while remaining aligned with the approved MVP.

The design intentionally separates runtime application data from machine learning artifacts, supports SQLModel-based implementation, enforces logical data integrity through keys and relationships, and maintains compatibility with future PostgreSQL migration.

This document serves as the authoritative database implementation contract for EVision Telangana throughout development, testing, and future system evolution.
