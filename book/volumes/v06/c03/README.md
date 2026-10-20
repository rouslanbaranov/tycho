---
metadata_version: 1
id: "tycho.chapter.5dc7b18369054daa852565a5dab2502b"
kind: "chapter"
parent_id: "tycho.volume.69e6229b222f4535bc0b3941cee1b1cc"
canonical_path: "book/volumes/v06/c03/README.md"
title: "V06/C03 — Lexical full-text indexing and ranking"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which queries need tokenization, inverted indexes, BM25 or filtering?"
route_hints:
  questions:
    - "Which queries need tokenization, inverted indexes, BM25 or filtering?"
  prerequisites:
    - "tycho.chapter.1035327a459242b78329b41b8fddfee6"
  related_ids:
    - "tycho.chapter.6d25a036c078402a85ec464227a48a31"
    - "tycho.chapter.e3cf27f8212a455bb53e135ee18bbaa9"
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

| Page | Owning question |
|---|---|
| [Lexical retrieval: inverted indexes, BM25, PostgreSQL FTS and Lucene](lexical-indexing-bm25-and-sql-fts.md) | Which queries need tokenization, inverted indexes, BM25 or filtering? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Why inverted indexes work](lexical-indexing-bm25-and-sql-fts.md#1-why-inverted-indexes-work).
- [2. PostgreSQL 17 full-text search is a real candidate](lexical-indexing-bm25-and-sql-fts.md#2-postgresql-17-full-text-search-is-a-real-candidate).
- [Engineering walkthrough — Analyzer compatibility and a stale index generation](lexical-indexing-bm25-and-sql-fts.md#engineering-walkthrough-analyzer-compatibility-and-a-stale-index-generation).
- [Evidence and status](lexical-indexing-bm25-and-sql-fts.md#evidence-and-status).

## Boundaries and further reading

- [V06/C05 — Hybrid retrieval and reranking](../c05/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.
- [V06/C07 — Retrieval evaluation and index lifecycle](../c07/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V06 — Caching, indexing and information retrieval](../README.md) |
| Previous | [V06/C02 — Hot keys, cache stampedes and read amplification](../c02/README.md) |
| Next | [V06/C04 — Vector embeddings and nearest-neighbor retrieval](../c04/README.md) |
| Prerequisite | [V06/C02 — Hot keys, cache stampedes and read amplification](../c02/README.md) |
| Source reading | [Page-local evidence and versions](lexical-indexing-bm25-and-sql-fts.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
