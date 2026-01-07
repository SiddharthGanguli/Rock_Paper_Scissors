# Contributing Guide

This document explains how to contribute to the **Rock Paper Scissors** project.  
Please read it carefully before writing or submitting any code.

The goal is to keep the project stable, readable, and easy to collaborate on.

---

## Project Workflow Overview

- The `main` branch always contains **stable code**
- No one pushes directly to `main`
- All changes happen through **feature branches**
- Every change must be reviewed before merging

---

## Branch Rules

### Default Branch
- `main` is the default and protected branch
- It should always be in a working state

### Creating a Branch
Create a new branch for each task:

```bash
git checkout main
git pull
git checkout -b feature/<your-name>/<task-name>
```

### Branch Naming Format

```bash
feature/<your-name>/<short-task-description>
```

Example : 

```bash
feature/himadri/model-evaluation
feature/siddhartha/data-ingestion
feature/siddhartha/api-ui
```


File Ownership
Each contributor is assigned specific files in ```TASKS.md```
You should only modify files assigned to you
If a change affects another file, discuss it before making changes
This avoids conflicts and keeps responsibilities clear.


### Commit Guidelines

Each commit should represent one meaningful change.
```bash
Add model evaluation metrics
Implement accuracy calculation
Refactor evaluation helper function

```

### Pushing Changes

After committing:
```bash
git push -u origin feature/<your-name>/<task-name> 

```

### Communication : 

If you are unsure about:
Your task
File ownership
How to implement something

Ask before making changes.