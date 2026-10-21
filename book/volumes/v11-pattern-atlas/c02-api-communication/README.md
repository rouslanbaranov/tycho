---
metadata_version: 1
id: "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c02-api-communication/README.md"
title: "V11/C02 — API and service communication"
topic_ids:
  - "application-architecture"
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Phase 1 inventory of 12 catalog entries with candidate areas; no technical claim."
route_hints:
  questions:
    - "Which API and discovery patterns fit the trust boundary?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.e996607f707421ca388796732547cafd"
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  excludes:
    - "No source reading, card authoring or technical sufficiency is asserted."
  keywords:
    - "pattern atlas"
    - "api and service communication"
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
# V11/C02 — API and service communication

**Owning question:** Which API and discovery patterns fit the trust boundary?

## Purpose and mission

This chapter is the atlas entry point for **API and service communication**. It owns the
conditional decision route for 12 catalog entries, not the deep mechanism explanations. Read the
candidate technical owner before applying a mechanism claim.

## Pages and reasoning route

Page count is content-dependent. Phase 1 uses this landing as the entry inventory: all entries
are visible, but full decision cards, source ledgers and any page split follow in later phases.
A chapter may need one page or many; there is no fixed two- or three-page quota.

Start with the entry inventory below, then follow the candidate area and the candidate page when
one exists. A candidate is a reading hypothesis, not a confirmed canonical owner.

## Entry inventory

Each level-three heading is a stable atlas anchor. Candidate areas and pages are not audited. No
source was read for an entry in Phase 1.

### API Gateway

**Catalog problem:** Define a managed entry boundary for external clients and downstream
services

**Candidate area:** V08/C08 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Gateway Routing

**Catalog problem:** Route requests to the responsible backend via explicit contracts

**Candidate area:** V08/C08 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Gateway Aggregation

**Catalog problem:** Aggregate multiple downstream responses into one client-facing result

**Candidate area:** V08/C08 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Gateway Offloading

**Catalog problem:** Centralize reusable cross-cutting gateway functions without moving domain
authority

**Candidate area:** V08/C08 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Backend for Frontend (BFF)

**Catalog problem:** Tailor server interaction contracts to client populations

**Candidate area:** V02/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### API Composition

**Catalog problem:** Assemble responses requiring data from several service owners

**Candidate area:** V02/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Reverse Proxy

**Catalog problem:** Terminate and forward client connections with explicit trust/transport
scope

**Candidate area:** V08/C08 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Service Discovery

**Catalog problem:** Locate available service instances amid topology changes

**Candidate area:** V08/C08 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Client-Side Discovery

**Catalog problem:** Make the requesting client responsible for backend selection

**Candidate area:** V08/C08 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Server-Side Discovery

**Catalog problem:** Delegate backend selection to gateway, router or load balancer

**Candidate area:** V08/C08 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Asynchronous Request-Reply

**Catalog problem:** Separate long-running processing from the initiating request lifecycle

**Candidate area:** V03/C04 (provisional; not audited).

**Candidate page:** Asynchronous APIs and streaming: demand, deadlines and cancellation

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Gatekeeper

**Catalog problem:** Validate externally originated requests before privileged internal handling

**Candidate area:** V02/C07 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

## Chapter result and counterexample

This chapter inventories 12 catalog entries and routes each to a provisional candidate area; it
does not establish technical sufficiency.

A pattern name, a candidate link or a passing structural check is not evidence that the pattern
fits a workload.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C01](../c01-application-boundaries/README.md).
- Next: [V11/C03](../c03-messaging-integration/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- No external source was read for this chapter in Phase 1.
- Candidate area and page entries are provisional; no page-level audit was performed.
- All entries remain not-yet-assessed; no technical or decision coverage is claimed.
- The chapter is an inventory and route, not a full pattern card or a replacement for the
  technical owner.
