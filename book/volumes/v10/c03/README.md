---
metadata_version: 1
id: "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
kind: "chapter"
parent_id: "tycho.volume.e826731e3543471f94d5eb9af68cbfa7"
canonical_path: "book/volumes/v10/c03/README.md"
title: "V10/C03 — Pattern applicability and contraindications"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which evidence, preconditions and failures bound a pattern's usefulness?"
route_hints:
  questions:
    - "Which evidence, preconditions and failures bound a pattern's usefulness?"
  prerequisites:
    - "tycho.chapter.8605018cb9224f99bea9dd49be2b79e3"
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

# V10/C03 — Pattern applicability and contraindications

## Purpose and mission

Which evidence, preconditions and failures bound a pattern's usefulness? This chapter owns that question within decision support and modernization playbooks. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Treat a pattern as a conditional intervention with explicit prerequisites, contraindications and reversal evidence.

A cache and a service split can both fail the same serialized hot-key workload; naming a pattern does not establish causal fit. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Architecture patterns: applicability, contraindications and evidence gates](pattern-applicability-and-contraindications.md) | Which evidence, preconditions and failures bound a pattern's usefulness? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. A pattern card answers a decision, not a vocabulary question](pattern-applicability-and-contraindications.md#1-a-pattern-card-answers-a-decision-not-a-vocabulary-question).
- [2. Evaluate the baseline before choosing a target](pattern-applicability-and-contraindications.md#2-evaluate-the-baseline-before-choosing-a-target).
- [Engineering walkthrough — Two attractive patterns fail the same hot-key workload](pattern-applicability-and-contraindications.md#engineering-walkthrough-two-attractive-patterns-fail-the-same-hot-key-workload).
- [Applied M9 evidence: what transfers and what does not](pattern-applicability-and-contraindications.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V10 — Decision support and modernization playbooks](../README.md) |
| Previous | [V10/C02 — Baseline analysis for existing software](../c02/README.md) |
| Next | [V10/C04 — Alternatives, experiments and ADRs](../c04/README.md) |
| Prerequisite | [V10/C02 — Baseline analysis for existing software](../c02/README.md) |
| Source reading | [Page-local evidence and versions](pattern-applicability-and-contraindications.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
