---
metadata_version: 1
id: "tycho.chapter.4a3cbf0617e44be5b1e8d72568109dad"
kind: "chapter"
parent_id: "tycho.volume.c0927de8450647c49e2d33774eeb60be"
canonical_path: "book/volumes/v04/c03/README.md"
title: "V04/C03 — Consistency and distributed transactions"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which invariants need coordination, isolation or reconciliation?"
route_hints:
  questions:
    - "Which invariants need coordination, isolation or reconciliation?"
  prerequisites:
    - "tycho.chapter.6eba0cf391184a709f2e23e5ecc1c3d2"
  related_ids:
    - "tycho.chapter.f5df10e26e27467887ee2b22b6ce50e7"
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

# V04/C03 — Consistency and distributed transactions

## Purpose and mission

Which invariants need coordination, isolation or reconciliation? This chapter owns that question within distributed coordination and event integration. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Place invariants at their enforcing transaction boundary and state how cross-boundary uncertainty is reconciled.

A compensating action can fail or arrive late; a saga is not an atomic transaction across independent owners. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Consistency, transaction isolation and sagas across service boundaries](transaction-isolation-and-sagas.md) | Which invariants need coordination, isolation or reconciliation? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Define the invariant before naming consistency](transaction-isolation-and-sagas.md#1-define-the-invariant-before-naming-consistency).
- [2. PostgreSQL transaction isolation as a concrete bounded example](transaction-isolation-and-sagas.md#2-postgresql-transaction-isolation-as-a-concrete-bounded-example).
- [Engineering walkthrough — The cancel-versus-accept invariant crosses a transaction boundary](transaction-isolation-and-sagas.md#engineering-walkthrough-the-cancel-versus-accept-invariant-crosses-a-transaction-boundary).
- [Bounded public evidence and review state](transaction-isolation-and-sagas.md#bounded-public-evidence-and-review-state).

## Boundaries and further reading

- [V05/C01 — Relational modeling and transaction isolation](../../v05/c01/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V04 — Distributed coordination and event integration](../README.md) |
| Previous | [V04/C02 — Replication, consensus and leader changes](../c02/README.md) |
| Next | [V04/C04 — Retries, idempotency and duplicate effects](../c04/README.md) |
| Prerequisite | [V04/C02 — Replication, consensus and leader changes](../c02/README.md) |
| Source reading | [Page-local evidence and versions](transaction-isolation-and-sagas.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
