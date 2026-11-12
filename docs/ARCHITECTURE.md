# Restore Readiness Drill Tracker architecture

Tracks restore drill results and flags workloads that missed RTO or RPO targets.

```mermaid
flowchart LR
    N0["sample_drills.csv"]
    N1["restore_tracker.py"]
    N2["evaluate / failures"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
