---
metadata_version: 1
id: "tycho.page.765a54f5d9944577908b40b3fc6cb7ef"
kind: "page"
parent_id: "tycho.chapter.4166e932cbd64ce2a63fe0c6d6eb049a"
canonical_path: "book/volumes/v06/c01/cache-authority.md"
title: "Authority, freshness and cache placement"
topic_ids:
  - "scaling-mechanisms"
perspectives:
  - "architecture"
summary: "Which state remains authoritative when a local or distributed cache is used?"
route_hints:
  questions:
    - "Which state remains authoritative when a local or distributed cache is used?"
  prerequisites:
    - "tycho.page.33742c54f667446cbf57cb9f3696a533"
  related_ids:
    - "tycho.chapter.4166e932cbd64ce2a63fe0c6d6eb049a"
    - "tycho.page.33742c54f667446cbf57cb9f3696a533"
    - "tycho.page.76f6d792c80a448fa1a76001ca6699e1"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "cache"
    - "authority"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.33742c54f667446cbf57cb9f3696a533; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Authority, freshness and cache placement

**Owning question:** Which state remains authoritative when a local or distributed cache is used?

This page belongs to [V06/C01 — Local and distributed caching](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.33742c54f667446cbf57cb9f3696a533:1 -->
## 1. Begin with the authority and the data contract

**Original fictional case:** a tool-sharing application keeps authoritative reservations in a transactional store, and public display descriptions in a read-mostly catalogue. A cached display title can usually tolerate a bounded stale window; a cached “one device remains available” count cannot necessarily authorize acceptance of the final reservation.

For each cacheable value, record:

| Field | Requirement |
|---|---|
| Authority | Which system/state revision determines the correct value? |
| Key and scope | Stable resource, variant and tenant/permission scope |
| Freshness | Maximum tolerated age/version gap for the user journey |
| Cache miss | Whether and how to read from the authority |
| Cache loss | Safe operation when local/shared cache is down |
| Error | What to show when both source and cache are unavailable |
| Data class | Sensitive fields, retention, encryption and revocation |
| Validation | Evidence that hit/miss paths yield correct user effects |

A TTL expresses a cache lifetime condition; it does not guarantee that a stale value cannot be reinserted after invalidation by an in-flight load. Similarly, a cache hit ratio is not proof of user correctness.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.33742c54f667446cbf57cb9f3696a533:2 -->
## 2. Three basic placements

| Placement | Can help | Costs and correctness gap |
|---|---|---|
| No cache | Simplest authority/read path when origin is fast and affordable | Every query reaches origin, possibly expensive |
| Per-process local cache | Very low read overhead, no cache network call | Each replica warms independently; divergent contents, memory/GC cost, lost state on restart |
| Shared distributed cache | Many application replicas share reusable keyspace and memory | Added network/auth/HA dependency; cache node loss and consistency rules |
| Multi-level local + shared | Avoid remote cache on hot local hits and reduce origin work on misses | Two invalidation/expiration layers, complex stale-version and failure behavior |

The choice does not establish the authoritative database. A shared Redis instance can improve read reuse, but its key value is still a derived projection unless business policy deliberately makes it an authority with proven durability/transactions.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](local-and-distributed-cache-design.md) |
| Next | [Continue the reasoning](refresh-semantics.md) |
| Integrated question | [Original scenario and limits](local-and-distributed-cache-design.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
