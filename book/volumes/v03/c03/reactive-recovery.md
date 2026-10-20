---
metadata_version: 1
id: "tycho.page.577d52b851c3478eb73e301ace1bcfea"
kind: "page"
parent_id: "tycho.chapter.b9bf60e22dc04878a05aeca98610b5d1"
canonical_path: "book/volumes/v03/c03/reactive-recovery.md"
title: "Reactive failure and decision limits"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
summary: "What failure or overload observation would reject the proposed reactive design?"
route_hints:
  questions:
    - "What failure or overload observation would reject the proposed reactive design?"
  prerequisites:
    - "tycho.page.0c7b8f00661648f3b50e448471f5cc7e"
  related_ids:
    - "tycho.chapter.b9bf60e22dc04878a05aeca98610b5d1"
    - "tycho.page.114da51171c2474ebd56ee3bebad3bcb"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "reactive"
    - "recovery"
evidence_scope:
  source_ids:
    - "src.r2dbc"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.114da51171c2474ebd56ee3bebad3bcb; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Reactive failure and decision limits

**Owning question:** What failure or overload observation would reject the proposed reactive design?

This page belongs to [V03/C03 — Reactive streams, demand and cancellation](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.114da51171c2474ebd56ee3bebad3bcb:4 -->
## 5. Failure, recovery and overload boundaries

Consider an **invented** API returning a stream of 10,000 records. The HTTP client requests a small batch then disconnects. The server should stop unnecessary upstream work, release its DB connection and bound any prefetched rows. A non-cancellable driver might continue an expensive query after client disconnect. If a transaction committed before the disconnect, a replayed request needs a business idempotency key. [E01–E04; design inference]

Failure matrix:

| Failure | Visible signal | Required verification |
|---|---|---|
| Event-loop blocked by a synchronous call | Rising event-loop delay and p99 | Thread dump and deliberate slow-call fixture |
| Fast producer, slow client | Demand stall or buffer growth | Buffer cap, backpressure policy, cancel tests |
| R2DBC pool exhausted | Pending acquisition and timeouts | Configured pool cap, queue wait, no leaked connection |
| Client disconnect | Cancellation signal | Query cancellation, resource release, side-effect status |
| Retry after uncertain write | Duplicate or missing business effect | Idempotency/transaction boundary and reconciliation |
| Context loss on scheduler switch | Missing/wrong trace or auth metadata | Cross-scheduler context propagation tests |

A bounded `flatMap` concurrency setting can limit the number of inner publishers, but it does not automatically bound upstream hot sources, DB pool sizes, retries or every internal operator queue. Rate-limiting, admission, and request budgets must be placed at the correct boundaries. Refer to [virtual-thread capacity](../c02/platform-threads-executors-and-virtual-threads.md) for the same resource accounting in imperative code.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.114da51171c2474ebd56ee3bebad3bcb:5 -->
## 6. Decision procedure

Begin with actual request and stream semantics: unary vs streaming, independent vs ordered items, peak arrival, maximum buffering, DB transactions, client cancellation, and dependency quotas. Keep MVC/imperative if its measured capacity and simplicity meet requirements. If streaming and demand control matter, test an end-to-end reactive path with R2DBC or another truly nonblocking driver. If existing JDBC and sequential composition are central, evaluate virtual threads before rewriting every service as Reactor.

Run **equivalent open-loop offered-load** and bounded concurrency tests; include slow DB, slow consumer, disconnect, timeouts and retries. Record completed requests, rejection, CPU, heap, queue wait, event-loop stalls, DB connections, p95/p99 and correctness. Without these observations, no performance winner can be claimed.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](scheduler-context.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](reactor-webflux-r2dbc-and-backpressure.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
