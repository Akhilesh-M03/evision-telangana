- [System Architecture](#system-architecture)
- [Purpose](#purpose)
- [Relationship to Other Project Documents](#relationship-to-other-project-documents)
- [Architectural Goals](#architectural-goals)
  - [1. Modularity](#1-modularity)
  - [2. Separation of Concerns](#2-separation-of-concerns)
  - [3. Maintainability](#3-maintainability)
  - [4. Parallel Development](#4-parallel-development)
  - [5. Reproducibility](#5-reproducibility)
  - [6. Explainability](#6-explainability)
  - [7. Future Extensibility](#7-future-extensibility)
- [Architectural Principles](#architectural-principles)
  - [Layered Architecture](#layered-architecture)
  - [Backend-Centric Business Logic](#backend-centric-business-logic)
  - [Frontend as Presentation Layer](#frontend-as-presentation-layer)
  - [Single Source of Truth](#single-source-of-truth)
  - [Reusable Components](#reusable-components)
  - [Loose Coupling](#loose-coupling)
  - [Explainable AI](#explainable-ai)
- [Architectural Style](#architectural-style)
- [High-Level System Architecture](#high-level-system-architecture)
- [Technology Mapping](#technology-mapping)
- [Major System Components](#major-system-components)
  - [1. Presentation Layer](#1-presentation-layer)
  - [2. Backend API Layer](#2-backend-api-layer)
  - [3. Data Processing Pipeline](#3-data-processing-pipeline)
  - [4. Machine Learning Engine](#4-machine-learning-engine)
  - [5. Analytics Engine](#5-analytics-engine)
  - [6. Decision Engine](#6-decision-engine)
  - [7. AI Assistant](#7-ai-assistant)
- [Component Responsibility Matrix](#component-responsibility-matrix)
- [Component Interaction Overview](#component-interaction-overview)
- [System Data Flow](#system-data-flow)
- [Offline Data Flow](#offline-data-flow)
- [Online Data Flow](#online-data-flow)
- [End-to-End Request Flow](#end-to-end-request-flow)
- [Data Sources](#data-sources)
  - [EV Charging Consumption](#ev-charging-consumption)
  - [Charging Station Information](#charging-station-information)
  - [District Boundary Dataset](#district-boundary-dataset)
- [Data Processing Pipeline Architecture](#data-processing-pipeline-architecture)
- [Pipeline Stages](#pipeline-stages)
  - [Data Validation](#data-validation)
  - [Data Cleaning](#data-cleaning)
  - [Dataset Integration](#dataset-integration)
  - [Feature Engineering](#feature-engineering)
  - [Artifact Generation](#artifact-generation)
- [Backend Architecture](#backend-architecture)
- [API Layer](#api-layer)
- [Service Layer](#service-layer)
- [Machine Learning Service](#machine-learning-service)
- [Decision Engine Service](#decision-engine-service)
- [AI Service](#ai-service)
- [Repository Layer](#repository-layer)
- [Frontend Architecture](#frontend-architecture)
- [Frontend Layers](#frontend-layers)
- [Page Components](#page-components)
- [Shared Components](#shared-components)
- [API Service Layer](#api-service-layer)
- [State Management](#state-management)
- [Database Architecture](#database-architecture)
- [Database Responsibilities](#database-responsibilities)
- [Logical Data Organization](#logical-data-organization)
- [Model Storage](#model-storage)
- [API Architecture](#api-architecture)
- [API Design Principles](#api-design-principles)
  - [Stateless Communication](#stateless-communication)
  - [JSON-Based Communication](#json-based-communication)
  - [Consistent Response Structure](#consistent-response-structure)
  - [Validation](#validation)
  - [Error Handling](#error-handling)
- [Machine Learning Architecture](#machine-learning-architecture)
- [Machine Learning Workflow](#machine-learning-workflow)
- [Training Workflow](#training-workflow)
- [Model Evaluation](#model-evaluation)
- [Inference Workflow](#inference-workflow)
- [Clustering Architecture](#clustering-architecture)
- [Feature Engineering Architecture](#feature-engineering-architecture)
- [Model Persistence](#model-persistence)
- [Machine Learning Responsibilities](#machine-learning-responsibilities)
- [Decision Engine Architecture](#decision-engine-architecture)
- [Decision Engine Workflow](#decision-engine-workflow)
- [Decision Engine Inputs](#decision-engine-inputs)
- [District Priority Score](#district-priority-score)
- [Decision Engine Outputs](#decision-engine-outputs)
- [Explainability Support](#explainability-support)
- [AI Assistant Architecture](#ai-assistant-architecture)
- [AI Assistant Workflow](#ai-assistant-workflow)
- [AI Assistant Responsibilities](#ai-assistant-responsibilities)
- [AI Assistant Boundaries](#ai-assistant-boundaries)
- [Prompt Construction](#prompt-construction)
- [AI Provider Abstraction](#ai-provider-abstraction)
- [Repository Architecture](#repository-architecture)
- [Configuration Management](#configuration-management)
- [Environment Variables](#environment-variables)
- [Logging Strategy](#logging-strategy)
- [Error Handling Strategy](#error-handling-strategy)
- [Input Validation](#input-validation)
- [Performance Considerations](#performance-considerations)
- [Scalability Considerations](#scalability-considerations)
- [Security Considerations](#security-considerations)
- [API Security](#api-security)
- [Environment Variable Protection](#environment-variable-protection)
- [Input Sanitization](#input-sanitization)
- [Error Exposure](#error-exposure)
- [Model Protection](#model-protection)
- [AI Service Protection](#ai-service-protection)
- [Cross-Cutting Concerns](#cross-cutting-concerns)
- [Configuration](#configuration)
- [Validation](#validation-1)
- [Exception Handling](#exception-handling)
- [Logging](#logging)
- [Deployment Architecture](#deployment-architecture)
- [Local Development Architecture](#local-development-architecture)
- [Optional Cloud Deployment](#optional-cloud-deployment)
- [Runtime Startup Sequence](#runtime-startup-sequence)
- [Shutdown Sequence](#shutdown-sequence)
- [Architectural Decisions](#architectural-decisions)
  - [Decision 1 — Layered Client–Server Architecture](#decision-1--layered-clientserver-architecture)
  - [Decision 2 — FastAPI Backend](#decision-2--fastapi-backend)
  - [Decision 3 — React + Vite Frontend](#decision-3--react--vite-frontend)
  - [Decision 4 — SQLite Database](#decision-4--sqlite-database)
  - [Decision 5 — Joblib Model Persistence](#decision-5--joblib-model-persistence)
  - [Decision 6 — Separate Training and Inference](#decision-6--separate-training-and-inference)
  - [Decision 7 — Backend-Owned Business Logic](#decision-7--backend-owned-business-logic)
  - [Decision 8 — AI as an Explanation Layer](#decision-8--ai-as-an-explanation-layer)
- [Future Architectural Extensions](#future-architectural-extensions)
- [Architecture Diagram Index](#architecture-diagram-index)
- [Architecture Governance](#architecture-governance)
- [Conclusion](#conclusion)


# System Architecture

**Project:** EVision Telangana  
**Official Project Title:** AI-Based EV Charging Infrastructure Planning and Decision Support System for Telangana

**Version:** 1.0  
**Status:** Frozen  
**Last Updated:** July 2026

---

# Purpose

This document defines the approved software architecture for EVision Telangana.

It describes the overall architectural design, major system components, communication patterns, data flow, implementation responsibilities, deployment strategy, and technical decisions that govern the development of the application.

The architecture translates the approved project scope into an implementable technical blueprint while remaining fully aligned with the approved Project Scope, Master Roadmap, and Final Tech Stack.

This document serves as the authoritative architectural reference for all implementation activities throughout the project lifecycle.

---

# Relationship to Other Project Documents

The System Architecture document complements the existing project documentation.

| Document                                | Purpose                                                                                       |
| --------------------------------------- | --------------------------------------------------------------------------------------------- |
| Final Project Scope                     | Defines project objectives, deliverables, datasets, and functional boundaries.                |
| Master Roadmap                          | Defines implementation phases, milestones, and development workflow.                          |
| Final Tech Stack                        | Defines approved technologies, tooling, development standards, and implementation principles. |
| **System Architecture (This Document)** | Defines how the approved technologies are organized into a complete software system.          |

This document does not introduce new project features or alter the approved scope. Instead, it specifies how the approved modules interact to form a complete Decision Support System.

---

# Architectural Goals

The architecture has been designed around several primary objectives.

## 1. Modularity

Each major capability is implemented as an independent module with clearly defined responsibilities.

Examples include:

- Data Processing Pipeline
- Machine Learning Engine
- Analytics Engine
- Decision Engine
- Backend API
- Frontend Dashboard
- AI Assistant

This separation allows each component to evolve independently while minimizing unintended side effects.

---

## 2. Separation of Concerns

Each architectural layer performs one primary responsibility.

The frontend handles presentation.

The backend coordinates business logic.

Machine learning focuses on prediction.

The Decision Engine performs recommendation logic.

The AI Assistant explains system outputs.

This clear separation simplifies maintenance and testing.

---

## 3. Maintainability

The architecture favors readable, modular code over tightly coupled implementations.

Major responsibilities remain isolated within dedicated modules, allowing future improvements without requiring large-scale redesign.

---

## 4. Parallel Development

The project roadmap assigns different responsibilities to multiple team members.

The architecture therefore minimizes dependencies between modules so that backend, frontend, machine learning, and documentation work can proceed simultaneously.

---

## 5. Reproducibility

Every component of the system should be reproducible using the approved development environment.

Training workflows, preprocessing pipelines, dependency management, and API behavior should produce consistent results across development environments.

---

## 6. Explainability

The system emphasizes interpretable decision support rather than black-box automation.

Predictions, district rankings, and recommendations should be accompanied by meaningful explanations whenever possible.

---

## 7. Future Extensibility

Although the MVP focuses on historical analysis and district prioritization, the architecture should accommodate future enhancements without major structural changes.

Examples include:

- Multi-month forecasting
- PostgreSQL migration
- Cloud-native deployment
- Population density integration
- Retrieval-Augmented Generation (RAG)

These enhancements remain outside the current project scope.

---

# Architectural Principles

The architecture follows several guiding principles throughout implementation.

---

## Layered Architecture

Responsibilities are divided into independent layers.

Each layer communicates only with adjacent layers through well-defined interfaces.

This reduces coupling while improving maintainability.

---

## Backend-Centric Business Logic

Business rules are implemented exclusively within the backend.

Examples include:

- Machine learning inference
- District Priority Score generation
- Recommendation logic
- AI request orchestration
- Data aggregation

The frontend never performs business calculations.

---

## Frontend as Presentation Layer

The frontend focuses exclusively on user interaction and visualization.

Responsibilities include:

- Maps
- Charts
- Tables
- Search
- Filters
- Dashboard navigation
- AI chat interface

The frontend consumes backend APIs and does not directly access datasets or trained models.

---

## Single Source of Truth

Each type of project data has one authoritative source.

Examples include:

| Asset                 | Source of Truth                 |
| --------------------- | ------------------------------- |
| Raw datasets          | Original official datasets      |
| Clean datasets        | Generated preprocessing outputs |
| Trained models        | Joblib model artifacts          |
| Backend data          | SQLite database                 |
| Python dependencies   | pyproject.toml + uv.lock        |
| Frontend dependencies | package.json                    |

This minimizes inconsistencies throughout development.

---

## Reusable Components

Both frontend and backend components should maximize reuse.

Examples include:

Frontend:

- Reusable charts
- Shared layout components
- Common filters
- Shared API services

Backend:

- Shared utility functions
- Reusable service classes
- Modular prediction interfaces
- Common validation logic

---

## Loose Coupling

Modules communicate using stable interfaces rather than implementation details.

This enables future replacement or improvement of individual modules with minimal impact on the overall architecture.

---

## Explainable AI

Artificial Intelligence assists users by interpreting outputs rather than generating planning decisions.

Machine learning models remain responsible for prediction.

The Decision Engine remains responsible for district prioritization.

The LLM explains these outputs using natural language.

---

# Architectural Style

EVision Telangana follows a **Layered Client–Server Architecture**.

The system separates user interaction, application logic, machine learning, and data management into independent architectural layers.

```
+-----------------------------------------------------------+
|                    Presentation Layer                     |
|-----------------------------------------------------------|
| React Dashboard                                            |
| Maps • Charts • Tables • AI Chat • User Interaction       |
+----------------------------▲------------------------------+
                             │ REST API
+----------------------------│------------------------------+
|                    Application Layer                      |
|-----------------------------------------------------------|
| FastAPI Backend                                            |
| Routing • Validation • API Controllers                    |
+----------------------------▲------------------------------+
                             │
+----------------------------│------------------------------+
|                   Business Logic Layer                    |
|-----------------------------------------------------------|
| Decision Engine                                             |
| Analytics Engine                                            |
| AI Orchestration                                             |
| ML Service                                                   |
+----------------------------▲------------------------------+
                             │
+----------------------------│------------------------------+
|                  Machine Learning Layer                   |
|-----------------------------------------------------------|
| Random Forest                                                |
| XGBoost                                                      |
| K-Means                                                      |
| Model Persistence                                             |
+----------------------------▲------------------------------+
                             │
+----------------------------│------------------------------+
|                        Data Layer                          |
|-----------------------------------------------------------|
| SQLite Database                                              |
| Processed Datasets                                            |
| GeoJSON Files                                                 |
| Joblib Models                                                 |
+-----------------------------------------------------------+
```

Each layer communicates only through controlled interfaces.

This architecture simplifies maintenance, testing, debugging, and future expansion.

---

# High-Level System Architecture

The system consists of seven major components.

```
                     +----------------------+
                     |        User          |
                     +----------+-----------+
                                |
                                v
                 +------------------------------+
                 |     React Web Dashboard      |
                 +--------------+---------------+
                                |
                         REST API Requests
                                |
                                v
                 +------------------------------+
                 |      FastAPI Backend         |
                 +--------------+---------------+
                                |
        +-----------+-----------+-----------+-----------+
        |           |           |           |           |
        v           v           v           v           v
+---------------+ +---------------+ +---------------+ +---------------+
| SQLite DB     | | Decision      | | ML Engine     | | AI Assistant  |
|               | | Engine        | |               | | Service        |
+---------------+ +---------------+ +---------------+ +---------------+
                                        |
                                        v
                              +--------------------+
                              | Trained Models     |
                              | Random Forest      |
                              | XGBoost            |
                              | K-Means            |
                              +--------------------+
```

The backend acts as the central coordination layer.

All requests, predictions, recommendations, database operations, and AI interactions pass through the backend before responses are returned to the frontend.

No component communicates directly with the machine learning models or database except the backend.

---

# Technology Mapping

The following table maps each architectural layer to its approved implementation technologies.

| Architectural Layer     | Primary Technology                          | Purpose                                                |
| ----------------------- | ------------------------------------------- | ------------------------------------------------------ |
| Programming Language    | Python 3.12.x                               | Backend, machine learning, and data processing         |
| Python Environment      | uv                                          | Dependency and virtual environment management          |
| Frontend Framework      | React + Vite                                | Interactive web application                            |
| Styling                 | Tailwind CSS                                | Responsive user interface                              |
| Backend Framework       | FastAPI                                     | REST API and application services                      |
| ORM                     | SQLModel                                    | Database models and data validation                    |
| Database                | SQLite                                      | Local application data storage                         |
| Data Processing         | Pandas                                      | Data cleaning, transformation, and feature engineering |
| Numerical Computing     | NumPy                                       | Mathematical and numerical operations                  |
| Machine Learning        | Scikit-learn                                | Regression, clustering, and model evaluation           |
| Gradient Boosting       | XGBoost                                     | Alternative regression model                           |
| Model Persistence       | Joblib                                      | Serialization and loading of trained models            |
| Maps                    | React Leaflet + OpenStreetMap               | Geographic visualization                               |
| Charts                  | Recharts                                    | Interactive dashboard visualizations                   |
| HTTP Client             | Axios                                       | Frontend-to-backend communication                      |
| AI Integration          | Gemini API (Primary), OpenAI API (Optional) | Natural language explanations                          |
| API Testing             | Bruno                                       | REST API testing and request collections               |
| Linting & Formatting    | Ruff                                        | Python linting and formatting                          |
| Version Control         | Git + GitHub                                | Source code management                                 |
| Development Environment | Visual Studio Code                          | Integrated development environment                     |

This technology mapping provides a consolidated view of the approved implementation technologies used across each architectural layer.

---

# Major System Components

The architecture is composed of several independent but cooperating modules.

## 1. Presentation Layer

The Presentation Layer provides the graphical user interface through which users interact with the application.

Primary responsibilities include:

- Dashboard navigation
- Interactive maps
- Charts
- District comparison
- Search and filtering
- AI chat interface
- Display of predictions
- Display of recommendations

Technologies:

- React
- Vite
- Tailwind CSS
- React Leaflet
- Recharts

---

## 2. Backend API Layer

The Backend API Layer serves as the communication gateway between the frontend and the application's internal services.

Responsibilities include:

- API routing
- Request validation
- Response formatting
- Error handling
- Service orchestration
- Data aggregation

Technology:

- FastAPI

---

## 3. Data Processing Pipeline

The Data Processing Pipeline prepares all datasets used by downstream modules.

Responsibilities include:

- Data cleaning
- Dataset integration
- Duplicate removal
- Missing value handling
- Feature engineering
- Master dataset generation

The pipeline operates offline during the data preparation phase and produces processed datasets for model training and application use.

---

## 4. Machine Learning Engine

The Machine Learning Engine generates future charging demand predictions.

Responsibilities include:

- Model training
- Model evaluation
- Model comparison
- Model persistence
- Prediction inference
- Feature importance generation

Regression models considered include:

- Random Forest Regressor
- XGBoost Regressor

The better-performing model is selected based on evaluation metrics.

---

## 5. Analytics Engine

The Analytics Engine provides descriptive insights rather than predictive outputs.

Responsibilities include:

- K-Means clustering
- District profiling
- Trend analysis
- Exploratory analytics

These analyses support visualization and interpretation within the dashboard.

---

## 6. Decision Engine

The Decision Engine combines multiple analytical outputs to prioritize districts for future EV charging infrastructure expansion.

Responsibilities include:

- Infrastructure gap analysis
- Integration of prediction results
- District Priority Score computation
- District ranking
- Recommendation generation

The Decision Engine represents the primary decision support component of the system.

---

## 7. AI Assistant

The AI Assistant provides natural language explanations of system outputs.

Responsibilities include:

- Explaining predictions
- Comparing districts
- Summarizing trends
- Interpreting recommendations
- Answering project-related questions

The assistant does not replace machine learning models or make planning decisions independently.

---

# Component Responsibility Matrix

The following matrix summarizes the responsibilities, inputs, outputs, and dependencies of each major architectural component.

| Component                | Primary Responsibilities                                                               | Inputs                                      | Outputs                                             | Depends On                                                |
| ------------------------ | -------------------------------------------------------------------------------------- | ------------------------------------------- | --------------------------------------------------- | --------------------------------------------------------- |
| Data Processing Pipeline | Data validation, cleaning, integration, feature engineering, master dataset generation | Official datasets                           | Clean master dataset                                | Pandas, NumPy                                             |
| Machine Learning Engine  | Model training, evaluation, prediction, feature importance                             | Master dataset                              | Demand predictions, trained models                  | Scikit-learn, XGBoost, Joblib                             |
| Analytics Engine         | District clustering, trend analysis, district profiling                                | Processed dataset                           | Cluster assignments, analytical summaries           | Scikit-learn                                              |
| Decision Engine          | Infrastructure analysis, District Priority Score computation, district ranking         | Predictions, infrastructure data, analytics | District Priority Scores, rankings, recommendations | Machine Learning Engine, Analytics Engine                 |
| SQLite Database          | Store processed application data and metadata                                          | Processed datasets                          | Application data                                    | SQLModel                                                  |
| Backend API              | Request handling, business logic orchestration, response generation                    | Frontend API requests                       | JSON responses                                      | FastAPI, Database, Decision Engine, ML Engine, AI Service |
| AI Assistant Service     | Prompt construction, context preparation, explanation generation                       | User queries, backend context               | Natural language responses                          | Gemini API / OpenAI API                                   |
| Frontend Dashboard       | User interaction, visualization, maps, charts, AI interface                            | Backend responses                           | Interactive dashboard                               | React, Axios, Recharts, React Leaflet                     |
| Map Module               | Geographic visualization of Telangana districts and charging stations                  | GeoJSON, charging station data              | Interactive maps                                    | React Leaflet, OpenStreetMap                              |
| Visualization Module     | Display charts, comparisons, analytical summaries                                      | Analytics data                              | Charts and visual reports                           | Recharts                                                  |
| Repository Layer         | Database abstraction and data access                                                   | Service requests                            | Database records                                    | SQLModel, SQLite                                          |
| Configuration Module     | Centralized runtime configuration                                                      | Environment variables                       | Application configuration                           | `.env`, configuration loader                              |
| Logging Module           | Runtime logging and diagnostics                                                        | Application events                          | Log records                                         | Python logging utilities                                  |

The Component Responsibility Matrix provides a high-level overview of how the system modules collaborate while maintaining clear separation of concerns. Each component has a well-defined responsibility, communicates through controlled interfaces, and depends only on the services required to fulfill its role within the overall architecture.

---

# Component Interaction Overview

The major components interact through the following sequence.

1. Data Processing Pipeline prepares the master dataset.
2. Machine Learning Engine trains predictive models.
3. Trained models are persisted using Joblib.
4. FastAPI loads trained models during application startup.
5. Users interact with the React dashboard.
6. API requests are routed to backend services.
7. Backend retrieves required data.
8. Machine Learning Engine performs inference.
9. Decision Engine computes district priorities.
10. Results are returned to the frontend.
11. AI Assistant generates explanations using backend-provided context.
12. The dashboard presents visualizations and recommendations to the user.

This controlled interaction ensures that every architectural layer remains responsible only for its designated tasks.

---

# System Data Flow

The EVision Telangana system follows a structured data flow that transforms raw historical datasets into actionable decision support insights.

The workflow is divided into two major stages:

1. Offline Processing
2. Online Application Execution

Offline processing prepares datasets and trains machine learning models.

Online execution serves predictions, analytics, and explanations to end users through the web application.

---

# Offline Data Flow

Offline processing is performed before the application is deployed.

Its objective is to generate all artifacts required during application runtime.

```
Official Datasets
        │
        ▼
Data Validation
        │
        ▼
Data Cleaning
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
 ┌──────┴────────┐
 ▼               ▼
Analytics      Machine Learning
 │               │
 ▼               ▼
K-Means      Random Forest
             XGBoost
 │               │
 └──────┬────────┘
        ▼
Model Evaluation
        │
        ▼
Best Model Selection
        │
        ▼
Joblib Model Files
```

Outputs generated during offline processing include:

- Clean master dataset
- Trained regression model
- K-Means clustering model
- Feature engineering outputs
- Evaluation metrics
- Model artifacts

These artifacts are consumed by the application during runtime.

---

# Online Data Flow

The online workflow begins when a user interacts with the web application.

```
User
 │
 ▼
React Dashboard
 │
 ▼
FastAPI Backend
 │
 ├─────────────► SQLite Database
 │
 ├─────────────► Machine Learning Models
 │
 ├─────────────► Decision Engine
 │
 └─────────────► AI Assistant Service
 │
 ▼
JSON Response
 │
 ▼
Dashboard Visualization
```

Every request is processed through the backend.

The frontend never accesses the database or machine learning models directly.

---

# End-to-End Request Flow

The following sequence illustrates a typical application request.

1. User opens the dashboard.

2. Frontend requests district information.

3. Backend validates the request.

4. Backend retrieves required records.

5. Machine Learning Engine performs prediction if required.

6. Decision Engine computes district priority.

7. Backend formats the response.

8. Frontend updates maps and charts.

9. User may request additional explanation through the AI Assistant.

10. Backend prepares contextual information.

11. Gemini API generates a natural language explanation.

12. Response is displayed within the dashboard.

---

# Data Sources

The system uses multiple official datasets.

## EV Charging Consumption

Historical electricity consumption data provides the foundation for demand prediction.

These datasets are processed into a unified historical charging demand dataset.

---

## Charging Station Information

Existing charging station information provides infrastructure availability.

This data supports:

- Infrastructure visualization
- Gap analysis
- District comparison
- Decision Engine

---

## District Boundary Dataset

The district boundary dataset provides geographic visualization.

Responsibilities include:

- District polygons
- Interactive maps
- Spatial analysis
- Dashboard rendering

---

# Data Processing Pipeline Architecture

The Data Processing Pipeline is responsible for transforming raw datasets into machine learning-ready data.

```
Raw Dataset
     │
     ▼
Validation
     │
     ▼
Cleaning
     │
     ▼
Duplicate Removal
     │
     ▼
Missing Value Handling
     │
     ▼
Standardization
     │
     ▼
Feature Engineering
     │
     ▼
Master Dataset
```

Each stage performs one well-defined responsibility.

Intermediate outputs should remain reproducible.

---

# Pipeline Stages

## Data Validation

Responsibilities:

- Verify schema
- Verify column names
- Verify district names
- Detect corrupted records
- Validate numeric values

Outputs:

Validated raw datasets.

---

## Data Cleaning

Responsibilities:

- Remove invalid records
- Normalize formats
- Correct inconsistent values
- Standardize text

Outputs:

Clean datasets.

---

## Dataset Integration

Responsibilities:

- Merge datasets
- Align temporal information
- Standardize districts
- Preserve historical records

Outputs:

Unified historical dataset.

---

## Feature Engineering

Responsibilities:

- Generate predictive features
- Aggregate historical values
- Encode categorical information
- Prepare ML-ready variables

Outputs:

Training dataset.

---

## Artifact Generation

Responsibilities:

- Export processed dataset
- Save trained models
- Store evaluation results

Outputs:

Application-ready artifacts.

---

# Backend Architecture

The backend implements the application's business logic.

It coordinates every major system module.

The architecture follows a layered design.

```
+---------------------------------------+
| REST API Controllers                  |
+---------------------------------------+
| Application Services                  |
+---------------------------------------+
| Decision Engine                       |
| Machine Learning Service              |
| AI Service                            |
+---------------------------------------+
| Repository Layer                      |
+---------------------------------------+
| SQLite Database                       |
| Joblib Models                         |
+---------------------------------------+
```

Each layer has clearly defined responsibilities.

---

# API Layer

The API layer receives HTTP requests from the frontend.

Responsibilities include:

- Routing
- Validation
- Serialization
- Status codes
- Error responses

The API layer contains minimal business logic.

---

# Service Layer

The Service Layer coordinates application behavior.

Responsibilities include:

- Business workflows
- Data aggregation
- Calling repositories
- Calling ML services
- Calling AI services

The Service Layer serves as the primary orchestration layer.

---

# Machine Learning Service

The Machine Learning Service abstracts model inference.

Responsibilities include:

- Load trained models
- Prepare inference features
- Generate predictions
- Return prediction results

The frontend never communicates directly with trained models.

---

# Decision Engine Service

The Decision Engine combines analytical outputs into actionable recommendations.

Inputs include:

- Predicted charging demand
- Existing charging infrastructure
- District analytics

Outputs include:

- District Priority Score
- Ranking
- Supporting insights

---

# AI Service

The AI Service manages interactions with the LLM.

Responsibilities include:

- Prompt construction
- Context preparation
- API communication
- Response validation

The AI Service never performs predictive analytics.

---

# Repository Layer

The Repository Layer manages application data.

Responsibilities include:

- Database access
- Query abstraction
- Data retrieval
- Data persistence

Separating repositories from business logic improves maintainability.

---

# Frontend Architecture

The frontend follows a component-based architecture using React.

```
App
 │
 ├── Dashboard
 ├── Map View
 ├── Analytics
 ├── District Details
 ├── Recommendations
 ├── AI Assistant
 └── Shared Components
```

Reusable components minimize duplication throughout the application.

---

# Frontend Layers

The frontend is divided into four logical layers.

```
Pages
 │
 ▼
Reusable Components
 │
 ▼
API Service Layer
 │
 ▼
Backend REST APIs
```

This separation improves maintainability and testing.

---

# Page Components

Major pages include:

- Dashboard
- District Explorer
- Predictions
- Recommendation View
- AI Assistant

Each page combines multiple reusable UI components.

---

# Shared Components

Examples include:

- Navigation bar
- Sidebar
- Charts
- Cards
- Tables
- Filters
- Search box
- Loading indicators
- Error components

These components should remain presentation-only.

---

# API Service Layer

The API Service Layer centralizes all backend communication.

Responsibilities include:

- Axios configuration
- Request handling
- Response handling
- Error handling

This prevents HTTP logic from being duplicated across components.

---

# State Management

The application uses React Hooks for state management.

Typical state includes:

- Selected district
- Filters
- Search text
- Prediction results
- Dashboard settings
- AI conversation

Global state should remain minimal.

---

# Database Architecture

SQLite serves as the application's local database.

The database stores processed application data required during runtime.

Training datasets remain external artifacts.

---

# Database Responsibilities

The database supports:

- Processed district data
- Infrastructure metadata
- Application lookup data
- Cached processed information (if required)

Machine learning models are not stored within the database.

---

# Logical Data Organization

```
SQLite
 │
 ├── District Information
 ├── Charging Stations
 ├── Processed Metrics
 ├── Infrastructure Metadata
 └── Application Configuration
```

This logical organization simplifies future migration to PostgreSQL if required.

---

# Model Storage

Machine learning models are persisted separately.

```
models/
    best_regression.joblib
    kmeans.joblib
```

Models are loaded during backend startup.

No retraining occurs during normal application execution.

---

# API Architecture

The backend exposes RESTful APIs.

Each endpoint belongs to a logical functional category.

Examples include:

- Dashboard APIs
- District APIs
- Prediction APIs
- Analytics APIs
- Recommendation APIs
- AI Assistant APIs

Each endpoint returns JSON responses.

---

# API Design Principles

The API follows several design principles.

## Stateless Communication

Every request contains all information required for processing.

The server does not maintain conversational session state beyond what is necessary for the AI Assistant interaction.

---

## JSON-Based Communication

Requests and responses use JSON.

This simplifies integration between frontend and backend.

---

## Consistent Response Structure

Every response should follow a consistent structure.

Typical responses include:

- Status
- Requested data
- Optional metadata
- Error details when applicable

---

## Validation

All incoming requests are validated before processing.

Invalid requests return informative error responses without affecting application stability.

---

## Error Handling

Unexpected failures should return standardized error responses.

Internal implementation details should not be exposed to end users.

Meaningful logging should be performed within the backend for debugging purposes.

---

# Machine Learning Architecture

The Machine Learning Architecture is responsible for forecasting future EV charging demand and generating analytical insights that support infrastructure planning.

The machine learning workflow is intentionally separated into two independent stages:

1. Training Workflow
2. Inference Workflow

This separation ensures that computationally intensive model training occurs offline, while application runtime remains lightweight and responsive.

---

# Machine Learning Workflow

```
Historical Dataset
        │
        ▼
Feature Engineering
        │
        ▼
Training Dataset
        │
        ▼
Train Regression Models
        │
 ┌──────┴────────┐
 ▼               ▼
Random Forest   XGBoost
        │
        ▼
Model Evaluation
        │
        ▼
Best Model Selection
        │
        ▼
Joblib Model
        │
        ▼
Backend Inference
```

Only the selected regression model is loaded during application execution.

---

# Training Workflow

Model training is performed offline during development.

The workflow consists of the following stages:

1. Load processed training dataset.
2. Split data into training and testing sets.
3. Train Random Forest Regressor.
4. Train XGBoost Regressor.
5. Evaluate both models.
6. Compare evaluation metrics.
7. Select the better-performing model.
8. Persist the selected model using Joblib.

Training is not performed while the application is running.

---

# Model Evaluation

Regression models are evaluated using the approved metrics.

Evaluation metrics include:

- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- Coefficient of Determination (R² Score)

The final regression model is selected according to these evaluation results.

---

# Inference Workflow

During runtime, the backend performs prediction using the previously trained model.

```
API Request
      │
      ▼
Load Features
      │
      ▼
Load Joblib Model
      │
      ▼
Prediction
      │
      ▼
Prediction Result
```

Inference is stateless and does not modify the trained model.

---

# Clustering Architecture

District clustering is implemented independently of the regression workflow.

The clustering process provides descriptive analytics rather than predictive outputs.

```
Processed Dataset
        │
        ▼
Feature Selection
        │
        ▼
K-Means Training
        │
        ▼
District Clusters
        │
        ▼
Dashboard Visualization
```

Cluster assignments support district profiling and visualization.

They are not used as direct inputs for future demand prediction.

---

# Feature Engineering Architecture

Feature engineering transforms cleaned historical datasets into machine learning-ready inputs.

Typical responsibilities include:

- Temporal aggregation
- Historical demand summaries
- District normalization
- Numerical encoding
- Derived analytical variables

Feature engineering remains deterministic so that identical input datasets always produce identical training features.

---

# Model Persistence

Trained models are stored as serialized Joblib artifacts.

Responsibilities include:

- Fast loading
- Reproducible inference
- Version-controlled model artifacts
- Separation of training and runtime

Example directory:

```
models/
    regression.joblib
    kmeans.joblib
```

---

# Machine Learning Responsibilities

The Machine Learning Engine is responsible for:

- Historical demand prediction
- Model evaluation
- Model comparison
- Feature importance analysis
- Prediction inference

The Machine Learning Engine is not responsible for:

- District prioritization
- Infrastructure recommendations
- User interaction
- Natural language explanations

These responsibilities belong to other architectural modules.

---

# Decision Engine Architecture

The Decision Engine is the core decision support component of the system.

It combines outputs from multiple analytical modules to generate district-level recommendations for future EV charging infrastructure expansion.

The Decision Engine operates entirely within the backend.

---

# Decision Engine Workflow

```
Historical Analytics
          │
          ▼
Future Demand Prediction
          │
          ▼
Infrastructure Information
          │
          ▼
District Analytics
          │
          ▼
Decision Engine
          │
          ▼
District Priority Score
          │
          ▼
Ranked Districts
```

The Decision Engine does not train machine learning models.

Instead, it consumes prediction outputs generated by the Machine Learning Engine.

---

# Decision Engine Inputs

The Decision Engine receives information from several sources.

Examples include:

- Predicted charging demand
- Existing charging infrastructure
- District analytics
- Cluster information
- Historical demand summaries

These inputs are combined to produce recommendation outputs.

---

# District Priority Score

The District Priority Score (DPS) represents the primary recommendation produced by the application.

Its objective is to prioritize districts for future EV charging infrastructure expansion.

The precise computation remains implementation-dependent and may evolve following model evaluation.

Regardless of implementation details, the Decision Engine should produce a consistent and explainable ranking for every district.

---

# Decision Engine Outputs

Primary outputs include:

- District Priority Score
- District ranking
- Supporting analytical information
- Recommendation summaries

These outputs are consumed by both the frontend dashboard and the AI Assistant.

---

# Explainability Support

The Decision Engine should expose sufficient contextual information to allow downstream explanation.

Examples include:

- Predicted demand trends
- Infrastructure availability
- Relative district comparisons
- Supporting analytical indicators

This information enables the AI Assistant to generate meaningful explanations without independently interpreting raw datasets.

---

# AI Assistant Architecture

The AI Assistant provides natural language interaction for users exploring the dashboard.

The assistant serves as an interpretation layer rather than a prediction engine.

---

# AI Assistant Workflow

```
User Question
       │
       ▼
Frontend Chat Interface
       │
       ▼
FastAPI Backend
       │
       ▼
Context Preparation
       │
       ▼
LLM API
       │
       ▼
Generated Explanation
       │
       ▼
Frontend Response
```

The backend prepares all relevant context before sending a request to the selected LLM provider.

---

# AI Assistant Responsibilities

The AI Assistant is responsible for:

- Explaining predictions
- Explaining district rankings
- Comparing districts
- Summarizing dashboard insights
- Explaining analytical visualizations
- Answering project-related questions

---

# AI Assistant Boundaries

The AI Assistant is intentionally restricted.

It does not:

- Train models
- Generate predictions
- Compute District Priority Scores
- Modify analytical results
- Replace backend decision logic

The assistant explains outputs produced by the Machine Learning Engine and Decision Engine.

---

# Prompt Construction

The backend constructs prompts using trusted application context.

Prompt context may include:

- District information
- Prediction outputs
- Infrastructure statistics
- Analytical summaries
- User questions

The LLM should never receive unrestricted access to internal datasets or application logic.

---

# AI Provider Abstraction

The architecture supports interchangeable LLM providers.

Primary provider:

- Gemini API

Optional provider:

- OpenAI API

Provider abstraction allows future migration with minimal changes to application code.

---

# Repository Architecture

The project follows a modular repository organization. The definitive repository structure is specified in the Repository Structure document. The overview below illustrates the intended architectural organization of the project.

Each directory has a single primary responsibility.

```
EVision-Telangana/
│
├── backend/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── database/
│   ├── schemas/
│   ├── repositories/
│   ├── utils/
│   ├── config/
│   └── main.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   ├── services/
│   │   ├── hooks/
│   │   ├── assets/
│   │   ├── styles/
│   │   └── App.jsx
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── models/
│
├── notebooks/
│
├── scripts/
│
├── tests/
│
├── docs/
│
├── report/
│
├── presentation/
│
├── .env.example
├── pyproject.toml
├── uv.lock
├── package.json
├── README.md
└── .gitignore
```

This structure separates implementation, datasets, documentation, and project artifacts while supporting parallel team development.

---

# Configuration Management

Application configuration should remain external to source code.

Configuration includes:

- API keys
- Environment variables
- Database location
- Model paths
- Runtime settings

Sensitive information should never be committed to version control.

---

# Environment Variables

Typical configuration values include:

- Gemini API key
- OpenAI API key (optional)
- Database path
- Model directory
- Backend host
- Backend port

An `.env.example` file should document all required configuration variables.

---

# Logging Strategy

The backend should maintain structured logging throughout application execution.

Typical logging events include:

- Application startup
- Model loading
- API requests
- Prediction requests
- AI requests
- Errors
- Unexpected exceptions

Logging should assist debugging without exposing sensitive information.

---

# Error Handling Strategy

Errors should be handled consistently across all architectural layers.

Categories include:

- Validation errors
- Missing resources
- Prediction failures
- AI service failures
- Internal server errors

The frontend should receive informative but user-friendly error messages.

Detailed diagnostic information should remain within backend logs.

---

# Input Validation

Incoming requests should be validated before processing.

Validation responsibilities include:

- Required fields
- Data types
- Accepted parameter ranges
- Request format

Invalid requests should terminate before reaching business logic.

---

# Performance Considerations

The architecture prioritizes responsive user interaction.

Performance improvements include:

- Loading trained models once during application startup
- Reusing database connections where appropriate
- Avoiding unnecessary recomputation
- Separating offline training from online inference

These decisions reduce runtime latency while keeping the implementation straightforward.

---

# Scalability Considerations

Although the MVP targets a local academic deployment, the architecture avoids unnecessary constraints that would prevent future growth.

Potential scalability improvements include:

- Migration to PostgreSQL
- Distributed model serving
- Cloud deployment
- External object storage
- API rate limiting
- Response caching

These enhancements remain outside the approved MVP scope.

---

# Security Considerations

EVision Telangana is an academic Decision Support System intended for local deployment.

Although the project does not process sensitive personal information or implement user authentication, the architecture incorporates basic security practices to promote safe and reliable operation.

---

# API Security

The backend serves as the only entry point to application services.

All requests should pass through the FastAPI application where they are validated before processing.

The frontend must never communicate directly with:

- SQLite database
- Machine learning models
- Local data files
- AI provider APIs

Centralizing all communication through the backend simplifies validation and reduces the application's attack surface.

---

# Environment Variable Protection

Sensitive configuration values should be stored outside the source code.

Examples include:

- Gemini API key
- OpenAI API key (optional)
- Future deployment configuration

Configuration values should be loaded from environment variables during application startup.

The repository should include an `.env.example` file documenting the required variables without exposing actual credentials.

---

# Input Sanitization

All incoming requests should be validated before entering the business logic layer.

Validation should include:

- Required parameter checks
- Data type validation
- Range validation
- String sanitization
- Invalid request rejection

These measures improve application robustness and reduce unexpected failures.

---

# Error Exposure

Unexpected internal errors should never expose implementation details.

User-facing responses should contain concise, informative messages, while detailed diagnostic information should remain available only through backend logs.

---

# Model Protection

Machine learning models are application assets.

The frontend should never have direct access to serialized model files.

All inference requests should be routed through the backend's Machine Learning Service.

---

# AI Service Protection

The backend controls all communication with external LLM providers.

Responsibilities include:

- Prompt construction
- Context preparation
- API authentication
- Response validation

This architecture prevents exposure of API credentials and ensures consistent AI behavior.

---

# Cross-Cutting Concerns

Several architectural concerns apply across all system modules.

These concerns improve maintainability, consistency, and operational quality.

---

# Configuration

Application configuration should be centralized.

Configuration includes:

- Environment variables
- API settings
- Database location
- Model paths
- Runtime options

Modules should access configuration through a common configuration service rather than hard-coded values.

---

# Validation

Validation should occur as early as possible within the request lifecycle.

Responsibilities include:

- API validation
- Schema validation
- Database validation
- Machine learning input validation

Consistent validation reduces downstream errors.

---

# Exception Handling

Exceptions should be handled at the appropriate architectural layer.

Examples include:

| Layer                    | Responsibility                    |
| ------------------------ | --------------------------------- |
| API Layer                | Return appropriate HTTP responses |
| Service Layer            | Handle business exceptions        |
| Repository Layer         | Handle data access failures       |
| AI Service               | Handle provider-specific failures |
| Machine Learning Service | Handle inference failures         |

Unhandled exceptions should be logged and converted into standardized error responses.

---

# Logging

Logging should remain consistent throughout the application.

Recommended logging events include:

- Application startup
- Configuration loading
- Database initialization
- Model loading
- API requests
- Prediction execution
- AI requests
- Warning events
- Error events

Structured logging improves troubleshooting during integration and demonstration.

---

# Deployment Architecture

Deployment is considered an optional enhancement after successful completion of the MVP.

The architecture supports both local execution and optional cloud deployment without requiring structural changes.

---

# Local Development Architecture

During development, all services execute on the developer's local machine.

```
+----------------------+
| React Development    |
| Server               |
+----------+-----------+
           |
           v
+----------------------+
| FastAPI Backend      |
+----------+-----------+
           |
    +------+------+------------------+
    |             |                  |
    v             v                  v
SQLite      Joblib Models      Gemini API
```

This deployment model supports rapid development and debugging.

---

# Optional Cloud Deployment

If deployment is attempted after feature completion, the recommended architecture is:

```
                 Users
                   │
                   ▼
        +----------------------+
        |       Vercel         |
        | React Frontend       |
        +----------+-----------+
                   │
             HTTPS Requests
                   │
                   ▼
        +----------------------+
        |       Render         |
        | FastAPI Backend      |
        +----------+-----------+
                   │
        +----------+-----------+
        |                      |
        ▼                      ▼
   SQLite Database       Gemini API
```

The deployment architecture mirrors the local architecture while replacing local services with hosted equivalents.

---

# Runtime Startup Sequence

When the backend starts, the following sequence is executed.

1. Load configuration.
2. Initialize logging.
3. Connect to SQLite.
4. Load trained Joblib models.
5. Register API routes.
6. Initialize AI service.
7. Start FastAPI application.

Completing initialization before serving requests reduces runtime delays.

---

# Shutdown Sequence

During application shutdown, the backend should:

1. Close database connections.
2. Release application resources.
3. Flush pending logs.
4. Terminate gracefully.

Graceful shutdown helps maintain application stability during development and deployment.

---

# Architectural Decisions

The architecture incorporates several intentional design decisions to balance simplicity, maintainability, and project requirements.

---

## Decision 1 — Layered Client–Server Architecture

**Decision**

Adopt a layered client–server architecture.

**Rationale**

This architecture clearly separates presentation, business logic, machine learning, and data management.

It also supports independent module development and simplifies maintenance.

---

## Decision 2 — FastAPI Backend

**Decision**

Use FastAPI as the backend framework.

**Rationale**

FastAPI provides:

- High performance
- Automatic validation
- REST API support
- Interactive API documentation
- Strong integration with Python data science libraries

---

## Decision 3 — React + Vite Frontend

**Decision**

Use React with Vite.

**Rationale**

React enables reusable component-based interfaces, while Vite provides a lightweight development experience with fast build times.

---

## Decision 4 — SQLite Database

**Decision**

Use SQLite for the MVP.

**Rationale**

SQLite satisfies project requirements without introducing unnecessary operational complexity.

The architecture remains portable to PostgreSQL if future migration becomes necessary.

---

## Decision 5 — Joblib Model Persistence

**Decision**

Persist trained models using Joblib.

**Rationale**

Joblib provides efficient serialization for Scikit-learn and XGBoost models while keeping runtime inference lightweight.

---

## Decision 6 — Separate Training and Inference

**Decision**

Separate machine learning training from runtime inference.

**Rationale**

Training is computationally expensive and unnecessary during normal application execution.

Separating these workflows improves responsiveness and reproducibility.

---

## Decision 7 — Backend-Owned Business Logic

**Decision**

Centralize all business logic within the backend.

**Rationale**

This prevents duplication of logic, simplifies maintenance, and ensures consistent analytical results regardless of frontend implementation.

---

## Decision 8 — AI as an Explanation Layer

**Decision**

Restrict the AI Assistant to explanation and interpretation.

**Rationale**

Predictions and recommendations should remain deterministic outputs generated by the Machine Learning Engine and Decision Engine.

The LLM enhances usability by translating these outputs into natural language rather than making planning decisions independently.

---

# Future Architectural Extensions

The current architecture intentionally focuses on the approved MVP.

Several architectural enhancements may be considered for future versions.

Possible enhancements include:

- PostgreSQL migration
- Cloud-native deployment
- Retrieval-Augmented Generation (RAG)
- Population density integration
- Road network analysis
- Multi-month forecasting
- Advanced dashboard analytics
- Continuous model updates
- Mobile application support

These enhancements should be implemented without altering the modular architecture established in this document.

---

# Architecture Diagram Index

The following diagrams accompany this architecture document.

| Diagram    | Description                      |
| ---------- | -------------------------------- |
| Diagram 1  | High-Level System Architecture   |
| Diagram 2  | Offline Data Processing Workflow |
| Diagram 3  | Online Application Data Flow     |
| Diagram 4  | Backend Layered Architecture     |
| Diagram 5  | Frontend Component Architecture  |
| Diagram 6  | Machine Learning Workflow        |
| Diagram 7  | Decision Engine Workflow         |
| Diagram 8  | AI Assistant Workflow            |
| Diagram 9  | Repository Structure             |
| Diagram 10 | Deployment Architecture          |

These diagrams provide visual representations of the architectural concepts described throughout this document.

---

# Architecture Governance

This document defines the approved software architecture for EVision Telangana.

All implementation activities should conform to the architectural principles, component responsibilities, and communication patterns described herein.

Architectural modifications should only be made when:

- Required to resolve verified implementation constraints,
- Required to address compatibility issues,
- Required by the project supervisor, or
- Required to correct factual inaccuracies.

Changes that expand the functional scope of the project should not be introduced through architectural modifications.

Any proposed enhancements beyond the approved MVP should be documented as future architectural extensions rather than incorporated into the current implementation.

---

# Conclusion

The EVision Telangana System Architecture establishes a modular, layered, and maintainable foundation for developing an AI-based EV Charging Infrastructure Planning and Decision Support System.

By separating data processing, machine learning, analytics, decision support, backend services, frontend presentation, and AI-assisted explanation into clearly defined architectural modules, the system promotes maintainability, parallel development, and reproducibility.

The architecture aligns with the approved project scope, implementation roadmap, and technology stack while remaining sufficiently flexible to accommodate future enhancements after completion of the MVP.

This document serves as the authoritative architectural reference for the implementation, integration, testing, deployment, and future evolution of EVision Telangana.
