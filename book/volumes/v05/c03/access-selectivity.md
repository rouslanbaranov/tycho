---
metadata_version: 1
id: "tycho.page.d66b60c435cc4f8480c15cc6e400b369"
kind: "page"
parent_id: "tycho.chapter.e451bfe1e0cb4c588f0576e0b2b7d3d0"
canonical_path: "book/volumes/v05/c03/access-selectivity.md"
title: "Access methods, selectivity and estimates"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
summary: "Which distribution and operators make an index or access path appropriate?"
route_hints:
  questions:
    - "Which distribution and operators make an index or access path appropriate?"
  prerequisites:
    - "tycho.page.7a136445bbfe4a8194c2c4db8a8818ee"
  related_ids:
    - "tycho.chapter.e451bfe1e0cb4c588f0576e0b2b7d3d0"
    - "tycho.page.7a136445bbfe4a8194c2c4db8a8818ee"
    - "tycho.page.9b9c3ab86633469185416e4e88c0caca"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "access"
    - "selectivity"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.7a136445bbfe4a8194c2c4db8a8818ee; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Access methods, selectivity and estimates

**Owning question:** Which distribution and operators make an index or access path appropriate?

This page belongs to [V05/C03 — Query planning, indexes and access paths](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.7a136445bbfe4a8194c2c4db8a8818ee:1 -->
## 1. Model the query and distribution first

Original fictional case: a community tool catalogue stores tools, bookings and descriptive tags. Representative requests:
- find one tool by stable identifier;
- list currently available devices for one site and date;
- search by term or tag;
- list most recently updated public descriptions;
- display all reservations for one member during a bounded period.

These workloads do not necessarily benefit from the **same index**. A primary-key lookup, range filter, full-text query and ordered pagination impose different access patterns and selectivity.

An index design question should include:
- columns/operator predicates and sort order;
- total table size, estimated rows after each filter and data skew;
- actual query frequency and latency objectives;
- write/update/delete rate, storage budget and vacuum/maintenance behavior;
- joined table cardinalities and relationships;
- whether partial, expression or covering indexes fit the data contract;
- index-build and version/deployment constraints.

“An index exists” is not sufficient: the planner may correctly choose a sequential scan when a large fraction of rows qualifies, or when the index path is more expensive under its assumptions.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7a136445bbfe4a8194c2c4db8a8818ee:2 -->
## 2. Compare access methods by the supported operator/workload

| PostgreSQL index family | Typical supported purpose | Limitation to verify |
|---|---|---|
| B-tree | Equality, ordered comparison/range and matching ordered scan | Column order and selectivity affect multicolumn usefulness |
| Hash | Hashable equality | Narrower operator coverage; not universal substitute for B-tree |
| GiST | Extensible general search tree for configured operator classes | Behavior depends on datatype/operator implementation |
| SP-GiST | Space-partitioned search trees for supported operator classes | Not appropriate for arbitrary text/range operations |
| GIN | Inverted lookup for composite values such as lexemes, arrays or compatible JSONB operators | Update and posting-list maintenance, result semantics |
| BRIN | Compact block-range summaries for data whose physical locality correlates with values | May need rechecks and can be ineffective with random scatter |

The exact operator support is **not a property of the index name alone**. Consult PostgreSQL's [index types](https://www.postgresql.org/docs/17/indexes-types.html) and [built-in index methods](https://www.postgresql.org/docs/17/indextypes.html) for current version details. A GIN text search index is not a general-purpose semantic vector index.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7a136445bbfe4a8194c2c4db8a8818ee:3 -->
## 3. Planner estimates are hypotheses about table contents

The [PostgreSQL 17 planner statistics, §14.2](https://www.postgresql.org/docs/17/planner-stats.html) explains row-count and distribution estimates and how PostgreSQL uses single-column and extended multivariate statistics. Correlated predicates can fool naive independence assumptions, producing badly estimated joins or scan plans.

**Synthetic illustration:** one location has 90% of devices tagged as “portable”, while other locations rarely use the tag. A planner relying on approximate independent selectivities may underestimate rows for a combined location-and-tag predicate. A suitable extended-statistics object (when supported for the chosen predicate) and ANALYZE may improve estimates; the design still requires an actual EXPLAIN and controlled workload test.

Planner estimates are *not* guaranteed measured data, and creating extended statistics does not itself gather representative samples until ANALYZE runs. Samples, data growth, skew and schema changes can invalidate prior assumptions.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](postgresql-indexes-statistics-and-query-plans.md) |
| Next | [Continue the reasoning](plan-lifecycle.md) |
| Integrated question | [Original scenario and limits](postgresql-indexes-statistics-and-query-plans.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
