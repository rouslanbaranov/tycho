---
metadata_version: 1
id: "tycho.volume.69e6229b222f4535bc0b3941cee1b1cc"
kind: "volume"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/volumes/v06/README.md"
title: "V06 — Caching, indexing and information retrieval"
topic_ids:
  - "scaling-mechanisms"
  - "search-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Clarify authority/cache/projection/search separation; show lexical, vector, hybrid and graph fits with quantitative evaluation and failure boundaries."
route_hints:
  questions:
    - "Clarify authority/cache/projection/search separation; show lexical, vector, hybrid and graph fits with quantitative evaluation and failure boundaries."
  prerequisites:
    - "tycho.chapter.7031445877fb4f8d831d962d170521c8"
    - "tycho.chapter.e451bfe1e0cb4c588f0576e0b2b7d3d0"
    - "tycho.chapter.3e2e1da8f99c4a7ba05121baf1ef4d91"
    - "tycho.chapter.3d0f6dd1e8e94cd397326e129b5c287f"
  related_ids:
    - "tycho.chapter.4166e932cbd64ce2a63fe0c6d6eb049a"
    - "tycho.chapter.1035327a459242b78329b41b8fddfee6"
    - "tycho.chapter.5dc7b18369054daa852565a5dab2502b"
    - "tycho.chapter.1c08d660af40408188c2d556f8d77358"
    - "tycho.chapter.6d25a036c078402a85ec464227a48a31"
    - "tycho.chapter.1f0c8323023f4adfaa1affc7bf2993d4"
    - "tycho.chapter.e3cf27f8212a455bb53e135ee18bbaa9"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.pgvector"
  claim_ids: []
  status: "source-linked"
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

# V06 — Caching, indexing and information retrieval

## Purpose and mission

Show why different acceleration and search mechanisms solve different problems.

The outcome of this volume is: Clarify authority/cache/projection/search separation; show lexical, vector, hybrid and graph fits with quantitative evaluation and failure boundaries.

## A worked cross-chapter synthesis

A fictional catalogue serves a cached item view and two search indexes. The item changes, one index refresh is delayed, and an access grant is revoked. Fast responses can now be stale, incomplete or forbidden; none of those failures is detected by a relevance score alone.

Separate authoritative data, cache freshness, index membership and query authorization. Compare lexical matching, vector similarity, fusion and explicit relationship traversal according to the questions they answer. Keep corpus version, configuration, judgments and negative queries together when evaluating the candidate.

## Questions and chapters

| Chapter | Owning question |
|---|---|
| [V06/C01 — Local and distributed caching](c01/README.md) | How do authority, freshness, eviction and invalidation differ? |
| [V06/C02 — Hot keys, cache stampedes and read amplification](c02/README.md) | When does adding a cache worsen recovery or contention? |
| [V06/C03 — Lexical full-text indexing and ranking](c03/README.md) | Which queries need tokenization, inverted indexes, BM25 or filtering? |
| [V06/C04 — Vector embeddings and nearest-neighbor retrieval](c04/README.md) | What are exact versus approximate search and recall trade-offs? |
| [V06/C05 — Hybrid retrieval and reranking](c05/README.md) | When do fusion and metadata filters improve measured relevance? |
| [V06/C06 — Graph relationships and traversal](c06/README.md) | When is explicit typed connectivity preferable to lexical or vector similarity? |
| [V06/C07 — Retrieval evaluation and index lifecycle](c07/README.md) | How are index freshness, reproducibility, latency and result quality measured? |

## Choosing a reading route

For a first reading, follow the chapter order. For diagnosis, connect the observed outcome to its authority and failure boundary using: [V06/C01](c01/README.md), [V06/C02](c02/README.md), [V06/C03](c03/README.md), [V06/C05](c05/README.md), [V06/C07](c07/README.md). Return to the exact page-local source ledger before making a version-specific claim.

Prerequisite context: V02/C02; V05/C03–C06.

Read [V02/C02](../v02/c02/README.md), [V05/C03](../v05/c03/README.md), [V05/C05](../v05/c05/README.md), [V05/C06](../v05/c06/README.md) for the named entry assumptions.

### Reasoning boundaries

This original conceptual map separates competing inputs rather than promising a universal solution.

~~~mermaid
flowchart TD
    Q["V06/C01 — Local and distributed caching"] --> M["V06/C02 — Hot keys, cache stampedes and read amplification"]
    Q --> E["Evidence and unknown inputs"]
    M --> D{"Meets the declared constraints?"}
    E --> D
    D -->|Supported| R["V06/C07 — Retrieval evaluation and index lifecycle"]
    D -->|Unresolved| U["Measure, revise or retain the baseline"]
~~~

Text alternative: establish local and distributed caching, compare hot keys, cache stampedes and read amplification with the available evidence, and either carry a supported result forward or return to unresolved inputs. The figure describes a reasoning route, not observed runtime behavior.

## Counterexample and handoff

Graph traversal is a subject of the book, not a requirement to create a curated Tycho graph. Approximate-neighbor recall and BM25 relevance do not establish source truth. Carry candidate-generation cost, invalidation storms and refresh lag into performance analysis, with an exact account of what each result can and cannot support.

## Navigation and source boundaries

| Route | Destination |
|---|---|
| Parent | [Book contents](../../README.md) |
| Previous volume | [V05](../v05/README.md) |
| Next volume | [V07](../v07/README.md) |
| Historical applications | [Casebook and synthetic playbooks](../../cases/README.md) |

## Evidence and known limits

The scenario is original synthetic reasoning. The chapters contain the accepted manuscript and its published evidence; no synthetic number or historical result is a measured prediction for another system. This new synthesis is editorially self-checked, not independently certified. Source-access restrictions, unexecuted technology experiments and original case denominators remain explicit in their owning pages. Product-specific adoption still requires compatible versions and the target workload.
