---
metadata_version: 1
id: "tycho.chapter.a4b31346a691566550633efe0cf2693e"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c03-messaging-integration/README.md"
title: "V11/C03 — Messaging and event-driven integration"
topic_ids:
  - "integration-architecture"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Phase 1 inventory of 20 catalog entries with candidate areas; no technical claim."
route_hints:
  questions:
    - "Which messaging patterns fit the delivery contract?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
  excludes:
    - "No source reading, card authoring or technical sufficiency is asserted."
  keywords:
    - "pattern atlas"
    - "messaging and event-driven integration"
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
# V11/C03 — Messaging and event-driven integration

**Owning question:** Which messaging patterns fit the delivery contract?

## Purpose and mission

This chapter is the atlas entry point for **Messaging and event-driven integration**. It owns
the conditional decision route for 20 catalog entries, not the deep mechanism explanations. Read
the candidate technical owner before applying a mechanism claim.

## Pages and reasoning route

Page count is content-dependent. Phase 1 uses this landing as the entry inventory: all entries
are visible, but full decision cards, source ledgers and any page split follow in later phases.
A chapter may need one page or many; there is no fixed two- or three-page quota.

Start with the entry inventory below, then follow the candidate area and the candidate page when
one exists. A candidate is a reading hypothesis, not a confirmed canonical owner.

## Entry inventory

Each level-three heading is a stable atlas anchor. Candidate areas and pages are not audited. No
source was read for an entry in Phase 1.

### Publish / Subscribe

**Catalog problem:** Distribute an event to independent interested subscribers

**Candidate area:** V04/C06 (provisional; not audited).

**Candidate page:** Consumer requirements and messaging families

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Point-to-Point Queue

**Catalog problem:** Dispatch individual work items to consumers

**Candidate area:** V04/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Competing Consumers

**Catalog problem:** Parallelize processing from a shared work queue

**Candidate area:** V04/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Event-Driven Consumer

**Catalog problem:** Trigger processing from message arrival rather than polling a data source

**Candidate area:** V04/C06 (provisional; not audited).

**Candidate page:** Consumer requirements and messaging families

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Request-Reply Messaging

**Catalog problem:** Correlate asynchronous message requests and responses

**Candidate area:** V04/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Correlation Identifier

**Catalog problem:** Identify replies and events belonging to one logical operation

**Candidate area:** V04/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Content-Based Router

**Catalog problem:** Select destinations from message contents

**Candidate area:** V04/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Message Filter

**Catalog problem:** Reject or pass messages based on explicit conditions

**Candidate area:** V04/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Pipes and Filters

**Catalog problem:** Compose processing from independent transformation stages

**Candidate area:** V04/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Splitter

**Catalog problem:** Divide composite messages into processable parts

**Candidate area:** V04/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Aggregator

**Catalog problem:** Combine correlated messages with completion/time-window semantics

**Candidate area:** V04/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Scatter-Gather

**Catalog problem:** Fan out requests and reconcile their responses

**Candidate area:** V04/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Dead Letter Channel / DLQ

**Catalog problem:** Isolate messages whose processing cannot safely complete

**Candidate area:** V04/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Durable Subscriber

**Catalog problem:** Retain deliverable events across temporary subscriber outages

**Candidate area:** V04/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Idempotent Receiver

**Catalog problem:** Handle duplicate deliveries without duplicate business effects

**Candidate area:** V04/C04 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Resequencer

**Catalog problem:** Reconstruct an acceptable order from reordered messages

**Candidate area:** V04/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Claim Check

**Catalog problem:** Store a large payload separately and send a controlled reference

**Candidate area:** V04/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Message Broker / Messaging Bridge

**Catalog problem:** Mediate routing or bridge incompatible messaging systems

**Candidate area:** V04/C06 (provisional; not audited).

**Candidate page:** Consumer requirements and messaging families

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Canonical Data Model

**Catalog problem:** Normalize interapplication messages via a shared representation

**Candidate area:** V04/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Process Manager / Routing Slip

**Catalog problem:** Orchestrate or encode a multi-stage integration path

**Candidate area:** V04/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

## Chapter result and counterexample

This chapter inventories 20 catalog entries and routes each to a provisional candidate area; it
does not establish technical sufficiency.

A pattern name, a candidate link or a passing structural check is not evidence that the pattern
fits a workload.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C02](../c02-api-communication/README.md).
- Next: [V11/C04](../c04-consistency-events/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- No external source was read for this chapter in Phase 1.
- Candidate area and page entries are provisional; no page-level audit was performed.
- All entries remain not-yet-assessed; no technical or decision coverage is claimed.
- The chapter is an inventory and route, not a full pattern card or a replacement for the
  technical owner.
