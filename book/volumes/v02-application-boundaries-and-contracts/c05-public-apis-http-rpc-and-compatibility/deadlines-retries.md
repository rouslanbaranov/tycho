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
    - "src.sre-overload"
    - "src.sre-cascading"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.cccbd188936543a2aaf904f4002236d8; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-21"
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

### Local overload versus broad overload

An error response does not by itself justify a retry. The decision also depends on how much
of the fleet is failing and on which layer observed the failure.

- **A small overloaded subset.** If one backend or a small fraction of instances is
  overloaded while other eligible instances have capacity, an immediate retry on another
  instance can redistribute work. The operation must still be safe to repeat, the remaining
  deadline must allow it, and the retry must consume the same budget.
- **Broad overload.** If a large fraction of instances is overloaded, another attempt is
  likely to meet the same condition. Return an explicit overload result and let the caller
  decide. A backend should propagate a specific "overloaded; do not retry" signal rather
  than a generic error that every layer retries.
- **Retry at one layer.** Retry only at the layer immediately above the layer that rejected
  the request. Lower layers should return a classified result, not independently retry work
  that the caller has already judged non-retryable. This avoids a combinatorial retry
  explosion across proxy, API, service and client layers.

### Three retry budgets

A per-request attempt cap bounds one logical operation. It does not bound the aggregate work
created by many clients. Use complementary budgets:

- **Per-request attempt cap.** Bounds attempts for one logical operation and consumes the
  remaining deadline. It does not bound aggregate retry load.
- **Per-client retry ratio.** Bounds retries relative to a client's recent original
  requests. Sparse clients may lack enough history for a stable ratio; do not treat the
  ratio as a guarantee or as a substitute for a deadline.
- **Process- or service-wide retry budget.** Caps total retry work across clients and
  operations. This is the one budget that directly protects a shared dependency from a
  retry storm.

The source's example thresholds are contextual. Use measured failure rates, deadlines and
dependency capacity; record the chosen budgets and the observations that would change them.
Count original attempts and retries separately, and measure retry amplification by layer.

[Handling Overload](https://sre.google/sre-book/handling-overload/) and
[Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)
describe the local-versus-broad distinction and complementary retry budgets. Their numeric
thresholds are examples, not defaults.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Retry with Exponential Backoff](../../v11-pattern-atlas/c07-resilience/README.md#retry-with-exponential-backoff) — decision conditions and contraindications.
> [Retry with Jitter](../../v11-pattern-atlas/c07-resilience/README.md#retry-with-jitter) — decision conditions and contraindications.
> [Timeout](../../v11-pattern-atlas/c07-resilience/README.md#timeout) — decision conditions and contraindications.
> [Deadline Propagation](../../v11-pattern-atlas/c07-resilience/README.md#deadline-propagation) — decision conditions and contraindications.


## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](effect-identity.md) |
| Next | [Continue the reasoning](version-compatibility.md) |
| Integrated question | [Original scenario and limits](http-rpc-contracts-and-compatibility.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is not the main subject of
this page. They are synthetic design guidance, not measured evidence, and they do not create a new
source claim.

### Retry with Jitter

Jitter randomizes each retry delay so independent clients do not retry in lockstep, spreading
attempts across a window or adding a random offset to an exponential base. Every attempt must
consume the same end-to-end deadline and attempt budget, so added delay cannot extend the caller's
useful completion window.

Synchronized retries convert a brief failure into a sustained overload; compare actual attempt
counts and retry arrivals with the planned budget and stop the retry policy when pushback persists.
Retry without jitter at a single layer, or do not retry at all when the failure is non-retryable;
add jitter when many clients share the same dependency and retry signal.
