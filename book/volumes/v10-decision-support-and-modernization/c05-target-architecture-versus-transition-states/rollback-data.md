---
metadata_version: 1
id: "tycho.page.47b67ebf3dbf477e818e83f9e1683ffe"
kind: "page"
parent_id: "tycho.chapter.0a5e430b39094337aa6a211d9b5b4bd0"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c05-target-architecture-versus-transition-states/rollback-data.md"
title: "Rollback limits and semantic reconciliation"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Which durable differences survive reverting the deployed binary?"
route_hints:
  questions:
    - "Which durable differences survive reverting the deployed binary?"
  prerequisites:
    - "tycho.page.78d0f89ac4184b19bfef3a72e8b4f2cc"
  related_ids:
    - "tycho.chapter.0a5e430b39094337aa6a211d9b5b4bd0"
    - "tycho.page.cf0ce38c73e44950aec5a9c2869bee63"
    - "tycho.page.ea1c3ca31f974bcbb6a432c55e56bc03"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "rollback"
    - "data"
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
# Rollback limits and semantic reconciliation

**Owning question:** Which durable differences survive reverting the deployed binary?

This page belongs to [V10/C05 — Target architecture versus transition states](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.cf0ce38c73e44950aec5a9c2869bee63:4 -->
## 4. When rollback means less than users think

A code rollback is reversible only if:
1. Older binaries still correctly interpret persisted state produced by newer binaries.
2. External clients and asynchronous consumers still accept the older response/event contract.
3. Effects committed during the new release can be reconciled or safely replayed.
4. The old route is still operational and authorized.
5. The rollback itself doesn't reintroduce a known security or correctness defect.

If a new version has written a field with novel meaning, the older version may parse it but make wrong decisions. If the system has sent an irreversible notification or performed an external effect, re-deploying an older container does not retract it. If a database migration removed an old column, old SQL may fail entirely.

Distinguish **reversible before write exposure**, **conditionally reversible during coexistence**, and **forward repair or restore required after irreversible effects**. A restore may lose acknowledged operations if the recovery point predates their commits; state explicitly which business loss is permissible. See [backup/PITR and restore drills](../../v05-data-models-engines-and-lifecycle/c07-replication-backups-and-restore-drills/backup-restore-pitr-and-recovery-drills.md).

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.cf0ce38c73e44950aec5a9c2869bee63:5 -->
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

<!-- /tycho-question-source -->

## Reconciliation, repair and evidence for a migration cutover

**Enrichment contract:** decide whether the target contains the intended effects and relationships, rather than whether a copy job finished. This section owns transition acceptance; engine-specific replication belongs to its canonical owner.

### Original count-equality counterexample

A fictional source snapshot has records A, B and C. A target with A, B and B also has three rows; equal counts conceal missing C and duplicate B. Equal aggregate sums can conceal compensating errors. Define canonical identities and invariants before choosing a comparison.

A proposed comparison plan partitions by a stable key range, fixes the source/target observation boundary and checks membership, per-key normalized values, relationship constraints and selected business outcomes. A digest can efficiently flag differences only if canonical encoding, schema interpretation and comparison windows agree. It is a detector, not proof that a faulty canonicalizer preserved meaning.

| Comparison | Detects | Important blind spot |
|---|---|---|
| Row/event count | Some missing/excess records | Equal loss and duplication |
| Key-set comparison | Missing/excess identity | Wrong values under an existing identity |
| Canonical per-key digest | Value differences under one encoding | Shared conversion bug or omitted fields |
| Cross-record invariant | Broken relationships and forbidden states | Unspecified business rules |
| Representative user journey | Some externally visible defects | Unexercised populations and rare states |

### Match the observation boundary

Comparing a live source at revision 120 with a lagging target at 110 produces expected differences. Do not repair those by overwriting newer target data from an older snapshot. Record watermark/snapshot identity and ownership of each writable field. If a source snapshot and its subsequent change stream cannot be joined without a gap, the cutover lacks a completeness argument.

For original synthetic convergence, assume incoming changes produce 200 work units/s and repair applies 300 units/s. A 60,000-unit backlog takes at least 600 seconds at a net 100 units/s under steady rates. If application changes consume the same constrained capacity or create more repair work, that estimate is invalid. Arithmetic is illustrative, not a measured throughput.

### Repair is an authorized mutation

Classify discrepancies before changing state: missing target record, stale projection, transformed value, duplicate external effect, deleted source entity or unresolved ownership. Prefer idempotent repair keyed by the original logical effect and guarded by current version/epoch. Recheck authorization and retirement records. Do not let a generic replayer reissue irreversible effects merely because target state is incomplete.

~~~mermaid
flowchart TD
    O["Pinned comparison boundary"] --> D["Classified discrepancy"]
    D --> A{"Authoritative owner and repair known?"}
    A -->|No| H["Hold cutover and investigate"]
    A -->|Yes| R["Apply guarded idempotent repair"]
    R --> V["Recompare values and invariants"]
    V --> G{"Acceptance envelope satisfied?"}
    G -->|No| H
    G -->|Yes| C["Authorized cutover with recorded residual limits"]
~~~

Text alternative: a discrepancy becomes a scoped repair only after identifying authority. Recomparison precedes cutover. This original reasoning flow is not an executed migration.

### Acceptance, recovery and sources

Record unresolved differences, affected populations, repair backlog/age, dual-write divergence, rollback compatibility and the point where old state is no longer sufficient for reversal. A binary rollback cannot restore discarded meanings, later retired data or already emitted external effects.

Use [Kafka recovery boundaries](../../v04-distributed-coordination-and-events/c07-kafka-logs-partitions-and-transactions/offsets-effects.md#rebalance-external-effects-and-expired-replay-positions), [PostgreSQL replica state](../../v05-data-models-engines-and-lifecycle/c02-postgresql-mvcc-wal-and-recovery/replica-recovery.md#replica-lag-retained-wal-and-standby-feedback) and [deletion after restore](../../v05-data-models-engines-and-lifecycle/c06-schema-evolution-data-migration-and-retention/migration-retirement.md#deletion-across-derived-state-and-restored-backups) for exact mechanisms. Selected [Kafka external-output coordination](https://kafka.apache.org/41/design/design/) supports the need to coordinate position and output; the comparison/repair plan and numbers are original synthesis.

Proposed acceptance: inject one loss and one duplicate with unchanged count, update while comparing, fail a repair halfway, and restore before a retirement. Require complete classified outcomes under a named boundary. No migration or repair execution was performed.

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](authority-states.md) |
| Next | [Continue the reasoning](cutover-gates.md) |
| Integrated question | [Original scenario and limits](target-and-transition-architecture-states.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
