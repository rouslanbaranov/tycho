---
metadata_version: 1
id: "tycho.page.43414664520b4866929f7f006f27f59b"
kind: "page"
parent_id: "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/deadlines-retries.md"
title: "Deadlines, cancellation and retry budgets"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "How should one end-to-end time budget bound nested calls and retries?"
route_hints:
  questions:
    - "How should one end-to-end time budget bound nested calls and retries?"
  prerequisites:
    - "tycho.page.e7e65b602c5a41fb80fa4a1e88a33298"
  related_ids:
    - "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
    - "tycho.page.de9c5bc478ba44718fcb731e69109dce"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "deadlines"
    - "retries"
evidence_scope:
  source_ids:
    - "src.http-semantics"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.cccbd188936543a2aaf904f4002236d8; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Deadlines, cancellation and retry budgets

**Owning question:** How should one end-to-end time budget bound nested calls and retries?

This page belongs to [V02/C05 — Public APIs, HTTP/RPC and compatibility](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.cccbd188936543a2aaf904f4002236d8:3 -->
## 3. End-to-end deadlines, cancellation and retry budgets

A timeout on one socket is not a complete request deadline. The caller has an end-to-end business time budget; proxies, authentication, queueing, internal RPCs and durable state can consume it. An API must define which result is still meaningful after the caller stops waiting, and what resource cleanup follows.

The [gRPC deadlines guide](https://grpc.io/docs/guides/deadlines/) explains that an RPC deadline is the latest point at which the client is willing to wait; propagation between calls can subtract elapsed time and thereby limit an internal call to the remaining budget. Language-specific defaults and propagation configuration differ. The [gRPC cancellation guide](https://grpc.io/docs/guides/cancellation/) makes clear that cancellation of a call should stop initiated work where possible; user code may need to check and propagate the signal. **Cancellation is not proof that a previously committed effect was undone.**

A **hypothetical** 900-ms request budget could be partitioned into 50 ms of edge/auth overhead, 100 ms in queueing, 450 ms downstream work, 100 ms durable write, and 200 ms network/margin. These numbers are invented for illustration, not a target for any product. Per-hop independent 900-ms timeouts would allow the aggregate to vastly exceed the caller's deadline. At each hop the effective budget is at most the remaining time, subject to clock and propagation behavior. Critical cleanup and reconciliation may need to continue after the synchronous response budget expires, using an explicitly durable workflow rather than an unbounded request task.

The [gRPC retry guide](https://grpc.io/docs/guides/retry/) distinguishes transparent retries from configured retry policies; configurable retries are limited by status, attempts, backoff and commitment boundaries. A service configuration can also set per-method timeouts and retry/hedging behavior. These client mechanisms cannot infer application effect identity: an RPC retry is safe only when the underlying operation semantics and downstream effects allow it.

**Retry decision contract:**

- First ask whether the operation is read-only, semantically idempotent, or protected by an application effect key.
- Retry only a documented retryable failure class, with a bounded total deadline and bounded attempt/backoff budget; observe server pushback/backpressure.
- Prefer explicit outcome lookup for an ambiguous durable command, rather than treating every timeout as “nothing happened”.
- Avoid retry amplification across proxy, API and downstream clients; designate where retries are owned and instrument actual attempt counts.
- Reject the assumption that a cancelled response retracts committed state or emitted events.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](effect-identity.md) |
| Next | [Continue the reasoning](version-compatibility.md) |
| Integrated question | [Original scenario and limits](http-rpc-contracts-and-compatibility.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
