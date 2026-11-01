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
summary: "All 14 C05 cards with bounded owner links; decision coverage partial."
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
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "caching and retrieval"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.hazelcast"
    - "src.aws-caching-strategies"
    - "src.microsoft-caching-guidance"
    - "src.redis"
    - "src.google-cdn-negative-caching"
    - "src.rfc5861"
    - "src.rfc9111-enrichment"
    - "src.mdn-cache-control"
    - "src.microsoft-cloud-patterns"
  claim_ids: []
  status: "source-linked"
  notes: >-
    14 cards cite read units; owner links are bounded. Negative Caching moved to
    a dedicated page on 2026-10-31 with RFC 9111, CloudFront 4xx/5xx processing,
    OWASP authorization-decision reuse guidance and Cloudflare status-code
    defaults; the Google Cloud CDN per-status TTL example is retained.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# V11/C05 — Caching and retrieval

**Owning question:** Which cache patterns fit the authority and freshness contract?

## Purpose and mission

This chapter is the atlas entry point for **Caching and retrieval**. It owns the
conditional decision route for 14 catalog entries, not the deep mechanism explanations.
Read the exact owner section before applying a mechanism claim.

All 14 entries have a self-checked card. Owner sections are bounded: a caching page may
own authority/freshness without owning every cache implementation.

## Pages and reasoning route

Page count is content-dependent. This chapter uses a landing page plus dedicated card
pages for moved entries; a later split is an editorial change, not a plan failure. Start
with the card, check its conditions and contraindications, then read the exact owner
section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Distributed Cache

See the [Distributed Cache](distributed-cache.md) card.

### Cache-Aside / Lazy Loading

See the [dedicated Cache-Aside / Lazy Loading card](cache-aside-lazy-loading.md).

### Read-Through Cache

See the [Read-Through Cache](read-through-cache.md) card.

### Write-Through Cache

See the [Write-Through Cache](write-through-cache.md) card.

### Write-Behind / Write-Back

See the [Write-Behind / Write-Back](write-behind-write-back.md) card.

### Write-Around

See the [Write-Around](write-around.md) card.

### Cache Invalidation

See the [dedicated Cache Invalidation card](cache-invalidation.md).

### TTL-Based Expiration

See the [dedicated TTL-Based Expiration card](ttl-based-expiration.md).

### Negative Caching

See the [dedicated Negative Caching card](negative-caching.md).

### Cache Stampede Protection

See the [dedicated Cache Stampede Protection card](cache-stampede.md).

### Single Flight / Request Coalescing

See the [Single Flight / Request Coalescing](single-flight-request-coalescing.md) card.

### Stale-While-Revalidate

See the [dedicated Stale-While-Revalidate card](stale-while-revalidate.md).

### Multi-Level Caching

See the [dedicated Multi-Level Caching card](multi-level-caching.md).

### CDN / Edge Caching

See the [dedicated CDN / Edge Caching card](cdn-edge-caching.md).

## Chapter result and counterexample

Fourteen cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: a CDN configured to cache a personalized response is not evidence for
the edge-caching card's cacheability conditions.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C04](../c04-consistency-events/README.md).
- Next: [V11/C06](../c06-database-storage/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 14 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.
