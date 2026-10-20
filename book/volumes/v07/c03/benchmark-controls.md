---
metadata_version: 1
id: "tycho.page.180a25e8e7504ef4aa52257f76dbd1a8"
kind: "page"
parent_id: "tycho.chapter.a55ddaaa45a647e29b51d6b5c0adbe05"
canonical_path: "book/volumes/v07/c03/benchmark-controls.md"
title: "Confounders, fault injection and acceptance"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which invariant and distribution must remain comparable across benchmark variants?"
route_hints:
  questions:
    - "Which invariant and distribution must remain comparable across benchmark variants?"
  prerequisites:
    - "tycho.page.bfa3a283746b42998825234aca63b101"
  related_ids:
    - "tycho.chapter.a55ddaaa45a647e29b51d6b5c0adbe05"
    - "tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "benchmark"
    - "controls"
evidence_scope:
  source_ids:
    - "src.sre-overload"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Confounders, fault injection and acceptance

**Owning question:** Which invariant and distribution must remain comparable across benchmark variants?

This page belongs to [V07/C03 — Load-test methods and benchmark validity](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e:4 -->
## 4. Control confounders without erasing real behavior

A warmed cache or JIT can make a benchmark unrepresentative of cold start; a perpetually cold cache can likewise exaggerate steady-state cost. Record both states when relevant. If the experiment aims to compare architecture changes, changing request distribution or backend quotas at the same time confounds the conclusion.

Candidate controls:
- Pin artifact/container, dependencies, data snapshot, tool version and test script.
- Declare warmed, cold and recovery phases rather than discarding inconvenient transients.
- Use equal offered demand traces, or disclose which differences are intentional.
- Detect background contention and noisy-neighbor effects; repeat with randomized trial order.
- Record node/container throttling, GC, connection wait, and load-generator saturation.
- Collect per-operation/tenant successes and side effects, not just aggregate bandwidth.
- Preserve full test and measurement configuration in version control where legally appropriate.
- Treat local test passes as **bounded results** rather than proof of global production behavior.

### Fictional comparative trace

Consider two invented runs under 200 scheduled operations/s for 60 s: 12,000 operations intended. Run A transmits all but returns many explicit 503 responses. Run B reports excellent p99 for 8,000 completed requests but has 4,000 **unsent** scheduled iterations due to generator exhaustion. The runs **cannot** be ranked based on the response histogram alone. Run B's apparent improvement might simply be missing demand. The numbers are invented to illustrate denominator errors; no generator executed them.

A valid repair is to increase generator capacity, capture actual arrivals, repeat under equal demand and compare logical outcomes and resource cost. If generator capacity cannot be improved, report the limitation rather than silently using an unsupported ranking.


### Worked invalid benchmark: the load generator is the limiting system

**Original hypothetical experiment:** Team A claims a service sustains 1,000 requests/s because it scheduled 1,000 new iterations per second in an open-model generator. The generator actually starts 720/s while reporting 280/s `dropped_iterations`, and the service completes 600/s with another 120/s timing out. This is invented arithmetic, not an observed performance claim.

| Denominator | Synthetic rate | Valid meaning |
|---|---:|---|
| Scheduled iterations | 1,000/s | Intended offered generator load |
| Started attempts | 720/s | Potential actual arrivals; verify at server ingress |
| Generator-dropped | 280/s | Not presented to application; do not label HTTP rejection |
| Correct completed | 600/s | Observed correct attempt completions under these assumptions |
| Timed-out attempts | 120/s | Outcome ambiguous until durable effect identity is reconciled |

A healthy generator must show it can **deliver** the load; even then an application might intentionally reject excess work. [k6 dropped iterations](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/dropped-iterations/) documents that VU scarcity and slowing responses can cause scheduler drops. [Open and closed models](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/) explains why client feedback can suppress offered arrivals as a service slows. Neither document proves where this fictional bottleneck occurred.

**Proposed discriminating test, not run:** run a generator-only calibration against a controlled endpoint, independently count ingress arrivals and correlate logical-operation IDs with durable results. Then apply equal arrival distribution, payload/key skew, warm-up, endpoint configuration, pool limits, retries and cancellation to candidate systems. Record test duration, environment, failures and distribution confidence, not only p99 and a headline RPS.

The correct result for this invented trace is **INSUFFICIENT_EVIDENCE to claim 1,000 RPS capacity**. The same test may still demonstrate that the observed setup performed 600 correct completions/s in its stated window, but cannot generalize without a saturation and recovery envelope. Workload definitions live in [V01/C02](../../v01/c02/workload-demand-and-arrival-models.md); this chapter owns the validity of the experiment.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e:5 -->
## 5. Fault injection must preserve the claim being tested

Different failure classes require distinct tests:

| Fault | What to observe | What a passing run cannot establish |
|---|---|---|
| One slow downstream response | Parent deadlines, per-hop waits, cancellation and retry amplification | All failure classes are tolerated |
| Partial dependency outage | Queue bounds, explicit errors, unaffected user journeys | Correct durable state after all recovery paths |
| Generator overload | Scheduled versus sent arrivals and generator metrics | That service throughput was limited at all |
| Database lock contention | Per-key skew, transaction success, deadlock outcomes | That sharding would cure the hot key |
| Replica restart | Readiness, drain, in-flight effects, recovery backlog | Region disaster recoverability |
| Search-index lag | Query correctness/freshness and controlled stale responses | Total integrity of authoritative records |

A failure experiment must define a safe abort condition. Never run disruptive load against uncontrolled real systems or collect restricted production content for this independent reference book.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e:6 -->
## 6. Decide from distributions, invariants and cost together

An architecture should be compared at a **comparable resource budget** as well as at a comparable offered workload. If one candidate deploys twice as many instances, lower latency may be a capacity purchase rather than an efficiency gain; this distinction may still be acceptable if cost constraints permit it.

For candidate A/B, report:
- correctness and authorized-user outcome distribution;
- offered, transmitted, admitted, completed, rejected and unsent rates;
- median, p95/p99 and timeout outcomes by operation class;
- CPU, heap, network, DB concurrency, queue age and error budget;
- minimum/peak replicas, startup delay and total resource-seconds;
- trial variability, parameter sensitivity and whether the selected option wins under alternate representative demand.

A result can be **inconclusive** because variance is high, samples are insufficient, the generator saturated, or the system differs too much from the target environment. That is valuable evidence and should lead to a better scoped experiment, not a stronger conclusion.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](arrival-design.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](load-testing-and-benchmark-validity.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
