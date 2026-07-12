- [Coding Standards](#coding-standards)
- [Purpose](#purpose)
- [Relationship to Other Project Documents](#relationship-to-other-project-documents)
- [Coding Standards Objectives](#coding-standards-objectives)
  - [1. Consistency](#1-consistency)
  - [2. Readability](#2-readability)
  - [3. Maintainability](#3-maintainability)
  - [4. Reliability](#4-reliability)
  - [5. Collaboration](#5-collaboration)
  - [6. Scalability](#6-scalability)
- [General Coding Philosophy](#general-coding-philosophy)
  - [Simplicity First](#simplicity-first)
  - [Single Responsibility Principle](#single-responsibility-principle)
  - [Separation of Concerns](#separation-of-concerns)
  - [Modularity](#modularity)
  - [Readability Over Cleverness](#readability-over-cleverness)
  - [Explicit Over Implicit](#explicit-over-implicit)
  - [Consistency Over Personal Preference](#consistency-over-personal-preference)
  - [Reusability](#reusability)
  - [Predictable Behavior](#predictable-behavior)
  - [Defensive Programming](#defensive-programming)
  - [Fail Gracefully](#fail-gracefully)
  - [Keep Business Logic Centralized](#keep-business-logic-centralized)
  - [Maintain API Contract Integrity](#maintain-api-contract-integrity)
  - [Maintain Database Contract Integrity](#maintain-database-contract-integrity)
  - [Preserve Data Contract Consistency](#preserve-data-contract-consistency)
  - [Prefer Composition Over Duplication](#prefer-composition-over-duplication)
  - [Continuous Refactoring](#continuous-refactoring)
  - [Documentation as Part of Development](#documentation-as-part-of-development)
  - [Team-Oriented Development](#team-oriented-development)
- [Core Development Principles](#core-development-principles)
  - [Build for Maintainability](#build-for-maintainability)
  - [Follow the Approved Architecture](#follow-the-approved-architecture)
  - [Keep Modules Small](#keep-modules-small)
  - [Minimize Coupling](#minimize-coupling)
  - [Maximize Cohesion](#maximize-cohesion)
  - [Prefer Configuration Over Hardcoding](#prefer-configuration-over-hardcoding)
  - [Avoid Magic Values](#avoid-magic-values)
  - [Write Deterministic Code](#write-deterministic-code)
  - [Validate Early](#validate-early)
  - [Keep Functions Focused](#keep-functions-focused)
  - [Avoid Deep Nesting](#avoid-deep-nesting)
  - [Do Not Repeat Yourself (DRY)](#do-not-repeat-yourself-dry)
  - [Prefer Explicit Error Handling](#prefer-explicit-error-handling)
  - [Protect Sensitive Information](#protect-sensitive-information)
  - [Write Testable Code](#write-testable-code)
  - [Optimize Only When Necessary](#optimize-only-when-necessary)
  - [Keep Dependencies Minimal](#keep-dependencies-minimal)
  - [Respect Existing Contracts](#respect-existing-contracts)
  - [Continuous Integration Mindset](#continuous-integration-mindset)
  - [Prioritize Team Readability](#prioritize-team-readability)
- [Python Coding Standards](#python-coding-standards)
- [Python Style Guide](#python-style-guide)
- [Indentation](#indentation)
- [Maximum Line Length](#maximum-line-length)
- [Blank Lines](#blank-lines)
- [Variable Naming](#variable-naming)
- [Constants](#constants)
- [Function Naming](#function-naming)
- [Class Naming](#class-naming)
- [Module Naming](#module-naming)
- [Package Naming](#package-naming)
- [Function Size](#function-size)
- [Parameter Count](#parameter-count)
- [Return Values](#return-values)
- [Type Hints](#type-hints)
- [Docstrings](#docstrings)
- [Imports](#imports)
- [List Comprehensions](#list-comprehensions)
- [Boolean Expressions](#boolean-expressions)
- [Context Managers](#context-managers)
- [Exceptions](#exceptions)
- [Logging](#logging)
- [Mutable Default Arguments](#mutable-default-arguments)
- [Global Variables](#global-variables)
- [Magic Numbers](#magic-numbers)
- [Assertions](#assertions)
- [Deprecated Features](#deprecated-features)
- [Code Formatting](#code-formatting)
- [JavaScript / React Coding Standards](#javascript--react-coding-standards)
- [JavaScript Style Guide](#javascript-style-guide)
- [Indentation](#indentation-1)
- [Maximum Line Length](#maximum-line-length-1)
- [Variable Naming](#variable-naming-1)
- [Constants](#constants-1)
- [Function Naming](#function-naming-1)
- [React Component Naming](#react-component-naming)
- [File Naming](#file-naming)
- [Component Design](#component-design)
- [Functional Components](#functional-components)
- [Hooks](#hooks)
- [State Management](#state-management)
- [Props](#props)
- [Event Handler Naming](#event-handler-naming)
- [API Calls](#api-calls)
- [Async Programming](#async-programming)
- [Conditional Rendering](#conditional-rendering)
- [Lists](#lists)
- [Styling](#styling)
- [Error Handling](#error-handling)
- [Logging](#logging-1)
- [Comments](#comments)
- [Code Formatting](#code-formatting-1)
- [Naming Conventions](#naming-conventions)
- [General Principles](#general-principles)
- [Variables](#variables)
  - [Python](#python)
  - [JavaScript](#javascript)
- [Constants](#constants-2)
- [Functions](#functions)
- [Classes](#classes)
- [React Components](#react-components)
- [SQLModel Models](#sqlmodel-models)
- [Pydantic Schemas](#pydantic-schemas)
- [API Routers](#api-routers)
- [Services](#services)
- [Repositories](#repositories)
- [Utility Modules](#utility-modules)
- [Exceptions](#exceptions-1)
- [Test Files](#test-files)
- [Environment Variables](#environment-variables)
- [Database Tables](#database-tables)
- [Database Columns](#database-columns)
- [API Endpoints](#api-endpoints)
- [Branch Names](#branch-names)
- [Commit Messages](#commit-messages)
- [File and Directory Consistency](#file-and-directory-consistency)
- [Abbreviation Guidelines](#abbreviation-guidelines)
- [Reserved Terminology](#reserved-terminology)
- [File Naming Conventions](#file-naming-conventions)
- [General Principles](#general-principles-1)
- [Python Files](#python-files)
- [JavaScript Files](#javascript-files)
- [React Component Files](#react-component-files)
- [CSS Files](#css-files)
- [Configuration Files](#configuration-files)
- [Environment Files](#environment-files)
- [API Router Files](#api-router-files)
- [Service Files](#service-files)
- [Repository Files](#repository-files)
- [SQLModel Files](#sqlmodel-files)
- [Schema Files](#schema-files)
- [Utility Files](#utility-files)
- [Test Files](#test-files-1)
- [Notebook Files](#notebook-files)
- [Dataset Files](#dataset-files)
- [Machine Learning Model Files](#machine-learning-model-files)
- [Documentation Files](#documentation-files)
- [Image Files](#image-files)
- [Generated Output Files](#generated-output-files)
- [Temporary Files](#temporary-files)
- [File Naming Best Practices](#file-naming-best-practices)
- [Directory Conventions](#directory-conventions)
- [General Principles](#general-principles-2)
- [Backend Directory Conventions](#backend-directory-conventions)
  - [api/](#api)
  - [core/](#core)
  - [database/](#database)
  - [models/](#models)
  - [schemas/](#schemas)
  - [repositories/](#repositories-1)
  - [services/](#services-1)
  - [ml/](#ml)
  - [utils/](#utils)
- [Frontend Directory Conventions](#frontend-directory-conventions)
  - [components/](#components)
  - [pages/](#pages)
  - [services/](#services-2)
  - [hooks/](#hooks-1)
  - [assets/](#assets)
  - [styles/](#styles)
- [Data Directory Conventions](#data-directory-conventions)
  - [raw/](#raw)
  - [processed/](#processed)
  - [external/](#external)
- [Models Directory](#models-directory)
- [Notebooks Directory](#notebooks-directory)
- [Scripts Directory](#scripts-directory)
- [Tests Directory](#tests-directory)
- [Documentation Directory](#documentation-directory)
- [Generated Files](#generated-files)
- [Temporary Files](#temporary-files-1)
- [Directory Depth](#directory-depth)
- [One Responsibility Per Directory](#one-responsibility-per-directory)
- [Consistent Organization](#consistent-organization)
- [Directory Creation Guidelines](#directory-creation-guidelines)
- [Long-Term Maintainability](#long-term-maintainability)
- [Function Design Standards](#function-design-standards)
- [General Principles](#general-principles-3)
- [Single Responsibility](#single-responsibility)
- [Function Length](#function-length)
- [Descriptive Names](#descriptive-names)
- [Clear Parameters](#clear-parameters)
- [Type Hints](#type-hints-1)
- [Return Values](#return-values-1)
- [Minimize Side Effects](#minimize-side-effects)
- [Early Returns](#early-returns)
- [Avoid Deep Nesting](#avoid-deep-nesting-1)
- [Pure Functions](#pure-functions)
- [Validation Responsibilities](#validation-responsibilities)
- [Avoid Hidden Dependencies](#avoid-hidden-dependencies)
- [Exception Handling](#exception-handling)
- [Logging](#logging-2)
- [Reusability](#reusability-1)
- [Documentation](#documentation)
- [Default Parameters](#default-parameters)
- [Async Functions](#async-functions)
- [Avoid Duplicate Logic](#avoid-duplicate-logic)
- [Function Organization](#function-organization)
- [Testing Expectations](#testing-expectations)
- [Function Review Checklist](#function-review-checklist)
- [Class Design Standards](#class-design-standards)
- [General Principles](#general-principles-4)
- [Single Responsibility](#single-responsibility-1)
- [Class Naming](#class-naming-1)
- [Keep Classes Small](#keep-classes-small)
- [High Cohesion](#high-cohesion)
- [Low Coupling](#low-coupling)
- [Constructor Responsibilities](#constructor-responsibilities)
- [Dependency Injection](#dependency-injection)
- [Instance Variables](#instance-variables)
- [Public and Private Methods](#public-and-private-methods)
- [Method Design](#method-design)
- [Class Documentation](#class-documentation)
- [SQLModel Classes](#sqlmodel-classes)
- [Pydantic Schemas](#pydantic-schemas-1)
- [Service Classes](#service-classes)
- [Repository Classes](#repository-classes)
- [Utility Classes](#utility-classes)
- [Inheritance](#inheritance)
- [Composition](#composition)
- [Mutable State](#mutable-state)
- [Error Handling](#error-handling-1)
- [Logging](#logging-3)
- [Testing Expectations](#testing-expectations-1)
- [Class Organization](#class-organization)
- [Class Review Checklist](#class-review-checklist)
- [API Coding Conventions](#api-coding-conventions)
- [General Principles](#general-principles-5)
- [RESTful Design](#restful-design)
- [API Versioning](#api-versioning)
- [HTTP Methods](#http-methods)
- [Resource Naming](#resource-naming)
- [Request Validation](#request-validation)
- [Response Models](#response-models)
- [Status Codes](#status-codes)
- [Route Responsibilities](#route-responsibilities)
- [Dependency Injection](#dependency-injection-1)
- [Error Responses](#error-responses)
- [Response Consistency](#response-consistency)
- [Pagination](#pagination)
- [Query Parameters](#query-parameters)
- [Path Parameters](#path-parameters)
- [JSON Responses](#json-responses)
- [Serialization](#serialization)
- [Logging](#logging-4)
- [OpenAPI Documentation](#openapi-documentation)
- [Asynchronous Endpoints](#asynchronous-endpoints)
- [Security Considerations](#security-considerations)
- [Testing Expectations](#testing-expectations-2)
- [API Review Checklist](#api-review-checklist)
- [SQLModel Conventions](#sqlmodel-conventions)
- [General Principles](#general-principles-6)
- [One Model Per Table](#one-model-per-table)
- [Class Naming](#class-naming-2)
- [File Organization](#file-organization)
- [Table Names](#table-names)
- [Column Naming](#column-naming)
- [Primary Keys](#primary-keys)
- [Foreign Keys](#foreign-keys)
- [Relationships](#relationships)
- [Field Definitions](#field-definitions)
- [Type Annotations](#type-annotations)
- [Nullable Fields](#nullable-fields)
- [Default Values](#default-values)
- [Timestamp Fields](#timestamp-fields)
- [Validation](#validation)
- [Business Logic](#business-logic)
- [Database Independence](#database-independence)
- [Import Organization](#import-organization)
- [Indexes](#indexes)
- [Documentation](#documentation-1)
- [Testing Expectations](#testing-expectations-3)
- [SQLModel Review Checklist](#sqlmodel-review-checklist)
- [Error Handling Conventions](#error-handling-conventions)
- [General Principles](#general-principles-7)
- [Fail Fast](#fail-fast)
- [Validate Before Processing](#validate-before-processing)
- [Raise Specific Exceptions](#raise-specific-exceptions)
- [Avoid Bare Exceptions](#avoid-bare-exceptions)
- [Do Not Suppress Errors](#do-not-suppress-errors)
- [Use Custom Exceptions](#use-custom-exceptions)
- [Preserve Context](#preserve-context)
- [Error Messages](#error-messages)
- [API Error Responses](#api-error-responses)
- [HTTP Status Codes](#http-status-codes)
- [Database Errors](#database-errors)
- [Machine Learning Errors](#machine-learning-errors)
- [File Handling Errors](#file-handling-errors)
- [Configuration Errors](#configuration-errors)
- [Frontend Error Handling](#frontend-error-handling)
- [Logging Errors](#logging-errors)
- [Retry Strategy](#retry-strategy)
- [Cleanup After Failure](#cleanup-after-failure)
- [Testing Error Scenarios](#testing-error-scenarios)
- [Error Handling Review Checklist](#error-handling-review-checklist)
- [Logging Conventions](#logging-conventions)
- [Logging Objectives](#logging-objectives)
- [General Principles](#general-principles-8)
- [Use the Standard Logging Module](#use-the-standard-logging-module)
- [Log Levels](#log-levels)
- [DEBUG Logs](#debug-logs)
- [INFO Logs](#info-logs)
- [WARNING Logs](#warning-logs)
- [ERROR Logs](#error-logs)
- [CRITICAL Logs](#critical-logs)
- [Log Message Style](#log-message-style)
- [Include Relevant Context](#include-relevant-context)
- [Avoid Sensitive Information](#avoid-sensitive-information)
- [Exception Logging](#exception-logging)
- [Startup Logging](#startup-logging)
- [Shutdown Logging](#shutdown-logging)
- [API Logging](#api-logging)
- [Database Logging](#database-logging)
- [Machine Learning Logging](#machine-learning-logging)
- [Data Processing Logging](#data-processing-logging)
- [Frontend Logging](#frontend-logging)
- [Log Formatting](#log-formatting)
- [Logging Frequency](#logging-frequency)
- [Testing Logging](#testing-logging)
- [Logging Review Checklist](#logging-review-checklist)
- [Documentation Conventions](#documentation-conventions)
- [Documentation Objectives](#documentation-objectives)
- [General Principles](#general-principles-9)
- [Single Source of Truth](#single-source-of-truth)
- [Keep Documentation Current](#keep-documentation-current)
- [Module Documentation](#module-documentation)
- [Class Documentation](#class-documentation-1)
- [Function Documentation](#function-documentation)
- [API Documentation](#api-documentation)
- [Database Documentation](#database-documentation)
- [Data Documentation](#data-documentation)
- [README Files](#readme-files)
- [Inline Documentation](#inline-documentation)
- [Architecture Documentation](#architecture-documentation)
- [Configuration Documentation](#configuration-documentation)
- [Markdown Style](#markdown-style)
- [Diagrams](#diagrams)
- [Examples](#examples)
- [Avoid Redundant Documentation](#avoid-redundant-documentation)
- [Documentation During Development](#documentation-during-development)
- [Review Expectations](#review-expectations)
- [Documentation Review Checklist](#documentation-review-checklist)
- [Commenting Guidelines](#commenting-guidelines)
- [Commenting Objectives](#commenting-objectives)
- [General Principles](#general-principles-10)
- [Prefer Self-Documenting Code](#prefer-self-documenting-code)
- [Explain Why, Not What](#explain-why-not-what)
- [Document Business Rules](#document-business-rules)
- [Explain Complex Logic](#explain-complex-logic)
- [Use Block Comments Sparingly](#use-block-comments-sparingly)
- [Inline Comments](#inline-comments)
- [TODO Comments](#todo-comments)
- [FIXME Comments](#fixme-comments)
- [HACK Comments](#hack-comments)
- [Module Comments](#module-comments)
- [Class Comments](#class-comments)
- [Function Comments](#function-comments)
- [Comment Accuracy](#comment-accuracy)
- [Avoid Redundant Comments](#avoid-redundant-comments)
- [Comment Style](#comment-style)
- [Avoid Dead Code](#avoid-dead-code)
- [Frontend Comments](#frontend-comments)
- [Machine Learning Comments](#machine-learning-comments)
- [Review Expectations](#review-expectations-1)
- [Commenting Review Checklist](#commenting-review-checklist)
- [Type Hint Guidelines](#type-hint-guidelines)
- [Objectives](#objectives)
- [General Principles](#general-principles-11)
- [Public Functions](#public-functions)
- [Private Functions](#private-functions)
- [Return Types](#return-types)
- [Variable Annotations](#variable-annotations)
- [Collections](#collections)
- [Optional Values](#optional-values)
- [Union Types](#union-types)
- [SQLModel Fields](#sqlmodel-fields)
- [Pydantic Schemas](#pydantic-schemas-2)
- [Class Attributes](#class-attributes)
- [Constants](#constants-3)
- [Callable Types](#callable-types)
- [Generic Types](#generic-types)
- [Any](#any)
- [Type Aliases](#type-aliases)
- [Forward References](#forward-references)
- [Third-Party Libraries](#third-party-libraries)
- [Runtime Validation](#runtime-validation)
- [Static Analysis](#static-analysis)
- [Consistency](#consistency)
- [Type Hint Review Checklist](#type-hint-review-checklist)
- [Import Organization](#import-organization-1)
- [General Principles](#general-principles-12)
- [Python Import Order](#python-import-order)
- [Standard Library Imports](#standard-library-imports)
- [Third-Party Imports](#third-party-imports)
- [Local Project Imports](#local-project-imports)
- [Alphabetical Ordering](#alphabetical-ordering)
- [One Import Per Line](#one-import-per-line)
- [Avoid Wildcard Imports](#avoid-wildcard-imports)
- [Import Only What Is Needed](#import-only-what-is-needed)
- [Circular Imports](#circular-imports)
- [Relative Imports](#relative-imports)
- [Conditional Imports](#conditional-imports)
- [Imports Inside Functions](#imports-inside-functions)
- [JavaScript Import Order](#javascript-import-order)
- [Named vs Default Imports](#named-vs-default-imports)
- [Grouping Imports](#grouping-imports)
- [Remove Unused Imports](#remove-unused-imports)
- [Import Side Effects](#import-side-effects)
- [Dependency Direction](#dependency-direction)
- [Import Review Checklist](#import-review-checklist)
- [Project Organization Principles](#project-organization-principles)
- [Organization Objectives](#organization-objectives)
- [Layered Architecture](#layered-architecture)
- [Separation of Concerns](#separation-of-concerns-1)
- [Modular Design](#modular-design)
- [Domain-Oriented Organization](#domain-oriented-organization)
- [One Responsibility Per File](#one-responsibility-per-file)
- [One Responsibility Per Directory](#one-responsibility-per-directory-1)
- [Business Logic Centralization](#business-logic-centralization)
- [Reusable Components](#reusable-components)
- [Consistent Naming](#consistent-naming)
- [Keep Dependencies Directional](#keep-dependencies-directional)
- [Avoid Circular Dependencies](#avoid-circular-dependencies)
- [Feature Isolation](#feature-isolation)
- [Shared Utilities](#shared-utilities)
- [Configuration Management](#configuration-management)
- [Data Ownership](#data-ownership)
- [Keep Experimental Code Separate](#keep-experimental-code-separate)
- [Test Organization](#test-organization)
- [Documentation Organization](#documentation-organization)
- [Scalability](#scalability)
- [Project Organization Review Checklist](#project-organization-review-checklist)
- [Testing Expectations](#testing-expectations-4)
- [Testing Objectives](#testing-objectives)
- [General Principles](#general-principles-13)
- [Test Organization](#test-organization-1)
- [Unit Testing](#unit-testing)
- [Integration Testing](#integration-testing)
- [API Testing](#api-testing)
- [Database Testing](#database-testing)
- [Machine Learning Testing](#machine-learning-testing)
- [Data Pipeline Testing](#data-pipeline-testing)
- [Frontend Testing](#frontend-testing)
- [Error Handling Tests](#error-handling-tests)
- [Input Validation Tests](#input-validation-tests)
- [Mocking](#mocking)
- [Test Data](#test-data)
- [Deterministic Tests](#deterministic-tests)
- [Performance](#performance)
- [Independence](#independence)
- [Naming Conventions](#naming-conventions-1)
- [Assertions](#assertions-1)
- [Regression Testing](#regression-testing)
- [Continuous Verification](#continuous-verification)
- [Test Coverage](#test-coverage)
- [Testing Review Checklist](#testing-review-checklist)
- [Ruff Usage](#ruff-usage)
- [Objectives](#objectives-1)
- [Scope](#scope)
- [Formatting](#formatting)
- [Linting](#linting)
- [Import Organization](#import-organization-2)
- [Line Length](#line-length)
- [Naming Compliance](#naming-compliance)
- [Error Resolution](#error-resolution)
- [Ignore Rules](#ignore-rules)
- [Automatic Formatting](#automatic-formatting)
- [IDE Integration](#ide-integration)
- [Continuous Integration](#continuous-integration)
- [Relationship with PEP 8](#relationship-with-pep-8)
- [Common Ruff Checks](#common-ruff-checks)
- [Before Committing](#before-committing)
- [Ruff Review Checklist](#ruff-review-checklist)
- [Prettier Usage](#prettier-usage)
- [Objectives](#objectives-2)
- [Scope](#scope-1)
- [Formatting Philosophy](#formatting-philosophy)
- [Indentation](#indentation-2)
- [Line Length](#line-length-1)
- [Quotes](#quotes)
- [Semicolons](#semicolons)
- [Trailing Commas](#trailing-commas)
- [Object Formatting](#object-formatting)
- [JSX Formatting](#jsx-formatting)
- [Markdown Formatting](#markdown-formatting)
- [JSON Formatting](#json-formatting)
- [CSS Formatting](#css-formatting)
- [Automatic Formatting](#automatic-formatting-1)
- [IDE Integration](#ide-integration-1)
- [Relationship with ESLint](#relationship-with-eslint)
- [Before Committing](#before-committing-1)
- [Prettier Review Checklist](#prettier-review-checklist)
- [Code Review Checklist](#code-review-checklist)
- [Review Objectives](#review-objectives)
- [General Review Principles](#general-review-principles)
- [Architecture Compliance](#architecture-compliance)
- [Repository Organization](#repository-organization)
- [Coding Standards](#coding-standards-1)
- [Readability](#readability)
- [Business Logic](#business-logic-1)
- [Database Compliance](#database-compliance)
- [API Compliance](#api-compliance)
- [Data Contract Compliance](#data-contract-compliance)
- [Error Handling](#error-handling-2)
- [Logging](#logging-5)
- [Documentation](#documentation-2)
- [Comments](#comments-1)
- [Type Hints](#type-hints-2)
- [Testing](#testing)
- [Formatting](#formatting-1)
- [Security](#security)
- [Performance](#performance-1)
- [Git Hygiene](#git-hygiene)
- [Final Review Checklist](#final-review-checklist)
- [Approval Criteria](#approval-criteria)
- [Best Practices Summary](#best-practices-summary)
- [General Development](#general-development)
- [Project Organization](#project-organization)
- [Naming](#naming)
- [Functions](#functions-1)
- [Classes](#classes-1)
- [Backend Development](#backend-development)
- [Database](#database-1)
- [Frontend Development](#frontend-development)
- [Machine Learning](#machine-learning)
- [Error Handling](#error-handling-3)
- [Logging](#logging-6)
- [Documentation](#documentation-3)
- [Comments](#comments-2)
- [Type Hints](#type-hints-3)
- [Imports](#imports-1)
- [Testing](#testing-1)
- [Formatting](#formatting-2)
- [Collaboration](#collaboration)
- [Security](#security-1)
- [Continuous Improvement](#continuous-improvement)
- [Final Development Principles](#final-development-principles)
- [Coding Standards Governance](#coding-standards-governance)
  - [Authority](#authority)
  - [Applicability](#applicability)
  - [Exceptions](#exceptions-2)
  - [Future Revisions](#future-revisions)
  - [Compliance](#compliance)
  - [Final Statement](#final-statement)


# Coding Standards

**Project:** EVision Telangana  
**Official Project Title:** AI-Based EV Charging Infrastructure Planning and Decision Support System for Telangana

**Version:** 1.0  
**Status:** Frozen  
**Last Updated:** July 2026

---

# Purpose

This document defines the approved coding standards for EVision Telangana.

It establishes the implementation conventions, programming practices, formatting rules, naming conventions, documentation standards, testing expectations, and code quality requirements that shall be followed throughout the project.

The Coding Standards document serves as the implementation guide for all contributors, ensuring that code written by different team members remains consistent, readable, maintainable, and compatible with the approved architecture.

This document intentionally defines **how code should be written** rather than **what the system should do**.

Project scope, architecture, API contracts, database design, and data contracts remain defined in their respective Project Sources.

This document serves as the authoritative reference for implementation standards throughout the project lifecycle.

---

# Relationship to Other Project Documents

The Coding Standards document complements the existing Project Sources by defining implementation conventions.

| Document                             | Purpose                                                                                                                                       |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Final Project Scope                  | Defines project objectives, datasets, deliverables, and scope.                                                                                |
| Master Roadmap                       | Defines implementation phases and milestones.                                                                                                 |
| Final Tech Stack                     | Defines approved technologies and development tools.                                                                                          |
| System Architecture                  | Defines system components and module interactions.                                                                                            |
| Repository Structure                 | Defines project directory organization.                                                                                                       |
| Git Workflow                         | Defines collaboration and version control practices.                                                                                          |
| API Specification                    | Defines REST API contracts.                                                                                                                   |
| Database Schema                      | Defines the logical database design.                                                                                                          |
| Data Contracts                       | Defines datasets and data exchange contracts.                                                                                                 |
| **Coding Standards (This Document)** | Defines implementation conventions, formatting, naming standards, documentation practices, testing expectations, and code quality guidelines. |

This document does not modify the approved architecture or technology stack.

Instead, it standardizes how implementation should be performed across the entire codebase.

---

# Coding Standards Objectives

The approved coding standards have been designed around several primary objectives.

## 1. Consistency

Ensure every contributor writes code in a consistent style.

---

## 2. Readability

Prioritize code that is easy to understand and review.

---

## 3. Maintainability

Promote modular, organized, and easily maintainable code.

---

## 4. Reliability

Encourage implementation practices that reduce defects and improve robustness.

---

## 5. Collaboration

Allow multiple developers to contribute without introducing inconsistent coding styles.

---

## 6. Scalability

Encourage implementation patterns that support future project expansion.

---

# General Coding Philosophy

The implementation of EVision Telangana follows a **clean, simple, modular, and maintainable** coding philosophy.

The project is an academic decision support system developed by a four-member team within a limited development timeline. Therefore, implementation should prioritize clarity, consistency, and correctness over unnecessary complexity.

Every implementation decision should align with the approved System Architecture, Repository Structure, API Specification, Database Schema, and Data Contracts.

---

## Simplicity First

Code should solve the problem using the simplest practical solution.

Developers should avoid unnecessary abstractions, excessive design patterns, or premature optimization.

Readable code is preferred over clever code.

---

## Single Responsibility Principle

Every module, class, and function should have one clearly defined responsibility.

Examples include:

- API routes handle HTTP communication.
- Services contain business logic.
- Repositories manage database access.
- Machine learning modules perform inference.
- Utility modules provide reusable helper functions.

Responsibilities should never overlap across layers.

---

## Separation of Concerns

Application layers should remain independent.

Implementation should respect the approved layered architecture.

Examples include:

- API routes should not contain database queries.
- Machine learning models should not generate HTTP responses.
- Database models should not implement business logic.
- Frontend components should not perform backend processing.

Each layer communicates only through its defined interfaces.

---

## Modularity

Implementation should be divided into small, reusable modules.

Large files should be avoided whenever practical.

Each module should represent one logical feature or responsibility.

---

## Readability Over Cleverness

Code should be understandable by every project contributor.

Avoid:

- Deeply nested logic
- Overly compact expressions
- Excessive chaining
- Unclear variable names
- Hidden side effects

Future maintainability takes priority over minimizing lines of code.

---

## Explicit Over Implicit

Implementation should make behavior obvious.

Examples include:

- Use descriptive variable names.
- Pass explicit function parameters.
- Return predictable values.
- Avoid hidden dependencies.
- Avoid unexpected global state.

Explicit code improves debugging and collaboration.

---

## Consistency Over Personal Preference

Personal coding styles should not override the approved project conventions.

All contributors should follow the same:

- Naming conventions
- Formatting rules
- File organization
- Documentation style
- Error handling approach

Consistency across the repository is more important than individual preferences.

---

## Reusability

Reusable logic should be extracted into shared modules whenever appropriate.

Avoid duplicating:

- Validation logic
- Database queries
- Utility functions
- Formatting functions
- Common calculations

Shared functionality should exist in one authoritative implementation.

---

## Predictable Behavior

Functions should produce consistent outputs for identical inputs whenever possible.

Avoid implementations that rely on:

- Hidden global variables
- Uncontrolled side effects
- Unpredictable execution order

Deterministic behavior improves testing and debugging.

---

## Defensive Programming

Implementation should validate inputs before processing.

Functions should:

- Verify required parameters.
- Handle invalid data gracefully.
- Return meaningful errors.
- Avoid unexpected crashes.

Assume that external input may be invalid.

---

## Fail Gracefully

Unexpected situations should be handled through structured exceptions rather than application crashes.

Errors should:

- Be logged.
- Provide meaningful messages.
- Avoid exposing internal implementation details.
- Return standardized API responses where applicable.

---

## Keep Business Logic Centralized

Business logic belongs in the Service Layer.

Avoid placing business rules inside:

- API routes
- SQLModel models
- Database repositories
- Frontend components

Centralizing business logic improves maintainability and prevents duplication.

---

## Maintain API Contract Integrity

Implementation must strictly follow the approved API Specification.

Developers should not introduce undocumented:

- Endpoints
- Response fields
- Request fields
- Status codes
- Error structures

Any contract changes require corresponding updates to the API Specification.

---

## Maintain Database Contract Integrity

Database implementation must remain consistent with the approved Database Schema.

Developers should not introduce undocumented:

- Tables
- Columns
- Relationships
- Primary keys
- Foreign keys

Schema changes require formal updates to the Database Schema document.

---

## Preserve Data Contract Consistency

Generated datasets and machine learning artifacts must conform to the approved Data Contracts.

Data formats should remain deterministic and reproducible.

Processed datasets should never be modified manually.

---

## Prefer Composition Over Duplication

Shared functionality should be composed through reusable modules rather than copied across the codebase.

Code duplication increases maintenance effort and inconsistency.

---

## Continuous Refactoring

Developers are encouraged to improve code quality while implementing new functionality.

Refactoring should:

- Preserve behavior.
- Improve readability.
- Reduce duplication.
- Simplify implementation.

Large architectural changes should be discussed with the team before implementation.

---

## Documentation as Part of Development

Documentation should evolve alongside implementation.

When significant implementation changes occur, corresponding documentation should also be updated where applicable.

Documentation should never become outdated relative to the codebase.

---

## Team-Oriented Development

Implementation should prioritize collaboration over individual optimization.

Every contributor should write code that:

- Can be understood by the rest of the team.
- Follows approved conventions.
- Minimizes merge conflicts.
- Supports future maintenance.

The project should appear as though it was written by a single development team rather than multiple independent contributors.

# Core Development Principles

The following principles govern implementation across the entire EVision Telangana codebase.

These principles complement the project's coding philosophy by defining practical expectations that every contributor should follow during development.

---

## Build for Maintainability

Code should be written with future maintenance in mind.

Implementation should prioritize:

- Clear structure
- Logical organization
- Consistent formatting
- Minimal duplication

Code is expected to be read far more often than it is written.

---

## Follow the Approved Architecture

Every implementation must respect the approved layered architecture.

Dependencies should flow only in the approved direction.

```text
Frontend
    │
    ▼
API Layer
    │
    ▼
Service Layer
    │
    ▼
Repository Layer
    │
    ▼
Database
```

Layers should never bypass intermediate layers.

For example:

- API routes should not directly query the database.
- Frontend components should not communicate with SQLite.
- Services should not manipulate UI state.

---

## Keep Modules Small

Each module should represent one logical responsibility.

As a general guideline:

- One router per API resource.
- One service per business domain.
- One repository per database entity.
- One SQLModel class per table.

Large "utility" modules that collect unrelated functionality should be avoided.

---

## Minimize Coupling

Components should depend on abstractions and public interfaces rather than implementation details.

Avoid tightly coupling modules through:

- Shared mutable state
- Circular imports
- Cross-layer dependencies
- Hardcoded implementation assumptions

Loose coupling improves maintainability and testing.

---

## Maximize Cohesion

Related functionality should remain together.

Examples:

- Prediction logic belongs inside the Prediction Service.
- Analytics logic belongs inside the Analytics module.
- Recommendation calculations belong inside the Decision Engine.

Unrelated functionality should never share the same module.

---

## Prefer Configuration Over Hardcoding

Values that may reasonably change should be configurable.

Examples include:

- File paths
- API keys
- Database locations
- Model filenames
- Environment-specific settings

These values should be loaded through the project's configuration system rather than embedded directly in source code.

---

## Avoid Magic Values

Literal values with special meaning should be replaced with descriptive constants.

Instead of:

```python
if priority_score > 80:
```

Prefer:

```python
HIGH_PRIORITY_THRESHOLD = 80

if priority_score > HIGH_PRIORITY_THRESHOLD:
```

Named constants improve readability and simplify maintenance.

---

## Write Deterministic Code

Identical inputs should produce identical outputs whenever possible.

Implementation should avoid:

- Hidden randomness
- Uncontrolled global state
- Non-deterministic side effects

This is especially important for:

- Data preprocessing
- Machine learning pipelines
- Recommendation generation

---

## Validate Early

Input validation should occur as close to the source as possible.

Typical validation locations include:

- API request validation
- Dataset validation
- Configuration loading
- User input processing

Invalid data should be rejected before business logic executes.

---

## Keep Functions Focused

Functions should perform one logical task.

Functions that become excessively long or perform multiple unrelated operations should be refactored into smaller helper functions.

---

## Avoid Deep Nesting

Nested conditional blocks reduce readability.

Prefer:

- Early returns
- Guard clauses
- Helper functions

Over deeply nested `if` statements.

---

## Do Not Repeat Yourself (DRY)

Common functionality should be implemented once and reused.

Examples include:

- Validation helpers
- Response builders
- Database utilities
- Formatting helpers

Copying code between modules should be avoided.

---

## Prefer Explicit Error Handling

Expected failure scenarios should be handled explicitly.

Avoid empty exception handlers or silently ignoring errors.

Every exception should either:

- Be handled appropriately, or
- Be propagated with additional context.

---

## Protect Sensitive Information

Sensitive information must never appear in source code.

Examples include:

- API keys
- Tokens
- Secrets
- Passwords
- Database credentials

These values belong in environment variables and local configuration files that are excluded from version control.

---

## Write Testable Code

Implementation should be designed so that units can be tested independently.

Avoid unnecessary dependencies on:

- Global variables
- File system state
- External services
- User interfaces

Clear interfaces improve automated testing.

---

## Optimize Only When Necessary

Correctness and readability take priority over premature optimization.

Performance improvements should be introduced only after identifying genuine bottlenecks.

Unnecessary micro-optimizations should be avoided.

---

## Keep Dependencies Minimal

Only approved libraries from the Final Tech Stack should be introduced into the project.

New dependencies should only be added when they provide clear value and have been agreed upon by the team.

---

## Respect Existing Contracts

Implementation must remain consistent with the approved:

- API Specification
- Database Schema
- Data Contracts
- Repository Structure

Developers should implement within these contracts rather than modifying them during coding.

---

## Continuous Integration Mindset

Code should remain in a mergeable state throughout development.

Developers should:

- Commit logical changes frequently.
- Keep feature branches focused.
- Ensure code builds successfully.
- Resolve issues before creating Pull Requests.

This aligns implementation with the approved Git Workflow.

---

## Prioritize Team Readability

The primary audience for the code is the project team.

Every implementation should be understandable by any contributor without requiring extensive explanation.

Readable, well-structured code is considered higher quality than overly compact or overly complex implementations.

# Python Coding Standards

Python is the primary implementation language for the backend, machine learning pipeline, data processing pipeline, and Decision Engine.

All Python code should follow consistent conventions to maximize readability, maintainability, and collaboration.

The project targets **Python 3.12+** as defined in the approved technology stack.

---

# Python Style Guide

The project follows:

- PEP 8 for code style
- PEP 257 for docstrings
- PEP 484 for type hints

Ruff serves as the primary formatter, linter, and import organizer.

All Python code should pass Ruff checks before being committed.

---

# Indentation

Use **4 spaces** for indentation.

Tabs should never be used.

Example:

```python
def predict():
    return "Prediction"
```

---

# Maximum Line Length

Recommended maximum line length:

```text
88 characters
```

This aligns with Ruff's default formatting behavior.

Long expressions should be wrapped naturally rather than using backslashes whenever possible.

---

# Blank Lines

Use blank lines consistently to improve readability.

Recommended spacing:

- Two blank lines between top-level classes and functions.
- One blank line between related methods.
- Separate logical sections inside long functions with a single blank line.

Avoid excessive empty lines.

---

# Variable Naming

Variables should use:

```text
snake_case
```

Examples:

```python
district_name

prediction_result

priority_score

charging_station_count
```

Avoid unclear abbreviations.

Instead of:

```python
ds
```

Prefer:

```python
district_summary
```

---

# Constants

Constants should use:

```text
UPPER_SNAKE_CASE
```

Examples:

```python
API_VERSION

DEFAULT_PAGE_SIZE

HIGH_PRIORITY_THRESHOLD
```

Constants should be declared near the top of the module whenever practical.

---

# Function Naming

Functions should use descriptive snake_case names.

Examples:

```python
load_dataset()

generate_predictions()

calculate_priority_score()

get_district_profile()
```

Avoid generic names such as:

```python
run()

process()

execute()

handle()
```

unless the surrounding context makes their purpose immediately obvious.

---

# Class Naming

Classes should use:

```text
PascalCase
```

Examples:

```python
PredictionService

DistrictRepository

RecommendationEngine

HistoricalDemandProcessor
```

Class names should be nouns representing a logical entity.

---

# Module Naming

Python module filenames should use:

```text
snake_case.py
```

Examples:

```text
prediction_service.py

district_repository.py

data_loader.py
```

Avoid:

```text
PredictionService.py

Prediction-Service.py

predictionService.py
```

---

# Package Naming

Package names should use:

```text
lowercase
```

Examples:

```text
services

repositories

schemas

models
```

Avoid uppercase package names.

---

# Function Size

Functions should remain focused on one responsibility.

Recommended guideline:

- Prefer fewer than 40 lines.
- Consider refactoring functions that exceed approximately 60 lines.

Large functions usually indicate multiple responsibilities.

---

# Parameter Count

Functions should accept only the parameters they genuinely require.

As a general guideline:

- Prefer five or fewer parameters.
- Consider grouping related parameters into a model or configuration object when appropriate.

---

# Return Values

Functions should return consistent and predictable values.

Avoid returning different data types depending on execution path.

Instead of:

```python
return False
```

or

```python
return data
```

Prefer raising an appropriate exception for error conditions and returning a single well-defined type on success.

---

# Type Hints

Public functions should include type hints.

Example:

```python
def get_prediction(district: str) -> float:
    ...
```

Type hints improve readability, tooling support, and maintainability.

---

# Docstrings

Public modules, classes, and functions should include concise docstrings.

Use triple double quotes.

Example:

```python
def load_dataset(path: Path) -> pd.DataFrame:
    """Load the processed dataset from disk."""
```

Docstrings should describe intent rather than restating obvious implementation details.

---

# Imports

Imports should appear at the top of each module.

Import groups should be ordered as follows:

1. Standard library
2. Third-party packages
3. Local project modules

Separate groups using a single blank line.

Example:

```python
from pathlib import Path

import pandas as pd
from fastapi import APIRouter

from app.services.prediction_service import PredictionService
```

Wildcard imports are prohibited.

---

# List Comprehensions

Use list comprehensions only when they improve readability.

Avoid deeply nested comprehensions.

Prefer explicit loops for complex transformations.

---

# Boolean Expressions

Write boolean expressions clearly.

Prefer:

```python
if district_exists:
```

Instead of:

```python
if district_exists == True:
```

---

# Context Managers

Use context managers for resources that require cleanup.

Examples include:

- Files
- Database sessions
- Temporary resources

Example:

```python
with open(file_path) as file:
    data = file.read()
```

---

# Exceptions

Catch only exceptions that can be handled meaningfully.

Avoid:

```python
except:
```

Prefer:

```python
except FileNotFoundError:
```

or another specific exception type.

---

# Logging

Use the standard logging module instead of print statements.

Example:

```python
logger.info("Predictions generated successfully.")
```

Debugging print statements should be removed before committing code.

---

# Mutable Default Arguments

Never use mutable objects as default parameter values.

Avoid:

```python
def process(items=[]):
```

Prefer:

```python
def process(items: list | None = None):
    if items is None:
        items = []
```

---

# Global Variables

Avoid mutable global variables.

Shared application state should be managed through appropriate services or configuration modules.

---

# Magic Numbers

Replace unexplained numeric values with named constants.

Instead of:

```python
if score > 80:
```

Prefer:

```python
HIGH_PRIORITY_THRESHOLD = 80

if score > HIGH_PRIORITY_THRESHOLD:
```

---

# Assertions

Assertions should only be used to verify internal assumptions during development.

They should not replace runtime validation of user input or external data.

---

# Deprecated Features

Avoid deprecated language features and outdated syntax.

Implementation should remain compatible with the approved Python version throughout the project.

---

# Code Formatting

All Python source files should be automatically formatted using Ruff before being committed.

Manual formatting should not override automated formatting unless absolutely necessary.

Formatting consistency takes precedence over personal style preferences.

# JavaScript / React Coding Standards

JavaScript is used for implementing the React frontend of EVision Telangana.

All frontend code should follow consistent conventions to ensure readability, maintainability, and compatibility with the approved technology stack.

The project uses **React**, **Vite**, **JavaScript (ES2023)**, and **Tailwind CSS**.

---

# JavaScript Style Guide

The project follows modern ECMAScript (ES2023) standards.

Formatting should be handled automatically using **Prettier**.

Developers should avoid manually formatting code that conflicts with the project's formatter configuration.

---

# Indentation

Use **2 spaces** for indentation.

Tabs should never be used.

Example:

```javascript
function App() {
  return <Dashboard />;
}
```

---

# Maximum Line Length

Recommended maximum line length:

```text
100 characters
```

Long expressions should be wrapped naturally for readability.

---

# Variable Naming

Variables should use:

```text
camelCase
```

Examples:

```javascript
districtName;

priorityScore;

selectedDistrict;

predictionResults;
```

Avoid unclear abbreviations.

Instead of:

```javascript
res;
```

Prefer:

```javascript
predictionResponse;
```

---

# Constants

Constants should use:

```text
UPPER_SNAKE_CASE
```

Examples:

```javascript
API_BASE_URL;

DEFAULT_ZOOM_LEVEL;

HIGH_PRIORITY_COLOR;
```

Constants should be declared near the top of the module whenever practical.

---

# Function Naming

Functions should use descriptive camelCase names.

Examples:

```javascript
fetchDistricts();

loadDashboard();

generateMapMarkers();

handleDistrictSelection();
```

Avoid generic names such as:

```javascript
run();

doStuff();

process();
```

unless their purpose is immediately clear from context.

---

# React Component Naming

React component names should use:

```text
PascalCase
```

Examples:

```javascript
Dashboard;

DistrictCard;

PredictionTable;

RecommendationPanel;

InteractiveMap;
```

Each component file should export one primary component.

---

# File Naming

React component files should use:

```text
PascalCase.jsx
```

Examples:

```text
Dashboard.jsx

DistrictDetails.jsx

RecommendationTable.jsx
```

Utility modules should use:

```text
camelCase.js
```

Examples:

```text
apiClient.js

dateUtils.js

mapHelpers.js
```

---

# Component Design

Each component should have one clearly defined responsibility.

Large components should be divided into smaller reusable components.

Avoid components that simultaneously:

- Fetch data
- Manage complex state
- Render multiple unrelated sections
- Perform business logic

---

# Functional Components

Use functional components exclusively.

Do not use class-based React components.

Example:

```javascript
function Dashboard() {
  return <div>Dashboard</div>;
}
```

---

# Hooks

React Hooks should always follow the official Rules of Hooks.

Hooks must:

- Be called only at the top level.
- Never be called inside loops.
- Never be called inside conditions.
- Never be called inside nested functions.

---

# State Management

Use React state only where necessary.

Prefer:

- Local component state
- Props
- Context (if required)

Avoid unnecessary duplication of state.

Derived values should be computed rather than stored.

---

# Props

Component props should be:

- Clearly named
- Minimal
- Predictable

Avoid passing large objects when only a few values are required.

Prefer:

```javascript
<DistrictCard
  districtName={district.name}
  priorityScore={district.priorityScore}
/>
```

instead of passing an entire object unnecessarily.

---

# Event Handler Naming

Event handlers should begin with:

```text
handle
```

Examples:

```javascript
handleSubmit();

handleSearch();

handleDistrictChange();

handleMapClick();
```

---

# API Calls

All backend communication should be centralized through the approved API client.

Components should never directly construct API URLs.

Avoid:

```javascript
fetch("http://localhost:8000/api/v1/dashboard");
```

Prefer:

```javascript
apiClient.getDashboardOverview();
```

This improves maintainability and keeps API logic centralized.

---

# Async Programming

Use:

```javascript
async / await
```

instead of chained `.then()` calls whenever practical.

Example:

```javascript
const districts = await apiClient.getDistricts();
```

---

# Conditional Rendering

Prefer simple and readable conditional rendering.

Example:

```javascript
{
  loading && <Spinner />;
}
```

Avoid deeply nested ternary operators.

---

# Lists

Always provide stable keys when rendering lists.

Prefer unique identifiers whenever available.

Example:

```javascript
districts.map((district) => (
  <DistrictCard key={district.id} district={district} />
));
```

Avoid using array indexes as keys unless the list is static.

---

# Styling

Use Tailwind CSS utility classes consistently.

Avoid inline style objects unless absolutely necessary.

Prefer:

```jsx
<div className="rounded-lg bg-white p-4 shadow">
```

Instead of:

```jsx
<div style={{ padding: "16px" }}>
```

Reusable styling patterns should be extracted into reusable components where appropriate.

---

# Error Handling

Frontend components should gracefully handle API failures.

Users should receive informative messages instead of blank screens or console-only errors.

Errors should not expose backend implementation details.

---

# Logging

Use `console.log()` only during development.

Before committing code:

- Remove debugging statements.
- Keep only intentional warnings or errors when appropriate.

---

# Comments

Comments should explain **why** something exists rather than **what** the code is doing.

Avoid redundant comments.

Instead of:

```javascript
// Increment counter
count++;
```

Prefer comments that explain non-obvious decisions or implementation constraints.

---

# Code Formatting

All JavaScript, JSX, JSON, CSS, and Markdown files should be automatically formatted using Prettier before being committed.

Manual formatting should not conflict with the formatter configuration.

Consistent formatting across the frontend codebase takes precedence over personal coding preferences.

# Naming Conventions

Consistent naming conventions improve readability, maintainability, collaboration, and code navigation.

Every contributor should follow the approved naming standards across the entire project.

Naming should always prioritize clarity over brevity.

---

# General Principles

Names should be:

- Descriptive
- Consistent
- Predictable
- Easy to understand
- Free of unnecessary abbreviations

Good names reduce the need for comments.

---

# Variables

Variable names should clearly describe the stored value.

## Python

Use:

```text
snake_case
```

Examples:

```python
district_name

priority_score

predicted_demand

historical_average

charging_station_count
```

---

## JavaScript

Use:

```text
camelCase
```

Examples:

```javascript
districtName;

priorityScore;

selectedDistrict;

predictionResults;
```

---

# Constants

Constants should use:

```text
UPPER_SNAKE_CASE
```

Examples:

```text
API_VERSION

DEFAULT_PAGE_SIZE

MAX_UPLOAD_SIZE

HIGH_PRIORITY_THRESHOLD
```

Constants should represent values that are not expected to change during runtime.

---

# Functions

Function names should:

- Describe the performed action.
- Begin with a verb.
- Be concise but meaningful.

Python examples:

```python
load_dataset()

generate_predictions()

calculate_priority_score()

get_district_profile()

validate_request()
```

JavaScript examples:

```javascript
fetchDashboard();

loadDistricts();

handleSubmit();

calculateStatistics();
```

Avoid vague names such as:

```text
run

execute

process

handle

temp
```

unless their surrounding context makes the meaning obvious.

---

# Classes

Class names should use:

```text
PascalCase
```

Class names should represent nouns.

Examples:

```text
PredictionService

DistrictRepository

RecommendationEngine

AnalyticsService

HistoricalDemandProcessor
```

Avoid abbreviations unless they are universally recognized.

---

# React Components

Component names should use:

```text
PascalCase
```

Examples:

```text
Dashboard

DistrictCard

RecommendationTable

InteractiveMap

PredictionChart
```

Component names should describe the UI element they represent.

---

# SQLModel Models

Database models should use:

```text
PascalCase
```

Examples:

```text
District

ChargingStation

HistoricalDemand

DistrictPrediction

DistrictRecommendation
```

Model names should correspond directly to the logical database entities defined in the Database Schema.

---

# Pydantic Schemas

Schema names should clearly indicate their purpose.

Examples:

```text
DistrictResponse

PredictionRequest

RecommendationResponse

DashboardSummaryResponse

AssistantChatRequest
```

Common suffixes include:

- Request
- Response
- Create
- Update
- Base

---

# API Routers

Router modules should use descriptive snake_case filenames.

Examples:

```text
dashboard.py

districts.py

predictions.py

analytics.py

recommendations.py

assistant.py

health.py
```

These names should align with the approved REST resources.

---

# Services

Service classes should end with:

```text
Service
```

Examples:

```text
PredictionService

AnalyticsService

RecommendationService

DashboardService
```

---

# Repositories

Repository classes should end with:

```text
Repository
```

Examples:

```text
DistrictRepository

PredictionRepository

ChargingStationRepository
```

Repositories should represent database access only.

---

# Utility Modules

Utility modules should describe their functionality.

Examples:

```text
date_utils.py

geo_utils.py

response_helpers.py

validation.py
```

Avoid generic filenames such as:

```text
helpers.py

utils.py

common.py
```

unless the module genuinely contains closely related shared utilities.

---

# Exceptions

Custom exception classes should end with:

```text
Error
```

Examples:

```text
ValidationError

PredictionError

DatabaseError

RecommendationError
```

Exception names should clearly communicate the failure condition.

---

# Test Files

Test files should begin with:

```text
test_
```

Examples:

```text
test_predictions.py

test_dashboard.py

test_api.py

test_services.py
```

This ensures automatic test discovery.

---

# Environment Variables

Environment variables should use:

```text
UPPER_SNAKE_CASE
```

Examples:

```text
OPENAI_API_KEY

DATABASE_URL

API_HOST

API_PORT

LOG_LEVEL
```

Sensitive values should never appear directly in source code.

---

# Database Tables

Database table names should follow the approved Database Schema.

Use:

```text
lowercase_plural_snake_case
```

Examples:

```text
districts

charging_stations

historical_demand

district_predictions

district_recommendations
```

---

# Database Columns

Column names should use:

```text
snake_case
```

Examples:

```text
district_name

priority_score

predicted_demand

generated_at

reporting_month
```

---

# API Endpoints

Endpoint paths should remain consistent with the approved API Specification.

Examples:

```text
/api/v1/dashboard

/api/v1/districts

/api/v1/predictions

/api/v1/analytics

/api/v1/recommendations

/api/v1/assistant

/api/v1/health
```

Endpoint names should use lowercase letters and plural nouns where appropriate.

---

# Branch Names

Branch names should follow the approved Git Workflow.

Examples:

```text
feature/backend-api

feature/dashboard-ui

feature/model-training

docs/report

fix/api-validation
```

Branch names should remain concise and focused on a single task.

---

# Commit Messages

Commit messages should follow the approved commit convention.

Examples:

```text
feat: implement dashboard overview endpoint

fix: resolve prediction validation bug

docs: update coding standards

refactor: simplify analytics service

test: add recommendation API tests
```

Commit messages should describe **what changed**, not how much work was completed.

---

# File and Directory Consistency

Names should remain consistent across the project.

Examples include:

- Service class ↔ Service filename
- Repository ↔ Database entity
- Router ↔ API resource
- SQLModel ↔ Database table
- Schema ↔ API request/response model

Using consistent terminology throughout the repository reduces confusion and improves maintainability.

---

# Abbreviation Guidelines

Avoid abbreviations unless they are widely recognized.

Prefer:

```text
prediction_result
```

instead of:

```text
pred_res
```

Prefer:

```text
recommendation_service
```

instead of:

```text
rec_srv
```

Clear names are always preferred over shorter names.

---

# Reserved Terminology

The following terms should be used consistently throughout the project.

| Concept                            | Preferred Term         |
| ---------------------------------- | ---------------------- |
| Telangana district                 | district               |
| Charging demand forecast           | predicted_demand       |
| District ranking score             | priority_score         |
| Recommendation category            | priority_level         |
| Historical electricity consumption | demand_kwh             |
| Charging station total             | charging_station_count |
| Cluster identifier                 | cluster_id             |

These names should remain consistent across:

- Source code
- APIs
- Database schema
- Data contracts
- Documentation
- Machine learning outputs

Maintaining a single vocabulary across the entire project improves collaboration and minimizes ambiguity.

# File Naming Conventions

Consistent file naming improves project organization, discoverability, and collaboration.

Every source file should follow predictable naming conventions that align with the approved Repository Structure and technology stack.

File names should clearly communicate their purpose without requiring developers to inspect their contents.

---

# General Principles

All filenames should:

- Be descriptive.
- Be consistent across the project.
- Avoid unnecessary abbreviations.
- Use lowercase where appropriate.
- Avoid spaces.
- Avoid special characters.
- Use meaningful file extensions.

Examples:

```text
prediction_service.py

district_repository.py

Dashboard.jsx

apiClient.js
```

---

# Python Files

Python source files should use:

```text
snake_case.py
```

Examples:

```text
prediction_service.py

analytics_service.py

district_repository.py

response_helpers.py

database.py
```

Avoid:

```text
PredictionService.py

Prediction-Service.py

predictionService.py
```

---

# JavaScript Files

JavaScript utility files should use:

```text
camelCase.js
```

Examples:

```text
apiClient.js

dateUtils.js

mapHelpers.js

chartConfig.js
```

These files typically contain reusable frontend utilities.

---

# React Component Files

React component files should use:

```text
PascalCase.jsx
```

Examples:

```text
Dashboard.jsx

DistrictCard.jsx

PredictionTable.jsx

InteractiveMap.jsx

RecommendationPanel.jsx
```

Each component file should export one primary component.

---

# CSS Files

If custom CSS files are required beyond Tailwind CSS, filenames should use:

```text
kebab-case.css
```

Examples:

```text
dashboard-layout.css

map-controls.css
```

Component-specific styling should remain minimal and only be introduced when Tailwind utilities are insufficient.

---

# Configuration Files

Configuration files should retain their conventional names.

Examples:

```text
pyproject.toml

package.json

vite.config.js

tailwind.config.js

eslint.config.js

.env.example
```

These filenames should not be renamed.

---

# Environment Files

Environment files should follow standard conventions.

Examples:

```text
.env

.env.example

.env.local
```

Sensitive environment files should never be committed to version control.

Only `.env.example` should be tracked.

---

# API Router Files

Router files should match the corresponding API resource.

Examples:

```text
dashboard.py

districts.py

predictions.py

analytics.py

recommendations.py

assistant.py

health.py
```

Router filenames should remain consistent with the approved REST API.

---

# Service Files

Service modules should end with:

```text
_service.py
```

Examples:

```text
dashboard_service.py

prediction_service.py

analytics_service.py

recommendation_service.py
```

Each service file should implement one business domain.

---

# Repository Files

Repository modules should end with:

```text
_repository.py
```

Examples:

```text
district_repository.py

prediction_repository.py

charging_station_repository.py
```

Repository modules should contain database access logic only.

---

# SQLModel Files

Database model files should describe the represented entity.

Examples:

```text
district.py

charging_station.py

historical_demand.py

district_prediction.py

district_recommendation.py
```

Avoid combining multiple unrelated database models into a single file unless they are closely related.

---

# Schema Files

Pydantic schema modules should represent one API domain.

Examples:

```text
dashboard.py

district.py

prediction.py

recommendation.py

assistant.py
```

Request and response models for the same domain may reside within the same schema module.

---

# Utility Files

Utility modules should clearly describe their purpose.

Examples:

```text
validation.py

date_utils.py

geo_utils.py

response_helpers.py
```

Avoid overly generic filenames such as:

```text
helpers.py

utils.py

common.py
```

unless the contents are genuinely shared across the project.

---

# Test Files

Test files should begin with:

```text
test_
```

Examples:

```text
test_dashboard.py

test_predictions.py

test_recommendations.py

test_api.py
```

This naming convention supports automatic test discovery.

---

# Notebook Files

Jupyter Notebook filenames should use:

```text
snake_case.ipynb
```

Examples:

```text
data_exploration.ipynb

feature_engineering.ipynb

model_training.ipynb

model_evaluation.ipynb
```

Notebook names should reflect a single stage of experimentation.

---

# Dataset Files

Dataset filenames should follow the approved Data Contracts.

Examples:

```text
tgspdcl_ev_consumption.csv

tgnpdcl_ev_consumption.csv

tgredco_charging_stations.csv

master_dataset.csv

prediction_outputs.csv

recommendation_outputs.csv
```

Processed datasets should never receive manually created alternative names.

---

# Machine Learning Model Files

Serialized model artifacts should use descriptive filenames.

Examples:

```text
best_regression.joblib

kmeans.joblib
```

Model filenames should remain consistent with the Data Contracts.

---

# Documentation Files

Documentation files should use:

```text
Title Case.md
```

for Project Sources.

Examples:

```text
00 - Project Handbook.md

04 - System Architecture.md

10 - Coding Standards.md
```

Repository documentation outside the Project Sources may use conventional filenames such as:

```text
README.md

LICENSE

CONTRIBUTING.md
```

---

# Image Files

Project images should use:

```text
kebab-case.png
```

or

```text
kebab-case.svg
```

Examples:

```text
system-architecture.png

repository-structure.svg

workflow-diagram.png
```

Image filenames should describe the diagram or asset.

---

# Generated Output Files

Generated reports, evaluation summaries, and exported results should use descriptive filenames.

Examples:

```text
model_evaluation_report.json

feature_importance.csv

prediction_summary.csv
```

Generated filenames should remain deterministic whenever possible.

---

# Temporary Files

Temporary files should not be committed to the repository.

Examples include:

```text
temp.csv

backup.py

draft.ipynb

test_copy.py
```

These files should remain local or be removed before committing changes.

---

# File Naming Best Practices

All project files should follow these principles:

- One file should have one primary responsibility.
- Filenames should describe their contents.
- Avoid version numbers in filenames.
- Avoid personal initials in filenames.
- Avoid spaces and special characters (except approved Project Source documents).
- Follow technology-specific naming conventions consistently.
- Keep filenames concise while remaining descriptive.

Consistent file naming makes the repository easier to navigate, reduces ambiguity during collaboration, and supports long-term maintainability.

# Directory Conventions

The repository structure of EVision Telangana has been designed to support modular development, clear ownership, and long-term maintainability.

Every directory should have a well-defined purpose, and source files should only be placed in their appropriate locations.

Developers should follow the approved Repository Structure when creating new files or modules.

---

# General Principles

Directories should:

- Represent one logical responsibility.
- Have a clear purpose.
- Avoid overlapping responsibilities.
- Minimize unnecessary nesting.
- Remain consistent throughout the project.

New directories should only be introduced when justified by the project structure.

---

# Backend Directory Conventions

The backend follows a layered architecture.

Each directory corresponds to one application layer.

```text
backend/
```

contains all backend implementation.

---

## api/

Purpose:

Contains FastAPI route definitions.

Responsibilities:

- Define REST endpoints.
- Receive HTTP requests.
- Validate request data.
- Return API responses.
- Delegate business logic to services.

Should NOT contain:

- SQL queries
- Machine learning logic
- Business rules
- Data processing

---

## core/

Purpose:

Contains application-wide configuration and shared infrastructure.

Typical contents:

- Configuration management
- Environment variable loading
- Application settings
- Logging configuration
- Security utilities

This directory should remain lightweight.

---

## database/

Purpose:

Contains database infrastructure.

Typical contents:

- Database connection
- Session management
- Database initialization
- SQLModel metadata

Business logic should not be implemented here.

---

## models/

Purpose:

Contains SQLModel database models.

Responsibilities:

- Database table definitions
- Relationships
- ORM mappings

Models should not implement business logic.

---

## schemas/

Purpose:

Contains Pydantic request and response models.

Responsibilities:

- API validation
- Request schemas
- Response schemas
- Serialization

Database models and API schemas should remain separate.

---

## repositories/

Purpose:

Contains database access logic.

Responsibilities:

- CRUD operations
- Query execution
- Data retrieval
- Persistence

Repositories should not implement business rules.

---

## services/

Purpose:

Contains business logic.

Responsibilities:

- Application rules
- Analytics
- Predictions
- Recommendation generation
- AI orchestration

The Service Layer serves as the core of backend implementation.

---

## ml/

Purpose:

Contains machine learning runtime components.

Typical contents:

- Model loading
- Prediction services
- Feature preparation
- Inference utilities

Training notebooks and experiments should not be stored here.

---

## utils/

Purpose:

Contains reusable helper functions.

Examples:

- Date utilities
- Geographic calculations
- Validation helpers
- Formatting utilities

Utilities should remain generic and reusable.

---

# Frontend Directory Conventions

The frontend follows a component-based architecture.

```text
frontend/
```

contains all React application code.

---

## components/

Purpose:

Contains reusable UI components.

Examples:

- Cards
- Tables
- Charts
- Map components
- Navigation components

Components should remain presentation-focused whenever practical.

---

## pages/

Purpose:

Contains top-level application pages.

Examples:

- Dashboard
- District Details
- Analytics
- Recommendations

Pages compose reusable components into complete views.

---

## services/

Purpose:

Contains frontend API communication.

Responsibilities:

- Backend requests
- Response handling
- API client wrappers

API URLs should be centralized here.

---

## hooks/

Purpose:

Contains reusable React Hooks.

Examples:

- Data fetching hooks
- Custom UI hooks
- Shared application logic

Hooks should encapsulate reusable behavior.

---

## assets/

Purpose:

Stores static resources.

Examples:

- Images
- Icons
- Logos
- Fonts

Generated data should never be stored here.

---

## styles/

Purpose:

Contains global styling resources if required.

Most styling should be implemented using Tailwind CSS.

Custom CSS should remain minimal.

---

# Data Directory Conventions

The `data/` directory stores project datasets.

---

## raw/

Contains official datasets.

Characteristics:

- Read-only
- Never modified manually
- Source of truth

---

## processed/

Contains generated datasets.

Characteristics:

- Produced by preprocessing
- Regenerable
- Used throughout the application

Manual editing is prohibited.

---

## external/

Contains supporting datasets.

Examples:

- GeoJSON files
- Geographic reference data

These datasets support visualization and analysis.

---

# Models Directory

```text
models/
```

stores serialized machine learning artifacts.

Typical contents include:

- Regression model
- Clustering model
- Evaluation outputs

Training scripts should not be stored here.

---

# Notebooks Directory

```text
notebooks/
```

contains exploratory development.

Examples:

- Data exploration
- Feature engineering
- Model experimentation
- Evaluation

Production code should eventually be migrated into the appropriate Python packages.

---

# Scripts Directory

```text
scripts/
```

contains standalone executable utilities.

Examples:

- Database initialization
- Dataset preprocessing
- Model training
- Data import

Scripts should remain independent of application runtime.

---

# Tests Directory

```text
tests/
```

contains automated tests.

Subdirectories should mirror the project structure.

Example:

```text
tests/
├── api/
├── services/
├── repositories/
├── ml/
└── utils/
```

This organization simplifies navigation and test maintenance.

---

# Documentation Directory

Project documentation should remain organized and separated from source code.

Examples include:

```text
docs/

Project Sources/

reports/
```

Generated reports should not be mixed with implementation code.

---

# Generated Files

Generated outputs should remain inside their designated directories.

Examples:

```text
models/

data/processed/

models/evaluation/
```

Generated files should not be manually edited.

---

# Temporary Files

Temporary development files should never become part of the repository.

Examples include:

- Scratch notebooks
- Backup files
- Exported datasets
- Personal experiments

These files should remain local or be removed before committing.

---

# Directory Depth

Avoid excessive directory nesting.

As a general guideline:

- Prefer no more than three or four levels of nesting.
- Create additional directories only when they improve organization.
- Avoid deeply nested structures that reduce discoverability.

---

# One Responsibility Per Directory

Every directory should have one clearly defined purpose.

Avoid combining unrelated responsibilities.

Examples:

Good:

```text
services/
repositories/
schemas/
models/
```

Avoid:

```text
misc/
common/
others/
```

unless their contents genuinely share a common responsibility.

---

# Consistent Organization

Equivalent functionality should be organized consistently across the repository.

For example:

- Every API resource should have a corresponding router.
- Every database entity should have a corresponding model and repository.
- Every business domain should have a corresponding service.
- Every major feature should have corresponding tests.

Maintaining parallel directory structures improves navigation and reduces development errors.

---

# Directory Creation Guidelines

Before introducing a new directory, developers should consider:

- Does an appropriate directory already exist?
- Does the new directory represent a distinct responsibility?
- Will multiple files belong here?
- Does it improve repository organization?

Avoid creating directories for a single file unless future growth is expected.

---

# Long-Term Maintainability

Directory organization should remain stable throughout the project lifecycle.

As the codebase grows, new files should integrate into the existing structure rather than introducing alternative organizational patterns.

A predictable directory structure improves onboarding, simplifies code reviews, and ensures the repository remains easy to navigate for every contributor.

# Function Design Standards

Functions are the fundamental building blocks of the EVision Telangana codebase.

Well-designed functions improve readability, maintainability, testability, and code reuse.

Every function should perform one clearly defined responsibility and remain easy to understand.

---

# General Principles

Functions should be:

- Small
- Focused
- Predictable
- Reusable
- Well documented
- Easy to test

A reader should understand a function's purpose from its name and signature alone.

---

# Single Responsibility

Each function should perform one logical task.

Good examples:

- Load a dataset
- Validate an API request
- Calculate a priority score
- Retrieve district information
- Generate predictions

Avoid combining unrelated responsibilities into a single function.

Instead of:

```python
def process_data():
```

Prefer:

```python
load_dataset()

clean_dataset()

generate_predictions()

save_predictions()
```

---

# Function Length

Functions should remain concise.

Recommended guideline:

- Prefer fewer than 40 lines.
- Consider refactoring functions that exceed approximately 60 lines.

Large functions usually indicate multiple responsibilities.

---

# Descriptive Names

Function names should clearly describe the performed action.

Functions should begin with verbs.

Examples:

```python
load_dataset()

calculate_priority_score()

generate_recommendations()

fetch_dashboard_summary()

validate_prediction_request()
```

Avoid vague names such as:

```python
run()

execute()

process()

handle()
```

unless their context makes the meaning immediately obvious.

---

# Clear Parameters

Functions should accept only the parameters they genuinely require.

Avoid long parameter lists.

Instead of:

```python
calculate_score(a, b, c, d, e, f, g)
```

Prefer grouping related information into structured objects or models where appropriate.

---

# Type Hints

Public functions should include complete type hints.

Example:

```python
def calculate_priority_score(
    predicted_demand: float,
    charging_station_count: int,
) -> float:
    ...
```

Type hints improve tooling support and readability.

---

# Return Values

Functions should return one well-defined type whenever practical.

Avoid inconsistent return values such as:

```python
False
```

or

```python
list
```

depending on execution path.

Use exceptions for error conditions instead of returning sentinel values.

---

# Minimize Side Effects

Functions should avoid modifying unrelated application state.

Prefer:

- Returning values
- Receiving explicit parameters

Instead of relying on hidden global variables.

---

# Early Returns

Use guard clauses to simplify control flow.

Prefer:

```python
if district is None:
    raise ValueError("District is required")

return calculate_prediction(district)
```

instead of deeply nested conditional statements.

---

# Avoid Deep Nesting

Nested loops and conditional blocks reduce readability.

If nesting exceeds two or three levels, consider:

- Helper functions
- Guard clauses
- Smaller functions

---

# Pure Functions

Whenever practical, functions should behave as pure functions.

Pure functions:

- Produce deterministic outputs.
- Do not modify external state.
- Depend only on provided inputs.

Pure functions are easier to test and debug.

---

# Validation Responsibilities

Functions should validate their own required inputs when appropriate.

Validation should occur before performing expensive processing.

Invalid inputs should produce meaningful exceptions.

---

# Avoid Hidden Dependencies

Functions should receive required dependencies explicitly.

Avoid relying on:

- Global state
- Singleton objects
- Implicit configuration

Explicit dependencies improve readability and testability.

---

# Exception Handling

Functions should either:

- Handle expected exceptions appropriately, or
- Propagate exceptions with additional context.

Avoid suppressing exceptions silently.

---

# Logging

Functions should log significant events when appropriate.

Examples include:

- Long-running operations
- External API failures
- Model loading
- Database initialization

Routine helper functions generally do not require logging.

---

# Reusability

Common functionality should be extracted into reusable helper functions.

Avoid duplicating:

- Validation logic
- Formatting logic
- Database query construction
- Mathematical calculations

One implementation should serve all consumers.

---

# Documentation

Public functions should include concise docstrings describing:

- Purpose
- Parameters
- Return value
- Raised exceptions (when applicable)

Docstrings should explain intent rather than implementation.

---

# Default Parameters

Default parameter values should be immutable.

Avoid:

```python
def add_item(items=[]):
```

Prefer:

```python
def add_item(items: list | None = None):
    if items is None:
        items = []
```

---

# Async Functions

Only use asynchronous functions when performing asynchronous operations such as:

- HTTP requests
- Database operations (if asynchronous)
- File I/O (when appropriate)

CPU-bound computations should remain synchronous unless parallel processing is intentionally introduced.

---

# Avoid Duplicate Logic

If similar code appears in multiple functions, extract the shared behavior into a reusable helper.

Duplicated logic increases maintenance effort and inconsistency.

---

# Function Organization

Within a module, functions should generally appear in the following order:

1. Public functions
2. Internal helper functions
3. Private utility functions

Related functions should be grouped together logically.

---

# Testing Expectations

Functions should be designed for independent unit testing.

A well-designed function should:

- Produce deterministic outputs.
- Avoid unnecessary external dependencies.
- Be easy to mock where required.
- Have clearly defined inputs and outputs.

Complex functions should be covered by automated tests.

---

# Function Review Checklist

Before committing code, verify that each function:

- Has one clearly defined responsibility.
- Has a descriptive name.
- Accepts only necessary parameters.
- Returns predictable results.
- Includes type hints where applicable.
- Includes a docstring if public.
- Avoids unnecessary side effects.
- Handles errors appropriately.
- Is easy to understand.
- Can be tested independently.

Following these standards ensures that functions remain modular, reusable, maintainable, and consistent throughout the EVision Telangana codebase.

# Class Design Standards

Classes encapsulate related data and behavior into reusable, maintainable components.

The EVision Telangana project uses classes primarily for services, repositories, SQLModel models, Pydantic schemas, and selected utility components.

Every class should have a clearly defined purpose and should remain consistent with the approved layered architecture.

---

# General Principles

Classes should be:

- Focused
- Cohesive
- Reusable
- Easy to understand
- Easy to test
- Well documented

Each class should represent one logical concept within the system.

---

# Single Responsibility

A class should have one primary responsibility.

Examples include:

- Managing predictions
- Accessing district data
- Calculating recommendations
- Loading machine learning models

Avoid classes that perform multiple unrelated tasks.

Instead of:

```text
PredictionManager
```

handling predictions, analytics, database access, and API responses,

prefer:

```text
PredictionService

AnalyticsService

PredictionRepository
```

each with a single responsibility.

---

# Class Naming

Class names should:

- Use PascalCase.
- Be nouns.
- Clearly describe their purpose.

Examples:

```python
PredictionService

DistrictRepository

RecommendationEngine

HistoricalDemandProcessor

DashboardService
```

Avoid vague names such as:

```text
Manager

Handler

Processor

Utility
```

unless the name accurately reflects the class's responsibility.

---

# Keep Classes Small

Classes should remain reasonably small and focused.

Large classes usually indicate multiple responsibilities and should be refactored into smaller collaborating classes.

---

# High Cohesion

Methods within a class should be closely related.

For example:

A `PredictionService` should contain prediction-related operations only.

It should not also:

- Access unrelated APIs
- Generate charts
- Manage authentication

---

# Low Coupling

Classes should minimize dependencies on other classes.

Dependencies should be explicit rather than hidden.

Loose coupling improves:

- Testability
- Maintainability
- Reusability

---

# Constructor Responsibilities

Constructors should perform lightweight initialization only.

Avoid expensive operations such as:

- Database queries
- Model training
- File loading
- Network requests

Heavy initialization should occur through dedicated methods.

---

# Dependency Injection

Dependencies should be provided explicitly.

Example:

```python
class PredictionService:
    def __init__(self, repository: PredictionRepository):
        self.repository = repository
```

Avoid constructing dependencies internally whenever practical.

---

# Instance Variables

Instance variables should:

- Be initialized in the constructor.
- Have descriptive names.
- Represent persistent object state.

Avoid dynamically creating attributes outside the constructor.

---

# Public and Private Methods

Public methods define the class interface.

Internal helper methods should be treated as private using a leading underscore.

Example:

```python
class RecommendationService:
    def generate(self):
        ...

    def _calculate_score(self):
        ...
```

Private methods should support public behavior rather than becoming independent APIs.

---

# Method Design

Methods should follow the approved Function Design Standards.

Each method should:

- Perform one responsibility.
- Have descriptive names.
- Accept minimal parameters.
- Return predictable results.

Very large methods should be decomposed into helper methods.

---

# Class Documentation

Public classes should include concise docstrings describing their purpose.

Example:

```python
class PredictionService:
    """Generates charging demand predictions for Telangana districts."""
```

Documentation should explain the class's responsibility rather than implementation details.

---

# SQLModel Classes

SQLModel classes should represent database entities only.

They should contain:

- Field definitions
- Relationships
- Database metadata

They should not contain:

- Business logic
- Validation workflows
- Analytics
- API behavior

Business rules belong in the Service Layer.

---

# Pydantic Schemas

Pydantic schema classes should represent API request and response structures only.

They should remain independent of SQLModel implementations.

Avoid embedding business logic inside schemas.

---

# Service Classes

Service classes implement business logic.

Responsibilities include:

- Prediction generation
- Recommendation calculation
- Dashboard aggregation
- Analytics processing
- AI orchestration

Services should never directly expose HTTP behavior.

---

# Repository Classes

Repository classes manage data persistence.

Responsibilities include:

- CRUD operations
- Database queries
- Transaction management
- Data retrieval

Repositories should not implement business rules.

---

# Utility Classes

Utility classes should only be introduced when object-oriented organization clearly improves readability.

Stateless helper functions should generally remain as standalone functions rather than being wrapped inside utility classes unnecessarily.

---

# Inheritance

Inheritance should be used sparingly.

Prefer composition whenever practical.

Deep inheritance hierarchies reduce readability and increase maintenance complexity.

---

# Composition

Favor composing small collaborating classes.

Example:

```text
RecommendationService
        │
        ├── PredictionRepository
        ├── AnalyticsService
        └── DistrictRepository
```

Composition provides greater flexibility than inheritance.

---

# Mutable State

Classes should minimize mutable internal state.

Where possible:

- Compute values when needed.
- Keep objects predictable.
- Avoid unnecessary state changes.

This simplifies debugging and testing.

---

# Error Handling

Classes should raise meaningful exceptions when operations fail.

They should not silently ignore errors.

Exception handling responsibilities should remain consistent with the project's Error Handling Standards.

---

# Logging

Classes should log significant operations such as:

- Model loading
- Recommendation generation
- Database initialization
- External API failures

Routine getter methods generally do not require logging.

---

# Testing Expectations

Classes should be easy to instantiate and test independently.

Dependencies should be mockable.

Business logic should be isolated from infrastructure concerns whenever possible.

---

# Class Organization

Within a class, members should generally appear in the following order:

1. Class docstring
2. Class constants
3. Constructor
4. Public methods
5. Protected/private helper methods

This organization improves readability and consistency.

---

# Class Review Checklist

Before committing code, verify that each class:

- Has one clearly defined responsibility.
- Uses a descriptive PascalCase name.
- Maintains high cohesion.
- Minimizes coupling.
- Accepts dependencies explicitly.
- Keeps constructors lightweight.
- Separates business logic from infrastructure.
- Includes appropriate documentation.
- Is easy to test.
- Follows the approved architecture.

Following these standards ensures that classes remain modular, reusable, maintainable, and aligned with the layered architecture of EVision Telangana.

# API Coding Conventions

The backend APIs of EVision Telangana are implemented using **FastAPI** and follow RESTful design principles.

All API implementations must remain fully consistent with the approved API Specification.

The API layer is responsible only for HTTP communication and request orchestration. Business logic belongs exclusively in the Service Layer.

---

# General Principles

Every API endpoint should be:

- Predictable
- Consistent
- Stateless
- Well documented
- Easy to consume
- Easy to maintain

Endpoints should expose application functionality without revealing internal implementation details.

---

# RESTful Design

The project follows REST architectural principles.

Endpoints should represent resources rather than actions.

Examples:

```text
GET    /api/v1/districts

GET    /api/v1/predictions

GET    /api/v1/recommendations

POST   /api/v1/assistant
```

Avoid action-oriented endpoints such as:

```text
/getPredictions

/runRecommendation

/doAnalytics
```

---

# API Versioning

All endpoints should include the approved API version.

Example:

```text
/api/v1/
```

Version identifiers should remain consistent across the entire API.

---

# HTTP Methods

Use HTTP methods according to their intended purpose.

| Method | Purpose                                              |
| ------ | ---------------------------------------------------- |
| GET    | Retrieve data                                        |
| POST   | Submit requests or perform computations              |
| PUT    | Replace existing resources (if required in future)   |
| PATCH  | Partially update resources (if required in future)   |
| DELETE | Remove resources (not required for the approved MVP) |

Methods should not be repurposed for unrelated operations.

---

# Resource Naming

Endpoint paths should:

- Use lowercase letters.
- Use plural nouns where appropriate.
- Avoid verbs.
- Remain descriptive.

Examples:

```text
/api/v1/districts

/api/v1/dashboard

/api/v1/predictions

/api/v1/recommendations

/api/v1/analytics
```

---

# Request Validation

All incoming requests should be validated using Pydantic schemas.

Validation should occur before business logic executes.

API routes should never manually validate request payloads when schema validation can perform the task automatically.

---

# Response Models

Every endpoint should define an explicit response model.

Benefits include:

- Automatic validation
- Consistent serialization
- Accurate OpenAPI documentation
- Improved maintainability

Responses should never return raw SQLModel objects directly.

---

# Status Codes

Endpoints should return appropriate HTTP status codes.

Common examples include:

| Status Code | Meaning                          |
| ----------- | -------------------------------- |
| 200         | Successful request               |
| 201         | Resource created (if applicable) |
| 400         | Invalid request                  |
| 404         | Resource not found               |
| 422         | Validation error                 |
| 500         | Internal server error            |

Status codes should accurately represent the outcome of the request.

---

# Route Responsibilities

API routes should remain lightweight.

Responsibilities include:

- Receiving HTTP requests
- Validating input
- Calling service methods
- Returning responses

Routes should NOT contain:

- Business rules
- SQL queries
- Machine learning inference
- Data processing logic

---

# Dependency Injection

Use FastAPI dependency injection where appropriate.

Typical dependencies include:

- Database sessions
- Configuration
- Authentication (future scope)
- Shared services

Dependencies should be explicit and reusable.

---

# Error Responses

Errors should follow a consistent response structure.

Responses should:

- Clearly describe the error.
- Avoid exposing stack traces.
- Avoid revealing internal implementation details.

Clients should receive meaningful messages while internal debugging information remains in server logs.

---

# Response Consistency

Similar endpoints should return responses with consistent structure.

Examples:

- Collection endpoints return arrays.
- Detail endpoints return a single resource.
- Errors follow a standardized format.

Consistency improves frontend development and API usability.

---

# Pagination

The approved MVP does not require pagination due to the relatively small dataset.

If pagination is introduced in future versions, it should follow a consistent query parameter convention.

Example:

```text
?page=1&limit=20
```

---

# Query Parameters

Query parameters should be used for filtering and optional behavior.

Examples:

```text
/api/v1/districts?name=Hyderabad

/api/v1/predictions?forecast_period=2027
```

Required resource identifiers should remain part of the path whenever appropriate.

---

# Path Parameters

Use path parameters for identifying specific resources.

Example:

```text
/api/v1/districts/{district_id}
```

Path parameter names should be descriptive and consistent.

---

# JSON Responses

All API responses should use JSON.

Keys should follow:

```text
snake_case
```

to remain consistent with the backend, database schema, and data contracts.

---

# Serialization

Response serialization should be handled through Pydantic schemas.

Avoid manually constructing JSON responses unless necessary.

This ensures validation and consistent output formatting.

---

# Logging

Routes should log significant API events such as:

- Startup
- Shutdown
- Unexpected failures
- Long-running operations

Routine successful requests generally do not require detailed logging.

---

# OpenAPI Documentation

Every endpoint should include:

- Summary
- Description
- Response model
- Status codes

FastAPI's automatic documentation should accurately reflect the implemented API.

---

# Asynchronous Endpoints

Use asynchronous endpoints when performing asynchronous operations.

Examples include:

- External API communication
- Non-blocking database operations
- Long-running I/O tasks

Synchronous operations may remain standard functions where asynchronous execution provides no benefit.

---

# Security Considerations

Although authentication is outside the approved MVP scope, API implementations should:

- Validate all inputs.
- Sanitize user-provided data.
- Avoid exposing sensitive information.
- Reject malformed requests.

Future security enhancements should integrate cleanly into the existing API structure.

---

# Testing Expectations

Every endpoint should be testable independently.

Tests should verify:

- Successful responses
- Validation failures
- Invalid resource requests
- Expected status codes
- Response schema compliance

API behavior should remain deterministic and consistent with the approved API Specification.

---

# API Review Checklist

Before implementing or reviewing an endpoint, verify that it:

- Follows REST principles.
- Uses the correct HTTP method.
- Uses the approved endpoint path.
- Validates requests with Pydantic.
- Returns the correct response model.
- Uses appropriate HTTP status codes.
- Delegates business logic to the Service Layer.
- Does not access the database directly.
- Produces consistent JSON responses.
- Remains fully compliant with the approved API Specification.

Following these conventions ensures that the EVision Telangana API remains consistent, maintainable, scalable, and easy for both frontend developers and future contributors to use.

# SQLModel Conventions

EVision Telangana uses **SQLModel** as the Object Relational Mapper (ORM) for interacting with the SQLite database.

SQLModel provides a unified approach for defining database models using Python type annotations while integrating SQLAlchemy and Pydantic capabilities.

All SQLModel implementations must remain consistent with the approved Database Schema.

---

# General Principles

SQLModel models should:

- Represent database entities only.
- Remain lightweight.
- Mirror the approved database schema.
- Avoid business logic.
- Use clear relationships.
- Be easy to maintain.

Each database table should have one corresponding SQLModel class.

---

# One Model Per Table

Every logical database table should map to exactly one SQLModel model.

Examples:

| Database Table           | SQLModel Class         |
| ------------------------ | ---------------------- |
| districts                | District               |
| charging_stations        | ChargingStation        |
| historical_demand        | HistoricalDemand       |
| district_predictions     | DistrictPrediction     |
| district_analytics       | DistrictAnalytics      |
| district_recommendations | DistrictRecommendation |
| application_metadata     | ApplicationMetadata    |

Models should not combine unrelated tables.

---

# Class Naming

SQLModel classes should use:

```text
PascalCase
```

Examples:

```python
District

ChargingStation

HistoricalDemand

DistrictPrediction
```

Class names should directly reflect the logical entity represented by the database table.

---

# File Organization

Each SQLModel should reside in its own module whenever practical.

Examples:

```text
models/
├── district.py
├── charging_station.py
├── historical_demand.py
├── district_prediction.py
├── district_analytics.py
├── district_recommendation.py
└── application_metadata.py
```

This organization improves maintainability as the project grows.

---

# Table Names

Table names should follow the approved Database Schema.

Use:

```text
lowercase_plural_snake_case
```

Examples:

```python
__tablename__ = "districts"

__tablename__ = "charging_stations"
```

Table names should remain identical to those defined in the Database Schema.

---

# Column Naming

Database fields should use:

```text
snake_case
```

Examples:

```python
district_name

priority_score

generated_at

reporting_month
```

Field names should remain consistent with:

- Database Schema
- Data Contracts
- API Specification

---

# Primary Keys

Every table should define a single surrogate primary key.

Example:

```python
id: int | None = Field(default=None, primary_key=True)
```

Primary keys should:

- Be immutable.
- Auto-increment.
- Never be reused.

---

# Foreign Keys

Relationships should be represented explicitly using foreign keys.

Example:

```python
district_id: int = Field(
    foreign_key="districts.id"
)
```

Foreign keys should always reference valid parent tables.

---

# Relationships

SQLModel relationships should mirror the logical database relationships.

Example:

```python
charging_stations: list["ChargingStation"] = Relationship(
    back_populates="district"
)
```

Relationships should be kept simple and aligned with the approved schema.

Avoid introducing undocumented relationships.

---

# Field Definitions

Fields should include appropriate metadata where applicable.

Examples include:

- Primary keys
- Foreign keys
- Default values
- Nullable fields
- Indexes

Field definitions should remain descriptive and explicit.

---

# Type Annotations

Every field should use explicit Python type annotations.

Examples:

```python
district_name: str

priority_score: float

generated_at: datetime

organization: str | None
```

Avoid using ambiguous types whenever a more specific type is available.

---

# Nullable Fields

Optional database columns should be represented using optional type annotations.

Example:

```python
organization: str | None = None
```

Required fields should never be optional unless defined as nullable in the Database Schema.

---

# Default Values

Default values should only be used when appropriate.

Examples include:

- Creation timestamps
- Generated timestamps
- Default configuration values

Avoid assigning unnecessary defaults that may obscure missing data.

---

# Timestamp Fields

Timestamp fields should follow standardized names.

Examples:

```python
created_at

updated_at

generated_at
```

Timestamp generation should be handled consistently across all models.

---

# Validation

Basic structural validation may be implemented using SQLModel field constraints.

Examples include:

- Required fields
- Maximum string lengths
- Numeric constraints

Complex business validation belongs in the Service Layer rather than the database model.

---

# Business Logic

SQLModel classes should **not** contain business logic.

Avoid implementing:

- Prediction calculations
- Recommendation scoring
- Analytics
- Data preprocessing
- API response generation

Models should represent persistent data only.

---

# Database Independence

SQLModel models should avoid SQLite-specific implementation details whenever possible.

This supports future migration to PostgreSQL with minimal changes.

Implementation should rely on SQLModel abstractions rather than database-specific behavior.

---

# Import Organization

Model files should import only the dependencies they require.

Typical imports include:

```python
from datetime import datetime

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel
```

Avoid circular imports by using forward references where appropriate.

---

# Indexes

Frequently queried columns should define indexes consistent with the approved Database Schema.

Typical indexed fields include:

- district_name
- district_id
- reporting_month
- metadata_key

Indexes should only be added where justified by query patterns.

---

# Documentation

Public SQLModel classes should include concise docstrings.

Example:

```python
class District(SQLModel, table=True):
    """Represents a Telangana district."""
```

Documentation should explain the entity rather than implementation details.

---

# Testing Expectations

SQLModel implementations should be verified through automated tests.

Tests should confirm:

- Table creation
- Field definitions
- Relationships
- Constraints
- Default values
- CRUD compatibility

Model behavior should remain consistent with the approved Database Schema.

---

# SQLModel Review Checklist

Before committing a model, verify that it:

- Represents one database table.
- Matches the approved Database Schema.
- Uses PascalCase naming.
- Uses snake_case field names.
- Defines appropriate primary and foreign keys.
- Includes explicit type annotations.
- Uses relationships appropriately.
- Contains no business logic.
- Remains portable across supported database engines.
- Is easy to test and maintain.

Following these conventions ensures that SQLModel models remain clean, consistent, maintainable, and fully aligned with the approved database architecture.

# Error Handling Conventions

Robust error handling improves application reliability, simplifies debugging, and provides a better user experience.

The EVision Telangana project follows a structured approach to error handling across the backend, frontend, machine learning pipeline, and data processing pipeline.

Errors should be anticipated, handled gracefully, logged appropriately, and communicated consistently.

---

# General Principles

Error handling should be:

- Predictable
- Consistent
- Informative
- Secure
- Recoverable where possible

Errors should never expose sensitive implementation details to end users.

---

# Fail Fast

Applications should detect invalid conditions as early as possible.

Examples include:

- Invalid API requests
- Missing configuration
- Missing datasets
- Invalid database connections
- Invalid model files

Early detection simplifies debugging and prevents cascading failures.

---

# Validate Before Processing

Input validation should occur before business logic executes.

Validation includes:

- API request payloads
- Dataset structure
- Configuration values
- File existence
- Function parameters

Invalid input should produce meaningful exceptions.

---

# Raise Specific Exceptions

Always raise the most appropriate exception type.

Prefer:

```python
raise ValueError("District name cannot be empty.")
```

Instead of:

```python
raise Exception("Error")
```

Specific exceptions improve readability and debugging.

---

# Avoid Bare Exceptions

Never use:

```python
except:
```

Always catch explicit exception types.

Example:

```python
except FileNotFoundError:
    ...
```

or

```python
except ValidationError:
    ...
```

Avoid hiding unexpected failures.

---

# Do Not Suppress Errors

Exceptions should never be silently ignored.

Avoid:

```python
try:
    ...
except Exception:
    pass
```

If an exception is intentionally handled, it should either:

- Be logged.
- Be converted into a meaningful application error.
- Be re-raised with additional context.

---

# Use Custom Exceptions

Application-specific failures should use custom exception classes.

Examples:

```python
ValidationError

PredictionError

DatabaseError

RecommendationError

DatasetError

ModelLoadingError
```

Custom exceptions improve readability and allow targeted error handling.

---

# Preserve Context

When re-raising exceptions, preserve the original cause whenever possible.

Example:

```python
raise PredictionError(
    "Prediction generation failed."
) from error
```

This maintains the exception chain and simplifies debugging.

---

# Error Messages

Error messages should:

- Clearly describe the problem.
- Explain what failed.
- Avoid implementation-specific details.
- Avoid exposing sensitive information.

Good example:

```text
Prediction model could not be loaded.
```

Avoid:

```text
AttributeError on line 147 in prediction_service.py
```

Internal implementation details belong only in logs.

---

# API Error Responses

All API errors should return consistent JSON responses.

Typical structure:

```json
{
  "detail": "District not found."
}
```

Unexpected server errors should not expose stack traces.

---

# HTTP Status Codes

Errors should use appropriate HTTP status codes.

Examples:

| Status Code | Usage                 |
| ----------- | --------------------- |
| 400         | Invalid request       |
| 404         | Resource not found    |
| 422         | Validation error      |
| 500         | Internal server error |

Status codes should accurately reflect the failure.

---

# Database Errors

Database-related exceptions should be handled within the Repository Layer whenever practical.

Examples include:

- Connection failures
- Missing records
- Integrity violations

Repositories should not expose raw database exceptions directly to API routes.

---

# Machine Learning Errors

Machine learning components should handle failures such as:

- Missing model artifacts
- Corrupted Joblib files
- Invalid prediction inputs
- Unsupported feature sets

Prediction failures should generate meaningful application exceptions.

---

# File Handling Errors

Before reading files, verify that they exist when appropriate.

Typical failures include:

- Missing datasets
- Missing GeoJSON files
- Missing configuration
- Missing serialized models

Applications should fail gracefully with informative error messages.

---

# Configuration Errors

Required configuration values should be validated during application startup.

Examples include:

- Missing environment variables
- Invalid database paths
- Missing API keys
- Invalid configuration values

Startup should fail immediately if essential configuration is unavailable.

---

# Frontend Error Handling

Frontend components should handle backend failures gracefully.

Users should receive informative feedback such as:

- Data unavailable
- Request failed
- Resource not found

The UI should avoid blank screens or uncaught exceptions.

---

# Logging Errors

Unexpected errors should always be logged.

Logs should include:

- Timestamp
- Error type
- Message
- Relevant context

Sensitive information should never appear in logs.

---

# Retry Strategy

Retries should only be used for temporary failures.

Examples include:

- Temporary network interruptions
- External API timeouts (future scope)

Validation failures and programming errors should not be retried.

---

# Cleanup After Failure

Resources should always be released after exceptions occur.

Examples include:

- Closing files
- Releasing database sessions
- Cleaning temporary resources

Use context managers whenever practical.

---

# Testing Error Scenarios

Automated tests should verify common failure cases.

Examples include:

- Invalid requests
- Missing districts
- Invalid datasets
- Missing model files
- Database failures

Expected exceptions should be validated explicitly.

---

# Error Handling Review Checklist

Before committing code, verify that it:

- Validates inputs before processing.
- Raises specific exception types.
- Avoids bare `except` statements.
- Never suppresses unexpected exceptions.
- Uses meaningful error messages.
- Preserves exception context when re-raising.
- Returns consistent API error responses.
- Logs unexpected failures.
- Cleans up resources correctly.
- Avoids exposing sensitive implementation details.

Following these conventions ensures that errors are handled consistently, predictably, and securely across every component of EVision Telangana.

# Logging Conventions

Logging provides visibility into application behavior, simplifies debugging, supports maintenance, and assists in diagnosing production issues.

EVision Telangana uses Python's built-in **logging** module for backend logging.

The frontend should use browser console logging only during development.

Logging should provide useful operational information without exposing sensitive data.

---

# Logging Objectives

Logging should:

- Record important application events.
- Assist debugging.
- Simplify issue investigation.
- Support monitoring.
- Improve maintainability.

Logging is intended for developers and maintainers, not end users.

---

# General Principles

Logs should be:

- Consistent
- Informative
- Concise
- Structured
- Actionable

Every log entry should provide meaningful information.

---

# Use the Standard Logging Module

Backend logging should use the standard Python logging library.

Example:

```python
import logging

logger = logging.getLogger(__name__)
```

Avoid using:

```python
print()
```

for runtime logging.

---

# Log Levels

Use the appropriate logging level for each event.

| Level    | Purpose                                            |
| -------- | -------------------------------------------------- |
| DEBUG    | Detailed diagnostic information during development |
| INFO     | Normal application events                          |
| WARNING  | Unexpected situations that do not stop execution   |
| ERROR    | Recoverable failures                               |
| CRITICAL | Severe failures that prevent application operation |

Developers should avoid logging everything as ERROR.

---

# DEBUG Logs

DEBUG logs provide detailed diagnostic information.

Examples include:

- Function entry
- Intermediate calculations
- Temporary debugging information

DEBUG logging should primarily be used during development.

---

# INFO Logs

INFO logs record expected application events.

Examples include:

- Backend startup
- Backend shutdown
- Database initialization
- Model loading
- Prediction generation
- Recommendation generation

These logs help understand normal application execution.

---

# WARNING Logs

WARNING logs indicate unexpected but recoverable situations.

Examples include:

- Missing optional data
- Unsupported optional configuration
- Empty datasets
- Deprecated behavior

Warnings should not indicate application failure.

---

# ERROR Logs

ERROR logs indicate failures that affect a specific operation but allow the application to continue running.

Examples include:

- Prediction failure
- Database query failure
- Dataset loading failure
- API request processing failure

Errors should include sufficient context for debugging.

---

# CRITICAL Logs

CRITICAL logs indicate failures that prevent the application from operating.

Examples include:

- Application startup failure
- Missing required configuration
- Database initialization failure
- Corrupted model artifacts preventing inference

Critical failures typically require immediate attention.

---

# Log Message Style

Log messages should:

- Be concise.
- Use complete sentences where appropriate.
- Describe what happened.
- Include relevant context.

Good example:

```text
Loaded regression model successfully.
```

Avoid vague messages such as:

```text
Done.

Success.

Error occurred.
```

---

# Include Relevant Context

Logs should include useful contextual information.

Examples include:

- District name
- Forecast period
- Dataset filename
- API endpoint
- Exception type

Example:

```text
Prediction generation failed for district Hyderabad.
```

Avoid logging excessive internal implementation details.

---

# Avoid Sensitive Information

Logs must never contain:

- API keys
- Passwords
- Tokens
- Secrets
- Personal information
- Environment variable values

Sensitive information should remain confidential.

---

# Exception Logging

Unexpected exceptions should be logged with traceback information when appropriate.

Example:

```python
logger.exception("Prediction generation failed.")
```

This automatically records the exception stack trace.

---

# Startup Logging

The application should log important startup events.

Examples include:

- Configuration loaded
- Database connected
- Models loaded
- API initialized

Startup logs assist troubleshooting deployment issues.

---

# Shutdown Logging

Application shutdown should be logged cleanly.

Typical events include:

- Server shutdown
- Resource cleanup
- Database session closure

---

# API Logging

The API layer should log significant events such as:

- Server startup
- Unexpected request failures
- Internal server errors

Routine successful requests generally do not require verbose logging.

---

# Database Logging

Database infrastructure should log:

- Successful initialization
- Connection failures
- Migration errors (future scope)

Routine CRUD operations should not produce excessive logs.

---

# Machine Learning Logging

Machine learning components should log:

- Model loading
- Prediction generation
- Model initialization
- Missing model artifacts

Prediction logs should avoid recording large datasets.

---

# Data Processing Logging

The preprocessing pipeline should log:

- Dataset loading
- Validation results
- Cleaning progress
- Output generation
- Completion status

Long-running processing tasks should provide progress updates where appropriate.

---

# Frontend Logging

Frontend logging should be limited to development.

Before committing code:

- Remove debugging `console.log()` statements.
- Retain only intentional warnings or errors when appropriate.

The frontend should display user-friendly error messages instead of relying on console output.

---

# Log Formatting

Log output should remain consistent throughout the project.

Typical information includes:

- Timestamp
- Log level
- Module name
- Log message

Consistent formatting improves readability and simplifies debugging.

---

# Logging Frequency

Avoid excessive logging.

Developers should not log:

- Every variable assignment
- Every loop iteration
- Every helper function call

Logs should communicate meaningful events rather than implementation details.

---

# Testing Logging

Automated tests generally should not depend on log output.

Logs support debugging but should not form part of application logic.

---

# Logging Review Checklist

Before committing code, verify that logging:

- Uses the standard logging module.
- Uses appropriate log levels.
- Provides meaningful messages.
- Includes useful context.
- Avoids sensitive information.
- Does not use `print()` for runtime logging.
- Logs unexpected exceptions appropriately.
- Avoids excessive verbosity.
- Remains consistent across the project.

Following these conventions ensures that logging remains useful, secure, consistent, and maintainable throughout the EVision Telangana codebase.

# Documentation Conventions

Good documentation improves collaboration, onboarding, maintainability, and long-term project quality.

Documentation should clearly communicate **why** the system exists, **how** it works, and **how** it should be used.

Every contributor is responsible for keeping documentation accurate and synchronized with the implementation.

---

# Documentation Objectives

Project documentation should:

- Improve code readability.
- Simplify onboarding.
- Support collaboration.
- Explain implementation decisions.
- Reduce unnecessary knowledge sharing through verbal communication.

Documentation should evolve together with the codebase.

---

# General Principles

Documentation should be:

- Clear
- Accurate
- Concise
- Up to date
- Easy to navigate

Documentation should explain concepts rather than repeat obvious implementation details.

---

# Single Source of Truth

Every topic should have one authoritative location.

Examples:

| Topic                    | Authoritative Document |
| ------------------------ | ---------------------- |
| Project scope            | Final Project Scope    |
| Architecture             | System Architecture    |
| API behavior             | API Specification      |
| Database structure       | Database Schema        |
| Data formats             | Data Contracts         |
| Implementation standards | Coding Standards       |

Developers should update the authoritative document rather than creating duplicate documentation elsewhere.

---

# Keep Documentation Current

Whenever implementation changes require updates to documentation, both should be updated together.

Documentation should never become outdated relative to the codebase.

Examples include changes to:

- API contracts
- Database schema
- Repository structure
- Configuration
- Project workflow

---

# Module Documentation

Every public module should begin with a concise module-level docstring describing its purpose.

Example:

```python
"""
Prediction service responsible for generating charging demand forecasts.
"""
```

Module documentation should explain responsibilities rather than implementation details.

---

# Class Documentation

Public classes should include docstrings describing:

- Purpose
- Responsibility
- Intended usage

Example:

```python
class RecommendationService:
    """Generates district recommendations using prediction and analytics data."""
```

---

# Function Documentation

Public functions should include docstrings describing:

- Purpose
- Parameters
- Return value
- Raised exceptions (when applicable)

Example:

```python
def generate_predictions() -> list[Prediction]:
    """Generate charging demand predictions for all districts."""
```

Private helper functions may omit docstrings when their behavior is obvious.

---

# API Documentation

Every API endpoint should include:

- Summary
- Description
- Request schema
- Response schema
- Status codes

FastAPI's automatic OpenAPI documentation should accurately represent the implemented API.

---

# Database Documentation

Database changes should be reflected in the approved Database Schema document.

SQLModel classes should include concise docstrings describing the represented entity.

Database implementation should not become the primary source of schema documentation.

---

# Data Documentation

Datasets, generated artifacts, and machine learning outputs should remain consistent with the approved Data Contracts.

New data structures should not be introduced without corresponding documentation updates.

---

# README Files

Each major repository should include an appropriate README where necessary.

Typical README contents include:

- Purpose
- Setup instructions
- Running the application
- Development workflow
- Important notes

README files should provide high-level guidance rather than detailed implementation explanations.

---

# Inline Documentation

Use inline documentation only when necessary.

Documentation should explain:

- Why a decision was made.
- Business assumptions.
- Architectural constraints.
- Non-obvious implementation choices.

Avoid documenting obvious code.

---

# Architecture Documentation

Implementation should remain consistent with the approved System Architecture.

Significant architectural changes require updates to the Architecture document before implementation is considered complete.

---

# Configuration Documentation

Environment variables should be documented within:

```text
.env.example
```

Each variable should have:

- Name
- Purpose
- Example value (where appropriate)

Sensitive values should never be documented with real credentials.

---

# Markdown Style

Project documentation should consistently use Markdown.

General guidelines include:

- Use descriptive headings.
- Use tables where appropriate.
- Use fenced code blocks.
- Keep sections logically organized.
- Maintain consistent formatting across Project Sources.

Consistency improves readability and navigation.

---

# Diagrams

Architecture and workflow diagrams should be updated whenever major structural changes occur.

Diagrams should remain synchronized with:

- Repository Structure
- System Architecture
- Data Flow
- Development Workflow

Outdated diagrams reduce documentation quality.

---

# Examples

Documentation should include examples where they improve understanding.

Examples may include:

- API requests
- API responses
- Configuration
- Directory structure
- Code snippets

Examples should remain simple and representative.

---

# Avoid Redundant Documentation

The same information should not be documented in multiple locations.

Instead:

- Link related concepts conceptually.
- Update the authoritative source.
- Avoid conflicting descriptions.

Redundant documentation increases maintenance effort.

---

# Documentation During Development

Documentation should be treated as part of implementation rather than an afterthought.

When completing a feature, developers should verify whether related documentation requires updates.

Documentation tasks should be completed before merging changes.

---

# Review Expectations

Documentation changes should be reviewed with the same attention as source code.

Reviewers should verify:

- Technical accuracy.
- Consistency with implementation.
- Grammar and clarity.
- Alignment with existing Project Sources.

Incomplete or outdated documentation should be corrected before approval.

---

# Documentation Review Checklist

Before committing code, verify that:

- Public modules are documented.
- Public classes include docstrings.
- Public functions include docstrings.
- API documentation remains accurate.
- Database documentation reflects implementation.
- Data Contracts remain valid.
- README files remain current.
- Markdown formatting is consistent.
- Examples remain accurate.
- No duplicate or conflicting documentation exists.

Following these conventions ensures that documentation remains accurate, maintainable, and valuable throughout the lifecycle of the EVision Telangana project.

# Commenting Guidelines

Comments should improve understanding of the code by explaining **why** something exists rather than **what** the code is doing.

Well-written code should be largely self-explanatory through meaningful names and clear structure. Comments should supplement readable code, not compensate for poor implementation.

---

# Commenting Objectives

Comments should:

- Explain intent.
- Clarify complex logic.
- Document assumptions.
- Describe architectural decisions.
- Improve maintainability.

Comments should not become a substitute for good code.

---

# General Principles

Comments should be:

- Accurate
- Concise
- Helpful
- Up to date
- Easy to understand

Outdated comments are worse than having no comments.

---

# Prefer Self-Documenting Code

Whenever possible, improve code readability instead of adding comments.

Instead of:

```python
# Calculate district priority score
score = a * b + c
```

Prefer:

```python
priority_score = (
    predicted_demand * demand_weight
    + infrastructure_score
)
```

Meaningful names reduce the need for explanatory comments.

---

# Explain Why, Not What

Comments should explain reasoning rather than restating implementation.

Avoid:

```python
# Increment index
index += 1
```

Prefer:

```python
# Skip the current district because incomplete historical data
# would produce unreliable prediction results.
```

The reason behind the implementation is far more valuable than describing the syntax.

---

# Document Business Rules

Business rules that are not immediately obvious should be documented.

Examples include:

- Recommendation scoring assumptions
- Data validation requirements
- Feature engineering decisions
- Domain-specific calculations

These comments help future contributors understand project-specific logic.

---

# Explain Complex Logic

Complex algorithms or calculations should include brief explanatory comments.

Example:

```python
# Normalize demand values before clustering to prevent
# districts with extremely high consumption from dominating
# the distance calculation.
```

Comments should summarize the approach rather than describe every line.

---

# Use Block Comments Sparingly

Multi-line comments should be used only when necessary.

They are appropriate for:

- Complex algorithms
- Architectural decisions
- Temporary implementation constraints

Avoid large blocks of unnecessary explanation.

---

# Inline Comments

Inline comments should be used sparingly.

They are appropriate only when a single line requires clarification.

Example:

```python
priority_score += 5  # Bonus for underserved districts.
```

Avoid excessive inline comments throughout the code.

---

# TODO Comments

Use TODO comments only for planned future improvements that are outside the approved MVP scope.

Format:

```python
# TODO: Support multiple forecast periods in a future release.
```

Every TODO should:

- Describe the future task.
- Be specific.
- Be actionable.

Avoid vague TODOs such as:

```python
# TODO: Fix this.
```

---

# FIXME Comments

Use FIXME comments only for known issues that require correction.

Example:

```python
# FIXME: Replace temporary mock data with database query.
```

Known issues should also be tracked through the team's issue management process.

---

# HACK Comments

Avoid HACK comments whenever possible.

If a temporary workaround is absolutely necessary, explain:

- Why it exists.
- When it should be removed.

Example:

```python
# HACK:
# Temporary compatibility workaround until the preprocessing
# pipeline supports the updated dataset format.
```

Such comments should not remain indefinitely.

---

# Module Comments

Every public module should include a module-level docstring rather than introductory comments.

Avoid:

```python
# Prediction Service
# Generates predictions
```

Prefer:

```python
"""
Prediction service responsible for generating charging demand forecasts.
"""
```

---

# Class Comments

Public classes should use docstrings instead of standalone comments.

Example:

```python
class PredictionService:
    """Generates district demand predictions."""
```

---

# Function Comments

Public functions should use docstrings.

Avoid placing explanatory comments immediately above every function.

Example:

```python
def generate_predictions():
    """Generate charging demand predictions."""
```

---

# Comment Accuracy

Comments should always reflect the current implementation.

Whenever code changes, related comments should also be reviewed and updated.

Incorrect comments are misleading and should be removed or corrected.

---

# Avoid Redundant Comments

Do not comment obvious code.

Avoid:

```python
# Return predictions
return predictions
```

Such comments provide no additional value.

---

# Comment Style

Comments should:

- Use proper grammar.
- Begin with a capital letter.
- End with a period when written as complete sentences.
- Remain professional and objective.

Avoid informal or humorous comments that may become confusing over time.

---

# Avoid Dead Code

Do not leave commented-out code in the repository.

Avoid:

```python
# old_prediction = model.predict(data)
```

Unused code should be removed.

Version control preserves historical implementations.

---

# Frontend Comments

React components should follow the same principles.

Comments should explain:

- UI behavior
- Performance considerations
- Non-obvious rendering logic

Avoid commenting straightforward JSX markup.

---

# Machine Learning Comments

Machine learning code should document:

- Feature engineering assumptions
- Model selection rationale
- Preprocessing requirements
- Prediction constraints

This improves reproducibility and maintainability.

---

# Review Expectations

During code review, comments should be evaluated for:

- Accuracy
- Relevance
- Clarity
- Consistency

Outdated or unnecessary comments should be removed.

---

# Commenting Review Checklist

Before committing code, verify that:

- Comments explain _why_, not _what_.
- Public modules use docstrings.
- Public classes use docstrings.
- Public functions use docstrings.
- Complex logic is documented.
- Business rules are explained.
- TODO/FIXME comments are specific.
- No commented-out code remains.
- Comments accurately reflect the implementation.
- Comments improve readability rather than duplicate the code.

Following these guidelines ensures that comments remain valuable documentation rather than unnecessary noise throughout the EVision Telangana codebase.

# Type Hint Guidelines

Type hints improve code readability, editor support, static analysis, and maintainability.

All Python code in EVision Telangana should use explicit type hints wherever practical.

The project follows **PEP 484** and modern Python 3.12 type annotation conventions.

---

# Objectives

Type hints should:

- Improve readability.
- Clarify function interfaces.
- Support static analysis.
- Reduce runtime errors.
- Improve IDE auto-completion.
- Simplify code reviews.

Type hints document expected inputs and outputs without affecting runtime behavior.

---

# General Principles

Type hints should be:

- Explicit
- Consistent
- Accurate
- Readable

Avoid unnecessary complexity in type annotations.

---

# Public Functions

All public functions should include complete type hints.

Example:

```python
def get_prediction(district: str) -> float:
    ...
```

Both parameters and return values should be annotated.

---

# Private Functions

Private helper functions should also use type hints whenever practical.

Example:

```python
def _normalize_score(score: float) -> float:
    ...
```

Consistent type hinting throughout the project improves maintainability.

---

# Return Types

Every function should declare its return type.

Examples:

```python
def load_dataset() -> pd.DataFrame:
```

```python
def calculate_priority_score() -> float:
```

```python
def initialize_database() -> None:
```

Returning `None` should be explicitly declared.

---

# Variable Annotations

Annotate variables when the type is not immediately obvious.

Example:

```python
district_scores: dict[str, float] = {}
```

Avoid excessive annotations when the type is already clear from assignment.

---

# Collections

Use built-in generic collection types.

Examples:

```python
list[str]

dict[str, float]

set[int]

tuple[int, str]
```

Prefer these over legacy imports from `typing`.

---

# Optional Values

Use the modern union operator (`|`) for optional values.

Example:

```python
organization: str | None = None
```

Avoid older syntax such as:

```python
Optional[str]
```

unless compatibility requires it.

---

# Union Types

Use the `|` operator for multiple possible types.

Example:

```python
value: int | float
```

This syntax is preferred over `typing.Union`.

---

# SQLModel Fields

SQLModel models should use explicit field annotations.

Example:

```python
district_name: str

priority_score: float

organization: str | None
```

Type hints should accurately reflect the approved Database Schema.

---

# Pydantic Schemas

All schema fields should include explicit types.

Example:

```python
class PredictionRequest(BaseModel):
    district: str
```

Schema annotations should remain consistent with the API Specification.

---

# Class Attributes

Instance variables should include type annotations where appropriate.

Example:

```python
class PredictionService:
    repository: PredictionRepository
```

Explicit attribute types improve readability and IDE support.

---

# Constants

Constants should also use type annotations when useful.

Example:

```python
API_VERSION: str = "v1"

DEFAULT_PAGE_SIZE: int = 20
```

---

# Callable Types

When functions accept other functions as parameters, use `Callable`.

Example:

```python
from collections.abc import Callable

processor: Callable[[str], float]
```

Only use callable annotations when they improve clarity.

---

# Generic Types

Use generic type parameters where appropriate.

Example:

```python
def first_item(items: list[T]) -> T:
    ...
```

Avoid unnecessary generic complexity for straightforward functions.

---

# Any

Avoid using:

```python
Any
```

unless there is a legitimate reason.

Using `Any` removes the benefits of static type checking.

Prefer specific types whenever possible.

---

# Type Aliases

Use type aliases for complex or frequently repeated types.

Example:

```python
type DistrictScores = dict[str, float]
```

Type aliases improve readability and reduce duplication.

---

# Forward References

Use forward references only when necessary to avoid circular imports.

Example:

```python
districts: list["District"]
```

Forward references should remain minimal.

---

# Third-Party Libraries

Use the types provided by third-party libraries when available.

Examples include:

```python
pd.DataFrame

Path

datetime
```

Avoid replacing well-defined library types with generic annotations.

---

# Runtime Validation

Type hints do not replace validation.

Application code should continue validating:

- User input
- API requests
- Configuration
- Dataset contents

Type annotations describe expected types but do not enforce runtime correctness.

---

# Static Analysis

Type hints should support static analysis tools.

Code should avoid annotations that generate unnecessary type-checking warnings.

Where practical, implementations should remain compatible with modern static analysis tools.

---

# Consistency

Equivalent functions should use consistent type annotations.

Example:

```python
def get_prediction(...) -> PredictionResponse
```

should not return dictionaries elsewhere unless intentionally designed to do so.

Consistency improves maintainability.

---

# Type Hint Review Checklist

Before committing code, verify that:

- Public functions include parameter and return type annotations.
- Class attributes are typed where appropriate.
- SQLModel fields use explicit types.
- Pydantic schemas use explicit types.
- Optional values use `| None`.
- Collection types use modern built-in generics.
- `Any` is avoided unless necessary.
- Type aliases are used for complex repeated types.
- Type hints remain consistent throughout the project.
- Runtime validation is not replaced by type annotations.

Following these guidelines ensures that type hints remain consistent, readable, and valuable across the EVision Telangana codebase.

# Import Organization

Consistent import organization improves readability, reduces merge conflicts, and simplifies dependency management.

Every source file in EVision Telangana should organize imports in a predictable and standardized manner.

Automatic import sorting should be handled by **Ruff** for Python and **Prettier** (with the project's configuration) for JavaScript where applicable.

---

# General Principles

Imports should be:

- Organized
- Minimal
- Explicit
- Readable
- Free of duplication

Each module should import only the dependencies it actually uses.

Unused imports should be removed before committing code.

---

# Python Import Order

Python imports should be grouped into the following order:

1. Standard library
2. Third-party libraries
3. Local project modules

Separate each group with a single blank line.

Example:

```python
from pathlib import Path
from datetime import datetime

import pandas as pd
from fastapi import APIRouter
from sqlmodel import Session

from app.repositories.district_repository import DistrictRepository
from app.services.prediction_service import PredictionService
```

This ordering should remain consistent throughout the project.

---

# Standard Library Imports

Standard library imports should always appear first.

Examples:

```python
from datetime import datetime
from pathlib import Path
from typing import Literal
import logging
```

Do not mix standard library imports with third-party packages.

---

# Third-Party Imports

Third-party packages should appear after standard library imports.

Examples:

```python
import pandas as pd
from fastapi import APIRouter
from sqlmodel import SQLModel
```

Third-party imports should remain alphabetically ordered within their group whenever practical.

---

# Local Project Imports

Project modules should appear last.

Examples:

```python
from app.core.config import settings
from app.schemas.prediction import PredictionResponse
from app.services.analytics_service import AnalyticsService
```

Local imports should clearly indicate project ownership.

---

# Alphabetical Ordering

Within each import group, imports should generally be ordered alphabetically.

Example:

```python
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

from app.repositories import repository
from app.services import service
```

Consistent ordering improves readability and reduces merge conflicts.

---

# One Import Per Line

Prefer one imported module per line.

Instead of:

```python
import os, sys
```

Prefer:

```python
import os
import sys
```

This improves readability and version control diffs.

---

# Avoid Wildcard Imports

Wildcard imports are prohibited.

Avoid:

```python
from utils import *
```

Prefer:

```python
from utils.validation import validate_dataset
```

Explicit imports improve readability and prevent namespace conflicts.

---

# Import Only What Is Needed

Import only the symbols required by the module.

Avoid:

```python
import pandas
```

when only:

```python
import pandas as pd
```

or a specific object is needed.

Similarly, avoid importing unused modules.

---

# Circular Imports

Circular imports should be avoided through proper project organization.

If unavoidable, consider:

- Refactoring responsibilities.
- Moving shared logic into another module.
- Using forward references where appropriate.

Circular imports should never become a permanent architectural dependency.

---

# Relative Imports

Prefer absolute imports within the project.

Instead of:

```python
from ..services.prediction_service import PredictionService
```

Prefer:

```python
from app.services.prediction_service import PredictionService
```

Absolute imports improve readability and simplify refactoring.

---

# Conditional Imports

Conditional imports should only be used when genuinely necessary.

Typical cases include:

- Optional dependencies
- Platform-specific functionality
- Type checking

Conditional imports should remain rare.

---

# Imports Inside Functions

Imports should normally appear at the top of the module.

Function-level imports should only be used when necessary.

Typical reasons include:

- Avoiding circular imports
- Reducing startup time for optional dependencies

Routine imports should not be placed inside functions.

---

# JavaScript Import Order

JavaScript and React modules should organize imports in the following order:

1. React
2. Third-party packages
3. Local components
4. Local hooks
5. Services
6. Utilities
7. Styles
8. Static assets

Example:

```javascript
import { useEffect, useState } from "react";

import { MapContainer } from "react-leaflet";

import DashboardCard from "../components/DashboardCard";

import useDistrictData from "../hooks/useDistrictData";

import apiClient from "../services/apiClient";

import { formatNumber } from "../utils/numberUtils";

import "../styles/dashboard.css";

import logo from "../assets/logo.svg";
```

Maintaining a consistent order improves navigation.

---

# Named vs Default Imports

Use named imports when multiple exports are available.

Example:

```javascript
import { useEffect, useState } from "react";
```

Use default imports only when the module intentionally exports a single primary object.

---

# Grouping Imports

Separate different import groups using a single blank line.

Avoid mixing unrelated imports together.

This improves readability and makes dependencies easier to identify.

---

# Remove Unused Imports

Unused imports should never remain in committed code.

Developers should remove:

- Unused modules
- Unused functions
- Unused classes
- Unused constants

Ruff and other development tools should detect these automatically.

---

# Import Side Effects

Avoid modules that execute significant side effects during import.

Imports should generally:

- Define functionality
- Register objects
- Provide reusable components

Heavy initialization should occur explicitly rather than automatically during module loading.

---

# Dependency Direction

Imports should follow the approved layered architecture.

For example:

```text
API
    ↓
Services
    ↓
Repositories
    ↓
Database
```

Higher layers may depend on lower layers.

Lower layers should never import higher layers.

Example:

- Services may import repositories.
- Repositories should not import services.
- SQLModel models should not import API routers.

This prevents circular dependencies and preserves architectural boundaries.

---

# Import Review Checklist

Before committing code, verify that:

- Imports follow the approved ordering.
- Standard library, third-party, and local imports are grouped correctly.
- Unused imports have been removed.
- Wildcard imports are not used.
- Absolute imports are preferred.
- Circular dependencies have been avoided.
- Imports are alphabetically ordered within each group where practical.
- Function-level imports are used only when justified.
- JavaScript imports follow the approved grouping order.
- Module dependencies respect the approved architecture.

Following these conventions ensures that imports remain organized, predictable, and consistent across the EVision Telangana codebase.

# Project Organization Principles

The EVision Telangana codebase is organized around a modular, layered architecture to promote maintainability, collaboration, and scalability.

Every contributor should organize new code according to the approved Repository Structure and System Architecture.

The organization of the project should remain predictable throughout the entire development lifecycle.

---

# Organization Objectives

The project organization aims to:

- Promote modular development.
- Reduce coupling between components.
- Improve code discoverability.
- Simplify maintenance.
- Support parallel team development.
- Preserve architectural consistency.

Every file should have a clearly defined place within the repository.

---

# Layered Architecture

The project follows the approved layered architecture.

```text
Frontend
        │
        ▼
API Layer
        │
        ▼
Service Layer
        │
        ▼
Repository Layer
        │
        ▼
Database
```

Each layer has one clearly defined responsibility.

Layers should communicate only through their approved interfaces.

---

# Separation of Concerns

Each project layer should focus on one responsibility.

Examples include:

| Layer            | Responsibility                     |
| ---------------- | ---------------------------------- |
| Frontend         | User interface and visualization   |
| API              | HTTP request and response handling |
| Services         | Business logic                     |
| Repositories     | Database access                    |
| SQLModel Models  | Database representation            |
| Schemas          | Request and response validation    |
| Machine Learning | Prediction and clustering          |
| Data Pipeline    | Data preprocessing                 |

Responsibilities should never overlap.

---

# Modular Design

The project should be divided into independent modules.

Each module should represent one logical feature or domain.

Examples:

```text
dashboard/

districts/

predictions/

analytics/

recommendations/

assistant/
```

Modules should communicate through well-defined interfaces.

---

# Domain-Oriented Organization

Business functionality should be grouped by domain rather than by implementation style whenever practical.

For example, prediction-related logic should remain together across:

- API routes
- Services
- Repositories
- Schemas
- Tests

This improves navigation and maintainability.

---

# One Responsibility Per File

Each source file should have one primary responsibility.

Examples:

Good:

```text
prediction_service.py

district_repository.py

dashboard.py
```

Avoid files containing multiple unrelated features.

---

# One Responsibility Per Directory

Directories should represent one logical responsibility.

Examples:

```text
services/

repositories/

schemas/

models/

components/

hooks/
```

Avoid generic directories such as:

```text
misc/

common/

others/
```

unless their purpose is clearly justified.

---

# Business Logic Centralization

Business logic belongs exclusively in the Service Layer.

Business rules should not be implemented inside:

- API routes
- SQLModel models
- Repositories
- React components

This keeps the architecture clean and prevents duplication.

---

# Reusable Components

Common functionality should be extracted into reusable modules.

Examples include:

- Validation helpers
- Response builders
- API client
- Utility functions
- Shared React components

Duplicated implementations should be avoided.

---

# Consistent Naming

Equivalent concepts should use consistent names throughout the project.

Examples:

- PredictionService
- prediction_service.py
- prediction.py
- prediction_outputs.csv

Using consistent terminology improves readability and collaboration.

---

# Keep Dependencies Directional

Dependencies should always follow the approved architecture.

Allowed dependency flow:

```text
Frontend
    ↓
API
    ↓
Services
    ↓
Repositories
    ↓
Database
```

Lower layers should never depend on higher layers.

Examples:

- Services may import repositories.
- Repositories should not import services.
- SQLModel models should not import API routers.

---

# Avoid Circular Dependencies

Modules should remain independent.

Circular imports usually indicate poor organization.

When circular dependencies appear, consider:

- Extracting shared functionality.
- Introducing a utility module.
- Refactoring responsibilities.

Circular dependencies should be resolved rather than worked around.

---

# Feature Isolation

Each major project feature should remain largely independent.

Examples:

```text
Dashboard

Predictions

Recommendations

Analytics

AI Assistant
```

Implementation for one feature should not unnecessarily affect unrelated features.

---

# Shared Utilities

Shared functionality should be placed inside dedicated utility modules.

Examples include:

- Date handling
- Geographic calculations
- Response formatting
- Validation
- Configuration helpers

Utility modules should remain generic and reusable.

---

# Configuration Management

Configuration should remain centralized.

Examples include:

- Environment variables
- Database configuration
- Application settings
- Logging configuration

Configuration values should never be scattered throughout the codebase.

---

# Data Ownership

Each dataset, model, and generated artifact should have one authoritative owner as defined in the Data Contracts.

Source code should not create competing sources of truth.

Examples:

- Raw datasets remain immutable.
- Processed datasets are generated by the preprocessing pipeline.
- SQLite stores runtime application data.
- Machine learning artifacts are generated by the training pipeline.

---

# Keep Experimental Code Separate

Exploratory work should remain outside production code.

Examples:

```text
notebooks/

experiments/
```

Experimental implementations should be migrated into production modules only after validation.

---

# Test Organization

Tests should mirror the project structure.

Example:

```text
tests/
├── api/
├── services/
├── repositories/
├── ml/
├── utils/
└── frontend/
```

This makes tests easy to locate and maintain.

---

# Documentation Organization

Documentation should remain separated from implementation.

Project Sources, reports, diagrams, and other documentation should not be mixed with application code.

Documentation should remain synchronized with implementation throughout development.

---

# Scalability

The project structure should support future expansion without requiring major reorganization.

New features should integrate into the existing architecture rather than introducing alternative organizational patterns.

Consistency should be preserved as the repository grows.

---

# Project Organization Review Checklist

Before committing new code, verify that:

- Files are placed in the correct directory.
- Each file has one primary responsibility.
- Business logic resides in the Service Layer.
- Dependencies follow the approved architecture.
- Circular dependencies have been avoided.
- Shared functionality has not been duplicated.
- Naming remains consistent across modules.
- Tests follow the project structure.
- Documentation remains synchronized.
- The new code integrates naturally into the existing repository organization.

Following these principles ensures that the EVision Telangana codebase remains organized, maintainable, scalable, and easy for every team member to navigate.

# Testing Expectations

Testing ensures that the EVision Telangana application behaves correctly, remains reliable, and continues to function as expected as new features are implemented.

Every major component should be designed to support automated testing.

Testing should verify correctness rather than implementation details.

---

# Testing Objectives

The project's testing strategy aims to:

- Detect defects early.
- Prevent regressions.
- Verify business logic.
- Improve maintainability.
- Increase development confidence.
- Support collaborative development.

Testing is considered part of the implementation process rather than a separate activity.

---

# General Principles

Tests should be:

- Reliable
- Repeatable
- Independent
- Readable
- Fast
- Deterministic

Executing the same test multiple times should always produce the same result under identical conditions.

---

# Test Organization

Tests should mirror the project structure.

Example:

```text
tests/
├── api/
├── services/
├── repositories/
├── ml/
├── utils/
├── frontend/
└── data/
```

Each production module should have a corresponding test module whenever practical.

---

# Unit Testing

Unit tests verify individual functions, classes, and modules in isolation.

Typical unit test targets include:

- Utility functions
- Business logic
- Validation functions
- Recommendation calculations
- Feature engineering
- Prediction logic

Unit tests should avoid unnecessary dependencies on databases or external services.

---

# Integration Testing

Integration tests verify interactions between components.

Examples include:

- API ↔ Service
- Service ↔ Repository
- Repository ↔ Database
- Backend ↔ Machine Learning
- Backend ↔ Data Pipeline

Integration tests ensure components work together correctly.

---

# API Testing

API tests should verify:

- Endpoint availability
- Request validation
- Response schemas
- HTTP status codes
- Error handling
- Business logic integration

Every public endpoint defined in the API Specification should be covered.

---

# Database Testing

Database tests should verify:

- Table creation
- CRUD operations
- Relationships
- Constraints
- Query correctness

Database tests should use isolated test databases whenever practical.

Production data should never be modified during testing.

---

# Machine Learning Testing

Machine learning components should be tested for:

- Model loading
- Prediction execution
- Feature compatibility
- Output format
- Error handling

Testing should verify application integration rather than model accuracy.

Model evaluation remains a separate activity.

---

# Data Pipeline Testing

The preprocessing pipeline should verify:

- Dataset loading
- Data validation
- Cleaning operations
- Output generation
- Reproducibility

Generated datasets should conform to the approved Data Contracts.

---

# Frontend Testing

Frontend tests should verify:

- Component rendering
- User interactions
- API integration
- Conditional rendering
- Error states

Components should remain predictable for identical inputs.

---

# Error Handling Tests

Tests should explicitly verify expected failure scenarios.

Examples include:

- Invalid API requests
- Missing datasets
- Invalid configuration
- Missing database records
- Corrupted model artifacts

Applications should fail gracefully.

---

# Input Validation Tests

Validation tests should confirm that:

- Required fields are enforced.
- Invalid values are rejected.
- Boundary conditions are handled correctly.
- Error messages remain consistent.

Input validation is a critical part of application reliability.

---

# Mocking

External dependencies should be mocked whenever practical.

Examples include:

- Database access
- File system operations
- Machine learning models
- External APIs (future scope)

Mocking allows business logic to be tested independently.

---

# Test Data

Tests should use small, deterministic datasets.

Avoid relying on:

- Production datasets
- Randomly generated values
- External resources

Test data should remain easy to understand and maintain.

---

# Deterministic Tests

Tests should avoid randomness.

If random behavior is required, use a fixed random seed.

Identical tests should produce identical outcomes.

---

# Performance

Tests should execute quickly.

Long-running computations should be minimized or isolated.

Fast test execution encourages frequent testing during development.

---

# Independence

Each test should be independent.

Tests should not rely on:

- Execution order
- Shared mutable state
- Previous test results

Independent tests improve reliability and simplify debugging.

---

# Naming Conventions

Test filenames should begin with:

```text
test_
```

Examples:

```text
test_predictions.py

test_dashboard.py

test_recommendations.py
```

Test function names should clearly describe the expected behavior.

Examples:

```python
def test_generate_predictions_returns_valid_results():
```

```python
def test_invalid_request_returns_validation_error():
```

---

# Assertions

Each test should verify one primary behavior.

Avoid overly broad tests with many unrelated assertions.

Focused tests simplify debugging when failures occur.

---

# Regression Testing

Whenever a defect is fixed, a corresponding automated test should be added to prevent the issue from recurring.

Regression tests improve long-term software quality.

---

# Continuous Verification

Before creating a Pull Request, developers should verify that:

- New tests pass.
- Existing tests continue to pass.
- No previously working functionality has been broken.

Code should not be merged with failing tests.

---

# Test Coverage

The project prioritizes meaningful coverage over maximizing coverage percentages.

Testing should focus on:

- Core business logic
- API behavior
- Database interactions
- Data processing
- Machine learning integration
- Critical utility functions

Simple getters, setters, and trivial wrappers generally do not require dedicated tests.

---

# Testing Review Checklist

Before merging code, verify that:

- New functionality includes appropriate tests.
- Existing tests continue to pass.
- Tests remain deterministic.
- Test data is isolated.
- External dependencies are mocked where appropriate.
- API endpoints are tested.
- Error scenarios are covered.
- Validation logic is tested.
- Tests remain readable and maintainable.
- Production code has not been modified solely to satisfy tests.

Following these testing expectations helps ensure that EVision Telangana remains reliable, maintainable, and robust throughout its development lifecycle.

# Ruff Usage

EVision Telangana uses **Ruff** as the official Python formatter, linter, and import organizer.

Ruff provides fast, consistent, and automated code quality enforcement across the backend, machine learning pipeline, data processing pipeline, and utility modules.

All Python source code must pass Ruff checks before being committed to the repository.

---

# Objectives

Ruff is used to:

- Enforce consistent code formatting.
- Detect common programming errors.
- Maintain coding standards.
- Organize imports automatically.
- Reduce style-related code review comments.
- Improve overall code quality.

Ruff should be treated as the authoritative code formatting tool for Python.

---

# Scope

Ruff applies to all Python source files within the repository.

Examples include:

```text
backend/

scripts/

tests/

notebooks/ (where practical)
```

Generated files should not be manually reformatted unless they are maintained as source code.

---

# Formatting

Python files should be formatted using Ruff before committing changes.

Formatting should not be performed manually if it conflicts with Ruff's output.

Developers should allow Ruff to determine:

- Indentation
- Line wrapping
- Blank lines
- Spacing
- Import formatting

Formatting consistency takes precedence over personal preference.

---

# Linting

All Python code should pass Ruff linting without errors.

Typical checks include:

- Unused imports
- Unused variables
- Undefined names
- Duplicate definitions
- Syntax issues
- Common code quality problems

Lint warnings should be resolved before code review whenever practical.

---

# Import Organization

Ruff is responsible for automatically organizing imports.

Imports should follow the approved ordering:

1. Standard library
2. Third-party libraries
3. Local project modules

Developers should avoid manually rearranging imports.

---

# Line Length

Python code should follow Ruff's default formatting behavior.

Recommended maximum line length:

```text
88 characters
```

Long expressions should be wrapped naturally rather than using manual formatting tricks.

---

# Naming Compliance

Ruff should be used together with the project's approved naming conventions.

Developers remain responsible for using meaningful:

- Variables
- Functions
- Classes
- Modules

Ruff enforces formatting rather than naming quality.

---

# Error Resolution

Developers should resolve Ruff issues rather than suppress them.

Avoid disabling lint rules unless there is a clear technical justification.

Code should be improved instead of bypassing quality checks.

---

# Ignore Rules

Ignore directives should be used sparingly.

If a rule must be ignored, the reason should be documented.

Example:

```python
# noqa: F401
```

Ignoring warnings should never become routine practice.

---

# Automatic Formatting

Developers are encouraged to format code automatically before creating commits or Pull Requests.

Typical workflow:

```text
Write Code
      │
      ▼
Run Ruff Formatter
      │
      ▼
Run Ruff Linter
      │
      ▼
Resolve Issues
      │
      ▼
Commit Changes
```

Automatic formatting reduces unnecessary review comments.

---

# IDE Integration

Developers should configure their editor to use Ruff where supported.

Recommended features include:

- Format on save
- Automatic import organization
- Real-time lint diagnostics

Consistent editor configuration improves team productivity.

---

# Continuous Integration

Ruff checks should pass before code is merged into the main branch.

Code that fails formatting or linting should be corrected prior to approval.

Maintaining a consistently formatted codebase simplifies collaboration.

---

# Relationship with PEP 8

The project follows PEP 8 with Ruff serving as the automated enforcement mechanism.

When Ruff formatting differs slightly from personal style preferences, Ruff should take precedence.

Consistency across the repository is more important than individual formatting choices.

---

# Common Ruff Checks

Typical issues identified by Ruff include:

- Unused imports
- Unused variables
- Undefined names
- Duplicate imports
- Incorrect import ordering
- Formatting inconsistencies
- Trailing whitespace
- Missing blank lines

Developers should become familiar with these common diagnostics.

---

# Before Committing

Before creating a commit, developers should verify that:

- Ruff formatting has been applied.
- Ruff linting reports no unresolved issues.
- Imports have been organized automatically.
- No unnecessary ignore directives remain.
- Formatting changes have been reviewed.

This helps keep the repository consistent and minimizes style-related review feedback.

---

# Ruff Review Checklist

Before submitting code for review, verify that:

- All Python files are formatted with Ruff.
- Lint checks pass successfully.
- Imports are automatically organized.
- Line length remains consistent.
- No unused imports remain.
- No unnecessary ignore directives are present.
- Formatting is not manually overridden.
- Code follows the approved Coding Standards.

Following these conventions ensures that the Python codebase remains clean, consistent, readable, and easy to maintain throughout the EVision Telangana project.

# Prettier Usage

EVision Telangana uses **Prettier** as the official code formatter for the frontend and repository documentation.

Prettier ensures that JavaScript, JSX, JSON, CSS, Markdown, and related files maintain a consistent formatting style across the project.

All applicable files should be formatted with Prettier before being committed to the repository.

---

# Objectives

Prettier is used to:

- Enforce consistent code formatting.
- Improve readability.
- Reduce formatting-related code review comments.
- Minimize merge conflicts.
- Maintain a uniform coding style across the frontend.

Prettier should be treated as the authoritative formatting tool for all supported file types.

---

# Scope

Prettier applies to the following file types:

```text
.js

.jsx

.json

.css

.md
```

Typical directories include:

```text
frontend/

docs/

Project Sources/
```

Configuration files supported by Prettier should also follow its formatting rules.

---

# Formatting Philosophy

Formatting decisions should be automated.

Developers should avoid manually adjusting:

- Indentation
- Spacing
- Line wrapping
- Quote style
- Object formatting

Prettier should determine the final formatting.

Consistency takes precedence over personal formatting preferences.

---

# Indentation

Prettier should use:

```text
2 spaces
```

for JavaScript, JSX, JSON, and CSS formatting.

Tabs should never be used.

---

# Line Length

Recommended maximum line length:

```text
100 characters
```

Long expressions should be wrapped automatically by Prettier.

Developers should avoid manually inserting unnecessary line breaks.

---

# Quotes

Formatting should remain consistent according to the project configuration.

Developers should not manually mix quote styles throughout the project.

Consistency is more important than individual preference.

---

# Semicolons

Semicolon usage should remain consistent with the project's Prettier configuration.

Developers should avoid manually introducing inconsistent formatting.

---

# Trailing Commas

Trailing commas should follow the project configuration.

Automatic formatting should determine their placement.

---

# Object Formatting

Objects, arrays, and JSX should be formatted automatically.

Example:

```javascript
const district = {
  name: "Hyderabad",
  priorityScore: 92,
  chargingStations: 15,
};
```

Manual alignment of object properties should be avoided.

---

# JSX Formatting

JSX should remain clean and readable.

Long component declarations should be wrapped automatically.

Example:

```jsx
<DistrictCard
  district={district}
  priorityScore={priorityScore}
  onSelect={handleSelect}
/>
```

Developers should allow Prettier to determine wrapping.

---

# Markdown Formatting

Markdown documentation should also be formatted consistently.

Examples include:

- README.md
- Project Sources
- Reports
- Documentation

Consistent Markdown formatting improves readability across all project documentation.

---

# JSON Formatting

JSON files should be formatted automatically.

Examples include:

```text
package.json

launch.json

settings.json
```

Manual alignment or spacing adjustments should not be performed.

---

# CSS Formatting

Custom CSS files should also be formatted automatically.

Example:

```css
.dashboard-card {
  padding: 1rem;
  border-radius: 0.5rem;
}
```

Formatting should remain consistent throughout the project.

---

# Automatic Formatting

Developers are encouraged to enable automatic formatting within their editor.

Typical workflow:

```text
Write Code
      │
      ▼
Save File
      │
      ▼
Prettier Formats File
      │
      ▼
Review Changes
      │
      ▼
Commit Code
```

Automatic formatting reduces unnecessary review comments.

---

# IDE Integration

Editors should be configured to:

- Format on save.
- Use the project's Prettier configuration.
- Avoid conflicting formatting extensions.

Using a consistent editor configuration improves collaboration across the team.

---

# Relationship with ESLint

Prettier is responsible for formatting.

Linting responsibilities remain separate.

Formatting rules should not be duplicated across multiple tools.

Developers should allow each tool to perform its intended responsibility.

---

# Before Committing

Before creating a commit, developers should verify that:

- All supported files have been formatted with Prettier.
- No manual formatting overrides remain.
- Formatting changes have been reviewed.
- Repository formatting remains consistent.

This reduces formatting-related Pull Request feedback.

---

# Prettier Review Checklist

Before submitting code for review, verify that:

- JavaScript files are formatted with Prettier.
- JSX files are formatted with Prettier.
- JSON files are formatted with Prettier.
- CSS files are formatted with Prettier.
- Markdown files are formatted consistently.
- Indentation is consistent.
- Line wrapping follows the formatter.
- No manual formatting overrides remain.
- Formatting remains consistent across the repository.

Following these conventions ensures that the frontend codebase and project documentation remain clean, consistent, readable, and easy to maintain throughout the EVision Telangana project.

# Code Review Checklist

Code review is a critical part of the EVision Telangana development workflow.

Every Pull Request should undergo review to ensure that implementation remains consistent with the approved project architecture, coding standards, and quality expectations.

The objective of code review is to improve code quality, share knowledge, detect defects early, and maintain consistency across the project.

---

# Review Objectives

Every review should verify that the proposed changes are:

- Correct
- Readable
- Maintainable
- Consistent
- Well tested
- Aligned with the approved project documentation

Code review should improve the overall quality of the repository rather than simply approve changes.

---

# General Review Principles

Reviewers should focus on:

- Correctness
- Maintainability
- Simplicity
- Consistency
- Architectural compliance

Reviews should remain constructive, objective, and solution-oriented.

---

# Architecture Compliance

Verify that the implementation follows the approved System Architecture.

Confirm that:

- API routes contain no business logic.
- Services implement business rules.
- Repositories handle database access.
- SQLModel models represent database entities only.
- Frontend components remain presentation-focused.
- Layer dependencies follow the approved architecture.

No architectural boundaries should be violated.

---

# Repository Organization

Verify that:

- Files are located in the correct directories.
- Naming conventions are followed.
- New modules fit naturally into the existing repository structure.
- No unnecessary directories have been introduced.

Repository organization should remain predictable.

---

# Coding Standards

Confirm that implementation follows the approved Coding Standards.

Review:

- Naming conventions
- Function design
- Class design
- Import organization
- Formatting
- Type hints
- Documentation

The repository should appear consistent regardless of the contributor.

---

# Readability

Verify that the code is easy to understand.

Reviewers should consider:

- Descriptive names
- Logical organization
- Small functions
- Small classes
- Clear control flow
- Minimal nesting

If additional explanation is required to understand the implementation, the code may require simplification.

---

# Business Logic

Verify that business rules are implemented correctly.

Business logic should:

- Be centralized within the Service Layer.
- Avoid duplication.
- Remain deterministic.
- Match the approved project scope.

Reviewers should verify correctness as well as implementation quality.

---

# Database Compliance

Confirm that database changes remain consistent with the approved Database Schema.

Review:

- Table definitions
- Relationships
- Constraints
- SQLModel models
- Repository queries

Undocumented schema changes should not be introduced.

---

# API Compliance

Verify that API implementations match the approved API Specification.

Review:

- Endpoint paths
- HTTP methods
- Request schemas
- Response schemas
- Status codes
- Error handling

The implemented API should remain fully consistent with the documented contracts.

---

# Data Contract Compliance

Verify that generated datasets and machine learning artifacts remain consistent with the approved Data Contracts.

Review:

- Dataset structure
- File naming
- Column naming
- Output formats
- Validation rules

Implementation should not introduce undocumented data structures.

---

# Error Handling

Reviewers should confirm that:

- Exceptions are handled appropriately.
- Specific exception types are used.
- Error messages are meaningful.
- Sensitive information is not exposed.
- API error responses remain consistent.

Unexpected failures should be logged appropriately.

---

# Logging

Verify that:

- Important events are logged.
- Appropriate log levels are used.
- Sensitive information is not logged.
- Debugging statements have been removed.

`print()` statements should not remain in production code.

---

# Documentation

Confirm that:

- Public modules include docstrings.
- Public classes include docstrings.
- Public functions include docstrings where appropriate.
- Related documentation has been updated if implementation changed.

Documentation should remain synchronized with the codebase.

---

# Comments

Review comments to ensure they:

- Explain _why_ rather than _what_.
- Are accurate.
- Are still relevant.
- Do not duplicate the implementation.

Outdated comments should be removed.

---

# Type Hints

Verify that:

- Public functions include type hints.
- SQLModel models use explicit types.
- Pydantic schemas use explicit types.
- Optional values are annotated correctly.
- `Any` is avoided unless justified.

Type annotations should improve clarity without introducing unnecessary complexity.

---

# Testing

Confirm that:

- Appropriate tests have been added.
- Existing tests continue to pass.
- Error scenarios are covered.
- New business logic is tested.
- No existing functionality has regressed.

Features should not be merged without appropriate test coverage.

---

# Formatting

Verify that:

- Ruff formatting has been applied to Python code.
- Ruff linting passes.
- Prettier formatting has been applied where applicable.
- Imports are organized correctly.
- No unnecessary formatting changes are included.

Formatting should be consistent across the repository.

---

# Security

Reviewers should verify that:

- No secrets have been committed.
- Environment variables are used correctly.
- Sensitive information is not exposed.
- Input validation is present.
- Unsafe code patterns are avoided.

Security should be considered even though advanced authentication is outside the approved MVP scope.

---

# Performance

Verify that implementation:

- Avoids unnecessary database queries.
- Avoids duplicated computations.
- Uses appropriate algorithms.
- Does not introduce premature optimization.

Correctness and maintainability remain the primary priorities.

---

# Git Hygiene

Confirm that:

- Commit history is logical.
- Commit messages follow the approved convention.
- Feature branches remain focused.
- Unrelated changes are excluded from the Pull Request.

Each Pull Request should represent one logical unit of work.

---

# Final Review Checklist

Before approving a Pull Request, verify that:

- ✅ The implementation follows the approved architecture.
- ✅ Repository organization remains consistent.
- ✅ Coding standards have been followed.
- ✅ Naming conventions are consistent.
- ✅ Business logic is correctly implemented.
- ✅ Database changes match the approved schema.
- ✅ API implementation matches the API Specification.
- ✅ Data Contracts remain satisfied.
- ✅ Error handling is appropriate.
- ✅ Logging follows project standards.
- ✅ Documentation has been updated where necessary.
- ✅ Comments remain accurate and useful.
- ✅ Type hints are complete and consistent.
- ✅ Tests have been added or updated.
- ✅ Ruff and Prettier formatting have been applied.
- ✅ No security issues have been introduced.
- ✅ Performance considerations are reasonable.
- ✅ The Pull Request is focused, readable, and ready to merge.

---

# Approval Criteria

A Pull Request is ready for approval only when:

- It satisfies the approved project scope.
- It complies with all Project Sources.
- It follows the Coding Standards defined in this document.
- All review comments have been addressed.
- Automated checks pass successfully.
- The implementation is maintainable, readable, and production-ready for the project's approved MVP.

Consistently applying this review checklist ensures that EVision Telangana maintains a high-quality, well-structured, and collaborative codebase throughout its development lifecycle.

# Best Practices Summary

This section summarizes the key implementation principles that every contributor should follow throughout the EVision Telangana project.

These best practices reinforce the detailed standards defined throughout this document and serve as a quick reference during development.

---

# General Development

- Write simple, readable, and maintainable code.
- Follow the approved System Architecture.
- Keep implementations modular.
- Prefer clarity over cleverness.
- Refactor duplicated code.
- Avoid unnecessary complexity.

---

# Project Organization

- Place files in their approved directories.
- Keep one primary responsibility per file.
- Keep one logical responsibility per directory.
- Respect the approved Repository Structure.
- Avoid introducing unnecessary modules.

---

# Naming

- Use descriptive names.
- Follow the approved naming conventions.
- Avoid unnecessary abbreviations.
- Maintain consistent terminology throughout the project.
- Prefer explicit names over short names.

---

# Functions

- Keep functions small.
- Perform one logical task per function.
- Use descriptive names.
- Include type hints.
- Return predictable values.
- Avoid hidden side effects.

---

# Classes

- Keep classes focused.
- Follow the Single Responsibility Principle.
- Prefer composition over inheritance.
- Keep constructors lightweight.
- Separate business logic from data models.

---

# Backend Development

- Keep API routes lightweight.
- Place business logic in the Service Layer.
- Use repositories for database access.
- Validate requests using Pydantic.
- Follow the approved API Specification.

---

# Database

- Keep SQLModel models free of business logic.
- Follow the approved Database Schema.
- Use explicit relationships.
- Use descriptive field names.
- Maintain schema consistency.

---

# Frontend Development

- Build reusable React components.
- Keep components focused.
- Centralize API communication.
- Use Tailwind CSS consistently.
- Remove development console statements before committing.

---

# Machine Learning

- Keep preprocessing reproducible.
- Preserve deterministic outputs.
- Store trained models in the approved location.
- Follow the approved Data Contracts.
- Separate training code from runtime inference.

---

# Error Handling

- Validate inputs early.
- Raise meaningful exceptions.
- Catch specific exception types.
- Never suppress unexpected errors.
- Return consistent API error responses.

---

# Logging

- Use the standard logging module.
- Log meaningful events.
- Use appropriate log levels.
- Avoid excessive logging.
- Never log sensitive information.

---

# Documentation

- Keep documentation synchronized with implementation.
- Document public modules, classes, and functions.
- Update Project Sources when implementation changes require it.
- Keep documentation concise and accurate.

---

# Comments

- Explain _why_, not _what_.
- Remove outdated comments.
- Avoid redundant comments.
- Do not leave commented-out code.
- Keep TODO comments specific and actionable.

---

# Type Hints

- Annotate public interfaces.
- Use modern Python type syntax.
- Avoid unnecessary use of `Any`.
- Keep annotations consistent.
- Continue validating runtime input.

---

# Imports

- Follow the approved import ordering.
- Remove unused imports.
- Avoid wildcard imports.
- Prefer absolute imports.
- Prevent circular dependencies.

---

# Testing

- Test business logic.
- Test API endpoints.
- Test validation.
- Test error scenarios.
- Keep tests deterministic and independent.

---

# Formatting

- Format Python code with Ruff.
- Format frontend code with Prettier.
- Keep imports organized.
- Do not manually override automated formatting.
- Maintain formatting consistency across the repository.

---

# Collaboration

- Follow the approved Git Workflow.
- Keep Pull Requests focused.
- Write meaningful commit messages.
- Participate in code reviews.
- Address review feedback constructively.

---

# Security

- Never commit secrets.
- Use environment variables for configuration.
- Validate external input.
- Avoid exposing internal implementation details.
- Follow secure coding practices even within the MVP scope.

---

# Continuous Improvement

Developers are encouraged to continuously improve the codebase by:

- Refactoring when appropriate.
- Removing duplication.
- Improving readability.
- Simplifying implementations.
- Updating documentation.
- Strengthening automated tests.

Code quality should improve over time without deviating from the approved project scope or architecture.

---

# Final Development Principles

Every contributor should strive to ensure that their code is:

- Correct
- Readable
- Maintainable
- Modular
- Well documented
- Properly tested
- Consistently formatted
- Architecturally compliant
- Easy for teammates to understand

Following these best practices ensures that the EVision Telangana codebase remains professional, consistent, and maintainable throughout the entire project lifecycle.

---

# Coding Standards Governance

This document serves as the authoritative implementation standard for the EVision Telangana project.

All contributors are expected to follow the conventions and practices defined throughout this document.

---

## Authority

The Coding Standards document governs implementation conventions across the entire project.

It complements, but does not replace, the approved:

- Final Project Scope
- Master Roadmap
- Final Tech Stack
- System Architecture
- Repository Structure
- Git Workflow
- API Specification
- Database Schema
- Data Contracts

Where conflicts arise, project scope and architectural documents take precedence over implementation preferences.

---

## Applicability

These standards apply to:

- Backend development
- Frontend development
- Machine learning implementation
- Data preprocessing
- Database implementation
- API development
- Testing
- Documentation
- Project utilities

Every contributor is responsible for adhering to these standards.

---

## Exceptions

Exceptions to these standards should be rare.

Any deviation should:

- Have a clear technical justification.
- Improve the implementation without compromising maintainability.
- Be discussed and agreed upon by the team before adoption.

Personal preference alone is not sufficient justification for deviating from the approved standards.

---

## Future Revisions

As the project evolves, these standards may be refined to address new implementation requirements.

Any updates should:

- Remain consistent with the approved project architecture.
- Preserve backward consistency where practical.
- Be reviewed and agreed upon by the team.

Changes should be documented before they are adopted.

---

## Compliance

Before merging code into the main branch, contributors should verify that their implementation:

- Follows the approved Coding Standards.
- Passes formatting and linting checks.
- Includes appropriate documentation.
- Includes appropriate testing.
- Complies with all relevant Project Sources.

Code reviews should verify compliance with these standards.

---

## Final Statement

The Coding Standards document establishes a common implementation language for the EVision Telangana team.

By following these conventions consistently, the project will maintain a clean, readable, maintainable, and collaborative codebase that aligns with the approved architecture, technology stack, and project objectives from initial development through final delivery.
