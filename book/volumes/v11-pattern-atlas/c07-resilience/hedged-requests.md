---
metadata_version: 1
id: "tycho.page.667f60a8c7d146809d4e3b98efe02213"
kind: "page"
parent_id: "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
canonical_path: "book/volumes/v11-pattern-atlas/c07-resilience/hedged-requests.md"
title: "Hedged Requests"
topic_ids:
  - "performance-engineering"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "operations"
summary: >-
  Decision card for Hedged Requests; all four dimensions source-bound; coverage
  remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should a duplicate request be issued after a latency threshold to reduce
      tail latency?
  prerequisites:
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
  related_ids:
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "hedging"
    - "tail latency"
    - "resilience and fault tolerance"
evidence_scope:
  source_ids:
    - "src.sre-cascading"
    - "src.tail-at-scale"
    - "src.grpc-hedging"
    - "src.aws-backoff"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.sre-cascading-hedging.2026-10-31,
    read.tail-at-scale-hedged.2026-10-31, read.grpc-hedging.2026-10-31 and
    read.aws-backoff-hedging.2026-10-31; read.batch4-hedged.2026-10-21 is
    retained historical evidence; owner section and limits are bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-31"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# Hedged Requests

**Identity.** Hedged Requests; family Resilience and fault tolerance; kind
resilience-pattern; priority advanced.

**Decision question.** Should a duplicate request be issued after a latency
threshold to reduce tail latency?

**Good-fit conditions.** The operation is a read served by equivalent replicas or
instances; the delay comes from a measured latency percentile for that request
class; attempts are capped and the speculative budget is bounded; cancellation
stops outstanding copies; the first acceptable response wins. Google SRE describes
sending "the same request to other instances of the same service" and canceling
"the now-superfluous requests"; the *Tail at Scale* paper defers the second request
until the first has been outstanding beyond the 95th-percentile expected latency;
gRPC makes `maxAttempts` mandatory, caps values above 5 at 5, and cancels
outstanding requests when a response arrives. **Tycho conditions:** record the
percentile, the replica-equivalence check, the attempt cap and the cancellation
evidence.

**Hard contraindications.** Reject a write or any effect that is not safely
repeatable; reject when replicas share a bottleneck, when the latency threshold is
below normal latency, when attempts are unbounded, or when cancellation cannot stop
the duplicate. gRPC's guide does not make a hedged write safe: it describes
hedging as "retrying the original RPC before a failure is even received", and AWS
warns that APIs with side effects "aren't safe to retry unless they provide
idempotency". **Tycho contraindication:** a speculative write is unsafe until the
effect has an idempotency identity and committed losers can be reconciled.

**Competing alternative.** A single bounded attempt with a timeout chosen from the
measured latency percentile, or a retry with backoff, jitter and a token-bucket
retry budget. AWS recommends choosing a timeout from the downstream latency
percentile (its example uses p99.9), jitter to spread retries, and a local token
bucket to limit them. gRPC classifies hedging as one of two retry policies, so its
ordinary retry policy is the competing configuration. **Tycho choice rule:**
reverse when the extra copy's measured tail benefit is smaller than its added load,
or when a loser can commit an effect before cancellation.

**Failure and recovery.** A hedge adds a second copy of the work and can raise load
when a shared dependency is saturated. The paper warns that naive implementations
"add unacceptable additional load"; gRPC says they "could add significant load to
the backend servers" and provides throttling "to prevent server overload"; AWS says
retries under overload "can make matters significantly worse" and "can even delay
recovery". Duplicate effects are separate: a timeout or failure "doesn't
necessarily mean that side effects haven't happened". Detect extra load, duplicate
effects and ineffective cancellation; cap speculation, cancel losers promptly, and
disable hedging when the tails are not independent. **Tycho runbook:** compare the
added load with the measured tail benefit, and reconcile any effect that a
canceled loser may have committed.

**Technical owner.** [Hedging, replication and selective degradation](../../v07-performance-scale-and-resilience/c04-tail-latency-fan-out-and-time-budgets/deadline-hedging.md#4-hedging-replication-and-selective-degradation) — hedging is bounded to the tail-latency discussion.

**Sources.** Four public units inspected on 2026-10-31: Google SRE
*Addressing Cascading Failures*, section *Cancellation propagation*; Dean and
Barroso, *The Tail at Scale*, CACM February 2013, section *Hedged requests*; gRPC
*Request Hedging*; and AWS Builders' Library, *Timeouts, Retries, and Backoff with
Jitter*. Read records: `read.sre-cascading-hedging.2026-10-31`,
`read.tail-at-scale-hedged.2026-10-31`, `read.grpc-hedging.2026-10-31` and
`read.aws-backoff-hedging.2026-10-31`; source ids `src.sre-cascading`,
`src.tail-at-scale`, `src.grpc-hedging` and `src.aws-backoff` are registered.
The units are a book chapter, a research article, documentation and an engineering
article, not benchmarks or production observations.

**Decision state.** applicable-under-conditions.

**Related entries.** Timeout; Retry with Exponential Backoff; Load Shedding;
Scatter-Gather.
