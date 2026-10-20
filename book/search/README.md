---
metadata_version: 1
id: "tycho.landing.4348c76938fc4d41b239721b94338436"
kind: "landing"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/search/README.md"
title: "Search and retrieval architecture"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
summary: "Reader entry for Search and retrieval architecture. Scope includes Question-driven reading route; Canonical research pages; Cross-domain context."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Search and retrieval architecture?"
  prerequisites: []
  related_ids:
    - "tycho.page.39a694d604d646a996bf90c3357c3b27"
    - "tycho.page.7a67fd6346a54eff97784465c22bbc74"
    - "tycho.page.d34afc7f27b54431b779f7f75f11e2c3"
    - "tycho.page.d79b0a48b30f4995a9bc110dbe691e52"
    - "tycho.page.359813d554c84da794a353d4416b8047"
    - "tycho.landing.be90d29e1bc04524b2ea41ee9beaab0f"
    - "tycho.landing.984c44f8dbd44d8e89105b4d31787636"
    - "tycho.landing.ddbfbbbe1a85406faa2705102378beea"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Search"
    - "and"
    - "retrieval"
    - "architecture"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
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

# Search and retrieval architecture

> Bounded public-source technical coverage for [Issue #85](https://github.com/rouslanbaranov/tycho/issues/85). These pages explain system-design methods; no production search cluster, vector index, agent-answer evaluation or deployed MCP endpoint is claimed.

## Purpose and mission

Enable readers and AI agents to find the **right canonical architecture knowledge with exact source evidence** by comparing lexical, semantic and metadata retrieval methods; graph traversal is discussed independently as a System Design option. Ranking speed alone does not establish answer correctness.

## Question-driven reading route

```mermaid
flowchart LR
    Q["Reader/agent question"] --> Lex["Exact lexical / BM25 search"]
    Q --> Dense["Vector / ANN retrieval"]
    Lex --> Fuse["Hybrid ranking and version filters"]
    Dense --> Fuse
    Fuse --> Evidence["Source revision and evidence checks"]
    Evidence --> Answer["Minimal sufficient context"]
```

Text alternative: exact tokens and vector similarity provide candidate sets, hybrid ranking merges them and source revisions are checked before assembling small evidence-backed context. This is a retrieval *design*, not live service architecture.

## Canonical research pages

| Question | Technical page | Evidence |
|---|---|---|
| How do inverted indexes, BM25, PostgreSQL FTS and Lucene differ? | [Lexical indexing, ranking and SQL FTS](../volumes/v06/c03/lexical-indexing-bm25-and-sql-fts.md) | PostgreSQL 17 FTS, Lucene 10.3 BM25 API |
| What are exact vs approximate vector search, HNSW, IVF, Faiss and pgvector? | [Vector/ANN and filtered retrieval](../volumes/v06/c04/vector-hnsw-faiss-pgvector.md) | Official pgvector/Faiss index guides; versioned caveats |
| When is a graph model and bounded traversal preferable to indexed relational joins? | [Graph data models and traversal](../volumes/v06/c06/graph-data-models-and-traversal.md) | V06/C06; graph architectures as a theoretical topic only, not a Tycho knowledge graph |
| How do relevance judgments, index freshness and answer evidence determine search quality? | [Retrieval evaluation and index lifecycle](../volumes/v06/c07/retrieval-evaluation-and-index-lifecycle.md) | V06/C07; NIST TREC/BEIR methods; no benchmark/index built |
| When does hybrid retrieval and graph expansion actually improve answer quality? | [Hybrid, graph and evaluation](../volumes/v06/c05/hybrid-ranking-graph-and-evaluation.md) | Elasticsearch RRF, Neo4j graph, pgvector and explicit evaluation protocol |

## Cross-domain context

- [Source-driven architecture foundations](../application/README.md).
- [PostgreSQL physical/query models](../data/README.md).
- [Architecture dependency and event semantics](../distributed/README.md).
- [25-question pilot methodology limits](../../evaluation/PILOT-ASSESSMENT.md).

These pages provide independent **System Design education** and knowledge for future index, retrieval and MCP work. No curated Tycho knowledge graph is required, planned or implemented. The actual Tycho knowledge index, embedded vectors, permission and source gates, query evaluation and shared Rocinante specialist are separate roadmap capabilities and must not be falsely marked completed.

## Unresolved experiments

Measure indexing size, update/rebuild speed, recall against independent judgments, freshness/tombstones, filtered ANN recall, p95/p99 under load, end-to-end answer correctness and output/input token cost. No universal search engine ranking is claimed.
