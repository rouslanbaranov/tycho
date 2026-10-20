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
summary: "What must be isolated between clients, organizations and data owners? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "What must be isolated between clients, organizations and data owners?"
  prerequisites:
    - "tycho.chapter.4f7542e57fb74052a4a31cd4c4dce46a"
  related_ids:
    - "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
    - "tycho.page.31cda61d174248eaa326559d256ce352"
    - "tycho.page.6bbeb9533a324758a1b970471c5b04e1"
    - "tycho.page.c0dd410ffc6344b78e5a9c72589bf06f"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](authorization-boundaries-and-multitenancy.md) | What must be isolated between clients, organizations and data owners? |
| [Isolation dimensions and placement](isolation-axes.md) | How do domain, tenant, authorization and runtime isolation differ? |
| [Tenant-scoped effects and migration](tenant-effects.md) | Which cache, task and data-movement paths can bypass otherwise correct tenant scoping? |

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

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.31cda61d174248eaa326559d256ce352:7 -->
## 7. Source ledger, limitations and navigation

| Independent public source reviewed | Narrowly supports | Unverified |
|---|---|---|
| [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | Least privilege, deny-by-default and per-object checking | Actual app's correct enforcement |
| [OWASP Authorization Patterns](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Patterns_Cheat_Sheet.html) | Enforced object/tenant policy decisions near protected resource | End-to-end negative authorization test |
| [Microsoft Multitenant Tenancy Models](https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenancy-models) | Shared/dedicated/hybrid placement trade-offs | Suitability for invented libraries |

The software, names, diagrams, resources and attack cases are original invented examples. No policy/tenant/restore tests, deployed service, independent audit, actual cost comparison or final edition chapter metadata exists for this page.

**Navigation:** proposed **V02/C07** in [outline](../../../PROPOSED-STRUCTURE.md), [application landing](../../../application/README.md). Related [Domain ownership](../c02/domain-boundaries-data-ownership-and-contracts.md), [Identity and service isolation](../../v09/c05/identity-authorization-and-isolation.md), [Safe agent-accessible knowledge](../../v09/c07/safe-agent-access-and-knowledge-isolation.md), [Connection pool scaling](../../v03/c05/connection-pools-hikaricp-pgbouncer.md).

<!-- /tycho-question-source -->
