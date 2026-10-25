# Remaining source plan

**Date:** 2026-10-24. **Baseline:** 6754bac6e26faa57d65a301a60be10b3da93f65b.
**Machine-readable plan:** [source-plan-remaining.json](source-plan-remaining.json).

## Canonical count correction (historical snapshot)

The register contains 247 sources. Readings and reconciliations cover 134
register sources; 110 remain. The earlier 127 count was stale: it did not
include the completed OSTEP whole-book reconciliation and mixed unregistered
OpenTelemetry child-page IDs into the record count.

DDIA and Distributed Systems still count as landing. Their book records are
preview-only or blocked, not complete reads.

## Categories

- **Documentation sites:** 56.
- **Other single pages and patterns:** 35.
- **Books and book-like pages:** 18.
- **Source repositories:** 11.
- **Papers:** 0 (B18 read eight; TLA+ resources is partial).
- **Articles:** 1.

The 18 "book" entries include commercial books and public pattern pages; they
must be split before reading.

## Batch order

1. **B18 - papers (8 read; TLA+ partial).** Single PDFs: Lamport time, Raft, Paxos, Dynamo,
   Spanner, Bigtable, MapReduce, HNSW, TLA+ resources. Cheapest high-value batch.
2. **B19 - standards and specifications.** OpenAPI, AsyncAPI, CloudEvents,
   W3C Trace Context, W3C Baggage, R2DBC, SLSA, OpenGitOps, TLA+.
3. **B20 - public books.** SRE Workbook, Building Secure and Reliable Systems,
   AOSA, Introduction to Information Retrieval, Search Engines. Chapter
   manifests required; no commercial previews.
4. **B21 - databases and storage docs.** PostgreSQL, MySQL, Cassandra, MongoDB,
   CockroachDB, FoundationDB, Redis, Valkey, Memcached, Hazelcast, Infinispan,
   Caffeine. One bounded scope per product.
5. **B22 - search and retrieval docs.** Elasticsearch, OpenSearch, Solr, Vespa,
   Qdrant, Milvus, Weaviate, Faiss, PostgreSQL FTS.
6. **B23 - observability docs.** Prometheus, Jaeger, Micrometer, W3C
   trace/baggage, Mimir, Thanos, VictoriaMetrics, OpenLineage.
7. **B24 - delivery and platform docs.** Kubernetes, Envoy, Istio, GitHub
   Actions, GitLab CI, Jenkins, Tekton, Argo CD/Rollouts, Flux, Sigstore, SLSA,
   KEDA, Helm, Docker, Lambda.
8. **B25 - JVM and framework docs.** Spring WebFlux, Boot virtual threads,
   Reactor, RxJava, Mutiny, Vert.x, Resilience4j, Spring Modulith, Spring Kafka,
   Netty, Quarkus.
9. **B26 - commercial books.** DDIA, Database Internals, Fundamentals, Hard
   Parts, Building Microservices, Monolith to Microservices, Microservices
   Patterns, EAA, Release It. Blocked unless the owner supplies lawful text.
10. **B27 - source repositories.** Kafka, PostgreSQL, Reactor, OpenJDK,
    Caffeine, RxJava, JMH, HdrHistogram, wrk2, CloudEvents, FoundationDB
    simulation. Bounded README/architecture scope or blocked; never claim a
    full source read.

## Rules

- A batch starts only after its source units are enumerated with URLs and
  versions.
- One reader child gets 1-3 finite units, never a whole docs site.
- Every record carries line/word/SHA-256 and a partial/full status.
- A source leaves landing-only only when every unit in its declared scope is
  read and accepted.
- Commercial previews and search snippets are not evidence.
- Comparisons remain parent work.

## Next batch

B18: eight papers were read and accepted; TLA+ resources remains.
Each paper is a single PDF. The parent validates hash, line/word counts,
sections and spot-checks claims. Expected landing reduction was up to 9;
eight were accepted.
