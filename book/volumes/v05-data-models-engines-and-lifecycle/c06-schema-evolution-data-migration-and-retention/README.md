---
metadata_version: 1
id: "tycho.chapter.3d0f6dd1e8e94cd397326e129b5c287f"
kind: "chapter"
parent_id: "tycho.volume.01d303aaa7984edaac4127884592dd75"
canonical_path: "book/volumes/v05-data-models-engines-and-lifecycle/c06-schema-evolution-data-migration-and-retention/README.md"
title: "V05/C06 — Schema evolution, data migration and retention"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What compatibility windows and irreversibility constraints exist? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "What compatibility windows and irreversibility constraints exist?"
  prerequisites:
    - "tycho.chapter.3e2e1da8f99c4a7ba05121baf1ef4d91"
  related_ids:
    - "tycho.chapter.7d434d1a41e142d38bb729ee124ac548"
    - "tycho.chapter.0a5e430b39094337aa6a211d9b5b4bd0"
    - "tycho.page.357c2d162bd44f3aa06a995a1e691551"
    - "tycho.page.d00c6081ca664f619308712e245ef523"
    - "tycho.page.7e927696162f48beaa33fc834b36ee76"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](schema-lifecycle-and-semantic-migration.md) | What compatibility windows and irreversibility constraints exist? |
| [Schema shape and preserved meaning](semantic-compatibility.md) | Which old/new representation change can silently alter a domain invariant? |
| [Migration stages, retention and no-return points](migration-retirement.md) | Which authority and validation gates permit old data or contracts to be retired? |

## Boundaries and further reading

- [V08/C05 — Backward-compatible database change](../../v08-delivery-deployment-and-recovery/c05-backward-compatible-database-change/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.
- [V10/C05 — Target architecture versus transition states](../../v10-decision-support-and-modernization/c05-target-architecture-versus-transition-states/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V05 — Data models, engines and lifecycle](../README.md) |
| Previous | [V05/C05 — Partitioning, sharding and rebalancing](../c05-partitioning-sharding-and-rebalancing/README.md) |
| Next | [V05/C07 — Replication, backups and restore drills](../c07-replication-backups-and-restore-drills/README.md) |
| Prerequisite | [V05/C05 — Partitioning, sharding and rebalancing](../c05-partitioning-sharding-and-rebalancing/README.md) |
| Source reading | [Page-local evidence and versions](schema-lifecycle-and-semantic-migration.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.


## Further mechanism and recovery questions

- [Deletion across derived state and restored backups](migration-retirement.md#deletion-across-derived-state-and-restored-backups) — source-scoped enrichment; examples and proposed tests are not executed results.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.357c2d162bd44f3aa06a995a1e691551:7 -->
## 7. Public sources and nonclaims

| Independently read source | Supported point | Unproven |
|---|---|---|
| [Danilo Sato — Parallel Change](https://martinfowler.com/bliki/ParallelChange.html) | Expand/migrate/contract interface coexistence method | Automatic database consistency |
| [PostgreSQL 17 ALTER TABLE](https://www.postgresql.org/docs/17/sql-altertable.html) | Operation-specific DDL and lock constraints | Running migration result |
| [Prior Tycho combined schema study](../../../delivery/progressive-delivery-and-schema-evolution.md) | Original research on mixed versions and data transition | Accepted semantic migration |

The invented schema, example workflow, diagram, test matrix and conclusions are original. No versioned database data or human review was available.

**Navigation:** proposed **V05/C06** in [book outline](../../../PROPOSED-STRUCTURE.md) and [data landing](../../../data/README.md). Read [relational modeling](../c01-relational-modeling-and-transaction-isolation/relational-modeling-and-transaction-isolation.md), [mixed-version schema compatibility](../../v08-delivery-deployment-and-recovery/c05-backward-compatible-database-change/mixed-version-database-compatibility-and-online-ddl.md), [legacy transition](../../v10-decision-support-and-modernization/c05-target-architecture-versus-transition-states/target-and-transition-architecture-states.md).

<!-- /tycho-question-source -->
