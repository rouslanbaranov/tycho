---
metadata_version: 1
id: "tycho.volume.f7679623ca274bff8a00389d409d68c6"
kind: "volume"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/volumes/v07-performance-scale-and-resilience/README.md"
title: "V07 — Performance, scale and resilience under load"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "A capacity envelope joining Little's Law, offered load, contention, tails, overload controls, autoscaling lag and cost with falsification."
route_hints:
  questions:
    - "A capacity envelope joining Little's Law, offered load, contention, tails, overload controls, autoscaling lag and cost with falsification."
  prerequisites:
    - "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
    - "tycho.chapter.3d34f0b431814c9fa879a355029af2a9"
    - "tycho.chapter.ee2cd95003ab4018a9d49e2ff0b6b2f4"
    - "tycho.chapter.e436af815dc442f694deb55966077d9e"
    - "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
  related_ids:
    - "tycho.chapter.e365b78505784c20a4f3d72fe7904d9b"
    - "tycho.chapter.4cbc9e1582404965b696a63b79a66e93"
    - "tycho.chapter.a55ddaaa45a647e29b51d6b5c0adbe05"
    - "tycho.chapter.2ad010c2b29c4390b83bbdadeb346289"
    - "tycho.chapter.0718556e0eb14d499adbbe67073327df"
    - "tycho.chapter.1d8d87e683bc428e8dbed087106f37fd"
    - "tycho.chapter.b7924b3db65949df952fbb5ca706236c"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.aws-backoff"
    - "src.k8s-hpa"
    - "src.little-law"
    - "src.sre-cascading"
    - "src.sre-overload"
    - "src.tail-at-scale"
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

# V07 — Performance, scale and resilience under load

## Purpose and mission

Connect load and failure conditions to observed limits, avoiding universal thresholds.

The outcome of this volume is: A capacity envelope joining Little's Law, offered load, contention, tails, overload controls, autoscaling lag and cost with falsification.

## A worked cross-chapter synthesis

A fictional service stays within its mean response target until a short burst coincides with a slow dependency. Queues grow, retries multiply demand, and extra replicas become ready after the burst. A stable average computed over the entire run conceals the failed user journeys.

Build a capacity envelope from a declared arrival process and measured boundary. Relate occupancy and rates carefully, then inspect contention, arrival-model bias, critical paths, overload and scaling delay. Compare alternatives using correct outcomes over total cost, including peak and degraded operation.

## Questions and chapters

| Chapter | Owning question |
|---|---|
| [V07/C01 — Queueing, Little's Law and measurement boundaries](c01-queueing-littles-law-and-measurement-boundaries/README.md) | What do arrival, throughput, mean response and in-flight counts imply? |
| [V07/C02 — Contention, saturation and scaling laws](c02-contention-saturation-and-scaling-laws/README.md) | When does coordination dominate additional capacity? |
| [V07/C03 — Load-test methods and benchmark validity](c03-load-test-methods-and-benchmark-validity/README.md) | How do open/closed arrivals, warmup and coordinated omission bias conclusions? |
| [V07/C04 — Tail latency, fan-out and time budgets](c04-tail-latency-fan-out-and-time-budgets/README.md) | Why can p99 degrade despite adequate mean capacity? |
| [V07/C05 — Overload protection and graceful degradation](c05-overload-protection-and-graceful-degradation/README.md) | How should admissions, queues, retries and shedding be bounded? |
| [V07/C06 — Horizontal/vertical scaling and autoscaling delay](c06-horizontal-vertical-scaling-and-autoscaling-delay/README.md) | Which headroom, statefulness and failure assumptions shape capacity? |
| [V07/C07 — Capacity planning and cost/performance trade-offs](c07-capacity-planning-and-cost-performance-trade-offs/README.md) | What experiments can confirm or falsify a scaling hypothesis? |

## Choosing a reading route

For a first reading, follow the chapter order. For diagnosis, connect the observed outcome to its authority and failure boundary using: [V07/C01](c01-queueing-littles-law-and-measurement-boundaries/README.md), [V07/C03](c03-load-test-methods-and-benchmark-validity/README.md), [V07/C04](c04-tail-latency-fan-out-and-time-budgets/README.md), [V07/C05](c05-overload-protection-and-graceful-degradation/README.md), [V07/C06](c06-horizontal-vertical-scaling-and-autoscaling-delay/README.md). Return to the exact page-local source ledger before making a version-specific claim.

Prerequisite context: V01/C02–C04; V03/C05; V04/C04.

Read [V01/C02](../v01-requirements-and-architecture/c02-workload-and-demand-models/README.md), [V01/C03](../v01-requirements-and-architecture/c03-quality-attributes-and-trade-offs/README.md), [V01/C04](../v01-requirements-and-architecture/c04-evidence-hypotheses-and-architecture-experiments/README.md), [V03/C05](../v03-execution-concurrency-and-flow-control/c05-thread-connection-and-buffer-pools/README.md), [V04/C04](../v04-distributed-coordination-and-events/c04-retries-idempotency-and-duplicate-effects/README.md) for the named entry assumptions.

### Reasoning boundaries

This original conceptual map separates competing inputs rather than promising a universal solution.

~~~mermaid
flowchart TD
    Q["V07/C01 — Queueing, Little's Law and measurement boundaries"] --> M["V07/C03 — Load-test methods and benchmark validity"]
    Q --> E["Evidence and unknown inputs"]
    M --> D{"Meets the declared constraints?"}
    E --> D
    D -->|Supported| R["V07/C06 — Horizontal/vertical scaling and autoscaling delay"]
    D -->|Unresolved| U["Measure, revise or retain the baseline"]
~~~

Text alternative: establish queueing, little's law and measurement boundaries, compare load-test methods and benchmark validity with the available evidence, and either carry a supported result forward or return to unresolved inputs. The figure describes a reasoning route, not observed runtime behavior.

## Counterexample and handoff

Little's Law does not choose a pool size or predict p99. A closed-loop generator can hide external demand, and autoscaling cannot erase elapsed startup delay. Pass the admitted workload, failure headroom and recovery criteria into deployment design rather than carrying a single optimistic throughput number.

## Navigation and source boundaries

| Route | Destination |
|---|---|
| Parent | [Book contents](../../README.md) |
| Previous volume | [V06](../v06-caching-indexing-and-retrieval/README.md) |
| Next volume | [V08](../v08-delivery-deployment-and-recovery/README.md) |
| Historical applications | [Casebook and synthetic playbooks](../../cases/README.md) |

## Evidence and known limits

The scenario is original synthetic reasoning. The chapters contain the accepted manuscript and its published evidence; no synthetic number or historical result is a measured prediction for another system. This new synthesis is editorially self-checked, not independently certified. Source-access restrictions, unexecuted technology experiments and original case denominators remain explicit in their owning pages. Product-specific adoption still requires compatible versions and the target workload.
