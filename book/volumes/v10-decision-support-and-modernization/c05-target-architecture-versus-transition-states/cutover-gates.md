---
metadata_version: 1
id: "tycho.page.ea1c3ca31f974bcbb6a432c55e56bc03"
kind: "page"
parent_id: "tycho.chapter.0a5e430b39094337aa6a211d9b5b4bd0"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c05-target-architecture-versus-transition-states/cutover-gates.md"
title: "Migration mechanisms and no-return gates"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "What evidence permits a transition to cross an irreversible boundary?"
route_hints:
  questions:
    - "What evidence permits a transition to cross an irreversible boundary?"
  prerequisites:
    - "tycho.page.47b67ebf3dbf477e818e83f9e1683ffe"
  related_ids:
    - "tycho.chapter.0a5e430b39094337aa6a211d9b5b4bd0"
    - "tycho.page.cf0ce38c73e44950aec5a9c2869bee63"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "cutover"
    - "gates"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.cf0ce38c73e44950aec5a9c2869bee63; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Migration mechanisms and no-return gates

**Owning question:** What evidence permits a transition to cross an irreversible boundary?

This page belongs to [V10/C05 — Target architecture versus transition states](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.cf0ce38c73e44950aec5a9c2869bee63:6 -->
## 6. Alternative migration mechanisms and contraindications

| Mechanism | Fits when | Can fail when |
|---|---|---|
| Internal branch by abstraction | An internal interface can route old/new implementations with one deployable | Components cannot be separated without untested side effects |
| Strangler façade | Requests can be intercepted and routed by capability | Internal callers bypass façade or it becomes a bottleneck |
| Expand/migrate/contract | Supported readers/writers can coexist during additive schema phases | Old client semantics changed despite schema compatibility |
| Shadow reads | Side-effect-free comparisons are possible without user exposure | Shadow requests accidentally mutate authoritative state |
| Event/CDC projection | Derived reads tolerate bounded lag and replay discipline exists | Losing deletes/revocations causes unsafe stale data |
| Big-bang replacement | Tiny well-understood system, feasible downtime, fully proven restoration | Many unknown behaviors, long-tail clients or irreversible writes |

These are conditions, not prescriptive steps. The [Microsoft Strangler Fig pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) explicitly treats the façade as a temporary infrastructure cost and warns that request interception may be impossible. Use [anti-corruption adapters](../../v02-application-boundaries-and-contracts/c06-integration-adapters-and-anti-corruption-boundaries/anti-corruption-adapters-and-coexistence.md) when foreign meanings must be translated.

**Branch-by-abstraction invariant.** Old and new implementations behind the internal
interface must preserve the same contract and observable effects; the switch must remain
reversible until the old path is removed. Untested side effects, a bypass around the
abstraction and divergent implementations can break that contract. Detect with contract
tests and a bounded switch, then hold or roll back to the compatible path.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Branch by Abstraction](../../v11-pattern-atlas/c10-deployment-modernization/README.md#branch-by-abstraction) — decision conditions and contraindications.
> [Controlled Cutover](../../v11-pattern-atlas/c10-deployment-modernization/README.md#controlled-cutover) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.cf0ce38c73e44950aec5a9c2869bee63:7 -->
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

**Alternative.** Rolling or blue/green deployment, a canary with a reversible
gate, or scheduled maintenance may be preferable when the no-return evidence cannot be
obtained or the change is small enough to reverse. Reverse the controlled-cutover choice
when its evidence and hold costs exceed the no-return risk.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](rollback-data.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](target-and-transition-architecture-states.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

## Bounded pattern ownership notes

### Branch by Abstraction

Branch by abstraction inserts an internal interface between callers and the old/new
implementations, so both can run in one deployable while traffic moves gradually. The switch is a
runtime or configuration decision, not a long-lived source branch.

An internal interface can route old/new implementations with one deployable. Old and new
implementations behind the internal interface must preserve the same contract and observable
effects; the switch must remain reversible until the old path is removed. Give the seam a removal
date and owner; a permanent seam is a maintenance failure, and the switch must remain reversible
until removal. Untested side effects, a bypass around the abstraction and divergent implementations
can break that contract.

A strangler facade can route requests by capability when the boundary is external. Branch by
abstraction is a fit when the switch can stay inside one deployable and the interface is genuinely
owned; otherwise a facade or a parallel run is simpler. Reverse when abstraction cost exceeds
incremental change benefit, and remove the seam once the old path is gone.

### Controlled Cutover

A controlled cutover drains the write pipeline and verifies that source changes replicate before
switching writes. Verify pipeline health and DLQ state before cutover. Resolve DLQ errors before pausing writes. Verify the forward replication pipeline has no permanent errors and wait
for the data freshness metric to reach zero before switching. A contingency fallback pathway can be configured before cutover using reverse replication. The procedure assumes the target schema is deployed and the
backfill job is complete. Verify active CDC replication before pausing writes. Pause Datastream and
confirm that no replication events pass through the stream, then update connection strings and start
application services against the target. Monitor reverse replication errors after cutover. The
fallback path requires an active reverse pipeline before cutover starts. Strangler Fig replacement
moves authority incrementally through seams.
