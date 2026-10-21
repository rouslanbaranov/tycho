---
metadata_version: 1
id: "tycho.page.62ad1ae9e0d243d69b08be0ff32930a1"
kind: "page"
parent_id: "tycho.chapter.0718556e0eb14d499adbbe67073327df"
canonical_path: "book/volumes/v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-recovery.md"
title: "Recovery hysteresis and overload experiments"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What prevents a recovering dependency from being overwhelmed immediately?"
route_hints:
  questions:
    - "What prevents a recovering dependency from being overwhelmed immediately?"
  prerequisites:
    - "tycho.page.80ab784dafed47a7baf31722fce5eabc"
  related_ids:
    - "tycho.chapter.0718556e0eb14d499adbbe67073327df"
    - "tycho.page.c5d20ae7ef6445e5b23dd5fbac625060"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "overload"
    - "recovery"
evidence_scope:
  source_ids:
    - "src.aws-backoff"
    - "src.sre-overload"
    - "src.sre-cascading"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.c5d20ae7ef6445e5b23dd5fbac625060; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---
# Recovery hysteresis and overload experiments

**Owning question:** What prevents a recovering dependency from being overwhelmed immediately?

This page belongs to [V07/C05 — Overload protection and graceful degradation](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.c5d20ae7ef6445e5b23dd5fbac625060:6 -->
## 6. Recovery and hysteresis must be deliberate

When load drops or a dependency becomes healthy, prematurely reopening traffic can cause a second collapse. Circuit-breaker recovery may use bounded probes; admission thresholds may need stability windows and progressive recovery. However, an excessive cooldown can strand healthy capacity. Review the actual demand and dependency recovery curve, not a generic constant.

Failure and restoration conditions should include:
- dependency/probe success and bounded error-rate sample;
- backlog, queue age, retries and in-flight state, not only CPU;
- completeness of accepted operations and reconciliation of unknown outcomes;
- fair re-admission and a controlled ramp to prevent a thundering herd;
- independent confirmation of user-facing core journey correctness.

A successful health endpoint check is not proof that old accepted writes were processed or that a stale derived read is safe.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.c5d20ae7ef6445e5b23dd5fbac625060:7 -->
## 7. Experiments, acceptance criteria and costs

A valid test matrix compares baseline and treatment under **the same attempted arrivals, key skew, logical outcomes and total resource limits**:

| Situation | Expected observation | Stop / failure condition |
|---|---|---|
| Normal steady traffic | Low rejection and bounded queue within defined target | Priority classes unexpectedly starved |
| Short burst beyond warm capacity | Some explicit shedding; critical work stays bounded | Unbounded queue or hidden timeout population |
| Dependency slowdown | Healthy unrelated class continues within agreed limits | Shared pool exhausted despite bulkhead |
| Repeated ambiguous command timeout | Safe identity reconciliation, no duplicate effect | Blind retries create extra committed operations |
| Recovery after fault removal | Gradual return without queue avalanche | Probe/retry surge collapses dependency again |
| Unauthorized or high-cost user input | Deterministic permission and quota enforcement | Overload bypass leaks data or monopolizes resources |

Record the **cost of protective capacity**: extra reserved pools, higher rejection ratios, additional deferred-work storage, alerting/operations, idle headroom and possibly less total peak throughput. A graceful degradation mechanism is a justified architecture choice only when the user contract makes its reduced outcome acceptable.

Additional observations for the same matrix:

- **Impulse versus gradual load.** A gradual ramp can warm caches, connection pools and
  runtime profiles; a step load of the same final rate may fail earlier. Test both, and do
  not accept a gradual-only result as evidence for a launch spike.
- **Exit from degraded mode.** After the fault is removed, can the service leave its
  degraded mode without a manual restart? If not, record the required action, its
  authorization and the risk of leaving protection active too long.
- **Rejection storm.** If rejected clients retry immediately, does the rejection rate grow
  even though the underlying resource is unchanged? This distinguishes a capacity problem
  from a retry-policy problem.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](dependency-isolation.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](overload-admission-control-and-graceful-degradation.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
