---
metadata_version: 1
id: "tycho.chapter.c5f8456752f34dd6a5b6b5c7e3e14715"
kind: "chapter"
parent_id: "tycho.volume.7e8f5fd0c9d94504b6dc74b9ae6c30f3"
canonical_path: "book/volumes/v02/c01/README.md"
title: "V02/C01 — Layered, modular and ports-and-adapters design"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How are dependencies directed and replaceable?"
route_hints:
  questions:
    - "How are dependencies directed and replaceable?"
  prerequisites:
    - "tycho.chapter.9d4f989ec9304e418f60f1ad7248094a"
    - "tycho.chapter.3d34f0b431814c9fa879a355029af2a9"
    - "tycho.chapter.bbfd14751d274868b152ba431dc904c9"
  related_ids: []
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
updated_at: "2026-10-20"
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

| Page | Owning question |
|---|---|
| [Layered, hexagonal and ports-and-adapters architecture](layered-hexagonal-ports-and-adapters.md) | How are dependencies directed and replaceable? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Layered design states a dependency policy](layered-hexagonal-ports-and-adapters.md#1-layered-design-states-a-dependency-policy).
- [2. A port is an application contract, not automatically a network port](layered-hexagonal-ports-and-adapters.md#2-a-port-is-an-application-contract-not-automatically-a-network-port).
- [Engineering walkthrough — The same adapter error in local and remote architectures](layered-hexagonal-ports-and-adapters.md#engineering-walkthrough-the-same-adapter-error-in-local-and-remote-architectures).
- [Applied M9 evidence: what transfers and what does not](layered-hexagonal-ports-and-adapters.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V02 — Application boundaries and interaction contracts](../README.md) |
| Previous | [V01/C06 — Capacity, operational constraints and total cost](../../v01/c06/README.md) |
| Next | [V02/C02 — Domain boundaries, data ownership and contracts](../c02/README.md) |
| Prerequisite | [V01/C01 — Problem framing and system boundaries](../../v01/c01/README.md) |
| Prerequisite | [V01/C03 — Quality attributes and trade-offs](../../v01/c03/README.md) |
| Prerequisite | [V01/C06 — Capacity, operational constraints and total cost](../../v01/c06/README.md) |
| Source reading | [Page-local evidence and versions](layered-hexagonal-ports-and-adapters.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
