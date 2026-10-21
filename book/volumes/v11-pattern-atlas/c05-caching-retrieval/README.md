---
metadata_version: 1
id: "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c05-caching-retrieval/README.md"
title: "V11/C05 — Caching and retrieval"
topic_ids:
  - "performance-engineering"
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Phase 1 inventory of 14 catalog entries with candidate areas; no technical claim."
route_hints:
  questions:
    - "Which cache patterns fit the authority and freshness contract?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
  excludes:
    - "No source reading, card authoring or technical sufficiency is asserted."
  keywords:
    - "pattern atlas"
    - "caching and retrieval"
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
# V11/C05 — Caching and retrieval

**Owning question:** Which cache patterns fit the authority and freshness contract?

## Purpose and mission

This chapter is the atlas entry point for **Caching and retrieval**. It owns the conditional
decision route for 14 catalog entries, not the deep mechanism explanations. Read the candidate
technical owner before applying a mechanism claim.

## Pages and reasoning route

Page count is content-dependent. Phase 1 uses this landing as the entry inventory: all entries
are visible, but full decision cards, source ledgers and any page split follow in later phases.
A chapter may need one page or many; there is no fixed two- or three-page quota.

Start with the entry inventory below, then follow the candidate area and the candidate page when
one exists. A candidate is a reading hypothesis, not a confirmed canonical owner.

## Entry inventory

Each level-three heading is a stable atlas anchor. Candidate areas and pages are not audited. No
source was read for an entry in Phase 1.

### Distributed Cache

**Catalog problem:** Provide a shared cache layer with explicit authority/failure semantics

**Candidate area:** V06/C01 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Cache-Aside / Lazy Loading

**Catalog problem:** Populate cache after miss while preserving origin authority

**Candidate area:** V06/C01 (provisional; not audited).

**Candidate page:** Eviction, refresh and cache-aside races

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Read-Through Cache

**Catalog problem:** Delegate miss loading to the caching layer

**Candidate area:** V06/C01 (provisional; not audited).

**Candidate page:** Local and distributed caching: authority, freshness and placement

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Write-Through Cache

**Catalog problem:** Update authoritative store and cache on a controlled write path

**Candidate area:** V06/C01 (provisional; not audited).

**Candidate page:** Local and distributed caching: authority, freshness and placement

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Write-Behind / Write-Back

**Catalog problem:** Defer durable writes behind cached mutations

**Candidate area:** V06/C01 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Write-Around

**Catalog problem:** Write directly to durable storage; populate cache on later reads

**Candidate area:** V06/C01 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Cache Invalidation

**Catalog problem:** Expire cached data when source state changes

**Candidate area:** V06/C02 (provisional; not audited).

**Candidate page:** Cache invalidation, stampedes and hot-key failure modes

**Candidate confidence:** strong; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### TTL-Based Expiration

**Catalog problem:** Bound cache lifetime/freshness through expiry

**Candidate area:** V06/C02 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Negative Caching

**Catalog problem:** Cache absence/errors when safely scoped and invalidatable

**Candidate area:** V06/C02 (provisional; not audited).

**Candidate page:** Negative caching and discriminating experiments

**Candidate confidence:** strong; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Cache Stampede Protection

**Catalog problem:** Prevent simultaneous regeneration from overwhelming the origin

**Candidate area:** V06/C02 (provisional; not audited).

**Candidate page:** Stampedes and source protection

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Single Flight / Request Coalescing

**Catalog problem:** Coalesce concurrent equivalent requests into one origin fetch

**Candidate area:** V06/C02 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Stale-While-Revalidate

**Catalog problem:** Serve permitted stale data while refreshing asynchronously

**Candidate area:** V06/C02 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Multi-Level Caching

**Catalog problem:** Combine local/shared/edge caches with coherent invalidation contracts

**Candidate area:** V06/C01 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### CDN / Edge Caching

**Catalog problem:** Serve permitted representations near requesters and protect origin

**Candidate area:** V08/C08 (provisional; not audited).

**Candidate page:** Edge caching, private content and origin recovery

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

## Chapter result and counterexample

This chapter inventories 14 catalog entries and routes each to a provisional candidate area; it
does not establish technical sufficiency.

A pattern name, a candidate link or a passing structural check is not evidence that the pattern
fits a workload.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C04](../c04-consistency-events/README.md).
- Next: [V11/C06](../c06-database-storage/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- No external source was read for this chapter in Phase 1.
- Candidate area and page entries are provisional; no page-level audit was performed.
- All entries remain not-yet-assessed; no technical or decision coverage is claimed.
- The chapter is an inventory and route, not a full pattern card or a replacement for the
  technical owner.
