---
metadata_version: 1
id: "tycho.page.da7cd1ad59584b8a8ece7aab0f8f35b5"
kind: "page"
parent_id: "tycho.chapter.7a07973ba5314c3983a4c93acc1d1b89"
canonical_path: "book/volumes/v03-execution-concurrency-and-flow-control/c04-asynchronous-apis-and-streaming/asynchronous-apis-streaming-and-cancellation.md"
title: "Asynchronous APIs and streaming: demand, deadlines and cancellation"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Asynchronous APIs and streaming. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which flow and cancellation semantics are required across protocols?"
  prerequisites: []
  related_ids:
    - "tycho.page.0b493340594c4c4392c5d93940a7f319"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.a2c47a0850154eaa95e1eb97e23f9c71"
    - "tycho.page.114da51171c2474ebd56ee3bebad3bcb"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.e181d96c75784f818a330bb0f266520c"
    - "tycho.page.4e075e4ebc644f0e9b92c05294f62ca4"
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
    - "tycho.page.eb130a7f820544a2ba0e0883c0ce587b"
    - "tycho.page.fbb4bc905d02495dbe3d7675d8670235"
    - "tycho.page.e067b74eabc24cabb209ca8835c0f7cd"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Asynchronous"
    - "APIs"
    - "and"
    - "streaming"
    - "demand"
    - "deadlines"
    - "cancellation"
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
<!-- tycho-question-source:tycho.page.da7cd1ad59584b8a8ece7aab0f8f35b5:-1 -->

# Asynchronous APIs and streaming: demand, deadlines and cancellation

> **Independent Tycho V03/C04 book draft, 2026-10-19.** This chapter compares contract and flow-control choices. Official Reactive Streams 1.0.4 and gRPC guides supply bounded public facts. The example and acceptance tests are original synthetic material; no streaming client/server, implementation or benchmark was exercised.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Asynchronous Request-Reply](../../v11-pattern-atlas/c02-api-communication/README.md#asynchronous-request-reply) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.da7cd1ad59584b8a8ece7aab0f8f35b5:0 -->
## Purpose and mission

An asynchronous interface can separate the sender and receiver in time, but does not make the receiver infinitely fast. A stream introduces questions absent from simple one-response calls: **who controls demand, what happens to in-flight messages on cancellation, how is order defined, and can the conversation resume safely after a disconnection?**

A streaming transport may deliver bytes reliably while an application still loses its *business outcome* after an ambiguous acknowledgment. Backpressure, cancellation, retry identity and durable replay are distinct guarantees.

The [Reactive Streams JVM specification 1.0.4](https://github.com/reactive-streams/reactive-streams-jvm) describes asynchronous stream processing with non-blocking backpressure. The [gRPC flow-control guide](https://grpc.io/docs/guides/flow-control/) describes transport-oriented flow control for streaming RPCs, not unary requests. Neither specification by itself establishes cross-service exactly-once business effects.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.da7cd1ad59584b8a8ece7aab0f8f35b5:7 -->
## Engineering walkthrough — Reconnect cannot recover unpersisted stream items

**Synthetic scenario:** a device-status server streams numbered updates over gRPC to a remote consumer. The network drops after the server sends sequence 41 but before the consumer can acknowledge it; the server emits 42 while the client is offline. Transport flow-control windows influence buffered bytes **while connected** but do not constitute a durable event log or replay cursor.

| Contract decision | Option A: transient live feed | Option B: resumable durable subscription |
|---|---|---|
| Owner of buffered state | Process/session with bounded bytes | Named storage/log with retention and sequence identity |
| Disconnect after sending 41 | Missing/duplicate 41 may be acceptable, explicitly labeled | Client resumes from last *durably processed* sequence; dedup and replay required |
| Slow consumer | Backpressure, drop/coalesce or explicit disconnect | Lag budget, quotas and replay horizon must be declared |
| Publisher restart | Session resumes from current state only | Rebuild cursor from durable authority; cannot replay what was never persisted |

If updates mean *current temperature*, dropping interim samples may be an acceptable product policy. If updates mean *irrevocable financial postings*, an ephemeral stream is not sufficient. Cancellation of a receive loop does not roll back a posting that another system already committed. This trade-off is separate from choosing gRPC vs WebSocket vs SSE.

**Proposed protocol (not implemented):** include `stream_id`, monotonically interpreted position within a declared partition, schema version, snapshot ID and retention boundary. Client checkpoints a position only after its required local effect is durable. Inject disconnect before/after acknowledgment, server restart, slow consumer and position expiry; return an explicit "resnapshot required" response when replay is impossible. The chapter's gRPC flow-control and Reactive Streams sources support bounded transport/demand semantics, not a durable replay guarantee.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Specify stream ordering, buffer ownership, cancellation, checkpoints and resume expiry as distinct contracts.

Transport flow control does not promise durable replay; a disconnected client may need a new snapshot rather than an invented continuation.

The detailed pages separate the mechanisms that make this decision conditional:

- [Stream interaction and buffer ownership](stream-contracts.md) — Who controls demand and owns buffered items in an asynchronous exchange?
- [Cancellation, reconnect and durable resume](resume-cancellation.md) — Which persisted state permits replay after a disconnect and when must a client resnapshot?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is not the main subject of
this page. They are synthetic design guidance, not measured evidence, and they do not create a new
source claim.

### Asynchronous Request-Reply

An asynchronous request-reply interface accepts a request, returns a durable handle and later
exposes the terminal result through polling or a callback. The handle must identify one recorded
operation whose outcome is durable, so a lost reply cannot turn an accepted request into an unknown
effect.

A lost or expired reply leaves the caller unable to decide the outcome; keep the operation record
queryable and reconcile before retrying the original request. A synchronous call with a bounded
deadline is simpler when the work reliably finishes inside the request budget; split the interaction
only when waiting would exceed it.

**Limits.** The handle store, retention, polling/callback security and terminal-state schema
are costs; callbacks need authentication and an idempotent receiver, and polling needs backoff
and expiry.
