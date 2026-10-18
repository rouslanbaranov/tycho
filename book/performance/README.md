# Performance, scaling and resilience — research landing

Status: **initial researched content**, not a completed volume. This landing page only links to pages that exist and states which questions remain open; it does not stand in for an approved table of contents.

## Purpose and mission

Explain how workload, service demand, queueing, tail latency, saturation and failure affect software architecture selection. Readers and AI agents should be able to distinguish derived mathematical relationships, directly observed workload properties and unresolved resource-capacity questions before recommending scale-out or redistribution.

## Available research

| Reader question | Canonical researched page | Status / evidence |
|---|---|---|
| What can mean in-flight work, throughput and residence time establish, and when is Little's Law misapplied? | [Queueing, Little's Law and measurement boundaries](queueing-littles-law.md) | Public-source-grounded draft from a fixed 2013 paper and specifically inspected k6/SRE documentation; not a benchmark or human-reviewed capacity study |

## Planned questions — **not yet written**

- Contention, coordination and scaling laws: evidence of shared-bottleneck saturation.
- Representative load tests, arrival distributions, coordinated omission and response-time percentiles.
- Tail latency, retries, fan-out and dependent-service time budgets.
- Overload shedding, autoscaling lag, recovery capacity, degraded-mode behavior and cost trade-offs.

The planning owners are listed in the [proposed book structure](../PROPOSED-STRUCTURE.md). The source-reading procedure and stopping conditions are in the [research workflow](../../authoring/RESEARCH-WORKFLOW.md).

## Cross-domain boundaries

Execution-model and connection-pool specifics belong to a future execution volume. Database shard placement belongs to the future data volume. This page intentionally does not duplicate those explanations or create dead links to nonexistent chapters.

## Research limits and next actions

This is the initial mechanism pilot [#38](https://github.com/rouslanbaranov/tycho/issues/38). See its chapter ledger for public-source scope, numerical example classification, unanswered experimental questions and review status. Subsequent research pilots cover event publication [#39](https://github.com/rouslanbaranov/tycho/issues/39) and recovery [#40](https://github.com/rouslanbaranov/tycho/issues/40).
