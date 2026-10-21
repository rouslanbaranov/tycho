---
metadata_version: 1
id: "tycho.page.c5d20ae7ef6445e5b23dd5fbac625060"
kind: "page"
parent_id: "tycho.chapter.0718556e0eb14d499adbbe67073327df"
canonical_path: "book/volumes/v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-admission-control-and-graceful-degradation.md"
title: "Overload protection, admission control and graceful degradation"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Integrated question, original scenario and transfer limits for Overload protection and graceful degradation. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How should admissions, queues, retries and shedding be bounded?"
  prerequisites: []
  related_ids:
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.49d9df04c0b4488e936b02e580a62271"
    - "tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e"
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
    - "tycho.page.f784d6ef723c4c0e8836ff9085bf7dcc"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.b08f16ced4a142a785c37b43eb340260"
    - "tycho.page.fdb4ef7f69154f8c8c433591f71494f9"
    - "tycho.page.eb130a7f820544a2ba0e0883c0ce587b"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.d9abd43bb7394c04a6bf77d4014f870d"
    - "tycho.page.80ab784dafed47a7baf31722fce5eabc"
    - "tycho.page.62ad1ae9e0d243d69b08be0ff32930a1"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Overload"
    - "protection"
    - "admission"
    - "control"
    - "and"
    - "graceful"
    - "degradation"
evidence_scope:
  source_ids:
    - "src.aws-backoff"
    - "src.sre-overload"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.c5d20ae7ef6445e5b23dd5fbac625060:-1 -->

# Overload protection, admission control and graceful degradation

> **Tycho book chapter draft V07/C05 (2026-10-19).** Original examples and diagrams, with scope-bound published SRE and Builders' Library guidance. No deployed protection, incident, load generator, performance comparison or independent expert review has been executed.
>
> The content_review field retains the decomposition-era draft state; no independent
> acceptance is asserted.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Fallback](../../v11-pattern-atlas/c07-resilience/README.md#fallback) — decision conditions and contraindications.
> [Graceful Degradation](../../v11-pattern-atlas/c07-resilience/README.md#graceful-degradation) — decision conditions and contraindications.
> [Load Shedding](../../v11-pattern-atlas/c07-resilience/README.md#load-shedding) — decision conditions and contraindications.
> [Throttling](../../v11-pattern-atlas/c07-resilience/README.md#throttling) — decision conditions and contraindications.
> [Rate Limiting](../../v11-pattern-atlas/c07-resilience/README.md#rate-limiting) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.c5d20ae7ef6445e5b23dd5fbac625060:0 -->
## Purpose and mission

When offered work exceeds a scarce resource's sustainable capacity, unlimited waiting is not reliability: it converts excess arrivals into growing queues, missed deadlines, retries and possible cascading failure. A sound architecture decides **which work to accept, reject, defer, cancel or degrade**, and makes those decisions visible to callers while protecting correctness invariants.

This chapter owns *overload policies and failure containment*, not the mathematical foundations of [Little's Law](../c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md), the [autoscaling control loop](../c06-horizontal-vertical-scaling-and-autoscaling-delay/autoscaling-lag-and-capacity-limits.md) or [load-test validity](../c03-load-test-methods-and-benchmark-validity/load-testing-and-benchmark-validity.md). Their evidence is necessary to size a control but does not itself supply a universal threshold.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.c5d20ae7ef6445e5b23dd5fbac625060:10 -->
## Engineering walkthrough — Optional dependency failure creates core-work starvation

**Original fictional traffic:** checkout needs an authoritative booking transaction and optionally calls a recommendation service. The optional service stalls for one second. A single shared outbound pool of twenty slots is consumed by recommendations, delaying bookings even though the database remains healthy. An API-edge quota alone does not protect the specific scarce pool.

| Phase | Controller's legitimate action | Unsafe behavior |
|---|---|---|
| Normal | Reserve core dependency budget; optional calls use a separate small bulkhead | One pool handles all classes without priority or cap |
| Optional service timeout | Stop admitting optional work, return core success with explicit absent recommendations | Retry stalled optional call before completing critical booking |
| Overload persists | Circuit may remain open with bounded retry/backoff and fair tenant budgets | Every failed request immediately probes again, amplifying load |
| Dependency recovers | Permit bounded trial probes; increase flow only after stable correct responses | Flood the recovering service as soon as first probe succeeds |

A circuit breaker monitors a declared *failure signal*, while admission protects a chosen scarce resource. Neither restores an ambiguous external effect after commit. Rejection codes and retry hints must prevent all clients from retrying in lockstep. The same mechanism that protects total completions can unfairly starve low-traffic tenants unless admission policy declares fairness and per-principal limits.

**Proposed negative experiment (not run):** stall recommendation service, then restore it intermittently. Measure correct booking completion, per-tenant rejection shares, pool wait, queue age, retry amplification and stabilization time. Reject a policy with great mean latency that systematically denies one tenant or hides committed unknown outcomes. The Google SRE and AWS load-shedding references motivate overload design, not the invented thresholds.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.c5d20ae7ef6445e5b23dd5fbac625060:11 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Uber — Cinnamon fairness](../../../cases/uber-cinnamon-admission-and-fairness.md)**. **Relevant mechanism or architectural contrast:** Static edge quotas may fail to protect storage; storage-local feedback can handle load and fairness. **Not established by this report/playbook:** Uber's reported later controller improvements are not proof that every database or customer tier supports the same policy.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Bound admitted work, queue residence, retry amplification and degraded behavior around protected outcomes.

Accepting every request can postpone rejection until after resource exhaustion; useful service may require earlier explicit refusal.

The detailed pages separate the mechanisms that make this decision conditional:

- [Scarce resources, admission and queues](admission-resource.md) — Where must rejection occur to protect the expensive operation?
- [Bulkheads, retries and optional dependencies](dependency-isolation.md) — How can failure in optional work starve core work?
- [Recovery hysteresis and overload experiments](overload-recovery.md) — What prevents a recovering dependency from being overwhelmed immediately?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
