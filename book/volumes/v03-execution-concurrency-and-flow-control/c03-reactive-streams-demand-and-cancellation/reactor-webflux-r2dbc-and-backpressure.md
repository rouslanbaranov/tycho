---
metadata_version: 1
id: "tycho.page.114da51171c2474ebd56ee3bebad3bcb"
kind: "page"
parent_id: "tycho.chapter.b9bf60e22dc04878a05aeca98610b5d1"
canonical_path: "book/volumes/v03-execution-concurrency-and-flow-control/c03-reactive-streams-demand-and-cancellation/reactor-webflux-r2dbc-and-backpressure.md"
title: "Reactive execution, WebFlux, R2DBC and backpressure"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Reactive streams, demand and cancellation. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How do backpressure, scheduling and blocking boundaries affect execution?"
  prerequisites: []
  related_ids:
    - "tycho.page.02238832b395417bae63939cd96b9134"
    - "tycho.page.83e414ec3d1b4b07a443de2c96ce2c4e"
    - "tycho.page.0c7b8f00661648f3b50e448471f5cc7e"
    - "tycho.page.577d52b851c3478eb73e301ace1bcfea"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Reactive"
    - "execution"
    - "WebFlux"
    - "R2DBC"
    - "and"
    - "backpressure"
evidence_scope:
  source_ids:
    - "src.r2dbc"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-18"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.114da51171c2474ebd56ee3bebad3bcb:-1 -->

# Reactive execution, WebFlux, R2DBC and backpressure

> **Tycho #82; research inspected 2026-10-18.** Canonical question: when does a nonblocking reactive chain improve a service, and which guarantees survive a database, queue or HTTP boundary? Scope: Reactor Core **3.7.0**, Spring Framework **6.2** reference, R2DBC SPI **1.0.0.RELEASE**. No running Spring application, driver, benchmark or independent review is claimed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.114da51171c2474ebd56ee3bebad3bcb:7 -->
## Engineering walkthrough — Subscriber demand does not protect an unseen blocking queue

**Original fictional streaming endpoint:** a Reactor service subscribes to a database-backed event stream and transforms updates for WebSocket clients. A downstream subscriber requests `n=1` item at a time, but a library callback invokes a blocking JDBC query on an event-loop thread and enqueues unbounded work before the publisher honors demand. The public Reactive Streams request protocol only coordinates compliant participants; it does not cap an unrelated driver pool or hidden queue.

| Boundary | Normal behavior | Fault injection / observation |
|---|---|---|
| Publisher → subscriber | Emit within recorded demand and cancellation state | Slow consumer requests zero additional items; count retained buffers |
| Scheduler/event loop | Nonblocking callbacks do brief work | Inject 200 ms blocking call; check event-loop delays of unrelated sessions |
| R2DBC/DB connections | Bounded leases and driver-specific cancellation | Close client while SQL is in flight; prove cleanup separately from transaction effect |
| Retry/reconnect | Stable event or operation identity | Lost reply after committed mutation cannot be undone by `cancel` |

On cancellation, stop *new* useful work and release buffers/leases where supported; any durable effect already committed requires authoritative reconciliation. Moving the blocking JDBC call to `boundedElastic` can protect event-loop responsiveness but only **relocates** waiting and resource budgeting. It may still saturate the downstream. Reactor 3.7 scheduler/context documentation and R2DBC 1.0 SPI describe API contracts, not proof that any specific driver or application meets them.

**Proposed (not run):** one slow client, one disconnected client and one stalled database under equal offered messages; observe emitted/requested counts, heap growth, queue age, pool leases and final durable effects. Compare bounded reactive path with a simpler thread-per-request architecture. Choose reactive only if its true end-to-end flow control and operational costs satisfy the workload.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.114da51171c2474ebd56ee3bebad3bcb:8 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Netflix — Zuul 2 nonblocking gateway](../../../cases/netflix-zuul2-nonblocking-gateway.md)**. **Relevant mechanism or architectural contrast:** Long-lived connections are a workload-specific reason to consider nonblocking gateway I/O. **Not established by this report/playbook:** Netflix's company-reported results do not prove reactive execution beats blocking APIs for all workloads or improve every failure mode.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Trace demand, queues and blocking work across the complete reactive pipeline, including scheduler boundaries.

Subscriber backpressure cannot bound an unrelated blocking queue; an event-loop-friendly API may still hide a bottleneck downstream.

The detailed pages separate the mechanisms that make this decision conditional:

- [Nonblocking execution and demand](demand-blocking.md) — Which demand boundary actually controls a producer and where can blocking escape it?
- [Schedulers, context and reactive database access](scheduler-context.md) — Which scheduling and context assumptions must hold at a reactive-to-database boundary?
- [Reactive failure and decision limits](reactive-recovery.md) — What failure or overload observation would reject the proposed reactive design?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
