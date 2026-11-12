# Restore Readiness Drill Tracker architecture

Tracks restore drill results and flags workloads that missed RTO or RPO targets.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
