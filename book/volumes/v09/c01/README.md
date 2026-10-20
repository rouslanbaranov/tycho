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
summary: "Which user outcomes are measured and how do budgets guide changes?"
route_hints:
  questions:
    - "Which user outcomes are measured and how do budgets guide changes?"
  prerequisites:
    - "tycho.chapter.5426707ddf264b758016aafe71f342b7"
    - "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
    - "tycho.chapter.a55ddaaa45a647e29b51d6b5c0adbe05"
  related_ids: []
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

| Page | Owning question |
|---|---|
| [User-visible service indicators, objectives and error-budget decisions](service-level-indicators-objectives-and-alerts.md) | Which user outcomes are measured and how do budgets guide changes? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Identify the service boundary and eligible population](service-level-indicators-objectives-and-alerts.md#1-identify-the-service-boundary-and-eligible-population).
- [2. An SLI is an observation; an SLO is a chosen target](service-level-indicators-objectives-and-alerts.md#2-an-sli-is-an-observation-an-slo-is-a-chosen-target).
- [Engineering walkthrough — What does a green SLO say about rejected business operations?](service-level-indicators-objectives-and-alerts.md#engineering-walkthrough-what-does-a-green-slo-say-about-rejected-business-operations).
- [7. Evidence and review boundaries](service-level-indicators-objectives-and-alerts.md#7-evidence-and-review-boundaries).

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
