---
metadata_version: 1
id: "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c06-database-storage/README.md"
title: "V11/C06 — Database and storage architecture"
topic_ids:
  - "data-architecture"
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Phase 1 inventory of 13 catalog entries with candidate areas; no technical claim."
route_hints:
  questions:
    - "Which storage patterns fit the workload and recovery boundary?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
  excludes:
    - "No source reading, card authoring or technical sufficiency is asserted."
  keywords:
    - "pattern atlas"
    - "database and storage architecture"
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
# V11/C06 — Database and storage architecture

**Owning question:** Which storage patterns fit the workload and recovery boundary?

## Purpose and mission

This chapter is the atlas entry point for **Database and storage architecture**. It owns the
conditional decision route for 13 catalog entries, not the deep mechanism explanations. Read the
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

### Sharding

**Catalog problem:** Split authoritative data across independently routed shards

**Candidate area:** V05/C05 (provisional; not audited).

**Candidate page:** Resharding and alternatives

**Candidate confidence:** strong; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Partitioning

**Catalog problem:** Divide datasets within or across storage engines by explicit partition
rules

**Candidate area:** V05/C05 (provisional; not audited).

**Candidate page:** Kafka interaction contracts and partitioning

**Candidate confidence:** strong; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Consistent Hashing

**Catalog problem:** Minimize key movement during node-set changes

**Candidate area:** V05/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Leader-Follower Replication

**Catalog problem:** Replicate writes under a single primary authority

**Candidate area:** V04/C02 (provisional; not audited).

**Candidate page:** Replication, consensus and leader change: safety and progress under failures

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Multi-Leader Replication

**Catalog problem:** Accept writes at multiple leaders and reconcile conflicts

**Candidate area:** V04/C02 (provisional; not audited).

**Candidate page:** Replication, consensus and leader change: safety and progress under failures

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Read Replicas

**Catalog problem:** Offload some reads using defined replication lag/staleness contracts

**Candidate area:** V04/C02 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Quorum-Based Reads / Writes

**Catalog problem:** Use participant quorums to enforce stated consistency assumptions

**Candidate area:** V04/C02 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Index Table

**Catalog problem:** Maintain secondary lookup structures with a clear update contract

**Candidate area:** V05/C03 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Polyglot Persistence

**Catalog problem:** Select heterogeneous stores for distinct needs and synchronize ownership

**Candidate area:** V05/C04 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### CQRS Read Projections

**Catalog problem:** Materialize read-optimized representations from change inputs

**Candidate area:** V04/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Expand-and-Contract Schema

**Catalog problem:** Evolve schemas compatibly across old and new writers/readers

**Candidate area:** V05/C06 (provisional; not audited).

**Candidate page:** Migration stages, retention and no-return points

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Online Data Migration

**Catalog problem:** Change authoritative representation while serving live traffic

**Candidate area:** V05/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Backup, PITR and Restore

**Catalog problem:** Recover consistent user-visible state under explicit RPO/RTO objectives

**Candidate area:** V05/C07 (provisional; not audited).

**Candidate page:** Backup, restore and recovery drills: proving data recoverability

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

## Chapter result and counterexample

This chapter inventories 13 catalog entries and routes each to a provisional candidate area; it
does not establish technical sufficiency.

A pattern name, a candidate link or a passing structural check is not evidence that the pattern
fits a workload.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C05](../c05-caching-retrieval/README.md).
- Next: [V11/C07](../c07-resilience/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- No external source was read for this chapter in Phase 1.
- Candidate area and page entries are provisional; no page-level audit was performed.
- All entries remain not-yet-assessed; no technical or decision coverage is claimed.
- The chapter is an inventory and route, not a full pattern card or a replacement for the
  technical owner.
