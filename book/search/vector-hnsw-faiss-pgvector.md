---
metadata_version: 1
id: "tycho.page.7a67fd6346a54eff97784465c22bbc74"
kind: "page"
parent_id: "tycho.landing.4348c76938fc4d41b239721b94338436"
canonical_path: "book/search/vector-hnsw-faiss-pgvector.md"
title: "Vector retrieval: exact distance, HNSW, IVF, filtering and pgvector/Faiss"
topic_ids:
  - "search-architecture"
perspectives:
  - "architecture"
summary: "Reader entry for Vector retrieval: exact distance, HNSW, IVF, filtering and pgvector/Faiss. Scope includes 1. The retrieval contract begins before embeddings; 3. ANN index types and their trade-offs; 4. Metadata filtering creates a subtle recall and security boundary."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Vector retrieval: exact distance, HNSW, IVF, filtering and pgvector/Faiss?"
  prerequisites: []
  related_ids: []
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Vector"
    - "retrieval"
    - "exact"
    - "distance"
    - "HNSW"
    - "IVF"
    - "filtering"
    - "and"
    - "pgvector/Faiss"
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

# Vector retrieval: exact distance, HNSW, IVF, filtering and pgvector/Faiss

> Tycho [Issue #85](https://github.com/rouslanbaranov/tycho/issues/85), independent official/public-source review on **2026-10-19**. Examples and diagrams are original. Versioned pgvector and Faiss claims are scoped to the *public documentation inspected*, not a claimed running database, embedding API or benchmark.

## Purpose and mission

A semantic embedding maps text, code or another input to a numerical vector. A distance operation can identify **nearby representations** but says nothing by itself about technical truth, source freshness, ACLs or correctness of a proposed architecture. Approximate nearest-neighbor (ANN) indexing exchanges some accuracy or operational cost for latency/throughput trade-offs.

**Primary question:** How should a system select exact/vector index strategies, measure ANN recall and candidate filtering effects, and preserve precise source evidence when using embeddings in a knowledge book?

## 1. The retrieval contract begins before embeddings

A valid vector search workflow requires:

1. A **canonical document/page** identifier and source revision.
2. An explicit chunk/paragraph boundary with relative navigation to its parent page.
3. A documented embedding model/version, dimension, preprocessing and tokenizer.
4. One distance metric (L2, cosine similarity or inner product) with correct normalization and query conventions.
5. Tenant/privacy/access filters enforced before a result can be returned.
6. Exact or approximate search with candidate IDs, distances and freshness information.
7. Retrieval of the **canonical page and precise source anchor** before a final factual answer.

```mermaid
flowchart LR
    Docs["Canonical public Markdown + source revisions"] --> Chunk["Bounded semantic chunks"]
    Chunk --> Encode["Versioned embedding model"]
    Encode --> Vector[("Vector / ANN index")]
    Query["Query + access/filters"] --> QEncode["Same compatible encoder"]
    QEncode --> Vector
    Vector --> Candidates["Candidate IDs and distances"]
    Candidates --> Verify["ACL, revision and exact public provenance"]
    Verify --> Excerpts["Bounded grounded source excerpts"]
```

Text alternative: canonical pages are chunked and embedded with a documented model. Queries are embedded compatibly; approximate candidates are checked against identity, access and revisions, then resolved to authoritative source text. The model does not replace source verification.

A vector distance measures representation proximity, **not business applicability**. A request to choose an architecture for 100,000 users requires constraints and evidence rather than a nearest paragraph.

## 2. Exact nearest neighbors are the reference baseline

An exact search can compare a query vector against every eligible candidate and rank by distance. This is a useful **ground truth for approximate search recall**, within the same model, metric, filtering and corpus version. It does not establish that the embedding ranking matches human relevance labels.

The public **pgvector** project README states that nearest-neighbor search is exact by default and supports approximate HNSW and IVFFlat indexes. The README documents distance/operator classes for L2, inner product and cosine distance. [E01]

A *fictional* mathematical sketch: three 2-D vectors `A=(1,0)`, `B=(0,1)`, `C=(0.8,0.2)` with query `q=(1,0)`. Under ordinary Euclidean distance, `A` ranks first at distance 0, `C` has distance `sqrt(0.08)≈0.283`, `B` has distance `sqrt(2)≈1.414`. This arithmetic says nothing about semantic quality or trained embedding behavior.

## 3. ANN index types and their trade-offs

| Index | Conceptual mechanism | Benefits and costs to evaluate |
|---|---|---|
| **Flat/exact** | Compare against every eligible vector | Deterministic exact top-k by chosen metric; potentially higher scan cost |
| **HNSW** | Multi-layer navigable proximity graph; approximate traversal | Recall/latency trade-off, graph memory/build/update costs |
| **IVF/IVFFlat** | Assign vectors to coarse lists and search selected lists | Adjustable probes/recall; training/centroid and load-skew considerations |
| **PQ/quantization** | Store compressed codes, sometimes with exact re-ranking | Smaller memory and faster candidate selection at added approximation/encoding complexity |
| **Hybrid index/cluster** | Couple ANN with metadata filters, replication and source lookup | More components, freshness/ACL coordination, operational failover |

Faiss's official open [Faiss Indexes wiki](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes), including the table of flat, HNSW, IVF and PQ methods, documents these index families and approximate/exhaustive distinctions. That is an index toolkit, not automatically a persistent, multi-tenant distributed vector database. [E02]

```mermaid
flowchart TD
    Input["Versioned query vector"] --> Exact{"Use exact search within required latency?"}
    Exact -->|Yes| Scan["Exact eligible vector distance ranking"]
    Exact -->|No| ANN["ANN candidate generation"]
    ANN --> Graph["HNSW graph traversal"]
    ANN --> Lists["IVF probing"]
    Graph --> Filter["Validate filtered candidate count and access"]
    Lists --> Filter
    Filter --> Rerank["Re-rank with exact distance / relevance model"]
    Rerank --> Source["Resolve canonical evidence and freshness"]
```

Text alternative: prefer exact search when it meets constraints. Otherwise use a graph or coarse-list ANN to generate candidates, apply correct filtering and optionally precise reranking, then return source-backed pages. This is an **original selection sketch**, not a software algorithm recommendation.

Neither HNSW nor IVF is an invariant that guarantees a particular recall percentage across all data distributions. Duplicate/near-duplicate vectors, dimension, cluster shape, vector quantization and deletion/update behavior can change efficiency and accuracy.

## 4. Metadata filtering creates a subtle recall and security boundary

The pgvector project README states that when using approximate indexes, filtering can happen **after** scanning candidates. If only a small fraction of nearest neighbors meet a restrictive filter (e.g. topic, version, tenant), the first approximate scan may return fewer than the requested `LIMIT` and lower observed recall. The README documents *iterative index scans*, partitioning and partial indexes as mitigations, with version-specific options. [E01]

```mermaid
sequenceDiagram
    participant Query
    participant ANN as ANN candidate generator
    participant Filter as Mandatory filter
    participant Canonical as Source revision/ACL checker
    Query->>ANN: Find top neighbors for query
    ANN-->>Filter: Approximate candidate IDs
    Filter-->>Canonical: Eligible IDs only
    Canonical-->>Query: Verified evidence pages
    Note over Filter,ANN: Restrictive filter can yield fewer than requested top-k
```

Text alternative: ANN produces candidates, which are filtered for required topic/version/ACL constraints and checked against authoritative source revisions. A selective filter may leave too few candidates; search design may need filtered indexes, broader scans or exact fallback.

**Security matters:** do not allow an approximate index to reveal restricted titles/excerpts through pre-filter snippets, side-channel counts or postfilter leakage. The intended Tycho corpus is independently public, but general methods should still model permission filtering and redaction explicitly.

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

A query-time tenant predicate and a policy-enforced access filter are different responsibilities. A shared vector index may choose candidate neighbors based on other tenants even if the final results are filtered; ranking leakage, query timing and insufficient eligible recall require separate threat and quality analysis. The [safe agent-access owner](../security/safe-agent-access-and-knowledge-isolation.md) owns policy enforcement.

**Proposed, not executed:** build a permission-labeled evaluation set with frozen snapshot/model versions and representative tenant skews, then measure *eligible* Recall@10, unauthorized-result count, latency, memory and index rebuild time for exact, ANN, partitioned ANN and lexical/hybrid alternatives. Reject a technique that violates isolation regardless of its unfiltered ranking score. No embedding, index or ACL evaluation has been run for this chapter.

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

## Source-to-claim evidence

| ID | Primary public source / exact inspected scope | Supports, not empirical Tycho outcomes |
|---|---|---|
| E01 | [pgvector project README](https://github.com/pgvector/pgvector), *Indexing, HNSW, IVFFlat, Filtering, Iterative Index Scans, Hybrid Search*, rolling main revision observed 2026-10-19 | Exact default and ANN choices, candidate postfilter and tuning features; pin tag before deployed version-specific instructions |
| E02 | [Faiss Indexes](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes), table of method classes, HNSW, IVF and PQ; wiki inspected 2026-10-19 | Index family properties, not an installed managed search service |
| E03 | [Faiss Index factory](https://github.com/facebookresearch/faiss/wiki/The-index-factory), IVF/PQ/HNSW construction overview | Index composition, not measured universal index ranking |

No embeddings were generated, model API invoked, index built, recall computed or human relevance annotated for this page; all numeric examples are synthetic.
