---
metadata_version: 1
id: "tycho.chapter.7031445877fb4f8d831d962d170521c8"
kind: "chapter"
parent_id: "tycho.volume.7e8f5fd0c9d94504b6dc74b9ae6c30f3"
canonical_path: "book/volumes/v02/c02/README.md"
title: "V02/C02 — Domain boundaries, data ownership and contracts"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "When should business capabilities form module or service boundaries?"
route_hints:
  questions:
    - "When should business capabilities form module or service boundaries?"
  prerequisites:
    - "tycho.chapter.c5f8456752f34dd6a5b6b5c7e3e14715"
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

# V02/C02 — Domain boundaries, data ownership and contracts

## Purpose and mission

When should business capabilities form module or service boundaries? This chapter owns that question within application boundaries and interaction contracts. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Assign each invariant and authoritative state transition to an owner before dividing storage or deployment.

Two teams using the same entity name can disagree on its legal transitions; schema agreement alone does not resolve ownership. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Domain boundaries, data ownership and contract evolution](domain-boundaries-data-ownership-and-contracts.md) | When should business capabilities form module or service boundaries? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Model behaviors and invariants before drawing ownership boxes](domain-boundaries-data-ownership-and-contracts.md#1-model-behaviors-and-invariants-before-drawing-ownership-boxes).
- [2. Authority and storage are separate concerns](domain-boundaries-data-ownership-and-contracts.md#2-authority-and-storage-are-separate-concerns).
- [Engineering walkthrough — Two teams change the same concept during a schema transition](domain-boundaries-data-ownership-and-contracts.md#engineering-walkthrough-two-teams-change-the-same-concept-during-a-schema-transition).
- [Applied M9 evidence: what transfers and what does not](domain-boundaries-data-ownership-and-contracts.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V02 — Application boundaries and interaction contracts](../README.md) |
| Previous | [V02/C01 — Layered, modular and ports-and-adapters design](../c01/README.md) |
| Next | [V02/C03 — Modular monolith and internal events](../c03/README.md) |
| Prerequisite | [V02/C01 — Layered, modular and ports-and-adapters design](../c01/README.md) |
| Source reading | [Page-local evidence and versions](domain-boundaries-data-ownership-and-contracts.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
