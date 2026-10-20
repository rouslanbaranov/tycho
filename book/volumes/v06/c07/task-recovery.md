---
metadata_version: 1
id: "tycho.page.5f1fe7b87ce443889dd4662fe845794a"
kind: "page"
parent_id: "tycho.chapter.e3cf27f8212a455bb53e135ee18bbaa9"
canonical_path: "book/volumes/v06/c07/task-recovery.md"
title: "End-to-end evaluation and index recovery"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
summary: "What distinguishes ranking quality from a correct information task?"
route_hints:
  questions:
    - "What distinguishes ranking quality from a correct information task?"
  prerequisites:
    - "tycho.page.990dac261357498fa433cf98e87817d3"
  related_ids:
    - "tycho.chapter.e3cf27f8212a455bb53e135ee18bbaa9"
    - "tycho.page.d79b0a48b30f4995a9bc110dbe691e52"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "task"
    - "recovery"
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
# End-to-end evaluation and index recovery

**Owning question:** What distinguishes ranking quality from a correct information task?

This page belongs to [V06/C07 — Retrieval evaluation and index lifecycle](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.d79b0a48b30f4995a9bc110dbe691e52:6 -->
## 6. Evaluate the end-to-end information task

An agent may retrieve one compact entry card and then fetch targeted source spans instead of loading 100 documents. This can reduce cost while preserving quality *if* the end answer is correct and has sufficient cited evidence.

A proposed evaluation would compare:
1. Retrieval Recall@k and relevance position on the same corpus.
2. End-to-end answered-task success, including correct no-answer outcomes.
3. Citation validity at exact source section/revision, independently judged.
4. Number of tokens/section reads and latency through the *complete* decision.
5. Permission, deleted-source, contradictory-version and overload cases.
6. Index generation/retention disk and refresh expense.
7. Correctness after a corpus edit or new source snapshot.

A method producing fewer tokens but worse claim support has **failed** a correctness gate, even if its query latency is lower. Likewise, reporting a high Recall@k on a toy dataset is not proof that human readers can answer practical architecture questions.


### Worked evaluation: a correct-looking rank list can fail authorization and citation freshness

**Original hypothetical test set:** twenty engineering questions have relevance judgments created from a **frozen, authorized corpus snapshot**. One question requests a tenant-specific account-ownership mechanism. A lexical engine returns the only exact authorized canonical section at rank 3; an ANN engine returns two semantically similar but non-authorized records at ranks 1–2, and a hybrid retriever returns an obsolete revision at rank 1. These are invented rankings for method explanation, not a Tycho index run.

A meaningful evaluation needs **three separate correctness gates**:

| Gate | Denominator and observation | Example failure |
|---|---|---|
| Eligible retrieval relevance | Judged **authorized** relevant documents for each question; report Recall@k and nDCG@k with unjudged handling declared | High global semantic similarity hides the only eligible owner |
| Access correctness | All exposed hits, titles, snippets, links and downstream expansions | Even one unauthorized preview is unacceptable regardless of nDCG |
| Citation/source freshness | Retrieved claim's source revision and canonical document generation at query time | High-ranking old citation supports a removed API contract |

For a simple manual illustration, if a query has two judged eligible relevant documents and only one appears in the first five results, eligible Recall@5 is **1/2**, not "five results returned". Without a complete judgment pool one must disclose that this is recall **against known judgments**, not absolute relevance. A 20-question corpus is much too small to claim general search quality for a broad book.

**Failure/recovery:** after a source edit or permission change, an index generation may temporarily contain old content. Rebuild or delta-update from a pinned snapshot, verify that tombstoned paths and revoked scopes cannot be served through old caches, then atomically publish a coherent generation. If ACL filtering or source revision cannot be trusted, **fail closed** for affected content instead of returning a confident answer from a stale snippet. A lexical fallback can preserve access to exact terms when embeddings drift, but it still must satisfy access and provenance gates.

The [TREC relevance-judgments resource](https://trec.nist.gov/data/reljudge_eng.html) illustrates qrels and judgments; [BEIR](https://github.com/beir-cellar/beir) offers reproducible evaluation methods. Neither establishes a benchmark score or index quality for Tycho. **No corpus evaluation, index rebuild, experiment or answer-quality study was executed.** This chapter owns retrieval evaluation; [ANN](../c04/vector-hnsw-faiss-pgvector.md) owns filtered nearest-neighbor mechanics and [security](../../v09/c07/safe-agent-access-and-knowledge-isolation.md) owns permissions.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.d79b0a48b30f4995a9bc110dbe691e52:7 -->
## 7. Failure and recovery

| Failure | Safe behavior or required repair |
|---|---|
| Mid-build crash | Retain known-good index generation; resume/rebuild with explicit source snapshot |
| New source revision | Publish valid new index only after integrity and retrieval smoke checks |
| Deleted/revoked source | Stop unauthorized exposure and invalidate caches/index references according to policy |
| Embedding/model change | Rebuild compatible vectors; compare exact/semantic benchmark results rather than mixing spaces |
| Missing qrels | Label judgment gap, do not count all unjudged documents as false |
| Index overload | Bound result size/work, explicit errors, no silently truncated relevant evidence |
| Source citation no longer resolves | Show unresolved evidence, do not invent a matching source |

These scenarios are proposed requirements, not observed incidents.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](snapshot-access.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](retrieval-evaluation-and-index-lifecycle.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
