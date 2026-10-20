---
metadata_version: 1
id: "tycho.chapter.d5b789c9cd7e4cb693c22943423531c2"
kind: "chapter"
parent_id: "tycho.volume.c4854b444d7c480e9616c5bf06f4db08"
canonical_path: "book/volumes/v03/c02/README.md"
title: "V03/C02 — Java execution and virtual threads"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What improves concurrency without creating downstream capacity?"
route_hints:
  questions:
    - "What improves concurrency without creating downstream capacity?"
  prerequisites:
    - "tycho.chapter.13ad4371e75b49dcb5e082ea62083ee3"
  related_ids: []
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.jep444"
    - "src.jep491"
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

# V03/C02 — Java execution and virtual threads

## Purpose and mission

What improves concurrency without creating downstream capacity? This chapter owns that question within execution models, concurrency and flow control. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Choose execution resources with explicit downstream permits and release-specific blocking assumptions.

Cheaper waiting can increase demand on a saturated connection pool; replacing platform threads with virtual threads does not create database capacity. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Platform-thread executors and virtual-thread capacity](platform-threads-executors-and-virtual-threads.md) | What improves concurrency without creating downstream capacity? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [The concurrency question](platform-threads-executors-and-virtual-threads.md#the-concurrency-question).
- [Platform pools, queues and deadlines](platform-threads-executors-and-virtual-threads.md#platform-pools-queues-and-deadlines).
- [Evidence and status](platform-threads-executors-and-virtual-threads.md#evidence-and-status).
- [Applied M9 evidence: what transfers and what does not](platform-threads-executors-and-virtual-threads.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V03 — Execution models, concurrency and flow control](../README.md) |
| Previous | [V03/C01 — Threads, tasks and coordination](../c01/README.md) |
| Next | [V03/C03 — Reactive streams, demand and cancellation](../c03/README.md) |
| Prerequisite | [V03/C01 — Threads, tasks and coordination](../c01/README.md) |
| Source reading | [Page-local evidence and versions](platform-threads-executors-and-virtual-threads.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
