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
summary: "When are document, wide-column, KV, distributed SQL or analytical stores useful?"
route_hints:
  questions:
    - "When are document, wide-column, KV, distributed SQL or analytical stores useful?"
  prerequisites:
    - "tycho.chapter.e451bfe1e0cb4c588f0576e0b2b7d3d0"
  related_ids: []
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

| Page | Owning question |
|---|---|
| [Storage model alternatives: embedded SQL, distributed SQL, document, wide-column, OLAP, graph and time series](storage-model-alternatives-and-workload-fit.md) | When are document, wide-column, KV, distributed SQL or analytical stores useful? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Start from the workload and invariant, not a database brand](storage-model-alternatives-and-workload-fit.md#1-start-from-the-workload-and-invariant-not-a-database-brand).
- [2. Transactional relational and embedded storage](storage-model-alternatives-and-workload-fit.md#2-transactional-relational-and-embedded-storage).
- [Engineering walkthrough — Four storage choices with disqualifying gates](storage-model-alternatives-and-workload-fit.md#engineering-walkthrough-four-storage-choices-with-disqualifying-gates).
- [Applied M9 evidence: what transfers and what does not](storage-model-alternatives-and-workload-fit.md#applied-m9-evidence-what-transfers-and-what-does-not).

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
