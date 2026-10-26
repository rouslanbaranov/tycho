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

**Fallback.** A fallback returns a declared alternate result or dependency when the primary
is unavailable. It must preserve the same correctness contract: a cached, fabricated or
partial value is not a successful authoritative result. Name the fallback's freshness,
authority and user-visible label; fail explicitly if none is valid. An explicit failure
or a queued retry may be safer than a plausible but wrong fallback.

**Graceful degradation.** Degradation removes optional features or reduces quality to
protect an essential outcome under overload. It is a product decision, not an automatic
consequence of a timeout: declare which outcomes remain mandatory, which become
unavailable, and how callers observe the reduced state. Hidden degradation that silently
drops correctness is worse than an explicit failure. A complete but explicit outage or
horizontal capacity increase may be preferable when no safe degraded mode exists.

**Load shedding.** Shedding rejects or drops work before a scarce resource is exhausted so
accepted work can meet its deadline. It needs a bottleneck-specific signal, fair principal
policy and retry guidance. A rejection without a retry hint can create a synchronized
retry storm; shedding one tenant's traffic can be unfair if the policy does not declare
quotas. Queueing/backpressure, admission control or provisioning may be preferable when
the work is deferrable or the bottleneck can be expanded.

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

**Throttling.** Throttling paces or slows admitted work below offered load to protect a
dependency. It needs a measurable bottleneck, a bounded queue and propagation of
backpressure. Throttling can hide capacity loss, add latency to essential classes or turn
a transient spike into a long tail; measure accepted work, queue age and per-class latency.
Admission control, queueing or provisioning may be preferable when work is deferrable or
capacity can expand.

**Rate limiting.** Rate limiting bounds requests per principal, key or window; it must
define the identity, window, burst allowance and rejection response. Fixed windows can
allow burst doubling, while per-principal limits can be bypassed through many keys. Unfair
limits and synchronized retries are common failure modes. Global admission or per-tenant
quotas may be preferable when the scarce resource is shared across principals.

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
## Bounded pattern ownership notes

### Fallback

The owner of the primary outcome also owns its fallback, because only that owner can judge
whether an alternate preserves the same correctness contract. A dependency team's proposal needs
explicit acceptance.

Document the trigger and caller-visible label. A plausible substitute that hides its limits is a
correctness failure; do not let the alternate impersonate the primary.

A read-only fallback may serve a display; a fallback that writes needs duplicate protection,
reconciliation and a repair procedure. An explicit error remains valid when no alternate
satisfies the contract.

Exercise the alternate under the same load profile as the primary and record how often it
activates. Remove it when the failure it hides outlives its usefulness. Ownership includes the
decision to stop offering the alternate, recorded alongside its original approval.

### Graceful Degradation

Graceful degradation removes optional features or reduces quality to protect an essential outcome
under overload. It must declare which outcomes stay mandatory, which become unavailable and how
callers observe the reduced state.

Silent loss of correctness is worse than an explicit failure. Each mode
needs an entry condition, a visible status, an owner and an audited override for emergency use.
Recovery needs hysteresis: remain degraded
until the trigger metric stays below threshold for a sustained window, then restore normal service
and re-test the essential path. Without that window the mode flaps between normal and degraded.

A complete, explicit outage or added capacity may be preferable when no safe mode exists.
Degradation is a product decision, not only an infrastructure switch, and the essential path must
be tested under the load that triggers the mode.

### Load Shedding

Shedding requires one named bottleneck and an admission point close to it. A load balancer
rejecting traffic without that link merely relocates the queue.

The policy owner defines criticality classes, tenant fairness and the share of work that may be
refused. Those are product choices that deserve review outside an incident. Publish the class
definitions so callers can predict which requests may be refused.

Return a typed rejection with a retry class and the protected resource, not a generic failure.
Count shed work by class so silent starvation cannot masquerade as health. The rejection
contract also states whether a retry is safe and when.

Deferral and added capacity remain the competing responses when rejection would waste useful
work. Revisit the thresholds when traffic mix, tenant count or bottleneck capacity changes. The
policy should also state who may approve an emergency exception and for how long.

### Throttling

Throttling slows work that has already been admitted; it does not decide who deserves service.
The invariant is that every admitted class has a bounded wait and a declared rejection point;
no class waits without a deadline. The owner must state which dependency is protected and which
class waits. That declaration
belongs with the operational policy, not only in a dashboard.

A finite buffer and an upstream backpressure signal make pacing enforceable. Without them,
pacing shifts latency and memory pressure downstream. That buffer converts overload into an
explicit decision rather than a growing delay. Sizing should follow observed service time, not
an arbitrary request count.

Publish the limit, measurement window and retry guidance so callers can pace themselves. Watch
waiting time and class-specific completion, not only the arrival rate.

Rejecting excess work or adding capacity may be cheaper than delaying everyone. Review the
policy when the protected dependency, traffic shape or deadline changes. Emergency work needs an
exception path with an owner and an expiry.

### Rate Limiting

Rate limiting bounds requests per principal, key or window; it must define the identity, window,
burst allowance and rejection response. The identity is the hard part: a shared key can let one
caller exhaust another's budget.

Unfair limits and synchronized retries are common failure modes. Publish the limit, return a retry
hint and keep a separate safety limit for abusive traffic. A limiter on one instance is not a global
quota unless the shared state makes it global.

Global admission or per-tenant quotas may be preferable when the scarce resource is shared across
principals. Rate limiting is a fit when fairness and abuse control matter more than exact capacity
utilization. A global quota needs shared state and a clock-skew test.
