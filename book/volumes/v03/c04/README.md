---
metadata_version: 1
id: "tycho.chapter.7a07973ba5314c3983a4c93acc1d1b89"
kind: "chapter"
parent_id: "tycho.volume.c4854b444d7c480e9616c5bf06f4db08"
canonical_path: "book/volumes/v03/c04/README.md"
title: "V03/C04 — Asynchronous APIs and streaming"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which flow and cancellation semantics are required across protocols?"
route_hints:
  questions:
    - "Which flow and cancellation semantics are required across protocols?"
  prerequisites:
    - "tycho.chapter.b9bf60e22dc04878a05aeca98610b5d1"
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

# V03/C04 — Asynchronous APIs and streaming

## Purpose and mission

Which flow and cancellation semantics are required across protocols? This chapter owns that question within execution models, concurrency and flow control. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Specify stream ordering, buffer ownership, cancellation, checkpoints and resume expiry as distinct contracts.

Transport flow control does not promise durable replay; a disconnected client may need a new snapshot rather than an invented continuation. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Asynchronous APIs and streaming: demand, deadlines and cancellation](asynchronous-apis-streaming-and-cancellation.md) | Which flow and cancellation semantics are required across protocols? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Four interaction contracts](asynchronous-apis-streaming-and-cancellation.md#1-four-interaction-contracts).
- [2. Backpressure is a contract between producers and consumers](asynchronous-apis-streaming-and-cancellation.md#2-backpressure-is-a-contract-between-producers-and-consumers).
- [Engineering walkthrough — Reconnect cannot recover unpersisted stream items](asynchronous-apis-streaming-and-cancellation.md#engineering-walkthrough-reconnect-cannot-recover-unpersisted-stream-items).
- [7. Public source ledger and limits](asynchronous-apis-streaming-and-cancellation.md#7-public-source-ledger-and-limits).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V03 — Execution models, concurrency and flow control](../README.md) |
| Previous | [V03/C03 — Reactive streams, demand and cancellation](../c03/README.md) |
| Next | [V03/C05 — Thread, connection and buffer pools](../c05/README.md) |
| Prerequisite | [V03/C03 — Reactive streams, demand and cancellation](../c03/README.md) |
| Source reading | [Page-local evidence and versions](asynchronous-apis-streaming-and-cancellation.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
