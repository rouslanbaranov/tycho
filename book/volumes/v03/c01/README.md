---
metadata_version: 1
id: "tycho.chapter.13ad4371e75b49dcb5e082ea62083ee3"
kind: "chapter"
parent_id: "tycho.volume.c4854b444d7c480e9616c5bf06f4db08"
canonical_path: "book/volumes/v03/c01/README.md"
title: "V03/C01 — Threads, tasks and coordination"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What creates concurrency and which shared state creates contention?"
route_hints:
  questions:
    - "What creates concurrency and which shared state creates contention?"
  prerequisites:
    - "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
    - "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
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

# V03/C01 — Threads, tasks and coordination

## Purpose and mission

What creates concurrency and which shared state creates contention? This chapter owns that question within execution models, concurrency and flow control. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Give concurrent work a lifetime, result owner and cancellation policy rather than treating each thread as an independent business operation.

Cancelling a task requests termination; it cannot undo a downstream commit that already occurred. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Threads, tasks and coordination: cancellation and resource ownership](threads-tasks-structured-coordination.md) | What creates concurrency and which shared state creates contention? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Four distinct concurrency boundaries](threads-tasks-structured-coordination.md#1-four-distinct-concurrency-boundaries).
- [2. ExecutorService and cooperative cancellation](threads-tasks-structured-coordination.md#2-executorservice-and-cooperative-cancellation).
- [6. Proposed tests and source ledger](threads-tasks-structured-coordination.md#6-proposed-tests-and-source-ledger).
- [Applied M9 evidence: what transfers and what does not](threads-tasks-structured-coordination.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V03 — Execution models, concurrency and flow control](../README.md) |
| Previous | [V02/C07 — Authorization boundaries and multitenancy](../../v02/c07/README.md) |
| Next | [V03/C02 — Java execution and virtual threads](../c02/README.md) |
| Prerequisite | [V01/C02 — Workload and demand models](../../v01/c02/README.md) |
| Prerequisite | [V02/C05 — Public APIs, HTTP/RPC and compatibility](../../v02/c05/README.md) |
| Source reading | [Page-local evidence and versions](threads-tasks-structured-coordination.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
