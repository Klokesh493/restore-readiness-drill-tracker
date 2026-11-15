# Skills and verification

## What this repository demonstrates

A recovery drill checker that compares observed restore duration to RTO and lost data time to RPO. It lists a workload whenever either target is missed.

## Reproduce the result

The archive workload appears in the failed-drill output. Reproduce the primary fixture with `python3 restore_tracker.py sample_drills.csv`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

The tool checks reported drill results. Schedule a restore drill to produce evidence for any untested workload.

Separate restore duration from data loss. A workload can satisfy one recovery target while missing the other.

[restore_tracker.py](../restore_tracker.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
