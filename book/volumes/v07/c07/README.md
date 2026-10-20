---
metadata_version: 1
id: "tycho.chapter.b7924b3db65949df952fbb5ca706236c"
kind: "chapter"
parent_id: "tycho.volume.f7679623ca274bff8a00389d409d68c6"
canonical_path: "book/volumes/v07/c07/README.md"
title: "V07/C07 — Capacity planning and cost/performance trade-offs"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What experiments can confirm or falsify a scaling hypothesis? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "What experiments can confirm or falsify a scaling hypothesis?"
  prerequisites:
    - "tycho.chapter.1d8d87e683bc428e8dbed087106f37fd"
  related_ids:
    - "tycho.page.5ae9f2c4b45842c7975fd32c252dc4d8"
    - "tycho.page.32a5de3daa2d4f74b879165a4119f63a"
    - "tycho.page.f8f41847ac424c17a5ac3e33fd5b0c6a"
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

# V07/C07 — Capacity planning and cost/performance trade-offs

## Purpose and mission

What experiments can confirm or falsify a scaling hypothesis? This chapter owns that question within performance, scale and resilience under load. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Compare correct work per total operating cost over steady, peak and degraded conditions with sensitivity to uncertain inputs.

Raw requests per second per instance ignores rejected work, recovery and shared-state costs; an apparent optimum can violate a hard requirement. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](capacity-planning-and-cost-performance.md) | What experiments can confirm or falsify a scaling hypothesis? |
| [Capacity envelopes and total operating cost](capacity-cost-model.md) | Which correct outcomes and lifecycle costs belong in a capacity comparison? |
| [Sensitivity, extrapolation and simpler alternatives](sensitivity-options.md) | Which uncertain input or hard constraint can reverse the preferred capacity option? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V07 — Performance, scale and resilience under load](../README.md) |
| Previous | [V07/C06 — Horizontal/vertical scaling and autoscaling delay](../c06/README.md) |
| Next | [V08/C01 — CI/CD architecture and artifact provenance](../../v08/c01/README.md) |
| Prerequisite | [V07/C06 — Horizontal/vertical scaling and autoscaling delay](../c06/README.md) |
| Source reading | [Page-local evidence and versions](capacity-planning-and-cost-performance.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.5ae9f2c4b45842c7975fd32c252dc4d8:7 -->
## 7. Public sources and nonclaims

| Source reviewed | Supports | Not demonstrated |
|---|---|---|
| [AWS Well-Architected: Cost Optimization design principles](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) | Cost attribution, consumption, outcome efficiency and operation | Current provider pricing or a real bill |
| [AWS Well-Architected: Demand/supply resources](https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/cost-mandem.html) | Workload-aligned supply, buffers/throttling, scaling-lag consideration | Economic viability of the invented options |
| [AWS Cost Based on Workload Metrics](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost_monitor_usage_allocate_outcome.html) | Output-based unit economics and allocation principles | Real cost-per-journey data |
| [Tycho scaling-law chapter](../c02/contention-saturation-and-scaling-laws.md) | Conditions for saturation and diminishing returns | Per-service measured fit |

All amounts, charts, load assumptions and architectural examples are original teaching models. They are not measured prices or actual workloads. The proposed decisions have no independent financial/operational reviewer, validated capacity curve, tool run, or final edition metadata.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.5ae9f2c4b45842c7975fd32c252dc4d8:9 -->
## Navigation

Proposed owner **V07/C07** in [outline](../../../PROPOSED-STRUCTURE.md), currently [performance landing](../../../performance/README.md). Read first [workload arrivals](../../v01/c02/workload-demand-and-arrival-models.md), [contended resources](../c02/contention-saturation-and-scaling-laws.md); continue with [autoscaling](../c06/autoscaling-lag-and-capacity-limits.md), [overload protection](../c05/overload-admission-control-and-graceful-degradation.md), [full book decision criteria](../../v10/c04/architecture-alternatives-experiments-and-adrs.md).
<!-- /tycho-question-source -->
