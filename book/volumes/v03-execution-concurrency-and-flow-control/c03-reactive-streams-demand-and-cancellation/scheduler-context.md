---
metadata_version: 1
id: "tycho.page.0c7b8f00661648f3b50e448471f5cc7e"
kind: "page"
parent_id: "tycho.chapter.b9bf60e22dc04878a05aeca98610b5d1"
canonical_path: "book/volumes/v03-execution-concurrency-and-flow-control/c03-reactive-streams-demand-and-cancellation/scheduler-context.md"
title: "Schedulers, context and reactive database access"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
summary: "Which scheduling and context assumptions must hold at a reactive-to-database boundary?"
route_hints:
  questions:
    - "Which scheduling and context assumptions must hold at a reactive-to-database boundary?"
  prerequisites:
    - "tycho.page.83e414ec3d1b4b07a443de2c96ce2c4e"
  related_ids:
    - "tycho.chapter.b9bf60e22dc04878a05aeca98610b5d1"
    - "tycho.page.114da51171c2474ebd56ee3bebad3bcb"
    - "tycho.page.577d52b851c3478eb73e301ace1bcfea"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "scheduler"
    - "context"
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
# Schedulers, context and reactive database access

**Owning question:** Which scheduling and context assumptions must hold at a reactive-to-database boundary?

This page belongs to [V03/C03 — Reactive streams, demand and cancellation](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.114da51171c2474ebd56ee3bebad3bcb:2 -->
## 3. Reactor 3.7.0: scheduler choice and context

Reactor `Mono<T>` models zero or one value; `Flux<T>` models zero to many. Their creation does not start a new thread or perform the work: subscription starts a chain. By default, most operators execute on the thread delivering their signal. `publishOn(scheduler)` changes execution of subsequent operators; `subscribeOn(scheduler)` changes the subscription path upstream. Neither makes a synchronous driver nonblocking. [E02]

Reactor 3.7.0 documents `Schedulers.boundedElastic()` for wrapping unavoidable blocking operations. It bounds backing resources but still has a queue; queue saturation and expired deadlines must be measured. It also documents a Java 21+ virtual-thread-backed variant controlled by `reactor.schedulers.defaultBoundedElasticOnVirtualThreads=true`. The virtual-thread option does not transform a blocking library into an asynchronous driver or replace explicit downstream admission. Reactor forbids certain blocking APIs on its default single/parallel nonblocking schedulers. [E02]

Illustrative reactive adaptation (not compiled):

```java
// Existing synchronous client: isolate blocking work from event loop.
Mono<Result> adapted = Mono.fromCallable(() -> blockingClient.read(key))
    .subscribeOn(Schedulers.boundedElastic())
    .timeout(Duration.ofSeconds(2));

// Prefer a genuinely reactive driver for a complete nonblocking path:
// DatabaseClient ... -> Mono<Result>, with pool/deadline controls.
```

The example does not configure a finite HTTP connection pool, retry, error mapping or server cancellation. A `timeout` signal alone is not proof that the underlying blocking operation was interrupted.

Reactor `Context` is immutable per-subscriber context propagated with subscription semantics; it is not simply a thread local. In Reactor 3.7.0 the `contextWrite` placement matters: upstream operators see context supplied by downstream subscribers, and asynchronous inner sequences have their own context boundaries. A correlation ID stored only in `ThreadLocal` may disappear or leak across interleaved requests. Test tracing, authentication and logging context through `flatMap`, scheduler switches and client adapters. [E03]

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.114da51171c2474ebd56ee3bebad3bcb:3 -->
## 4. R2DBC 1.0: a reactive SQL SPI, not a database guarantee

R2DBC SPI **1.0.0.RELEASE** (2022-04-25) specifies a Reactive Streams based Java interface for SQL-oriented databases. The spec's *Introduction — The R2DBC SPI* states that execution is deferred and backpressure-aware. *Compliance — R2DBC SPI Compliance* requires a nonblocking I/O layer and transaction support. The specification explicitly distinguishes required and optional driver capabilities. [E04]

R2DBC does not erase transaction isolation, SQL locks, network round trips, pool wait or DB CPU cost. A compliant SPI does not establish that every particular driver supports every feature identically, or that cancelling a reactive subscription aborts a committed transaction. Validate the concrete driver version, connection factory/pool, isolation, timeout, cancellation and error mapping against its own documentation and executable tests.

| Question | JDBC with virtual threads | R2DBC with reactive pipeline |
|---|---|---|
| Application composition | Sequential blocking calls, simple stack | Publishers and async composition |
| Waiting Java execution | Virtual thread normally parks on supported blocking I/O | Event loop generally remains available if all operators are nonblocking |
| SQL isolation and locks | Database-controlled | Database-controlled |
| Connection budget | Required | Required |
| Cancellation of in-flight query | Driver/JDK-specific | Driver/protocol-specific |
| When to prefer | Legacy blocking libraries and simple request flow | Reactive streaming, end-to-end async clients, controlled demand |
| What must be measured | Heap, carrier pinning, pool wait, p99 | Event-loop stalls, buffer growth, pool wait, p99 |

Neither column implies universally superior throughput. The **driver**, not just the return type, determines whether the network I/O path is nonblocking.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](demand-blocking.md) |
| Next | [Continue the reasoning](reactive-recovery.md) |
| Integrated question | [Original scenario and limits](reactor-webflux-r2dbc-and-backpressure.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
