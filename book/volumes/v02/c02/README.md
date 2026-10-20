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
summary: "When should business capabilities form module or service boundaries? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "When should business capabilities form module or service boundaries?"
  prerequisites:
    - "tycho.chapter.c5f8456752f34dd6a5b6b5c7e3e14715"
  related_ids:
    - "tycho.page.4681b3ba9e234c46bdb4b5993634b0e3"
    - "tycho.page.55c22c6b24ff456a95dd9cc3d71ca238"
    - "tycho.page.91c10dd544b441ddb940aaee24825638"
    - "tycho.page.461b24a5b47b4b8e82d37125cac20c8d"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](domain-boundaries-data-ownership-and-contracts.md) | When should business capabilities form module or service boundaries? |
| [Domain semantics and authoritative ownership](domain-authority.md) | When do shared names conceal different invariants and owners? |
| [Semantic adapters and evolving contracts](boundary-evolution.md) | How can incompatible domain meanings evolve without an atomic release? |
| [Ownership, isolation and boundary validation](ownership-isolation.md) | Which authorization and invariant tests establish a usable boundary? |

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

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.4681b3ba9e234c46bdb4b5993634b0e3:8 -->
## 8. Public evidence ledger and limits

| Independently inspected material | What it supports | What it does not prove |
|---|---|---|
| [Fowler — Bounded Context, 2014](https://martinfowler.com/bliki/BoundedContext.html) | Internally consistent domain languages and explicit relationships | Number of processes/databases for any application |
| [arc42 Context and Scope](https://docs.arc42.org/section-3/) | External business and technical exchanges in architecture descriptions | Tested integration between fictitious contexts |
| [Microsoft — Anti-corruption layer pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) | Translation protection and added latency/operations/consistency trade-offs | A validated schema mapping or real migration |
| [Tycho HTTP/RPC chapter](../c05/http-rpc-contracts-and-compatibility.md) | Explanation of request/response compatibility and effect identity | Actual contract-test execution |

The makerspace, rules, mappings, diagrams, decision alternatives and failures are original synthetic examples. The chapter does **not** claim complete reading of a proprietary DDD book, domain-expert review, executable contract tests or a measured distributed architecture. Canonical ownership and metadata for final edition are pending.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.4681b3ba9e234c46bdb4b5993634b0e3:9 -->
## Navigation

- Proposed V02/C02, currently [Application architecture landing](../../../application/README.md).
- Prerequisite: [System boundaries](../../v01/c01/problem-framing-and-system-boundaries.md), [architecture styles](../../../application/architecture-styles-and-module-boundaries.md).
- Further reading: [API/RPC compatibility](../c05/http-rpc-contracts-and-compatibility.md), [transaction and idempotency limits](../../../distributed/transactional-outbox-and-idempotency.md), [legacy transition](../../v10/c02/legacy-baseline-and-modernization-evidence.md).

<!-- /tycho-question-source -->
