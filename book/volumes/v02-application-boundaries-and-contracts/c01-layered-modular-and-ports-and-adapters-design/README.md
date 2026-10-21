---
metadata_version: 1
id: "tycho.chapter.c5f8456752f34dd6a5b6b5c7e3e14715"
kind: "chapter"
parent_id: "tycho.volume.7e8f5fd0c9d94504b6dc74b9ae6c30f3"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c01-layered-modular-and-ports-and-adapters-design/README.md"
title: "V02/C01 — Layered, modular and ports-and-adapters design"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How are dependencies directed and replaceable? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How are dependencies directed and replaceable?"
  prerequisites:
    - "tycho.chapter.9d4f989ec9304e418f60f1ad7248094a"
    - "tycho.chapter.3d34f0b431814c9fa879a355029af2a9"
    - "tycho.chapter.bbfd14751d274868b152ba431dc904c9"
  related_ids:
    - "tycho.page.77b512c4e2e946bd92d70b4a714600c8"
    - "tycho.page.f375bfcea48045d2a5d1f46014ca7758"
    - "tycho.page.65f9616c034643f9bf5f297037f027e4"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.hexagonal"
  claim_ids: []
  status: "source-linked"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---

# V02/C01 — Layered, modular and ports-and-adapters design

## Purpose and mission

How are dependencies directed and replaceable? This chapter owns that question within application boundaries and interaction contracts. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Direct source dependencies through application contracts while keeping runtime failure boundaries explicit.

Replacing a local adapter with a remote call changes deadlines and ambiguous outcomes even if the port signature is unchanged. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](layered-hexagonal-ports-and-adapters.md) | How are dependencies directed and replaceable? |
| [Dependency direction and application ports](dependencies-ports.md) | What does a port isolate and which runtime failure boundary remains? |
| [Adapter substitution and falsification](adapter-scenarios.md) | How do local and remote adapter replacements change the tests and operational obligations? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V02 — Application boundaries and interaction contracts](../README.md) |
| Previous | [V01/C06 — Capacity, operational constraints and total cost](../../v01-requirements-and-architecture/c06-capacity-operational-constraints-and-total-cost/README.md) |
| Next | [V02/C02 — Domain boundaries, data ownership and contracts](../c02-domain-boundaries-data-ownership-and-contracts/README.md) |
| Prerequisite | [V01/C01 — Problem framing and system boundaries](../../v01-requirements-and-architecture/c01-problem-framing/README.md) |
| Prerequisite | [V01/C03 — Quality attributes and trade-offs](../../v01-requirements-and-architecture/c03-quality-attributes-and-trade-offs/README.md) |
| Prerequisite | [V01/C06 — Capacity, operational constraints and total cost](../../v01-requirements-and-architecture/c06-capacity-operational-constraints-and-total-cost/README.md) |
| Source reading | [Page-local evidence and versions](layered-hexagonal-ports-and-adapters.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.77b512c4e2e946bd92d70b4a714600c8:8 -->
## 8. Source-to-claim ledger and limits

| Public independently inspected source | Narrow support | Not established |
|---|---|---|
| [Cockburn, *Hexagonal Architecture* (2005)](https://alistair.cockburn.us/hexagonal-architecture) | Driving/driven use cases, ports/adapters and isolation from external devices | Correctness of a fictional application's port layout |
| [Fowler/Lewis, *Microservices* (2014)](https://www.martinfowler.com/articles/microservices.html) | Distinction between one deployable and independently deployed collaborators | That a port should become its own service |
| [Existing Tycho application-style research](../../../application/architecture-styles-and-module-boundaries.md) | Earlier bounded treatment of module/deployment axes | An independently reviewed or compiler-enforced boundary |

The synthetic project, figure, tables and acceptance protocols are original. No executable module
architecture, real workload, interface fixture or claim-by-claim human audit was performed. Volume,
chapter and page IDs and frontmatter are canonical in V02.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.77b512c4e2e946bd92d70b4a714600c8:9 -->
### Archived proposal-era navigation

This retained proposal-era route is historical. Current navigation is the
"Navigation and prerequisites" table above; the original outline links are not
repeated.
<!-- /tycho-question-source -->
