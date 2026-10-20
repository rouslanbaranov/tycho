---
metadata_version: 1
id: "tycho.page.411a855b84384e86b3b7fb60a3f63464"
kind: "page"
parent_id: "tycho.chapter.1c08d660af40408188c2d556f8d77358"
canonical_path: "book/volumes/v06/c04/vector-architecture.md"
title: "Vector engine selection and failure evaluation"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
summary: "Which lifecycle and operating constraints distinguish an index library from a serving system?"
route_hints:
  questions:
    - "Which lifecycle and operating constraints distinguish an index library from a serving system?"
  prerequisites:
    - "tycho.page.9145b7ce81d4461b90d3c6285128c18a"
  related_ids:
    - "tycho.chapter.1c08d660af40408188c2d556f8d77358"
    - "tycho.page.7a67fd6346a54eff97784465c22bbc74"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "vector"
    - "architecture"
evidence_scope:
  source_ids:
    - "src.pgvector"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.7a67fd6346a54eff97784465c22bbc74; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
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
# Vector engine selection and failure evaluation

**Owning question:** Which lifecycle and operating constraints distinguish an index library from a serving system?

This page belongs to [V06/C04 — Vector embeddings and nearest-neighbor retrieval](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.7a67fd6346a54eff97784465c22bbc74:5 -->
## 5. pgvector versus Faiss versus a vector database

- **pgvector:** extension co-locates vector data with PostgreSQL tables/transactions. Attractive when source records and metadata already live in SQL and a single DB's resources suffice. Adds ANN index build/update pressure to that DB.
- **Faiss:** vector index/search library with CPU/GPU algorithms, often embedded in a service. Durable source-of-truth, data ingestion, ACLs, service replication and consistency are *additional responsibilities*, not implied by a Faiss index.
- **Dedicated vector-search service/database:** may provide distributed ingestion/sharding/metadata features, but product/edition semantics vary. Do not name a winner without pinned documentation and equal evaluation conditions.
- **Plain arrays in Python:** for a small corpus, exact similarity with a compact local index may be sufficient, easier to rebuild and cheaper to maintain than a distributed ANN platform.

For any particular corpus, index size and latency need **measurement using actual chunk count, dimension, precision, metadata, distance and device**, not a universal extrapolation from the number of document pages. A rough raw-vector budget can be calculated as `chunks × dimensions × bytes/component`, then add index graph/codebook, metadata, documents, replicas and persistence overhead.

### Original size arithmetic

A purely illustrative corpus of **4,500 chunks × 768 dimensions × 4 bytes (FP32)** requires **13,824,000 bytes** (about 13.2 MiB) of raw components. This is **not** a memory/SSD estimate for HNSW, metadata, source text or an actual Tycho build, and it assumes a model/dimension not selected by the project.


### Worked filtered-ANN counterexample: vector recall versus authorized recall

**Original synthetic corpus:** a shared knowledge system contains 10,000 vectors, but the requesting tenant is authorized to read only 100. An HNSW candidate scan returns forty approximate neighbors; only two are tenant-eligible after applying an authorization filter. A query with `LIMIT 10` can then return two results even though ten relevant authorized documents exist elsewhere in the corpus. This is a deliberately invented case, **not** a measured recall or a claim about the default behavior of every ANN engine.

The [pgvector README, Filtering and Iterative Index Scans](https://github.com/pgvector/pgvector/blob/master/README.md) documents that with approximate indexes, predicates can be applied after candidate scanning and too few rows can survive. Its **0.8.0+** iterative-scan controls can continue scanning under configured bounds; partitioning or partial indexes can be alternatives for selected filters. These performance mechanisms must not become security gates.

| Retrieval boundary | Required invariant | Falsifying observation |
|---|---|---|
| Authorization | Every visible title, snippet, citation and body is permitted for the caller | Any unauthorized result reaches ranking output, even if the final document open is denied |
| ANN recall | Compare to **exact top-k restricted to eligible documents** | Low eligible recall hidden by high unfiltered recall |
| Snapshot correctness | Index revision, embedding model and ACL revision remain compatible | Deleted or reclassified document survives through stale cached results |
| Failure recovery | Able to use exact/lexical fallback or rebuild when ANN quality gate fails | Service declares empty evidence despite known authorized exact neighbors |

A query-time tenant predicate and a policy-enforced access filter are different responsibilities. A shared vector index may choose candidate neighbors based on other tenants even if the final results are filtered; ranking leakage, query timing and insufficient eligible recall require separate threat and quality analysis. The [safe agent-access owner](../../v09/c07/safe-agent-access-and-knowledge-isolation.md) owns policy enforcement.

**Proposed, not executed:** build a permission-labeled evaluation set with frozen snapshot/model versions and representative tenant skews, then measure *eligible* Recall@10, unauthorized-result count, latency, memory and index rebuild time for exact, ANN, partitioned ANN and lexical/hybrid alternatives. Reject a technique that violates isolation regardless of its unfiltered ranking score. No embedding, index or ACL evaluation has been run for this chapter.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7a67fd6346a54eff97784465c22bbc74:6 -->
## 6. Failure cases and evaluation

| Condition | Common failure | Minimum check |
|---|---|---|
| Embedding model upgraded | Old/new vectors incomparable or ranking shifts | Model version lock, re-embed and dual-evaluation |
| ANN index stale | Deleted or revised page still retrieved | Source revision lock and rebuilding/tombstones |
| Highly selective filters | Too few eligible results returned | Recall@k against exact *filtered* baseline |
| High-volume ingestion | Build/merge contention or query latency | Throughput, p95/p99 and state/freshness under write load |
| Quantization enabled | Relevant neighbor drops from candidate set | Blind judgments and exact-distance re-rank comparison |
| Multi-tenant filter lost | Private material surfaced | Authorization-before-result policy and adversarial tests |
| Dense-only search on code symbols | Exact exception/API tokens lost | Hybrid lexical recall and code-term tests |

**Insufficient evidence:** "HNSW is always faster and more accurate than IVF, and it will save tokens." Not established. Need the actual corpus, dimensionality, query distribution, recall targets, hardware, update rate, latency/cost and bounded agent answer-quality tests.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](vector-filters.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](vector-hnsw-faiss-pgvector.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
