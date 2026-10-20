---
metadata_version: 1
id: "tycho.chapter.3d0f6dd1e8e94cd397326e129b5c287f"
kind: "chapter"
parent_id: "tycho.volume.01d303aaa7984edaac4127884592dd75"
canonical_path: "book/volumes/v05/c06/README.md"
title: "V05/C06 — Schema evolution, data migration and retention"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What compatibility windows and irreversibility constraints exist?"
route_hints:
  questions:
    - "What compatibility windows and irreversibility constraints exist?"
  prerequisites:
    - "tycho.chapter.3e2e1da8f99c4a7ba05121baf1ef4d91"
  related_ids:
    - "tycho.chapter.7d434d1a41e142d38bb729ee124ac548"
    - "tycho.chapter.0a5e430b39094337aa6a211d9b5b4bd0"
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

# V05/C06 — Schema evolution, data migration and retention

## Purpose and mission

What compatibility windows and irreversibility constraints exist? This chapter owns that question within data models, engines and lifecycle. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Treat data evolution as a semantic compatibility and authority transition, not just a successful DDL command.

A new value interpreted differently by old readers can break a mixed-version system even when every row passes schema validation. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Schema lifecycle, semantic data migration and data retirement](schema-lifecycle-and-semantic-migration.md) | What compatibility windows and irreversibility constraints exist? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Distinguish syntactic change from semantic change](schema-lifecycle-and-semantic-migration.md#1-distinguish-syntactic-change-from-semantic-change).
- [2. Original synthetic scenario: two equipment identities](schema-lifecycle-and-semantic-migration.md#2-original-synthetic-scenario-two-equipment-identities).
- [7. Public sources and nonclaims](schema-lifecycle-and-semantic-migration.md#7-public-sources-and-nonclaims).
- [Applied M9 evidence: what transfers and what does not](schema-lifecycle-and-semantic-migration.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

- [V08/C05 — Backward-compatible database change](../../v08/c05/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.
- [V10/C05 — Target architecture versus transition states](../../v10/c05/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V05 — Data models, engines and lifecycle](../README.md) |
| Previous | [V05/C05 — Partitioning, sharding and rebalancing](../c05/README.md) |
| Next | [V05/C07 — Replication, backups and restore drills](../c07/README.md) |
| Prerequisite | [V05/C05 — Partitioning, sharding and rebalancing](../c05/README.md) |
| Source reading | [Page-local evidence and versions](schema-lifecycle-and-semantic-migration.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
