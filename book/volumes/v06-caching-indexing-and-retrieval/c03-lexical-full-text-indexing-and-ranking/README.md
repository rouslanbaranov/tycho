---
metadata_version: 1
id: "tycho.chapter.5dc7b18369054daa852565a5dab2502b"
kind: "chapter"
parent_id: "tycho.volume.69e6229b222f4535bc0b3941cee1b1cc"
canonical_path: "book/volumes/v06-caching-indexing-and-retrieval/c03-lexical-full-text-indexing-and-ranking/README.md"
title: "V06/C03 — Lexical full-text indexing and ranking"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which queries need tokenization, inverted indexes, BM25 or filtering? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Which queries need tokenization, inverted indexes, BM25 or filtering?"
  prerequisites:
    - "tycho.chapter.1035327a459242b78329b41b8fddfee6"
  related_ids:
    - "tycho.chapter.6d25a036c078402a85ec464227a48a31"
    - "tycho.chapter.e3cf27f8212a455bb53e135ee18bbaa9"
    - "tycho.page.39a694d604d646a996bf90c3357c3b27"
    - "tycho.page.fa9fbde428884786b68dbfdf142cb1ad"
    - "tycho.page.0ea71c3228744d0c99a3e4826b9167ad"
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

# V06/C03 — Lexical full-text indexing and ranking

## Purpose and mission

Which queries need tokenization, inverted indexes, BM25 or filtering? This chapter owns that question within caching, indexing and information retrieval. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Match tokenization, inverted-index ranking and authorization filters to the actual query contract.

Lexical relevance is not source validity, and filtering too late can expose forbidden records or distort the candidate set. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](lexical-indexing-bm25-and-sql-fts.md) | Which queries need tokenization, inverted indexes, BM25 or filtering? |
| [Inverted indexes and SQL full-text search](lexical-model.md) | How do analyzer and query semantics define a lexical match? |
| [Search clusters, update visibility and stale citations](index-lifecycle.md) | Which generation and refresh contract keeps retrieved evidence attributable? |

## Boundaries and further reading

- [V06/C05 — Hybrid retrieval and reranking](../c05-hybrid-retrieval-and-reranking/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.
- [V06/C07 — Retrieval evaluation and index lifecycle](../c07-retrieval-evaluation-and-index-lifecycle/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V06 — Caching, indexing and information retrieval](../README.md) |
| Previous | [V06/C02 — Hot keys, cache stampedes and read amplification](../c02-hot-keys-cache-stampedes-and-read-amplification/README.md) |
| Next | [V06/C04 — Vector embeddings and nearest-neighbor retrieval](../c04-vector-embeddings-and-nearest-neighbor-retrieval/README.md) |
| Prerequisite | [V06/C02 — Hot keys, cache stampedes and read amplification](../c02-hot-keys-cache-stampedes-and-read-amplification/README.md) |
| Source reading | [Page-local evidence and versions](lexical-indexing-bm25-and-sql-fts.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.39a694d604d646a996bf90c3357c3b27:7 -->
## Evidence and status

| ID | Public source and bounded examined scope | Supports and limitations |
|---|---|---|
| E01 | [PostgreSQL 17 §12.3 Controlling Text Search](https://www.postgresql.org/docs/17/textsearch-controls.html), **Parsing Queries, Ranking Search Results**; [Chapter 12 indexes](https://www.postgresql.org/docs/17/textsearch-indexes.html) | tsvector/tsquery, scoring and index support; no Tycho benchmark |
| E02 | [Apache Lucene BM25Similarity API](https://lucene.apache.org/core/10_3_0/core/org/apache/lucene/search/similarities/BM25Similarity.html), selected **10.3.0** API | BM25 scorer as one versioned library implementation; full Lucene indexing docs not independently read end-to-end |
| E03 | [Lucene Overview](https://lucene.apache.org/core/10_3_0/core/overview-summary.html), selected 10.3.0 | In-process full-text indexing/search APIs, not a managed distributed product deployment |

**Review state:** original model with bounded official docs, no Lucene index built, PostgreSQL search executed, relevance judged by external annotators or human technical review. Full benchmark and choice remain future issues.
<!-- /tycho-question-source -->
