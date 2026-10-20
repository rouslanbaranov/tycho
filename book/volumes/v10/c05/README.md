---
metadata_version: 1
id: "tycho.chapter.0a5e430b39094337aa6a211d9b5b4bd0"
kind: "chapter"
parent_id: "tycho.volume.e826731e3543471f94d5eb9af68cbfa7"
canonical_path: "book/volumes/v10/c05/README.md"
title: "V10/C05 — Target architecture versus transition states"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What is safe during coexistence, migration, rollback and recovery?"
route_hints:
  questions:
    - "What is safe during coexistence, migration, rollback and recovery?"
  prerequisites:
    - "tycho.chapter.809c2f1d12e544b38af2460b80d6d24e"
  related_ids:
    - "tycho.chapter.3d0f6dd1e8e94cd397326e129b5c287f"
    - "tycho.chapter.7d434d1a41e142d38bb729ee124ac548"
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

# V10/C05 — Target architecture versus transition states

## Purpose and mission

What is safe during coexistence, migration, rollback and recovery? This chapter owns that question within decision support and modernization playbooks. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Plan coexistence, authority transfer, no-return conditions and recovery as real intermediate operating states.

Rolling back an image cannot undo new-only durable effects; transition safety requires a separate forward-repair path. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Target architecture versus transition states: coexistence, reversibility and recovery](target-and-transition-architecture-states.md) | What is safe during coexistence, migration, rollback and recovery? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Keep five distinct contracts](target-and-transition-architecture-states.md#1-keep-five-distinct-contracts).
- [2. The fictional migration: moving a public catalogue read model](target-and-transition-architecture-states.md#2-the-fictional-migration-moving-a-public-catalogue-read-model).
- [Engineering walkthrough — New-only persisted effects turn image rollback into forward repair](target-and-transition-architecture-states.md#engineering-walkthrough-new-only-persisted-effects-turn-image-rollback-into-forward-repair).
- [Applied M9 evidence: what transfers and what does not](target-and-transition-architecture-states.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

- [V05/C06 — Schema evolution, data migration and retention](../../v05/c06/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.
- [V08/C05 — Backward-compatible database change](../../v08/c05/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V10 — Decision support and modernization playbooks](../README.md) |
| Previous | [V10/C04 — Alternatives, experiments and ADRs](../c04/README.md) |
| Next | [V10/C06 — Search and question routes for architecture agents](../c06/README.md) |
| Prerequisite | [V10/C04 — Alternatives, experiments and ADRs](../c04/README.md) |
| Source reading | [Page-local evidence and versions](target-and-transition-architecture-states.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
