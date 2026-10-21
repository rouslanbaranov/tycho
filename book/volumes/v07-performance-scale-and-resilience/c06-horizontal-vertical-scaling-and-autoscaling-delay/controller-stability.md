---
metadata_version: 1
id: "tycho.page.d2a71d85f3144ba395303b8432b38d37"
kind: "page"
parent_id: "tycho.chapter.1d8d87e683bc428e8dbed087106f37fd"
canonical_path: "book/volumes/v07-performance-scale-and-resilience/c06-horizontal-vertical-scaling-and-autoscaling-delay/controller-stability.md"
title: "Scale-in safety and controller evaluation"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which state and feedback assumptions make horizontal or vertical scaling safe?"
route_hints:
  questions:
    - "Which state and feedback assumptions make horizontal or vertical scaling safe?"
  prerequisites:
    - "tycho.page.2f589d07205e4ecaab2fda36e9ac1cac"
  related_ids:
    - "tycho.chapter.1d8d87e683bc428e8dbed087106f37fd"
    - "tycho.page.49d9df04c0b4488e936b02e580a62271"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "controller"
    - "stability"
evidence_scope:
  source_ids:
    - "src.k8s-hpa"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.49d9df04c0b4488e936b02e580a62271; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Scale-in safety and controller evaluation

**Owning question:** Which state and feedback assumptions make horizontal or vertical scaling safe?

This page belongs to [V07/C06 — Horizontal/vertical scaling and autoscaling delay](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.49d9df04c0b4488e936b02e580a62271:4 -->
## 4. Controller stability: scale-out and scale-in are asymmetric

Rapidly reacting to each metric spike can cause replica oscillation, wasted startups and termination of still-useful work. Too much smoothing can underreact during genuine sustained overload. Controllers commonly separate **scale-up urgency** from **scale-down conservatism**.

The [Kubernetes HPA configurable behavior](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/#configurable-scaling-behavior) documents per-direction scaling policies, stabilization windows and tolerances, with concrete API/controller version semantics. EC2 Auto Scaling also differentiates target tracking/step scaling and older simple cooldown behavior; [AWS scaling-cooldown documentation](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html) explicitly discourages applying simple cooldown-based policy as a universal modern design.

An operating design records:
1. Metric type and measurement window, handling of missing/stale data and startup/readiness exclusions.
2. Minimum/maximum resource count, quota and permission failures; zone placement and fallback.
3. Scale-up/scale-down thresholds and their evidence-based stability rationale.
4. Work draining, termination grace, request cancellations, stateful session ownership and release concurrency.
5. Whether one controller can overwrite another controller's intended resources or compete for the same backend.
6. Alerting for stuck desired-versus-ready capacity and policy misconfiguration.

**Failure example:** a slow database makes application requests wait rather than use CPU. A CPU autoscaler sees low utilization and reduces replicas, increasing pressure and the fraction of pending requests. Correct mitigation may be upstream admission limits, query/lock repair or a database budget change—not adding more application instances.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.49d9df04c0b4488e936b02e580a62271:5 -->
## 5. Vertical versus horizontal scale under invariants

Vertical scaling increases CPU, RAM or other limits for a workload, potentially avoiding per-node coordination but often requiring a restart or rescheduling; its effectiveness depends on whether the scarce resource is affected. Horizontal scaling can increase throughput for divisible work but introduces/raises load on shared data, caches, quotas and coordination. A replicated stateful writer does not gain safe independent commit capacity merely from duplication.

| Property | Vertical | Horizontal |
|---|---|---|
| Capacity mechanism | More resources per running unit | More units performing work |
| Typical dependency risk | Node/instance ceiling, restart and memory/CPU sharing | Network, distributed consistency, load balancing and multiplied external usage |
| Availability | Scaling operation may disrupt unit | Placement and draining must be configured; correlated faults remain |
| Stateful writing | Same authority unless explicitly changed | Requires partitioning/leader/single-owner model when state is shared |
| Cost | Larger instance/container requests and potential overprovision | Extra instances, connection pools, inter-node traffic and operational overhead |
| Evidence | Measure whether work actually uses added resource | Prove workload divisibility and backend capacity |

This is a *decision table*, not an assertion about a particular cloud pricing model. Check versions, quotas, application start times, data ownership and workload experiments before selecting.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.49d9df04c0b4488e936b02e580a62271:6 -->
## 6. Test plan: evaluate the complete feedback loop

An evaluation should use the same replayable offered demand for baseline and alternative and record:

- Original demand arrival timestamps versus admitted, rejected, completed and timed-out work.
- When the autoscaler **observed** a threshold, emitted a decision, requested units, and when those units became *usefully ready*.
- p95/p99 user-visible latency, queue age/size, error and rejection ratios, duplicate side effects and retry amplification.
- Backend CPU/connections, DB lock waiting, broker quota and cache hit/miss, not only app CPU.
- Resource count, total resource-seconds and costs for quiet, burst, sustained and recovery periods.
- Startup failures, maximum-replica limit, missing metrics, delayed scale-in and the ability to drain active work.

**Negative experiment:** make a downstream storage dependency slow while offered requests increase; compare unbounded upstream scaling against bounded admission, keeping correctness requirements constant. If scale-out increases backend contention and timeout rate, the hypothesis that replicas are the correct limiting resource is falsified.

**Revisit trigger:** workload variability, dependency budget changes, runtime startup regression, different read/write mix or cost envelope invalidates prior decisions. No single CPU threshold or replica number should be presented as universally optimal.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](scaling-delay.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](autoscaling-lag-and-capacity-limits.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
