---
metadata_version: 1
id: "tycho.page.a726b2ab751b44dea1a659556ed4f4c6"
kind: "page"
parent_id: "tycho.landing.b656116463d9480f83199d8202b127a4"
canonical_path: "book/decisions/requirements-to-transition-decision-playbooks.md"
title: "Architecture decisions: from requirements, symptoms and legacy constraints to safe transition"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Reader entry for Architecture decisions: from requirements, symptoms and legacy constraints to safe transition. Scope includes 1. A shared decision envelope; 2. Route R1: a new requirement → feasible architecture; 3. Route R2: operational symptom → competing hypotheses."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Architecture decisions: from requirements, symptoms and legacy constraints to safe transition?"
  prerequisites: []
  related_ids:
    - "tycho.page.06b70cb83d4f490ea9ef698a025e7684"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.f784d6ef723c4c0e8836ff9085bf7dcc"
    - "tycho.page.dc2470904e004a4aa733abcdb25517ed"
    - "tycho.page.02238832b395417bae63939cd96b9134"
    - "tycho.page.9176c39f97f544f884666e291ae38b90"
    - "tycho.page.1c7350e3bc17483ba18f201d02727aea"
    - "tycho.page.47ffb5c160bd4b10aff27101414c2133"
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.page.ea94649bfd8c4be183f9114618d7ccaa"
    - "tycho.page.2536d18422944e27abe4ea8549beb9ab"
    - "tycho.page.ddeff7f1556f44f18c67659b73e6e15f"
    - "tycho.page.6b9a3f5c7bae455ab4f56f151f17b406"
    - "tycho.page.58c3c4e5e19d46bcb2da66255eb61068"
    - "tycho.page.7921e82a71b9446790f185c818326911"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Architecture"
    - "decisions"
    - "from"
    - "requirements"
    - "symptoms"
    - "and"
    - "legacy"
    - "constraints"
    - "safe"
    - "transition"
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

# Architecture decisions: from requirements, symptoms and legacy constraints to safe transition

> Tycho E14-12 [issue #90](https://github.com/rouslanbaranov/tycho/issues/90), original cross-topic book chapter, 2026-10-19. All worked scenarios are **synthetic**; assumptions, results and verification requests are not measurements of a deployed system. Canonical decision authoring contracts exist separately in [decision navigation](../../authoring/models/decision-navigation.md), [requirement profiles](../../authoring/models/requirements-workload-profile.md), [legacy baseline](../../authoring/models/legacy-modernization-profile.md), [candidate ADRs](../../authoring/models/candidate-comparison-adr.md), [pattern cards](../../authoring/models/pattern-applicability-card.md) and [target/transition states](../../authoring/models/target-transition-architecture.md).

## Purpose and mission

Architecture knowledge becomes useful when a reader can move from a real question to **only the relevant mechanisms**, test incompatible assumptions, rule out unsafe candidates and produce a decision with an evidence boundary. This chapter provides four worked **decision routes**, not an automatic product recommender.

Every route must end with one of four outcomes:

1. **Conditional selection:** a candidate passes hard gates under explicit workload and operating conditions, with remaining review/tests recorded.
2. **Retain or improve current design:** distribution/technology replacement does not demonstrate justified benefit over bounded optimizations.
3. **Measure first:** a finite discriminating experiment separates plausible bottlenecks and risks.
4. **Insufficient evidence:** a hard correctness/recovery/security assumption remains unknown and must block irreversible action.

A list of attractive technologies without a baseline, competing options and falsifiable gates is **not** an architectural decision.

## 1. A shared decision envelope

| Field | Obligation and evidence |
|---|---|
| User outcome | Named workflow and observable successful/failed effect, not just an implementation style |
| Workload | Offered versus admitted traffic, concurrency, operation mix, item skew, data size and growth window |
| Invariants | Data ownership, uniqueness, transaction boundaries, idempotency, authorization, durability |
| Failure class | Timeouts, dependency loss, partial commit, region loss, policy error, overload, schema mismatch |
| Deployment context | Team operations, compatibility, clients/consumers, delivery authority, recovery resources |
| Hard gates | Requirements that eliminate a candidate regardless of attractiveness |
| Alternatives | **Always** include retaining the current architecture (or simplest feasible greenfield baseline) |
| Evidence | Source/revision and inspected section; measured observations versus published mechanism versus hypothesis |
| Experiments | Smallest bounded test that would change decision; negative cases and owner |
| Target state | Desired responsibility/data/deployment boundaries and measurable acceptance |
| Transition state | Coexistence, stages, rollback/forward recovery, irreversible effects and stop conditions |

The evidence ledger of the canonical technical page remains authoritative. An ADR may cite the ledger but must not silently strengthen a provisional source claim.

## 2. Route R1: a new requirement → feasible architecture

**Synthetic requirement:** an event-registration system has a strict confirmed-capacity invariant and must tolerate brief upstream retry storms. No actual offered RPS, database transaction holding time or client retry policy is supplied.

**Candidates**

| Alternative | Potential fit | Contraindication | Proof needed |
|---|---|---|---|
| Keep a modular monolith and one transactional owner | One database can atomically check capacity and insert registration | Single-writer throughput/availability constraints may be violated | Observe lock waits, business SLIs, restore and horizontal-read needs |
| Separate HTTP admission tier, retain single authority | Cap ingress and queue/retry amplification without distributing write truth | Admission queues can hide timeouts or shed valuable users | Offered/admitted/completed rate, user outcomes, fairness and retry budget |
| Split registration into independent services | Ownership may aid independent deployment if teams/components evolve separately | Cross-service capacity invariant becomes ambiguous if jointly owned | Proven domain boundary, transactional ownership, saga/reconciliation failure plan |

**Decision:** neither the phrase high load nor a retry spike justifies decomposition. Start from an explicit transactional owner and measured admission limits. Refer to [quality drivers](../volumes/v01/c03/quality-drivers-and-architecture-views.md), [outbox/idempotency](../distributed/transactional-outbox-and-idempotency.md), [queueing](../volumes/v07/c01/queueing-littles-law.md) and [workload experiments](../performance/workload-profiles-and-capacity-experiments.md).

**Experiment:** apply an open-arrival load schedule with recorded dropped iterations, skewed workshop key and concurrent confirmations; verify capacity never exceeds the business limit, inspect lock waits and p99/error outcomes. A closed-load generator alone can hide offered overload. The test cannot be called passed until executed.

## 3. Route R2: operational symptom → competing hypotheses

**Synthetic symptom:** a Java API's p99 increases during load while CPU remains moderate. A dashboard shows frequent connection acquisition waits; request fan-out and retries are unknown.

Competing hypotheses require different evidence:

| Hypothesis | Predicted observation | Discriminating test |
|---|---|---|
| Database pool too small | Connection acquisition time grows but DB may have spare safe capacity | Observe pool active/idle/pending, DB transaction time, concurrent connections and DB waits |
| Slow DB query/transaction | Connections remain borrowed for long intervals; DB plan/locks show increased service demand | Compare query plans, lock/WAL/I/O, transaction duration and fan-out |
| Executor starvation/blocking | Queue and worker utilization increase independently of DB service time | Thread/virtual-thread diagnostics, scheduler and blocked-stack evidence |
| Retry amplification | Attempt rate exceeds logical user-work rate after dependency errors | Capture attempt IDs, retry counts, deadlines and downstream admission |
| Shared hot-key serialization | One workshop ID dominates blocked writes while aggregate utilization looks moderate | Key-level latency distribution and lock ownership/skew traces |

The first action is **not** to raise every pool size. More connections can worsen DB contention; virtual threads increase in-flight capacity but do not increase finite external resource budgets. Read [pooling](../volumes/v03/c05/connection-pools-hikaricp-pgbouncer.md), [Java execution](../volumes/v03/c02/platform-threads-executors-and-virtual-threads.md), [PostgreSQL plans](../data/postgresql-mvcc-indexes-and-query-plans.md) and [observability metrics](../observability/metrics-slo-timeseries-architecture.md).

**Outcome:** measure first. A hypothesis that predicts a different signal is falsifiable. The simplest safe change may be shortening transactions, bounding admission or fixing a query, not creating a service boundary.

## 4. Route R3: legacy constraint → architecture exclusions

**Synthetic baseline:** a modular monolith stores workshop registrations with a tightly coupled relational schema. Old long-running background workers consume messages for several days. The modernization objective is smaller deployable units without interrupting registrations.

Hard constraints:
- one authoritative capacity check must remain atomic;
- old workers may process events created before/during rollout;
- events can be replayed after temporary failure;
- restoring the old application image must not make newly committed registrations unreadable;
- no original runtime/build/artifact telemetry has yet been gathered.

**Excluded as currently proposed:** moving ownership of the capacity counter into a separate independently writable service while both old and new systems write it. This loses the identified invariant unless a specific coordination/transaction protocol is evidenced.

**Credible options:** (A) retain modular monolith, improve module interfaces and deployment testability; (B) extract *read-only* query/reporting with a versioned feed while retaining the write owner; (C) extract only a bounded notification responsibility via transactional outbox, retaining the canonical database authority.

| Transition phase | Invariant | Stop gate / recovery |
|---|---|---|
| Observe baseline | Known writers, readers, external clients and event retention | Unknown legacy reader/version: no destructive migration |
| Expand compatibility | Old and new binaries can read additive state | Old/new fixture matrix fails: remain on old writes |
| Shadow/read-only extraction | One authoritative writer, shadow output not user-authoritative | Divergence grows: disable shadow, reconcile |
| Controlled switch | New consumers decode historic events, retry safely | Lag/correctness gate fails: stop promotion |
| Retire old paths | No unknown old writers or replay obligations | Old clients still active: postpone contract |
| Contract | Proven restoration/forward recovery after irreversible change | No restore drill: no destructive removal |

The target architecture and safe transition are different artifacts. Read [architecture evolution](../application/architecture-evolution-and-extraction.md), [progressive delivery](../delivery/progressive-delivery-and-schema-evolution.md), [safe recovery](../delivery/safe-rollout-and-recovery.md) and [target/transition contract](../../authoring/models/target-transition-architecture.md).

**Outcome:** retain/write-owner first, then conditionally extract read paths or notifications. No distributed migration should be inferred from a headline objective of modularity.

## 5. Route R4: modernization objective → measured improvement

**Synthetic objective:** lower incident recovery time and regional exposure. The existing service has a durable primary database in one region, daily backups and one application deployment; restore times and data-loss windows were never measured.

A tempting proposal is instant multi-region active/active deployment. The proposal is **inadmissible without conflict resolution, authoritative writer/election/fencing, cross-region network failure policy, data reconciliation and actual replica lag evidence**.

Compare:

| Option | Possible value | Hidden risk and test |
|---|---|---|
| Retain single region, improve restore/backup discipline | Restore procedure with low standing complexity | Timed restore from independently protected artifact; data integrity |
| Multi-zone single-region + remote backup | Survive some zonal failures while keeping one data owner | Same-region control/data dependencies, backup corruption, failover |
| Warm standby second region | Faster service restoration for some named failures | Replica age/consistency, configuration drift, warm-up and credential readiness |
| Active/active multi-region | Regional serving redundancy where correctness protocol supports it | Split-brain/conflict/ordering, divergent acknowledgments and cost |

The actual decision requires user-defined RPO/RTO for **each failure class** and tested restore/failover. Read [deployment topology](../volumes/v08/c03/runtime-placement-and-control-plane.md), [multi-region recovery](../deployment/multi-region-disaster-recovery-contracts.md), [PostgreSQL replication](../volumes/v05/c02/postgresql-wal-replication-and-recovery.md) and [observability](../observability/trace-context-lineage-and-audit.md).

**Outcome:** insufficient evidence. Establish restore baselines before buying multi-region complexity; select the least complex topology demonstrated to meet a stated objective, not the one with the most regions.

## 6. Security as a cross-cutting hard gate

Every route above must re-evaluate identities and authorization when changing service count, data ownership, network boundaries, queues, caches, regions or control planes. Security is not a final polish stage.

- A newly extracted service may accept a token whose audience is a different resource server.
- A new indexed read path may return data for a different tenant unless all query and cache pathways bind authorization to object and property.
- A shadow replica or backup region may lack equally strict encryption keys, access audit and deletion/retention policy.
- Replaying durable messages may execute actions after the original delegated permission expired.
- A more permissive deployment pipeline may expose credentials across untrusted runner boundaries.

Read [identity, authorization and threat models](../security/identity-authorization-threat-models-and-isolation.md) and [CI/CD provenance](../volumes/v08/c01/ci-cd-provenance-and-gitops.md) before accepting irreversible transitions.

## 7. Example ADR — retain the simplest justified option

**ADR-TYCHO-SYN-001 — status: proposed, synthetic**

- **Context:** fictional registration service exhibits increased tail latency and retries during a demand burst; no established saturation cause.
- **Hard requirements:** never confirm capacity above quota; protect participant data; explicit error behavior; recovery from lost acknowledgments.
- **Options:** optimize monolith/admission and DB transaction scope; extract read service; distribute write ownership into services.
- **Decision now:** *measure first and retain a single write authority*. This is a decision **not** to adopt a complex architecture until evidence changes.
- **Known supporting mechanisms:** relational local transaction and conditional updates; bounded admission; idempotency key and result replay; outbox for independent notifications.
- **Unknown:** offered load history, tenant-key skew, DB lock time, retry rate, user SLO, recovery objectives and old-client mix.
- **Experiment:** instrument transaction holds, offered versus admitted work, retry attempts, skew and user-level p99; test simultaneous capacity reservation and lost response using a synthetic fixture.
- **Go/no-go:** a candidate only qualifies after preserving invariant under concurrency, meeting explicitly established workload/SLO gates and demonstrating safe rollback/forward recovery.
- **Alternatives rejected:** immediate independent write ownership **at this evidence stage** due to missing distributed invariant protocol, not a claim that microservices are always wrong.
- **Revisit:** named failure of the simple design on a reproducible workload despite bounded optimization, plus evidence of feasible transition with acceptable cost.

An ADR is a time-scoped record of justified trade-offs, not a universal selection rule. This chapter should link original source passages for mechanism facts instead of claiming that synthetic outcome is experimentally proven.

## 8. Verification and question-set regression

A later book-quality review can evaluate representative questions, with hard failure states:

| Test question | Required behavior | Explicit fail condition |
|---|---|---|
| Can 10,000 active users mean 10,000 RPS? | Ask for arrival rates, active sessions, operation mix, attempts and think time | Converts user count into RPS without assumptions |
| Does Kafka producer exactly-once imply one external side effect? | Distinguish Kafka transactional scope from consumer external system | Claims arbitrary external exactly once |
| Will more virtual threads fix slow DB calls? | Separate in-flight execution from DB connection and transaction budgets | Assumes downstream resources scale automatically |
| Can rolling back a container undo a schema change? | Check mixed-version compatibility and committed data state | Treats binary and data rollback as identical |
| Does active/active imply zero RPO? | Demand replication/ack/fencing/conflict evidence | Equates region count with loss guarantees |
| Is a valid token sufficient to read any object? | Apply object/property/tenant authorization | Equates authentication with permission |
| Is graph search required to answer these routes? | Use canonical metadata, sections, source evidence and conditional reasoning | Invents curated graph relationships as prerequisite |

No executable agent-search benchmark or human adjudication was performed for this chapter. The question set is **proposed editorial regression material**.

## 9. Source and evidence limits

The mechanism pages linked above contain their scoped public source-to-claim ledgers (Kafka 4.1 design, PostgreSQL 17 docs, Kubernetes, OpenTelemetry, official runtime docs). This synthesis adds only **original conditional reasoning**. It does not claim first-hand inspection of every source cited in another chapter, and does not override the source version or documented uncertainty of those chapters.

The four routes, thresholds, table entries and ADR are all synthetic; there is no measured selection success, live legacy assessment, performance comparison, independent technical review or external system modernization. Those facts must be obtained for real architecture decisions.
