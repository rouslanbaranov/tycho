---
metadata_version: 1
id: "tycho.page.5ae9f2c4b45842c7975fd32c252dc4d8"
kind: "page"
parent_id: "tycho.chapter.b7924b3db65949df952fbb5ca706236c"
canonical_path: "book/volumes/v07-performance-scale-and-resilience/c07-capacity-planning-and-cost-performance-trade-offs/capacity-planning-and-cost-performance.md"
title: "Capacity planning and cost/performance trade-offs"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Integrated question, original scenario and transfer limits for Capacity planning and cost/performance trade-offs. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "What experiments can confirm or falsify a scaling hypothesis?"
  prerequisites: []
  related_ids:
    - "tycho.page.49d9df04c0b4488e936b02e580a62271"
    - "tycho.page.7ad835c06d5a4e3aabf6b14632f92c86"
    - "tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.b08f16ced4a142a785c37b43eb340260"
    - "tycho.page.fdb4ef7f69154f8c8c433591f71494f9"
    - "tycho.page.c5d20ae7ef6445e5b23dd5fbac625060"
    - "tycho.page.f05854fcc406435bbf38a192bc7ab2f1"
    - "tycho.page.32a5de3daa2d4f74b879165a4119f63a"
    - "tycho.page.f8f41847ac424c17a5ac3e33fd5b0c6a"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Capacity"
    - "planning"
    - "and"
    - "cost/performance"
    - "trade-offs"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
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
<!-- tycho-question-source:tycho.page.5ae9f2c4b45842c7975fd32c252dc4d8:-1 -->

# Capacity planning and cost/performance trade-offs

> **Tycho original book manuscript V07/C07**, 2026-10-19. Calculations, scenario, parameters and diagrams are fictional; official public AWS Well-Architected cost guidance was consulted for principles, not for prices, forecasts or measured performance. No cloud bill, simulator, benchmark or production cost study was used. The content_review field retains the decomposition-era draft state; no independent acceptance is asserted.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.5ae9f2c4b45842c7975fd32c252dc4d8:0 -->
## Purpose and mission

Performance decisions buy *capacity over time*, not just a lower measured p99. More replicas can reduce queueing and absorb uneven demand while increasing total resource cost, per-instance connection pressure and operational work. A larger instance can improve one CPU-bound operation without changing an upstream quota or serialized data key.

The economic question is: **What is the least costly configuration that satisfies correctness, user-visible service targets, recovery and operational constraints across the actual demand distribution?** It is different from “Which option has the lowest price per virtual machine?”

The owning question is which experiments confirm or falsify a scaling hypothesis. Here the hypothesis is an economic capacity choice, so the decision test compares service outcomes and total operating cost under the demand distribution, not a raw price or a single peak metric.

The [AWS Well-Architected Cost Optimization principles](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) recommend measuring business output against expenditure, adopting consumption where appropriate and attributing costs to their actual owners. The [demand/supply guidance](https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/cost-mandem.html) notes the cost/latency role of scaling, throttling, buffering and deferred work. These references describe principles, not universally optimal budgets.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.5ae9f2c4b45842c7975fd32c252dc4d8:8 -->
## Engineering walkthrough — Provision, shed, optimize or simplify under uncertain prices

**Original synthetic envelope:** a hypothetical catalogue expects 100–400 requests/s depending on a publication event, with 10% writes and one hot resource. Direct unit prices and exact staffing rates are **unknown**. The architect must compare not a single monthly VM bill but correct peak outcomes, shared database budget, retention, multi-zone idle capacity and time to recover from overload.

| Candidate | Potential strength | Variable that may reverse choice |
|---|---|---|
| Provision extra replicas | Faster response to burst if app CPU is bottleneck | Shared DB lock/pool remains the limit; unused warm capacity costs money |
| Shed/defer optional work | Protect invariant and critical journeys | Product cannot accept deferred confirmation or unfair priority |
| Optimize query/key access | Less demand per correct operation | No meaningful backend query cost in measured bottleneck |
| Simplify/remove unnecessary distributed hop | Lower operational and retry overhead | True isolation/deployment requirement outweighs coordination cost |

A defensible cost model exposes quantities: instance-hours, data bytes×retention, egress GB, high-cardinality time-series, human on-call hours, migration person-days, repeated backup/DR exercises and expected rework risk. It must vary each cost input over a documented plausible range rather than pretend an invented provider price is a source-backed rate.

**Synthetic sensitivity rule:** if one candidate only wins when app instance prices fall 90% or when a known critical correctness constraint is waived, mark it fragile or inadmissible. Report correct throughput per total operating cost *conditional on* tested workload, not raw RPS per VM. **Proposed experiment, not run:** test steady/peak/degraded load, keep shared-state integrity, record actual unit use and capacity drain after overload; select an option only after gating security and recoverability separately. The existing Well-Architected cost guidance supports modeling categories, not numerical market forecasts.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Compare correct work per total operating cost over steady, peak and degraded conditions with sensitivity to uncertain inputs.

Raw requests per second per instance ignores rejected work, recovery and shared-state costs; an apparent optimum can violate a hard requirement.

The detailed pages separate the mechanisms that make this decision conditional:

- [Capacity envelopes and total operating cost](capacity-cost-model.md) — Which correct outcomes and lifecycle costs belong in a capacity comparison?
- [Sensitivity, extrapolation and simpler alternatives](sensitivity-options.md) — Which uncertain input or hard constraint can reverse the preferred capacity option?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
