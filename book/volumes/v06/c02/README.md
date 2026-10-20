---
metadata_version: 1
id: "tycho.chapter.1035327a459242b78329b41b8fddfee6"
kind: "chapter"
parent_id: "tycho.volume.69e6229b222f4535bc0b3941cee1b1cc"
canonical_path: "book/volumes/v06/c02/README.md"
title: "V06/C02 — Hot keys, cache stampedes and read amplification"
topic_ids:
  - "scaling-mechanisms"
perspectives:
  - "architecture"
  - "evaluation"
summary: "When does adding a cache worsen recovery or contention?"
route_hints:
  questions:
    - "When does adding a cache worsen recovery or contention?"
  prerequisites:
    - "tycho.chapter.4166e932cbd64ce2a63fe0c6d6eb049a"
  related_ids: []
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# V06/C02 — Hot keys, cache stampedes and read amplification

## Purpose and mission

When does adding a cache worsen recovery or contention? This chapter owns that question within caching, indexing and information retrieval. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Bound regeneration, hot-key fan-out and cold-start demand as part of cache recovery.

A cache outage or simultaneous expiry can concentrate traffic on the protected origin and amplify the original failure. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Cache invalidation, stampedes and hot-key failure modes](cache-invalidation-stampede-and-hot-keys.md) | When does adding a cache worsen recovery or contention? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. The stale-fill-after-invalidation race](cache-invalidation-stampede-and-hot-keys.md#1-the-stale-fill-after-invalidation-race).
- [2. Stampede at a synchronized expiry](cache-invalidation-stampede-and-hot-keys.md#2-stampede-at-a-synchronized-expiry).
- [6. A discriminating failure experiment](cache-invalidation-stampede-and-hot-keys.md#6-a-discriminating-failure-experiment).
- [7. Public references and limitations](cache-invalidation-stampede-and-hot-keys.md#7-public-references-and-limitations).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V06 — Caching, indexing and information retrieval](../README.md) |
| Previous | [V06/C01 — Local and distributed caching](../c01/README.md) |
| Next | [V06/C03 — Lexical full-text indexing and ranking](../c03/README.md) |
| Prerequisite | [V06/C01 — Local and distributed caching](../c01/README.md) |
| Source reading | [Page-local evidence and versions](cache-invalidation-stampede-and-hot-keys.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
