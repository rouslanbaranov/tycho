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
    - "src.grpc-deadlines"
    - "src.grpc-protocol"
    - "src.microsoft-cloud-patterns"
    - "src.aws-sqs"
    - "src.rabbitmq"
    - "src.morning-paper-tail-at-scale"
    - "src.kubernetes"
    - "src.postgresql"
    - "src.aws-route53"
    - "src.azure-site-recovery"
  claim_ids: []
  status: "source-linked"
  notes: >-
    16 cards cite read units; owner links are bounded. Failover/Failback binds
    all four dimensions on 2026-10-31 to AWS Route 53 failover routing, Azure
    Site Recovery failover and failback, PostgreSQL 17 promotion, and Google SRE
    disaster recovery testing. The Priority Queue card moved to a dedicated page
    on 2026-10-31 with RabbitMQ priority, the Azure Priority Queue pattern,
    Service Bus AMQP mapping and SQS queue-type and fair-queue units.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
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

Page count is content-dependent. This chapter currently uses one landing page plus
dedicated card pages for moved entries; a later split is an editorial change, not a plan
failure. Start with the card, check its conditions and contraindications, then read the
exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Circuit Breaker

See the [dedicated Circuit Breaker card](circuit-breaker.md).

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

See the [dedicated Deadline Propagation card](deadline-propagation.md).

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

See the [dedicated Graceful Degradation card](graceful-degradation.md).

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

**Decision question.** Should request rate be limited to protect a dependency or budget?

**Good-fit conditions.** A measurable bottleneck rate is known; throttling is observable;
callers can back off; queue age and per-class latency are measured.

**Hard contraindications.** Reject when the limit is arbitrary, when clients cannot react,
or when throttling would drop mandatory work.

**Competing alternative.** Rate limiting at the edge or admission control. Reverse the
choice when per-client fairness matters more than aggregate rate.

**Failure and recovery.** When capacity is exhausted, reject requests quickly rather than
processing them; callers may retry when appropriate.

**Technical owner.** [Throttling](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-admission-control-and-graceful-degradation.md#throttling) — throttling is bounded to already-admitted work, not a universal rate-limit algorithm.

**Sources.** [src.sre-overload](../../../../edition/patterns/reading-ledger.v1.json)
read record read.sre-overload.2026-10-21: all eleven served headings read.
The record covers client-side adaptive rejection, not server-side
pacing; server-side pacing is synthetic owner guidance. The source is a public
pattern/documentation unit, not a benchmark.

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

See the [dedicated Queue-Based Load Leveling card](queue-based-load-leveling.md).

### Priority Queue

See the [dedicated Priority Queue card](priority-queue.md).

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

See the [dedicated Health Endpoint Monitoring card](health-endpoint-monitoring.md).

### Failover / Failback

**Identity.** Failover / Failback; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should traffic move to a standby and later return to the original
authority?

**Good-fit conditions.** A standby exists; promotion is fenced; data reconciliation is
owned; failback is planned as a new migration, not a DNS switch. PostgreSQL defines
failover as starting standby procedures and promotion through `pg_ctl promote` or
`pg_promote()`; Azure Site Recovery requires reprotection and a complete synchronization
before failback. **Tycho conditions:** an authority epoch, a reconciliation owner and a
verified user journey are prerequisites.

**Hard contraindications.** Reject when no standby is maintained, when split brain cannot
be fenced, or when failback would lose writes. Also reject a DNS-only return while the old
authority can still accept writes. Route 53's active-passive choice follows health status;
health does not prove data authority. **Tycho contraindication.**

**Competing alternative.** Restore from backup or stay on the promoted primary. PostgreSQL
says "To return to normal operation, a standby server must be recreated, either on the
former primary system when it comes up, or on a third, possibly new, system"; Azure Site
Recovery reprotects the failed-over region before returning traffic. **Tycho choice rule:**
stay on the promoted region and rebuild the old region as a standby when fencing or
reconciliation evidence is incomplete; reverse only when the old region can be proven
consistent.

**Failure and recovery.** Split brain and lost writes are common; quarantine the old
authority, reconcile before failback, and hold writes when fencing evidence is missing.
PostgreSQL warns that two primaries lead to "confusion and ultimately data loss"; Azure
Site Recovery warns "If the source VM is powered on then it fails and thus fails the
failback operation." Route 53 health checks route to a healthy record, not to a reconciled
authority. Google SRE says disaster recovery tools compute a "checkpoint state that is
equivalent to cleanly stopping the service" and that broken constraints make confidence
harder. **Tycho runbook:** fence, reconcile, verify a user journey and record the achieved
RPO/RTO before declaring recovery.

**Technical owner.** [Failover / Failback](../../v08-delivery-deployment-and-recovery/c07-multi-region-recovery-and-data-reconciliation/authority-failback.md#failover-failback) — failover/failback is bounded to recovery state machines.

**Sources.** Five public units inspected on 2026-10-31: AWS Route 53 *Active-active and
active-passive failover*; Azure Site Recovery *Run a failover from on-premises to Azure*
and *Tutorial: Fail back Azure VM to the primary region*; PostgreSQL 17 *26.3. Failover*;
and Google SRE *Testing for Reliability*, section *Testing Disaster*. Retained:
`read.batch3-pg-warm.2026-10-21`; new records:
`read.aws-route53-failover.2026-10-31`, `read.azure-asr-failover.2026-10-31`,
`read.azure-asr-failback.2026-10-31`, `read.pg-failover.2026-10-31` and
`read.sre-testing-disaster.2026-10-31`. Source ids: `src.postgresql` and `src.sre` are
registered; `src.aws-route53` and `src.azure-site-recovery` are proposed pending
registration. Canonical text SHA-256 `cbeed64d...`, `5b1475e4...`, `dd092294...`,
`bd1cf093...` and `425eb0ec...`. Exact URLs, sections and revisions are in the owner
section and lane note. None is a benchmark or production observation; no failover,
failback or DNS change was run.

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
