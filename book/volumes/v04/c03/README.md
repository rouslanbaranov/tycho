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
summary: "Which invariants need coordination, isolation or reconciliation? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Which invariants need coordination, isolation or reconciliation?"
  prerequisites:
    - "tycho.chapter.6eba0cf391184a709f2e23e5ecc1c3d2"
  related_ids:
    - "tycho.chapter.f5df10e26e27467887ee2b22b6ce50e7"
    - "tycho.page.3c78e2b17ac74973b2ae658977843c2a"
    - "tycho.page.5da19d9b920940fb837bbb28e8fefe77"
    - "tycho.page.e4a2ae7fb1d74eadbdc6d8eb07db46ec"
    - "tycho.page.db64c44e7af846f9b54a524a37a1b9dd"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](transaction-isolation-and-sagas.md) | Which invariants need coordination, isolation or reconciliation? |
| [Invariants and local transaction isolation](invariants-isolation.md) | Which state owner and anomaly define the required coordination boundary? |
| [Distributed transactions and business protocols](distributed-protocols.md) | Which obligations remain when local transactions cannot atomically coordinate owners? |
| [Concurrency, compensation and negative experiments](coordination-failure.md) | What schedule would expose an unsafe cross-owner invariant or failed compensation? |

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

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.3c78e2b17ac74973b2ae658977843c2a:8 -->
## Bounded public evidence and review state

| ID | Public source, exact inspected section | Supports / limits |
|---|---|---|
| E01 | [PostgreSQL 17, §13.2 Transaction Isolation](https://www.postgresql.org/docs/17/transaction-iso.html), isolation-level table and serializable behavior, accessed 2026-10-18 | Local isolation semantics only; no assurance of a correct arbitrary domain schema or external transaction |
| E02 | [PostgreSQL 17, §13.5 Serialization Failure Handling](https://www.postgresql.org/docs/17/mvcc-serialization-failure-handling.html), retry requirements | Source transaction may need complete retry, not just repeating a single query |
| E03 | [Chris Richardson, Saga pattern](https://microservices.io/patterns/data/saga.html), Context/Solution/Resulting context: choreography/orchestration, isolation and compensation | Public pattern description, no production guarantee or measured fit |
| E04 | [Richardson, *Managing data consistency ... using Sagas — part 1*](https://microservices.io/post/microservices/2019/07/09/developing-sagas-part-1.html), compensating transactions and semantic-lock example (2019) | Identifies a design hazard and countermeasure; not a proof of the fictional workflow |

All diagram states, examples and numerical parameters here are **original synthetic descriptions**, not source-reproduced experiments. Independent human review, formal concurrency verification, distributed 2PC implementation and system deployment are **not** claimed.
<!-- /tycho-question-source -->
