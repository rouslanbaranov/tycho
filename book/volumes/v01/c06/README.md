---
metadata_version: 1
id: "tycho.chapter.bbfd14751d274868b152ba431dc904c9"
kind: "chapter"
parent_id: "tycho.volume.4d10f5c93f3b4356a553c8732e513a38"
canonical_path: "book/volumes/v01/c06/README.md"
title: "V01/C06 — Capacity, operational constraints and total cost"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which hard gates and team/budget limits invalidate otherwise appealing options? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Which hard gates and team/budget limits invalidate otherwise appealing options?"
  prerequisites:
    - "tycho.chapter.abcbb298887b49e79525ca00fead8926"
  related_ids:
    - "tycho.page.76244dbe2bd44035b7154f821191f6f2"
    - "tycho.page.8284605817fc48dba499425b0d908df0"
    - "tycho.page.b8d02f9b40c44c729e2b99e01a8b0dbf"
    - "tycho.page.f3b4041502a7403bbc63bb2611eb5c0f"
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

# V01/C06 — Capacity, operational constraints and total cost

## Purpose and mission

Which hard gates and team/budget limits invalidate otherwise appealing options? This chapter owns that question within requirements, quality attributes and architecture fundamentals. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Reject candidates that exceed an explicit operating, recovery, staffing or total-cost constraint before ranking attractive features.

A low instance price can conceal migration, dual-running and rollback costs; uncertain inputs must remain uncertain instead of becoming precise forecasts. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](operational-constraints-and-total-cost-gates.md) | Which hard gates and team/budget limits invalidate otherwise appealing options? |
| [Feasibility before preference scoring](feasibility-gates.md) | Which hard constraint makes a candidate inadmissible regardless of its score? |
| [Lifecycle cost and sensitivity](lifecycle-cost.md) | Which migration, dual-running and rollback costs can reverse a cost comparison? |
| [Operating capability and readiness](operating-capacity.md) | Which capacity, ownership and recovery constraints must be demonstrated before adoption? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V01 — Requirements, quality attributes and architecture fundamentals](../README.md) |
| Previous | [V01/C05 — Architecture descriptions and decision records](../c05/README.md) |
| Next | [V02/C01 — Layered, modular and ports-and-adapters design](../../v02/c01/README.md) |
| Prerequisite | [V01/C05 — Architecture descriptions and decision records](../c05/README.md) |
| Source reading | [Page-local evidence and versions](operational-constraints-and-total-cost-gates.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.76244dbe2bd44035b7154f821191f6f2:7 -->
## 7. Source-to-claim ledger and limitations

| Inspected public reference | Narrow support | Not established |
|---|---|---|
| [arc42 §2 — Architecture Constraints](https://docs.arc42.org/section-2/) | Technical/organizational conventions and limits constrain designs | Real constraints for any production system |
| [AWS Cost Optimization design principles](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) | Attribution, resource consumption and outcome unit economics | Actual provider prices or this example's operating cost |
| [Tycho requirements/workload decisions](../../v10/c01/requirements-and-workload-architecture-profiles.md) | Existing independent hard-gate decision reasoning | Accepted constraints or measured resource ceilings |
| [Tycho capacity/economic analysis](../../v07/c07/capacity-planning-and-cost-performance.md) | Original sensitivity analysis methodology | Real cost and capacity measurements |

Every workload, system, candidate, diagram and conclusion is invented for education. No security test, actual budget, backup exercise, execution evidence or independent review occurred. Metadata, exact chapter boundaries and final edition assembly remain pending.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.76244dbe2bd44035b7154f821191f6f2:9 -->
## Navigation

Proposed owner **V01/C06** in [outline](../../../PROPOSED-STRUCTURE.md), [application landing](../../../application/README.md). Prerequisites [system context](../c01/problem-framing-and-system-boundaries.md), [quality drivers](../c03/quality-drivers-and-architecture-views.md), [workload demand](../c02/workload-demand-and-arrival-models.md). Next [technical capacity cost](../../v07/c07/capacity-planning-and-cost-performance.md) and [alternative decision gates](../../v10/c04/architecture-alternatives-experiments-and-adrs.md).
<!-- /tycho-question-source -->
