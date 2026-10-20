---
metadata_version: 1
id: "tycho.page.47b67ebf3dbf477e818e83f9e1683ffe"
kind: "page"
parent_id: "tycho.chapter.0a5e430b39094337aa6a211d9b5b4bd0"
canonical_path: "book/volumes/v10/c05/rollback-data.md"
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

Distinguish **reversible before write exposure**, **conditionally reversible during coexistence**, and **forward repair or restore required after irreversible effects**. A restore may lose acknowledged operations if the recovery point predates their commits; state explicitly which business loss is permissible. See [backup/PITR and restore drills](../../v05/c07/backup-restore-pitr-and-recovery-drills.md).

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

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](authority-states.md) |
| Next | [Continue the reasoning](cutover-gates.md) |
| Integrated question | [Original scenario and limits](target-and-transition-architecture-states.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
