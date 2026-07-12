- [Git Workflow](#git-workflow)
- [Purpose](#purpose)
- [Relationship to Other Project Documents](#relationship-to-other-project-documents)
- [Git Workflow Objectives](#git-workflow-objectives)
  - [1. Support Parallel Development](#1-support-parallel-development)
  - [2. Maintain Repository Stability](#2-maintain-repository-stability)
  - [3. Simplify Collaboration](#3-simplify-collaboration)
  - [4. Enable Traceability](#4-enable-traceability)
  - [5. Reduce Merge Conflicts](#5-reduce-merge-conflicts)
  - [6. Support Continuous Integration](#6-support-continuous-integration)
- [Git Workflow Philosophy](#git-workflow-philosophy)
- [Repository Initialization](#repository-initialization)
- [Repository Configuration](#repository-configuration)
- [Branching Strategy](#branching-strategy)
- [Branch Types](#branch-types)
  - [main](#main)
  - [feature/\*](#feature)
  - [docs/\*](#docs)
  - [fix/\*](#fix)
- [Branch Ownership](#branch-ownership)
- [Collaboration Workflow](#collaboration-workflow)
  - [Before Starting Work](#before-starting-work)
  - [During Development](#during-development)
  - [Before Merging](#before-merging)
  - [After Merging](#after-merging)
- [Daily Development Workflow](#daily-development-workflow)
- [Working with Feature Branches](#working-with-feature-branches)
- [Working with Documentation Branches](#working-with-documentation-branches)
- [Commit Message Convention](#commit-message-convention)
- [Pull Request Workflow](#pull-request-workflow)
- [Merge Strategy](#merge-strategy)
- [Merge Conflict Resolution](#merge-conflict-resolution)
- [Conflict Prevention Guidelines](#conflict-prevention-guidelines)
- [GitHub Collaboration Rules](#github-collaboration-rules)
- [Release Workflow](#release-workflow)
  - [Before Feature Freeze](#before-feature-freeze)
  - [After Feature Freeze](#after-feature-freeze)
  - [Final Submission](#final-submission)
- [Repository Maintenance](#repository-maintenance)
- [Common Git Commands](#common-git-commands)
- [Best Practices](#best-practices)
- [Common Mistakes to Avoid](#common-mistakes-to-avoid)
- [Example Development Scenario](#example-development-scenario)
- [Workflow Summary](#workflow-summary)
- [Git Workflow Governance](#git-workflow-governance)
- [Conclusion](#conclusion)


# Git Workflow

**Project:** EVision Telangana  
**Official Project Title:** AI-Based EV Charging Infrastructure Planning and Decision Support System for Telangana

**Version:** 1.0  
**Status:** Frozen  
**Last Updated:** July 2026

---

# Purpose

This document defines the approved Git and GitHub collaboration workflow for EVision Telangana.

It establishes the branching strategy, repository setup, collaboration process, commit conventions, merge strategy, and day-to-day development practices to ensure that all team members can contribute efficiently while maintaining a stable and organized codebase.

The workflow is intentionally designed to be simple enough for a four-member academic project while supporting parallel development throughout the project lifecycle.

This document serves as the authoritative reference for all version control activities during development.

---

# Relationship to Other Project Documents

The Git Workflow document complements the existing project documentation by defining how project changes are managed throughout development.

| Document                         | Purpose                                                                                                   |
| -------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Final Project Scope              | Defines project objectives, datasets, deliverables, and project boundaries.                               |
| Master Roadmap                   | Defines implementation phases, milestones, and daily workflow.                                            |
| Final Tech Stack                 | Defines approved technologies, development tools, and coding practices.                                   |
| System Architecture              | Defines the software architecture and module interactions.                                                |
| Repository Structure             | Defines the physical organization of the project repository.                                              |
| **Git Workflow (This Document)** | Defines version control practices, collaboration workflow, branching strategy, and repository management. |

This document does not introduce new project features, technologies, or architectural changes. It defines how approved implementation work is coordinated using Git and GitHub.

---

# Git Workflow Objectives

The Git workflow has been designed around several primary objectives.

## 1. Support Parallel Development

Allow multiple team members to work simultaneously without interfering with each other's work.

---

## 2. Maintain Repository Stability

Ensure that the main branch always represents a stable and working version of the project.

---

## 3. Simplify Collaboration

Provide a straightforward workflow that can be followed consistently by developers with limited Git experience.

---

## 4. Enable Traceability

Maintain a clear history of project changes through meaningful commits and organized branches.

---

## 5. Reduce Merge Conflicts

Encourage frequent synchronization and small feature branches to minimize integration problems.

---

## 6. Support Continuous Integration

Promote regular integration of completed work instead of delaying merges until the end of development.

---

# Git Workflow Philosophy

EVision Telangana follows a **simple feature-branch workflow**.

Unlike more complex workflows such as Git Flow, this approach emphasizes simplicity, rapid collaboration, and continuous integration.

The workflow has been selected because:

- The project duration is approximately one week.
- The development team consists of four members.
- Multiple modules can be developed independently.
- Simplicity reduces the learning curve.
- Frequent integration reduces final-day merge conflicts.

Every new task is developed in its own branch before being merged into the main branch after verification.

---

# Repository Initialization

The repository should be initialized before implementation begins.

The recommended setup process is:

1. Create the GitHub repository.
2. Clone the repository locally.
3. Configure Git username and email.
4. Add the initial project structure.
5. Commit the initial repository.
6. Push the initial commit to GitHub.
7. Invite all team members as collaborators.
8. Verify repository access for every contributor.

After initialization, every developer should clone the repository rather than downloading project files manually.

---

# Repository Configuration

The repository includes several configuration files that should remain under version control.

These include:

- `.gitignore`
- `.editorconfig`
- `.env.example`
- `README.md`
- `pyproject.toml`
- `uv.lock`
- `package.json`

These files define project configuration, development standards, dependency management, and repository behavior.

Developers should avoid modifying these files unless the change is necessary and agreed upon by the team.

---

# Branching Strategy

The project follows a lightweight branching model.

```
main
│
├── feature/data-processing
├── feature/backend-api
├── feature/ml-training
├── feature/frontend-dashboard
├── feature/ai-assistant
│
├── docs/report
├── docs/presentation
│
└── fix/api-validation
```

Each branch should focus on a single logical task.

Long-running branches should be avoided whenever possible.

---

# Branch Types

## main

Purpose:

Stores the stable version of the project.

Rules:

- Always deployable.
- Always builds successfully.
- Never used for direct development.
- Receives completed work through merges.

---

## feature/\*

Purpose:

Implements new functionality.

Examples:

- feature/backend-api
- feature/dashboard-ui
- feature/model-training
- feature/decision-engine

Feature branches should remain focused on one feature or implementation task.

---

## docs/\*

Purpose:

Develop documentation independently from application code.

Examples:

- docs/report
- docs/presentation
- docs/readme

Documentation updates follow the same review and merge process as source code.

---

## fix/\*

Purpose:

Resolve bugs or defects.

Examples:

- fix/api-error
- fix/map-rendering
- fix/data-validation

Bug-fix branches should contain only the changes required to resolve the identified issue.

---

# Branch Ownership

Although any contributor may assist where necessary, the following ownership guidelines help reduce overlap.

| Team Area                 | Typical Branches                                       |
| ------------------------- | ------------------------------------------------------ |
| Data Engineering & ML     | feature/data-_, feature/ml-_                           |
| Backend & Decision Engine | feature/backend-_, feature/api-_, feature/decision-\*  |
| Frontend & Visualization  | feature/frontend-_, feature/dashboard-_, feature/ui-\* |
| Quality & Communication   | docs/_, fix/_, README updates                          |

Ownership defines the primary contributor for a branch but does not prevent collaboration.

---

# Collaboration Workflow

The Git workflow also serves as the project's collaboration workflow.

Every contributor should follow the same sequence when beginning and completing work.

## Before Starting Work

1. Pull the latest changes from the main branch.
2. Verify that the local repository is up to date.
3. Create a new branch for the assigned task.
4. Switch to the new branch before making changes.

---

## During Development

- Make small, logical commits.
- Commit frequently.
- Push work regularly to GitHub.
- Keep changes focused on the assigned task.
- Avoid unrelated modifications.

---

## Before Merging

- Pull the latest version of the main branch.
- Resolve any merge conflicts.
- Verify that the project builds successfully.
- Test the implemented feature.
- Confirm that documentation has been updated if required.

---

## After Merging

- Delete the merged branch.
- Pull the updated main branch.
- Begin the next task using a new feature branch.

---

# Daily Development Workflow

Every development day should follow the same workflow.

```
Pull Latest Main
        │
        ▼
Create New Branch
        │
        ▼
Develop Feature
        │
        ▼
Commit Changes
        │
        ▼
Push Branch
        │
        ▼
Create Pull Request
        │
        ▼
Review and Merge
        │
        ▼
Delete Branch
        │
        ▼
Update Local Main
```

Following the same workflow every day improves consistency and reduces integration issues.

---

# Working with Feature Branches

Feature branches are used for implementing new functionality.

Recommended workflow:

1. Create a feature branch.
2. Implement the assigned feature.
3. Commit regularly.
4. Push changes to GitHub.
5. Open a Pull Request.
6. Resolve review comments if necessary.
7. Merge into the main branch.
8. Delete the feature branch.

Feature branches should remain short-lived whenever possible.

---

# Working with Documentation Branches

Documentation is developed continuously throughout the project.

Documentation branches may include:

- Report updates
- Presentation updates
- README improvements
- Project Sources
- User documentation

Documentation changes should follow the same workflow as source code.

Keeping documentation synchronized with implementation avoids last-minute documentation work.

---

# Commit Message Convention

Every commit should begin with a descriptive prefix.

Recommended prefixes include:

| Prefix   | Purpose                                           |
| -------- | ------------------------------------------------- |
| feat     | New feature                                       |
| fix      | Bug fix                                           |
| docs     | Documentation update                              |
| refactor | Code restructuring without changing functionality |
| style    | Formatting or styling changes                     |
| test     | Testing updates                                   |
| chore    | Maintenance or configuration changes              |

Examples:

```text
feat: implement district prediction API

fix: resolve dashboard rendering issue

docs: update architecture diagrams

refactor: simplify preprocessing pipeline

test: add API integration tests

chore: update project dependencies
```

Commit messages should describe **what changed**, not **how much work was done**.

---

# Pull Request Workflow

Completed work should be integrated through Pull Requests.

Recommended workflow:

1. Push the completed branch.
2. Create a Pull Request.
3. Review the proposed changes.
4. Resolve feedback if required.
5. Merge into the main branch.
6. Delete the merged branch.

Even in a small academic team, Pull Requests provide an opportunity to verify changes before integration.

---

# Merge Strategy

The project uses a standard merge strategy.

Completed feature branches are merged into the main branch after verification.

Merge commits preserve project history and make it easier to understand how individual features were integrated.

Direct commits to the main branch should be avoided except for urgent repository maintenance when agreed upon by the team.

---

# Merge Conflict Resolution

Merge conflicts should be resolved as soon as they occur.

Recommended procedure:

1. Pull the latest main branch.
2. Identify conflicting files.
3. Review both versions carefully.
4. Preserve the intended functionality.
5. Build and test the project.
6. Commit the resolved changes.
7. Push the updated branch.

Conflicts should never be resolved by deleting another contributor's work without discussion.

---

# Conflict Prevention Guidelines

Most merge conflicts can be avoided through good development practices.

Recommended practices include:

- Pull changes before starting work.
- Push changes regularly.
- Merge completed work promptly.
- Keep branches short-lived.
- Avoid editing unrelated files.
- Coordinate major structural changes with the team.
- Complete one feature before starting another.

---

# GitHub Collaboration Rules

All contributors should follow the same collaboration rules.

- Never develop directly on the main branch.
- Create a new branch for every feature or bug fix.
- Pull the latest main branch before starting work.
- Push work regularly.
- Keep commits small and meaningful.
- Open a Pull Request before merging.
- Resolve conflicts immediately.
- Delete merged branches.
- Do not commit API keys or passwords.
- Do not commit local environment files.
- Do not force-push to the main branch.
- Keep documentation synchronized with implementation.

These practices promote a clean and maintainable repository throughout development.

---

# Release Workflow

The project follows the release schedule defined in the Master Roadmap.

## Before Feature Freeze

Development may include:

- New features
- Bug fixes
- Documentation updates
- Refactoring

---

## After Feature Freeze

Only the following changes are permitted:

- Bug fixes
- Documentation updates
- Presentation improvements
- README updates
- Deployment preparation

No new features should be introduced after the feature freeze milestone.

---

## Final Submission

Before submission:

- Verify the repository builds successfully.
- Confirm all branches have been merged.
- Remove obsolete branches.
- Update the README.
- Verify documentation completeness.
- Confirm the final project structure.
- Push the final version to GitHub.

---

# Repository Maintenance

The repository should remain organized throughout development.

Recommended maintenance activities include:

- Delete merged branches.
- Remove unused files.
- Keep the README updated.
- Synchronize documentation.
- Organize project assets.
- Maintain a clean commit history.
- Verify ignored files remain excluded.

Regular maintenance prevents unnecessary repository clutter.

---

# Common Git Commands

| Command           | Purpose                           |
| ----------------- | --------------------------------- |
| `git clone`       | Clone a repository                |
| `git status`      | View repository status            |
| `git pull`        | Download latest changes           |
| `git add`         | Stage files                       |
| `git commit`      | Save staged changes               |
| `git push`        | Upload commits                    |
| `git branch`      | List branches                     |
| `git switch`      | Switch branches                   |
| `git checkout -b` | Create and switch to a new branch |
| `git merge`       | Merge branches                    |
| `git log`         | View commit history               |

These commands represent the core Git operations required throughout the project.

---

# Best Practices

Developers should follow these best practices throughout implementation.

- Commit small logical changes.
- Pull changes before beginning work.
- Push changes regularly.
- Use descriptive commit messages.
- Keep branches focused on one task.
- Test before merging.
- Update documentation continuously.
- Delete completed branches.
- Keep the repository organized.
- Coordinate major changes with the team.
- Protect sensitive information.
- Review changes before committing.

---

# Common Mistakes to Avoid

The following practices should be avoided.

- Working directly on the main branch.
- Creating excessively large commits.
- Delaying merges for several days.
- Ignoring merge conflicts.
- Force-pushing shared branches.
- Committing API keys.
- Committing local environment files.
- Committing virtual environments.
- Mixing unrelated changes into one commit.
- Forgetting to update documentation.

Avoiding these mistakes improves repository stability and collaboration.

---

# Example Development Scenario

The following example illustrates the recommended workflow.

1. A backend developer is assigned to implement prediction APIs.
2. The developer pulls the latest main branch.
3. A new branch named `feature/backend-api` is created.
4. API endpoints are implemented.
5. Changes are committed using descriptive commit messages.
6. The branch is pushed to GitHub.
7. A Pull Request is opened.
8. The changes are reviewed.
9. The branch is merged into the main branch.
10. The feature branch is deleted.
11. Every team member pulls the updated main branch before starting new work.

This workflow should be followed for every implementation task regardless of project module.

---

# Workflow Summary

The complete development workflow can be summarized as follows.

```text
Pull Latest Main
        │
        ▼
Create Branch
        │
        ▼
Develop
        │
        ▼
Commit Frequently
        │
        ▼
Push Changes
        │
        ▼
Create Pull Request
        │
        ▼
Review
        │
        ▼
Merge into Main
        │
        ▼
Delete Branch
        │
        ▼
Pull Updated Main
```

Following this workflow throughout development supports stable integration, organized collaboration, and consistent project progress.

---

# Git Workflow Governance

This document defines the approved Git and GitHub collaboration workflow for EVision Telangana.

All contributors should follow the branching strategy, collaboration workflow, commit conventions, and repository management practices defined herein.

Workflow changes should only be made when:

- Required by verified implementation constraints,
- Required to resolve collaboration issues,
- Required by the project supervisor, or
- Required to improve repository maintainability without increasing unnecessary complexity.

Changes to the Git workflow must remain consistent with the approved Project Scope, Master Roadmap, Final Tech Stack, System Architecture, and Repository Structure.

---

# Conclusion

The Git Workflow establishes a simple, organized, and collaborative version control strategy for EVision Telangana.

By adopting a lightweight feature-branch workflow, maintaining a stable main branch, encouraging frequent integration, and following consistent commit and collaboration practices, the development team can work efficiently while minimizing conflicts and maintaining a clean project history.

The workflow aligns with the approved project documentation and provides a practical foundation for collaborative development throughout the implementation, testing, documentation, and final submission of the project.
