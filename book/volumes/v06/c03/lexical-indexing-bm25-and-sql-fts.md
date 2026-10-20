---
metadata_version: 1
id: "tycho.page.39a694d604d646a996bf90c3357c3b27"
kind: "page"
parent_id: "tycho.chapter.5dc7b18369054daa852565a5dab2502b"
canonical_path: "book/volumes/v06/c03/lexical-indexing-bm25-and-sql-fts.md"
title: "Lexical retrieval: inverted indexes, BM25, PostgreSQL FTS and Lucene"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Lexical full-text indexing and ranking. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which queries need tokenization, inverted indexes, BM25 or filtering?"
  prerequisites: []
  related_ids:
    - "tycho.page.359813d554c84da794a353d4416b8047"
    - "tycho.page.fa9fbde428884786b68dbfdf142cb1ad"
    - "tycho.page.0ea71c3228744d0c99a3e4826b9167ad"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Lexical"
    - "retrieval"
    - "inverted"
    - "indexes"
    - "BM25"
    - "PostgreSQL"
    - "FTS"
    - "and"
    - "Lucene"
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
<!-- tycho-question-source:tycho.page.39a694d604d646a996bf90c3357c3b27:-1 -->

# Lexical retrieval: inverted indexes, BM25, PostgreSQL FTS and Lucene

> Technical research for Tycho [Issue #85](https://github.com/rouslanbaranov/tycho/issues/85). Public source reading 2026-10-19; PostgreSQL docs **17**, Lucene concepts/version references as explicitly cited. Entirely original illustrations and synthetic examples, not a search deployment or benchmark.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.39a694d604d646a996bf90c3357c3b27:0 -->
## Purpose and mission

Technical documents contain precise symbols: class names, APIs, issue IDs, error codes, configuration keys and product versions. A lexical index preserves this exact-token evidence and can answer questions poorly served by paraphrase-only similarity. But word overlap alone cannot guarantee that a retrieved page explains the requested architecture, version or failure behavior.

**Primary question:** How do tokenization, postings, field weighting, ranking and index update mechanisms affect the quality and freshness of retrieving technical knowledge?

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.39a694d604d646a996bf90c3357c3b27:6 -->
## Engineering walkthrough — Analyzer compatibility and a stale index generation

**Original fictional search:** an engineer queries `Http2GoAwayException` and expects a document containing that exact symbol. A tokenizer that splits CamelCase or punctuation differently between indexing and searching may miss an otherwise relevant record. Stemming can help natural-language variants but can also reduce exact API-symbol fidelity. A raw query string is not an immutable analysis contract.

| Option | Fit condition | Negative example |
|---|---|---|
| PostgreSQL 17 FTS | Operational simplicity and suitable token dictionaries/query workload | Exact code identifier lost by text-search tokenization |
| Lucene inverted index/BM25 | Tunable per-field analyzers, term ranking and index lifecycle | Analyzer version mismatch between old and new generations |
| Exact term/keyword field | Exception/API identifier lookup | Pure keyword matching misses synonyms and explanations |

**Index transition:** an API document changes from revision R1 to R2, removing the old identifier. An index rebuild publishes R2 content but an old cache still returns a R1 citation. A high BM25 rank is not evidence that R1 remains authoritative. Bind results to an index generation and source revision; invalidate stale snippets and offer an exact-source fallback when generation comparison fails.

The existing PostgreSQL FTS and Lucene BM25 documentation specify ranking/analyzer mechanisms, not quality for this made-up corpus. **Proposed, not executed:** define human-judged questions that include code symbols, morphological variants and deprecated terms; evaluate keyword, FTS and Lucene under a frozen analyzer/version snapshot, while deliberately injecting stale citations. Choose lexical/hybrid retrieval based on eligible relevance and operational freshness, not headline index technology.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Match tokenization, inverted-index ranking and authorization filters to the actual query contract.

Lexical relevance is not source validity, and filtering too late can expose forbidden records or distort the candidate set.

The detailed pages separate the mechanisms that make this decision conditional:

- [Inverted indexes and SQL full-text search](lexical-model.md) — How do analyzer and query semantics define a lexical match?
- [Search clusters, update visibility and stale citations](index-lifecycle.md) — Which generation and refresh contract keeps retrieved evidence attributable?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
