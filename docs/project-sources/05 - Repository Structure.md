- [Repository Structure](#repository-structure)
- [Purpose](#purpose)
- [Relationship to Other Project Documents](#relationship-to-other-project-documents)
- [Repository Objectives](#repository-objectives)
  - [1. Clear Separation of Responsibilities](#1-clear-separation-of-responsibilities)
  - [2. Support Parallel Development](#2-support-parallel-development)
  - [3. Maintainability](#3-maintainability)
  - [4. Scalability](#4-scalability)
  - [5. Reproducibility](#5-reproducibility)
  - [6. Consistency](#6-consistency)
- [Repository Design Principles](#repository-design-principles)
  - [Single Responsibility](#single-responsibility)
  - [Modular Organization](#modular-organization)
  - [Separation of Source and Generated Artifacts](#separation-of-source-and-generated-artifacts)
  - [Source-Control Friendly Layout](#source-control-friendly-layout)
  - [Predictable Navigation](#predictable-navigation)
  - [Documentation Alongside Development](#documentation-alongside-development)
- [Complete Repository Hierarchy](#complete-repository-hierarchy)
- [Top-Level Directory Responsibilities](#top-level-directory-responsibilities)
  - [backend/](#backend)
  - [frontend/](#frontend)
  - [data/](#data)
  - [models/](#models)
  - [notebooks/](#notebooks)
  - [scripts/](#scripts)
  - [tests/](#tests)
  - [docs/](#docs)
  - [report/](#report)
  - [presentation/](#presentation)
- [Backend Repository Organization](#backend-repository-organization)
  - [api/](#api)
    - [api/routes/](#apiroutes)
    - [api/dependencies/](#apidependencies)
  - [services/](#services)
  - [repositories/](#repositories)
  - [database/](#database)
  - [schemas/](#schemas)
  - [models/](#models-1)
  - [config/](#config)
  - [utils/](#utils)
  - [logs/](#logs)
  - [main.py](#mainpy)
- [Frontend Repository Organization](#frontend-repository-organization)
  - [public/](#public)
  - [src/](#src)
  - [assets/](#assets)
  - [components/](#components)
  - [pages/](#pages)
  - [services/](#services-1)
  - [hooks/](#hooks)
  - [styles/](#styles)
  - [utils/](#utils-1)
  - [App.jsx](#appjsx)
  - [main.jsx](#mainjsx)
- [Data Repository Organization](#data-repository-organization)
  - [raw/](#raw)
  - [processed/](#processed)
  - [external/](#external)
- [Machine Learning Repository Organization](#machine-learning-repository-organization)
  - [regression.joblib](#regressionjoblib)
  - [kmeans.joblib](#kmeansjoblib)
  - [evaluation/](#evaluation)
- [Notebooks Organization](#notebooks-organization)
  - [Usage Guidelines](#usage-guidelines)
- [Scripts Organization](#scripts-organization)
  - [Responsibilities](#responsibilities)
- [Tests Organization](#tests-organization)
  - [backend/](#backend-1)
  - [api/](#api-1)
  - [integration/](#integration)
  - [utilities/](#utilities)
- [Documentation Repository Organization](#documentation-repository-organization)
  - [project-sources/](#project-sources)
  - [diagrams/](#diagrams)
  - [api/](#api-2)
  - [user-guide/](#user-guide)
  - [developer-guide/](#developer-guide)
  - [assets/](#assets-1)
- [Report Repository Organization](#report-repository-organization)
  - [figures/](#figures)
  - [tables/](#tables)
  - [references/](#references)
  - [assets/](#assets-2)
- [Presentation Repository Organization](#presentation-repository-organization)
  - [slides/](#slides)
  - [speaker-notes/](#speaker-notes)
  - [screenshots/](#screenshots)
  - [figures/](#figures-1)
  - [assets/](#assets-3)
- [Repository Configuration Files](#repository-configuration-files)
  - [pyproject.toml](#pyprojecttoml)
  - [uv.lock](#uvlock)
  - [package.json](#packagejson)
  - [.editorconfig](#editorconfig)
  - [.gitignore](#gitignore)
  - [.env.example](#envexample)
  - [README.md](#readmemd)
- [Environment Files](#environment-files)
- [Naming Conventions](#naming-conventions)
  - [Directories](#directories)
  - [Python Files](#python-files)
  - [React Components](#react-components)
  - [Data Files](#data-files)
  - [Model Files](#model-files)
- [File Placement Guidelines](#file-placement-guidelines)
- [Version-Controlled Files](#version-controlled-files)
- [Generated Files](#generated-files)
- [Repository Scalability Considerations](#repository-scalability-considerations)
- [Repository Governance](#repository-governance)
- [Conclusion](#conclusion)


# Repository Structure

**Project:** EVision Telangana  
**Official Project Title:** AI-Based EV Charging Infrastructure Planning and Decision Support System for Telangana

**Version:** 1.0  
**Status:** Frozen  
**Last Updated:** July 2026

---

# Purpose

This document defines the approved repository organization for EVision Telangana.

It specifies how the project source code, datasets, machine learning artifacts, documentation, configuration files, reports, presentation materials, and supporting resources are organized within the repository.

The repository structure serves as the implementation blueprint for organizing project assets while maintaining consistency with the approved Project Scope, Master Roadmap, Final Tech Stack, and System Architecture.

This document is the authoritative reference for repository organization throughout the project lifecycle.

---

# Relationship to Other Project Documents

The Repository Structure document complements the existing project documentation by defining how implementation assets are organized within the project repository.

| Document                                 | Purpose                                                                                       |
| ---------------------------------------- | --------------------------------------------------------------------------------------------- |
| Final Project Scope                      | Defines project objectives, datasets, deliverables, and boundaries.                           |
| Master Roadmap                           | Defines implementation phases, milestones, and development workflow.                          |
| Final Tech Stack                         | Defines approved technologies, tooling, and development standards.                            |
| System Architecture                      | Defines the architectural organization and interactions between system components.            |
| **Repository Structure (This Document)** | Defines the physical organization of all implementation assets within the project repository. |

This document does not introduce new technologies, features, datasets, or architectural decisions. It organizes the approved implementation into a maintainable repository layout.

---

# Repository Objectives

The repository organization has been designed around several primary objectives.

## 1. Clear Separation of Responsibilities

Each major project area is isolated into a dedicated directory with a single primary responsibility.

Examples include:

- Backend
- Frontend
- Data
- Machine Learning Models
- Documentation
- Testing
- Reports
- Presentation

This separation reduces coupling between project modules and simplifies navigation.

---

## 2. Support Parallel Development

The repository enables multiple team members to work simultaneously with minimal conflicts.

Data engineers, backend developers, frontend developers, and documentation contributors can each work within dedicated areas of the repository without affecting unrelated modules.

---

## 3. Maintainability

The repository favors a logical and predictable organization.

Developers should be able to locate project assets quickly without requiring extensive knowledge of the overall codebase.

Directories should remain focused on a single responsibility and avoid mixing unrelated content.

---

## 4. Scalability

Although the current implementation targets the approved MVP, the repository structure should accommodate future enhancements without requiring significant reorganization.

Examples include:

- Additional machine learning models
- New API endpoints
- Additional dashboard pages
- Expanded documentation
- Future datasets

The repository organization should remain stable as the project evolves.

---

## 5. Reproducibility

The repository is structured so that any team member can reproduce the complete development environment using only the approved tooling.

Configuration files, dependency definitions, documentation, and source code are maintained together to support consistent project setup across all development environments.

---

## 6. Consistency

Common organizational principles are applied throughout the repository.

Examples include:

- Modular directory organization
- Consistent naming conventions
- Predictable file placement
- Separation of generated and maintained artifacts

These conventions improve readability and reduce onboarding time for new contributors.

---

# Repository Design Principles

The repository follows several guiding principles.

---

## Single Responsibility

Every directory should have one clearly defined purpose.

Directories should not contain unrelated files or implementation logic.

---

## Modular Organization

Backend, frontend, data processing, machine learning, documentation, and presentation materials remain independent modules.

Each module can evolve without requiring structural changes to other parts of the repository.

---

## Separation of Source and Generated Artifacts

Files created manually should remain separate from files generated during preprocessing, model training, or application execution.

Generated artifacts should never overwrite manually maintained source files.

---

## Source-Control Friendly Layout

Frequently changing implementation files are separated from large static assets whenever possible.

This improves repository organization and reduces unnecessary merge conflicts.

---

## Predictable Navigation

Similar types of files are grouped together using consistent directory names.

Developers should be able to locate project resources without relying on undocumented conventions.

---

## Documentation Alongside Development

Documentation evolves throughout implementation rather than after feature completion.

Repository organization supports continuous documentation updates as defined in the Master Roadmap.

---

# Complete Repository Hierarchy

The following structure defines the approved repository organization for EVision Telangana.

```text
EVision-Telangana/
│
├── backend/
│
├── frontend/
│
├── data/
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
│
├── .env.example
├── .editorconfig
├── .gitignore
├── pyproject.toml
├── uv.lock
├── package.json
├── README.md
└── LICENSE (optional)
```

This hierarchy represents the top-level organization of the repository.

Subdirectory organization is defined in the following sections.

---

# Top-Level Directory Responsibilities

Each top-level directory has a clearly defined responsibility within the project.

Directories should not overlap in purpose.

---

## backend/

Purpose:

Contains the complete FastAPI application, backend business logic, Decision Engine, Machine Learning inference services, AI Assistant integration, database access layer, and application configuration.

Responsibilities include:

- REST API implementation
- Business logic
- Decision Engine
- Machine Learning inference
- AI Assistant orchestration
- Database interaction
- Configuration management
- Logging
- Utility functions

The backend serves as the only gateway between the frontend and the application's internal services.

---

## frontend/

Purpose:

Contains the complete React application responsible for user interaction and visualization.

Responsibilities include:

- Dashboard
- Maps
- Charts
- User interface
- AI Assistant interface
- API communication
- Reusable UI components

The frontend is responsible only for presentation and user interaction.

Business logic remains exclusively within the backend.

---

## data/

Purpose:

Stores all project datasets required throughout preprocessing, model training, and application execution.

Responsibilities include:

- Raw datasets
- Clean datasets
- External supporting datasets
- Generated master datasets

Raw datasets should never be modified directly.

Processed datasets are generated programmatically through the Data Processing Pipeline.

---

## models/

Purpose:

Stores serialized machine learning artifacts produced during model training.

Responsibilities include:

- Selected regression model
- K-Means clustering model
- Additional future model artifacts if required

Only trained model artifacts belong in this directory.

Training scripts remain outside this directory.

---

## notebooks/

Purpose:

Contains exploratory notebooks created during research, experimentation, and model development.

Typical uses include:

- Exploratory Data Analysis
- Feature engineering experiments
- Model experimentation
- Visualization prototypes

Notebooks should not contain production application logic.

Successful implementations should be migrated into reusable Python modules within the repository.

---

## scripts/

Purpose:

Contains executable project scripts that automate common development tasks.

Examples include:

- Data preprocessing
- Dataset validation
- Model training
- Model evaluation
- Database initialization
- Utility scripts

Scripts should perform well-defined tasks and remain independent from application runtime.

---

## tests/

Purpose:

Contains automated testing resources for the project.

Responsibilities include:

- Backend tests
- Machine learning validation tests
- API tests
- Integration tests
- Shared testing utilities

Testing resources should remain isolated from production source code.

---

## docs/

Purpose:

Stores all project documentation other than the academic report and presentation.

Examples include:

- Project Sources
- Architecture diagrams
- API documentation
- Development guides
- User guides
- Supporting figures

Documentation evolves continuously throughout development.

---

## report/

Purpose:

Contains the academic project report and supporting report assets.

Responsibilities include:

- Final report
- Figures
- Tables
- References
- Supporting images

Only report-related assets belong in this directory.

---

## presentation/

Purpose:

Stores all presentation materials prepared for project demonstration.

Responsibilities include:

- PowerPoint presentation
- Speaker notes
- Demonstration assets
- Screenshots
- Presentation figures

Presentation materials are maintained alongside project development as defined in the Master Roadmap.

---

# Backend Repository Organization

The backend follows a layered architecture consistent with the approved System Architecture.

```text
backend/
│
├── api/
│   ├── routes/
│   ├── dependencies/
│   └── __init__.py
│
├── services/
│
├── repositories/
│
├── database/
│
├── schemas/
│
├── models/
│
├── config/
│
├── utils/
│
├── logs/
│
├── main.py
└── __init__.py
```

Each directory has a single responsibility.

---

## api/

Purpose:

Contains all REST API routing logic.

Responsibilities include:

- API endpoints
- Route grouping
- Request validation
- Response serialization
- Dependency injection

The API layer should remain lightweight.

Business logic should not be implemented within route handlers.

---

### api/routes/

Contains route definitions grouped by functional area.

Typical organization may include:

- Dashboard routes
- District routes
- Prediction routes
- Analytics routes
- Recommendation routes
- AI Assistant routes

Each route module should expose related REST endpoints only.

---

### api/dependencies/

Contains reusable FastAPI dependencies shared across multiple routes.

Examples include:

- Shared validation
- Configuration dependencies
- Common request utilities

---

## services/

Purpose:

Implements application business logic.

Responsibilities include:

- Decision Engine
- Machine Learning inference
- Analytics services
- AI Assistant service
- Data aggregation
- Business workflows

Services coordinate application behavior and should remain independent of HTTP request handling.

---

## repositories/

Purpose:

Implements database access.

Responsibilities include:

- Database queries
- CRUD operations
- Data retrieval
- Data persistence

Repositories isolate database logic from higher application layers.

---

## database/

Purpose:

Contains database initialization and configuration.

Responsibilities include:

- Database connection
- SQLModel configuration
- Session management
- Database startup

Database implementation details remain isolated within this directory.

---

## schemas/

Purpose:

Defines request and response schemas.

Responsibilities include:

- Request models
- Response models
- Validation models
- Shared API schemas

Schemas define the public contract between frontend and backend.

---

## models/

Purpose:

Contains SQLModel database models.

Responsibilities include:

- Database entities
- Table definitions
- ORM models

This directory stores database models only.

Machine learning models are stored separately within the repository's top-level `models/` directory.

---

## config/

Purpose:

Centralizes backend configuration.

Responsibilities include:

- Environment loading
- Runtime configuration
- Constants
- Configuration helpers

Application configuration should never be hard-coded.

---

## utils/

Purpose:

Contains reusable helper functions shared across backend modules.

Examples include:

- Date utilities
- Formatting helpers
- Validation helpers
- General utility functions

Utilities should remain independent of business logic whenever possible.

---

## logs/

Purpose:

Stores runtime log files during local development if file-based logging is enabled.

This directory contains generated artifacts and should not be committed to version control unless explicitly required.

---

## main.py

Purpose:

Application entry point.

Responsibilities include:

- Application startup
- Configuration loading
- Route registration
- Database initialization
- Model loading
- AI service initialization

This file serves as the backend bootstrap for the FastAPI application.

---

# Frontend Repository Organization

The frontend follows a component-based architecture that separates presentation, reusable components, API communication, and application state.

```text
frontend/
│
├── public/
│
├── src/
│   ├── assets/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── hooks/
│   ├── styles/
│   ├── utils/
│   ├── App.jsx
│   └── main.jsx
│
├── package.json
└── vite.config.js
```

The frontend is responsible exclusively for user interaction and visualization.

Business logic remains within the backend.

---

## public/

Purpose:

Contains static files served directly by the frontend.

Typical contents include:

- Static images
- Icons
- Favicon
- Static assets required during application startup

Files in this directory should not require processing during the build process.

---

## src/

Purpose:

Contains the complete frontend application source code.

All React components, pages, services, styles, and utilities reside within this directory.

---

## assets/

Purpose:

Stores frontend assets used throughout the application.

Examples include:

- Images
- Logos
- SVG files
- Static graphics

Assets should remain organized and grouped by type whenever practical.

---

## components/

Purpose:

Contains reusable React components shared across multiple pages.

Typical examples include:

- Navigation bar
- Sidebar
- Dashboard cards
- Tables
- Charts
- Filter controls
- Search components
- Loading indicators
- Error messages
- Reusable map components

Components should remain presentation-focused and avoid implementing business logic.

---

## pages/

Purpose:

Contains the application's primary page-level components.

Typical pages include:

- Dashboard
- District Explorer
- Predictions
- Recommendations
- AI Assistant

Each page assembles reusable components into complete user interfaces.

---

## services/

Purpose:

Centralizes communication with the backend.

Responsibilities include:

- Axios configuration
- API request functions
- Response handling
- Error handling

No component should communicate directly with backend endpoints outside this service layer.

---

## hooks/

Purpose:

Contains reusable React Hooks shared across the application.

Examples include:

- API hooks
- Filter hooks
- Dashboard state hooks
- Reusable UI behavior

Hooks should encapsulate reusable frontend behavior while remaining independent of presentation.

---

## styles/

Purpose:

Stores global styling resources.

Typical contents include:

- Global CSS
- Tailwind entry files
- Shared styling utilities

Component-specific styling should remain close to the component whenever appropriate.

---

## utils/

Purpose:

Contains reusable frontend helper functions.

Examples include:

- Formatting utilities
- Date formatting
- Number formatting
- Common helper functions

Utilities should not duplicate backend business logic.

---

## App.jsx

Purpose:

Defines the root application component.

Responsibilities include:

- Overall application layout
- Page composition
- Global providers
- Routing integration

---

## main.jsx

Purpose:

Frontend application entry point.

Responsibilities include:

- React initialization
- Root rendering
- Global stylesheet loading

---

# Data Repository Organization

The `data/` directory stores every dataset used throughout the project lifecycle.

The directory separates immutable source datasets from generated outputs.

```text
data/
│
├── raw/
│
├── processed/
│
└── external/
```

---

## raw/

Purpose:

Stores the original official datasets.

Examples include:

- TGSPDCL EV Charging Station Consumption
- TGNPDCL EV Charging Station Consumption
- TGREDCO Charging Station Details

Files contained within this directory must remain unchanged.

Any preprocessing should generate new outputs rather than modifying the original datasets.

---

## processed/

Purpose:

Stores datasets generated by the preprocessing pipeline.

Typical contents include:

- Clean datasets
- Integrated datasets
- Feature-engineered datasets
- Master dataset
- Intermediate processing outputs

Processed files may be regenerated whenever preprocessing is executed.

The preprocessing pipeline should be deterministic so that identical raw inputs produce identical processed outputs.

---

## external/

Purpose:

Stores supporting datasets used by the application.

Examples include:

- Telangana district boundary GeoJSON
- Supporting spatial datasets

Supporting datasets remain separate from the primary historical charging datasets.

---

# Machine Learning Repository Organization

Machine learning artifacts are stored independently from source code.

```text
models/
│
├── regression.joblib
├── kmeans.joblib
└── evaluation/
```

The exact filenames may vary depending on the final implementation.

The organizational principle remains unchanged.

---

## regression.joblib

Purpose:

Stores the selected regression model after evaluation.

Only the best-performing regression model should be used during application runtime.

---

## kmeans.joblib

Purpose:

Stores the trained clustering model used for district profiling.

The clustering model supports analytics and visualization.

It is not used for prediction.

---

## evaluation/

Purpose:

Stores machine learning evaluation artifacts.

Typical contents may include:

- Evaluation summaries
- Feature importance outputs
- Model comparison results

Evaluation artifacts support documentation and analysis but are not required during application runtime.

---

# Notebooks Organization

The notebooks directory supports experimentation during development.

```text
notebooks/
│
├── exploratory_analysis.ipynb
├── feature_engineering.ipynb
├── model_experiments.ipynb
└── visualization_prototypes.ipynb
```

Notebook names are illustrative.

Actual notebook filenames should reflect their purpose.

---

## Usage Guidelines

Notebooks should be used for:

- Exploratory analysis
- Rapid experimentation
- Visualization development
- Machine learning research

Production code should not remain inside notebooks.

Reusable implementations should be migrated into the appropriate Python modules before project completion.

---

# Scripts Organization

The scripts directory contains standalone executable utilities.

```text
scripts/
│
├── preprocess_data.py
├── train_models.py
├── evaluate_models.py
├── initialize_database.py
└── utilities/
```

---

## Responsibilities

Scripts automate recurring development tasks.

Typical responsibilities include:

- Data preprocessing
- Dataset validation
- Feature engineering
- Model training
- Model evaluation
- Database initialization
- Development utilities

Scripts should remain independent from application runtime whenever possible.

---

# Tests Organization

Testing resources remain isolated from production code.

```text
tests/
│
├── backend/
├── api/
├── integration/
└── utilities/
```

---

## backend/

Contains backend-specific tests.

Examples include:

- Service tests
- Repository tests
- Decision Engine tests
- AI service tests

---

## api/

Contains REST API validation tests.

Examples include:

- Endpoint validation
- Request validation
- Response validation

Bruno collections used for API testing should also be maintained within the repository in accordance with the approved technology stack.

---

## integration/

Contains end-to-end integration tests.

Typical scenarios include:

- Backend and database integration
- Backend and machine learning integration
- Frontend and backend integration

---

## utilities/

Contains shared testing utilities used across multiple test suites.

Examples include:

- Mock data
- Shared fixtures
- Test helpers

---

# Documentation Repository Organization

Project documentation is maintained separately from implementation source code.

```text
docs/
│
├── project-sources/
├── diagrams/
├── api/
├── user-guide/
├── developer-guide/
└── assets/
```

Documentation should evolve continuously throughout development in accordance with the Master Roadmap.

---

## project-sources/

Purpose:

Stores all approved Project Source documents.

Examples include:

- Final Project Scope
- Master Roadmap
- Final Tech Stack
- System Architecture
- Repository Structure
- Git Workflow
- API Specification
- Database Schema
- Data Contracts
- Coding Standards
- ML Concepts

These documents serve as the authoritative references for project implementation.

---

## diagrams/

Purpose:

Stores architecture and design diagrams.

Examples include:

- System Architecture
- Data Flow
- Repository Structure
- Machine Learning Workflow
- Decision Engine Workflow
- Deployment Architecture

Diagram source files should be retained whenever practical to simplify future updates.

---

## api/

Purpose:

Stores generated or manually maintained API documentation.

Typical contents include:

- Endpoint documentation
- Request examples
- Response examples
- API reference material

This documentation complements the formal API Specification Project Source.

---

## user-guide/

Purpose:

Contains documentation intended for application users.

Typical topics include:

- Application overview
- Dashboard navigation
- Map usage
- AI Assistant usage
- Common workflows

---

## developer-guide/

Purpose:

Contains documentation intended for contributors.

Typical topics include:

- Development setup
- Local environment
- Build process
- Project conventions
- Troubleshooting

---

## assets/

Purpose:

Stores documentation assets.

Examples include:

- Images
- Figures
- Icons
- Screenshots
- Supporting graphics

Assets should remain organized to simplify report and presentation preparation.

---

# Report Repository Organization

The academic report is maintained independently from implementation documentation.

```text
report/
│
├── figures/
├── tables/
├── references/
├── assets/
└── report.docx (or equivalent)
```

---

## figures/

Purpose:

Stores report figures.

Examples include:

- Architecture diagrams
- Workflow diagrams
- Dashboard screenshots
- Charts
- Evaluation graphs

---

## tables/

Purpose:

Stores report tables.

Examples include:

- Dataset summaries
- Model comparison tables
- Evaluation metrics
- Experimental results

---

## references/

Purpose:

Stores bibliography resources and supporting reference material used during report preparation.

---

## assets/

Purpose:

Stores additional report resources such as logos, icons, and supporting images.

---

# Presentation Repository Organization

Presentation materials remain independent from both implementation code and report resources.

```text
presentation/
│
├── slides/
├── speaker-notes/
├── screenshots/
├── figures/
└── assets/
```

---

## slides/

Purpose:

Stores the presentation deck.

Presentation updates should occur continuously throughout development.

---

## speaker-notes/

Purpose:

Stores presenter notes used during demonstrations and project presentations.

---

## screenshots/

Purpose:

Stores application screenshots captured throughout development.

Typical examples include:

- Dashboard
- Maps
- AI Assistant
- Analytics
- Recommendation views

---

## figures/

Purpose:

Stores diagrams and illustrations used within the presentation.

---

## assets/

Purpose:

Stores logos, icons, and other reusable presentation resources.

---

# Repository Configuration Files

Several configuration files exist at the repository root.

These files define project behavior, dependency management, development standards, and repository configuration.

---

## pyproject.toml

Purpose:

Defines the Python project configuration.

Responsibilities include:

- Dependency definitions
- Project metadata
- Tool configuration

This file is the authoritative configuration for the Python environment.

---

## uv.lock

Purpose:

Stores the locked dependency versions generated by the package manager.

The lock file ensures reproducible development environments.

This file must remain under version control.

---

## package.json

Purpose:

Defines frontend dependencies and project scripts.

Responsibilities include:

- Frontend dependencies
- Development scripts
- Build scripts

This file serves as the authoritative dependency definition for the frontend.

---

## .editorconfig

Purpose:

Defines repository-wide editor behavior.

Examples include:

- Encoding
- Line endings
- Indentation
- Final newline
- Whitespace handling

Consistent editor settings reduce formatting inconsistencies across contributors.

---

## .gitignore

Purpose:

Defines files and directories excluded from version control.

Typical examples include:

- Virtual environments
- Build artifacts
- Cache files
- Runtime logs
- Environment files
- Generated temporary files

The `.gitignore` file should be maintained throughout the project lifecycle.

---

## .env.example

Purpose:

Provides a template for required environment variables.

Sensitive credentials should never be committed.

Developers should create their own local environment files based on this template.

---

## README.md

Purpose:

Serves as the primary entry point for the repository.

Typical contents include:

- Project overview
- Features
- Repository structure
- Installation instructions
- Development setup
- Running the application
- License information
- Contributors

The README should remain synchronized with project development.

---

# Environment Files

Environment configuration remains external to application source code.

Typical configuration values include:

- Gemini API key
- OpenAI API key (optional)
- Backend host
- Backend port
- Database location
- Model directory

Actual environment files should never be committed to version control.

Only `.env.example` should exist within the repository.

---

# Naming Conventions

Repository organization follows consistent naming conventions.

---

## Directories

Directory names should:

- Use lowercase letters
- Use descriptive names
- Avoid spaces
- Prefer hyphens only when necessary

Examples:

```text
backend
frontend
project-sources
developer-guide
```

---

## Python Files

Python modules should use:

```text
snake_case.py
```

Examples:

```text
train_models.py
decision_engine.py
prediction_service.py
```

---

## React Components

React component filenames should use:

```text
PascalCase.jsx
```

Examples:

```text
Dashboard.jsx
DistrictCard.jsx
MapView.jsx
RecommendationPanel.jsx
```

---

## Data Files

Dataset filenames should be descriptive and consistent.

Examples include:

```text
master_dataset.csv
processed_demand.csv
district_boundaries.geojson
```

Generated filenames should clearly distinguish processed data from raw source files.

---

## Model Files

Serialized models should use descriptive names.

Examples include:

```text
best_regression.joblib
kmeans.joblib
```

Model filenames should clearly identify their purpose.

---

# File Placement Guidelines

Every file should reside in the directory corresponding to its primary responsibility.

Examples include:

- Backend implementation belongs in `backend/`
- Frontend implementation belongs in `frontend/`
- Datasets belong in `data/`
- Trained models belong in `models/`
- Documentation belongs in `docs/`
- Presentation assets belong in `presentation/`

Files should not be duplicated across multiple directories unless required for generated outputs.

Generated artifacts should always remain separate from manually maintained source files.

---

# Version-Controlled Files

The following categories of files should normally remain under version control.

Examples include:

- Source code
- Documentation
- Configuration templates
- Dependency files
- Project Sources
- Architecture diagrams
- API documentation
- Machine learning source code
- Processing scripts
- Bruno collections
- README

Version-controlled files represent the authoritative project implementation.

---

# Generated Files

The following files are generated during development or execution.

Examples include:

- Python virtual environments
- Cache files
- Runtime logs
- Build outputs
- Temporary files
- Local environment files

Generated artifacts should generally be excluded from version control through `.gitignore`.

Model artifacts and processed datasets may be committed when they are required for reproducible application execution or project demonstration.

---

# Repository Scalability Considerations

The repository structure has been designed to accommodate future growth without requiring significant structural changes.

Potential future additions include:

- Additional machine learning models
- New datasets
- Additional backend services
- Expanded frontend pages
- New API modules
- Additional documentation
- Deployment configuration

Future enhancements should extend the existing directory organization rather than introduce parallel or duplicate structures.

Maintaining a stable repository organization improves maintainability, reduces onboarding effort, and minimizes disruption as the project evolves.

---

# Repository Governance

This document defines the approved repository organization for EVision Telangana.

All project implementation should follow the directory organization, naming conventions, and file placement guidelines defined herein.

Repository modifications should only be made when:

- Required by verified implementation constraints,
- Required to improve maintainability,
- Required to resolve compatibility issues, or
- Required by the project supervisor.

Repository changes must remain consistent with the approved Project Scope, Master Roadmap, Final Tech Stack, and System Architecture.

---

# Conclusion

The Repository Structure establishes a modular, organized, and scalable foundation for implementing EVision Telangana.

By separating backend services, frontend components, datasets, machine learning artifacts, documentation, reports, presentation materials, configuration files, and supporting resources into clearly defined directories, the repository promotes maintainability, reproducibility, and parallel team development.

The repository organization aligns with the approved software architecture and technology stack while providing a consistent framework for implementation, testing, documentation, deployment, and future project enhancements.
