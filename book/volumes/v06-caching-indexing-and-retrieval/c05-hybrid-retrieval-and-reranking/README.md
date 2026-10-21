---
metadata_version: 1
id: "tycho.chapter.6d25a036c078402a85ec464227a48a31"
kind: "chapter"
parent_id: "tycho.volume.69e6229b222f4535bc0b3941cee1b1cc"
canonical_path: "book/volumes/v06-caching-indexing-and-retrieval/c05-hybrid-retrieval-and-reranking/README.md"
title: "V06/C05 — Hybrid retrieval and reranking"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "When do fusion and metadata filters improve measured relevance? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "When do fusion and metadata filters improve measured relevance?"
  prerequisites:
    - "tycho.chapter.1c08d660af40408188c2d556f8d77358"
  related_ids:
    - "tycho.chapter.5dc7b18369054daa852565a5dab2502b"
    - "tycho.chapter.e3cf27f8212a455bb53e135ee18bbaa9"
    - "tycho.page.359813d554c84da794a353d4416b8047"
    - "tycho.page.b919c3c84861491c82334b6e00bf443e"
    - "tycho.page.5bee1736b2fe4418af5c50587ee4fbb0"
    - "tycho.page.a4335241afc0408d9e137bc2a027ebed"
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

# V06/C05 — Hybrid retrieval and reranking

## Purpose and mission

When do fusion and metadata filters improve measured relevance? This chapter owns that question within caching, indexing and information retrieval. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Compare fusion and reranking with constituent retrieval baselines under the same filters, judgments and budgets.

Combining rankings cannot repair a missing authorized document or an invalid relevance assessment. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](hybrid-ranking-graph-and-evaluation.md) | When do fusion and metadata filters improve measured relevance? |
| [Retrieval signals and rank fusion](fusion-signals.md) | How does rank fusion combine rankings without treating scores as comparable probabilities? |
| [Traversal, evidence and calibrated refusal](evidence-refusal.md) | Which relation or passage supports an answer and when should a system refuse? |
| [Hybrid evaluation and snapshot consistency](hybrid-evaluation.md) | What matched judgments and snapshot boundaries make an evaluation reproducible? |

## Boundaries and further reading

- [V06/C03 — Lexical full-text indexing and ranking](../c03-lexical-full-text-indexing-and-ranking/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.
- [V06/C07 — Retrieval evaluation and index lifecycle](../c07-retrieval-evaluation-and-index-lifecycle/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V06 — Caching, indexing and information retrieval](../README.md) |
| Previous | [V06/C04 — Vector embeddings and nearest-neighbor retrieval](../c04-vector-embeddings-and-nearest-neighbor-retrieval/README.md) |
| Next | [V06/C06 — Graph relationships and traversal](../c06-graph-relationships-and-traversal/README.md) |
| Prerequisite | [V06/C04 — Vector embeddings and nearest-neighbor retrieval](../c04-vector-embeddings-and-nearest-neighbor-retrieval/README.md) |
| Source reading | [Page-local evidence and versions](hybrid-ranking-graph-and-evaluation.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.359813d554c84da794a353d4416b8047:8 -->
## Engineering walkthrough — Hand-computed rank fusion and a false evidence match

**Original synthetic example:** lexical search ranks documents A, B, C; semantic search ranks C, D, A. Using Reciprocal Rank Fusion with illustrative `k=60`, the score for A is `1/61 + 1/63 ≈ 0.03227`; for C it is `1/63 + 1/61 ≈ 0.03227`; B and D each contribute one list hit. A and C tie under these assumptions, **without any claim that either is factually correct**. Different handling of missing ranks, duplicate IDs or list truncation changes the result.

A restricted document can be top-ranked in one retriever: fusion must not reveal its title or score through results, explanations or related links. Reranking may improve relevance for permitted candidate texts but cannot repair a source-revision mismatch or transform a speculative claim into published evidence. The [Elasticsearch RRF reference](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion) defines the general rank-only fusion mechanism; actual feature/version requirements must be pinned for production.

| Stage | Necessary gate | Failure consequence |
|---|---|---|
| Retrieve lexical/vector candidates | Source snapshot and permission scope | Authorized evidence omitted or forbidden text leaked |
| Fuse ranks | Stable identity and declared missing-rank behavior | Duplicate content treated as independent corroboration |
| Rerank | Preserve source boundaries and disclose heuristic nature | Plausible but stale claim promoted over current authority |
| Answer | Verify material claims against original source/version | Confident answer when evidence is insufficient |

**Proposed experiment, not run:** hand-verify small fusion scores, then evaluate real held-out questions with authorized judgment sets and deliberately contradictory/stale snippets. If relevant sources remain absent, **refuse a substantive architectural conclusion and request evidence** instead of increasing model confidence or traversal depth.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.359813d554c84da794a353d4416b8047:9 -->
## Evidence ledger and implementation boundaries

| ID | Public primary source / examined scope | Supports / exclusions |
|---|---|---|
| E01 | [Elasticsearch Reciprocal Rank Fusion reference](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion), RRF score equation and multi-retriever combination; rolling docs observed 2026-10-19 | Rank fusion semantics; no Tycho benchmark |
| E02 | [Neo4j property graph concepts](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/), *Node, Relationship, Schema* | Typed directional edges as a graph model, not a verified Tycho relationship dataset |
| E03 | [PostgreSQL 17 FTS ranking](https://www.postgresql.org/docs/17/textsearch-controls.html), §12.3.3 | Application-dependent lexical rank and structured weighting |
| E04 | [pgvector official README](https://github.com/pgvector/pgvector), exact vs ANN, filtered search and hybrid notes; rolling revision observed 2026-10-19 | Candidate generation mechanics, not search or agent-answer superiority |

**Review status:** conceptual evaluation method only; no full Tycho hybrid engine, graph traversal service, LLM answer evaluation, ranking judgment, cost measurement or independent reviewer approval has been implemented by this issue.
<!-- /tycho-question-source -->
