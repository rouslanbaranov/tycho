---
metadata_version: 1
id: "tycho.page.7a136445bbfe4a8194c2c4db8a8818ee"
kind: "page"
parent_id: "tycho.chapter.e451bfe1e0cb4c588f0576e0b2b7d3d0"
canonical_path: "book/volumes/v05-data-models-engines-and-lifecycle/c03-query-planning-indexes-and-access-paths/postgresql-indexes-statistics-and-query-plans.md"
title: "PostgreSQL indexing, planner statistics and query access paths"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Query planning, indexes and access paths. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which read/write trade-offs explain an observed query plan?"
  prerequisites: []
  related_ids:
    - "tycho.page.9176c39f97f544f884666e291ae38b90"
    - "tycho.page.6b42723bd575413bb0d1b94d3e179b6a"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.984c44f8dbd44d8e89105b4d31787636"
    - "tycho.page.ddeff7f1556f44f18c67659b73e6e15f"
    - "tycho.page.fdb4ef7f69154f8c8c433591f71494f9"
    - "tycho.page.39a694d604d646a996bf90c3357c3b27"
    - "tycho.page.d66b60c435cc4f8480c15cc6e400b369"
    - "tycho.page.9b9c3ab86633469185416e4e88c0caca"
    - "tycho.page.045713bc4f054663b676e4e1b6fe9725"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "PostgreSQL"
    - "indexing"
    - "planner"
    - "statistics"
    - "and"
    - "query"
    - "access"
    - "paths"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.7a136445bbfe4a8194c2c4db8a8818ee:-1 -->

# PostgreSQL indexing, planner statistics and query access paths

> **Tycho independent manuscript — proposed V05/C03**, prepared 2026-10-19, using version-scoped PostgreSQL 17 official documentation. The query shapes and workload are entirely synthetic. No DB engine, EXPLAIN ANALYZE, DDL, benchmark or reviewer approval was executed. Earlier [combined MVCC/index research](../../../data/postgresql-mvcc-indexes-and-query-plans.md) remains preserved for claim-by-claim reconciliation.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7a136445bbfe4a8194c2c4db8a8818ee:0 -->
## Purpose and mission

Index choice is not a contest to add as many lookup structures as possible. A database planner chooses a route through data based on the SQL predicate, available physical access paths, estimated row counts and system cost assumptions. An index can make selective reads faster but adds storage, maintenance and write overhead.

The right question is **which representative query shapes and actual row distributions justify a particular access path, with acceptable write and operating cost?**

[PostgreSQL 17 Indexes, Chapter 11](https://www.postgresql.org/docs/17/indexes.html) documents B-tree, hash, GiST, SP-GiST, GIN and BRIN as supported access-method families. [PostgreSQL 17 EXPLAIN, §14.1](https://www.postgresql.org/docs/17/using-explain.html) distinguishes estimated planner *cost units* from actual time measured when executing EXPLAIN ANALYZE. This chapter owns access paths and planner evidence; [relational invariants and isolation](../c01-relational-modeling-and-transaction-isolation/relational-modeling-and-transaction-isolation.md) owns correctness and transactional state authority.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7a136445bbfe4a8194c2c4db8a8818ee:9 -->
## Engineering walkthrough — Same index, different workload distribution

**Original synthetic query:** `SELECT ... WHERE tenant_id=? AND state='OPEN' ORDER BY created_at DESC LIMIT 20`. A compound index appears useful under a uniform tenant distribution. Later one tenant holds 60% of rows and most records are closed. PostgreSQL's planner may estimate different selectivities from stored statistics; the mere presence of an index does not guarantee it is chosen or useful under that skew.

| Observation | Can support | Cannot prove alone |
|---|---|---|
| `EXPLAIN` estimated rows/cost | Planner's modeled access-path preference | Measured end-to-end latency |
| `EXPLAIN ANALYZE` actual rows/time | Execution behavior for that statement and environment | The entire user population p99 or all tenant distributions |
| Stale histogram or correlation stats | A plausible cause of incorrect row estimates | That adding arbitrary indexes is safest |
| Pool wait/lock time | Architecture latency outside scan plan | Query optimization alone will restore availability |

**Two controlled cases:** A has 100,000 balanced rows; B has the same row count but a hot tenant and correlated `state` values. Use pinned query parameters, data shape, planner settings, statistics collection, available memory and cold/warm cache state. Compare index-only eligibility, actual buffer reads, estimated vs actual row counts and user-visible latency. A plan change may improve B and worsen A; that is a **decision condition**, not a universal index rule.

A read-model/materialized projection may be justified for analytically different queries, but introduces freshness and rebuild cost. A simple index/statistics repair is preferable if measured against the actual distribution. The PostgreSQL 17 planning/EXPLAIN references define versioned behavior; **no SQL workload was executed**, and the two data distributions are invented.


**Verification status:** The preceding original example and its predicted outcomes are synthetic. No implementation experiment, benchmark or independent technical review was executed for this example.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Interpret a query plan against row estimates, selectivity, write cost and workload rather than assuming an index is always beneficial.

A faster isolated read can increase update cost or fail under skew; compare plans and resource use on the relevant distribution.

The detailed pages separate the mechanisms that make this decision conditional:

- [Access methods, selectivity and estimates](access-selectivity.md) — Which distribution and operators make an index or access path appropriate?
- [Plan evidence and index lifecycle](plan-lifecycle.md) — What does EXPLAIN omit and what operational work does an index change create?
- [Negative query cases and controlled validation](query-counterexamples.md) — Which workload change can reverse an apparently successful index decision?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
