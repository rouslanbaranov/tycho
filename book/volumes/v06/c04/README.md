---
metadata_version: 1
id: "tycho.chapter.1c08d660af40408188c2d556f8d77358"
kind: "chapter"
parent_id: "tycho.volume.69e6229b222f4535bc0b3941cee1b1cc"
canonical_path: "book/volumes/v06/c04/README.md"
title: "V06/C04 — Vector embeddings and nearest-neighbor retrieval"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What are exact versus approximate search and recall trade-offs?"
route_hints:
  questions:
    - "What are exact versus approximate search and recall trade-offs?"
  prerequisites:
    - "tycho.chapter.5dc7b18369054daa852565a5dab2502b"
  related_ids: []
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

# V06/C04 — Vector embeddings and nearest-neighbor retrieval

## Purpose and mission

What are exact versus approximate search and recall trade-offs? This chapter owns that question within caching, indexing and information retrieval. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Evaluate embedding/version choices and approximate-neighbor recall against an exact reference and a relevant query set.

A nearby vector can be semantically plausible but wrong, stale or unauthorized; similarity is not proof of an answer. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Vector retrieval: exact distance, HNSW, IVF, filtering and pgvector/Faiss](vector-hnsw-faiss-pgvector.md) | What are exact versus approximate search and recall trade-offs? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. The retrieval contract begins before embeddings](vector-hnsw-faiss-pgvector.md#1-the-retrieval-contract-begins-before-embeddings).
- [2. Exact nearest neighbors are the reference baseline](vector-hnsw-faiss-pgvector.md#2-exact-nearest-neighbors-are-the-reference-baseline).
- [6. Failure cases and evaluation](vector-hnsw-faiss-pgvector.md#6-failure-cases-and-evaluation).
- [Source-to-claim evidence](vector-hnsw-faiss-pgvector.md#source-to-claim-evidence).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V06 — Caching, indexing and information retrieval](../README.md) |
| Previous | [V06/C03 — Lexical full-text indexing and ranking](../c03/README.md) |
| Next | [V06/C05 — Hybrid retrieval and reranking](../c05/README.md) |
| Prerequisite | [V06/C03 — Lexical full-text indexing and ranking](../c03/README.md) |
| Source reading | [Page-local evidence and versions](vector-hnsw-faiss-pgvector.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
