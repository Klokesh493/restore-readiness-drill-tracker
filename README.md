# Restore Readiness Drill Tracker

A backup is only useful if a restore meets recovery time and data loss objectives. Drill results need to expose missed targets.

## What I built

I built a recovery drill checker that compares observed restore duration to RTO and lost data time to RPO. It lists a workload whenever either target is missed.

## How it works

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

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [restore_tracker.py](restore_tracker.py) implements the CLI and decision rules. Uses `csv` to read tabular exports. |
| Make | Runs the documented example and the local `unittest` suite. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 restore_tracker.py sample_drills.csv
```

The archive workload appears in the failed-drill output. [Full expected output](examples/Demo%201.stdout.txt)

### Additional replay cases

- **Last sample record in isolation** · `python3 restore_tracker.py examples/last-record.csv` · [Expected output](examples/Last%20sample%20record%20in%20isolation.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

The tool checks reported drill results. Schedule a restore drill to produce evidence for any untested workload.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
