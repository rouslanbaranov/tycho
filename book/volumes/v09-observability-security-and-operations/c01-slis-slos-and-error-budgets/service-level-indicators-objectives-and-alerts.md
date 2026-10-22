---
metadata_version: 1
id: "tycho.page.c987c475cc5340bcb967f4b6f963b295"
kind: "page"
parent_id: "tycho.chapter.16f93a5e11e845d5b4c01a9e6a25f0c7"
canonical_path: "book/volumes/v09-observability-security-and-operations/c01-slis-slos-and-error-budgets/service-level-indicators-objectives-and-alerts.md"
title: "User-visible service indicators, objectives and error-budget decisions"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "operations"
summary: "Integrated question, original scenario and transfer limits for SLIs, SLOs and error budgets. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which user outcomes are measured and how do budgets guide changes?"
  prerequisites: []
  related_ids:
    - "tycho.page.61b76bbbef8b42de8cc8603a5bc9bf53"
    - "tycho.page.6b9a3f5c7bae455ab4f56f151f17b406"
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.1c7350e3bc17483ba18f201d02727aea"
    - "tycho.landing.b7ea8fb13ebb4079af2333e475f97106"
    - "tycho.page.d87f9ba3852b49ee8188d150bb679716"
    - "tycho.page.447ffb82d30f4a6999855c0a261e9a2a"
    - "tycho.page.8c596999929c47e48af6a7a2896bb9b9"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "User-visible"
    - "service"
    - "indicators"
    - "objectives"
    - "and"
    - "error-budget"
    - "decisions"
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
<!-- tycho-question-source:tycho.page.c987c475cc5340bcb967f4b6f963b295:-1 -->

# User-visible service indicators, objectives and error-budget decisions

> **Tycho chapter-owner draft V09/C01, 2026-10-19.** Public Google SRE Workbook, Prometheus and OpenTelemetry documentation inform the explanation. The workflow, numbers and examples are original fictional teaching material. No service SLO, alert rule, monitoring deployment, traffic trace, data sample or independent technical acceptance has been observed or executed.
>
> The content_review field retains the decomposition-era draft state; no independent
> acceptance is asserted.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [SLI/SLO and Error Budgets](../../v11-pattern-atlas/c11-security-operations/README.md#sli-slo-and-error-budgets) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.c987c475cc5340bcb967f4b6f963b295:0 -->
## Purpose and mission

A service-level objective (SLO) should make an explicit promise about **the user experience we want to preserve** and the window in which that promise is evaluated. Infrastructure utilization can help explain a problem, but a green CPU dashboard cannot show that an authorized user completed the intended operation or that a booking was not duplicated.

This chapter owns *which user events constitute success, how an indicator becomes a target, and how alerts create decisions*. [Metrics pipeline, cardinality and retention](../c02-metrics-ingestion-cardinality-and-time-series-storage/metric-pipelines-cardinality-and-retention.md) owns instrumentation temporality, metric representation and storage costs. [Distributed tracing](../../../observability/trace-context-lineage-and-audit.md) owns request-causality evidence, not the definition of successful user outcomes.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.c987c475cc5340bcb967f4b6f963b295:7 -->
## Engineering walkthrough — What does a green SLO say about rejected business operations?

**Original fictional service window:** a booking endpoint records 10,000 *eligible* distinct user intents in a 30-day measurement interval, of which 9,970 reach the declared correct final result within the user deadline. A hypothetical target SLO of 99.9% would allow at most 10 failures among 10,000 intents, while this window has 30, **consuming 300% of the target's error allowance**. These values and target are illustrative, not a real SLO or observed incident.

An instrumentation design that counts only HTTP 2xx responses among requests **admitted into the service**, excluding 500 deliberate overload rejections before the handler, can report misleading health. Whether user cancellations, blocked abusive traffic, malformed requests and legitimate overload rejections count must be agreed before measurement; exclusion policy cannot change retrospectively to improve the score.

| Signal | Valid intended meaning | Unacceptable substitution |
|---|---|---|
| Eligible intents | Named user population and observation boundary | Completed requests only, hiding admission failures |
| Correct within deadline | Durable domain result, not merely 2xx | Queue acknowledgment called final reservation |
| Error-budget burn | Rate/quantity under chosen SLO window | Arbitrary alert threshold with no user consequence |
| Incident recovery | Correct journey restored and sustained | Process liveness or dashboard green after data divergence |

**Policy decision:** with that invented budget overspend, a sensible organization might delay nonessential risky deployments and prioritize correctness recovery while permitting necessary security fixes through a separately reviewed exception. This is a conditional governance choice, not a rule universally imposed by Google's SRE guidance.

**Proposed, not run:** inject dependency outage, client retries and admission rejections, independently count durable logical intents and compare with telemetry numerator/denominator. Recompute burn under both legitimate and unjustified exclusions and document who authorizes any change. The existing Google SRE SLO and alerting references support measurement principles, not the fictional budget.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Define eligible events, good outcomes, observation window and an action policy before using an error budget.

A success-only denominator can hide rejected user operations, so a green dashboard may not describe the promised experience.

The detailed pages separate the mechanisms that make this decision conditional:

- [Eligible events, SLIs and objectives](sli-population.md) — Which user population and observation boundary define the promised outcome?
- [Error-budget decisions and revisions](budget-actions.md) — What action should a budget trigger and when should the objective be reconsidered?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

## Bounded pattern ownership notes

### SLI-SLO and Error Budgets

An SLI is a measured ratio of good events to valid events; an SLO is the target for that ratio over
a window, and the error budget is the allowed failure quantity. The measurement contract precedes
the number, because a green indicator built on the wrong denominator is worse than no indicator.

A hypothetical target SLO of 99.9% would allow at most 10 failures among 10,000 intents, while this
window has 30, **consuming 300% of the target's error allowance**. Whether user cancellations,
blocked abusive traffic, malformed requests and legitimate overload rejections count must be agreed
before measurement; exclusion policy cannot change retrospectively to improve the score.

An instrumentation design that counts only HTTP 2xx responses among requests **admitted into the
service**, excluding 500 deliberate overload rejections before the handler, can report misleading
health. Publish the denominator, the exclusions and the data source, and review the budget with the
product owner.

Metrics or a simpler availability check may be preferable when the user journey is not measurable.
An SLO is a fit when the team can act on the budget and the indicator tracks a real user outcome.
