---
metadata_version: 1
id: "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c07-resilience/README.md"
title: "V11/C07 — Resilience and fault tolerance"
topic_ids:
  - "performance-engineering"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "operations"
summary: "All 16 C07 cards with bounded owner links; decision coverage partial."
route_hints:
  questions:
    - "Which resilience mechanisms bound failure without amplifying it?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
    - "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
  excludes:
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "resilience and fault tolerance"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.resilience4j"
    - "src.sre-cascading"
    - "src.sre-overload"
    - "src.rabbitmq"
    - "src.morning-paper-tail-at-scale"
    - "src.kubernetes"
    - "src.postgresql"
  claim_ids: []
  status: "source-linked"
  notes: "16 cards cite read units; owner links are bounded."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-21"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-22"
source_inspection_date: "2026-10-21"
content_verified_at: null
---
# V11/C07 — Resilience and fault tolerance

**Owning question:** Which resilience pattern fits the failure and recovery contract?

## Purpose and mission

This chapter is the atlas entry point for **Resilience and fault tolerance**. It owns
the conditional decision route for 16 catalog entries, not the deep mechanism
explanations. Read the exact owner section before applying a mechanism claim.

All 16 entries have a self-checked card. Owner sections are bounded: an overload or
deadline page may own the failure contract without owning every resilience mechanism.

## Pages and reasoning route

Page count is content-dependent. This chapter currently uses one landing page for all
entries; a later split is an editorial change, not a plan failure. Start with the card,
check its conditions and contraindications, then read the exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Circuit Breaker

**Identity.** Circuit Breaker; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should calls to a failing dependency be rejected early until it
recovers?

**Good-fit conditions.** Failures are observable; a half-open probe is bounded and safe;
the fallback is defined; state is local or shared deliberately.

**Hard contraindications.** Reject when failures are caller-specific, when a circuit would
hide a required dependency, or when recovery probing would overload the dependency.

**Competing alternative.** Retry with backoff or bulkhead isolation. Reverse the choice
when circuit state and fallback complexity exceed failure containment benefit.

**Failure and recovery.** Shared opens, false recovery and a breaker that hides a local
resource problem are common; probe with a bounded budget and do not treat open as recovered.

**Technical owner.** [Circuit Breaker](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/dependency-isolation.md#circuit-breaker) — dependency isolation is bounded, not a full circuit-breaker library guide.

**Sources.** [src.resilience4j](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-r4j-circuit.2026-10-21: all eleven served headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Bulkhead; Retry with Exponential Backoff; Timeout; Fallback.

### Bulkhead

**Identity.** Bulkhead; family Resilience and fault tolerance; kind resilience-pattern;
priority core.

**Decision question.** Should concurrency or resources for one dependency be isolated from
the rest of the workload?

**Good-fit conditions.** One dependency can exhaust shared pools; isolation limits blast
radius; per-pool queue age/utilization are observable; rejection behavior is defined.

**Hard contraindications.** Reject when isolation would strand capacity, when the
dependency is essential to all work, or when pool sizing cannot be observed.

**Competing alternative.** Shared pool with admission control. Reverse the choice when
isolation overhead and stranded capacity exceed containment benefit.

**Failure and recovery.** Bypass, undersized partitions, a shared hidden queue and
starvation are common; detect per-pool metrics and fail the isolated class explicitly.

**Technical owner.** [Bulkhead](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/dependency-isolation.md#bulkhead) — bulkhead isolation is bounded, not a full resilience-library guide.

**Sources.** [src.resilience4j](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-r4j-bulkhead.2026-10-21: all eight served headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Circuit Breaker; Timeout; Load Shedding; Priority Queue.

### Retry with Exponential Backoff

**Identity.** Retry with Exponential Backoff; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should a failed call be retried after increasing delays?

**Good-fit conditions.** The failure is transient; the operation is idempotent or has an
effect identity; the attempt cap, backoff cap, jitter and remaining deadline are explicit;
a retry budget exists.

**Hard contraindications.** Reject when the operation is non-idempotent, when retries
amplify overload, or when the deadline cannot absorb the backoff.

**Competing alternative.** No retry or a single bounded retry. Reverse the choice when
retry latency and load exceed transient-failure benefit.

**Failure and recovery.** Retry storms, duplicate effects and synchronized clients are
common; jitter the delay, cap attempts and total delay, and stop on server pushback.

**Technical owner.** [Retry with Exponential Backoff](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/deadlines-retries.md#retry-with-exponential-backoff) — retry budget and backoff are bounded; permanent-failure classification is caller-specific.

**Sources.** [src.resilience4j](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-r4j-retry.2026-10-21: all six served headings read. The source is a public
pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Retry with Jitter; Timeout; Idempotency Key; Circuit Breaker.

### Retry with Jitter

**Identity.** Retry with Jitter; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should retry delays include randomness to avoid synchronized
retries?

**Good-fit conditions.** Many clients retry after the same failure; the operation has stable
effect identity or is naturally idempotent; sampled delay is bounded by the backoff cap and
remaining deadline.

**Hard contraindications.** Reject when retry timing must be deterministic, when jitter
would violate a deadline, when the thundering herd is caused by something else, or when a
non-idempotent effect has no stable operation identity.

**Competing alternative.** Fixed backoff or no retry. Reverse the choice when randomized
delays complicate tracing more than they reduce synchronization.

**Failure and recovery.** Jitter spreads load but does not fix a persistent dependency failure
or make a non-idempotent retry safe; bound the sampled delay and total attempts, and verify the
retry budget.

**Technical owner.** [Deadlines, cancellation and retry budgets](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/deadlines-retries.md#retry-with-jitter) — jitter and budget are bounded; PRNG quality is implementation-specific.

**Sources.** [src.resilience4j](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-r4j-retry.2026-10-21: all six served headings read. The source is a public
pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Retry with Exponential Backoff; Timeout; Load Shedding; Circuit
Breaker.

### Timeout

**Identity.** Timeout; family Resilience and fault tolerance; kind resilience-pattern;
priority core.

**Decision question.** Should each call have a bounded wait before it is treated as
failed?

**Good-fit conditions.** A local wait bound is known; cancellation is safe; late completion
is handled; the timeout is shorter than the caller's remaining budget.

**Hard contraindications.** Reject when work must complete regardless of time, when
cancellation leaves irreversible effects that cannot be reconciled, or when the timeout
is longer than the caller can wait.

**Competing alternative.** Long-running async request-reply. Reverse the choice when
synchronous waiting blocks capacity that could serve other work.

**Failure and recovery.** A timeout is an ambiguous outcome, not proof that the remote
effect stopped. Look up the durable outcome and clean up resources; do not blind-retry
non-idempotent work.

**Technical owner.** [Timeout](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/deadlines-retries.md#timeout) — timeout values and cancellation are bounded; transport timeout behavior is implementation-specific.

**Sources.** [src.resilience4j](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-r4j-timelimiter.2026-10-21: all four served headings read.
Cancellation semantics remain synthetic guidance. The source is
a public pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Deadline Propagation; Request-Reply; Circuit Breaker; Idempotency
Key.

### Deadline Propagation

**Identity.** Deadline Propagation; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should the caller’s remaining time budget be passed through
downstream calls?

**Good-fit conditions.** The full request path can carry a deadline; each hop can shorten
it; expiration is observable.

**Hard contraindications.** Reject when downstream work must outlive the caller request,
when only absolute wall-clock deadlines are available across hosts with unbounded skew,
or when no hop enforces expiry.

**Competing alternative.** Independent per-hop timeouts with a parent budget. Reverse the
choice when propagation complexity exceeds the benefit of end-to-end bounds.

**Failure and recovery.** Clock skew, lost deadlines and divergent per-hop timeouts are
common; transmit remaining duration where possible, enforce expiry at each hop and keep an
explicit cleanup path.

**Technical owner.** [Deadline Propagation](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/deadlines-retries.md#deadline-propagation) — deadline propagation and budget are bounded; clock-skew handling is platform-specific.

**Sources.** [src.sre-cascading](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-sre-cascading.2026-10-21: all forty-four served
headings read. The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Timeout; Retry with Exponential Backoff; Request-Reply; Async
Request-Reply.

### Fallback

**Identity.** Fallback; family Resilience and fault tolerance; kind resilience-pattern;
priority core.

**Decision question.** Should a failed primary path return a defined degraded result?

**Good-fit conditions.** The caller can act on a degraded result; fallback freshness,
authority and user-visible label are explicit; the fallback is cheaper and independently
safe.

**Hard contraindications.** Reject when no degraded result is meaningful, when fallback is
cached/fabricated without disclosure, or when the fallback depends on the same failed
resource.

**Competing alternative.** Fail fast with an explicit error. Reverse the choice when a
bounded degraded result is more useful than no result.

**Failure and recovery.** Fallback can mask failures and drift; a stale or partial result
must be labelled, and an explicit failure is safer than a plausible but wrong value.

**Technical owner.** [Fallback](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-admission-control-and-graceful-degradation.md#fallback) — fallback selection is bounded to the overload path, not a universal degradation strategy.

**Sources.** [src.sre-cascading](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-sre-cascading.2026-10-21: all forty-four served
headings read. The section covers graceful degradation, not fallback; the fallback
freshness/authority/independence contract is synthetic owner guidance. The source is a public
pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Graceful Degradation; Circuit Breaker; Timeout; Load Shedding.

### Graceful Degradation

**Identity.** Graceful Degradation; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should non-essential capabilities be reduced to protect essential
work under stress?

**Good-fit conditions.** Essential and optional work are distinguishable; the reduced
outcomes and user-visible state are declared; recovery and hysteresis are defined.

**Hard contraindications.** Reject when every capability is essential, when degradation
cannot be communicated, or when it silently changes correctness.

**Competing alternative.** Admission control or fail fast. Reverse the choice when partial
service creates more confusion than value.

**Failure and recovery.** Hidden degradation, sticky reduced modes and unclear recovery are
common; expose the reduced state and define how normal service resumes.

**Technical owner.** [Graceful Degradation](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-admission-control-and-graceful-degradation.md#graceful-degradation) — graceful degradation is bounded to the overload path, not a complete capacity plan.

**Sources.** [src.sre-cascading](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-sre-cascading.2026-10-21: all forty-four served
headings read. The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Fallback; Load Shedding; Throttling; Rate Limiting.

### Load Shedding

**Identity.** Load Shedding; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should the system reject some work to preserve useful throughput
under overload?

**Good-fit conditions.** Load exceeds capacity; rejection is cheaper than queueing; a
bottleneck-specific signal, fair principal policy and retry guidance are defined.

**Hard contraindications.** Reject when all work is equally critical, when rejection would
violate a hard obligation, or when capacity is actually available.

**Competing alternative.** Queueing or autoscaling. Reverse the choice when queue delay is
acceptable and capacity can expand.

**Failure and recovery.** Shedding the wrong work, unfair tenant impact and synchronized
retry storms are common; declare quotas and retry hints, and protect essential outcomes.

**Technical owner.** [Load Shedding](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-admission-control-and-graceful-degradation.md#load-shedding) — load shedding is bounded to the overload path, not a universal admission policy.

**Sources.** [src.sre-overload](../../../../edition/patterns/reading-ledger.v1.json)
read record read.sre-overload.2026-10-21: all eleven served headings read.
The source is a public pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Throttling; Rate Limiting; Graceful Degradation; Priority Queue.

### Throttling

**Identity.** Throttling; family Resilience and fault tolerance; kind resilience-pattern;
priority core.

**Decision question.** Should an out-of-quota request be rejected quickly and retried on another
backend?

**Good-fit conditions.** Per-customer limits exist; a retry path to another backend exists;
rejection is cheaper than processing.

**Hard contraindications.** Reject when all backends are overloaded or rejection costs as much as
processing.

**Competing alternative.** Do not retry when a large subset of backends is overloaded; bubble the
error to the caller.

**Failure and recovery.** A rejected request is retried immediately on a different backend with
spare resources.

**Technical owner.** [Overload admission and graceful degradation](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-admission-control-and-graceful-degradation.md#throttling) — bounded to client-side rejection and retry.

**Sources.** [src.sre-overload](../../../../edition/patterns/reading-ledger.v1.json)
read record read.sre-overload.2026-10-21: all eleven served headings read.
The source is public documentation, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Rate Limiting; Load Shedding; Retry with Jitter; Priority Queue.

### Rate Limiting

**Identity.** Rate Limiting; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should each client or tenant have an enforced request budget?

**Good-fit conditions.** Client identity is known; limits define window, burst and rejection
response; limits reflect capacity and fairness.

**Hard contraindications.** Reject when traffic is one internal caller, when limits would
block essential work, or when identity cannot be trusted.

**Competing alternative.** Global admission control or throttling. Reverse the choice when
per-client fairness is not required.

**Failure and recovery.** Bypass through many keys, burst doubling and unfair quotas are
common; bind limits to the scarce resource and declare retry guidance.

**Technical owner.** [Rate Limiting](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-admission-control-and-graceful-degradation.md#rate-limiting) — rate limiting is bounded to request admission, not a universal overload policy.

**Sources.** [src.sre-overload](../../../../edition/patterns/reading-ledger.v1.json)
read record read.sre-overload.2026-10-21: all eleven served headings read.
The source is a public pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Throttling; Load Shedding; API Gateway; Gatekeeper.

### Queue-Based Load Leveling

**Identity.** Queue-Based Load Leveling; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should work be buffered in a queue so producers and consumers can
run at different rates?

**Good-fit conditions.** Bursts exceed consumer capacity; queue durability, retention/age
bounds and idempotent consumers are owned; latency is acceptable.

**Hard contraindications.** Reject when the caller needs a synchronous result, when
backlog would violate a deadline, or when the queue becomes an unbounded hiding place.

**Competing alternative.** Direct synchronous calls or admission control. Reverse the
choice when queue delay and backlog risk exceed smoothing benefit.

**Failure and recovery.** Unbounded backlog, expired work and duplicate effects after ambiguous
acknowledgment are possible; bound age, reject early and drain.

**Technical owner.** [Queue-Based Load Leveling](../../v07-performance-scale-and-resilience/c01-queueing-littles-law-and-measurement-boundaries/queue-recovery.md#queue-based-load-leveling) — admission and drain guidance is synthetic; the cited guide covers reliability mechanics only.

**Sources.** [src.rabbitmq](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-rabbit-reliability.2026-10-21: sections "Acknowledgements and
Confirms", "Data Safety on the Publisher Side", "Data Safety on the Consumer Side". The source
supports reliability mechanics only;
admission and drain guidance is synthetic. The source is a public pattern/documentation unit,
not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Priority Queue; Load Shedding; Dead Letter Channel; Competing
Consumers.

### Priority Queue

**Identity.** Priority Queue; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should queued work be ordered by business priority rather than
arrival?

**Good-fit conditions.** Priorities are meaningful and bounded; starvation is handled; the
broker supports priority.

**Hard contraindications.** Reject when all work is equal, when priorities can starve
low-priority work indefinitely, or when producers can self-assign priority unchecked.

**Competing alternative.** FIFO with admission control. Reverse the choice when priority
inversion or starvation exceeds latency benefit.

**Failure and recovery.** Starvation, priority abuse and unauthenticated class claims are
common; define max wait, tenant isolation and a starvation policy, and verify the class at
each hop.

**Technical owner.** [Priority Queue](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/admission-resource.md#priority-queue) — admission/queue policy is bounded, not a universal priority scheme.

**Sources.** [src.rabbitmq](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-rabbit-priority.2026-10-21: all twenty-two served headings
read. The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Queue-Based Load Leveling; Load Shedding; Rate Limiting; Bulkhead.

### Hedged Requests

**Identity.** Hedged Requests; family Resilience and fault tolerance; kind
resilience-pattern; priority advanced.

**Decision question.** Should a duplicate request be issued after a latency threshold to
reduce tail latency?

**Good-fit conditions.** Replicas have independent tails; duplicate work is safe/idempotent;
the speculative budget is bounded; cancellation works; the first acceptable response wins.

**Hard contraindications.** Reject when operations are non-idempotent, when extra load
would overload the dependency, or when the threshold is below normal latency.

**Competing alternative.** Single request with retries or deadline tuning. Reverse the
choice when duplicate load and cancellation cost exceed tail benefit.

**Failure and recovery.** Hedging doubles work under shared saturation and can duplicate
effects; cap speculation, cancel losers and disable when tails are not independent.

**Technical owner.** [Hedging, replication and selective degradation](../../v07-performance-scale-and-resilience/c04-tail-latency-fan-out-and-time-budgets/deadline-hedging.md#4-hedging-replication-and-selective-degradation) — hedging is bounded to the tail-latency discussion.

**Sources.**
[src.morning-paper-tail-at-scale](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-hedged.2026-10-21: sections "The Tail at Scale". The source is a
public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Timeout; Retry with Exponential Backoff; Load Shedding;
Scatter-Gather.

### Health Endpoint Monitoring

**Identity.** Health Endpoint Monitoring; family Resilience and fault tolerance; kind
operations-pattern; priority core.

**Decision question.** Should an external monitor distinguish liveness, readiness and
startup health?

**Good-fit conditions.** Startup, readiness and liveness are separate probes; probe
semantics match the failure; restart and traffic removal are distinct; external journey
monitoring exists.

**Hard contraindications.** Reject when a liveness probe would restart a healthy process
because a shared dependency is down, or when one probe is used for every failure.

**Competing alternative.** Simple process check plus external journey monitoring. Reverse
the choice when probe complexity causes false restarts.

**Failure and recovery.** Shared-dependency failures can fail every probe and cause mass
restart/ejection; cached or missing health can keep routing to a draining instance. Define
no-response behavior, keep probes on an independent path, and bound frequency/exposure.

**Technical owner.** [Request routing and health signals](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/routing-and-health.md#health-endpoint-monitoring) — readiness/health is bounded, not a full monitoring product.

**Sources.** [src.kubernetes](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-k8s-probes.2026-10-21: all fifteen served headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Health, Readiness and Liveness Checks; Failover/Failback; Synthetic
Monitoring; Circuit Breaker.

### Failover / Failback

**Identity.** Failover / Failback; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should traffic move to a standby and later return to the original
authority?

**Good-fit conditions.** A standby exists; promotion is fenced; data reconciliation is
owned; failback is planned as a new migration, not a DNS switch.

**Hard contraindications.** Reject when no standby is maintained, when split brain cannot
be fenced, or when failback would lose writes.

**Competing alternative.** Restore from backup or stay on the promoted primary. Reverse
the choice when failback risk exceeds locality benefit.

**Failure and recovery.** Split brain and lost writes are common; quarantine the old
authority, reconcile before failback, and hold writes when fencing evidence is missing.

**Technical owner.** [Failover / Failback](../../v08-delivery-deployment-and-recovery/c07-multi-region-recovery-and-data-reconciliation/authority-failback.md#failover-failback) — failover/failback is bounded to recovery state machines.

**Sources.** [src.postgresql](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-pg-warm.2026-10-21: all twenty headings read; Failover
is a separate page. The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Leader-Follower Replication; Backup/PITR; Health Endpoint Monitoring;
Recovery Objectives.

## Chapter result and counterexample

Sixteen cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: retrying a non-idempotent write without a key is not evidence for the
retry card's contraindications.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C06](../c06-database-storage/README.md).
- Next: [V11/C08](../c08-coordination/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 16 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.
