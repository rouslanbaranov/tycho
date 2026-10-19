# Performance, scaling and resilience — research landing

Status: **several independently researched technical pages**, not a completed volume. This landing page only links to pages that exist and states which questions remain open; it does not stand in for an approved table of contents.

## Purpose and mission

Explain how workload, service demand, queueing, tail latency, saturation and failure affect software architecture selection. Readers and AI agents should be able to distinguish derived mathematical relationships, directly observed workload properties and unresolved resource-capacity questions before recommending scale-out or redistribution.

## Research navigation map

```mermaid
flowchart LR
    Demand["Arrivals and offered load"] --> Work["Queue, service and exits"]
    Work --> Means["Mean work and residence time"]
    Means --> Limits["Finite-window and tail-latency limits"]
    Limits --> Experiments["Load tests and failure experiments"]
```

Text alternative: establish demand and work boundaries before interpreting mean occupancy; then examine sampling limitations and validate hypotheses through controlled experiments. This is a navigation map, not an assertion that all related chapters are complete.

## How the research questions connect

```mermaid
flowchart LR
    Q["Workload / architecture question"] --> M["Define request and measurement boundary"]
    M --> L["Queueing and Little's Law: researched page"]
    L --> E{"Sufficient evidence to decide?"}
    E -->|No| X["Measure offered load, queueing and bottlenecks"]
    E -->|Yes| T["Compare bounded mitigation hypotheses"]
    X --> E
    T --> R["Validate under normal and degraded load"]
```

The chart is an **original reading and decision map**, not a simulated production system. The linked queueing, capacity-experiment, fan-out and autoscaling pages are researched drafts; other diagram boxes are diagnostic steps, not claims that a complete volume exists.

## Available research

| Reader question | Canonical researched page | Status / evidence |
|---|---|---|
| How do arrivals, logical operations, resource demand, concurrency and skew define a workload? | [Workload and arrival models](workload-demand-and-arrival-models.md) | V01/C02; original examples and public k6/queueing boundary, not a workload forecast |
| When is a benchmark invalid because the generator, denominators or fixture changed? | [Load testing and benchmark validity](load-testing-and-benchmark-validity.md) | V07/C03; independently published k6 and histogram-model scope, no test executed |
| What can mean in-flight work, throughput and residence time establish, and when is Little's Law misapplied? | [Queueing, Little's Law and measurement boundaries](queueing-littles-law.md) | Public-source-grounded draft from a fixed 2013 paper and specifically inspected k6/SRE documentation; not a benchmark or human-reviewed capacity study |
| How should offered load, failure and capacity hypotheses be tested? | [Workload profiles and capacity experiments](workload-profiles-and-capacity-experiments.md) | Source-bound methodology and synthetic examples; not a production load test |
| Why do p99 and user-visible deadlines worsen under dependency fan-out? | [Tail latency, fan-out and deadline budgets](tail-latency-fanout-and-deadline-budgets.md) | New V07/C04 evidence-based draft; no live tail benchmark |
| When does autoscaling help, and what do startup lag and shared limits invalidate? | [Autoscaling lag and capacity limits](autoscaling-lag-and-capacity-limits.md) | New V07/C06 draft against Kubernetes/AWS public docs; no executed platform test |

## Planned questions — **not yet written**

- Contention, coordination and scaling laws: evidence of shared-bottleneck saturation.
- Deeper cross-resource contention and capacity scaling-law comparisons.
- Overload shedding, recovery capacity and cost trade-offs beyond the bounded existing fan-out/autoscaling pages.

The planning owners are listed in the [proposed book structure](../PROPOSED-STRUCTURE.md). The source-reading procedure and stopping conditions are in the [research workflow](../../authoring/RESEARCH-WORKFLOW.md).

## Cross-domain boundaries

Execution-model and connection-pool specifics belong to a future execution volume. Database shard placement belongs to the future data volume. This page intentionally does not duplicate those explanations or create dead links to nonexistent chapters.

## Research limits and next actions

This is the initial mechanism pilot [#38](https://github.com/rouslanbaranov/tycho/issues/38). See its chapter ledger for public-source scope, numerical example classification, unanswered experimental questions and review status. Subsequent research pilots cover event publication [#39](https://github.com/rouslanbaranov/tycho/issues/39) and recovery [#40](https://github.com/rouslanbaranov/tycho/issues/40).
