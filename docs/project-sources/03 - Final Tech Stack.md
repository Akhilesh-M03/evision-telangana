- [Final Tech Stack](#final-tech-stack)
- [Purpose](#purpose)
- [Technology Selection Principles](#technology-selection-principles)
- [Technology Stack](#technology-stack)
- [Development Tool Versions](#development-tool-versions)
- [Repository Configuration](#repository-configuration)
  - [.editorconfig](#editorconfig)
- [Python Project Configuration](#python-project-configuration)
- [Backend Stack](#backend-stack)
  - [Framework](#framework)
  - [Database](#database)
  - [ORM](#orm)
- [Frontend Stack](#frontend-stack)
  - [Framework](#framework-1)
  - [Styling](#styling)
  - [Maps](#maps)
  - [Charts](#charts)
- [Data Science Stack](#data-science-stack)
  - [Data Processing](#data-processing)
  - [Numerical Computing](#numerical-computing)
  - [Machine Learning](#machine-learning)
  - [Gradient Boosting](#gradient-boosting)
  - [Model Persistence](#model-persistence)
- [AI Stack](#ai-stack)
- [API Testing](#api-testing)
- [Development Standards](#development-standards)
  - [Python](#python)
  - [Backend](#backend)
  - [Frontend](#frontend)
  - [Machine Learning](#machine-learning-1)
  - [Git](#git)
  - [Documentation](#documentation)
  - [Editor Standards](#editor-standards)
- [Project Structure Principles](#project-structure-principles)
  - [1. Separation of Concerns](#1-separation-of-concerns)
  - [2. Single Source of Truth](#2-single-source-of-truth)
  - [3. Backend Owns Business Logic](#3-backend-owns-business-logic)
  - [4. LLM Assists, It Does Not Decide](#4-llm-assists-it-does-not-decide)
  - [5. Reproducibility First](#5-reproducibility-first)
  - [6. Documentation Evolves with Development](#6-documentation-evolves-with-development)
  - [7. Deployment Is the Final Enhancement](#7-deployment-is-the-final-enhancement)
- [Deployment Strategy](#deployment-strategy)
  - [Frontend](#frontend-1)
  - [Backend](#backend-1)
  - [Database](#database-1)
- [Development Environment](#development-environment)
  - [Required Extensions](#required-extensions)
  - [Recommended Extensions](#recommended-extensions)
- [Technologies Not Selected](#technologies-not-selected)
- [Technology Governance](#technology-governance)


# Final Tech Stack

**Project:** EVision Telangana  
**Official Project Title:** AI-Based EV Charging Infrastructure Planning and Decision Support System for Telangana

**Version:** 1.0  
**Status:** Frozen  
**Last Updated:** July 2026

---

# Purpose

This document defines the approved technologies, development standards, tooling, and architectural principles for EVision Telangana.

The objective is to ensure that every team member develops the project using a consistent and reproducible technology stack.

This document is the authoritative reference for all implementation decisions unless superseded by a future approved revision.

---

# Technology Selection Principles

The technology stack has been selected using the following principles:

- Simplicity over unnecessary complexity
- Modern and industry-relevant technologies
- Open-source and free tools whenever possible
- Strong ecosystem and documentation
- Easy integration between components
- Reproducible development environment
- Suitable for completion within the project timeline

---

# Technology Stack

| Layer                  | Technology                                  | Purpose                                        |
| ---------------------- | ------------------------------------------- | ---------------------------------------------- |
| Programming Language   | Python 3.12.x                               | Backend, ML, Data Processing                   |
| Python Package Manager | uv                                          | Dependency and virtual environment management  |
| Dependency Files       | pyproject.toml + uv.lock                    | Reproducible Python environments               |
| Frontend               | React + Vite (JavaScript)                   | User Interface                                 |
| Styling                | Tailwind CSS                                | Responsive UI                                  |
| Backend                | FastAPI                                     | REST API                                       |
| ORM                    | SQLModel                                    | Database models and validation                 |
| Database               | SQLite                                      | Local application database                     |
| Data Processing        | Pandas                                      | Data cleaning and transformation               |
| Numerical Computing    | NumPy                                       | Numerical operations                           |
| Machine Learning       | Scikit-learn                                | Regression, clustering and evaluation          |
| Gradient Boosting      | XGBoost                                     | Alternative regression model                   |
| Model Persistence      | Joblib                                      | Save and load trained models                   |
| Maps                   | React Leaflet + OpenStreetMap               | Geographic visualization                       |
| Charts                 | Recharts                                    | Dashboard visualizations                       |
| HTTP Client            | Axios                                       | Frontend API communication                     |
| AI Assistant           | Gemini API (Primary), OpenAI API (Optional) | Natural language interaction                   |
| API Testing            | Bruno                                       | API testing and version-controlled collections |
| Linting & Formatting   | Ruff                                        | Python linting and formatting                  |
| Version Control        | Git + GitHub                                | Source code management                         |
| IDE                    | Visual Studio Code                          | Development environment                        |

---

# Development Tool Versions

The project targets the following runtime versions.

| Tool               | Version Policy            |
| ------------------ | ------------------------- |
| Python             | 3.12.x                    |
| Node.js            | 22.x LTS                  |
| npm                | Bundled with Node.js 22.x |
| Git                | Latest Stable             |
| Visual Studio Code | Latest Stable             |

Project libraries should use the latest stable version compatible with the selected runtime environments.

Exact dependency versions are managed by:

- `pyproject.toml`
- `uv.lock`
- `package.json`

---

# Repository Configuration

The following configuration files form part of the project and should always be committed to version control unless otherwise noted.

| File           | Purpose                                     |
| -------------- | ------------------------------------------- |
| pyproject.toml | Python project configuration                |
| uv.lock        | Locked Python dependencies                  |
| package.json   | Frontend dependencies                       |
| .editorconfig  | Repository editor configuration             |
| .gitignore     | Ignore generated files and local artifacts  |
| .env.example   | Template for required environment variables |
| README.md      | Project overview and setup instructions     |

---

## .editorconfig

The repository includes an `.editorconfig` file to maintain a consistent coding style across all development environments.

Standardized settings include:

- UTF-8 encoding
- LF line endings
- Final newline at end of file
- Spaces instead of tabs
- Four-space indentation for Python
- Two-space indentation for JSON, YAML, and Markdown
- Consistent whitespace handling

---

# Python Project Configuration

Python dependencies are managed using **uv**.

Project configuration is maintained in:

- `pyproject.toml`

Dependency locking is maintained in:

- `uv.lock`

The lock file must be committed to version control to ensure every team member uses an identical environment.

---

# Backend Stack

## Framework

FastAPI

Responsibilities:

- REST APIs
- Business logic
- Decision Engine
- AI Assistant integration
- Machine Learning inference

---

## Database

SQLite

Responsibilities:

- Store processed application data
- Store metadata if required
- Support local development

The architecture should remain portable to PostgreSQL if future migration becomes necessary.

---

## ORM

SQLModel

Responsibilities:

- Database models
- Data validation
- API schemas

---

# Frontend Stack

## Framework

React + Vite

Language:

JavaScript

Responsibilities:

- Dashboard
- Interactive maps
- Charts
- User interface
- AI Assistant interface

---

## Styling

Tailwind CSS

Purpose:

- Responsive layouts
- Consistent design system
- Rapid UI development

---

## Maps

React Leaflet

Map Provider:

OpenStreetMap

Purpose:

- Telangana district visualization
- Charging station visualization
- Interactive exploration

---

## Charts

Recharts

Primary chart types:

- Line Chart
- Bar Chart
- Pie Chart
- Scatter Plot

---

# Data Science Stack

## Data Processing

Pandas

Responsibilities:

- Cleaning
- Transformation
- Aggregation
- Feature engineering

---

## Numerical Computing

NumPy

Responsibilities:

- Mathematical operations
- Array processing

---

## Machine Learning

Scikit-learn

Algorithms:

- Random Forest Regressor
- K-Means Clustering

Evaluation:

- RMSE
- MAE
- R² Score

---

## Gradient Boosting

XGBoost

Purpose:

Alternative regression model for comparison against Random Forest.

---

## Model Persistence

Joblib

Purpose:

Store trained ML models for inference without retraining.

---

# AI Stack

Primary Provider

Gemini API

Optional Provider

OpenAI API

Responsibilities:

- Explain predictions
- Explain dashboard insights
- Compare districts
- Answer project-related questions

The LLM is not responsible for generating predictions or District Priority Scores.

---

# API Testing

Bruno

Responsibilities:

- Endpoint testing
- Request collections
- Version-controlled API documentation

Bruno collections should be stored inside the repository.

---

# Development Standards

## Python

- Python 3.12.x
- uv for dependency management
- Ruff for linting and formatting
- Modular project structure
- Type hints encouraged
- Docstrings for public functions

---

## Backend

- REST architecture
- JSON responses
- Business logic remains in backend
- ML inference performed only by backend

---

## Frontend

- JavaScript
- Functional React components
- React Hooks
- Reusable UI components
- Centralized API service layer

---

## Machine Learning

- Separate training and inference workflows
- Save trained models using Joblib
- Compare Random Forest and XGBoost
- Select final regression model based on evaluation metrics

---

## Git

- Feature branches
- Small commits
- Descriptive commit messages
- Push changes daily
- Synchronize frequently with the main branch

Detailed Git procedures are defined in the Git Workflow document.

---

## Documentation

Every completed feature must include:

- Documentation update
- Presentation update
- Relevant screenshots or figures (when applicable)

Documentation is developed continuously throughout the project rather than after implementation.

---

## Editor Standards

- Every team member should use the recommended development environment.
- Ruff is the single source of truth for Python linting and formatting.
- Prettier is used for frontend formatting.
- `.editorconfig` defines repository-wide editor behavior.
- Code should be formatted before every commit.

---

# Project Structure Principles

## 1. Separation of Concerns

Data processing, machine learning, backend, frontend, documentation, and presentation remain independent modules with clearly defined responsibilities.

---

## 2. Single Source of Truth

- Raw datasets remain unchanged.
- Clean datasets are generated programmatically.
- `pyproject.toml` and `uv.lock` define Python dependencies.
- `package.json` defines frontend dependencies.

---

## 3. Backend Owns Business Logic

The backend is responsible for:

- Machine learning inference
- District Priority Score generation
- Decision Engine
- AI integration
- API responses

The frontend is responsible only for presentation and user interaction.

---

## 4. LLM Assists, It Does Not Decide

The AI Assistant:

- Explains
- Summarizes
- Answers questions

The LLM does not replace machine learning models or make infrastructure planning decisions independently.

---

## 5. Reproducibility First

Any team member should be able to clone the repository and reproduce the development environment using only:

- uv
- Node.js
- npm

without manual dependency configuration.

---

## 6. Documentation Evolves with Development

Documentation and presentation materials are updated continuously during implementation.

No documentation sprint should occur at the end of the project.

---

## 7. Deployment Is the Final Enhancement

Deployment begins only after:

- Feature freeze
- Testing
- Documentation completion
- Presentation completion

Deployment must never delay implementation of core functionality.

---

# Deployment Strategy

Deployment is considered an optional enhancement for the MVP.

## Frontend

Recommended Platform:

Vercel

---

## Backend

Recommended Platform:

Render

---

## Database

SQLite

SQLite is sufficient for the MVP and academic demonstration.

Future deployments may migrate to PostgreSQL if required.

---

# Development Environment

The following Visual Studio Code extensions are recommended to ensure a consistent development experience across the team.

## Required Extensions

| Category | Extension                 | Purpose                        |
| -------- | ------------------------- | ------------------------------ |
| Python   | Python                    | Python language support        |
| Python   | Pylance                   | IntelliSense and type checking |
| Python   | Ruff                      | Linting and formatting         |
| Frontend | ESLint                    | JavaScript linting             |
| Frontend | Prettier                  | Frontend code formatting       |
| Frontend | Tailwind CSS IntelliSense | Tailwind CSS autocomplete      |

## Recommended Extensions

| Category      | Extension           | Purpose                                           |
| ------------- | ------------------- | ------------------------------------------------- |
| Git           | GitLens             | Git history, blame, and branch insights           |
| Documentation | Markdown All in One | Markdown editing and Table of Contents generation |
| Productivity  | Error Lens          | Display linting and compiler errors inline        |

---

# Technologies Not Selected

The following technologies were intentionally excluded to reduce unnecessary complexity.

| Technology | Reason                                    |
| ---------- | ----------------------------------------- |
| Docker     | Not required for project scope            |
| Redis      | No caching requirements                   |
| Celery     | No background task processing             |
| Next.js    | React + Vite is sufficient                |
| MongoDB    | Project data is relational and structured |
| Firebase   | No authentication requirements            |
| TensorFlow | Scikit-learn satisfies project needs      |
| PyTorch    | Unnecessary for the selected ML approach  |
| GraphQL    | REST APIs are simpler for the project     |
| Kubernetes | Out of scope                              |

---

# Technology Governance

This document defines the approved technology stack for EVision Telangana.

Technology changes should only be made when:

- Required by implementation constraints,
- Required to resolve compatibility issues,
- Required by the project supervisor.

Any technology that increases project complexity without directly supporting the approved project scope should not be introduced.
