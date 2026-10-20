---
metadata_version: 1
id: "tycho.chapter.e451bfe1e0cb4c588f0576e0b2b7d3d0"
kind: "chapter"
parent_id: "tycho.volume.01d303aaa7984edaac4127884592dd75"
canonical_path: "book/volumes/v05/c03/README.md"
title: "V05/C03 — Query planning, indexes and access paths"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which read/write trade-offs explain an observed query plan? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Which read/write trade-offs explain an observed query plan?"
  prerequisites:
    - "tycho.chapter.b4272c1342514a40afce9d3872a9664c"
  related_ids:
    - "tycho.page.7a136445bbfe4a8194c2c4db8a8818ee"
    - "tycho.page.d66b60c435cc4f8480c15cc6e400b369"
    - "tycho.page.9b9c3ab86633469185416e4e88c0caca"
    - "tycho.page.045713bc4f054663b676e4e1b6fe9725"
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

# V05/C03 — Query planning, indexes and access paths

## Purpose and mission

Which read/write trade-offs explain an observed query plan? This chapter owns that question within data models, engines and lifecycle. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Interpret a query plan against row estimates, selectivity, write cost and workload rather than assuming an index is always beneficial.

A faster isolated read can increase update cost or fail under skew; compare plans and resource use on the relevant distribution. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](postgresql-indexes-statistics-and-query-plans.md) | Which read/write trade-offs explain an observed query plan? |
| [Access methods, selectivity and estimates](access-selectivity.md) | Which distribution and operators make an index or access path appropriate? |
| [Plan evidence and index lifecycle](plan-lifecycle.md) | What does EXPLAIN omit and what operational work does an index change create? |
| [Negative query cases and controlled validation](query-counterexamples.md) | Which workload change can reverse an apparently successful index decision? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V05 — Data models, engines and lifecycle](../README.md) |
| Previous | [V05/C02 — PostgreSQL MVCC, WAL and recovery](../c02/README.md) |
| Next | [V05/C04 — Alternative data models and stores](../c04/README.md) |
| Prerequisite | [V05/C02 — PostgreSQL MVCC, WAL and recovery](../c02/README.md) |
| Source reading | [Page-local evidence and versions](postgresql-indexes-statistics-and-query-plans.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.7a136445bbfe4a8194c2c4db8a8818ee:8 -->
## 8. Public evidence ledger and limits

| Independently read PostgreSQL 17 source | Narrow claim supported | Unproven |
|---|---|---|
| [Chapter 11, Indexes](https://www.postgresql.org/docs/17/indexes.html) | Index/operator families, read-versus-write trade-offs | One index's measured benefit for the fictional workload |
| [§14.1, Using EXPLAIN](https://www.postgresql.org/docs/17/using-explain.html) | Plan nodes, cost units, actual rows/timing and instrumented query | Actual trace or tested query plan |
| [§14.2, Planner Statistics](https://www.postgresql.org/docs/17/planner-stats.html) | Per-column and extended selectivity statistics, ANALYZE | Evidence about this invented data distribution |
| [CREATE INDEX](https://www.postgresql.org/docs/17/sql-createindex.html) | Index creation/concurrency options and limitations | Safe migration or measured write impact |

Every query scenario, diagram and table was independently authored for education. No PostgreSQL engine, SQL statements, index DDL or independent technical acceptance were executed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7a136445bbfe4a8194c2c4db8a8818ee:10 -->
## Navigation

Proposed **V05/C03** in [draft outline](../../../PROPOSED-STRUCTURE.md), [data landing](../../../data/README.md). Prerequisite [relational modeling and isolation](../c01/relational-modeling-and-transaction-isolation.md). Related [PostgreSQL WAL/recovery](../c02/postgresql-wal-replication-and-recovery.md), [query distribution/performance](../../v01/c02/workload-demand-and-arrival-models.md), [lexical full-text ranking](../../v06/c03/lexical-indexing-bm25-and-sql-fts.md).
<!-- /tycho-question-source -->
