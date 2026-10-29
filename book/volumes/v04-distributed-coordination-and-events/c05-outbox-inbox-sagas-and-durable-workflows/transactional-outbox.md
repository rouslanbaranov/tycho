---
metadata_version: 1
id: "tycho.page.61636057f11b418a9478066a8034ff56"
kind: "page"
parent_id: "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/transactional-outbox.md"
title: "Transactional Outbox"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
summary: "Bounded technical ownership note for Transactional Outbox; mechanism, invariant, failure and alternative limits."
route_hints:
  questions:
    - "Should publication intent be stored in the same local transaction as the state change?"
  prerequisites:
    - "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
  related_ids:
    - "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "transactional outbox"
    - "owner note"
evidence_scope:
  source_ids:
    - "src.microservices-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Moved verbatim from the outbox, inbox, sagas and durable workflows page; the bound source claims and limits remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: null
content_verified_at: null
---

# Transactional Outbox

> **Pattern atlas:**
> [Transactional Outbox](../../v11-pattern-atlas/c04-consistency-events/transactional-outbox.md#transactional-outbox) — decision conditions and contraindications.

This page owns the bounded technical note moved from the
[outbox, inbox, sagas and durable workflows page](outbox-inbox-sagas-and-durable-workflows.md#transactional-outbox)
on 2026-10-29. The integrated walkthrough remains on the chapter page.

An outbox is a durable publication queue inside the state store. The business row and an intent row
commit together; a relay leases rows, publishes them and records completion. The broker sees
at-least-once attempts, not a distributed transaction.

The relay needs bounded attempts and age, a publication key, per-aggregate ordering and a terminal
quarantine for poison rows. A crash after publish before completion duplicates; after commit before
publish retries. A consumer still deduplicates by effect identity, and a repair operator needs the
row, payload digest and attempt history retained for the declared window. The consumer deduplicates
by message ID or effect identity, so a relay replay remains safe.

Use an outbox when the lost-publication and duplicate-effect risk justifies relay
complexity. Event sourcing is an alternative solution.

## Navigation

| Route | Destination |
|---|---|
| Parent chapter | [V04/C05 — Outbox, inbox, sagas and durable workflows](README.md) |
| Originating page | [Bounded pattern ownership notes](outbox-inbox-sagas-and-durable-workflows.md#bounded-pattern-ownership-notes) |
