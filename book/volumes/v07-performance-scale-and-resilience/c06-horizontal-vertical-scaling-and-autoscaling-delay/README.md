---
metadata_version: 1
id: "tycho.chapter.1d8d87e683bc428e8dbed087106f37fd"
kind: "chapter"
parent_id: "tycho.volume.f7679623ca274bff8a00389d409d68c6"
canonical_path: "book/volumes/v07-performance-scale-and-resilience/c06-horizontal-vertical-scaling-and-autoscaling-delay/README.md"
title: "V07/C06 — Horizontal/vertical scaling and autoscaling delay"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which headroom, statefulness and failure assumptions shape capacity? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Which headroom, statefulness and failure assumptions shape capacity?"
  prerequisites:
    - "tycho.chapter.0718556e0eb14d499adbbe67073327df"
  related_ids:
    - "tycho.page.49d9df04c0b4488e936b02e580a62271"
    - "tycho.page.2f589d07205e4ecaab2fda36e9ac1cac"
    - "tycho.page.d2a71d85f3144ba395303b8432b38d37"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.k8s-hpa"
  claim_ids: []
  status: "source-linked"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# V07/C06 — Horizontal/vertical scaling and autoscaling delay

## Purpose and mission

Which headroom, statefulness and failure assumptions shape capacity? This chapter owns that question within performance, scale and resilience under load. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Compare demand timescale with detection, provisioning, readiness and warm-up delay before relying on autoscaling.

Capacity that arrives after a short burst cannot prevent its initial overload; reserved headroom or admission control may still be needed. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](autoscaling-lag-and-capacity-limits.md) | Which headroom, statefulness and failure assumptions shape capacity? |
| [Demand signals and scale-out delay](scaling-delay.md) | When does new capacity become useful relative to the demand timescale? |
| [Scale-in safety and controller evaluation](controller-stability.md) | Which state and feedback assumptions make horizontal or vertical scaling safe? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V07 — Performance, scale and resilience under load](../README.md) |
| Previous | [V07/C05 — Overload protection and graceful degradation](../c05-overload-protection-and-graceful-degradation/README.md) |
| Next | [V07/C07 — Capacity planning and cost/performance trade-offs](../c07-capacity-planning-and-cost-performance-trade-offs/README.md) |
| Prerequisite | [V07/C05 — Overload protection and graceful degradation](../c05-overload-protection-and-graceful-degradation/README.md) |
| Source reading | [Page-local evidence and versions](autoscaling-lag-and-capacity-limits.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.49d9df04c0b4488e936b02e580a62271:7 -->
## 7. Public evidence and review limits

| Source reviewed | Narrow support | Limit |
|---|---|---|
| [Kubernetes Horizontal Pod Autoscaling docs](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) | Horizontal controller concepts, target metrics, scaling behavior and limitations | Actual policy/version settings must be checked in deployed platform |
| [AWS default instance warm-up](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-default-instance-warmup.html) | Time-to-metric readiness and why warm-up affects control | Not a startup measurement for a fictional workload |
| [AWS scaling cooldowns](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html) | Policy-family distinctions and anti-flapping considerations | Not a claim that fixed cooldowns should be universally applied |
| [Tycho queueing study](../c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md) and [capacity experiments](../../../performance/workload-profiles-and-capacity-experiments.md) | Mean workload boundary and proposed testing discipline | No empirical scaling result |

**Unverified:** everything numeric in the burst example, all diagrams, practical thresholds, cost and failure outcomes are synthetic. The chapter was not executed as a cloud/autoscaler experiment, does not prove provider interoperability, and has not been independently reviewed. It must be placed under the final V07/C06 chapter structure after content-completeness acceptance.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.49d9df04c0b4488e936b02e580a62271:9 -->
## Navigation

- Current landing: [Performance](../../../performance/README.md), future owner V07/C06 in [proposed TOC](../../../PROPOSED-STRUCTURE.md).
- Core limits: [Queueing](../c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md), [Tail latency](../c04-tail-latency-fan-out-and-time-budgets/tail-latency-fanout-and-deadline-budgets.md), [Workload experiments](../../../performance/workload-profiles-and-capacity-experiments.md).
- Dependency and deployment: [Connection pools](../../v03-execution-concurrency-and-flow-control/c05-thread-connection-and-buffer-pools/connection-pools-hikaricp-pgbouncer.md), [Deployment topology](../../v08-delivery-deployment-and-recovery/c03-vms-containers-orchestration-and-serverless/runtime-placement-and-control-plane.md), [Multi-region recovery](../../../deployment/multi-region-disaster-recovery-contracts.md).
<!-- /tycho-question-source -->
