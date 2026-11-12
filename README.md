# Restore Readiness Drill Tracker

Tracks restore drill results and flags workloads that missed RTO or RPO targets.

Focus: Backup-platform DevSecOps recovery.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 restore_tracker.py sample_drills.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Project walkthrough

```mermaid
flowchart LR
    A["Restore duration and data loss metrics"]
    B["Compare duration to RTO and loss to RPO"]
    C{"Either target missed?"}
    D["Emit failed workload"]
    E["Omit passing workload"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)
