---
metadata_version: 1
id: "tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9"
kind: "page"
parent_id: "tycho.landing.b656116463d9480f83199d8202b127a4"
canonical_path: "book/decisions/cross-domain-modernization-and-adr-examples.md"
title: "Cross-domain architecture decisions and modernization under constraints"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Reader entry for Cross-domain architecture decisions and modernization under constraints. Scope includes 1. Four valid starting points; 2. First example: a burst does not imply a service split; 3. Second example: runtime modernization without data loss."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Cross-domain architecture decisions and modernization under constraints?"
  prerequisites: []
  related_ids:
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.f784d6ef723c4c0e8836ff9085bf7dcc"
    - "tycho.page.dc2470904e004a4aa733abcdb25517ed"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
    - "tycho.page.9176c39f97f544f884666e291ae38b90"
    - "tycho.page.ded52d8d012347b79d70e608488cf6a4"
    - "tycho.page.0d34dd26886340b89fd4f1499d790a81"
    - "tycho.page.ea94649bfd8c4be183f9114618d7ccaa"
    - "tycho.page.2536d18422944e27abe4ea8549beb9ab"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.page.dde63373c50f4f4a80e727b6e160def5"
    - "tycho.page.0b493340594c4c4392c5d93940a7f319"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Cross-domain"
    - "architecture"
    - "decisions"
    - "and"
    - "modernization"
    - "under"
    - "constraints"
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
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# Cross-domain architecture decisions and modernization under constraints

> Tycho E14-12 [issue #90](https://github.com/rouslanbaranov/tycho/issues/90), original synthesis of existing canonical models and technical chapters, 2026-10-19. All scenarios are fictional and all outcomes conditional. No live modernization project, benchmark, review board decision or independent domain review is claimed.

## Purpose and mission

Architecture selection is a process of excluding proven bad fits, measuring unknowns and comparing the cost of feasible options. There is no universally preferable topology: a modular monolith, a service split, asynchronous queue or caching tier can each be correct under different state ownership, failure and workload constraints.

**Question:** Given a requirement, an operational symptom, a legacy constraint or a modernization objective, how do we select an architecture and a safe transition with auditable evidence rather than fashionable technology names?

Canonical methods already exist: [requirements/workload](../../authoring/models/requirements-workload-profile.md), [legacy baseline](../../authoring/models/legacy-modernization-profile.md), [pattern applicability](../../authoring/models/pattern-applicability-card.md), [ADR comparison](../../authoring/models/candidate-comparison-adr.md), [target/transition architecture](../../authoring/models/target-transition-architecture.md) and [decision navigation](../../authoring/models/decision-navigation.md). This chapter applies them rather than inventing a second framework.

## 1. Four valid starting points

| Entry | What is actually known? | First discriminating task | Premature answer to avoid |
|---|---|---|---|
| **Requirement** | A wanted outcome, not its implementation | Quantify workloads, user-visible quality targets, hard constraints, data ownership | Select microservices merely because future growth is mentioned |
| **Symptom** | An observed failure or service-level degradation, not necessarily root cause | Correlate offered/completed demand, latency, retries, queues and dependency state | Replace synchronous calls with Kafka because p99 increased |
| **Legacy constraint** | Existing runtime/data/API boundaries that cannot all change at once | Inventory versions, consumer compatibility, committed state and operational ownership | Recommend big-bang rewriting as a universal migration |
| **Modernization objective** | Desired reduction in risk or cost/change latency | Compare retain, in-place upgrade, branch-by-abstraction and extraction | Assume independent deployment is the goal itself |

A valid outcome may be **retain**, **stabilize first**, **measure first**, **conditional candidate**, **contraindicated** or **insufficient evidence**. An agent or reviewer should be able to trace each exclusion to a named hard requirement and a specific supporting source or experiment.

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

Relevant technical chapters: [queueing](../performance/queueing-littles-law.md), [capacity experiments](../performance/workload-profiles-and-capacity-experiments.md), [connection pools](../scaling/connection-pools-hikaricp-pgbouncer.md), [idempotency](../distributed/transactional-outbox-and-idempotency.md).

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

An irreversible new-format commit can make an image-only rollback unsafe. The [progressive delivery chapter](../delivery/progressive-delivery-and-schema-evolution.md) and [target-versus-transition model](../../authoring/models/target-transition-architecture.md) own the full failure/repair rules.

**Decision state:** CONDITIONAL_CANDIDATE for in-place upgrade; insufficient evidence for a big-bang service extraction until the needed independent data/API boundary is demonstrated.

## 4. Third example: a slow query may not need a cache

**Synthetic symptom:** p99 latency increased during evening bursts. One proposal is to add a distributed cache.

Competing hypotheses:
1. Connection pool wait is growing while backend DB CPU is not saturated.
2. One hot aggregate key serializes otherwise cheap writes.
3. The SQL access path changed and scans more data.
4. Retry storm amplifies downstream calls.
5. Read traffic is high and repetitive with a tolerable staleness budget.

A cache addresses only a subset of these causes and can create **invalidated reads, stampedes, credential/data isolation concerns and another failure path**. Measure query traces, actual DB plans, pool waiting, key skew, cacheability, write invalidation and acceptable staleness before selecting.

| Candidate | Helps only if | Falsifying observation |
|---|---|---|
| Tune query/index | Slow plan is measurable and fixable | Plan already optimal; delay elsewhere |
| Right-size pool/timeouts | Pool wait limits actual throughput | Dependency CPU/lock is bottleneck; more connections worsen it |
| Cache selected reads | High repeated reads with bounded staleness and clear invalidation | Low reuse, strict freshness or write-heavy hotspots |
| Shard data | Independent partitions with distributed ownership justified | One hot key dominates; split does not remove serialization |
| Separate read model | Different read projections/workload justify denormalized state | Lag/consistency contract is incompatible |

Read [PostgreSQL query plans](../data/postgresql-mvcc-indexes-and-query-plans.md), [cache invalidation](../scaling/local-distributed-caching-and-invalidation.md), and [shard hotspots](../scaling/shard-keys-hotspots-and-resharding.md). Correctness and retrieval freshness are first-class criteria, not afterthoughts.

**Decision state:** INSUFFICIENT_EVIDENCE. The next action is instrumenting the suspected boundary with a source-anchored query plan and user-visible latency trace.

## 5. Fourth example: high availability is not a deployment logo

**Synthetic requirement:** an application must continue a limited read journey after a zone loss, with a separate objective for authoritative state restoration after a region loss.

Options include multi-zone pre-provisioned capacity, standby region with replicated state or backup-and-restore. The right choice depends on *different failure classes and RPO/RTO objectives*, role fencing, service access, data correctness and the ability to restore a named user journey.

Two active regions can be inappropriate when they introduce conflicting writes and no reconciled ownership policy. A single region with a practiced restore can outperform a superficially redundant setup against the *specific* required disaster class, if the time/loss targets permit it.

Read [deployment/control-plane](../deployment/runtime-placement-and-control-plane.md), [disaster recovery](../deployment/multi-region-disaster-recovery-contracts.md) and [safe rollout](../delivery/safe-rollout-and-recovery.md). The correct outcome is not a deployment selection unless actual drills and data reconciliation support it.

## 6. Security and cost are hard gates, not a ranking afterthought

A candidate that violates object authorization, tenant isolation, data restoration or permissions boundaries is not a viable choice even when it appears fastest or easiest to deploy. The [security architecture chapter](../security/identity-authorization-and-isolation.md) describes mandatory enforcement and failure checks; a gateway cannot compensate for missing resource-level authorization.

Likewise, evaluate *total operating cost*: components, retention/egress, high-cardinality telemetry, staff skills, on-call load, separate environments, dependency lifecycle, recovery drills and irreversible migration expense. A small deployment count is not a sufficient proxy for lower total ownership cost, and a high RPS figure is not a sufficient reason to introduce distributed state.

## 7. Reproducible decision record (original synthetic ADR)

**ADR-SYN-04: retain the single registration state owner while instrumenting burst behavior.**

- **Status:** PROPOSED, no real stakeholder acceptance.
- **Context:** hypothetical temporary surge; success invariant and client feedback timing matter; actual bottleneck unmeasured.
- **Hard constraints:** no double-confirmed seat, bounded user deadline, one authoritative state writer; old API compatibility through any trial.
- **Alternatives:** A retain+instrument; B admission/queue; C service extraction with independent store.
- **Decision:** select **measure first**; provisionally retain A. Consider B only if admission semantics fit and a controlled experiment demonstrates service protection. Do not choose C without a proven separation benefit and migration plan.
- **Evidence:** source-linked queueing, pooling and transaction chapters; **no production data**.
- **Falsification:** measured offered arrivals, bottleneck, logical duplicates, p99 and retry amplification show existing design cannot meet defined constraints after smaller safe changes.
- **Transition:** no irreversible change authorized; instrument and run bounded experiments; record rollback for any admission policy.
- **Review trigger:** workload shift, new hard isolation requirement, repeated exhausted resource boundary or failed controlled capacity experiment.

The [arc42 architecture decisions guidance](https://docs.arc42.org/section-9/) explains why important decisions should record alternatives and rationale; this original ADR is **not** an implementation of an accepted organization-specific governance process.

## 8. Verification and question-answering contract

A complete answer for an engineering choice should include:
- user outcome and exact system/source boundaries,
- workload, error/failure class and old data/API constraints,
- assumptions separated from inspected source claims and measured values,
- at least the retained/simple option and realistic alternatives,
- disqualifiers, operational/security costs and irreversible transition risks,
- a falsifiable measurement, test or source request for unknowns,
- decision status, accountable review and a revisiting condition.

When the question lacks a workload profile, ownership model or mandatory permission constraints, the valid answer may be **MEASURE_FIRST** or **INSUFFICIENT_EVIDENCE**. No universal number of requests, nodes, services or team members chooses microservices, Kafka, distributed caches or vector retrieval.

This synthesis relies on canonical Tycho material rather than inventing a hidden knowledge graph; a page or source reference must be read and verified at its actual version before making a consequential decision.

## 9. Research and review status

Source grounding: existing inspected-source ledgers in [queueing](../performance/queueing-littles-law.md), [outbox](../distributed/transactional-outbox-and-idempotency.md), [Kafka](../integration/kafka-partitions-replication-and-contracts.md), [safe rollout](../delivery/safe-rollout-and-recovery.md) and [security](../security/identity-authorization-and-isolation.md); [arc42 §9](https://docs.arc42.org/section-9/) inspected 2026-10-19 for decision documentation principles.

**Open research:** no organization-specific runtime/operational requirements, real data-set or distributed traces, independent architecture review, deployment experiment, SLO/cost budget or results are available for the scenarios. All numerical/comparative recommendations remain conditional and falsifiable. Completion of the manuscript chapter is not a completed architecture modernization project or 100% coverage of the ten-volume outline.

## Applied M9 evidence: what transfers and what does not

The following historical cases are **time-scoped publisher/practitioner reports**, not a Tycho benchmark or proof of a universal architecture choice. Any associated decision playbook is an **original synthetic comparison**, not a decision made by the companies cited. These cases inform the specific mechanism and contraindications above:

- **[Agent-assisted migration safety](../cases/decisions/agentic-migration-safety.md)** illustrates synthetic ADR requires behavior, isolation and evidence gates before agent-generated code can change production. **It cannot establish:** shopify/Spotify reports do not provide authorization for fully autonomous unsafe changes or benchmarked universal agent correctness.

A different system must recheck its workload, source date, version, authority boundary and failure/recovery acceptance criteria before transferring any decision. See the case's own evidence ledger for exact public references and unresolved claims.
