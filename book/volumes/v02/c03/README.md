---
metadata_version: 1
id: "tycho.chapter.5de52a840c14448c946a65c924f28487"
kind: "chapter"
parent_id: "tycho.volume.7e8f5fd0c9d94504b6dc74b9ae6c30f3"
canonical_path: "book/volumes/v02/c03/README.md"
title: "V02/C03 — Modular monolith and internal events"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which coupling and deployment constraints fit an in-process architecture?"
route_hints:
  questions:
    - "Which coupling and deployment constraints fit an in-process architecture?"
  prerequisites:
    - "tycho.chapter.7031445877fb4f8d831d962d170521c8"
  related_ids:
    - "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
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

# V02/C03 — Modular monolith and internal events

## Purpose and mission

Which coupling and deployment constraints fit an in-process architecture? This chapter owns that question within application boundaries and interaction contracts. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Use enforced module contracts to retain useful local transactions and make internal event durability explicit.

An after-commit callback is not a durable external delivery mechanism; process death can separate a committed change from its notification. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Modular monolith architecture and internal domain events](modular-monolith-and-internal-events.md) | Which coupling and deployment constraints fit an in-process architecture? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Stable module boundaries before event buses](modular-monolith-and-internal-events.md#1-stable-module-boundaries-before-event-buses).
- [2. Original synthetic example: community workshop reservation](modular-monolith-and-internal-events.md#2-original-synthetic-example-community-workshop-reservation).
- [Engineering walkthrough — An internal event that survives neither process death nor commit](modular-monolith-and-internal-events.md#engineering-walkthrough-an-internal-event-that-survives-neither-process-death-nor-commit).
- [Applied M9 evidence: what transfers and what does not](modular-monolith-and-internal-events.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

- [V04/C05 — Outbox, inbox, sagas and durable workflows](../../v04/c05/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V02 — Application boundaries and interaction contracts](../README.md) |
| Previous | [V02/C02 — Domain boundaries, data ownership and contracts](../c02/README.md) |
| Next | [V02/C04 — SOA, microservices and distributed boundaries](../c04/README.md) |
| Prerequisite | [V02/C02 — Domain boundaries, data ownership and contracts](../c02/README.md) |
| Source reading | [Page-local evidence and versions](modular-monolith-and-internal-events.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
