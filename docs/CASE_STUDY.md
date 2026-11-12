# Restore Readiness Drill Tracker walkthrough

## Business problem

Tracks restore drill results and flags workloads that missed RTO or RPO targets.

## Reproduce the workflow

Run `python3 restore_tracker.py sample_drills.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
archive
```

The sample supplies these fields. `workload`, `restore_minutes`, `rto_minutes`, `data_loss_minutes`, `rpo_minutes`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
