---
metadata_version: 1
id: "tycho.page.7a67fd6346a54eff97784465c22bbc74"
kind: "page"
parent_id: "tycho.chapter.1c08d660af40408188c2d556f8d77358"
canonical_path: "book/volumes/v06/c04/vector-hnsw-faiss-pgvector.md"
title: "Vector retrieval: exact distance, HNSW, IVF, filtering and pgvector/Faiss"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Vector embeddings and nearest-neighbor retrieval. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "What are exact versus approximate search and recall trade-offs?"
  prerequisites: []
  related_ids:
    - "tycho.page.66d2977575264168a8616e09d0900af6"
    - "tycho.page.9145b7ce81d4461b90d3c6285128c18a"
    - "tycho.page.411a855b84384e86b3b7fb60a3f63464"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Vector"
    - "retrieval"
    - "exact"
    - "distance"
    - "HNSW"
    - "IVF"
    - "filtering"
    - "and"
    - "pgvector/Faiss"
evidence_scope:
  source_ids:
    - "src.pgvector"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-18"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.7a67fd6346a54eff97784465c22bbc74:-1 -->

# Vector retrieval: exact distance, HNSW, IVF, filtering and pgvector/Faiss

> Tycho [Issue #85](https://github.com/rouslanbaranov/tycho/issues/85), independent official/public-source review on **2026-10-19**. Examples and diagrams are original. Versioned pgvector and Faiss claims are scoped to the *public documentation inspected*, not a claimed running database, embedding API or benchmark.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7a67fd6346a54eff97784465c22bbc74:0 -->
## Purpose and mission

A semantic embedding maps text, code or another input to a numerical vector. A distance operation can identify **nearby representations** but says nothing by itself about technical truth, source freshness, ACLs or correctness of a proposed architecture. Approximate nearest-neighbor (ANN) indexing exchanges some accuracy or operational cost for latency/throughput trade-offs.

**Primary question:** How should a system select exact/vector index strategies, measure ANN recall and candidate filtering effects, and preserve precise source evidence when using embeddings in a knowledge book?

<!-- /tycho-question-source -->

## Integrated decision and reading route

Evaluate embedding/version choices and approximate-neighbor recall against an exact reference and a relevant query set.

A nearby vector can be semantically plausible but wrong, stale or unauthorized; similarity is not proof of an answer.

The detailed pages separate the mechanisms that make this decision conditional:

- [Embedding contracts and approximate-neighbor trade-offs](exact-ann.md) — What exact reference and workload define acceptable ANN recall?
- [Filtering, authorization and recall](vector-filters.md) — How can filtering change the available neighbor set without granting access?
- [Vector engine selection and failure evaluation](vector-architecture.md) — Which lifecycle and operating constraints distinguish an index library from a serving system?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
