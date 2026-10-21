---
metadata_version: 1
id: "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c07-resilience/README.md"
title: "V11/C07 — Resilience and fault tolerance"
topic_ids:
  - "performance-engineering"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "operations"
summary: "Phase 1 inventory of 16 catalog entries with candidate areas; no technical claim."
route_hints:
  questions:
    - "Which resilience mechanisms bound failure without amplifying it?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
    - "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
  excludes:
    - "No source reading, card authoring or technical sufficiency is asserted."
  keywords:
    - "pattern atlas"
    - "resilience and fault tolerance"
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
# V11/C07 — Resilience and fault tolerance

**Owning question:** Which resilience mechanisms bound failure without amplifying it?

## Purpose and mission

This chapter is the atlas entry point for **Resilience and fault tolerance**. It owns the
conditional decision route for 16 catalog entries, not the deep mechanism explanations. Read the
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

### Circuit Breaker

**Catalog problem:** Bound repeated calls into failing dependencies

**Candidate area:** V07/C05 (provisional; not audited).

**Candidate page:** Bulkheads, retries and optional dependencies

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Bulkhead

**Catalog problem:** Isolate resources and failure blast radii between workloads

**Candidate area:** V07/C05 (provisional; not audited).

**Candidate page:** Bulkheads, retries and optional dependencies

**Candidate confidence:** strong; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Retry with Exponential Backoff

**Catalog problem:** Back off transient retries according to a finite budget

**Candidate area:** V02/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Retry with Jitter

**Catalog problem:** Desynchronize retry storms by randomized delays

**Candidate area:** V02/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Timeout

**Catalog problem:** Bound waiting for a particular operation

**Candidate area:** V02/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Deadline Propagation

**Catalog problem:** Preserve a shared end-to-end budget across hops

**Candidate area:** V02/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Fallback

**Catalog problem:** Use a defined alternate result or dependency under failure

**Candidate area:** V07/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Graceful Degradation

**Catalog problem:** Preserve essential outcomes under partial outage

**Candidate area:** V07/C05 (provisional; not audited).

**Candidate page:** Overload protection, admission control and graceful degradation

**Candidate confidence:** strong; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Load Shedding

**Catalog problem:** Reject excess work to preserve valid throughput

**Candidate area:** V07/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Throttling

**Catalog problem:** Regulate the pace of resource consumption

**Candidate area:** V07/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Rate Limiting

**Catalog problem:** Limit requests per caller, identity, tenant or time window

**Candidate area:** V07/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Queue-Based Load Leveling

**Catalog problem:** Buffer bounded bursts to decouple arrival from processing

**Candidate area:** V07/C05 (provisional; not audited).

**Candidate page:** Queueing, Little's Law and workload measurement boundaries

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Priority Queue

**Catalog problem:** Order queued work according to declared importance/fairness policy

**Candidate area:** V07/C05 (provisional; not audited).

**Candidate page:** Scarce resources, admission and queues

**Candidate confidence:** medium; candidate only, not audited.

**State:** not-yet-assessed; no source inspected.

### Hedged Requests

**Catalog problem:** Race bounded equivalent requests to mitigate high tail latency

**Candidate area:** V07/C05 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Health Endpoint Monitoring

**Catalog problem:** Observe useful service health and unhealthy dependency states

**Candidate area:** V09/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

### Failover / Failback

**Catalog problem:** Move serving or write authority during failure and safely return

**Candidate area:** V08/C06 (provisional; not audited). **Candidate page:** no strong or medium
candidate yet; see the coverage map.

**State:** not-yet-assessed; no source inspected.

## Chapter result and counterexample

This chapter inventories 16 catalog entries and routes each to a provisional candidate area; it
does not establish technical sufficiency.

A pattern name, a candidate link or a passing structural check is not evidence that the pattern
fits a workload.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C06](../c06-database-storage/README.md).
- Next: [V11/C08](../c08-coordination/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- No external source was read for this chapter in Phase 1.
- Candidate area and page entries are provisional; no page-level audit was performed.
- All entries remain not-yet-assessed; no technical or decision coverage is claimed.
- The chapter is an inventory and route, not a full pattern card or a replacement for the
  technical owner.
