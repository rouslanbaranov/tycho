---
metadata_version: 1
id: "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
kind: "chapter"
parent_id: "tycho.volume.c0927de8450647c49e2d33774eeb60be"
canonical_path: "book/volumes/v04/c06/README.md"
title: "V04/C06 — Messaging families and delivery contracts"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What are the consequences of acknowledgement, retention and consumer state?"
route_hints:
  questions:
    - "What are the consequences of acknowledgement, retention and consumer state?"
  prerequisites:
    - "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
  related_ids: []
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.nats"
    - "src.rabbitmq"
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

# V04/C06 — Messaging families and delivery contracts

## Purpose and mission

What are the consequences of acknowledgement, retention and consumer state? This chapter owns that question within distributed coordination and event integration. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Compare messaging mechanisms by acknowledgment, retention, ordering scope, consumer state and recovery behavior.

Acknowledging receipt can precede a durable application effect; delivery terminology cannot substitute for the consumer's commit contract. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Messaging families: RabbitMQ, Pulsar, NATS and durable workflows](messaging-families-and-durable-workflows.md) | What are the consequences of acknowledgement, retention and consumer state? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. First identify what a consumer must own](messaging-families-and-durable-workflows.md#1-first-identify-what-a-consumer-must-own).
- [2. Requirement-driven comparison, not a ranking](messaging-families-and-durable-workflows.md#2-requirement-driven-comparison-not-a-ranking).
- [Engineering walkthrough — Work queue versus ephemeral fan-out versus replayable history](messaging-families-and-durable-workflows.md#engineering-walkthrough-work-queue-versus-ephemeral-fan-out-versus-replayable-history).
- [Applied M9 evidence: what transfers and what does not](messaging-families-and-durable-workflows.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V04 — Distributed coordination and event integration](../README.md) |
| Previous | [V04/C05 — Outbox, inbox, sagas and durable workflows](../c05/README.md) |
| Next | [V04/C07 — Kafka logs, partitions and transactions](../c07/README.md) |
| Prerequisite | [V04/C05 — Outbox, inbox, sagas and durable workflows](../c05/README.md) |
| Source reading | [Page-local evidence and versions](messaging-families-and-durable-workflows.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
