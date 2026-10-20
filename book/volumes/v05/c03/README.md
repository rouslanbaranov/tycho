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
summary: "Which read/write trade-offs explain an observed query plan?"
route_hints:
  questions:
    - "Which read/write trade-offs explain an observed query plan?"
  prerequisites:
    - "tycho.chapter.b4272c1342514a40afce9d3872a9664c"
  related_ids: []
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

| Page | Owning question |
|---|---|
| [PostgreSQL indexing, planner statistics and query access paths](postgresql-indexes-statistics-and-query-plans.md) | Which read/write trade-offs explain an observed query plan? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Model the query and distribution first](postgresql-indexes-statistics-and-query-plans.md#1-model-the-query-and-distribution-first).
- [2. Compare access methods by the supported operator/workload](postgresql-indexes-statistics-and-query-plans.md#2-compare-access-methods-by-the-supported-operatorworkload).
- [8. Public evidence ledger and limits](postgresql-indexes-statistics-and-query-plans.md#8-public-evidence-ledger-and-limits).
- [Engineering walkthrough — Same index, different workload distribution](postgresql-indexes-statistics-and-query-plans.md#engineering-walkthrough-same-index-different-workload-distribution).

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
