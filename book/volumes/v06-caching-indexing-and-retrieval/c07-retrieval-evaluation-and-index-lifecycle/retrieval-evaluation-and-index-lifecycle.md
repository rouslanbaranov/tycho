---
metadata_version: 1
id: "tycho.page.d79b0a48b30f4995a9bc110dbe691e52"
kind: "page"
parent_id: "tycho.chapter.e3cf27f8212a455bb53e135ee18bbaa9"
canonical_path: "book/volumes/v06-caching-indexing-and-retrieval/c07-retrieval-evaluation-and-index-lifecycle/retrieval-evaluation-and-index-lifecycle.md"
title: "Retrieval evaluation and index lifecycle: relevance, freshness and evidence budgets"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Retrieval evaluation and index lifecycle. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How are index freshness, reproducibility, latency and result quality measured?"
  prerequisites: []
  related_ids:
    - "tycho.page.39a694d604d646a996bf90c3357c3b27"
    - "tycho.page.7a67fd6346a54eff97784465c22bbc74"
    - "tycho.page.359813d554c84da794a353d4416b8047"
    - "tycho.page.0ae1aabac3b64c2f924cc427684bdbab"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.4348c76938fc4d41b239721b94338436"
    - "tycho.page.d34afc7f27b54431b779f7f75f11e2c3"
    - "tycho.page.4dbb361891e04ed4b48e421be85b3a26"
    - "tycho.page.990dac261357498fa433cf98e87817d3"
    - "tycho.page.5f1fe7b87ce443889dd4662fe845794a"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Retrieval"
    - "evaluation"
    - "and"
    - "index"
    - "lifecycle"
    - "relevance"
    - "freshness"
    - "evidence"
    - "budgets"
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
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.d79b0a48b30f4995a9bc110dbe691e52:-1 -->

# Retrieval evaluation and index lifecycle: relevance, freshness and evidence budgets

> **Tycho System Design book manuscript V06/C07, 2026-10-19.** This describes evaluating *any* information retrieval system. It does not implement Tycho's ranked retrieval, embeddings, MCP or a curated graph. Public TREC/NIST and BEIR methodologies are cited; all queries, metrics and diagrams here are illustrative. No retrieval experiment, indexed corpus or independent judging exercise was executed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.d79b0a48b30f4995a9bc110dbe691e52:0 -->
## Purpose and mission

A search index can return results quickly and still fail users by missing the one relevant document, returning stale access instructions, hiding a change or supplying a section whose citation does not support the final answer. Information retrieval quality therefore spans **relevance, coverage, freshness, authorization, latency and cost**. A high similarity score alone is not evidence of a correct answer.

An index has a lifecycle: source admission → normalization/segmentation → build/version → update or rebuild → ranking → permission-aware result delivery → evaluation → retention/removal. An architecture must make failures and stale snapshots visible throughout that sequence.

The [BEIR project](https://github.com/beir-cellar/beir) publishes a framework for evaluating lexical, dense and reranking approaches across diverse datasets, including ranking metrics. [NIST TREC relevance judgments](https://trec.nist.gov/data/reljudge_eng.html) describe a query/document relevance-judgment setup and pooling limitations. Neither gives a free ground truth for a private or synthetic corpus.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.d79b0a48b30f4995a9bc110dbe691e52:9 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Discord — Search index cells](../../../cases/discord-search-index-cells.md)**. **Relevant mechanism or architectural contrast:** Index cells, queue changes and shard-key evolution address different search availability and growth constraints. **Not established by this report/playbook:** Search-cell results do not establish universal optimal shard sizes or retrieval quality for unrelated indexes.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Version corpus, indexing configuration, queries and judgments together so quality changes can be explained and reproduced.

A green latency result can conceal stale documents or degraded recall; evaluate missing and unanswerable cases as well as successes.

The detailed pages separate the mechanisms that make this decision conditional:

- [Judgments, metrics and matched retrieval baselines](retrieval-judgments.md) — Which relevance labels and query populations make variants comparable?
- [Index identity, access and provenance](snapshot-access.md) — Which identity and permission contract prevents stale or unauthorized results?
- [End-to-end evaluation and index recovery](task-recovery.md) — What distinguishes ranking quality from a correct information task?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
