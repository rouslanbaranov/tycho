---
metadata_version: 1
id: "tycho.chapter.809c2f1d12e544b38af2460b80d6d24e"
kind: "chapter"
parent_id: "tycho.volume.e826731e3543471f94d5eb9af68cbfa7"
canonical_path: "book/volumes/v10/c04/README.md"
title: "V10/C04 — Alternatives, experiments and ADRs"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which hypotheses distinguish feasible options under hard constraints? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Which hypotheses distinguish feasible options under hard constraints?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.page.f05854fcc406435bbf38a192bc7ab2f1"
    - "tycho.page.7079edf1ceeb4b1594083edf7a2c680e"
    - "tycho.page.a5285941dcba43d5a6a7c091cb4c99f9"
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

# V10/C04 — Alternatives, experiments and ADRs

## Purpose and mission

Which hypotheses distinguish feasible options under hard constraints? This chapter owns that question within decision support and modernization playbooks. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Compare feasible alternatives through experiments that can reverse the decision and record consequences in an ADR.

A changed hard requirement can invalidate a preferred score; a decision record should preserve why reconsideration is necessary. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](architecture-alternatives-experiments-and-adrs.md) | Which hypotheses distinguish feasible options under hard constraints? |
| [Alternatives and discriminating hypotheses](decision-discriminators.md) | Which observation would make one feasible option preferable to another? |
| [Sensitivity, consequences and stopping rules](adr-sensitivity.md) | When must a scored preference or recorded ADR be reconsidered? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V10 — Decision support and modernization playbooks](../README.md) |
| Previous | [V10/C03 — Pattern applicability and contraindications](../c03/README.md) |
| Next | [V10/C05 — Target architecture versus transition states](../c05/README.md) |
| Prerequisite | [V10/C03 — Pattern applicability and contraindications](../c03/README.md) |
| Source reading | [Page-local evidence and versions](architecture-alternatives-experiments-and-adrs.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.f05854fcc406435bbf38a192bc7ab2f1:7 -->
## 7. Public reference ledger and limitations

| Inspected independent source, 2026-10-19 | Supports | Does not establish |
|---|---|---|
| [arc42 §9 — Architecture Decisions](https://docs.arc42.org/section-9/) | Context, criteria, alternatives, statuses, rationale and consequences | Validity of the book's synthetic ratings |
| [arc42 §10 — Quality Requirements](https://docs.arc42.org/section-10/) | Measurable quality scenarios as inputs to decisions | Real SLO or measured acceptance result |
| [Tycho candidate comparison method](../../../../authoring/models/candidate-comparison-adr.md) | Reusable authored screening/ADR structure | An automatically computed or approved architectural choice |
| [Tycho performance experiments](../../../performance/workload-profiles-and-capacity-experiments.md) | Measurement boundaries and falsifiable trial design | Any real workload observation |

All sample identities, outcomes, weights and experiments here are **independent original synthetic content**. No system was evaluated or benchmarked. Real technical review, claim-by-claim public-source check and final chapter/page metadata remain pending.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.f05854fcc406435bbf38a192bc7ab2f1:8 -->
## Navigation

Proposed home: **V10/C04** in [proposed contents](../../../PROPOSED-STRUCTURE.md). Current landing: [Decision support](../../../decisions/README.md). Read [Requirements/workload](../c01/requirements-and-workload-architecture-profiles.md), [Pattern applicability](../c03/pattern-applicability-and-contraindications.md), [Legacy baseline](../c02/legacy-baseline-and-modernization-evidence.md), then [target and transition planning](../../../../authoring/models/target-transition-architecture.md) for implementation readiness.

<!-- /tycho-question-source -->
