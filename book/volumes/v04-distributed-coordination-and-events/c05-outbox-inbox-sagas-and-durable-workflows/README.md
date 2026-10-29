---
metadata_version: 1
id: "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
kind: "chapter"
parent_id: "tycho.volume.c0927de8450647c49e2d33774eeb60be"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/README.md"
title: "V04/C05 — Outbox, inbox, sagas and durable workflows"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How are state changes coordinated without claiming global atomicity? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How are state changes coordinated without claiming global atomicity?"
  prerequisites:
    - "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
  related_ids:
    - "tycho.chapter.5de52a840c14448c946a65c924f28487"
    - "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
    - "tycho.page.aa810dd152884b35a84f0f4cbe4369e9"
    - "tycho.page.9daa9ce90a5047fa849c637f24b063f7"
    - "tycho.page.eba0d0f0151c4044a71589c4d216b4b9"
    - "tycho.page.71aea7bc58a6411ba7baf8a2ff40ffbd"
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
updated_at: "2026-10-21"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](outbox-inbox-sagas-and-durable-workflows.md) | How are state changes coordinated without claiming global atomicity? |
| [Transactional Outbox owner note](transactional-outbox.md) | How is publication intent committed and relayed without a shared atomic transaction? |
| [Outbox publication and ordering](outbox-publication.md) | Which local atomic record closes a dual-write loss window? |
| [Inbox processing and atomic consumer effects](inbox-atomicity.md) | When can a receiver commit an effect and its deduplication record together? |
| [Sagas, workflow recovery and compensation](saga-workflows.md) | What business recovery contract replaces a nonexistent global rollback? |

Additional page:

- [Periodic work and leases](periodic-work-leases-and-exactly-once.md) — How do
  periodic jobs and pipelines recover when a launch is ambiguous or a lease is
  stale?

## Boundaries and further reading

- [V02/C03 — Modular monolith and internal events](../../v02-application-boundaries-and-contracts/c03-modular-monolith-and-internal-events/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.
- [V04/C04 — Retries, idempotency and duplicate effects](../c04-retries-idempotency-and-duplicate-effects/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V04 — Distributed coordination and event integration](../README.md) |
| Previous | [V04/C04 — Retries, idempotency and duplicate effects](../c04-retries-idempotency-and-duplicate-effects/README.md) |
| Next | [V04/C06 — Messaging families and delivery contracts](../c06-messaging-families-and-delivery-contracts/README.md) |
| Prerequisite | [V04/C04 — Retries, idempotency and duplicate effects](../c04-retries-idempotency-and-duplicate-effects/README.md) |
| Source reading | [Page-local evidence and versions](outbox-inbox-sagas-and-durable-workflows.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.aa810dd152884b35a84f0f4cbe4369e9:7 -->
## 7. Source-to-claim ledger

| Independently reviewed source | Narrow documented fact | Not proven |
|---|---|---|
| [Transactional Outbox pattern](https://microservices.io/patterns/data/transactional-outbox) | Local commit of state+publication intent and duplicate-relay risk | Cross-resource atomicity |
| [Debezium 3.6 Outbox Event Router](https://debezium.io/documentation/reference/3.6/transformations/outbox-event-router.html) | Version-scoped outbox event identity/key/payload mapping | Correctness of any deployed CDC pipeline |
| [Idempotent Consumer pattern](https://microservices.io/patterns/communication-style/idempotent-consumer.html) | Receiver-local processed-message and state effects | Exactly-once arbitrary external side effects |
| [Saga pattern](https://microservices.io/patterns/data/saga.html) | Coordinated local transactions and compensating actions | Automatic reversibility or distributed ACID |

- [SRE, *Cron Scheduling*](https://sre.google/sre-book/distributed-periodic-scheduling/)
  and [*Data Processing Pipelines*](https://sre.google/sre-book/data-processing-pipelines/),
  inspected 2026-10-21: ambiguous launches, overlapping runs and workflow
  correctness. The source's examples are contextual, not universal designs.

All examples and state descriptions here are original independent educational material. No service, database, broker, workflow, failure injection, compliance finding or independent review is claimed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.aa810dd152884b35a84f0f4cbe4369e9:8 -->
## Navigation

Proposed **V04/C05** in the [10-volume outline](../../../PROPOSED-STRUCTURE.md). Via [distributed landing](../../../distributed/README.md), read [V04/C04 retries](../c04-retries-idempotency-and-duplicate-effects/retries-idempotency-and-ambiguous-effects.md), [transaction isolation](../c03-consistency-and-distributed-transactions/transaction-isolation-and-sagas.md), [Kafka partition behavior](../c07-kafka-logs-partitions-and-transactions/kafka-partitions-replication-and-contracts.md), and [safe rollout](../../../delivery/safe-rollout-and-recovery.md).
<!-- /tycho-question-source -->
