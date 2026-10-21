---
metadata_version: 1
id: "tycho.page.2a3a20bc92314c7597b1792b8607c9d5"
kind: "page"
parent_id: "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
canonical_path: "book/volumes/v01-requirements-and-architecture/c02-workload-and-demand-models/arrivals-population.md"
title: "Population, arrival and admission models"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do user population and arrival process change offered work?"
route_hints:
  questions:
    - "How do user population and arrival process change offered work?"
  prerequisites:
    - "tycho.page.fdb4ef7f69154f8c8c433591f71494f9"
  related_ids:
    - "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
    - "tycho.page.fdb4ef7f69154f8c8c433591f71494f9"
    - "tycho.page.f66686aeabca4f5b8f550696bf37e557"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "arrivals"
    - "population"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.fdb4ef7f69154f8c8c433591f71494f9; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Population, arrival and admission models

**Owning question:** How do user population and arrival process change offered work?

This page belongs to [V01/C02 — Workload and demand models](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.fdb4ef7f69154f8c8c433591f71494f9:1 -->
## 1. Workload nouns that must not be interchanged

| Term | Meaning at a declared boundary | Misuse to prevent |
|---|---|---|
| Registered users | Accounts capable of future activity | “Registered = concurrent” |
| Active users (DAU/MAU) | People active in an observation interval | “Active = simultaneous requests” |
| Sessions/connections | Client interactions or open transports; may be idle | “Connection count = CPU concurrency” |
| Scheduled logical operations | Independent business intents offered over time | “Retries are new business demand” |
| Attempts | Actual transmitted requests including retries | “All attempts = distinct successful operations” |
| Offered rate | Arrivals presented to a defined boundary/window | “Completed throughput = offered rate” |
| Admitted rate | Work allowed into processing | “Rejected requests never existed” |
| Completed rate | Work reaching a reported exit state in a window | “Every exit was timely and correct” |
| In-flight concurrency | Work resident inside a stated system boundary | “More tasks always increase useful capacity” |
| Resource demand | CPU, storage I/O, locks, connections, memory and external quotas consumed per operation | “Equal RPS means equal backend cost” |

For any quantity, record **units, observation interval, measurement point, data source and confidence**. A ratio such as “requests per active user” requires an observed or explicitly assumed behavioral model and time window. RPS is a rate, not a storage capacity or business correctness measure.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.fdb4ef7f69154f8c8c433591f71494f9:2 -->
## 2. Arrival shape is part of the architecture requirement

Averages conceal peaks, clustering and correlations. A design must distinguish:
- baseline arrivals from short bursts and periodic batch imports;
- independent external arrivals from clients waiting for previous responses;
- retries after ambiguous outcomes from new logical operations;
- read operations from mutation and expensive analytical queries;
- broad key distributions from a few high-contention keys;
- time-varying payload sizes, tenant mixes, feature flags and geography;
- workload growth from workload **composition** changes.

A simplistic stationary rate is useful for bounded math, but should not be treated as an empirical forecast of bursts. Workload rates can vary within seconds; a one-hour mean hides a 10-second surge. A model without key skew can understate the cost of exclusive lock ownership even when total attempts match.

The public [k6 open/closed modeling guidance](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/) explains why closed client loops can reduce new arrivals as service time increases, whereas arrival-rate executors schedule arrivals independently. This is a generator-model distinction, not proof that all real users behave as open arrivals.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](workload-demand-and-arrival-models.md) |
| Next | [Continue the reasoning](demand-skew.md) |
| Integrated question | [Original scenario and limits](workload-demand-and-arrival-models.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
