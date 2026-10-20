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
summary: "Which hypotheses distinguish feasible options under hard constraints?"
route_hints:
  questions:
    - "Which hypotheses distinguish feasible options under hard constraints?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
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

# V10/C04 — Alternatives, experiments and ADRs

## Purpose and mission

Which hypotheses distinguish feasible options under hard constraints? This chapter owns that question within decision support and modernization playbooks. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Compare feasible alternatives through experiments that can reverse the decision and record consequences in an ADR.

A changed hard requirement can invalidate a preferred score; a decision record should preserve why reconsideration is necessary. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Architecture alternatives, discriminating experiments and decision records](architecture-alternatives-experiments-and-adrs.md) | Which hypotheses distinguish feasible options under hard constraints? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. A precise problem statement comes before alternatives](architecture-alternatives-experiments-and-adrs.md#1-a-precise-problem-statement-comes-before-alternatives).
- [2. Enumerate a genuine retained/simple option](architecture-alternatives-experiments-and-adrs.md#2-enumerate-a-genuine-retainedsimple-option).
- [Engineering walkthrough — A hard requirement reverses a previously preferred ADR](architecture-alternatives-experiments-and-adrs.md#engineering-walkthrough-a-hard-requirement-reverses-a-previously-preferred-adr).
- [Applied M9 evidence: what transfers and what does not](architecture-alternatives-experiments-and-adrs.md#applied-m9-evidence-what-transfers-and-what-does-not).

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
