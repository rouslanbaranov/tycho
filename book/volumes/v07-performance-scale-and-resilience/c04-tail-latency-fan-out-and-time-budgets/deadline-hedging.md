---
metadata_version: 1
id: "tycho.page.e229cbbcdc4a45bb9e368313f129b25b"
kind: "page"
parent_id: "tycho.chapter.2ad010c2b29c4390b83bbdadeb346289"
canonical_path: "book/volumes/v07-performance-scale-and-resilience/c04-tail-latency-fan-out-and-time-budgets/deadline-hedging.md"
title: "Deadlines, hedging and bounded degradation"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "When can an extra attempt improve a tail without exhausting the protected resource?"
route_hints:
  questions:
    - "When can an extra attempt improve a tail without exhausting the protected resource?"
  prerequisites:
    - "tycho.page.45935212b3b7476d8a163520f065b825"
  related_ids:
    - "tycho.chapter.2ad010c2b29c4390b83bbdadeb346289"
    - "tycho.page.eb130a7f820544a2ba0e0883c0ce587b"
    - "tycho.page.c8b09f5ad28441ab89a6d9e06e0ff4c9"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "deadline"
    - "hedging"
evidence_scope:
  source_ids:
    - "src.aws-backoff"
    - "src.sre-cascading"
    - "src.tail-at-scale"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.eb130a7f820544a2ba0e0883c0ce587b; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Deadlines, hedging and bounded degradation

**Owning question:** When can an extra attempt improve a tail without exhausting the protected resource?

This page belongs to [V07/C04 — Tail latency, fan-out and time budgets](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.eb130a7f820544a2ba0e0883c0ce587b:3 -->
## 3. Deadlines are a resource and correctness contract

A **deadline** is the latest useful completion time for a request at a named boundary. A per-hop timeout is a local waiting limit. An unlimited chain of generous per-hop timeouts can outlive the caller, waste resources, and amplify queueing after an upstream failure. The [Google SRE cascading failures chapter](https://sre.google/sre-book/addressing-cascading-failures/) describes why outstanding work past caller deadlines contributes to cascading problems; the [gRPC deadlines guide](https://grpc.io/docs/guides/deadlines/) describes deadline propagation and time remaining.

**Synthetic budget:** a 1,000 ms end-to-end ceiling is allocated at the start of a fictional request as:

| Segment | Planning reservation (not a measured percentile) |
|---|---:|
| Ingress and authorization | 60 ms |
| Parallel fan-out and required consistency | 600 ms |
| Aggregation and response formatting | 120 ms |
| Network, scheduling and explicit safety reserve | 220 ms |
| **Total hard planning envelope** | **1,000 ms** |

These are *negotiated planning limits*, not statistical predictions. If ingress takes 130 ms instead of 60 ms, no component should keep the original 1,000 ms from that point: remaining time must be recomputed against the original absolute deadline. Some processing may still complete after the response deadline if the domain explicitly requires durable accepted work and exposes a later outcome; that is a **separate durable job contract**, not an invisible extension of a synchronous request.

An implementation-aware deadline design records:

1. Clock and deadline propagation semantics; monotonic elapsed-time measurement locally, converted remaining duration for remote calls where appropriate.
2. Maximum time spent queued before work begins; a queue that admits already-expired work contributes cost without useful output.
3. What cancellation stops (further calculation, network reads, speculative replicas) and what it **cannot undo** (committed state, external side effects).
4. Per-hop retry ownership, attempts, backoff, cumulative budget, and which operation identities make retries safe.
5. How late replies are drained/ignored, how resources are released, and how partial results are represented to the caller.

**Failure example:** a parent invokes a slow service, times out, retries at two independent layers, then the retrying work saturates a shared pool. Even if each individual retry was below its local maximum, aggregate offered load can rise sharply while completed useful work falls. [Amazon Builders' Library: Timeouts, Retries, and Backoff with Jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) discusses timeout selection, retry multiplication and load spreading. A retry must be a business-safe, bounded, capacity-aware action, not a reflex triggered by every high latency.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.eb130a7f820544a2ba0e0883c0ce587b:4 -->
## 4. Hedging, replication and selective degradation

A **hedged request** sends an additional equivalent read to another viable replica when an earlier attempt appears unexpectedly slow, then uses an acceptable response and cancels remaining attempts. It can reduce an independent slow-replica tail; it can also double work exactly when a shared dependency is already saturated. The 2013 *Tail at Scale* paper describes deferred hedges and other tail-tolerance mechanisms; it is not evidence that hedging is safe in all deployments.

| Mitigation | Needed condition | Failure / contraindication |
|---|---|---|
| Improve slow path | The slow suboperation is identified in traces and controlled samples | Tuning a fast dependency changes no parent critical path |
| Parallelize independent reads | Outputs truly independent and resources available | Fan-out increases load, pool contention and tail exposure |
| Hedge delayed reads | Equivalent replicas; bounded speculative budget; cancellation; measured independent tails | Shared bottleneck, expensive writes, inconsistent replicas |
| Retry with jitter | Transient failure, safely repeatable effect and spare capacity | Retries magnify overload; caller deadline already expired |
| Return partial / cached result | Business semantics explicitly permit stale or absent optional data | Incomplete mandatory result presented as valid |
| Shed excess work | Defined admission priority, bounded queue and explicit caller outcome | Rejection without backoff creates retry storm |
| Async durable job | User need not block until completion; job state survives crash | Reinterpreting a synchronous contract without client agreement |

Speculative duplicate **writes** are not a general tail-latency technique. Different replicas may accept divergent effects, and a client receiving one reply cannot assume the other attempt did nothing. See [outbox/idempotency](../../../distributed/transactional-outbox-and-idempotency.md) and [HTTP/RPC operation identity](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/http-rpc-contracts-and-compatibility.md) before recommending retries for effects.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](tails-critical-path.md) |
| Next | [Continue the reasoning](tail-experiments.md) |
| Integrated question | [Original scenario and limits](tail-latency-fanout-and-deadline-budgets.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
