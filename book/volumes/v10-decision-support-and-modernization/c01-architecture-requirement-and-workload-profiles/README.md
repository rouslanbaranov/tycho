---
metadata_version: 1
id: "tycho.chapter.289750444f8040d292a474e3876046a1"
kind: "chapter"
parent_id: "tycho.volume.e826731e3543471f94d5eb9af68cbfa7"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c01-architecture-requirement-and-workload-profiles/README.md"
title: "V10/C01 — Architecture requirement and workload profiles"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What inputs are required before comparing candidate patterns? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "What inputs are required before comparing candidate patterns?"
  prerequisites:
    - "tycho.chapter.9d4f989ec9304e418f60f1ad7248094a"
    - "tycho.chapter.316b50ac3db440ae82c0986b896ff468"
    - "tycho.chapter.3d34f0b431814c9fa879a355029af2a9"
    - "tycho.chapter.ee2cd95003ab4018a9d49e2ff0b6b2f4"
    - "tycho.chapter.abcbb298887b49e79525ca00fead8926"
    - "tycho.chapter.bbfd14751d274868b152ba431dc904c9"
  related_ids:
    - "tycho.page.868027aee4884210bea1d8a6542fbfb0"
    - "tycho.page.84fa4a7505904bb2a492be1593690ed2"
    - "tycho.page.4e96abb6d4504ef1b09cbc355485108a"
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

# V10/C01 — Architecture requirement and workload profiles

## Purpose and mission

What inputs are required before comparing candidate patterns? This chapter owns that question within decision support and modernization playbooks. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Capture outcome, workload, invariant, constraint and evidence inputs before comparing architecture candidates.

A complete-looking questionnaire with unknown hot-key behavior or recovery ownership still cannot support a definite recommendation. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](requirements-and-workload-architecture-profiles.md) | What inputs are required before comparing candidate patterns? |
| [Outcomes, constraints and workload intake](intake-invariants.md) | Which inputs must be explicit before candidate architectures are compared? |
| [Adversarial requirements and candidate screening](evidence-screening.md) | Which missing evidence or hard gate must block a premature recommendation? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V10 — Decision support and modernization playbooks](../README.md) |
| Previous | [V09/C07 — Safety, isolation and privacy in agent-accessible services](../../v09-observability-security-and-operations/c07-safety-isolation-and-privacy-in-agent-accessible-services/README.md) |
| Next | [V10/C02 — Baseline analysis for existing software](../c02-baseline-analysis-for-existing-software/README.md) |
| Prerequisite | [V01/C01 — Problem framing and system boundaries](../../v01-requirements-and-architecture/c01-problem-framing/README.md) |
| Prerequisite | [V01/C02 — Workload and demand models](../../v01-requirements-and-architecture/c02-workload-and-demand-models/README.md) |
| Prerequisite | [V01/C03 — Quality attributes and trade-offs](../../v01-requirements-and-architecture/c03-quality-attributes-and-trade-offs/README.md) |
| Prerequisite | [V01/C04 — Evidence, hypotheses and architecture experiments](../../v01-requirements-and-architecture/c04-evidence-hypotheses-and-architecture-experiments/README.md) |
| Prerequisite | [V01/C05 — Architecture descriptions and decision records](../../v01-requirements-and-architecture/c05-architecture-descriptions-and-decision-records/README.md) |
| Prerequisite | [V01/C06 — Capacity, operational constraints and total cost](../../v01-requirements-and-architecture/c06-capacity-operational-constraints-and-total-cost/README.md) |
| Source reading | [Page-local evidence and versions](requirements-and-workload-architecture-profiles.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.868027aee4884210bea1d8a6542fbfb0:8 -->
## 8. Source-to-claim ledger, limitations and next research

| Inspected independent public evidence | Narrow use | Not established |
|---|---|---|
| [arc42 §1 — Introduction and Goals](https://docs.arc42.org/section-1/) | Stakeholder expectations, fundamental requirements and architectural goals | Any specific system's actual workload |
| [arc42 §3 — Context and Scope](https://docs.arc42.org/section-3/) | Business and technical interface boundaries | Runtime isolation or measured behavior |
| [arc42 §10 — Quality Requirements](https://docs.arc42.org/section-10/) | Measurable usage/change scenarios | Universal numerical SLOs |
| [SEI, Kazman et al., ATAM, CMU/SEI-98-TR-008 (1998)](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/) | Evaluation of competing architectural quality attributes | ATAM assessment of this illustrative booking design |
| [Tycho queueing study](../../v07-performance-scale-and-resilience/c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md) | Distinction between offered/completed load and stable-average modeling | Validation of synthetic 100/s demand |

All booking numbers, diagrams, decision tables, tests, hypotheses and outcomes are **original invented teaching material**. They were not exercised on a running service. No independent review, real cost study, workload collection or whole-volume coverage is claimed. For an actual project, obtain consented stakeholder requirements and telemetry before moving a provisional decision to accepted. The method's machine-readable integration remains independent future work.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.868027aee4884210bea1d8a6542fbfb0:10 -->
## Navigation

- Planned owner: **V10/C01** in [book outline](../../../PROPOSED-STRUCTURE.md); current section [System Design decision support](../../../decisions/README.md).
- Prerequisite: [Quality drivers](../../v01-requirements-and-architecture/c03-quality-attributes-and-trade-offs/quality-drivers-and-architecture-views.md); [Queueing](../../v07-performance-scale-and-resilience/c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md).
- Next concepts: [Legacy evolution](../../../application/architecture-evolution-and-extraction.md); [Cross-domain ADR decisions](../c07-cross-domain-worked-comparisons-and-unresolved-cases/cross-domain-modernization-and-adr-examples.md); [Safe rollout](../../../delivery/safe-rollout-and-recovery.md).
- Supporting non-book tooling: [Requirements/workload template](../../../../authoring/models/requirements-workload-profile.md), [Candidate ADR format](../../../../authoring/models/candidate-comparison-adr.md).
<!-- /tycho-question-source -->
