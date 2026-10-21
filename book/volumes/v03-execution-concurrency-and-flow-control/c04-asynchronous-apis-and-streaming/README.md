---
metadata_version: 1
id: "tycho.chapter.7a07973ba5314c3983a4c93acc1d1b89"
kind: "chapter"
parent_id: "tycho.volume.c4854b444d7c480e9616c5bf06f4db08"
canonical_path: "book/volumes/v03-execution-concurrency-and-flow-control/c04-asynchronous-apis-and-streaming/README.md"
title: "V03/C04 — Asynchronous APIs and streaming"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which flow and cancellation semantics are required across protocols? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Which flow and cancellation semantics are required across protocols?"
  prerequisites:
    - "tycho.chapter.b9bf60e22dc04878a05aeca98610b5d1"
  related_ids:
    - "tycho.page.da7cd1ad59584b8a8ece7aab0f8f35b5"
    - "tycho.page.fbb4bc905d02495dbe3d7675d8670235"
    - "tycho.page.e067b74eabc24cabb209ca8835c0f7cd"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](asynchronous-apis-streaming-and-cancellation.md) | Which flow and cancellation semantics are required across protocols? |
| [Stream interaction and buffer ownership](stream-contracts.md) | Who controls demand and owns buffered items in an asynchronous exchange? |
| [Cancellation, reconnect and durable resume](resume-cancellation.md) | Which persisted state permits replay after a disconnect and when must a client resnapshot? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V03 — Execution models, concurrency and flow control](../README.md) |
| Previous | [V03/C03 — Reactive streams, demand and cancellation](../c03-reactive-streams-demand-and-cancellation/README.md) |
| Next | [V03/C05 — Thread, connection and buffer pools](../c05-thread-connection-and-buffer-pools/README.md) |
| Prerequisite | [V03/C03 — Reactive streams, demand and cancellation](../c03-reactive-streams-demand-and-cancellation/README.md) |
| Source reading | [Page-local evidence and versions](asynchronous-apis-streaming-and-cancellation.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.da7cd1ad59584b8a8ece7aab0f8f35b5:8 -->
## 7. Public source ledger and limits

| Published source | Narrow support | Unknown |
|---|---|---|
| [Reactive Streams JVM 1.0.4](https://github.com/reactive-streams/reactive-streams-jvm) | Nonblocking demand/backpressure semantics and specification/TCK | Correctness of a fictional streaming API |
| [gRPC Flow Control](https://grpc.io/docs/guides/flow-control/) | Transport streaming buffers/read capacity and non-unary scope | Application-level durable replay |
| [gRPC Cancellation](https://grpc.io/docs/guides/cancellation/) | Caller/worker cancellation propagation | Reversal of committed external effects |
| [Tycho reactive execution](../c03-reactive-streams-demand-and-cancellation/reactor-webflux-r2dbc-and-backpressure.md) | Version-scoped framework scheduling and demand mechanics | Executed end-to-end client/server validation |

The streaming protocol, failure cases and diagrams are original synthetic educational material. No real integration tests, resource measurements, vendor conformance audit or editorial acceptance occurred.

**Navigation:** proposed **V03/C04** in [book outline](../../../PROPOSED-STRUCTURE.md), current [execution landing](../../../execution/README.md). Before: [Threads/tasks](../c01-threads-tasks-and-coordination/threads-tasks-structured-coordination.md), [Reactive execution](../c03-reactive-streams-demand-and-cancellation/reactor-webflux-r2dbc-and-backpressure.md). After: [API/RPC compatibility](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/http-rpc-contracts-and-compatibility.md), [Tail latency](../../v07-performance-scale-and-resilience/c04-tail-latency-fan-out-and-time-budgets/tail-latency-fanout-and-deadline-budgets.md).
<!-- /tycho-question-source -->
