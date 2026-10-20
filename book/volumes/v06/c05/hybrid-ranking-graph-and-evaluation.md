---
metadata_version: 1
id: "tycho.page.359813d554c84da794a353d4416b8047"
kind: "page"
parent_id: "tycho.chapter.6d25a036c078402a85ec464227a48a31"
canonical_path: "book/volumes/v06/c05/hybrid-ranking-graph-and-evaluation.md"
title: "Hybrid retrieval, graph expansion, reranking and evidence-quality evaluation"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Hybrid retrieval and reranking. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "When do fusion and metadata filters improve measured relevance?"
  prerequisites: []
  related_ids:
    - "tycho.page.39a694d604d646a996bf90c3357c3b27"
    - "tycho.page.7a67fd6346a54eff97784465c22bbc74"
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.9176c39f97f544f884666e291ae38b90"
    - "tycho.landing.73dff529d70048569efef74bffa88b00"
    - "tycho.page.b919c3c84861491c82334b6e00bf443e"
    - "tycho.page.5bee1736b2fe4418af5c50587ee4fbb0"
    - "tycho.page.a4335241afc0408d9e137bc2a027ebed"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Hybrid"
    - "retrieval"
    - "graph"
    - "expansion"
    - "reranking"
    - "and"
    - "evidence-quality"
    - "evaluation"
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
<!-- tycho-question-source:tycho.page.359813d554c84da794a353d4416b8047:-1 -->

# Hybrid retrieval, graph expansion, reranking and evidence-quality evaluation

> Tycho technical research for [Issue #85](https://github.com/rouslanbaranov/tycho/issues/85); inspected public Elasticsearch RRF, PostgreSQL text search, pgvector and Neo4j graph concepts on 2026-10-19. Original algorithms/diagrams and **synthetic** examples only. No deployed retrieval server or independently judged quality benchmark is claimed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.359813d554c84da794a353d4416b8047:0 -->
## Purpose and mission

A good knowledge-search system answers *why*, *under which constraints* and *according to which source*—not merely "what documents have similar words". AI agents also have a token budget: returning 30 whole chapters can be less useful than a precise primary page plus its dependency/source anchors.

**Primary question:** How can lexical, semantic, metadata and graph signals be combined while measuring relevance, grounding, freshness, latency, resource cost and total tokens rather than ranking a system by queries per second alone?

<!-- /tycho-question-source -->

## Integrated decision and reading route

Compare fusion and reranking with constituent retrieval baselines under the same filters, judgments and budgets.

Combining rankings cannot repair a missing authorized document or an invalid relevance assessment.

The detailed pages separate the mechanisms that make this decision conditional:

- [Retrieval signals and rank fusion](fusion-signals.md) — How does rank fusion combine rankings without treating scores as comparable probabilities?
- [Traversal, evidence and calibrated refusal](evidence-refusal.md) — Which relation or passage supports an answer and when should a system refuse?
- [Hybrid evaluation and snapshot consistency](hybrid-evaluation.md) — What matched judgments and snapshot boundaries make an evaluation reproducible?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
