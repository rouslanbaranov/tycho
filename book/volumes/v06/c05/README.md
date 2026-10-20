---
metadata_version: 1
id: "tycho.chapter.6d25a036c078402a85ec464227a48a31"
kind: "chapter"
parent_id: "tycho.volume.69e6229b222f4535bc0b3941cee1b1cc"
canonical_path: "book/volumes/v06/c05/README.md"
title: "V06/C05 — Hybrid retrieval and reranking"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "When do fusion and metadata filters improve measured relevance?"
route_hints:
  questions:
    - "When do fusion and metadata filters improve measured relevance?"
  prerequisites:
    - "tycho.chapter.1c08d660af40408188c2d556f8d77358"
  related_ids:
    - "tycho.chapter.5dc7b18369054daa852565a5dab2502b"
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

# V06/C05 — Hybrid retrieval and reranking

## Purpose and mission

When do fusion and metadata filters improve measured relevance? This chapter owns that question within caching, indexing and information retrieval. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Compare fusion and reranking with constituent retrieval baselines under the same filters, judgments and budgets.

Combining rankings cannot repair a missing authorized document or an invalid relevance assessment. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Hybrid retrieval, graph expansion, reranking and evidence-quality evaluation](hybrid-ranking-graph-and-evaluation.md) | When do fusion and metadata filters improve measured relevance? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Retrieval has multiple independent signals](hybrid-ranking-graph-and-evaluation.md#1-retrieval-has-multiple-independent-signals).
- [2. Reciprocal Rank Fusion handles incompatible score scales](hybrid-ranking-graph-and-evaluation.md#2-reciprocal-rank-fusion-handles-incompatible-score-scales).
- [Engineering walkthrough — Hand-computed rank fusion and a false evidence match](hybrid-ranking-graph-and-evaluation.md#engineering-walkthrough-hand-computed-rank-fusion-and-a-false-evidence-match).
- [Evidence ledger and implementation boundaries](hybrid-ranking-graph-and-evaluation.md#evidence-ledger-and-implementation-boundaries).

## Boundaries and further reading

- [V06/C03 — Lexical full-text indexing and ranking](../c03/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.
- [V06/C07 — Retrieval evaluation and index lifecycle](../c07/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V06 — Caching, indexing and information retrieval](../README.md) |
| Previous | [V06/C04 — Vector embeddings and nearest-neighbor retrieval](../c04/README.md) |
| Next | [V06/C06 — Graph relationships and traversal](../c06/README.md) |
| Prerequisite | [V06/C04 — Vector embeddings and nearest-neighbor retrieval](../c04/README.md) |
| Source reading | [Page-local evidence and versions](hybrid-ranking-graph-and-evaluation.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
