---
metadata_version: 1
id: "tycho.landing.be90d29e1bc04524b2ea41ee9beaab0f"
kind: "landing"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/application/README.md"
title: "Foundations and application architecture — researched entry"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Reader entry for Foundations and application architecture — researched entry. Scope includes How the material fits together; Research pages; Related existing book content."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Foundations and application architecture — researched entry?"
  prerequisites: []
  related_ids:
    - "tycho.page.a2cd4465792a4740aa5150ad248fd420"
    - "tycho.page.b42e3ffc4a924b7089d261d0a3dc33b0"
    - "tycho.page.a06fd146f96b4b17a754f4d3b608ebdf"
    - "tycho.page.76244dbe2bd44035b7154f821191f6f2"
    - "tycho.page.31cda61d174248eaa326559d256ce352"
    - "tycho.page.4318e542ac7e445b9e8b3150effd2cff"
    - "tycho.page.06b70cb83d4f490ea9ef698a025e7684"
    - "tycho.page.4681b3ba9e234c46bdb4b5993634b0e3"
    - "tycho.page.31c8e450f78c451d90cb6090df330c5a"
    - "tycho.page.77b512c4e2e946bd92d70b4a714600c8"
    - "tycho.page.acb452608a8b42898aae7482c27f5f04"
    - "tycho.page.c226850223614886b61b7cb36c7d5032"
    - "tycho.page.47ffb5c160bd4b10aff27101414c2133"
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Foundations"
    - "and"
    - "application"
    - "architecture"
    - "researched"
    - "entry"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-18"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

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
| Which operational, cost, support and environment hard gates limit an architecture? | [Operational constraints and total-cost gates](operational-constraints-and-total-cost-gates.md) | V01/C06; public arc42/AWS principles and original eligibility comparison, review pending |
| How do tenant-specific identity, data authority and resources affect module boundaries? | [Authorization boundaries and multitenancy](authorization-boundaries-and-multitenancy.md) | V02/C07; OWASP and public tenancy models, original negative cases, review pending |
| Which actors, external interfaces and authoritative effects define the system before choosing a style? | [Problem framing and system boundaries](problem-framing-and-system-boundaries.md) | V01/C01 original arc42/C4 context and evidence-scope draft; independent review pending |
| What outcomes, constraints and quality attributes should drive architecture choices? | [Architecture drivers, quality scenarios and readable views](quality-drivers-and-architecture-views.md) | Source-grounded draft: arc42, public SRE Workbook and C4 |
| Where are business models, data authority, contracts and cross-context mappings owned? | [Domain boundaries, data ownership and contract evolution](domain-boundaries-data-ownership-and-contracts.md) | V02/C02 public bounded-context/arc42 evidence and original makerspace cases; unreviewed |
| When and how can an anti-corruption adapter translate incompatible models during a migration? | [Anti-corruption adapters and coexistence](anti-corruption-adapters-and-coexistence.md) | V02/C06 public ACL/Strangler references and original failure paths; unreviewed |
| How are application-layer and port/adapter dependencies directed and enforceable? | [Layered and hexagonal design](layered-hexagonal-ports-and-adapters.md) | V02/C01; original testable responsibility/port layout and Cockburn primary source; not executed |
| When do SOA/microservice remote boundaries justify independent deployment costs? | [Service orientation and microservices](service-orientation-microservices-and-distribution.md) | V02/C04; OASIS 1.0 and Fowler/Lewis scope plus original failure comparisons; not executed |
| How do those styles interact, historically? | [Combined application-style research](architecture-styles-and-module-boundaries.md) | Preserved source research; not a single canonical chapter owner for V02/C01 or V02/C04 |
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
