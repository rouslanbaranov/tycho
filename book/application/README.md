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
| How should evidence and competing hypotheses be tested before deciding on an architecture? | [Architecture evidence and decision experiments](architecture-evidence-hypotheses-and-experiments.md) | V01/C04 original controlled decision method; no experiment executed |
| How do context, static, runtime and deployment views remain coherent with ADRs? | [Architecture views and decision records](architecture-views-and-decision-records.md) | V01/C05 public arc42 view/decision sources; fictional example and review pending |
| What do internal events, transactions and module checks guarantee inside a modular monolith? | [Modular monolith and internal events](modular-monolith-and-internal-events.md) | V02/C03 public Spring transactions/Modulith reference; no code/test run |
| Which actors, external interfaces and authoritative effects define the system before choosing a style? | [Problem framing and system boundaries](problem-framing-and-system-boundaries.md) | V01/C01 original arc42/C4 context and evidence-scope draft; independent review pending |
| What outcomes, constraints and quality attributes should drive architecture choices? | [Architecture drivers, quality scenarios and readable views](quality-drivers-and-architecture-views.md) | Source-grounded draft: arc42, public SRE Workbook and C4 |
| Where are business models, data authority, contracts and cross-context mappings owned? | [Domain boundaries, data ownership and contract evolution](domain-boundaries-data-ownership-and-contracts.md) | V02/C02 public bounded-context/arc42 evidence and original makerspace cases; unreviewed |
| When and how can an anti-corruption adapter translate incompatible models during a migration? | [Anti-corruption adapters and coexistence](anti-corruption-adapters-and-coexistence.md) | V02/C06 public ACL/Strangler references and original failure paths; unreviewed |
| How do a modular monolith, hexagonal architecture, service orientation, bounded contexts and microservices differ? | [Application architecture styles and module boundaries](architecture-styles-and-module-boundaries.md) | Source-grounded draft: Fowler/Lewis, Cockburn, OASIS and Spring Modulith |
| When should a legacy module remain internal versus become an independently deployed service? | [Architecture evolution and service extraction](architecture-evolution-and-extraction.md) | Source-grounded draft: Cockburn, Fowler and versioned Modulith verification |
| How do public HTTP/RPC contracts survive retries, timeouts and old/new client versions? | [HTTP and RPC contracts, compatibility and deadlines](http-rpc-contracts-and-compatibility.md) | New source-grounded draft (V02/C05); RFC 9110, RFC 9457, OpenAPI 3.2.1, gRPC and Protocol Buffers; review pending |

These pages explain distinct canonical questions. They cite published source sections and original synthetic failures; none was verified by running a real domain/application architecture experiment.

## Related existing book content

- [Requirements and workload profile](../../authoring/models/requirements-workload-profile.md) — reusable information-gathering contract, not a performance test.
- [Queueing and measurement](../performance/queueing-littles-law.md) — exact occupancy/throughput/latency boundaries.
- [Transactional outbox and idempotency](../distributed/transactional-outbox-and-idempotency.md) — cross-boundary event effects and retries.
- [Safe rollout and recovery](../delivery/safe-rollout-and-recovery.md) — compatibility, rollback/forward recovery and RPO/RTO evidence.

## Missing coverage and further research

Direct verification of the original proprietary DDD reference text and broader domain modeling, specific hexagonal implementations beyond original pattern intent, code-level module verification on an executable fixture, broad SOA governance alternatives, empirical style comparisons, measured teams/cost and independent expert review remain outside this bounded chapter set.

The proposed full [Tycho structure](../PROPOSED-STRUCTURE.md) continues to own those topics. Neither the navigation diagram nor the page count proves book completion.
