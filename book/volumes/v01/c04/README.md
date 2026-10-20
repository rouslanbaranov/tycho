---
metadata_version: 1
id: "tycho.chapter.ee2cd95003ab4018a9d49e2ff0b6b2f4"
kind: "chapter"
parent_id: "tycho.volume.4d10f5c93f3b4356a553c8732e513a38"
canonical_path: "book/volumes/v01/c04/README.md"
title: "V01/C04 — Evidence, hypotheses and architecture experiments"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What do sources, estimates, simulations and measurements actually prove? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "What do sources, estimates, simulations and measurements actually prove?"
  prerequisites:
    - "tycho.chapter.3d34f0b431814c9fa879a355029af2a9"
  related_ids:
    - "tycho.page.a2cd4465792a4740aa5150ad248fd420"
    - "tycho.page.d8118d40313143e4ac47323274fbb594"
    - "tycho.page.3a5cdaf97d0b4e51ae5828507f033dd0"
    - "tycho.page.dff5d6affea243cca3c426d04d290802"
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

# V01/C04 — Evidence, hypotheses and architecture experiments

## Purpose and mission

What do sources, estimates, simulations and measurements actually prove? This chapter owns that question within requirements, quality attributes and architecture fundamentals. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Keep published semantics, synthetic arithmetic, hypotheses and observed experiments as distinct evidence classes with different permissible conclusions.

A cache experiment can improve latency while failing freshness; the result rejects that configuration rather than proving a universal claim about caching. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](architecture-evidence-hypotheses-and-experiments.md) | What do sources, estimates, simulations and measurements actually prove? |
| [Evidence classes and competing hypotheses](evidence-hypotheses.md) | Which evidence class supports a claim and which alternative explanation remains possible? |
| [Discriminating architecture experiments](experiment-contract.md) | What observation would distinguish cache benefit from query repair? |
| [Negative evidence and stopping rules](negative-results.md) | When should an attractive candidate be rejected or research stop? |


## Additional mechanism and project routes

These independently scoped pages extend the chapter without replacing its original walkthrough or source ledger.

| Page | Owning question |
| --- | --- |
| [Distributed protocol verification](protocol-correctness.md) | How can histories, invariants and executable models expose a distributed correctness defect? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V01 — Requirements, quality attributes and architecture fundamentals](../README.md) |
| Previous | [V01/C03 — Quality attributes and trade-offs](../c03/README.md) |
| Next | [V01/C05 — Architecture descriptions and decision records](../c05/README.md) |
| Prerequisite | [V01/C03 — Quality attributes and trade-offs](../c03/README.md) |
| Source reading | [Page-local evidence and versions](architecture-evidence-hypotheses-and-experiments.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.a2cd4465792a4740aa5150ad248fd420:7 -->
## 7. Public ledger and limitations

| Public source consulted | Supported narrow principle | Unproven |
|---|---|---|
| [arc42 Quality Requirements §10](https://docs.arc42.org/section-10/) | Explicit, measurable quality scenarios | Any workload's achieved SLO |
| [arc42 Architecture Decisions §9](https://docs.arc42.org/section-9/) | Alternatives, rationale and decisions | An accepted option for the fictional trail app |
| [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) | Service-indicator boundaries and SLO methodology | Actual user latency/availability |
| [Tycho benchmark validity](../../v07/c03/load-testing-and-benchmark-validity.md) | Generator and observation limitations | A performed controlled test |

The trial, metric hypotheses, workload, figure and failure consequences are original teaching material. There are no run results, third-party architecture approvals or measured improvements. Full source-by-claim audit, book metadata and final volume organization remain outstanding.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.a2cd4465792a4740aa5150ad248fd420:9 -->
## Navigation

Proposed **V01/C04** in [planned outline](../../../PROPOSED-STRUCTURE.md); current [application landing](../../../application/README.md). Prerequisite [system context](../c01/problem-framing-and-system-boundaries.md), [quality drivers](../c03/quality-drivers-and-architecture-views.md). Continue to [architecture alternatives/ADRs](../../v10/c04/architecture-alternatives-experiments-and-adrs.md), [benchmark methods](../../v07/c03/load-testing-and-benchmark-validity.md), and [capacity experiments](../../../performance/workload-profiles-and-capacity-experiments.md).
<!-- /tycho-question-source -->
