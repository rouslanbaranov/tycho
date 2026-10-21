---
metadata_version: 1
id: "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
kind: "chapter"
parent_id: "tycho.volume.4d10f5c93f3b4356a553c8732e513a38"
canonical_path: "book/volumes/v01-requirements-and-architecture/c02-workload-and-demand-models/README.md"
title: "V01/C02 — Workload and demand models"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do active users, offered arrivals, concurrency, operation mix and skew differ? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How do active users, offered arrivals, concurrency, operation mix and skew differ?"
  prerequisites:
    - "tycho.chapter.9d4f989ec9304e418f60f1ad7248094a"
  related_ids:
    - "tycho.chapter.e365b78505784c20a4f3d72fe7904d9b"
    - "tycho.page.fdb4ef7f69154f8c8c433591f71494f9"
    - "tycho.page.2a3a20bc92314c7597b1792b8607c9d5"
    - "tycho.page.f66686aeabca4f5b8f550696bf37e557"
    - "tycho.page.59682af71a9f435680917ae5ece63088"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---

# V01/C02 — Workload and demand models

## Purpose and mission

How do active users, offered arrivals, concurrency, operation mix and skew differ? This chapter owns that question within requirements, quality attributes and architecture fundamentals. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Separate offered attempts, admitted work, successful outcomes, concurrency and per-operation demand before estimating capacity.

Two equally sized user populations can impose different bursts and hot-key pressure; average requests per second conceals that difference. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](workload-demand-and-arrival-models.md) | How do active users, offered arrivals, concurrency, operation mix and skew differ? |
| [Population, arrival and admission models](arrivals-population.md) | How do user population and arrival process change offered work? |
| [Demand arithmetic and skew](demand-skew.md) | What does a demand estimate conceal about operation mix, bursts and hot keys? |
| [Workload contracts for architecture choices](workload-contract.md) | What must a workload contract state before it can reject or support an option? |

## Boundaries and further reading

- [V07/C01 — Queueing, Little's Law and measurement boundaries](../../v07-performance-scale-and-resilience/c01-queueing-littles-law-and-measurement-boundaries/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V01 — Requirements, quality attributes and architecture fundamentals](../README.md) |
| Previous | [V01/C01 — Problem framing and system boundaries](../c01-problem-framing/README.md) |
| Next | [V01/C03 — Quality attributes and trade-offs](../c03-quality-attributes-and-trade-offs/README.md) |
| Prerequisite | [V01/C01 — Problem framing and system boundaries](../c01-problem-framing/README.md) |
| Source reading | [Page-local evidence and versions](workload-demand-and-arrival-models.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.fdb4ef7f69154f8c8c433591f71494f9:8 -->
## 8. Public evidence and unverified claims

| Source consulted | Scope | Limitation |
|---|---|---|
| [Grafana k6 Open and Closed Models](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/) | Arrival coupling and generator model semantics | Not a survey of user behavior |
| [Grafana k6 Dropped Iterations](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/dropped-iterations/) | Explicit unsent scheduled arrivals and multiple causes | No observed Tycho or fictional system load |
| [John D. C. Little, 1961 queueing identity (DOI)](https://doi.org/10.1287/opre.9.3.383) | Classical mean occupancy/throughput/residence relation under its assumptions | Not a tail-latency or capacity prediction |
| [Tycho Little's Law study](../../v07-performance-scale-and-resilience/c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md) | Original derivation and finite-window caveats | No exercised benchmark |

The user populations, arrival rates, averages, resource budgets, diagrams and work schedules are **wholly synthetic**. No customer data or restricted sources were used. Neither the forecast nor a benchmark has been independently validated. Editorial source-to-claim verification, case selection and final volume/page structure remain open.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.fdb4ef7f69154f8c8c433591f71494f9:9 -->
### Archived proposal-era navigation

This retained proposal-era route is historical. Current navigation is the
"Navigation and prerequisites" table above; the original outline links are not
repeated.
<!-- /tycho-question-source -->
