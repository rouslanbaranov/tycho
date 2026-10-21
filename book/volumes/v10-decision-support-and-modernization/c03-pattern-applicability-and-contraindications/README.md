---
metadata_version: 1
id: "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
kind: "chapter"
parent_id: "tycho.volume.e826731e3543471f94d5eb9af68cbfa7"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c03-pattern-applicability-and-contraindications/README.md"
title: "V10/C03 — Pattern applicability and contraindications"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which evidence, preconditions and failures bound a pattern's usefulness? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Which evidence, preconditions and failures bound a pattern's usefulness?"
  prerequisites:
    - "tycho.chapter.8605018cb9224f99bea9dd49be2b79e3"
  related_ids:
    - "tycho.page.35d5be6a4e074758afff95bf3ec68bc5"
    - "tycho.page.2176fe3dcdf24a199d1656cba602e8e1"
    - "tycho.page.2debc63415184b02ad0a144b2649c171"
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

# V10/C03 — Pattern applicability and contraindications

## Purpose and mission

Which evidence, preconditions and failures bound a pattern's usefulness? This chapter owns that question within decision support and modernization playbooks. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Treat a pattern as a conditional intervention with explicit prerequisites, contraindications and reversal evidence.

A cache and a service split can both fail the same serialized hot-key workload; naming a pattern does not establish causal fit. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](pattern-applicability-and-contraindications.md) | Which evidence, preconditions and failures bound a pattern's usefulness? |
| [Conditional applicability cards and baseline fit](pattern-cards.md) | Which invariant, workload and operating precondition makes a pattern useful? |
| [Contraindications and transition falsification](contraindications-transition.md) | Which counterexample or migration cost should reverse the pattern choice? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V10 — Decision support and modernization playbooks](../README.md) |
| Previous | [V10/C02 — Baseline analysis for existing software](../c02-baseline-analysis-for-existing-software/README.md) |
| Next | [V10/C04 — Alternatives, experiments and ADRs](../c04-alternatives-experiments-and-adrs/README.md) |
| Prerequisite | [V10/C02 — Baseline analysis for existing software](../c02-baseline-analysis-for-existing-software/README.md) |
| Source reading | [Page-local evidence and versions](pattern-applicability-and-contraindications.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.35d5be6a4e074758afff95bf3ec68bc5:8 -->
## 8. Source-to-claim ledger and review limits

| Reviewed independent public source | Narrow support | Limit |
|---|---|---|
| [Fowler, Microservice Trade-Offs (2015)](https://martinfowler.com/articles/microservice-trade-offs.html) | Independent deployment, boundaries and distributed/operational costs | Not proof that any particular project needs microservices |
| [SEI ATAM, Kazman et al. (1998)](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/) | Evaluating interacting quality attributes and design risks | Not an automated ranking or acceptance of this book's example |
| [Tycho module and style chapter](../../../application/architecture-styles-and-module-boundaries.md) | Canonical mechanism distinction for modular monolith/SOA/services | No executable modularity enforcement for fictional app |
| [Tycho caching chapter](../../../scaling/local-distributed-caching-and-invalidation.md) | Boundaries of the referenced caching pattern | No real-world performance values transferred to the example |

All matrix entries and the resource reservation example are original educational statements under explicit assumptions. No live workload, executed migration, independently reviewed pattern suitability, cost study or deployed architecture selection agent is claimed. Validation of a real decision requires source/version evidence and domain review.

**Navigation:** canonical **V10/C03** in the current edition; start at the [decision-support landing](../../../decisions/README.md). Next: [V10/C04 — alternatives, experiments and ADRs](../c04-alternatives-experiments-and-adrs/README.md).

<!-- /tycho-question-source -->
