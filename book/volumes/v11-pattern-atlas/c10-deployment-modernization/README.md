---
metadata_version: 1
id: "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md"
title: "V11/C10 — Deployment and legacy modernization"
topic_ids:
  - "deployment-architecture"
  - "software-delivery"
perspectives:
  - "architecture"
  - "migration"
summary: "Phase 1 inventory of 12 catalog entries with candidate areas; no technical claim."
route_hints:
  questions:
    - "Which deployment patterns keep change reversible?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "No source reading, card authoring or technical sufficiency is asserted."
  keywords:
    - "pattern atlas"
    - "deployment and legacy modernization"
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
# V11/C10 — Deployment and legacy modernization

**Owning question:** Which deployment patterns keep change reversible?

## Purpose and mission

This chapter is the atlas entry point for **Deployment and legacy modernization**. It owns the
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

### Rolling Deployment

**Catalog problem:** Replace instances incrementally while preserving service

**Candidate area:** V08/C04 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Blue / Green Deployment

**Catalog problem:** Switch traffic between two provisioned versions/environments

**Candidate area:** V08/C04 (provisional; not audited).

**Candidate page:** GitOps, rolling, blue/green and canary release architecture

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Canary Release

**Catalog problem:** Expose a controlled subset of traffic before promotion

**Candidate area:** V08/C04 (provisional; not audited).

**Candidate page:** GitOps, rolling, blue/green and canary release architecture

**Candidate confidence:** strong; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Feature Flags / Feature Toggles

**Catalog problem:** Decouple code rollout from feature activation

**Candidate area:** V08/C04 (provisional; not audited).

**Candidate page:** Dynamic configuration and feature flags

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### GitOps

**Catalog problem:** Reconcile declared desired deployment state with actual state

**Candidate area:** V08/C01 (provisional; not audited).

**Candidate page:** CI/CD architecture, artifact provenance and GitOps reconciliation

**Candidate confidence:** strong; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Immutable Infrastructure

**Catalog problem:** Replace rather than mutate deployed infrastructure in place

**Candidate area:** V08/C03 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Strangler Fig

**Catalog problem:** Incrementally replace old capabilities at controlled boundaries

**Candidate area:** V10/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Branch by Abstraction

**Catalog problem:** Switch implementations behind stable in-process interfaces

**Candidate area:** V10/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Parallel Run

**Catalog problem:** Execute old and new paths to reconcile outputs before authority transfer

**Candidate area:** V10/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Dark Launching / Shadow Traffic

**Catalog problem:** Exercise new implementation using mirrored traffic without publishing its
effects

**Candidate area:** V10/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Expand-and-Contract

**Catalog problem:** Maintain version coexistence during interface/data migration

**Candidate area:** V08/C05 (provisional; not audited).

**Candidate page:** Reader/writer compatibility and migration stages

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Controlled Cutover

**Catalog problem:** Transfer authoritative traffic/state at explicit verified gates

**Candidate area:** V10/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

## Chapter result and counterexample

This chapter inventories 12 catalog entries and routes each to a provisional candidate area; it
does not establish technical sufficiency.

A pattern name, a candidate link or a passing structural check is not evidence that the pattern
fits a workload.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C09](../c09-scalability/README.md).
- Next: [V11/C11](../c11-security-operations/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- No external source was read for this chapter in Phase 1.
- Candidate area and page entries are provisional; no page-level audit was performed.
- All entries remain not-yet-assessed; no technical or decision coverage is claimed.
- The chapter is an inventory and route, not a full pattern card or a replacement for the
  technical owner.
