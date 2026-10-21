---
metadata_version: 1
id: "tycho.page.045713bc4f054663b676e4e1b6fe9725"
kind: "page"
parent_id: "tycho.chapter.e451bfe1e0cb4c588f0576e0b2b7d3d0"
canonical_path: "book/volumes/v05-data-models-engines-and-lifecycle/c03-query-planning-indexes-and-access-paths/query-counterexamples.md"
title: "Negative query cases and controlled validation"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
summary: "Which workload change can reverse an apparently successful index decision?"
route_hints:
  questions:
    - "Which workload change can reverse an apparently successful index decision?"
  prerequisites:
    - "tycho.page.9b9c3ab86633469185416e4e88c0caca"
  related_ids:
    - "tycho.chapter.e451bfe1e0cb4c588f0576e0b2b7d3d0"
    - "tycho.page.7a136445bbfe4a8194c2c4db8a8818ee"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "query"
    - "counterexamples"
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
# Negative query cases and controlled validation

**Owning question:** Which workload change can reverse an apparently successful index decision?

This page belongs to [V05/C03 — Query planning, indexes and access paths](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.7a136445bbfe4a8194c2c4db8a8818ee:6 -->
## 6. Original negative cases

| Proposed observation | Possible interpretation | What it does not establish |
|---|---|---|
| Index scan appears after creating B-tree | Planner found it cheaper for tested input | End-to-end p99 improvement under peak load |
| Estimate 10 rows; actual 100,000 | Bad cardinality/statistics assumption possible | That adding another index is the only fix |
| GIN reduces tag search scan work | Inverted lookup fits the predicate | Low write amplification or semantic relevance |
| BRIN index is tiny | Block summary has low storage overhead | It can prune enough unrelated blocks on shuffled data |
| Covering index enables index-only scan sometimes | Visibility map and query shape made it possible | Heap reads always disappear |
| More parallel workers lower one query time | Extra capacity is used | Overall system throughput improves with fixed resource budget |

These observations are **illustrative possibilities, not executed results**. A planner may change choices across parameter values, row distributions and PostgreSQL minor updates.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7a136445bbfe4a8194c2c4db8a8818ee:7 -->
## 7. Controlled acceptance method

1. Fix PostgreSQL major/minor version, input SQL/parameters and schema.
2. Use an admitted synthetic dataset reflecting cardinality and correlated distributions; record construction method.
3. Freeze comparable CPU/memory/IO and concurrency envelopes.
4. Gather statistics, inspect estimated rows and safely run EXPLAIN ANALYZE for read-only queries.
5. Compare with and without candidate index under the same input and warm/cold state.
6. Include writes, index maintenance, lock waits, storage and backup cost in the result.
7. Capture client-level latency, successful/failed outcome denominators and p95/p99 on an appropriate sample.
8. Review negative edge cases (rare keys, extreme skew, empty results, retention/change).
9. Reject improvements based only on non-representative synthetic query selection.

The procedure is a design proposal. No steps were run or published as performance findings.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](plan-lifecycle.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](postgresql-indexes-statistics-and-query-plans.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
