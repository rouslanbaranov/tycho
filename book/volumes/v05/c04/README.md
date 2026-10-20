---
metadata_version: 1
id: "tycho.chapter.4a127ad6ab514ede9ff74394e5174f9c"
kind: "chapter"
parent_id: "tycho.volume.01d303aaa7984edaac4127884592dd75"
canonical_path: "book/volumes/v05/c04/README.md"
title: "V05/C04 — Alternative data models and stores"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "When are document, wide-column, KV, distributed SQL or analytical stores useful? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "When are document, wide-column, KV, distributed SQL or analytical stores useful?"
  prerequisites:
    - "tycho.chapter.e451bfe1e0cb4c588f0576e0b2b7d3d0"
  related_ids:
    - "tycho.page.c75a11f9786442a5b5456f11c2412df4"
    - "tycho.page.7b980e671a324f769064bc5233761c62"
    - "tycho.page.ee2dd008d4f445eaa9b20998f855a786"
    - "tycho.page.06363f8c9c8244aaa2bbc12abee16fa4"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.sqlite"
  claim_ids: []
  status: "source-linked"
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

# V05/C04 — Alternative data models and stores

## Purpose and mission

When are document, wide-column, KV, distributed SQL or analytical stores useful? This chapter owns that question within data models, engines and lifecycle. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Choose a storage model from access patterns, invariant scope and operating constraints, keeping migration costs visible.

Replacing an engine does not remove a hot logical key or a cross-owner transaction requirement. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](storage-model-alternatives-and-workload-fit.md) | When are document, wide-column, KV, distributed SQL or analytical stores useful? |
| [Relational, embedded and transactional key-value models](transactional-models.md) | Which transaction and locality requirements distinguish these storage choices? |
| [Document, wide-column and analytical access](specialized-models.md) | Which access pattern justifies specialized modeling and what is lost? |
| [Cross-model comparison and synchronization](multi-store-selection.md) | Which extra authority and recovery obligations appear when stores are combined? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V05 — Data models, engines and lifecycle](../README.md) |
| Previous | [V05/C03 — Query planning, indexes and access paths](../c03/README.md) |
| Next | [V05/C05 — Partitioning, sharding and rebalancing](../c05/README.md) |
| Prerequisite | [V05/C03 — Query planning, indexes and access paths](../c03/README.md) |
| Source reading | [Page-local evidence and versions](storage-model-alternatives-and-workload-fit.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.c75a11f9786442a5b5456f11c2412df4:9 -->
## Public evidence, version scope and limitations

| ID | Exact public source actually inspected | Supports, not a benchmark |
|---|---|---|
| E01 | [SQLite Architecture](https://www.sqlite.org/arch.html), *Overview; Bytecode Engine; B-Tree; Page Cache*, last-updated 2025-05-31 | Embedded compiled-to-VM SQL/B-tree/pager mechanisms |
| E02 | [CockroachDB v24.3 Architecture Overview](https://www.cockroachlabs.com/docs/v24.3/architecture/overview), *SQL, Transaction, Distribution, Replication and Storage Layers* | Architectural role decomposition, not measured universal SQL compatibility |
| E03 | [FoundationDB 8.0 Architecture](https://apple.github.io/foundationdb/architecture.html), *Detailed FoundationDB Architecture, Coordinator/Storage roles* | Distributed transactional ordered KV API and role separation |
| E04 | [MongoDB data modeling best practices](https://www.mongodb.com/docs/manual/data-modeling/best-practices/), *Link Related Data*, and [Embedding](https://www.mongodb.com/docs/manual/data-modeling/embedding/); current rolling docs observed 2026-10-19 | Embed/reference workload trade-offs; release-specific claims must be independently pinned |
| E05 | [Apache Cassandra 5.0 architecture overview](https://cassandra.apache.org/doc/stable/cassandra/architecture/overview.html), *Overview* | Partitioned wide-column/replication principles; not all consistency modes verified |
| E06 | [ClickHouse MergeTree engine](https://clickhouse.com/docs/reference/engines/table-engines/mergetree-family/mergetree), *Data parts, primary key and ordering*, rolling official docs observed 2026-10-19 | Sorted data parts/merges and pruning, no measured comparative throughput |
| E07 | [Neo4j property graph concepts](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/), *Introduction; Node; Relationship; Schema*, rolling official docs observed 2026-10-19 | Property graph model, not universal graph query speed advantage |

**Review state:** explanatory comparison, fictional workload diagrams only; no engine installed or benchmark run, no independent domain review, no comprehensive time-series vendor comparison and no measured migration. This page does **not** give a database product recommendation for a real user system.

<!-- /tycho-question-source -->
