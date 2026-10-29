---
metadata_version: 1
id: "tycho.page.49d9df04c0b4488e936b02e580a62271"
kind: "page"
parent_id: "tycho.chapter.1d8d87e683bc428e8dbed087106f37fd"
canonical_path: "book/volumes/v07-performance-scale-and-resilience/c06-horizontal-vertical-scaling-and-autoscaling-delay/autoscaling-lag-and-capacity-limits.md"
title: "Horizontal and vertical scaling: autoscaling lag, resource ceilings and stability"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Integrated question, original scenario and transfer limits for Horizontal/vertical scaling and autoscaling delay. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which headroom, statefulness and failure assumptions shape capacity?"
  prerequisites: []
  related_ids:
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.eb130a7f820544a2ba0e0883c0ce587b"
    - "tycho.page.dc2470904e004a4aa733abcdb25517ed"
    - "tycho.page.f784d6ef723c4c0e8836ff9085bf7dcc"
    - "tycho.landing.b08f16ced4a142a785c37b43eb340260"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.page.ea94649bfd8c4be183f9114618d7ccaa"
    - "tycho.page.2536d18422944e27abe4ea8549beb9ab"
    - "tycho.page.2f589d07205e4ecaab2fda36e9ac1cac"
    - "tycho.page.d2a71d85f3144ba395303b8432b38d37"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Horizontal"
    - "and"
    - "vertical"
    - "scaling"
    - "autoscaling"
    - "lag"
    - "resource"
    - "ceilings"
    - "stability"
evidence_scope:
  source_ids:
    - "src.k8s-hpa"
    - "src.kubernetes"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-29"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.49d9df04c0b4488e936b02e580a62271:-1 -->

# Horizontal and vertical scaling: autoscaling lag, resource ceilings and stability

> **Original System Design chapter, V07/C06.** Public specifications reviewed 2026-10-19; synthetic
> examples only. No autoscaler, Kubernetes cluster, cloud instance, load generator, production
> telemetry or independent review was used to validate the proposed designs.
>
> The content_review field retains the decomposition-era draft state; no independent
> acceptance is asserted.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Horizontal Scaling](../../v11-pattern-atlas/c09-scalability/README.md#horizontal-scaling) — decision conditions and contraindications.
> [Vertical Scaling](../../v11-pattern-atlas/c09-scalability/vertical-scaling.md#vertical-scaling) — decision conditions and contraindications.
> [Autoscaling](../../v11-pattern-atlas/c09-scalability/README.md#autoscaling) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.49d9df04c0b4488e936b02e580a62271:0 -->
## Purpose and mission

Autoscaling is a **feedback-control mechanism**, not a promise of immediate extra capacity. A signal must be collected, interpreted, acted on, and followed by resource provisioning, application readiness and dependent-service capacity. During that delay, new demand still reaches the old infrastructure. Horizontal scaling multiplies processing replicas; vertical scaling changes resources available to existing replicas. Neither can increase throughput past a serial or externally fixed bottleneck.

This chapter answers when automatic capacity changes can help, how warm-up and stabilization affect behavior, what fails during bursts, and how to test the scaling policy *as an end-to-end system*. [Queueing](../c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md) owns throughput/occupancy mean identities, [tail latency](../c04-tail-latency-fan-out-and-time-budgets/tail-latency-fanout-and-deadline-budgets.md) owns critical-path budgets, and [connection-pool budgets](../../v03-execution-concurrency-and-flow-control/c05-thread-connection-and-buffer-pools/connection-pools-hikaricp-pgbouncer.md) owns backend resource multiplication.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.49d9df04c0b4488e936b02e580a62271:8 -->
## Engineering walkthrough — A burst ends before new replicas become useful

**Original hypothetical control loop:** arrival intensity doubles for 40 seconds. Metrics take 15 seconds to capture and be sampled; the controller decision takes 10 more; node scheduling takes 20; application startup and data warm-up need another 25. The first additional healthy capacity would therefore become useful around `15+10+20+25=70` seconds after the triggering change—**after the burst ends**. These invented delays are not documented Kubernetes defaults or observed service timings.

| Stage | Clock from onset (synthetic) | Required observation |
|---|---:|---|
| Measurement + controller | 0–25 s | Distinguish offered load from already-shed load |
| Scheduling | 25–45 s | Placement quota, spare nodes, topology constraints |
| Readiness + warm-up | 45–70 s | App and downstream actually ready; cache/pool warming counted |
| Scale-in | After demand falls and stability window passes | Drain long-lived work and prevent retry oscillation |

**Negative case:** all extra replicas connect to the same database lock on a single hot reservation key. Adding replicas can raise conflict retries and make correct throughput worse while increasing instance cost. A reactive autoscaler cannot replace bounded admission, pre-warming or removal of serialized bottlenecks.

**Proposed evaluation, not performed:** inject a 40-second arrival spike and a separate 10-minute step load, record time from first offered demand to *correct* extra capacity, retries, warm-up, cost and scale-in loss. Compare reserved headroom, pre-scale schedule, dynamic scaling and a simpler DB optimization. Choose according to an actual workload timescale rather than interpreting the number of configured replicas as achieved availability.

<!-- /tycho-question-source -->

## Bounded pattern ownership notes

### Horizontal Scaling

Horizontal scaling multiplies processing replicas; vertical scaling changes resources available to
existing replicas. Adding replicas is not useful unless the work can be partitioned and the new
replica becomes ready inside the demand window.

Neither can increase throughput past a serial or externally fixed bottleneck. A new replica may
start cold, contend on a shared dependency or amplify connection churn; test scale-out under a burst
and bound the work each replica can claim. Instances must serve any request without local session
state, or the shared state must be externalized; otherwise adding replicas only multiplies the
bottleneck. Keep a per-replica concurrency limit and a readiness gate so traffic does not reach a
process before its caches and pools are usable.

Vertical scaling or a queue/backpressure policy may be preferable when the bottleneck is per-replica
resource or the workload cannot partition. Horizontal scaling is a fit when the work is
partitionable and the coordination cost is lower than the capacity gain.

### Vertical Scaling

Vertical scaling changes resources available to existing replicas. It can raise per-replica
throughput without adding partition or routing complexity, but it changes the failure domain: one
larger node is still one node.

Neither horizontal nor vertical scaling can increase throughput past a serial or externally fixed
bottleneck. A resize usually needs a restart or migration, so the old capacity is unavailable during
the change; bound the maintenance window and keep a fallback. The provider must allow a larger size,
and cost must not grow superlinearly with that size. Measure the resource that actually saturates,
not only CPU, and verify that the operating system, runtime and dependency can use the larger
allocation.

Horizontal scaling may be preferable when the workload partitions and a single node is an
unacceptable failure domain. The Kubernetes autoscaling page frames the same choice as either
changing the replica count (horizontal scaling) or adjusting resources in place (vertical
scaling). It states:

> When you scale a workload, you can either increase or decrease the number of replicas managed by
> the workload, or adjust the resources available to the replicas in-place. The first approach is
> referred to as horizontal scaling, while the second is referred to as vertical scaling.

The page defines the two approaches but does not state when horizontal scaling is preferable;
partition, failure-domain and restart conditions remain Tycho synthesis. Vertical scaling is a fit
when the workload is hard to partition and the resize can be staged safely.

### Autoscaling

Autoscaling is a **feedback-control mechanism**, not a promise of immediate extra capacity. A signal
must be collected, interpreted, acted on, and followed by resource provisioning, application
readiness and dependent-service capacity.

During that delay, new demand still reaches the old infrastructure. Pre-provision headroom for the
measured lag, add queueing or admission control for the gap and alert when the controller cannot
converge. A metric that tenants or operators can influence adversarially must be paired with an
independent guardrail; otherwise the control loop can be gamed. A scale-in needs a stabilization
window and a check that in-flight work has drained.

Scheduled capacity or static headroom may be simpler when demand is predictable or the scale-out
path is slower than the burst. Autoscaling is a fit when demand varies enough to justify the control
loop and the dependency chain can absorb the change under real load.

## Integrated decision and reading route

Compare demand timescale with detection, provisioning, readiness and warm-up delay before relying on autoscaling.

Capacity that arrives after a short burst cannot prevent its initial overload; reserved headroom or admission control may still be needed.

The detailed pages separate the mechanisms that make this decision conditional:

- [Demand signals and scale-out delay](scaling-delay.md) — When does new capacity become useful relative to the demand timescale?
- [Scale-in safety and controller evaluation](controller-stability.md) — Which state and feedback assumptions make horizontal or vertical scaling safe?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
