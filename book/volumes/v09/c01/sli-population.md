---
metadata_version: 1
id: "tycho.page.447ffb82d30f4a6999855c0a261e9a2a"
kind: "page"
parent_id: "tycho.chapter.16f93a5e11e845d5b4c01a9e6a25f0c7"
canonical_path: "book/volumes/v09/c01/sli-population.md"
title: "Eligible events, SLIs and objectives"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "operations"
summary: "Which user population and observation boundary define the promised outcome?"
route_hints:
  questions:
    - "Which user population and observation boundary define the promised outcome?"
  prerequisites:
    - "tycho.page.c987c475cc5340bcb967f4b6f963b295"
  related_ids:
    - "tycho.chapter.16f93a5e11e845d5b4c01a9e6a25f0c7"
    - "tycho.page.c987c475cc5340bcb967f4b6f963b295"
    - "tycho.page.8c596999929c47e48af6a7a2896bb9b9"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "sli"
    - "population"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.c987c475cc5340bcb967f4b6f963b295; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Eligible events, SLIs and objectives

**Owning question:** Which user population and observation boundary define the promised outcome?

This page belongs to [V09/C01 — SLIs, SLOs and error budgets](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.c987c475cc5340bcb967f4b6f963b295:1 -->
## 1. Identify the service boundary and eligible population

An indicator needs a **denominator**. Consider an original fictional public equipment-reservation service. A user submits a logical attempt for a valid timeslot; it can be accepted, explicitly rejected because another reservation won, rejected for capacity, timed out, or commit without a delivered acknowledgment.

A proposed availability SLI could be the fraction of *eligible logical booking decisions* returned correctly within a deadline, where the service owner must determine which rejection classes are legitimate expected outcomes. A conflict rejection may represent correct business behavior, while a capacity rejection indicates service inability under a declared demand envelope. The treatment must be documented before measurements begin; otherwise changing the denominator can manufacture an apparent improvement.

| Defining question | Decision that must be explicit |
|---|---|
| What is one eligible operation? | Intent identity rather than HTTP attempt count across retries |
| Which boundary starts the clock? | Client, edge, API ingress, or asynchronous final decision |
| Which outcomes count as good? | Correct accepted/rejected result under business rules and deadline |
| How are pending/unknown outcomes treated? | Pending is not silently equivalent to completed; status contract matters |
| What window is meaningful? | 30 days, a shorter operating window or a stated peak event |
| Whose experience is represented? | Client type, route, operation class and authorized population |

The [SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) begins with user-facing SLIs and deliberately asks teams to select meaningful service boundaries and objectives. It does not set a universal success percentage for this fictional scenario.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.c987c475cc5340bcb967f4b6f963b295:2 -->
## 2. An SLI is an observation; an SLO is a chosen target

A service-level indicator is a quantified property of service behavior, such as the share of eligible requests that satisfy correctness and deadline gates. An objective is the target for that indicator over a specified rolling or calendar window. A signed external SLA is a separate agreement, not automatically the same as an internal SLO.

**Synthetic arithmetic, not a real objective:** suppose an owner elects a 99.9% good-event target over a 30-day period and exactly 500,000 eligible logical decisions occur. The allowed number of bad decisions under this arithmetic is **500**, assuming the unit, population and boundary are consistently counted.

A target without a specified event population can be meaningless. In a system with strongly varying demand, a time-based downtime ratio and a request-based failure ratio measure different effects. Neither automatically captures incorrect durable writes.

An error budget is an accounting expression of **permitted bad events under the chosen SLO**, not permission to violate a non-negotiable state invariant, authorization rule or contractual data-loss constraint. One duplicate committed allocation remains forbidden if exclusivity is a hard requirement, even if the overall availability SLO appears green.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.c987c475cc5340bcb967f4b6f963b295:3 -->
## 3. Measure the right signals at the right level

Choose enough instrumentation to derive the end-user SLI:
- an authoritative logical operation ID spanning retries;
- attempt, admission and final outcome states, including explicit unknown/timeout;
- request/operation elapsed time from the selected clock;
- route, operation and bounded response classification;
- relevant policy/version context, without leaking private principals in metric labels;
- reconciliation outcomes after lost acknowledgments.

[Prometheus metric types](https://prometheus.io/docs/concepts/metric_types/) distinguishes counters (monotone cumulative except reset), gauges and histograms. A counter of attempted requests can be a useful measurement; it is not the same denominator as successful *unique booking decisions* if clients retry. A histogram can support latency SLO computation under its bucket/exemplar resolution and aggregation constraints. One recorded p99 without rejected/timed-out populations cannot prove user experience.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](service-level-indicators-objectives-and-alerts.md) |
| Next | [Continue the reasoning](budget-actions.md) |
| Integrated question | [Original scenario and limits](service-level-indicators-objectives-and-alerts.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
