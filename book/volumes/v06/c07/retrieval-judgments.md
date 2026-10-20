---
metadata_version: 1
id: "tycho.page.4dbb361891e04ed4b48e421be85b3a26"
kind: "page"
parent_id: "tycho.chapter.e3cf27f8212a455bb53e135ee18bbaa9"
canonical_path: "book/volumes/v06/c07/retrieval-judgments.md"
title: "Judgments, metrics and matched retrieval baselines"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
summary: "Which relevance labels and query populations make variants comparable?"
route_hints:
  questions:
    - "Which relevance labels and query populations make variants comparable?"
  prerequisites:
    - "tycho.page.d79b0a48b30f4995a9bc110dbe691e52"
  related_ids:
    - "tycho.chapter.e3cf27f8212a455bb53e135ee18bbaa9"
    - "tycho.page.d79b0a48b30f4995a9bc110dbe691e52"
    - "tycho.page.990dac261357498fa433cf98e87817d3"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "retrieval"
    - "judgments"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.d79b0a48b30f4995a9bc110dbe691e52; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Judgments, metrics and matched retrieval baselines

**Owning question:** Which relevance labels and query populations make variants comparable?

This page belongs to [V06/C07 — Retrieval evaluation and index lifecycle](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.d79b0a48b30f4995a9bc110dbe691e52:1 -->
## 1. Build an evaluation set before choosing a vector model

A meaningful test set includes:
- exact entity identifiers, abbreviations and rare symbols;
- broader natural-language conceptual questions and synonyms;
- multi-part questions requiring more than one source;
- false friends: terms that match but describe a different version, system or meaning;
- negative/unanswerable questions with explicit expected no-result behavior;
- renamed/deleted content and contradictory editions;
- permission scopes where relevant, including restricted sections;
- changed documents and stale index refresh windows.

Document which users/questions the test represents. A dataset containing only automatically generated simple keyword queries cannot establish real expert search quality. Label questions and their relevant documents/sections with reviewer context and snapshot/version identity; disagreements and unjudged results remain uncertain.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.d79b0a48b30f4995a9bc110dbe691e52:2 -->
## 2. What ranking metrics actually measure

| Metric | Question it helps answer | Common misuse |
|---|---|---|
| Precision@k | How many of the top k retrieved items were judged relevant? | Treating unjudged as definitely irrelevant |
| Recall@k | How much of the judged relevant set appears in top k? | Assuming judgments include every relevant item |
| MRR@k | How early is the first relevant result found? | Using it when an answer needs many sources |
| nDCG@k | How good is ranking with graded relevance and position discount? | Treating grades as true probabilities or ignoring evaluation pool |
| Coverage/no-answer accuracy | Are necessary classes of queries and unsupported questions handled? | Scoring only queries with easy positives |
| End-to-end answer correctness | Does the synthesized answer use sufficient valid evidence? | Assuming retrieval relevance guarantees correct reasoning |
| Time to useful evidence | How quickly can an agent/person obtain verifiable source spans? | Only measuring raw index lookup latency |
| Cost per resolved task | CPU, storage, tokens/reads, maintenance and reindex effort per correct answer | Optimizing token count by suppressing necessary evidence |

For a given k, Precision@k = (judged relevant retrieved items in first k) / k. Recall@k uses a denominator of **all judged relevant items** under the chosen qrels. NIST TREC documentation makes clear that pooled judgments are assumptions/approximations for a particular collection, not an eternal complete map of relevance. BEIR's reported nDCG/MAP/Recall/Precision comparisons are benchmark procedures, not guaranteed results for another corpus.

### Original fictional example

Imagine five documents about a device's usage rules. A query has two judged relevant items. System A returns both relevant documents in positions 1 and 3; system B returns one relevant at position 1 and another outside top 5. Under the stated *complete fictional* judgments, Recall@5(A)=2/2=1 and Recall@5(B)=1/2=0.5. This says nothing by itself about trustworthiness, version freshness, citations or total user outcome.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.d79b0a48b30f4995a9bc110dbe691e52:3 -->
## 3. Lexical, vector and hybrid need matched comparisons

A defensible comparison uses the **same source snapshot, chunk/section boundaries, qrels, permission filters and evaluation queries** where possible. Normalize only what the task requires. For each candidate report:
- index build/update time, disk size and RAM;
- p50/p95/p99 query time under controlled concurrent demand;
- freshness lag and deletion/revocation latency;
- Precision/Recall/nDCG under fixed judgments;
- handling of exact symbols and negative questions;
- citation/source span recoverability;
- operational cost and maintenance failure modes.

Lexical retrieval may excel for exact identifiers; vector retrieval may help vocabulary mismatch; hybrid fusion/reranking can combine evidence but adds complexity and needs benchmarking. Neither semantic similarity nor “top result found” certifies that a source supports the requested claim. Read [BM25 and inverted indexes](../c03/lexical-indexing-bm25-and-sql-fts.md), [vector/ANN](../c04/vector-hnsw-faiss-pgvector.md) and [hybrid ranking](../c05/hybrid-ranking-graph-and-evaluation.md).

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](retrieval-evaluation-and-index-lifecycle.md) |
| Next | [Continue the reasoning](snapshot-access.md) |
| Integrated question | [Original scenario and limits](retrieval-evaluation-and-index-lifecycle.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
