---
metadata_version: 1
id: "tycho.chapter.b4272c1342514a40afce9d3872a9664c"
kind: "chapter"
parent_id: "tycho.volume.01d303aaa7984edaac4127884592dd75"
canonical_path: "book/volumes/v05/c02/README.md"
title: "V05/C02 — PostgreSQL MVCC, WAL and recovery"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What are the consequences of durability, vacuum and replication mechanisms?"
route_hints:
  questions:
    - "What are the consequences of durability, vacuum and replication mechanisms?"
  prerequisites:
    - "tycho.chapter.f5df10e26e27467887ee2b22b6ce50e7"
  related_ids:
    - "tycho.chapter.388c48be24414421a63481b37d05fdce"
    - "tycho.chapter.30e63461f024419ab87cd012b140c600"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# V05/C02 — PostgreSQL MVCC, WAL and recovery

## Purpose and mission

What are the consequences of durability, vacuum and replication mechanisms? This chapter owns that question within data models, engines and lifecycle. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Trace acknowledged writes through transaction state, WAL, replication and recovery before assigning a durability promise.

A reachable replica may lag, and a replication setting alone does not establish a successful restore or the application's recovery objective. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [PostgreSQL 17 WAL, physical/logical replication and recovery evidence](postgresql-wal-replication-and-recovery.md) | What are the consequences of durability, vacuum and replication mechanisms? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Why write-ahead logging exists](postgresql-wal-replication-and-recovery.md#1-why-write-ahead-logging-exists).
- [2. Physical streaming replication versus logical replication](postgresql-wal-replication-and-recovery.md#2-physical-streaming-replication-versus-logical-replication).
- [Engineering walkthrough — Primary acknowledgment is not standby completeness](postgresql-wal-replication-and-recovery.md#engineering-walkthrough-primary-acknowledgment-is-not-standby-completeness).
- [Exact public evidence ledger](postgresql-wal-replication-and-recovery.md#exact-public-evidence-ledger).

## Boundaries and further reading

- [V05/C07 — Replication, backups and restore drills](../c07/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.
- [V08/C07 — Multi-region recovery and data reconciliation](../../v08/c07/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V05 — Data models, engines and lifecycle](../README.md) |
| Previous | [V05/C01 — Relational modeling and transaction isolation](../c01/README.md) |
| Next | [V05/C03 — Query planning, indexes and access paths](../c03/README.md) |
| Prerequisite | [V05/C01 — Relational modeling and transaction isolation](../c01/README.md) |
| Source reading | [Page-local evidence and versions](postgresql-wal-replication-and-recovery.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
