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
  source_ids:
    - "src.sre"
    - "src.sre-workbook"
    - "src.prometheus"
    - "src.openslo"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Bounded pattern owner section for tycho.pattern.sli-slo-and-error-budgets.
    The 2026-10-31 section binds Google SRE Workbook, Google SRE Book, OpenSLO
    and Prometheus units; src.openslo is registered in the shared source
    register. Exact digests and limits are recorded in the lane note and the
    reading ledger.
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-31"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.c987c475cc5340bcb967f4b6f963b295:-1 -->

# User-visible service indicators, objectives and error-budget decisions

> **Tycho chapter-owner draft V09/C01, 2026-10-19.** Public Google SRE Workbook, Prometheus and OpenTelemetry documentation inform the explanation. The workflow, numbers and examples are original fictional teaching material. No service SLO, alert rule, monitoring deployment, traffic trace, data sample or independent technical acceptance has been observed or executed.
>
> The 2026-10-31 source bindings and self-check are recorded in the lane note,
> reading ledger and owner-unit metadata; the page keeps its decomposition-era
> review field. No independent acceptance is asserted.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [SLI/SLO and Error Budgets](../../v11-pattern-atlas/c11-security-operations/sli-slo-and-error-budgets.md#sli--slo-and-error-budgets) — decision conditions and contraindications.

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

**Mechanism.** The Google SRE Workbook defines an SLI as "an indicator of the level of
service that you are providing" and recommends "treating the SLI as the ratio of two
numbers: the number of good events divided by the total number of events." It states that
"the SLO is a target percentage and the error budget is 100% minus the SLO." The SRE Book
calls the SLO "a target value or range of values for a service level that is measured by an
SLI" and the error budget "a rate at which the SLOs can be missed." OpenSLO likewise
defines an SLO as "a target value or a range of values for a service level that is
described by a service level indicator (SLI)."
**Tycho reading:** the ratio, target and complement are a measurement contract, not a
dashboard label. The arithmetic below is Tycho synthetic illustration, not a source claim:
A hypothetical target SLO of 99.9% would allow at most 10 failures among 10,000 intents,
while this window has 30, **consuming 300% of the target's error allowance**.

**Invariant.** The SRE Book warns that "we often aggregate raw measurements. This needs to
be done carefully" and recommends that teams "standardize on common definitions for SLIs so
that you don’t have to reason about them from first principles each time." Its standard
template names "Which requests are included" and gives "HTTP GETs from black-box monitoring
jobs" as an example. The Workbook permits "a rolling window or a calendar-aligned window"
and defines the ratio as good events over total events. Whether user cancellations, blocked
abusive traffic, malformed requests and legitimate overload rejections count must be agreed
before measurement; exclusion policy cannot change retrospectively to improve the score.
**Tycho rule:** fix the eligible population, numerator, denominator, window, aggregation and
exclusions before measurement, and publish them with the data source. A later change is a
new SLO version and must be reviewed, not used to rewrite an earlier score.

**Failure and recovery.** The Workbook states that "once you exhaust your error budget (or
come close to exhausting it), you should do something in order to restore stability to your
system." Its policy must "cover the specific actions that must be taken when a service has
consumed its entire error budget for a given period of time, and specify who will take
them." The alerting chapter defines "Burn rate is how fast, relative to the SLO, the
service consumes the error budget" and recommends "the multiwindow, multi-burn-rate alerting
technique" as "the most appropriate approach to defending your application’s SLOs."
Prometheus implements alerts with an optional `for` clause that waits for a condition to
persist and a `keep_firing_for` clause that "tells Prometheus to keep this alert firing for
the specified duration after the firing condition was last met." That clause can prevent
"flapping alerts, false resolutions due to lack of data loss, etc." **Tycho reading:** a
skipped evaluation is a real blind spot: "the next evaluation will be skipped" and
`rule_group_iterations_missed_total` increments. The Book's control loop is to "Monitor and
measure the system’s SLIs. Compare the SLIs to the SLOs, and decide whether or not action is
needed. If action is needed, figure out what needs to happen in order to meet the target.
Take that action."
**Tycho runbook:** alert on user-visible burn, not raw 2xx counts; use multiwindow burn-rate
rules with bounded `for` and `keep_firing_for`; treat missed rule evaluations as a monitoring
gap; and on budget exhaustion execute the written policy (prioritize reliability work, freeze
risky changes, allow reviewed security exceptions). An instrumentation design that counts
only HTTP 2xx responses among requests **admitted into the service**, excluding 500
deliberate overload rejections before the handler, can report misleading health.

**Alternative.** OpenSLO aims "to provide an open specification for defining SLOs to enable a
common, vendor–agnostic approach to tracking and interfacing with SLOs", but
"Platform-specific implementation details are purposefully excluded from the scope of this
specification." Prometheus takes the executable side: "Recording rules allow you to
precompute frequently needed or computationally expensive expressions and save their result
as a new set of time series", and "Alerting rules allow you to define alert conditions based
on Prometheus expression language expressions and to send notifications about firing alerts
to an external service."
**Tycho choice rule:** use OpenSLO when one SLO definition must travel across tools and
teams; use Prometheus recording and alerting rules when one execution environment owns the
definition and executable queries and routing matter. Reverse when translation and duplicate
maintenance cost exceeds the portability benefit, or when the platform-specific rule itself
is the contract. Metrics or a simpler availability check may be preferable when the user
journey is not measurable.

**Bound source limits.** Six public units were read on 2026-10-31: Google SRE Workbook
"Implementing SLOs" and "Alerting on SLOs"; Google SRE Book "Service Level Objectives";
OpenSLO "Specification"; and Prometheus "Alerting rules" and "Defining recording rules."
They are public documentation or specification pages, not benchmarks or production
observations. Headers, digests and section lists are in the lane note. No SLO, alert rule,
recording rule or monitoring deployment was created or executed; no budget, burn rate or
alert latency was measured. The 99.9%/300% arithmetic, the 2xx-only blind spot and the
action policy remain Tycho synthetic guidance. Quotes are short whitespace-normalized
excerpts, not full-page reproductions.
