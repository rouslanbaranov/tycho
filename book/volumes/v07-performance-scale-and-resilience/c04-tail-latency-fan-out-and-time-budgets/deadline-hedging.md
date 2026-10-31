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
    - "src.grpc-hedging"
    - "src.sre-cascading"
    - "src.tail-at-scale"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Bounded question from tycho.page.eb130a7f820544a2ba0e0883c0ce587b; four
    public units inspected 2026-10-31: Google SRE cascading-failure
    cancellation, the 2013 Tail at Scale hedged-request section, gRPC request
    hedging, and AWS retry/backoff guidance. Exact inherited citation rows and
    limits remain in the chapter source ledger. New synthetic additions are
    separately labelled.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
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

> **Pattern atlas:**
> [Hedged Requests](../../v11-pattern-atlas/c07-resilience/README.md#hedged-requests) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.eb130a7f820544a2ba0e0883c0ce587b:4 -->
## 4. Hedging, replication and selective degradation

A **hedged request** sends the same read to another replica or service instance when
the first attempt is slow, uses the first acceptable response, and cancels the
remaining attempts. Google SRE's
[cascading-failures chapter](https://sre.google/sre-book/addressing-cascading-failures/)
says systems send "RPCs to a primary server, then some time later, send the same
request to other instances of the same service" and then "cancel the
now-superfluous requests." The 2013 *Tail at Scale* paper calls this a hedge and
reports that deferring the second request until the first has been outstanding
beyond the 95th-percentile expected latency limited the extra load to about 5% in
its example. [gRPC's request-hedging guide](https://grpc.io/docs/guides/request-hedging/)
implements the same shape: multiple copies of the same request go to different
backends, the first response wins, and outstanding copies are canceled.

**Invariant.** A hedge is defensible only when four conditions hold together.
(1) The replicas must be equivalent for the operation: the paper issues the same
request to multiple replicas, gRPC sends it to different backends, and SRE sends it
to other instances of the same service. (2) The speculation must be bounded:
gRPC makes `maxAttempts` mandatory and caps values above 5 at 5, and its retry
throttling cancels further hedges when the token count falls to the threshold.
(3) Cancellation must stop the losers: SRE says the client sends cancellation
messages for the now-superfluous requests and that cancellation should propagate
through the stack; gRPC cancels outstanding requests when a response arrives.
(4) The delay must come from the measured latency distribution of that request
class, not a guess: the paper uses the 95th percentile and reports a
99.9th-percentile effect in its benchmark. **Tycho rule:** record the measured
percentile, the replica-equivalence check, the attempt cap and the cancellation
evidence; a hedge without all four is an unbounded duplicate.

The decision aid below is Tycho guidance; the labelled paragraphs are the bound
claims.

- **Hedge a delayed read.** Require equivalent replicas, bounded attempts,
  cancellation and a delay from a measured latency percentile. A shared
  bottleneck, an expensive write or non-equivalent replicas contraindicate it.
- **Single measured timeout.** Choose the timeout from the downstream latency
  percentile; a timeout below normal latency or late work that still consumes
  capacity is a failure.
- **Retry with backoff.** Retry only a transient, safely repeatable effect with a
  retry budget; retries amplify overload and a caller deadline can expire first.
- **Partial or cached result.** Return it only when semantics permit stale or
  missing optional data; an incomplete mandatory result presented as valid is a
  failure.
- **Shed excess work.** Require admission priority, a bounded queue and an
  explicit caller outcome; rejection without backoff creates a retry storm.
- **Async durable job.** Use it when the caller need not block and job state
  survives a crash; do not reinterpret a synchronous contract without agreement.

**Failure and recovery.** A hedge adds a second copy of the work and can raise load
when a shared dependency is saturated. The paper warns that naive implementations
"add unacceptable additional load"; gRPC says they "could add significant load to
the backend servers" and provides throttling "to prevent server overload"; AWS says
retries under overload "can make matters significantly worse" and "can even delay
recovery". Duplicate effects are a separate hazard. gRPC describes hedging as
"retrying the original RPC before a failure is even received"; AWS warns that a
timeout or failure "doesn't necessarily mean that side effects haven't happened"
and that APIs with side effects "aren't safe to retry unless they provide
idempotency" because duplicate side effects are possible. **Tycho inference:** a
hedged write can therefore duplicate an effect even when the client accepts only one
response; treat a speculative write as unsafe until the effect has an idempotency
identity and cancellation is shown to stop committed work. Disable the hedge when
replicas share a bottleneck, when the operation is not safely repeatable, or when
cancellation cannot stop the duplicate.

**Alternative.** Prefer a single bounded attempt with a timeout chosen from the
measured latency distribution, or a retry with backoff, jitter and a token-bucket
retry budget, when the replicas share a bottleneck or the operation is not safely
repeatable. AWS recommends choosing a timeout from the downstream latency
percentile (its example uses p99.9) and describes jitter as spreading retries in
time and a local token bucket as limiting them. gRPC classifies hedging as one of
two retry policies, so its ordinary retry policy is the competing configuration.
**Tycho choice rule:** reverse the hedge when the extra copy's measured tail benefit
is smaller than its added load, or when a loser can commit an effect before
cancellation.

**Unbound heuristics.** Improving a known slow suboperation or parallelizing truly
independent reads can also help, but neither is a substitute for the hedge's
equivalence and cancellation conditions; this page keeps both as Tycho guidance
because the bound units do not test them.

Speculative duplicate **writes** are not a general tail-latency technique. Different
replicas may accept divergent effects, and a client receiving one reply cannot
assume the other attempt did nothing. See
[outbox/idempotency](../../../distributed/transactional-outbox-and-idempotency.md)
and
[HTTP/RPC operation identity](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/http-rpc-contracts-and-compatibility.md)
before recommending retries for effects.

**Bound source limits.** Four public units were inspected on 2026-10-31: Google
SRE, *Addressing Cascading Failures*, section *Cancellation propagation*; Dean and
Barroso, *The Tail at Scale*, CACM February 2013, section *Hedged requests*; gRPC,
*Request Hedging*; and AWS Builders' Library, *Timeouts, Retries, and Backoff with
Jitter*. The exact units are
<https://sre.google/sre-book/addressing-cascading-failures/>,
<https://mags.acm.org/communications/201302/?pg=79>,
<https://grpc.io/docs/guides/request-hedging/> and
<https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/>.
Bound and retained records: `read.sre-cascading-hedging.2026-10-31`,
`read.tail-at-scale-hedged.2026-10-31`, `read.grpc-hedging.2026-10-31` and
`read.aws-backoff-hedging.2026-10-31`; `read.batch4-sre-cascading.2026-10-21` and
`read.aws-builders-timeouts-retries.2026-10-31` are retained records. The units
are a book chapter, a research article, documentation and an engineering article,
not benchmarks or production observations. The measured-percentile example is the
paper's 2013 benchmark, not a prediction for another deployment. The operational
rule to record the percentile, equivalence check, attempt cap and cancellation
evidence is Tycho guidance; the sources do not establish a universal hedge delay,
attempt count or cancellation guarantee. The slow-path and independent-read options
are Tycho heuristics, not bound claims.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](tails-critical-path.md) |
| Next | [Continue the reasoning](tail-experiments.md) |
| Integrated question | [Original scenario and limits](tail-latency-fanout-and-deadline-budgets.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
