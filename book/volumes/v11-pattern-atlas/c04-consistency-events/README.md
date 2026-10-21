---
metadata_version: 1
id: "tycho.chapter.e9c650012060143639af44b0cfdc4236"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c04-consistency-events/README.md"
title: "V11/C04 — Data consistency, transactions and event sourcing"
topic_ids:
  - "data-architecture"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Phase 1 inventory of 14 catalog entries with candidate areas; no technical claim."
route_hints:
  questions:
    - "Which consistency patterns preserve the required invariants?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
  excludes:
    - "No source reading, card authoring or technical sufficiency is asserted."
  keywords:
    - "pattern atlas"
    - "data consistency, transactions and event sourcing"
    - "decision layer"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Phase 1 entry inventory; no source or technical claim."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-21"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---
# V11/C04 — Data consistency, transactions and event sourcing

**Owning question:** Which consistency patterns preserve the required invariants?

## Purpose and mission

This chapter is the atlas entry point for **Data consistency, transactions and event sourcing**.
It owns the conditional decision route for 14 catalog entries, not the deep mechanism
explanations. Read the candidate technical owner before applying a mechanism claim.

## Pages and reasoning route

Page count is content-dependent. Phase 1 uses this landing as the entry inventory: all entries
are visible, but full decision cards, source ledgers and any page split follow in later phases.
A chapter may need one page or many; there is no fixed two- or three-page quota.

Start with the entry inventory below, then follow the candidate area and the candidate page when
one exists. A candidate is a reading hypothesis, not a confirmed canonical owner.

## Entry inventory

Each level-three heading is a stable atlas anchor. Candidate areas and pages are not audited. No
source was read for an entry in Phase 1.

### Command Query Responsibility Segregation (CQRS)

**Catalog problem:** Separate write-command and read-query responsibilities/models

**Candidate area:** V04/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Event Sourcing

**Catalog problem:** Derive state from an authoritative ordered event history

**Candidate area:** V04/C05 (provisional; not audited).

**Candidate page:** CQRS, event sourcing and reliable read projections

**Candidate confidence:** strong; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Domain Events

**Catalog problem:** Communicate meaningful changes to domain state or decisions

**Candidate area:** V04/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Saga

**Catalog problem:** Coordinate multi-service business outcomes through local transactions

**Candidate area:** V04/C05 (provisional; not audited).

**Candidate page:** Outbox, inbox, sagas and durable workflow coordination

**Candidate confidence:** strong; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Saga Choreography

**Catalog problem:** Coordinate local effects through events without central orchestration

**Candidate area:** V04/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Saga Orchestration

**Catalog problem:** Manage multi-step local transactions through an explicit coordinator

**Candidate area:** V04/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Compensating Transaction

**Catalog problem:** Counteract prior business effects with defined compensation semantics

**Candidate area:** V04/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Transactional Outbox

**Catalog problem:** Atomically store local state and event-publication intent

**Candidate area:** V04/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Transactional Inbox

**Catalog problem:** Atomically track received message identity and local processing effect

**Candidate area:** V04/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Idempotency Key

**Catalog problem:** Associate retries with one logical intent and payload

**Candidate area:** V04/C04 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Change Data Capture (CDC)

**Catalog problem:** Propagate committed database changes via change streams

**Candidate area:** V04/C08 (provisional; not audited).

**Candidate page:** CDC, task state and changelog replay

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Materialized View

**Catalog problem:** Maintain a derived read representation with explicit freshness semantics

**Candidate area:** V04/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Command-Side Replica

**Catalog problem:** Supply local read-only facts for decisions without synchronous owner calls

**Candidate area:** V04/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Two-Phase Commit (2PC)

**Catalog problem:** Coordinate prepare/commit across transactional participants

**Candidate area:** V04/C03 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

## Chapter result and counterexample

This chapter inventories 14 catalog entries and routes each to a provisional candidate area; it
does not establish technical sufficiency.

A pattern name, a candidate link or a passing structural check is not evidence that the pattern
fits a workload.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C03](../c03-messaging-integration/README.md).
- Next: [V11/C05](../c05-caching-retrieval/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- No external source was read for this chapter in Phase 1.
- Candidate area and page entries are provisional; no page-level audit was performed.
- All entries remain not-yet-assessed; no technical or decision coverage is claimed.
- The chapter is an inventory and route, not a full pattern card or a replacement for the
  technical owner.
