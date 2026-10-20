---
metadata_version: 1
id: "tycho.chapter.16f93a5e11e845d5b4c01a9e6a25f0c7"
kind: "chapter"
parent_id: "tycho.volume.4a94b1e6f8234841afaa51af14330627"
canonical_path: "book/volumes/v09/c01/README.md"
title: "V09/C01 — SLIs, SLOs and error budgets"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which user outcomes are measured and how do budgets guide changes? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Which user outcomes are measured and how do budgets guide changes?"
  prerequisites:
    - "tycho.chapter.5426707ddf264b758016aafe71f342b7"
    - "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
    - "tycho.chapter.a55ddaaa45a647e29b51d6b5c0adbe05"
  related_ids:
    - "tycho.page.c987c475cc5340bcb967f4b6f963b295"
    - "tycho.page.447ffb82d30f4a6999855c0a261e9a2a"
    - "tycho.page.8c596999929c47e48af6a7a2896bb9b9"
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
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# V09/C01 — SLIs, SLOs and error budgets

## Purpose and mission

Which user outcomes are measured and how do budgets guide changes? This chapter owns that question within observability, security and operational architecture. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Define eligible events, good outcomes, observation window and an action policy before using an error budget.

A success-only denominator can hide rejected user operations, so a green dashboard may not describe the promised experience. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](service-level-indicators-objectives-and-alerts.md) | Which user outcomes are measured and how do budgets guide changes? |
| [Eligible events, SLIs and objectives](sli-population.md) | Which user population and observation boundary define the promised outcome? |
| [Error-budget decisions and revisions](budget-actions.md) | What action should a budget trigger and when should the objective be reconsidered? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V09 — Observability, security and operational architecture](../README.md) |
| Previous | [V08/C07 — Multi-region recovery and data reconciliation](../../v08/c07/README.md) |
| Next | [V09/C02 — Metrics ingestion, cardinality and time-series storage](../c02/README.md) |
| Prerequisite | [V02/C07 — Authorization boundaries and multitenancy](../../v02/c07/README.md) |
| Prerequisite | [V04/C04 — Retries, idempotency and duplicate effects](../../v04/c04/README.md) |
| Prerequisite | [V07/C03 — Load-test methods and benchmark validity](../../v07/c03/README.md) |
| Source reading | [Page-local evidence and versions](service-level-indicators-objectives-and-alerts.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.c987c475cc5340bcb967f4b6f963b295:8 -->
## 7. Evidence and review boundaries

| Public source inspected | Supports | Does not establish |
|---|---|---|
| [Google SRE Workbook, Implementing SLOs](https://sre.google/workbook/implementing-slos/) | User-facing service indicators, meaningful targets and measurable populations | An approved target or availability result for any real service |
| [Google SRE Workbook, Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) | Error budget consumption and burn-rate alert considerations | Portable universal alert parameters |
| [Prometheus metric types](https://prometheus.io/docs/concepts/metric_types/) | Counter, gauge and histogram semantics | Correct configured metric labels or business outcome mapping |
| [Tycho performance and queueing](../../v07/c01/queueing-littles-law.md) | Why rate/response-time measurement boundaries matter | End-to-end SLO success for invented booking |

The equipment-booking example, logical outcomes, figures, hypothetical threshold and policy are original invented educational material. No data was collected, alert fired, recording rule executed, production target evaluated, privacy audit or technical peer review performed. The former combined [metrics/SLO/TSDB research page](../../../observability/metrics-slo-timeseries-architecture.md) remains as prior source material until a complete source-to-claim consolidation is accepted.

**Navigation:** proposed **V09/C01**, [observability landing](../../../observability/README.md). Next [Metrics pipeline, cardinality and retention](../c02/metric-pipelines-cardinality-and-retention.md), [Tracing and audit](../../../observability/trace-context-lineage-and-audit.md), and [Incident response](../c06/incident-response-and-operational-change.md).
<!-- /tycho-question-source -->
