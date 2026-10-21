---
metadata_version: 1
id: "tycho.page.2eb290f6307f4797a5981510f1248d70"
kind: "page"
parent_id: "tycho.chapter.5fb14670d0b24967a5e6c24df7221d74"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c07-cross-domain-worked-comparisons-and-unresolved-cases/workload-runtime.md"
title: "Workload and runtime modernization comparisons"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Which bottleneck and migration invariant distinguish the first alternatives?"
route_hints:
  questions:
    - "Which bottleneck and migration invariant distinguish the first alternatives?"
  prerequisites:
    - "tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9"
  related_ids:
    - "tycho.chapter.5fb14670d0b24967a5e6c24df7221d74"
    - "tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9"
    - "tycho.page.22b12598c23b4fc5ac74b1adc960ebe5"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "workload"
    - "runtime"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Workload and runtime modernization comparisons

**Owning question:** Which bottleneck and migration invariant distinguish the first alternatives?

This page belongs to [V10/C07 — Cross-domain worked comparisons and unresolved cases](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9:1 -->
## 1. Four valid starting points

| Entry | What is actually known? | First discriminating task | Premature answer to avoid |
|---|---|---|---|
| **Requirement** | A wanted outcome, not its implementation | Quantify workloads, user-visible quality targets, hard constraints, data ownership | Select microservices merely because future growth is mentioned |
| **Symptom** | An observed failure or service-level degradation, not necessarily root cause | Correlate offered/completed demand, latency, retries, queues and dependency state | Replace synchronous calls with Kafka because p99 increased |
| **Legacy constraint** | Existing runtime/data/API boundaries that cannot all change at once | Inventory versions, consumer compatibility, committed state and operational ownership | Recommend big-bang rewriting as a universal migration |
| **Modernization objective** | Desired reduction in risk or cost/change latency | Compare retain, in-place upgrade, branch-by-abstraction and extraction | Assume independent deployment is the goal itself |

A valid outcome may be **retain**, **stabilize first**, **measure first**, **conditional candidate**, **contraindicated** or **insufficient evidence**. An agent or reviewer should be able to trace each exclusion to a named hard requirement and a specific supporting source or experiment.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9:2 -->
## 2. First example: a burst does not imply a service split

**Synthetic requirement:** the registration journey must serve sudden surges while preserving a one-seat-per-confirmed-registration invariant. Observed client arrivals, peak duration, key skew, database wait and retry amplification are initially unknown.

Compare:

- **A: retain a modular monolith and instrument** offered/admitted/completed requests, per-key contention, DB connection acquisition, latency histograms and queue age. Least structural change; evidence can disprove the need for new topology.
- **B: add bounded admission/queue discipline** before the bottleneck when explicit rejection or deferral is permitted. Stabilizes resource use but creates fairness, capacity and retry behavior that must be measured.
- **C: extract a registration service** with a separate data ownership boundary. Independent scaling may help if component-specific capacity is the actual limiter; this introduces network failure, consistency, observability and migration costs.

| Hard gate or observation | A | B | C |
|---|---|---|---|
| Current data ownership must remain serializable for seat allocation | Existing local transaction might meet it | Queue does not replace transaction correctness | Must design cross-boundary authority and migration |
| Client requires synchronous confirmation | Compatible if processing finishes within deadline | Deferral may violate contract | Still needs a confirmation boundary |
| Offered load and bottleneck unknown | Measure first | **Do not select until measured** | **Not justified** |
| Strict operational simplicity | Often favorable | Additional queue budgets | More running parts and failure paths |
| Safe reversible experiment | Instrumentation baseline | Controlled bounded gate under synthetic load | Extraction needs compatibility/restore plan |

**Decision state:** MEASURE_FIRST, not “adopt option C”. A bounded experiment would compare A/B at identical offered arrival schedule, preserving logical outcomes and capturing p95/p99, retries, admission and DB waits. Any claimed gain from C needs independent load and correctness evidence before architecture approval.

Relevant technical chapters: [queueing](../../v07-performance-scale-and-resilience/c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md), [capacity experiments](../../../performance/workload-profiles-and-capacity-experiments.md), [connection pools](../../v03-execution-concurrency-and-flow-control/c05-thread-connection-and-buffer-pools/connection-pools-hikaricp-pgbouncer.md), [idempotency](../../../distributed/transactional-outbox-and-idempotency.md).

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9:3 -->
## 3. Second example: runtime modernization without data loss

**Synthetic objective:** retire an aging runtime while continuing to accept existing external clients. Unknowns are language/framework compatibility, data format, old-client lifetime, contract owner and acceptable downtime.

**Target candidate:** a supported runtime in the same deployment with unchanged public API. This may be simpler than service decomposition. If internal implementation changes cannot be made atomically, adopt branch-by-abstraction or a compatible migration step, **without changing the externally visible state owner by default**.

### Target is not transition

| Time | Versions present | Data and client contract | Safety proof required |
|---|---|---|---|
| T0 old stable | N only | Legacy schema and client contract | Baseline and restore-point evidence |
| T1 expand | N | Compatible additive interfaces/schema | N unaffected under changed storage/API |
| T2 mixed | N and N+1 | Old and new clients/events still active | N/N+1 cross-version reads/writes, idempotency and rejection |
| T3 guarded promotion | Mostly N+1 | New functionality enabled only after measured gates | Actual SLO, data integrity and service compatibility |
| T4 cleanup | N+1 | Old readers/writers retired | No historic replays require old encoding; restore test passes |

An irreversible new-format commit can make an image-only rollback unsafe. The [progressive delivery chapter](../../../delivery/progressive-delivery-and-schema-evolution.md) and [target-versus-transition model](../../../../authoring/models/target-transition-architecture.md) own the full failure/repair rules.

**Decision state:** CONDITIONAL_CANDIDATE for in-place upgrade; insufficient evidence for a big-bang service extraction until the needed independent data/API boundary is demonstrated.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](cross-domain-modernization-and-adr-examples.md) |
| Next | [Continue the reasoning](data-availability.md) |
| Integrated question | [Original scenario and limits](cross-domain-modernization-and-adr-examples.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
