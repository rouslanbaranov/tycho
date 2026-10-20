---
metadata_version: 1
id: "tycho.chapter.8605018cb9224f99bea9dd49be2b79e3"
kind: "chapter"
parent_id: "tycho.volume.e826731e3543471f94d5eb9af68cbfa7"
canonical_path: "book/volumes/v10/c02/README.md"
title: "V10/C02 — Baseline analysis for existing software"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which observed limitations justify changing the architecture?"
route_hints:
  questions:
    - "Which observed limitations justify changing the architecture?"
  prerequisites:
    - "tycho.chapter.289750444f8040d292a474e3876046a1"
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

# V10/C02 — Baseline analysis for existing software

## Purpose and mission

Which observed limitations justify changing the architecture? This chapter owns that question within decision support and modernization playbooks. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Describe observed legacy behavior and limitations before assigning expected benefits to a target architecture.

Old technology is not itself evidence of a defect; retaining and improving the baseline must remain a real alternative. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Legacy system baseline and modernization evidence: deciding what to keep](legacy-baseline-and-modernization-evidence.md) | Which observed limitations justify changing the architecture? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Old software is not itself an architecture defect](legacy-baseline-and-modernization-evidence.md#1-old-software-is-not-itself-an-architecture-defect).
- [2. Collect a baseline as an evidence-bearing architecture model](legacy-baseline-and-modernization-evidence.md#2-collect-a-baseline-as-an-evidence-bearing-architecture-model).
- [Engineering walkthrough — Observed legacy baseline versus hypothetical future benefit](legacy-baseline-and-modernization-evidence.md#engineering-walkthrough-observed-legacy-baseline-versus-hypothetical-future-benefit).
- [Applied M9 evidence: what transfers and what does not](legacy-baseline-and-modernization-evidence.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V10 — Decision support and modernization playbooks](../README.md) |
| Previous | [V10/C01 — Architecture requirement and workload profiles](../c01/README.md) |
| Next | [V10/C03 — Pattern applicability and contraindications](../c03/README.md) |
| Prerequisite | [V10/C01 — Architecture requirement and workload profiles](../c01/README.md) |
| Source reading | [Page-local evidence and versions](legacy-baseline-and-modernization-evidence.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
