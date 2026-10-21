---
metadata_version: 1
id: "tycho.chapter.7d434d1a41e142d38bb729ee124ac548"
kind: "chapter"
parent_id: "tycho.volume.cb10070ba233477fae8aa5d18e74fee8"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c05-backward-compatible-database-change/README.md"
title: "V08/C05 — Backward-compatible database change"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What permits old and new binaries/data schemas to coexist? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "What permits old and new binaries/data schemas to coexist?"
  prerequisites:
    - "tycho.chapter.5e4761e1a3e34c2f8023ec8ac4fa81d5"
  related_ids:
    - "tycho.chapter.3d0f6dd1e8e94cd397326e129b5c287f"
    - "tycho.chapter.0a5e430b39094337aa6a211d9b5b4bd0"
    - "tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb"
    - "tycho.page.96a702434b714ed4906b1301bc6e0248"
    - "tycho.page.48d9c34e755c4f7ab912ecad14f5794f"
    - "tycho.page.d1fa0462922e4a37922cea279975a3bd"
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
updated_at: "2026-10-21"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](mixed-version-database-compatibility-and-online-ddl.md) | What permits old and new binaries/data schemas to coexist? |
| [Reader/writer compatibility and migration stages](reader-writer-matrix.md) | Which combinations must work during expansion, coexistence and contraction? |
| [DDL budgets and event compatibility](ddl-events.md) | Which resource and consumer contracts can fail despite a compatible table shape? |
| [No-return points and forward repair](no-return-recovery.md) | Which persisted effect makes reverting an old binary unsafe? |

## Boundaries and further reading

- [V05/C06 — Schema evolution, data migration and retention](../../v05-data-models-engines-and-lifecycle/c06-schema-evolution-data-migration-and-retention/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.
- [V10/C05 — Target architecture versus transition states](../../v10-decision-support-and-modernization/c05-target-architecture-versus-transition-states/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V08 — Delivery, deployment and disaster recovery](../README.md) |
| Previous | [V08/C04 — GitOps, rollout and progressive delivery](../c04-gitops-rollout-and-progressive-delivery/README.md) |
| Next | [V08/C06 — High availability and failure-domain placement](../c06-high-availability-and-failure-domain-placement/README.md) |
| Prerequisite | [V08/C04 — GitOps, rollout and progressive delivery](../c04-gitops-rollout-and-progressive-delivery/README.md) |
| Source reading | [Page-local evidence and versions](mixed-version-database-compatibility-and-online-ddl.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.77957bf0f2d44c4a9bc819fc5b3e1ddb:7 -->
## 7. Source ledger and remaining verification

| Public evidence | Supported point | Not proven |
|---|---|---|
| [PostgreSQL 17 ALTER TABLE](https://www.postgresql.org/docs/17/sql-altertable.html) | Versioned DDL/lock/subcommand semantics | Actual online migration time |
| [Confluent Schema Registry evolution](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html) | Format- and version-specific backward/forward/full compatibility | Business meaning or real consumer compatibility |
| [Danilo Sato Parallel Change](https://martinfowler.com/bliki/ParallelChange.html) | Expansion, migration and contraction as transition method | DB/backfill safety |
| [Prior combined Tycho research](../../../delivery/progressive-delivery-and-schema-evolution.md) | Earlier rollout/schema study and failure matrix | Independently accepted chapter split |

Every system, schema, migration diagram and experiment is original synthetic work. No SQL,
client/consumer, restore or load test was run; chapter metadata is recorded in the current edition.

**Navigation:** canonical chapter in the current edition. Start at the
[volume landing](../README.md).
<!-- /tycho-question-source -->
