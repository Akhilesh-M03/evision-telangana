- [API Specification](#api-specification)
- [Purpose](#purpose)
- [Relationship to Other Project Documents](#relationship-to-other-project-documents)
- [API Objectives](#api-objectives)
  - [1. Consistent Communication](#1-consistent-communication)
  - [2. Clear Separation of Responsibilities](#2-clear-separation-of-responsibilities)
  - [3. Predictable Integration](#3-predictable-integration)
  - [4. Maintainability](#4-maintainability)
  - [5. Scalability](#5-scalability)
  - [6. Reusability](#6-reusability)
  - [7. Consistency](#7-consistency)
- [API Design Principles](#api-design-principles)
  - [RESTful Architecture](#restful-architecture)
  - [Stateless Communication](#stateless-communication)
  - [JSON-Based Communication](#json-based-communication)
  - [Resource-Oriented Design](#resource-oriented-design)
  - [Consistent Response Structure](#consistent-response-structure)
  - [Validation First](#validation-first)
  - [Backend-Owned Business Logic](#backend-owned-business-logic)
  - [Explainable Responses](#explainable-responses)
  - [Forward Compatibility](#forward-compatibility)
- [REST Design Philosophy](#rest-design-philosophy)
- [API Versioning Strategy](#api-versioning-strategy)
- [Base URL](#base-url)
- [URL Naming Conventions](#url-naming-conventions)
  - [Principles](#principles)
- [HTTP Method Conventions](#http-method-conventions)
- [Authentication Assumptions](#authentication-assumptions)
  - [Current Authentication Model](#current-authentication-model)
  - [Future Authentication Support](#future-authentication-support)
- [Content Types](#content-types)
  - [Request Content Type](#request-content-type)
  - [Response Content Type](#response-content-type)
- [Standard Request Headers](#standard-request-headers)
- [Standard Request Format](#standard-request-format)
  - [GET Requests](#get-requests)
  - [POST Requests](#post-requests)
- [Standard Success Response Format](#standard-success-response-format)
  - [Response Fields](#response-fields)
    - [success](#success)
    - [message](#message)
    - [data](#data)
    - [metadata](#metadata)
- [Example Success Response](#example-success-response)
- [Standard Collection Response Format](#standard-collection-response-format)
- [Standard Error Response Format](#standard-error-response-format)
- [Error Response Fields](#error-response-fields)
  - [success](#success-1)
  - [message](#message-1)
  - [error.code](#errorcode)
  - [error.details](#errordetails)
- [Example Error Response](#example-error-response)
- [Metadata Format](#metadata-format)
- [Timestamp Convention](#timestamp-convention)
- [Pagination Convention](#pagination-convention)
- [Filtering Conventions](#filtering-conventions)
- [Sorting Conventions](#sorting-conventions)
- [Endpoint Categories](#endpoint-categories)
- [Dashboard API Endpoints](#dashboard-api-endpoints)
  - [Dashboard Endpoint Overview](#dashboard-endpoint-overview)
- [GET /dashboard/overview](#get-dashboardoverview)
  - [Purpose](#purpose-1)
  - [Request](#request)
  - [Query Parameters](#query-parameters)
  - [Request Body](#request-body)
  - [Successful Response](#successful-response)
  - [Response Fields](#response-fields-1)
  - [Status Codes](#status-codes)
- [GET /dashboard/map](#get-dashboardmap)
  - [Purpose](#purpose-2)
  - [Request](#request-1)
  - [Query Parameters](#query-parameters-1)
  - [Request Body](#request-body-1)
  - [Successful Response](#successful-response-1)
  - [Response Fields](#response-fields-2)
  - [Status Codes](#status-codes-1)
- [GET /dashboard/stations](#get-dashboardstations)
  - [Purpose](#purpose-3)
  - [Request](#request-2)
  - [Optional Query Parameters](#optional-query-parameters)
  - [Successful Response](#successful-response-2)
  - [Response Fields](#response-fields-3)
  - [Status Codes](#status-codes-2)
- [GET /dashboard/trends](#get-dashboardtrends)
  - [Purpose](#purpose-4)
  - [Request](#request-3)
  - [Optional Query Parameters](#optional-query-parameters-1)
  - [Successful Response](#successful-response-3)
  - [Response Fields](#response-fields-4)
  - [Status Codes](#status-codes-3)
- [GET /dashboard/summary](#get-dashboardsummary)
  - [Purpose](#purpose-5)
  - [Request](#request-4)
  - [Successful Response](#successful-response-4)
  - [Response Fields](#response-fields-5)
  - [Status Codes](#status-codes-4)
- [Dashboard Endpoint Design Notes](#dashboard-endpoint-design-notes)
- [District API Endpoints](#district-api-endpoints)
  - [District Endpoint Overview](#district-endpoint-overview)
- [GET /districts](#get-districts)
  - [Purpose](#purpose-6)
  - [Request](#request-5)
  - [Query Parameters](#query-parameters-2)
  - [Request Body](#request-body-2)
  - [Successful Response](#successful-response-5)
  - [Response Fields](#response-fields-6)
  - [Status Codes](#status-codes-5)
- [GET /districts/{district}](#get-districtsdistrict)
  - [Purpose](#purpose-7)
  - [Request](#request-6)
  - [Path Parameters](#path-parameters)
  - [Successful Response](#successful-response-6)
  - [Response Fields](#response-fields-7)
  - [Status Codes](#status-codes-6)
- [GET /districts/{district}/comparison](#get-districtsdistrictcomparison)
  - [Purpose](#purpose-8)
  - [Request](#request-7)
  - [Path Parameters](#path-parameters-1)
  - [Query Parameters](#query-parameters-3)
  - [Successful Response](#successful-response-7)
  - [Response Fields](#response-fields-8)
    - [districtA](#districta)
    - [districtB](#districtb)
  - [Status Codes](#status-codes-7)
- [GET /districts/search](#get-districtssearch)
  - [Purpose](#purpose-9)
  - [Request](#request-8)
  - [Query Parameters](#query-parameters-4)
  - [Successful Response](#successful-response-8)
  - [Response Fields](#response-fields-9)
  - [Status Codes](#status-codes-8)
- [District API Validation Rules](#district-api-validation-rules)
  - [District Name Validation](#district-name-validation)
  - [Comparison Validation](#comparison-validation)
  - [Search Validation](#search-validation)
- [District API Design Notes](#district-api-design-notes)
- [Prediction API Endpoints](#prediction-api-endpoints)
  - [Prediction Endpoint Overview](#prediction-endpoint-overview)
- [GET /predictions](#get-predictions)
  - [Purpose](#purpose-10)
  - [Request](#request-9)
  - [Optional Query Parameters](#optional-query-parameters-2)
  - [Successful Response](#successful-response-9)
  - [Response Fields](#response-fields-10)
  - [Status Codes](#status-codes-9)
- [GET /predictions/{district}](#get-predictionsdistrict)
  - [Purpose](#purpose-11)
  - [Request](#request-10)
  - [Path Parameters](#path-parameters-2)
  - [Successful Response](#successful-response-10)
  - [Response Fields](#response-fields-11)
  - [Status Codes](#status-codes-10)
- [GET /predictions/top](#get-predictionstop)
  - [Purpose](#purpose-12)
  - [Request](#request-11)
  - [Optional Query Parameters](#optional-query-parameters-3)
  - [Successful Response](#successful-response-11)
  - [Response Fields](#response-fields-12)
  - [Status Codes](#status-codes-11)
- [GET /predictions/summary](#get-predictionssummary)
  - [Purpose](#purpose-13)
  - [Request](#request-12)
  - [Successful Response](#successful-response-12)
  - [Response Fields](#response-fields-13)
  - [Status Codes](#status-codes-12)
- [Prediction API Validation Rules](#prediction-api-validation-rules)
  - [District Validation](#district-validation)
  - [Query Parameter Validation](#query-parameter-validation)
  - [Prediction Availability](#prediction-availability)
- [Prediction API Design Notes](#prediction-api-design-notes)
- [Analytics API Endpoints](#analytics-api-endpoints)
  - [Analytics Endpoint Overview](#analytics-endpoint-overview)
- [GET /analytics/clusters](#get-analyticsclusters)
  - [Purpose](#purpose-14)
  - [Request](#request-13)
  - [Query Parameters](#query-parameters-5)
  - [Successful Response](#successful-response-13)
  - [Response Fields](#response-fields-14)
  - [Status Codes](#status-codes-13)
- [GET /analytics/trends](#get-analyticstrends)
  - [Purpose](#purpose-15)
  - [Request](#request-14)
  - [Optional Query Parameters](#optional-query-parameters-4)
  - [Successful Response](#successful-response-14)
  - [Response Fields](#response-fields-15)
  - [Status Codes](#status-codes-14)
- [GET /analytics/profile/{district}](#get-analyticsprofiledistrict)
  - [Purpose](#purpose-16)
  - [Request](#request-15)
  - [Path Parameters](#path-parameters-3)
  - [Successful Response](#successful-response-15)
  - [Response Fields](#response-fields-16)
  - [Status Codes](#status-codes-15)
- [GET /analytics/statistics](#get-analyticsstatistics)
  - [Purpose](#purpose-17)
  - [Request](#request-16)
  - [Successful Response](#successful-response-16)
  - [Response Fields](#response-fields-17)
  - [Status Codes](#status-codes-16)
- [Analytics API Validation Rules](#analytics-api-validation-rules)
  - [District Validation](#district-validation-1)
  - [Query Parameter Validation](#query-parameter-validation-1)
  - [Trend Validation](#trend-validation)
- [Analytics API Design Notes](#analytics-api-design-notes)
- [Recommendation API Endpoints](#recommendation-api-endpoints)
  - [Recommendation Endpoint Overview](#recommendation-endpoint-overview)
- [GET /recommendations](#get-recommendations)
  - [Purpose](#purpose-18)
  - [Request](#request-17)
  - [Optional Query Parameters](#optional-query-parameters-5)
  - [Successful Response](#successful-response-17)
  - [Response Fields](#response-fields-18)
  - [Status Codes](#status-codes-17)
- [GET /recommendations/{district}](#get-recommendationsdistrict)
  - [Purpose](#purpose-19)
  - [Request](#request-18)
  - [Path Parameters](#path-parameters-4)
  - [Successful Response](#successful-response-18)
  - [Response Fields](#response-fields-19)
  - [Status Codes](#status-codes-18)
- [GET /recommendations/top](#get-recommendationstop)
  - [Purpose](#purpose-20)
  - [Request](#request-19)
  - [Optional Query Parameters](#optional-query-parameters-6)
  - [Successful Response](#successful-response-19)
  - [Response Fields](#response-fields-20)
  - [Status Codes](#status-codes-19)
- [GET /recommendations/summary](#get-recommendationssummary)
  - [Purpose](#purpose-21)
  - [Request](#request-20)
  - [Successful Response](#successful-response-20)
  - [Response Fields](#response-fields-21)
  - [Status Codes](#status-codes-20)
- [Recommendation API Validation Rules](#recommendation-api-validation-rules)
  - [District Validation](#district-validation-2)
  - [Query Parameter Validation](#query-parameter-validation-2)
  - [Recommendation Availability](#recommendation-availability)
- [Recommendation API Design Notes](#recommendation-api-design-notes)
- [AI Assistant API Endpoints](#ai-assistant-api-endpoints)
  - [AI Assistant Endpoint Overview](#ai-assistant-endpoint-overview)
- [POST /assistant/chat](#post-assistantchat)
  - [Purpose](#purpose-22)
  - [Request](#request-21)
  - [Request Body](#request-body-3)
  - [Request Fields](#request-fields)
  - [Successful Response](#successful-response-21)
  - [Response Fields](#response-fields-22)
  - [Status Codes](#status-codes-21)
- [POST /assistant/explain](#post-assistantexplain)
  - [Purpose](#purpose-23)
  - [Request](#request-22)
  - [Request Body](#request-body-4)
  - [Request Fields](#request-fields-1)
  - [Accepted Context Values](#accepted-context-values)
  - [Successful Response](#successful-response-22)
  - [Response Fields](#response-fields-23)
  - [Status Codes](#status-codes-22)
- [GET /assistant/suggestions](#get-assistantsuggestions)
  - [Purpose](#purpose-24)
  - [Request](#request-23)
  - [Query Parameters](#query-parameters-6)
  - [Successful Response](#successful-response-23)
  - [Response Fields](#response-fields-24)
  - [Status Codes](#status-codes-23)
- [AI Assistant Validation Rules](#ai-assistant-validation-rules)
  - [Question Validation](#question-validation)
  - [District Validation](#district-validation-3)
  - [Context Validation](#context-validation)
  - [AI Service Availability](#ai-service-availability)
- [AI Assistant Design Notes](#ai-assistant-design-notes)
- [Health API Endpoints](#health-api-endpoints)
  - [Health Endpoint Overview](#health-endpoint-overview)
- [GET /health](#get-health)
  - [Purpose](#purpose-25)
  - [Request](#request-24)
  - [Query Parameters](#query-parameters-7)
  - [Request Body](#request-body-5)
  - [Successful Response](#successful-response-24)
  - [Response Fields](#response-fields-25)
  - [Status Codes](#status-codes-24)
- [GET /health/database](#get-healthdatabase)
  - [Purpose](#purpose-26)
  - [Request](#request-25)
  - [Successful Response](#successful-response-25)
  - [Response Fields](#response-fields-26)
  - [Status Codes](#status-codes-25)
- [GET /health/models](#get-healthmodels)
  - [Purpose](#purpose-27)
  - [Request](#request-26)
  - [Successful Response](#successful-response-26)
  - [Response Fields](#response-fields-27)
  - [Status Codes](#status-codes-26)
- [GET /health/ai](#get-healthai)
  - [Purpose](#purpose-28)
  - [Request](#request-27)
  - [Successful Response](#successful-response-27)
  - [Response Fields](#response-fields-28)
  - [Status Codes](#status-codes-27)
- [Request Schema Definitions](#request-schema-definitions)
  - [ChatRequest](#chatrequest)
    - [Schema](#schema)
    - [Field Definitions](#field-definitions)
  - [ExplainRequest](#explainrequest)
    - [Schema](#schema-1)
    - [Field Definitions](#field-definitions-1)
- [Response Schema Definitions](#response-schema-definitions)
  - [SuccessResponse](#successresponse)
    - [Field Definitions](#field-definitions-2)
  - [ErrorResponse](#errorresponse)
    - [Field Definitions](#field-definitions-3)
- [Common Data Models](#common-data-models)
  - [District](#district)
  - [Prediction](#prediction)
  - [Recommendation](#recommendation)
  - [Cluster](#cluster)
  - [Charging Station](#charging-station)
  - [Trend Record](#trend-record)
  - [AI Response](#ai-response)
- [Error Model](#error-model)
  - [Standard Error Structure](#standard-error-structure)
  - [Error Fields](#error-fields)
- [Standard Error Codes](#standard-error-codes)
- [Validation Rules](#validation-rules)
  - [General Validation](#general-validation)
  - [Path Parameter Validation](#path-parameter-validation)
  - [Query Parameter Validation](#query-parameter-validation-3)
  - [JSON Validation](#json-validation)
  - [String Validation](#string-validation)
  - [Numeric Validation](#numeric-validation)
  - [District Validation](#district-validation-4)
  - [AI Request Validation](#ai-request-validation)
- [HTTP Status Code Conventions](#http-status-code-conventions)
  - [200 OK](#200-ok)
  - [400 Bad Request](#400-bad-request)
  - [404 Not Found](#404-not-found)
  - [405 Method Not Allowed](#405-method-not-allowed)
  - [422 Unprocessable Entity](#422-unprocessable-entity)
  - [500 Internal Server Error](#500-internal-server-error)
  - [503 Service Unavailable](#503-service-unavailable)
- [API Consistency Rules](#api-consistency-rules)
  - [Response Consistency](#response-consistency)
  - [Naming Consistency](#naming-consistency)
  - [Validation Consistency](#validation-consistency)
  - [Error Consistency](#error-consistency)
  - [JSON Consistency](#json-consistency)
- [Future API Extension Guidelines](#future-api-extension-guidelines)
- [API Governance](#api-governance)
- [Conclusion](#conclusion)


# API Specification

**Project:** EVision Telangana  
**Official Project Title:** AI-Based EV Charging Infrastructure Planning and Decision Support System for Telangana

**Version:** 1.0  
**Status:** Frozen  
**Last Updated:** July 2026

---

# Purpose

This document defines the approved REST API contract for EVision Telangana.

It specifies the communication interface between the frontend application and the backend services by defining endpoint organization, request and response structures, validation rules, versioning strategy, and API conventions.

The API Specification serves as the implementation contract that enables independent development of the frontend and backend while ensuring seamless integration.

This document intentionally defines **what the API exposes** rather than **how it is implemented**.

Implementation details such as database queries, service-layer logic, machine learning algorithms, and infrastructure configuration are defined in their respective project documents.

This document serves as the authoritative reference for all API-related development throughout the project lifecycle.

---

# Relationship to Other Project Documents

The API Specification complements the existing project documentation by defining the public communication contract used by the application.

| Document                              | Purpose                                                                                        |
| ------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Final Project Scope                   | Defines project objectives, datasets, deliverables, and system boundaries.                     |
| Master Roadmap                        | Defines implementation phases, milestones, and development workflow.                           |
| Final Tech Stack                      | Defines approved technologies, tooling, and development standards.                             |
| System Architecture                   | Defines the layered architecture and component interactions.                                   |
| Repository Structure                  | Defines repository organization and project layout.                                            |
| Git Workflow                          | Defines collaboration and version control practices.                                           |
| **API Specification (This Document)** | Defines REST endpoints, request and response contracts, validation rules, and API conventions. |

This document does not introduce new application functionality or alter the approved project scope.

Instead, it formalizes the communication interface that connects the frontend dashboard with the backend services.

---

# API Objectives

The REST API has been designed around several primary objectives.

## 1. Consistent Communication

Provide a standardized interface for all communication between the React frontend and the FastAPI backend.

Every endpoint follows consistent naming conventions, request formats, response structures, and error handling.

---

## 2. Clear Separation of Responsibilities

The API exposes only application capabilities.

Business logic, machine learning inference, decision support logic, database interaction, and AI orchestration remain internal backend responsibilities.

The frontend interacts only through REST endpoints.

---

## 3. Predictable Integration

A consistent API contract allows frontend and backend development to proceed independently.

Changes within backend implementation should not require frontend modifications unless the public API contract changes.

---

## 4. Maintainability

The API groups related endpoints into logical functional categories.

Each endpoint has one well-defined responsibility.

This organization simplifies maintenance and future expansion.

---

## 5. Scalability

Although the MVP remains intentionally lightweight, the API structure supports future enhancements without breaking existing clients.

Examples include:

- Additional analytics
- New dashboard views
- Advanced recommendation services
- Future authentication
- Additional machine learning capabilities

---

## 6. Reusability

The API is designed so that multiple frontend clients could consume the same services.

Future desktop, mobile, or third-party applications could interact with the backend using the same REST contract.

---

## 7. Consistency

All endpoints follow common conventions for:

- URL structure
- HTTP methods
- Request bodies
- Response bodies
- Error responses
- Validation
- Status codes

This minimizes ambiguity throughout development.

---

# API Design Principles

The API follows several guiding principles.

---

## RESTful Architecture

The backend exposes functionality using REST principles.

Resources are identified using predictable URLs.

HTTP methods communicate the intended action.

Every endpoint represents a well-defined application capability.

---

## Stateless Communication

Each request contains all information required for processing.

The server does not depend on previous requests when processing standard API operations.

Requests remain independent of one another.

---

## JSON-Based Communication

The API communicates exclusively using JSON.

Request payloads are transmitted as JSON objects.

Responses are returned using standardized JSON structures.

This ensures compatibility between frontend and backend technologies.

---

## Resource-Oriented Design

Endpoints are organized around logical application resources rather than implementation details.

Examples include:

- Dashboard
- Districts
- Predictions
- Analytics
- Recommendations
- AI Assistant
- System Health

Internal services remain hidden from API consumers.

---

## Consistent Response Structure

Every endpoint returns responses using a common structure.

Responses consistently include:

- Status information
- Requested data
- Optional metadata
- Error details when applicable

This simplifies frontend integration and reduces conditional handling.

---

## Validation First

Incoming requests are validated before reaching business logic.

Validation includes:

- Required fields
- Data types
- Accepted values
- Parameter formats

Invalid requests return informative error responses.

---

## Backend-Owned Business Logic

The API exposes application functionality without revealing implementation details.

Examples:

- Prediction endpoints return prediction results.

- Recommendation endpoints return district priorities.

- Analytics endpoints return processed analytical information.

The API never exposes internal computation methods.

---

## Explainable Responses

Where appropriate, API responses include supporting metadata that enables the frontend and AI Assistant to present meaningful explanations.

Responses should provide sufficient context without exposing internal implementation details.

---

## Forward Compatibility

The API is designed to accommodate future expansion while preserving compatibility with existing clients.

Future versions should extend the API without unnecessarily breaking existing endpoints.

---

# REST Design Philosophy

The EVision Telangana API follows a resource-oriented REST design.

Resources represent logical entities within the application rather than backend implementation modules.

Examples include:

```
/dashboard
/districts
/predictions
/analytics
/recommendations
/assistant
/health
```

Each resource groups related operations into a cohesive endpoint category.

Operations remain intuitive, predictable, and consistent across the entire API.

---

# API Versioning Strategy

The API uses URL-based versioning.

Current version:

```text
v1
```

Example base path:

```text
/api/v1/
```

Example endpoint:

```text
GET /api/v1/dashboard/overview
```

URL-based versioning provides several advantages:

- Explicit version identification
- Backward compatibility
- Independent evolution of future API versions
- Simplified client integration

Breaking API changes should only be introduced through a new major version.

Minor enhancements that remain backward compatible should continue within the current version.

---

# Base URL

During local development, the backend exposes the REST API under the following base path:

```text
http://localhost:8000/api/v1
```

Example:

```text
GET http://localhost:8000/api/v1/dashboard/overview
```

Deployment URLs may differ depending on the hosting environment.

Clients should construct all endpoint URLs relative to the configured API base URL rather than hardcoding full URLs.

---

# URL Naming Conventions

Endpoint paths follow consistent naming conventions.

## Principles

- Use lowercase letters.
- Use plural nouns for collections.
- Use hyphens only when necessary.
- Avoid verbs within resource names whenever possible.
- Keep URLs concise and descriptive.

Examples:

```text
/api/v1/dashboard/overview

/api/v1/districts

/api/v1/districts/{district}

/api/v1/predictions

/api/v1/analytics/clusters

/api/v1/recommendations

/api/v1/assistant/chat

/api/v1/health
```

Avoid endpoint names that expose implementation details.

Examples of discouraged patterns:

```text
/getPrediction

/doAnalytics

/runModel

/calculatePriority
```

Instead, expose the resulting resource rather than the underlying action.

---

# HTTP Method Conventions

The API uses standard HTTP methods consistently.

| Method | Purpose                                                |
| ------ | ------------------------------------------------------ |
| GET    | Retrieve data                                          |
| POST   | Submit data or initiate processing                     |
| PUT    | Replace an existing resource (reserved for future use) |
| PATCH  | Partially update a resource (reserved for future use)  |
| DELETE | Remove a resource (reserved for future use)            |

For the approved MVP, the API primarily uses:

- GET
- POST

because the application functions primarily as a Decision Support System rather than a full CRUD platform.

Future versions may introduce additional methods as application capabilities expand.

# Authentication Assumptions

The MVP of EVision Telangana is intended for academic demonstration and local deployment.

Accordingly, the REST API assumes a trusted environment and does not require user authentication for normal application usage.

This design minimizes unnecessary implementation complexity while remaining consistent with the approved project scope.

Future authentication mechanisms can be incorporated without requiring structural changes to the API.

---

## Current Authentication Model

For the approved MVP:

- No user registration
- No login system
- No role-based authorization
- No session management
- No refresh tokens
- No user accounts

All endpoints are considered publicly accessible within the local application environment.

---

## Future Authentication Support

The API has been designed so authentication may be introduced in future versions.

Possible future enhancements include:

- JWT Authentication
- OAuth 2.0
- API Keys
- Organization accounts
- Role-based access control

Introducing authentication should not require modification of existing endpoint structures.

Instead, authentication should be applied as an additional API layer.

---

# Content Types

All API communication uses JSON.

## Request Content Type

```http
Content-Type: application/json
```

---

## Response Content Type

```http
Content-Type: application/json
```

The API does not expose XML or other serialization formats.

---

# Standard Request Headers

Typical request headers include:

```http
Accept: application/json
Content-Type: application/json
```

Future authentication mechanisms may introduce additional headers such as:

```http
Authorization: Bearer <token>
```

This header is intentionally reserved for future expansion.

---

# Standard Request Format

Every request should follow consistent formatting rules.

## GET Requests

GET requests transmit parameters using:

- Path parameters
- Query parameters

Example:

```http
GET /api/v1/districts/Hyderabad
```

Example:

```http
GET /api/v1/predictions?year=2027
```

GET requests should not contain request bodies.

---

## POST Requests

POST requests transmit JSON payloads.

Example:

```json
{
  "district": "Hyderabad",
  "question": "Why is Hyderabad ranked highly?"
}
```

Only documented fields should be accepted.

Unexpected fields should either be ignored or rejected according to endpoint validation rules.

---

# Standard Success Response Format

Every successful API response follows the same high-level structure.

```json
{
  "success": true,
  "message": "Operation completed successfully.",
  "data": {},
  "metadata": {}
}
```

---

## Response Fields

### success

Boolean value indicating whether the request completed successfully.

Example:

```json
true
```

---

### message

Human-readable summary of the request result.

Example:

```json
"District data retrieved successfully."
```

---

### data

Contains the requested resource.

The structure depends on the endpoint.

Examples include:

- Dashboard statistics
- District information
- Prediction results
- Recommendations
- Analytics
- AI responses

---

### metadata

Contains optional supplementary information.

Typical metadata may include:

- Timestamp
- API version
- Record count
- Processing duration

Metadata is optional but should follow a consistent structure whenever included.

---

# Example Success Response

```json
{
  "success": true,
  "message": "Prediction generated successfully.",
  "data": {
    "district": "Hyderabad",
    "predictedDemand": 14253.7
  },
  "metadata": {
    "apiVersion": "v1"
  }
}
```

---

# Standard Collection Response Format

Endpoints returning collections follow the same structure.

Example:

```json
{
  "success": true,
  "message": "Districts retrieved successfully.",
  "data": [
    {
      "district": "Hyderabad"
    },
    {
      "district": "Warangal"
    }
  ],
  "metadata": {
    "count": 33
  }
}
```

---

# Standard Error Response Format

All errors use a standardized response structure.

```json
{
  "success": false,
  "message": "Validation failed.",
  "error": {
    "code": "VALIDATION_ERROR",
    "details": []
  }
}
```

---

# Error Response Fields

## success

Always:

```json
false
```

---

## message

High-level description suitable for frontend display.

Examples:

```text
Validation failed.

District not found.

Prediction unavailable.

Internal server error.
```

---

## error.code

Machine-readable error identifier.

Examples include:

```text
VALIDATION_ERROR

RESOURCE_NOT_FOUND

INVALID_PARAMETER

PREDICTION_FAILED

AI_SERVICE_ERROR

INTERNAL_SERVER_ERROR
```

---

## error.details

Contains additional validation or diagnostic information.

Example:

```json
[
  {
    "field": "district",
    "issue": "District name is required."
  }
]
```

The structure may vary depending on the error category.

---

# Example Error Response

```json
{
  "success": false,
  "message": "District not found.",
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "details": [
      {
        "field": "district",
        "issue": "Specified district does not exist."
      }
    ]
  }
}
```

---

# Metadata Format

Metadata provides supplementary information that is not part of the requested resource.

Typical metadata fields include:

| Field          | Description                  |
| -------------- | ---------------------------- |
| apiVersion     | Current API version          |
| timestamp      | Response generation time     |
| count          | Number of returned records   |
| processingTime | Request processing duration  |
| generatedAt    | Dataset generation timestamp |

Metadata remains optional.

Endpoints should include only metadata relevant to the requested operation.

---

# Timestamp Convention

Whenever timestamps are returned, they should use ISO 8601 format.

Example:

```text
2026-07-11T15:30:00Z
```

Using a standardized timestamp format simplifies frontend parsing and future integrations.

---

# Pagination Convention

Most MVP endpoints return relatively small datasets and therefore do not require pagination.

However, the API reserves a consistent pagination format for future expansion.

Typical query parameters include:

```text
?page=1

&pageSize=20
```

Example:

```text
GET /api/v1/districts?page=1&pageSize=20
```

Paginated responses should include metadata similar to:

```json
{
  "page": 1,
  "pageSize": 20,
  "totalRecords": 33,
  "totalPages": 2
}
```

Current MVP endpoints are expected to return complete datasets without pagination unless future scalability requirements dictate otherwise.

---

# Filtering Conventions

Filtering is performed using query parameters.

Example:

```text
GET /api/v1/districts?cluster=2
```

Example:

```text
GET /api/v1/recommendations?priority=High
```

Multiple filters may be combined.

Example:

```text
GET /api/v1/analytics/trends?district=Hyderabad&year=2026
```

Filtering should remain deterministic.

Identical requests should produce identical responses.

---

# Sorting Conventions

Sorting is also expressed using query parameters.

Reserved parameters include:

```text
sortBy

sortOrder
```

Example:

```text
GET /api/v1/recommendations?sortBy=priorityScore&sortOrder=desc
```

Accepted sort orders:

```text
asc

desc
```

If no sorting is specified, each endpoint should return data using its documented default ordering.

---

# Endpoint Categories

The EVision Telangana API organizes endpoints into logical functional groups.

The approved endpoint categories are:

| Category        | Purpose                                     |
| --------------- | ------------------------------------------- |
| Dashboard       | Dashboard summaries and overview statistics |
| Districts       | District information and comparisons        |
| Predictions     | Future charging demand predictions          |
| Analytics       | Clustering, trends, and analytical insights |
| Recommendations | District Priority Score and ranking         |
| AI Assistant    | Natural language interaction                |
| Health          | System status and service availability      |

Each category is described in the following sections of this specification.

---

# Dashboard API Endpoints

The Dashboard API provides high-level information displayed on the application's main dashboard.

These endpoints aggregate processed data from multiple backend services and present summary information suitable for visualization.

The Dashboard API does not expose implementation details or perform business logic within the API layer.

---

## Dashboard Endpoint Overview

| Method | Endpoint              | Purpose                                  |
| ------ | --------------------- | ---------------------------------------- |
| GET    | `/dashboard/overview` | Retrieve dashboard summary statistics    |
| GET    | `/dashboard/map`      | Retrieve district map visualization data |
| GET    | `/dashboard/stations` | Retrieve charging station information    |
| GET    | `/dashboard/trends`   | Retrieve historical demand trends        |
| GET    | `/dashboard/summary`  | Retrieve overall dashboard summary       |

---

# GET /dashboard/overview

## Purpose

Returns the primary dashboard statistics displayed on the application's home page.

This endpoint provides aggregated information that summarizes the current state of the available datasets.

---

## Request

```http
GET /api/v1/dashboard/overview
```

---

## Query Parameters

None.

---

## Request Body

None.

---

## Successful Response

```json
{
  "success": true,
  "message": "Dashboard overview retrieved successfully.",
  "data": {
    "districtCount": 33,
    "chargingStationCount": 412,
    "historicalRecords": 1248,
    "latestReportingMonth": "2026-06"
  },
  "metadata": {
    "apiVersion": "v1"
  }
}
```

---

## Response Fields

| Field                | Description                                |
| -------------------- | ------------------------------------------ |
| districtCount        | Total number of districts                  |
| chargingStationCount | Total charging stations available          |
| historicalRecords    | Historical observations used by the system |
| latestReportingMonth | Most recent reporting period               |

---

## Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 500  | Internal Server Error |

---

# GET /dashboard/map

## Purpose

Returns geographic information required for rendering the Telangana district map.

The response supplies visualization data only.

The frontend is responsible for rendering the map.

---

## Request

```http
GET /api/v1/dashboard/map
```

---

## Query Parameters

None.

---

## Request Body

None.

---

## Successful Response

```json
{
  "success": true,
  "message": "Map data retrieved successfully.",
  "data": [
    {
      "district": "Hyderabad",
      "priorityScore": 92.4,
      "cluster": 2
    },
    {
      "district": "Warangal",
      "priorityScore": 78.6,
      "cluster": 1
    }
  ]
}
```

---

## Response Fields

| Field         | Description                 |
| ------------- | --------------------------- |
| district      | District name               |
| priorityScore | District Priority Score     |
| cluster       | Assigned analytical cluster |

---

## Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 500  | Internal Server Error |

---

# GET /dashboard/stations

## Purpose

Returns charging station information required for dashboard visualization.

The endpoint exposes station metadata suitable for displaying markers on the interactive map.

---

## Request

```http
GET /api/v1/dashboard/stations
```

---

## Optional Query Parameters

| Parameter | Type   | Description        |
| --------- | ------ | ------------------ |
| district  | string | Filter by district |

---

## Successful Response

```json
{
  "success": true,
  "message": "Charging stations retrieved successfully.",
  "data": [
    {
      "stationName": "EV Charging Station A",
      "district": "Hyderabad",
      "latitude": 17.385,
      "longitude": 78.486,
      "organization": "TGREDCO"
    }
  ]
}
```

---

## Response Fields

| Field        | Description                       |
| ------------ | --------------------------------- |
| stationName  | Charging station name             |
| district     | District where station is located |
| latitude     | Geographic latitude               |
| longitude    | Geographic longitude              |
| organization | Station owner/operator            |

---

## Status Codes

| Code | Meaning                 |
| ---- | ----------------------- |
| 200  | Success                 |
| 400  | Invalid Query Parameter |
| 500  | Internal Server Error   |

---

# GET /dashboard/trends

## Purpose

Returns historical charging demand information for dashboard charts.

This endpoint supports trend visualizations without exposing raw datasets.

---

## Request

```http
GET /api/v1/dashboard/trends
```

---

## Optional Query Parameters

| Parameter | Type    | Description              |
| --------- | ------- | ------------------------ |
| district  | string  | Filter by district       |
| year      | integer | Filter by reporting year |

---

## Successful Response

```json
{
  "success": true,
  "message": "Trend data retrieved successfully.",
  "data": [
    {
      "month": "2026-01",
      "demand": 10342.5
    },
    {
      "month": "2026-02",
      "demand": 10891.7
    }
  ]
}
```

---

## Response Fields

| Field  | Description                |
| ------ | -------------------------- |
| month  | Reporting month            |
| demand | Historical charging demand |

---

## Status Codes

| Code | Meaning                 |
| ---- | ----------------------- |
| 200  | Success                 |
| 400  | Invalid Query Parameter |
| 500  | Internal Server Error   |

---

# GET /dashboard/summary

## Purpose

Returns aggregated dashboard information suitable for executive summaries.

This endpoint combines multiple analytical outputs into a concise overview.

---

## Request

```http
GET /api/v1/dashboard/summary
```

---

## Successful Response

```json
{
  "success": true,
  "message": "Dashboard summary retrieved successfully.",
  "data": {
    "highestPriorityDistrict": "Hyderabad",
    "highestPredictedDemand": 14253.7,
    "clusterCount": 3,
    "recommendationCount": 33
  }
}
```

---

## Response Fields

| Field                   | Description                        |
| ----------------------- | ---------------------------------- |
| highestPriorityDistrict | Highest-ranked district            |
| highestPredictedDemand  | Maximum predicted demand           |
| clusterCount            | Number of analytical clusters      |
| recommendationCount     | Number of district recommendations |

---

## Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 500  | Internal Server Error |

---

# Dashboard Endpoint Design Notes

The Dashboard API is intended to support the application's landing page.

Endpoints should:

- Return aggregated information only.
- Remain lightweight.
- Minimize frontend processing.
- Use consistent response structures.
- Avoid exposing implementation details.

The frontend remains responsible for:

- Charts
- Maps
- Tables
- Cards
- Visual formatting

The backend remains responsible for:

- Data aggregation
- Business logic
- Decision support
- Machine learning inference
- Response generation

---

# District API Endpoints

The District API provides detailed information about Telangana districts used throughout the dashboard, analytics, prediction, recommendation, and AI Assistant modules.

These endpoints allow the frontend to retrieve district-specific information without exposing internal database structures or implementation details.

The District API represents the primary source of district-level information within the application.

---

## District Endpoint Overview

| Method | Endpoint                           | Purpose                                |
| ------ | ---------------------------------- | -------------------------------------- |
| GET    | `/districts`                       | Retrieve all districts                 |
| GET    | `/districts/{district}`            | Retrieve detailed district information |
| GET    | `/districts/{district}/comparison` | Compare one district with another      |
| GET    | `/districts/search`                | Search districts                       |

---

# GET /districts

## Purpose

Returns the complete list of districts available within the application.

This endpoint supports:

- Dropdown selections
- Filters
- Search suggestions
- Dashboard navigation

---

## Request

```http
GET /api/v1/districts
```

---

## Query Parameters

None.

---

## Request Body

None.

---

## Successful Response

```json
{
  "success": true,
  "message": "Districts retrieved successfully.",
  "data": [
    {
      "district": "Adilabad"
    },
    {
      "district": "Hyderabad"
    },
    {
      "district": "Warangal"
    }
  ],
  "metadata": {
    "count": 33
  }
}
```

---

## Response Fields

| Field    | Description            |
| -------- | ---------------------- |
| district | Official district name |

---

## Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 500  | Internal Server Error |

---

# GET /districts/{district}

## Purpose

Returns complete information for a single district.

This endpoint supplies the detailed information required by the District Details page.

---

## Request

```http
GET /api/v1/districts/Hyderabad
```

---

## Path Parameters

| Parameter | Type   | Description            |
| --------- | ------ | ---------------------- |
| district  | string | Official district name |

---

## Successful Response

```json
{
  "success": true,
  "message": "District information retrieved successfully.",
  "data": {
    "district": "Hyderabad",
    "cluster": 2,
    "chargingStations": 54,
    "predictedDemand": 14253.7,
    "priorityScore": 92.4
  }
}
```

---

## Response Fields

| Field            | Description                 |
| ---------------- | --------------------------- |
| district         | District name               |
| cluster          | Assigned analytical cluster |
| chargingStations | Existing charging stations  |
| predictedDemand  | Forecasted charging demand  |
| priorityScore    | District Priority Score     |

---

## Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 404  | District Not Found    |
| 500  | Internal Server Error |

---

# GET /districts/{district}/comparison

## Purpose

Compares two districts using the application's analytical outputs.

The comparison is intended to support dashboard visualization and AI explanations.

---

## Request

```http
GET /api/v1/districts/Hyderabad/comparison?compareWith=Warangal
```

---

## Path Parameters

| Parameter | Type   | Description      |
| --------- | ------ | ---------------- |
| district  | string | Primary district |

---

## Query Parameters

| Parameter   | Type   | Description                 |
| ----------- | ------ | --------------------------- |
| compareWith | string | District to compare against |

---

## Successful Response

```json
{
  "success": true,
  "message": "District comparison generated successfully.",
  "data": {
    "districtA": {
      "name": "Hyderabad",
      "priorityScore": 92.4,
      "predictedDemand": 14253.7,
      "cluster": 2
    },
    "districtB": {
      "name": "Warangal",
      "priorityScore": 78.6,
      "predictedDemand": 10418.3,
      "cluster": 1
    }
  }
}
```

---

## Response Fields

### districtA

Information for the requested district.

### districtB

Information for the comparison district.

---

## Status Codes

| Code | Meaning                    |
| ---- | -------------------------- |
| 200  | Success                    |
| 400  | Invalid District Parameter |
| 404  | District Not Found         |
| 500  | Internal Server Error      |

---

# GET /districts/search

## Purpose

Searches districts using partial text matching.

This endpoint supports:

- Search bar autocomplete
- Dashboard filtering
- AI Assistant suggestions

---

## Request

```http
GET /api/v1/districts/search?q=Hyd
```

---

## Query Parameters

| Parameter | Type   | Description |
| --------- | ------ | ----------- |
| q         | string | Search text |

---

## Successful Response

```json
{
  "success": true,
  "message": "Search completed successfully.",
  "data": [
    {
      "district": "Hyderabad"
    }
  ]
}
```

---

## Response Fields

| Field    | Description            |
| -------- | ---------------------- |
| district | Matching district name |

---

## Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 400  | Invalid Search Query  |
| 500  | Internal Server Error |

---

# District API Validation Rules

The District API applies the following validation rules before processing requests.

---

## District Name Validation

District names must:

- Be provided when required.
- Match one of the official Telangana districts contained within the processed dataset.
- Be treated as case-insensitive during lookup.
- Be normalized before backend processing.

Requests containing unknown district names should return:

```http
404 Not Found
```

---

## Comparison Validation

District comparison requests must satisfy the following conditions:

- Both districts must exist.
- The comparison district must be specified.
- A district may be compared with itself, although no special analytical interpretation is implied.

---

## Search Validation

Search requests should:

- Ignore leading and trailing whitespace.
- Support partial matching.
- Return an empty collection when no matches exist.
- Never return duplicate district names.

---

# District API Design Notes

The District API serves as the authoritative source for district-level information throughout the application.

These endpoints intentionally expose only processed, presentation-ready information.

They do not expose:

- Raw datasets
- Internal database identifiers
- Machine learning features
- Decision Engine calculations
- Intermediate analytical artifacts

The backend remains responsible for aggregating and preparing all district information before returning standardized API responses.

---

# Prediction API Endpoints

The Prediction API provides forecasted EV charging demand generated by the Machine Learning Engine.

These endpoints expose prediction results only.

They do not expose machine learning implementation details, feature engineering logic, model internals, evaluation metrics, or training artifacts.

Prediction results are generated by the backend using the selected regression model approved during model evaluation.

---

## Prediction Endpoint Overview

| Method | Endpoint                  | Purpose                                              |
| ------ | ------------------------- | ---------------------------------------------------- |
| GET    | `/predictions`            | Retrieve predictions for all districts               |
| GET    | `/predictions/{district}` | Retrieve prediction for a specific district          |
| GET    | `/predictions/top`        | Retrieve districts with the highest predicted demand |
| GET    | `/predictions/summary`    | Retrieve prediction summary statistics               |

---

# GET /predictions

## Purpose

Returns predicted EV charging demand for every district.

This endpoint supports:

- Dashboard prediction tables
- District ranking
- Recommendation generation
- Analytics visualizations

---

## Request

```http
GET /api/v1/predictions
```

---

## Optional Query Parameters

| Parameter | Type    | Description                      |
| --------- | ------- | -------------------------------- |
| year      | integer | Forecast year (future extension) |

For the MVP, predictions correspond to the approved forecasting horizon.

---

## Successful Response

```json
{
  "success": true,
  "message": "Predictions retrieved successfully.",
  "data": [
    {
      "district": "Hyderabad",
      "predictedDemand": 14253.7
    },
    {
      "district": "Warangal",
      "predictedDemand": 10418.3
    }
  ]
}
```

---

## Response Fields

| Field           | Description                |
| --------------- | -------------------------- |
| district        | District name              |
| predictedDemand | Forecasted charging demand |

---

## Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 500  | Internal Server Error |

---

# GET /predictions/{district}

## Purpose

Returns the predicted charging demand for a single district.

This endpoint supports the District Details page, comparison views, recommendation pages, and AI Assistant context generation.

---

## Request

```http
GET /api/v1/predictions/Hyderabad
```

---

## Path Parameters

| Parameter | Type   | Description            |
| --------- | ------ | ---------------------- |
| district  | string | Official district name |

---

## Successful Response

```json
{
  "success": true,
  "message": "Prediction retrieved successfully.",
  "data": {
    "district": "Hyderabad",
    "predictedDemand": 14253.7
  }
}
```

---

## Response Fields

| Field           | Description                |
| --------------- | -------------------------- |
| district        | District name              |
| predictedDemand | Forecasted charging demand |

---

## Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 404  | District Not Found    |
| 500  | Internal Server Error |

---

# GET /predictions/top

## Purpose

Returns the highest predicted demand districts.

This endpoint supports leaderboard-style dashboard widgets and executive summaries.

---

## Request

```http
GET /api/v1/predictions/top
```

---

## Optional Query Parameters

| Parameter | Type    | Description                           |
| --------- | ------- | ------------------------------------- |
| limit     | integer | Maximum number of districts to return |

---

## Successful Response

```json
{
  "success": true,
  "message": "Top predictions retrieved successfully.",
  "data": [
    {
      "district": "Hyderabad",
      "predictedDemand": 14253.7
    },
    {
      "district": "Warangal",
      "predictedDemand": 10418.3
    },
    {
      "district": "Karimnagar",
      "predictedDemand": 9765.4
    }
  ]
}
```

---

## Response Fields

| Field           | Description                |
| --------------- | -------------------------- |
| district        | District name              |
| predictedDemand | Forecasted charging demand |

---

## Status Codes

| Code | Meaning                 |
| ---- | ----------------------- |
| 200  | Success                 |
| 400  | Invalid Query Parameter |
| 500  | Internal Server Error   |

---

# GET /predictions/summary

## Purpose

Returns aggregated prediction statistics for the complete dataset.

This endpoint provides high-level analytical information rather than individual district predictions.

---

## Request

```http
GET /api/v1/predictions/summary
```

---

## Successful Response

```json
{
  "success": true,
  "message": "Prediction summary retrieved successfully.",
  "data": {
    "highestPrediction": 14253.7,
    "lowestPrediction": 3812.4,
    "averagePrediction": 8127.6,
    "districtCount": 33
  }
}
```

---

## Response Fields

| Field             | Description                   |
| ----------------- | ----------------------------- |
| highestPrediction | Maximum predicted demand      |
| lowestPrediction  | Minimum predicted demand      |
| averagePrediction | Mean predicted demand         |
| districtCount     | Number of predicted districts |

---

## Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 500  | Internal Server Error |

---

# Prediction API Validation Rules

The Prediction API validates all incoming requests before model inference.

---

## District Validation

Prediction requests requiring a district must satisfy the following conditions:

- District name must be provided.
- District must exist within the processed dataset.
- District names are treated as case-insensitive.
- District names should be normalized before prediction.

Unknown districts should return:

```http
404 Not Found
```

---

## Query Parameter Validation

If query parameters are supplied:

- Numeric values must be valid integers where applicable.
- Unsupported parameters should be ignored or rejected according to API validation policy.
- Parameter values must remain within documented limits.

---

## Prediction Availability

Prediction endpoints assume that the trained regression model has already been loaded during backend startup.

If prediction services are temporarily unavailable, the API should return:

```http
503 Service Unavailable
```

rather than exposing internal implementation details.

---

# Prediction API Design Notes

The Prediction API exposes only the outputs produced by the Machine Learning Engine.

The API intentionally does not expose:

- Feature engineering variables
- Training datasets
- Evaluation metrics
- Model hyperparameters
- Feature importance
- Regression algorithm selection
- Serialized model artifacts

Those implementation details belong to the Machine Learning Engine and remain internal to the backend.

Prediction endpoints return only finalized prediction results that are intended for dashboard visualization, recommendation generation, and AI-assisted explanation.

---

# Analytics API Endpoints

The Analytics API provides descriptive insights generated by the Analytics Engine.

These endpoints expose processed analytical information that supports dashboard visualizations, district profiling, and exploratory analysis.

Unlike the Prediction API, Analytics endpoints do not forecast future demand.

Instead, they summarize and interpret historical and processed data.

---

## Analytics Endpoint Overview

| Method | Endpoint                        | Purpose                                |
| ------ | ------------------------------- | -------------------------------------- |
| GET    | `/analytics/clusters`           | Retrieve district clustering results   |
| GET    | `/analytics/trends`             | Retrieve historical demand trends      |
| GET    | `/analytics/profile/{district}` | Retrieve district analytical profile   |
| GET    | `/analytics/statistics`         | Retrieve analytical summary statistics |

---

# GET /analytics/clusters

## Purpose

Returns the cluster assignment for every district.

Cluster information supports:

- Dashboard visualization
- District grouping
- Comparative analysis
- AI explanations

Cluster assignments are generated by the approved K-Means clustering model.

---

## Request

```http
GET /api/v1/analytics/clusters
```

---

## Query Parameters

None.

---

## Successful Response

```json
{
  "success": true,
  "message": "Cluster information retrieved successfully.",
  "data": [
    {
      "district": "Hyderabad",
      "cluster": 2
    },
    {
      "district": "Warangal",
      "cluster": 1
    }
  ]
}
```

---

## Response Fields

| Field    | Description                 |
| -------- | --------------------------- |
| district | District name               |
| cluster  | Assigned cluster identifier |

---

## Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 500  | Internal Server Error |

---

# GET /analytics/trends

## Purpose

Returns historical charging demand trends.

This endpoint provides processed time-series information for dashboard charts and analytical reports.

---

## Request

```http
GET /api/v1/analytics/trends
```

---

## Optional Query Parameters

| Parameter | Type    | Description              |
| --------- | ------- | ------------------------ |
| district  | string  | Filter by district       |
| year      | integer | Filter by reporting year |

---

## Successful Response

```json
{
  "success": true,
  "message": "Trend analysis retrieved successfully.",
  "data": [
    {
      "month": "2026-01",
      "demand": 10342.5
    },
    {
      "month": "2026-02",
      "demand": 10891.7
    },
    {
      "month": "2026-03",
      "demand": 11246.2
    }
  ]
}
```

---

## Response Fields

| Field  | Description                |
| ------ | -------------------------- |
| month  | Reporting period           |
| demand | Historical charging demand |

---

## Status Codes

| Code | Meaning                 |
| ---- | ----------------------- |
| 200  | Success                 |
| 400  | Invalid Query Parameter |
| 500  | Internal Server Error   |

---

# GET /analytics/profile/{district}

## Purpose

Returns an analytical profile for a specific district.

The profile combines descriptive analytical information prepared by the Analytics Engine.

It is intended for:

- District Details page
- Recommendation explanations
- AI Assistant context
- Comparative dashboard views

---

## Request

```http
GET /api/v1/analytics/profile/Hyderabad
```

---

## Path Parameters

| Parameter | Type   | Description            |
| --------- | ------ | ---------------------- |
| district  | string | Official district name |

---

## Successful Response

```json
{
  "success": true,
  "message": "District profile retrieved successfully.",
  "data": {
    "district": "Hyderabad",
    "cluster": 2,
    "historicalAverageDemand": 11842.6,
    "chargingStations": 54,
    "trend": "Increasing"
  }
}
```

---

## Response Fields

| Field                   | Description                     |
| ----------------------- | ------------------------------- |
| district                | District name                   |
| cluster                 | Assigned cluster                |
| historicalAverageDemand | Average historical demand       |
| chargingStations        | Existing charging station count |
| trend                   | Overall historical demand trend |

---

## Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 404  | District Not Found    |
| 500  | Internal Server Error |

---

# GET /analytics/statistics

## Purpose

Returns high-level analytical statistics summarizing the processed dataset.

This endpoint supports executive summaries and dashboard overview cards.

---

## Request

```http
GET /api/v1/analytics/statistics
```

---

## Successful Response

```json
{
  "success": true,
  "message": "Analytical statistics retrieved successfully.",
  "data": {
    "districtCount": 33,
    "clusterCount": 3,
    "averageDemand": 8127.6,
    "highestHistoricalDemand": 13841.9,
    "lowestHistoricalDemand": 3526.4
  }
}
```

---

## Response Fields

| Field                   | Description                        |
| ----------------------- | ---------------------------------- |
| districtCount           | Number of districts                |
| clusterCount            | Number of analytical clusters      |
| averageDemand           | Mean historical charging demand    |
| highestHistoricalDemand | Maximum observed historical demand |
| lowestHistoricalDemand  | Minimum observed historical demand |

---

## Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 500  | Internal Server Error |

---

# Analytics API Validation Rules

The Analytics API validates all requests before analytical data is returned.

---

## District Validation

Endpoints requiring a district name must satisfy the following conditions:

- District name must be supplied.
- District must exist within the processed dataset.
- District lookup should be case-insensitive.
- Invalid district names should return:

```http
404 Not Found
```

---

## Query Parameter Validation

Where query parameters are supported:

- Parameters must conform to documented data types.
- Invalid numeric values should return:

```http
400 Bad Request
```

- Unsupported parameters should not alter analytical results.

---

## Trend Validation

Trend requests should return only processed historical information available within the approved datasets.

If no matching records exist, the endpoint should return an empty collection rather than an internal error.

---

# Analytics API Design Notes

The Analytics API exposes descriptive insights only.

It intentionally does not expose:

- Machine learning models
- Prediction algorithms
- Decision Engine calculations
- Raw datasets
- Intermediate feature engineering outputs
- Internal statistical computations

Analytics endpoints return processed information prepared by the Analytics Engine and intended for visualization, interpretation, and explanation.

Cluster identifiers should be treated as analytical group labels only.

They should not be interpreted as rankings or recommendation levels.

---

# Recommendation API Endpoints

The Recommendation API provides district prioritization results generated by the Decision Engine.

These endpoints expose recommendation outputs intended to support infrastructure planning and decision-making.

Recommendations are derived from processed analytical information and machine learning predictions.

The API returns only finalized recommendation results and does not expose the internal computation of the District Priority Score.

---

## Recommendation Endpoint Overview

| Method | Endpoint                      | Purpose                                         |
| ------ | ----------------------------- | ----------------------------------------------- |
| GET    | `/recommendations`            | Retrieve recommendations for all districts      |
| GET    | `/recommendations/{district}` | Retrieve recommendation for a specific district |
| GET    | `/recommendations/top`        | Retrieve highest-priority districts             |
| GET    | `/recommendations/summary`    | Retrieve recommendation summary statistics      |

---

# GET /recommendations

## Purpose

Returns recommendation information for every district.

This endpoint provides the primary output of the Decision Engine.

It supports:

- Recommendation dashboard
- District ranking
- Executive summaries
- AI Assistant explanations

---

## Request

```http
GET /api/v1/recommendations
```

---

## Optional Query Parameters

| Parameter | Type    | Description                    |
| --------- | ------- | ------------------------------ |
| priority  | string  | Filter by recommendation level |
| limit     | integer | Limit returned districts       |

---

## Successful Response

```json
{
  "success": true,
  "message": "Recommendations retrieved successfully.",
  "data": [
    {
      "district": "Hyderabad",
      "priorityScore": 92.4,
      "priorityLevel": "High"
    },
    {
      "district": "Warangal",
      "priorityScore": 78.6,
      "priorityLevel": "Medium"
    }
  ]
}
```

---

## Response Fields

| Field         | Description             |
| ------------- | ----------------------- |
| district      | District name           |
| priorityScore | District Priority Score |
| priorityLevel | Recommendation category |

---

## Status Codes

| Code | Meaning                 |
| ---- | ----------------------- |
| 200  | Success                 |
| 400  | Invalid Query Parameter |
| 500  | Internal Server Error   |

---

# GET /recommendations/{district}

## Purpose

Returns the recommendation generated for a specific district.

The endpoint combines the finalized outputs of the Machine Learning Engine and Decision Engine into a presentation-ready recommendation.

---

## Request

```http
GET /api/v1/recommendations/Hyderabad
```

---

## Path Parameters

| Parameter | Type   | Description            |
| --------- | ------ | ---------------------- |
| district  | string | Official district name |

---

## Successful Response

```json
{
  "success": true,
  "message": "Recommendation retrieved successfully.",
  "data": {
    "district": "Hyderabad",
    "priorityScore": 92.4,
    "priorityLevel": "High",
    "predictedDemand": 14253.7,
    "chargingStations": 54
  }
}
```

---

## Response Fields

| Field            | Description                     |
| ---------------- | ------------------------------- |
| district         | District name                   |
| priorityScore    | District Priority Score         |
| priorityLevel    | Recommendation category         |
| predictedDemand  | Forecasted charging demand      |
| chargingStations | Existing charging station count |

---

## Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 404  | District Not Found    |
| 500  | Internal Server Error |

---

# GET /recommendations/top

## Purpose

Returns the highest-ranked districts according to the Decision Engine.

This endpoint supports:

- Top recommendations
- Dashboard leaderboards
- Executive summaries
- Presentation views

---

## Request

```http
GET /api/v1/recommendations/top
```

---

## Optional Query Parameters

| Parameter | Type    | Description                          |
| --------- | ------- | ------------------------------------ |
| limit     | integer | Maximum number of returned districts |

---

## Successful Response

```json
{
  "success": true,
  "message": "Top recommendations retrieved successfully.",
  "data": [
    {
      "district": "Hyderabad",
      "priorityScore": 92.4
    },
    {
      "district": "Warangal",
      "priorityScore": 78.6
    },
    {
      "district": "Karimnagar",
      "priorityScore": 75.1
    }
  ]
}
```

---

## Response Fields

| Field         | Description             |
| ------------- | ----------------------- |
| district      | District name           |
| priorityScore | District Priority Score |

---

## Status Codes

| Code | Meaning                 |
| ---- | ----------------------- |
| 200  | Success                 |
| 400  | Invalid Query Parameter |
| 500  | Internal Server Error   |

---

# GET /recommendations/summary

## Purpose

Returns aggregated recommendation statistics for the complete dataset.

This endpoint provides high-level decision-support information for dashboard summary cards and executive reports.

---

## Request

```http
GET /api/v1/recommendations/summary
```

---

## Successful Response

```json
{
  "success": true,
  "message": "Recommendation summary retrieved successfully.",
  "data": {
    "districtCount": 33,
    "highestPriorityScore": 92.4,
    "averagePriorityScore": 68.8,
    "highPriorityDistricts": 8,
    "mediumPriorityDistricts": 15,
    "lowPriorityDistricts": 10
  }
}
```

---

## Response Fields

| Field                   | Description                         |
| ----------------------- | ----------------------------------- |
| districtCount           | Number of evaluated districts       |
| highestPriorityScore    | Maximum District Priority Score     |
| averagePriorityScore    | Mean District Priority Score        |
| highPriorityDistricts   | Number of high-priority districts   |
| mediumPriorityDistricts | Number of medium-priority districts |
| lowPriorityDistricts    | Number of low-priority districts    |

---

## Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 500  | Internal Server Error |

---

# Recommendation API Validation Rules

The Recommendation API validates all requests before returning recommendation results.

---

## District Validation

Endpoints requiring a district name must satisfy the following conditions:

- District name must be provided.
- District must exist within the processed dataset.
- District names are matched case-insensitively.
- Unknown districts return:

```http
404 Not Found
```

---

## Query Parameter Validation

Where filtering parameters are supported:

- Parameter values must conform to documented formats.
- Invalid values should return:

```http
400 Bad Request
```

- Unsupported parameters should not influence recommendation results.

---

## Recommendation Availability

Recommendation endpoints assume that:

- Predictions have been generated.
- District analytics are available.
- The Decision Engine has successfully produced recommendation outputs.

If recommendation generation is unavailable, the API should return:

```http
503 Service Unavailable
```

without exposing internal processing details.

---

# Recommendation API Design Notes

The Recommendation API exposes only finalized recommendation outputs.

It intentionally does not expose:

- District Priority Score calculation formula
- Decision Engine implementation
- Weighting strategy
- Infrastructure scoring logic
- Machine learning features
- Intermediate analytical values
- Internal ranking algorithms

The Decision Engine remains solely responsible for generating recommendations.

The API functions only as the public interface through which those recommendation results are delivered to the frontend and AI Assistant.

The exact computation of the District Priority Score remains implementation-dependent, consistent with the approved Project Scope and System Architecture, allowing refinement during implementation without requiring changes to the public API contract.

---

# AI Assistant API Endpoints

The AI Assistant API provides natural language interaction capabilities for EVision Telangana.

These endpoints allow users to ask questions about dashboard insights, district recommendations, prediction results, and analytical summaries.

The AI Assistant serves as an explanation layer only.

It does not generate predictions, compute District Priority Scores, or replace the Decision Engine.

All AI responses are generated using backend-prepared context.

---

## AI Assistant Endpoint Overview

| Method | Endpoint                 | Purpose                                |
| ------ | ------------------------ | -------------------------------------- |
| POST   | `/assistant/chat`        | Submit a user question                 |
| POST   | `/assistant/explain`     | Explain a recommendation or prediction |
| GET    | `/assistant/suggestions` | Retrieve suggested questions           |

---

# POST /assistant/chat

## Purpose

Accepts a natural language question from the user and returns an AI-generated response.

The backend prepares relevant application context before communicating with the configured LLM provider.

---

## Request

```http
POST /api/v1/assistant/chat
```

---

## Request Body

```json
{
  "question": "Which district has the highest predicted charging demand?"
}
```

---

## Request Fields

| Field    | Type   | Required | Description                   |
| -------- | ------ | -------- | ----------------------------- |
| question | string | Yes      | User's natural language query |

---

## Successful Response

```json
{
  "success": true,
  "message": "Response generated successfully.",
  "data": {
    "answer": "Hyderabad currently has the highest predicted charging demand based on the available forecasting results."
  }
}
```

---

## Response Fields

| Field  | Description                            |
| ------ | -------------------------------------- |
| answer | AI-generated natural language response |

---

## Status Codes

| Code | Meaning                |
| ---- | ---------------------- |
| 200  | Success                |
| 400  | Invalid Request        |
| 503  | AI Service Unavailable |
| 500  | Internal Server Error  |

---

# POST /assistant/explain

## Purpose

Generates a natural language explanation for an existing system output.

Examples include:

- District recommendation
- Prediction result
- Cluster assignment
- Dashboard insight

Unlike `/assistant/chat`, this endpoint expects structured application context rather than an open-ended question.

---

## Request

```http
POST /api/v1/assistant/explain
```

---

## Request Body

```json
{
  "district": "Hyderabad",
  "context": "recommendation"
}
```

---

## Request Fields

| Field    | Type   | Required | Description                    |
| -------- | ------ | -------- | ------------------------------ |
| district | string | Yes      | District requiring explanation |
| context  | string | Yes      | Type of explanation requested  |

---

## Accepted Context Values

Typical values include:

```text
recommendation

prediction

analytics

cluster
```

Additional context types may be introduced in future API versions.

---

## Successful Response

```json
{
  "success": true,
  "message": "Explanation generated successfully.",
  "data": {
    "explanation": "Hyderabad receives a high recommendation because it combines strong forecasted charging demand with significant infrastructure planning potential."
  }
}
```

---

## Response Fields

| Field       | Description              |
| ----------- | ------------------------ |
| explanation | AI-generated explanation |

---

## Status Codes

| Code | Meaning                |
| ---- | ---------------------- |
| 200  | Success                |
| 400  | Validation Error       |
| 404  | District Not Found     |
| 503  | AI Service Unavailable |
| 500  | Internal Server Error  |

---

# GET /assistant/suggestions

## Purpose

Returns predefined example questions that help users interact with the AI Assistant.

These suggestions improve discoverability and provide examples of supported queries.

---

## Request

```http
GET /api/v1/assistant/suggestions
```

---

## Query Parameters

None.

---

## Successful Response

```json
{
  "success": true,
  "message": "Suggestions retrieved successfully.",
  "data": [
    "Which district has the highest predicted demand?",
    "Why is Hyderabad highly recommended?",
    "Compare Hyderabad and Warangal.",
    "Explain the district clusters.",
    "Summarize dashboard insights."
  ]
}
```

---

## Response Fields

| Field | Description                       |
| ----- | --------------------------------- |
| data  | Collection of suggested questions |

---

## Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 500  | Internal Server Error |

---

# AI Assistant Validation Rules

The AI Assistant validates all requests before contacting the configured LLM provider.

---

## Question Validation

Questions must satisfy the following conditions:

- Question must be provided.
- Question must not be empty.
- Leading and trailing whitespace should be ignored.
- Extremely long requests may be rejected according to backend limits.

Invalid requests should return:

```http
400 Bad Request
```

---

## District Validation

Endpoints requiring district information must verify that:

- District exists within the processed dataset.
- District lookup is case-insensitive.
- Invalid district names return:

```http
404 Not Found
```

---

## Context Validation

The `context` field must contain one of the documented explanation categories.

Unsupported values should return:

```http
400 Bad Request
```

---

## AI Service Availability

If communication with the configured LLM provider fails, the backend should return:

```http
503 Service Unavailable
```

The response should remain user-friendly and must not expose:

- API credentials
- Provider-specific diagnostics
- Internal prompt construction
- Backend implementation details

---

# AI Assistant Design Notes

The AI Assistant operates as an interpretation layer within the overall system architecture.

The API intentionally exposes only natural language responses.

It does not expose:

- Prompt templates
- Prompt engineering strategies
- Machine learning models
- Decision Engine calculations
- Internal application logic
- Raw datasets
- API provider configuration

The backend remains responsible for:

- Context preparation
- Prompt construction
- AI provider communication
- Response validation
- Output formatting

The AI Assistant explains outputs generated by the Machine Learning Engine and Decision Engine.

It never performs prediction, district prioritization, or analytical computation independently.

---

# Health API Endpoints

The Health API provides operational information about the backend application.

These endpoints support application monitoring, startup verification, deployment validation, and troubleshooting.

Health endpoints report service availability only.

They do not expose internal configuration, sensitive information, or implementation details.

---

## Health Endpoint Overview

| Method | Endpoint           | Purpose                             |
| ------ | ------------------ | ----------------------------------- |
| GET    | `/health`          | Overall application health          |
| GET    | `/health/database` | Database connectivity status        |
| GET    | `/health/models`   | Machine learning model availability |
| GET    | `/health/ai`       | AI service availability             |

---

# GET /health

## Purpose

Returns the overall operational status of the backend application.

This endpoint is intended for:

- Application startup verification
- Deployment validation
- System monitoring
- Backend availability checks

---

## Request

```http
GET /api/v1/health
```

---

## Query Parameters

None.

---

## Request Body

None.

---

## Successful Response

```json
{
  "success": true,
  "message": "Application is healthy.",
  "data": {
    "status": "Healthy",
    "apiVersion": "v1"
  }
}
```

---

## Response Fields

| Field      | Description                |
| ---------- | -------------------------- |
| status     | Overall application status |
| apiVersion | Current API version        |

---

## Status Codes

| Code | Meaning             |
| ---- | ------------------- |
| 200  | Healthy             |
| 503  | Service Unavailable |

---

# GET /health/database

## Purpose

Returns the availability of the application's database connection.

The endpoint verifies connectivity only.

It does not expose:

- Database schema
- Tables
- Queries
- Records
- Connection strings

---

## Request

```http
GET /api/v1/health/database
```

---

## Successful Response

```json
{
  "success": true,
  "message": "Database connection successful.",
  "data": {
    "status": "Connected"
  }
}
```

---

## Response Fields

| Field  | Description                |
| ------ | -------------------------- |
| status | Database connection status |

---

## Status Codes

| Code | Meaning              |
| ---- | -------------------- |
| 200  | Connected            |
| 503  | Database Unavailable |

---

# GET /health/models

## Purpose

Verifies that the trained machine learning models have been loaded successfully.

The endpoint reports model availability only.

It does not expose:

- Model files
- Algorithms
- Hyperparameters
- Evaluation metrics
- Feature engineering

---

## Request

```http
GET /api/v1/health/models
```

---

## Successful Response

```json
{
  "success": true,
  "message": "Machine learning models loaded successfully.",
  "data": {
    "status": "Available"
  }
}
```

---

## Response Fields

| Field  | Description        |
| ------ | ------------------ |
| status | Model availability |

---

## Status Codes

| Code | Meaning            |
| ---- | ------------------ |
| 200  | Models Available   |
| 503  | Models Unavailable |

---

# GET /health/ai

## Purpose

Returns the operational status of the configured AI provider.

This endpoint verifies that the AI Assistant service is available.

It does not expose:

- API keys
- Provider configuration
- Prompt templates
- Request history

---

## Request

```http
GET /api/v1/health/ai
```

---

## Successful Response

```json
{
  "success": true,
  "message": "AI service is available.",
  "data": {
    "status": "Available"
  }
}
```

---

## Response Fields

| Field  | Description             |
| ------ | ----------------------- |
| status | AI service availability |

---

## Status Codes

| Code | Meaning                |
| ---- | ---------------------- |
| 200  | AI Service Available   |
| 503  | AI Service Unavailable |

---

# Request Schema Definitions

This section defines the standard request payloads used throughout the API.

Individual endpoints may extend these schemas where necessary.

---

## ChatRequest

Used by:

```text
POST /assistant/chat
```

### Schema

```json
{
  "question": "string"
}
```

---

### Field Definitions

| Field    | Type   | Required | Description                   |
| -------- | ------ | -------- | ----------------------------- |
| question | string | Yes      | User's natural language query |

---

## ExplainRequest

Used by:

```text
POST /assistant/explain
```

### Schema

```json
{
  "district": "string",
  "context": "string"
}
```

---

### Field Definitions

| Field    | Type   | Required | Description                    |
| -------- | ------ | -------- | ------------------------------ |
| district | string | Yes      | District requiring explanation |
| context  | string | Yes      | Explanation category           |

---

# Response Schema Definitions

Every endpoint returns one of two standard response models.

---

## SuccessResponse

```json
{
  "success": true,
  "message": "string",
  "data": {},
  "metadata": {}
}
```

---

### Field Definitions

| Field    | Type            | Description                        |
| -------- | --------------- | ---------------------------------- |
| success  | boolean         | Indicates successful execution     |
| message  | string          | Human-readable status message      |
| data     | object or array | Requested resource                 |
| metadata | object          | Optional supplementary information |

---

## ErrorResponse

```json
{
  "success": false,
  "message": "string",
  "error": {
    "code": "string",
    "details": []
  }
}
```

---

### Field Definitions

| Field         | Type    | Description                       |
| ------------- | ------- | --------------------------------- |
| success       | boolean | Always false                      |
| message       | string  | Human-readable error summary      |
| error.code    | string  | Machine-readable error identifier |
| error.details | array   | Additional validation details     |

---

# Common Data Models

The following reusable data models appear throughout multiple endpoints.

---

## District

```json
{
  "district": "Hyderabad"
}
```

---

## Prediction

```json
{
  "district": "Hyderabad",
  "predictedDemand": 14253.7
}
```

---

## Recommendation

```json
{
  "district": "Hyderabad",
  "priorityScore": 92.4,
  "priorityLevel": "High"
}
```

---

## Cluster

```json
{
  "district": "Hyderabad",
  "cluster": 2
}
```

---

## Charging Station

```json
{
  "stationName": "EV Charging Station A",
  "district": "Hyderabad",
  "latitude": 17.385,
  "longitude": 78.486,
  "organization": "TGREDCO"
}
```

---

## Trend Record

```json
{
  "month": "2026-06",
  "demand": 10891.7
}
```

---

## AI Response

```json
{
  "answer": "Natural language explanation."
}
```

---

# Error Model

The EVision Telangana API uses a standardized error model across all endpoints.

A consistent error structure enables predictable frontend behavior, simplifies debugging, and improves maintainability.

Every failed request returns an HTTP status code together with a structured JSON response.

The API should never expose internal implementation details, stack traces, SQL queries, machine learning artifacts, or configuration information.

---

## Standard Error Structure

```json
{
  "success": false,
  "message": "Validation failed.",
  "error": {
    "code": "VALIDATION_ERROR",
    "details": [
      {
        "field": "district",
        "issue": "District name is required."
      }
    ]
  }
}
```

---

## Error Fields

| Field         | Description                                     |
| ------------- | ----------------------------------------------- |
| success       | Always `false`                                  |
| message       | Human-readable error summary                    |
| error.code    | Machine-readable error identifier               |
| error.details | Additional validation or diagnostic information |

---

# Standard Error Codes

The API uses consistent application-level error codes.

| Error Code            | Description                               |
| --------------------- | ----------------------------------------- |
| VALIDATION_ERROR      | Request validation failed                 |
| INVALID_PARAMETER     | Invalid query or path parameter           |
| RESOURCE_NOT_FOUND    | Requested resource does not exist         |
| PREDICTION_FAILED     | Prediction could not be generated         |
| AI_SERVICE_ERROR      | AI provider unavailable                   |
| DATABASE_ERROR        | Backend database unavailable              |
| INTERNAL_SERVER_ERROR | Unexpected backend failure                |
| SERVICE_UNAVAILABLE   | Requested service temporarily unavailable |

These error codes remain stable across API versions.

---

# Validation Rules

Validation is performed before business logic execution.

Invalid requests should terminate immediately with an appropriate HTTP response.

---

## General Validation

All endpoints should validate:

- Required fields
- Data types
- Accepted value ranges
- Supported parameter names
- Request format
- JSON syntax

---

## Path Parameter Validation

Path parameters must satisfy the following requirements:

- Required values must be supplied.
- Parameters must follow documented formats.
- Invalid resources should return:

```http
404 Not Found
```

Example:

```http
GET /districts/UnknownDistrict
```

---

## Query Parameter Validation

Query parameters should:

- Match supported parameter names.
- Use correct data types.
- Remain within documented limits.

Example:

```text
limit=10
```

Invalid values should return:

```http
400 Bad Request
```

---

## JSON Validation

POST requests must contain valid JSON.

Malformed JSON should return:

```http
400 Bad Request
```

The backend should never attempt to process invalid request bodies.

---

## String Validation

String fields should:

- Trim leading whitespace.
- Trim trailing whitespace.
- Reject empty values where required.
- Apply case-insensitive matching where documented.

---

## Numeric Validation

Numeric values should:

- Be valid numeric types.
- Remain within supported ranges.
- Reject invalid formats.

Example:

```text
limit=-5
```

should return:

```http
400 Bad Request
```

---

## District Validation

District names must:

- Exist within the processed dataset.
- Match official district names after normalization.
- Be compared case-insensitively.

Unknown districts should return:

```http
404 Not Found
```

---

## AI Request Validation

AI requests must satisfy the following conditions:

- Question must not be empty.
- Context must use supported values.
- District must exist where applicable.

Requests violating these rules should return validation errors before contacting the AI provider.

---

# HTTP Status Code Conventions

The API uses standard HTTP status codes consistently.

---

## 200 OK

Returned when a request completes successfully.

Examples:

- Dashboard retrieved
- Prediction generated
- Recommendation returned
- AI explanation generated

---

## 400 Bad Request

Returned when the client submits an invalid request.

Examples:

- Invalid JSON
- Missing required field
- Invalid query parameter
- Unsupported context type

---

## 404 Not Found

Returned when the requested resource cannot be located.

Examples:

- Unknown district
- Invalid endpoint
- Missing recommendation

---

## 405 Method Not Allowed

Returned when an unsupported HTTP method is used.

Example:

```http
DELETE /predictions
```

---

## 422 Unprocessable Entity

Returned when request syntax is valid but semantic validation fails.

Examples include:

- Invalid field format
- Invalid request schema
- Type validation failure

---

## 500 Internal Server Error

Returned for unexpected backend failures.

User-facing responses should remain concise.

Detailed diagnostics should be written only to backend logs.

---

## 503 Service Unavailable

Returned when a required backend service is temporarily unavailable.

Examples:

- Database unavailable
- Machine learning models unavailable
- AI provider unavailable

---

# API Consistency Rules

All endpoints should follow the same implementation-independent conventions.

---

## Response Consistency

Every response should contain:

- success
- message
- data (or error)
- optional metadata

The overall response structure should never vary between endpoint categories.

---

## Naming Consistency

Endpoints should:

- Use lowercase paths.
- Use plural resource names.
- Avoid implementation terminology.
- Remain REST-oriented.

Example:

```text
/api/v1/recommendations
```

Preferred over:

```text
/getRecommendation
```

---

## Validation Consistency

Validation should occur before:

- Database access
- Machine learning inference
- Decision Engine execution
- AI provider communication

Early validation improves reliability and performance.

---

## Error Consistency

Errors should:

- Use standardized structures.
- Use documented error codes.
- Avoid exposing implementation details.
- Remain human-readable.

---

## JSON Consistency

All request and response payloads use JSON.

Alternative serialization formats are intentionally unsupported.

---

# Future API Extension Guidelines

The API has been designed to support future enhancements without disrupting existing clients.

Possible future additions include:

- Authentication and authorization
- User management
- Saved dashboard views
- Report export endpoints
- Multi-year forecasting
- Additional analytics
- Population density endpoints
- Road network analysis
- Administrative APIs
- Mobile application support

New capabilities should extend the existing endpoint hierarchy rather than introducing duplicate resource structures.

Breaking API changes should only be introduced through a new major version.

---

# API Governance

This document defines the approved REST API contract for EVision Telangana.

Frontend and backend development should conform to the endpoint definitions, request formats, response structures, validation rules, and API conventions described herein.

Changes to the API contract should only be made when:

- Required by verified implementation constraints,
- Required to resolve integration issues,
- Required by the project supervisor,
- Required to correct factual inaccuracies, or
- Introduced as a new API version.

Implementation changes that do not affect the public API contract should not require modification of this document.

The API Specification must remain consistent with the approved Project Scope, Master Roadmap, Final Tech Stack, System Architecture, Repository Structure, and Git Workflow.

---

# Conclusion

The EVision Telangana API Specification establishes a consistent, maintainable, and implementation-independent REST API contract for communication between the frontend dashboard and backend services.

By defining standardized endpoint organization, request and response schemas, validation rules, error handling, versioning strategy, and resource conventions, the specification enables parallel frontend and backend development while ensuring reliable system integration.

The API remains fully aligned with the approved project architecture and intentionally abstracts internal implementation details such as database operations, machine learning models, and Decision Engine logic behind a stable and predictable REST interface.

This document serves as the authoritative API contract for the implementation, testing, integration, and future evolution of EVision Telangana.

```

```
