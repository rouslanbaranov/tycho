---
metadata_version: 1
id: "tycho.page.cf0ce38c73e44950aec5a9c2869bee63"
kind: "page"
parent_id: "tycho.landing.b656116463d9480f83199d8202b127a4"
canonical_path: "book/decisions/target-and-transition-architecture-states.md"
title: "Target architecture versus transition states: coexistence, reversibility and recovery"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Reader entry for Target architecture versus transition states: coexistence, reversibility and recovery. Scope includes 1. Keep five distinct contracts; 2. The fictional migration: moving a public catalogue read model; 3. A versioned sequence of safe intermediate states."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Target architecture versus transition states: coexistence, reversibility and recovery?"
  prerequisites: []
  related_ids:
    - "tycho.page.81efb7e6d72349768b6f202845cbe35e"
    - "tycho.page.31c8e450f78c451d90cb6090df330c5a"
    - "tycho.landing.b656116463d9480f83199d8202b127a4"
    - "tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1"
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
    - "tycho.page.4681b3ba9e234c46bdb4b5993634b0e3"
    - "tycho.page.f05854fcc406435bbf38a192bc7ab2f1"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.page.ca056fe720e74a9691ce0c253d9526fc"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Target"
    - "architecture"
    - "versus"
    - "transition"
    - "states"
    - "coexistence"
    - "reversibility"
    - "and"
    - "recovery"
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

# Target architecture versus transition states: coexistence, reversibility and recovery

> **Independent Tycho manuscript draft V10/C05, 2026-10-19.** Original fictional case and decision tables. This chapter applies, but does not replace or copy, the reusable [target/transition authoring model](../../authoring/models/target-transition-architecture.md). No real migration, data movement, approval or restore drill occurred.

## Purpose and mission

A target architecture describes what a system should *eventually be*. It cannot explain how existing clients, stored data, deployments and external effects survive the change. The **transition architecture** is a sequence of real operating configurations in which old and new software may coexist, data ownership is transferred or deliberately retained, and some steps cannot simply be rolled back.

The fundamental reader question is: **What may happen between the old and target designs without violating an invariant?** An attractive future-state diagram has no answer unless it specifies compatibility, authority, evidence and recovery at intermediate steps.

[Fowler's 2024 Strangler Fig explanation](https://martinfowler.com/bliki/StranglerFigApplication.html) motivates gradual replacement rather than assuming a wholesale rewrite is well understood. [Microsoft's Strangler Fig guidance](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) describes façade-based incremental routing, coexistence cost and conditions where the pattern is unsuitable. Neither guarantees a safe migration for a particular data model.

## 1. Keep five distinct contracts

| Contract | Target state must say | Every transition state must additionally say |
|---|---|---|
| Functional ownership | Which capability accepts each user-visible operation | Whether old or new implementation receives each client/version |
| State authority | Where each authoritative entity is written and validated | How double-writing is prevented, which source is current, and how to reconcile |
| API/event semantics | Public operation identity, schema, ordering and errors | Old/new versions simultaneously supported, unknown outcomes and replay horizon |
| Security/operations | Trust boundaries, access control, dependency/service budget | Which principal/role may switch routing or write, and whose on-call can recover |
| Failure and recovery | Long-term RPO/RTO and availability model | Exact cutover rollback window, irreversible effects, restore and forward-repair path |

A target architecture might consist of one improved modular application; a transition need not split services. Conversely, a migration that introduces a second deployment needs extra protection even if the target only promises the same user journey.

## 2. The fictional migration: moving a public catalogue read model

Imagine a standalone community tool catalogue that stores authoritative items and serves a query endpoint from the same runtime. The proposed target moves **read-only search projection** into a specialized index while leaving authoritative item edits in the existing store. The objective is to improve search relevance under a measured query mix, not to rewrite the data authority.

Synthetic assumptions:
- The authoritative store is the sole writer of item metadata.
- Existing clients must continue to get consistent identity and authorization semantics.
- A search projection may lag up to a **hypothetical** approved bound; no real tolerance has been obtained.
- Some callers use exact item IDs, so full-text search must not silently replace exact identity lookup.
- Events may replay, arrive late or be lost in the proposed pipeline unless recovery is designed.

A future-state description could show catalogue writes flowing to an authoritative store, a versioned event/indexing path and query reads from a search projection. But the transition also needs a migration protocol that tests exactly **which query versions and index generations** are live.

## 3. A versioned sequence of safe intermediate states

| State | Routing and ownership | Entry gate | Exit or recovery gate |
|---|---|---|---|
| S0 — Baseline | Old query and write paths; one authoritative store | Pin code, data, client versions and key invariants | Observed baseline and restore evidence exist |
| S1 — Shadow index | Writes remain authoritative; separate index ingests copied updates; clients still read old path | Snapshot/CDC identity, event ordering and safe isolation | Compare source/index records; repair gaps without user exposure |
| S2 — Compatibility reads | A bounded subset of authorized queries uses new index; exact lookup remains authoritative | Old/new client contract, scoped access checks and freshness guard | Failed query can route back **only if** behavior/data assumptions still hold |
| S3 — Bounded promotion | More traffic uses the projection under measured lag and result-quality SLO | Equivalence/quality samples, error budget and no leakage | Revert reader route if safe; replay missing updates by stable ID |
| S4 — Stabilized | Old read path may retire after client/query inventory proves safe | No unsupported clients or queries; recovery drill approved | Removal requires independent no-return approval |

The index is **derived state**. Rebuilding it from the current authoritative store and a compatible event sequence may be safe; deleting that store is not authorized by an index migration. If the project later moves *authoritative writes*, the state machine and consistency requirements must be redesigned; the index example is not proof of safe writer migration.

```mermaid
stateDiagram-v2
    [*] --> Baseline
    Baseline --> Shadow: create isolated derived index
    Shadow --> Compatible: prove identity/freshness and ACL
    Compatible --> Canary: limited read exposure
    Canary --> Stable: correctness and quality gates pass
    Compatible --> Shadow: revert routes if safe
    Canary --> Shadow: stale results / auth failure
    Shadow --> Repair: missing events or failed replay
    Repair --> Shadow: reconcile against authority
    Stable --> [*]
```

Text alternative: start with one authoritative source, build a shadow projection, validate a bounded mixed-version read path, then gradually increase traffic. Failure returns to the previous safe reader path or rebuilds the projection. No automatic restoration or successful real migration is implied.

## 4. When rollback means less than users think

A code rollback is reversible only if:
1. Older binaries still correctly interpret persisted state produced by newer binaries.
2. External clients and asynchronous consumers still accept the older response/event contract.
3. Effects committed during the new release can be reconciled or safely replayed.
4. The old route is still operational and authorized.
5. The rollback itself doesn't reintroduce a known security or correctness defect.

If a new version has written a field with novel meaning, the older version may parse it but make wrong decisions. If the system has sent an irreversible notification or performed an external effect, re-deploying an older container does not retract it. If a database migration removed an old column, old SQL may fail entirely.

Distinguish **reversible before write exposure**, **conditionally reversible during coexistence**, and **forward repair or restore required after irreversible effects**. A restore may lose acknowledged operations if the recovery point predates their commits; state explicitly which business loss is permissible. See [backup/PITR and restore drills](../data/backup-restore-pitr-and-recovery-drills.md).

## 5. Data movement is not a row-count exercise

Even an apparently harmless read-index migration needs to compare *semantics*, not only row totals:

- stable entity/tenant identity and per-object access filters;
- deletions, revocations, updates that cross transaction boundaries and repeated events;
- source revision and index-generation checkpoint;
- replay order, deduplication, late arrivals and incomplete snapshot coverage;
- normal and degraded freshness; clocks and unknown timestamps;
- query modes (identifier, exact match, prefix, full-text) and pagination/ordering guarantees;
- matching visible results under old/new client versions;
- measured cost and operations required to re-index after failure.

A million indexed rows and a million source rows can still disagree on critical values or expose stale access decisions. During a shadow run, measure **source-to-target semantic differences** and model their business significance. Reproducible tests and manual sampling may still miss rare defects, so acceptance must disclose residual risk and recovery limits.

## 6. Alternative migration mechanisms and contraindications

| Mechanism | Fits when | Can fail when |
|---|---|---|
| Internal branch by abstraction | An internal interface can route old/new implementations with one deployable | Components cannot be separated without untested side effects |
| Strangler façade | Requests can be intercepted and routed by capability | Internal callers bypass façade or it becomes a bottleneck |
| Expand/migrate/contract | Supported readers/writers can coexist during additive schema phases | Old client semantics changed despite schema compatibility |
| Shadow reads | Side-effect-free comparisons are possible without user exposure | Shadow requests accidentally mutate authoritative state |
| Event/CDC projection | Derived reads tolerate bounded lag and replay discipline exists | Losing deletes/revocations causes unsafe stale data |
| Big-bang replacement | Tiny well-understood system, feasible downtime, fully proven restoration | Many unknown behaviors, long-tail clients or irreversible writes |

These are conditions, not prescriptive steps. The [Microsoft Strangler Fig pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) explicitly treats the façade as a temporary infrastructure cost and warns that request interception may be impossible. Use [anti-corruption adapters](../application/anti-corruption-adapters-and-coexistence.md) when foreign meanings must be translated.

## 7. Go/no-go and the no-return contract

Before a transition changes authoritative state or retirements become irreversible, require evidence for:

- named change owner and approved versions/assets;
- old/new client × API × data compatibility matrix, including asynchronous readers;
- no overlapping uncoordinated writers;
- tested retry identity and late acknowledgment handling;
- representative user-level integrity/authorization tests;
- source-to-target reconciliation and residual unknowns;
- recovery point, actual restored data validity, maximum permissible loss and time;
- explicit stop/hold mechanism if monitoring misses a fault;
- decommissioning evidence for all old callers/subscriptions.

**Negative synthetic test:** insert then revoke an item permission while the indexing connector is stopped, restart from an older offset, replay the delete and test a stale query. A correct solution either filters by authoritative access at the point of response or refuses the stale result according to the approved policy. Merely reaching a “green” index state is insufficient evidence.

A transition state should end with **an observed gate**, not a calendar milestone. A failure after the no-return point must use an approved forward-repair path rather than fictional rollback.

## 8. Source and nonclaim ledger

| Independently inspected source | Applies to | Not verified |
|---|---|---|
| [Fowler, Strangler Fig, 22 Aug 2024](https://martinfowler.com/bliki/StranglerFigApplication.html) | Incremental outcomes-led displacement and coexisting capabilities | Feasibility for the hypothetical catalogue |
| [Microsoft, Strangler Fig pattern, revision available 2026](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) | Interception/coexistence, façade bottleneck and inapplicability conditions | Actual routing, data integrity or recovery |
| [arc42 Architecture Decisions §9](https://docs.arc42.org/section-9/) | Decision context, evidence, alternatives and consequences | Approval of any migration design |
| [Tycho target/transition authoring model](../../authoring/models/target-transition-architecture.md) | Existing independent workflow and scope fields | Executed migration, model conformance or external test |

The example, diagrams, client versions, recovery gates and migration states are original hypothetical material, not production facts. No architecture approval, full repository boundary check, deployed migration, source snapshot verification or independently reviewed acceptance is claimed.

## Navigation

Proposed **V10/C05**, currently [decision support landing](README.md). Prerequisites: [legacy baseline](legacy-baseline-and-modernization-evidence.md), [API compatibility](../application/http-rpc-contracts-and-compatibility.md), [data ownership](../application/domain-boundaries-data-ownership-and-contracts.md). Next: [architecture alternatives/ADR](architecture-alternatives-experiments-and-adrs.md), [safe rollout](../delivery/safe-rollout-and-recovery.md), and [question-driven decision routes](question-routes-for-architecture-analysis.md).
