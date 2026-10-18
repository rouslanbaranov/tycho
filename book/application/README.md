# Foundations and application architecture — researched entry

> **Status:** initial evidence-backed material for [Issue #79](https://github.com/rouslanbaranov/tycho/issues/79), not a completed ten-volume book or independently peer-reviewed reference. This is a practical reading route across V01 requirements foundations and V02 application-boundary content, pending final persistent page-ID schema.

## Purpose and mission

Help engineers and AI agents describe architecture in terms of observable business outcomes, quality scenarios, module/domain ownership, and feasible technical/operational changes. The goal is to **compare alternatives under explicit constraints**, not prescribe universal monolith, microservice or SOA preferences.

## How the material fits together

```mermaid
flowchart LR
    Q["Goals and measurable quality scenarios"] --> B["Module / domain / service boundaries"]
    B --> D["Style and deployment choice"]
    D --> M["Legacy modernization and transition"]
    M --> E["Evidence, failure tests and review"]
    E --> Q
```

Text alternative: start from quality drivers, identify cohesive responsibilities, compare architectural styles, design safe modernization paths, and test evidence. Feedback may change the original requirements or decomposition.

## Research pages

| Reader question | Canonical page | Status |
|---|---|---|
| What outcomes, constraints and quality attributes should drive architecture choices? | [Architecture drivers, quality scenarios and readable views](quality-drivers-and-architecture-views.md) | Source-grounded draft: arc42, public SRE Workbook and C4 |
| How do a modular monolith, hexagonal architecture, service orientation, bounded contexts and microservices differ? | [Application architecture styles and module boundaries](architecture-styles-and-module-boundaries.md) | Source-grounded draft: Fowler/Lewis, Cockburn, OASIS and Spring Modulith |
| When should a legacy module remain internal versus become an independently deployed service? | [Architecture evolution and service extraction](architecture-evolution-and-extraction.md) | Source-grounded draft: Cockburn, Fowler and versioned Modulith verification |

These pages explain distinct canonical questions. They cite published source sections and original synthetic failures; none was verified by running a real domain/application architecture experiment.

## Related existing book content

- [Requirements and workload profile](../../authoring/models/requirements-workload-profile.md) — reusable information-gathering contract, not a performance test.
- [Queueing and measurement](../performance/queueing-littles-law.md) — exact occupancy/throughput/latency boundaries.
- [Transactional outbox and idempotency](../distributed/transactional-outbox-and-idempotency.md) — cross-boundary event effects and retries.
- [Safe rollout and recovery](../delivery/safe-rollout-and-recovery.md) — compatibility, rollback/forward recovery and RPO/RTO evidence.

## Missing coverage and further research

DDD primary reference text and comprehensive domain modeling, specific hexagonal implementations beyond original pattern intent, code-level module verification on an executable fixture, broad SOA governance alternatives, empirical style comparisons, measured teams/cost and independent expert review remain outside this bounded chapter set.

The proposed full [Tycho structure](../PROPOSED-STRUCTURE.md) continues to own those topics. Neither the navigation diagram nor the page count proves book completion.
