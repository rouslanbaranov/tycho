# ADR-LEX-001 — Provisional embedded lexical engine for Tycho

> **Status: proposed for the next bounded search prototype, not production-accepted.** Date: 2026-10-19. Issue [#48](https://github.com/rouslanbaranov/tycho/issues/48), E07-02 / M4. No claim of independent approval, measured production savings, latency SLO or a completed hybrid/vector search system.

## Decision and explicit boundary

**Use SQLite FTS5 with built-in BM25 as the default *candidate* embedded lexical baseline for the first local, read-only, snapshot-pinned Tycho search prototype**, and retain a parameterized SQL scan as a diagnostic comparator. Do not deploy a separate Elasticsearch cluster or incorporate Lucene as a mandatory JVM service solely for the current small *synthetic* retrieval pilot. This is a **provisional engineering choice**, not a universal winner or an instruction to skip later size/relevance benchmarks.

Reasons: SQLite is already available with Python's standard library when FTS5 support is compiled in; an on-disk virtual index can be rebuilt atomically from canonical published chapters; it requires no distinct search daemon or distributed cluster to operate. Its SQL and tokenizer facilities are documented by the SQLite maintainers. The proposed single-writer/index-build, read-only-snapshot, immutable-version approach fits the current *plan*, but no real Tycho-index artifact has been built. It must fail closed when FTS5 is missing rather than silently changing search semantics.

## Comparable candidates and operating costs

| Alternative | Strength and implementation boundary | Operational burden and exit condition | Actual execution in this issue |
|---|---|---|---|
| SQLite FTS5 + BM25, `unicode61`, title weight 5, body weight 1 | In-process inverted index, documented BM25 ranking, possible section-level metadata filters | One persistent SQLite file per immutable snapshot, index generation/validation, backup/atomic publish and version tracking; poor alias recall without dictionary and ranking work | **Synthetic harness source provided; reconstructed local FTS5 run recorded separately** |
| Parameterized SQL scan over original paragraphs (`instr`) | Minimal separate index, understandable exact substring semantics | Scans content and performs expression evaluation per query; cannot be assumed scalable without measured corpus load | **Compared in the same reconstructed synthetic harness** |
| Embedded Apache Lucene | Mature index/search library with BM25Similarity, richer analyzer ecosystem | Adds JVM/sidecar/FFI or language-runtime integration complexity not justified by a benchmark so far | **Not installed or run** |
| Elasticsearch/OpenSearch-style distributed search | Remote index, concurrency controls and potentially multiple tenants/shards | Cluster/server deployment, security, upgrades, backups, shard/replica lifecycle, heap monitoring; worthwhile only when measured load and feature requirements justify it | **Not deployed or benchmarked** |
| Vector-only or hybrid retrieval | Potentially useful for terminology mismatch and semantic questions | Embeddings, vector index rebuild and source-version provenance, different relevance/latency/cost envelope | **Outside lexical #48; planned and unmeasured** |

**Source boundaries (inspected official materials, 2026-10-19):** [SQLite FTS5 documentation](https://www.sqlite.org/fts5.html) §§3, 4.3, 5.1.1 for query syntax, tokenizers, BM25 ranking and column weights; [Apache Lucene 10.3.1 Similarity API](https://lucene.apache.org/core/10_3_1/core/org/apache/lucene/search/similarities/Similarity.html) for an available BM25 implementation, not performance equivalence; [Elastic production guidance](https://www.elastic.co/docs/deploy-manage/production-guidance/elasticsearch-in-production-environments) and [important settings](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/important-settings-configuration) for cluster/shard/heap/operations obligations. These public references are technical product documentation, not controlled head-to-head measurements.

## Fixed original benchmark scope and results

Pilot sources are **12 entirely synthetic English snippets** in [fixtures/lexical-engine-pilot.json](../fixtures/lexical-engine-pilot.json); **14 explicitly labeled queries** (12 expected term matches, two terminology/alias cases). See [benchmark script](../scripts/benchmark_lexical.py), [six focused test cases](../tests/test_tycho_lexical_benchmark.py) and [separate reconstruction report](../reports/lexical-pilot-reconstruction-2026-10-19.json).

The existing report explicitly describes **locally measured reconstructed code**, not execution of the exact GitHub-committed script/fixture bytes. Do not conflate the two. This is a warm sequential single-process, fixed-small-data example, not a head-to-head Lucene/Elasticsearch comparison. Measurements in that narrowly reported environment were:

| Metric | SQLite FTS5/BM25 | Parameterized SQL scan |
|---|---:|---:|
| MRR@5 over 14 fixed questions | 0.8571 | 0.9286 |
| Mean Recall@5 | 0.8571 | 0.9286 |
| Median query latency, ms | 0.02663 | 0.03631 |
| p95 query latency, ms | 0.08137 | 0.14244 |

Reported reconstruction: SQLite 3.46.1, 100 repeats/query, combined data table + FTS index file **32,768 bytes**, reported combined build 23.73831 ms. The index's **standalone** storage cost is unknown. Even if these exact numbers reproduce, this tiny test **does not show better relevance for FTS5** (the SQL scan scored higher), capacity advantage at Tycho's real book size, concurrency behavior, disk usage per chapter, normalized hardware performance, nor any reduction in tokens consumed by agents. Neither 32,768 bytes nor the timings should be multiplied by document count as a production size forecast.

**Known negative cases:** the two deliberately paraphrased alias queries have no curated synonym expansion; tokenized lexical retrieval can miss them. Exact substring scan and full-text token matching use **different retrieval semantics** and so do not constitute a perfectly controlled ranking-only A/B test. The script needs to be rerun from exact GitHub bytes in a checkout before citing its output as integration evidence.

## Publication and validation contract

1. **Build identity:** freeze one canonical book snapshot; derive section-level IDs, title, headings, provenance and source revision. Keep original Markdown and claim ledger authoritative. Build into a new temporary SQLite file, validate index identity, document/section counts and checksums, then atomically publish a read-only snapshot. No agent query mutates documents, provenance or index. Rebuilding is not chapter enrichment.
2. **Scoring:** document the actual tokenizer/version and BM25 weights with deterministic tie ordering; preserve filters for canonical IDs/sections and source coverage. Implement a curated alias dictionary as an independently reviewed, versioned artifact, not unexplained hidden query expansion.
3. **Search budget:** first return short metadata snippets/citations, then bounded exact section reads with snapshot and offset checks, followed by evidence verification. Token savings are a **hypothesis**, to be measured using defined agent tasks, relevance, missed evidence and input/output tokens; no percentage asserted.
4. **Evaluation:** rerun the committed synthetic baseline; then expand to an authorized representative *public* Tycho chapter corpus with independent qrels, exact-term/alias/contradiction/revision-staleness scenarios. Measure cold and warm p50/p95/p99, memory, FTS index vs underlying text sizes, rebuild/incremental update, concurrency, ranking and recall under unchanged hardware. No universal SLA/throughput threshold is proposed.
5. **Fallback and reconsideration:** if section-level relevance/alias recall, Unicode/query features, index size, concurrency or operational resilience fail user-defined gates, re-evaluate embedded Lucene before choosing a cluster. Distributed Elasticsearch merits a separate operational decision only when the extra capabilities justify its real infrastructure cost.

**Decision status: proposed / conditional.** The next step is build and validate the actual snapshot-based index; do not mark a deployed retrieval service, complete M4, or independent domain review from this ADR alone. The source engine choice may change after proper real-corpus tests.
