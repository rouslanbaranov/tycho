---
metadata_version: 1
id: "tycho.chapter.f5df10e26e27467887ee2b22b6ce50e7"
kind: "chapter"
parent_id: "tycho.volume.01d303aaa7984edaac4127884592dd75"
canonical_path: "book/volumes/v05/c01/README.md"
title: "V05/C01 — Relational modeling and transaction isolation"
topic_ids:
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which invariants and anomalies are relevant to the data contract?"
route_hints:
  questions:
    - "Which invariants and anomalies are relevant to the data contract?"
  prerequisites:
    - "tycho.chapter.4a3cbf0617e44be5b1e8d72568109dad"
    - "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
    - "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
  related_ids:
    - "tycho.chapter.4a3cbf0617e44be5b1e8d72568109dad"
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

# V05/C01 — Relational modeling and transaction isolation

## Purpose and mission

Which invariants and anomalies are relevant to the data contract? This chapter owns that question within data models, engines and lifecycle. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Derive relational constraints and isolation requirements from the anomalies the application must forbid.

Selecting an isolation label without considering transaction retries and constraint placement leaves the invariant unproven. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Relational modeling, business constraints and transaction isolation](relational-modeling-and-transaction-isolation.md) | Which invariants and anomalies are relevant to the data contract? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Model business identities before tables](relational-modeling-and-transaction-isolation.md#1-model-business-identities-before-tables).
- [2. A snapshot is not an invariant](relational-modeling-and-transaction-isolation.md#2-a-snapshot-is-not-an-invariant).
- [6. Architecture alternatives and limits](relational-modeling-and-transaction-isolation.md#6-architecture-alternatives-and-limits).
- [7. Public source ledger and nonclaims](relational-modeling-and-transaction-isolation.md#7-public-source-ledger-and-nonclaims).

## Boundaries and further reading

- [V04/C03 — Consistency and distributed transactions](../../v04/c03/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V05 — Data models, engines and lifecycle](../README.md) |
| Previous | [V04/C08 — Stateful/event-time stream processing](../../v04/c08/README.md) |
| Next | [V05/C02 — PostgreSQL MVCC, WAL and recovery](../c02/README.md) |
| Prerequisite | [V04/C03 — Consistency and distributed transactions](../../v04/c03/README.md) |
| Prerequisite | [V04/C04 — Retries, idempotency and duplicate effects](../../v04/c04/README.md) |
| Prerequisite | [V04/C05 — Outbox, inbox, sagas and durable workflows](../../v04/c05/README.md) |
| Source reading | [Page-local evidence and versions](relational-modeling-and-transaction-isolation.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
