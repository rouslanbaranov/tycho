---
metadata_version: 1
id: "tycho.chapter.5426707ddf264b758016aafe71f342b7"
kind: "chapter"
parent_id: "tycho.volume.7e8f5fd0c9d94504b6dc74b9ae6c30f3"
canonical_path: "book/volumes/v02/c07/README.md"
title: "V02/C07 — Authorization boundaries and multitenancy"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What must be isolated between clients, organizations and data owners?"
route_hints:
  questions:
    - "What must be isolated between clients, organizations and data owners?"
  prerequisites:
    - "tycho.chapter.4f7542e57fb74052a4a31cd4c4dce46a"
  related_ids:
    - "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
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

# V02/C07 — Authorization boundaries and multitenancy

## Purpose and mission

What must be isolated between clients, organizations and data owners? This chapter owns that question within application boundaries and interaction contracts. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Design tenant identity, authorization, resource sharing and data placement as separate but composing boundaries.

A tenant-aware query does not protect a wrongly scoped cache or background task; isolation must hold across the complete effect path. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Authorization boundaries and multitenancy: domain ownership and isolation](authorization-boundaries-and-multitenancy.md) | What must be isolated between clients, organizations and data owners? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Separate four isolation dimensions](authorization-boundaries-and-multitenancy.md#1-separate-four-isolation-dimensions).
- [2. Fictional example: community equipment libraries](authorization-boundaries-and-multitenancy.md#2-fictional-example-community-equipment-libraries).
- [Engineering walkthrough — Tenant isolation across four non-equivalent layers](authorization-boundaries-and-multitenancy.md#engineering-walkthrough-tenant-isolation-across-four-non-equivalent-layers).
- [Applied M9 evidence: what transfers and what does not](authorization-boundaries-and-multitenancy.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

- [V09/C05 — Identity, authorization and threat modeling](../../v09/c05/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V02 — Application boundaries and interaction contracts](../README.md) |
| Previous | [V02/C06 — Integration adapters and anti-corruption boundaries](../c06/README.md) |
| Next | [V03/C01 — Threads, tasks and coordination](../../v03/c01/README.md) |
| Prerequisite | [V02/C06 — Integration adapters and anti-corruption boundaries](../c06/README.md) |
| Source reading | [Page-local evidence and versions](authorization-boundaries-and-multitenancy.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
