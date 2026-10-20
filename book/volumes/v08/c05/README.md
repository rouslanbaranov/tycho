---
metadata_version: 1
id: "tycho.chapter.7d434d1a41e142d38bb729ee124ac548"
kind: "chapter"
parent_id: "tycho.volume.cb10070ba233477fae8aa5d18e74fee8"
canonical_path: "book/volumes/v08/c05/README.md"
title: "V08/C05 — Backward-compatible database change"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What permits old and new binaries/data schemas to coexist?"
route_hints:
  questions:
    - "What permits old and new binaries/data schemas to coexist?"
  prerequisites:
    - "tycho.chapter.5e4761e1a3e34c2f8023ec8ac4fa81d5"
  related_ids:
    - "tycho.chapter.3d0f6dd1e8e94cd397326e129b5c287f"
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

# V08/C05 — Backward-compatible database change

## Purpose and mission

What permits old and new binaries/data schemas to coexist? This chapter owns that question within delivery, deployment and disaster recovery. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Describe reader/writer compatibility across expansion, coexistence, backfill and contraction stages.

Reverting binaries cannot restore a removed column or reinterpret a new-only persisted value; the no-return point needs forward repair. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Backward-compatible database change: mixed-version reads, writes and online DDL](mixed-version-database-compatibility-and-online-ddl.md) | What permits old and new binaries/data schemas to coexist? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Check the real combinations, including old readers](mixed-version-database-compatibility-and-online-ddl.md#1-check-the-real-combinations-including-old-readers).
- [2. Expand-migrate-contract includes a compatibility window](mixed-version-database-compatibility-and-online-ddl.md#2-expand-migrate-contract-includes-a-compatibility-window).
- [7. Source ledger and remaining verification](mixed-version-database-compatibility-and-online-ddl.md#7-source-ledger-and-remaining-verification).
- [Applied M9 evidence: what transfers and what does not](mixed-version-database-compatibility-and-online-ddl.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

- [V05/C06 — Schema evolution, data migration and retention](../../v05/c06/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.
- [V10/C05 — Target architecture versus transition states](../../v10/c05/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V08 — Delivery, deployment and disaster recovery](../README.md) |
| Previous | [V08/C04 — GitOps, rollout and progressive delivery](../c04/README.md) |
| Next | [V08/C06 — High availability and failure-domain placement](../c06/README.md) |
| Prerequisite | [V08/C04 — GitOps, rollout and progressive delivery](../c04/README.md) |
| Source reading | [Page-local evidence and versions](mixed-version-database-compatibility-and-online-ddl.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
