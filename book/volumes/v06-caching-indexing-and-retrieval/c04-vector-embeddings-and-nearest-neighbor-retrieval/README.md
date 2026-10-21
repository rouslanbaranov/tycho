---
metadata_version: 1
id: "tycho.chapter.1c08d660af40408188c2d556f8d77358"
kind: "chapter"
parent_id: "tycho.volume.69e6229b222f4535bc0b3941cee1b1cc"
canonical_path: "book/volumes/v06-caching-indexing-and-retrieval/c04-vector-embeddings-and-nearest-neighbor-retrieval/README.md"
title: "V06/C04 — Vector embeddings and nearest-neighbor retrieval"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What are exact versus approximate search and recall trade-offs? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "What are exact versus approximate search and recall trade-offs?"
  prerequisites:
    - "tycho.chapter.5dc7b18369054daa852565a5dab2502b"
  related_ids:
    - "tycho.page.7a67fd6346a54eff97784465c22bbc74"
    - "tycho.page.66d2977575264168a8616e09d0900af6"
    - "tycho.page.9145b7ce81d4461b90d3c6285128c18a"
    - "tycho.page.411a855b84384e86b3b7fb60a3f63464"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](vector-hnsw-faiss-pgvector.md) | What are exact versus approximate search and recall trade-offs? |
| [Embedding contracts and approximate-neighbor trade-offs](exact-ann.md) | What exact reference and workload define acceptable ANN recall? |
| [Filtering, authorization and recall](vector-filters.md) | How can filtering change the available neighbor set without granting access? |
| [Vector engine selection and failure evaluation](vector-architecture.md) | Which lifecycle and operating constraints distinguish an index library from a serving system? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V06 — Caching, indexing and information retrieval](../README.md) |
| Previous | [V06/C03 — Lexical full-text indexing and ranking](../c03-lexical-full-text-indexing-and-ranking/README.md) |
| Next | [V06/C05 — Hybrid retrieval and reranking](../c05-hybrid-retrieval-and-reranking/README.md) |
| Prerequisite | [V06/C03 — Lexical full-text indexing and ranking](../c03-lexical-full-text-indexing-and-ranking/README.md) |
| Source reading | [Page-local evidence and versions](vector-hnsw-faiss-pgvector.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.7a67fd6346a54eff97784465c22bbc74:7 -->
## Source-to-claim evidence

| ID | Primary public source / exact inspected scope | Supports, not empirical Tycho outcomes |
|---|---|---|
| E01 | [pgvector project README](https://github.com/pgvector/pgvector), *Indexing, HNSW, IVFFlat, Filtering, Iterative Index Scans, Hybrid Search*, rolling main revision observed 2026-10-19 | Exact default and ANN choices, candidate postfilter and tuning features; pin tag before deployed version-specific instructions |
| E02 | [Faiss Indexes](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes), table of method classes, HNSW, IVF and PQ; wiki inspected 2026-10-19 | Index family properties, not an installed managed search service |
| E03 | [Faiss Index factory](https://github.com/facebookresearch/faiss/wiki/The-index-factory), IVF/PQ/HNSW construction overview | Index composition, not measured universal index ranking |

No embeddings were generated, model API invoked, index built, recall computed or human relevance annotated for this page; all numeric examples are synthetic.
<!-- /tycho-question-source -->
