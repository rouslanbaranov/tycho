---
metadata_version: 1
id: "tycho.chapter.e996607f707421ca388796732547cafd"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c01-application-boundaries/README.md"
title: "V11/C01 — Application architecture and boundaries"
topic_ids:
  - "application-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Phase 1 inventory of 12 catalog entries with candidate areas; no technical claim."
route_hints:
  questions:
    - "Which application patterns fit a bounded ownership model?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  excludes:
    - "No source reading, card authoring or technical sufficiency is asserted."
  keywords:
    - "pattern atlas"
    - "application architecture and boundaries"
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
# V11/C01 — Application architecture and boundaries

**Owning question:** Which application patterns fit a bounded ownership model?

## Purpose and mission

This chapter is the atlas entry point for **Application architecture and boundaries**. It owns
the conditional decision route for 12 catalog entries, not the deep mechanism explanations. Read
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

### Layered Architecture

**Catalog problem:** Separate responsibilities into layers with controlled dependency direction

**Candidate area:** V02/C01 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Modular Monolith

**Catalog problem:** Enforce module ownership while retaining one deployment unit

**Candidate area:** V02/C03 (provisional; not audited).

**Candidate page:** Modular monolith architecture and internal domain events

**Candidate confidence:** strong; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Microservices Architecture

**Catalog problem:** Independently deploy bounded business capabilities with explicit
distributed costs

**Candidate area:** V02/C04 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Service-Oriented Architecture (SOA)

**Catalog problem:** Compose independently governed service contracts and integrations

**Candidate area:** V02/C04 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Hexagonal Architecture / Ports and Adapters

**Catalog problem:** Isolate core logic from technology-specific adapters

**Candidate area:** V02/C01 (provisional; not audited).

**Candidate page:** Layered, hexagonal and ports-and-adapters architecture

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Clean / Onion Architecture

**Catalog problem:** Direct dependencies inward toward domain policies

**Candidate area:** V02/C01 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Domain-Driven Design / Bounded Context

**Catalog problem:** Separate models according to business meaning and ownership

**Candidate area:** V02/C02 (provisional; not audited).

**Candidate page:** Domain semantics and authoritative ownership

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Database per Service

**Catalog problem:** Give each service independent authoritative data ownership

**Candidate area:** V02/C02 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Self-Contained Service

**Catalog problem:** Reduce synchronous cross-service dependencies within a capability boundary

**Candidate area:** V02/C04 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Sidecar

**Catalog problem:** Add auxiliary runtime behavior in a colocated process/container

**Candidate area:** V08/C03 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Ambassador

**Catalog problem:** Mediate client-side network capabilities through a local proxy

**Candidate area:** V08/C03 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Anti-Corruption Layer

**Catalog problem:** Translate legacy or external semantics without contaminating the domain
model

**Candidate area:** V02/C06 (provisional; not audited).

**Candidate page:** Anti-corruption adapters: semantic translation and safe coexistence

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

## Chapter result and counterexample

This chapter inventories 12 catalog entries and routes each to a provisional candidate area; it
does not establish technical sufficiency.

A pattern name, a candidate link or a passing structural check is not evidence that the pattern
fits a workload.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Next: [V11/C02](../c02-api-communication/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- No external source was read for this chapter in Phase 1.
- Candidate area and page entries are provisional; no page-level audit was performed.
- All entries remain not-yet-assessed; no technical or decision coverage is claimed.
- The chapter is an inventory and route, not a full pattern card or a replacement for the
  technical owner.
