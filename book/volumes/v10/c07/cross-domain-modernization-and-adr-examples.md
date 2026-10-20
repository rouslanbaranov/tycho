---
metadata_version: 1
id: "tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9"
kind: "page"
parent_id: "tycho.chapter.5fb14670d0b24967a5e6c24df7221d74"
canonical_path: "book/volumes/v10/c07/cross-domain-modernization-and-adr-examples.md"
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

Canonical methods already exist: [requirements/workload](../../../../authoring/models/requirements-workload-profile.md), [legacy baseline](../../../../authoring/models/legacy-modernization-profile.md), [pattern applicability](../../../../authoring/models/pattern-applicability-card.md), [ADR comparison](../../../../authoring/models/candidate-comparison-adr.md), [target/transition architecture](../../../../authoring/models/target-transition-architecture.md) and [decision navigation](../../../../authoring/models/decision-navigation.md). This chapter applies them rather than inventing a second framework.

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

Relevant technical chapters: [queueing](../../v07/c01/queueing-littles-law.md), [capacity experiments](../../../performance/workload-profiles-and-capacity-experiments.md), [connection pools](../../v03/c05/connection-pools-hikaricp-pgbouncer.md), [idempotency](../../../distributed/transactional-outbox-and-idempotency.md).

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

Read [PostgreSQL query plans](../../../data/postgresql-mvcc-indexes-and-query-plans.md), [cache invalidation](../../../scaling/local-distributed-caching-and-invalidation.md), and [shard hotspots](../../v05/c05/shard-keys-hotspots-and-resharding.md). Correctness and retrieval freshness are first-class criteria, not afterthoughts.

**Decision state:** INSUFFICIENT_EVIDENCE. The next action is instrumenting the suspected boundary with a source-anchored query plan and user-visible latency trace.

## 5. Fourth example: high availability is not a deployment logo

**Synthetic requirement:** an application must continue a limited read journey after a zone loss, with a separate objective for authoritative state restoration after a region loss.

Options include multi-zone pre-provisioned capacity, standby region with replicated state or backup-and-restore. The right choice depends on *different failure classes and RPO/RTO objectives*, role fencing, service access, data correctness and the ability to restore a named user journey.

Two active regions can be inappropriate when they introduce conflicting writes and no reconciled ownership policy. A single region with a practiced restore can outperform a superficially redundant setup against the *specific* required disaster class, if the time/loss targets permit it.

Read [deployment/control-plane](../../v08/c03/runtime-placement-and-control-plane.md), [disaster recovery](../../../deployment/multi-region-disaster-recovery-contracts.md) and [safe rollout](../../../delivery/safe-rollout-and-recovery.md). The correct outcome is not a deployment selection unless actual drills and data reconciliation support it.

## 6. Security and cost are hard gates, not a ranking afterthought

A candidate that violates object authorization, tenant isolation, data restoration or permissions boundaries is not a viable choice even when it appears fastest or easiest to deploy. The [security architecture chapter](../../v09/c05/identity-authorization-and-isolation.md) describes mandatory enforcement and failure checks; a gateway cannot compensate for missing resource-level authorization.

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


### Complete synthetic ADR: improve a legacy reservation service without a forced decomposition

**Original fictional baseline (not a real benchmark):** one Java modular application and one PostgreSQL authority manage 12,000 accounts. A timed event presents a proposed 120 new intents/s during 15 seconds; no verified ingress trace exists. SLO requirement: correct exclusive booking decisions with a bounded user-visible deadline. Constraints: the current public contract must remain supported, no simultaneous independent booking writers, limited on-call capacity, and a reversible first rollout. No real organizational approval or cost quotes exist.

| Candidate | Hypothesis | Hard gate | Observation that reverses preference |
|---|---|---|---|
| A — Retain modular architecture, improve SQL/admission | Database and queue behavior may be optimized without remote calls | One authoritative booking transaction; old clients supported | Controlled load still misses accepted completion requirement after safe changes |
| B — Durable admission queue for booking commands | Queue protects one hot authority during burst | Product permits pending/async responses; durable operation ID and backlog visibility | Clients require immediate final confirmation or backlog recovery breaches deadline |
| C — Extract booking service with independent datastore | Boundary-specific scaling and team autonomy repay distribution cost | Verified migration of state authority, fencing, mixed-client compatibility and on-call ownership | No independently measured boundary gain, or invariant fails in coexistence |

**Decision:** `MEASURE_FIRST`, provisionally A; this is not approval to deploy. Collect offered-versus-delivered load, correct completions, DB pool waits, per-key contention, retries, p99 and an explicit source snapshot. If A fails a fair test and product semantics accept pending work, evaluate B next. Candidate C requires a separate source-of-truth migration and a demonstrated operating benefit, not simply a higher peak RPS estimate.

| Transition state | What is deployed and authoritative | Gate and recovery |
|---|---|---|
| T0 baseline | Existing Java service and PostgreSQL writer | Capture trace/model, pinned code and restorable data |
| T1 observe and bound | Instrumentation and bounded admission, **same database writer** | Revert configuration if admission harms correct outcomes; no domain-data move |
| T2 pilot alternate | Canary queue/adapter for a permitted cohort, old API semantics preserved | Reconcile accepted command IDs; hold promotion on unknown/duplicate effects |
| T3 optional authority transition | Only after evidence favors C: compatible old/new clients, a *fenced* single writer | Prove identity mapping, replay and failback; never let two owners independently confirm |
| T4 stabilize / retire | Remove legacy path only after replay horizon and restore proof | Document irreversible state and forward-repair route; old binary rollback may be unsafe |

**Failure test:** commit a booking before losing the response, then retry while the canary is switching. Correctness is *one logical booking and a discoverable outcome*, not "one HTTP request." An interrupted migration must preserve one accepted authority and known restoration options. If real requirements, acceptable queue semantics or authoritative failure telemetry remain unknown, the final recommendation stays **INSUFFICIENT_EVIDENCE**.

**Transfer evidence limits:** the [Shopify modular-monolith case](../../../cases/shopify-modular-monolith.md) supports conditional modularity, [Uber DOMA](../../../cases/uber-doma-domains.md) illustrates governing distributed domain dependencies, and [Stripe's online migration](../../../cases/stripe-online-subscriptions-migration.md) illustrates staged change of data ownership. None establishes that this invented application should adopt its historical architecture. The numbers, options, states and acceptance tests above are invented; **no modernization, rollback or benchmark was performed**.

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

Source grounding: existing inspected-source ledgers in [queueing](../../v07/c01/queueing-littles-law.md), [outbox](../../../distributed/transactional-outbox-and-idempotency.md), [Kafka](../../v04/c07/kafka-partitions-replication-and-contracts.md), [safe rollout](../../../delivery/safe-rollout-and-recovery.md) and [security](../../v09/c05/identity-authorization-and-isolation.md); [arc42 §9](https://docs.arc42.org/section-9/) inspected 2026-10-19 for decision documentation principles.

**Open research:** no organization-specific runtime/operational requirements, real data-set or distributed traces, independent architecture review, deployment experiment, SLO/cost budget or results are available for the scenarios. All numerical/comparative recommendations remain conditional and falsifiable. Completion of the manuscript chapter is not a completed architecture modernization project or 100% coverage of the ten-volume outline.

## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Agent-assisted migration safety](../../../cases/decisions/agentic-migration-safety.md)**. **Relevant mechanism or architectural contrast:** Synthetic ADR requires behavior, isolation and evidence gates before agent-generated code can change production. **Not established by this report/playbook:** Shopify/Spotify reports do not provide authorization for fully autonomous unsafe changes or benchmarked universal agent correctness.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.

<!-- tycho-edition-navigation -->

## Edition navigation and evidence scope

| Route | Destination |
|---|---|
| Parent chapter | [Question, conclusions and reading route](README.md) |
| Parent volume | [Volume synthesis](../README.md) |
| Book | [Authoritative contents](../../../README.md) |
| Source versions and access scope | [Registered sources](../../../../sources/README.md) and the exact page-local citation ledger above |

The original manuscript was accepted under #213 at the recorded baseline. Earlier draft/review labels describe historical authoring events. Source access, versions, unexecuted experiments and nonclaims retain their original scope; assembly does not assert a new source read or benchmark. The chapter landing adds editorial synthesis and navigation.
