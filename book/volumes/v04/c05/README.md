---
metadata_version: 1
id: "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
kind: "chapter"
parent_id: "tycho.volume.c0927de8450647c49e2d33774eeb60be"
canonical_path: "book/volumes/v04/c05/README.md"
title: "V04/C05 — Outbox, inbox, sagas and durable workflows"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How are state changes coordinated without claiming global atomicity?"
route_hints:
  questions:
    - "How are state changes coordinated without claiming global atomicity?"
  prerequisites:
    - "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
  related_ids:
    - "tycho.chapter.5de52a840c14448c946a65c924f28487"
    - "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
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

# V04/C05 — Outbox, inbox, sagas and durable workflows

## Purpose and mission

How are state changes coordinated without claiming global atomicity? This chapter owns that question within distributed coordination and event integration. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Separate local atomic publication intent, relay retries, consumer deduplication and compensation state.

Writing an outbox does not make a remote notification atomic with the original transaction; relay and receiver failures still need recovery. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Outbox, inbox, sagas and durable workflow coordination](outbox-inbox-sagas-and-durable-workflows.md) | How are state changes coordinated without claiming global atomicity? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Two unsafe dual-write orders](outbox-inbox-sagas-and-durable-workflows.md#1-two-unsafe-dual-write-orders).
- [2. Publication schema and ordering boundaries](outbox-inbox-sagas-and-durable-workflows.md#2-publication-schema-and-ordering-boundaries).
- [6. Test failures rather than just the happy path](outbox-inbox-sagas-and-durable-workflows.md#6-test-failures-rather-than-just-the-happy-path).
- [7. Source-to-claim ledger](outbox-inbox-sagas-and-durable-workflows.md#7-source-to-claim-ledger).

## Boundaries and further reading

- [V02/C03 — Modular monolith and internal events](../../v02/c03/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.
- [V04/C04 — Retries, idempotency and duplicate effects](../c04/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V04 — Distributed coordination and event integration](../README.md) |
| Previous | [V04/C04 — Retries, idempotency and duplicate effects](../c04/README.md) |
| Next | [V04/C06 — Messaging families and delivery contracts](../c06/README.md) |
| Prerequisite | [V04/C04 — Retries, idempotency and duplicate effects](../c04/README.md) |
| Source reading | [Page-local evidence and versions](outbox-inbox-sagas-and-durable-workflows.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
