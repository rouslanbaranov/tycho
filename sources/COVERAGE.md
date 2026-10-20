# Research coverage map

> **Historical manuscript transition — 2026-10-20, before edition assembly:** The owner confirmed independent substantive/content acceptance of all 69 primary chapter manuscripts at `986b1ddbe985079b7c647182fcf1c2fc8911d96c`. PR #218 merged into main at `f9834ef903fc5808f3a1edede208d82aac08f4e6`; #213 and E14 #15 are completed. #214 is open and ready for ten-volume/69-chapter edition assembly and named publication. The exact accepted-head 13/13 validation groups and 215/215 tests PASS are owner-reported in [PR #218](https://github.com/rouslanbaranov/tycho/pull/218#issuecomment-6294804915), not a new run on a later status commit. Earlier pending/0-of-69/review-open rows and pre-merge instructions below are historical and superseded for the manuscript acceptance gate. Their original observations and evidence limits are retained; no signed per-chapter reviewer records are manufactured. No finished physical edition or deployed service is claimed; visual rendering/live MCP remain owner-cancelled. See [current state](../authoring/STATE.md) and [reconciliation](../authoring/PROJECT_STATUS_RECONCILIATION_2026-10-20.md).


## Purpose and interpretation

Map engineering questions to public research entry points. Every row is a planned research area; sources are discovered, not yet exhausted or synthesized into a reviewed chapter. IDs resolve through the [register](register.json). This map is not an approved table of contents.

| Area / questions to answer | Initial source IDs | Important boundaries |
|---|---|---|
| Architecture drivers, quality attributes and trade-offs | src.fundamentals-architecture, src.architecture-hard-parts, src.arc42, src.ddia | Workload, team constraints, security, cost and change rate all affect choices. |
| Monolith, modular monolith and microservices | src.monolith-first, src.monolith-to-microservices, src.spring-modulith, src.building-microservices | Distribution is a trade-off, not a maturity ladder. |
| SOA, integration, ports/adapters and domain boundaries | src.soa-model, src.enterprise-integration, src.camel, src.hexagonal, src.ddd-reference | Service contracts and ownership versus deployment topology. |
| Distributed systems, causality and consensus | src.distributed-systems, src.lamport-time, src.raft, src.paxos, src.jepsen-consistency | Explicit failure, clock and consistency assumptions. |
| Idempotency, deduplication and retries | src.http-semantics, src.stripe-idempotency, src.aws-idempotency, src.aws-backoff, src.debezium-outbox | Protocol method semantics, key scope/expiry, concurrent duplicates and external effects. |
| Transactions, sagas, outbox/inbox, CQRS and event sourcing | src.ddia, src.microservices-patterns, src.debezium-outbox, src.temporal | Compare local atomicity, publication, consumer deduplication, replay and compensation. |
| Kafka and log-based architecture | src.kafka, src.kafka-design, src.kafka-streams, src.spring-kafka, src.kafka-code | Partitions, KRaft/version scope, ordering, producer idempotence, transactions, rebalancing and recovery. |
| Alternative brokers and stream processing | src.rabbitmq, src.pulsar, src.nats, src.flink | Acknowledgments, event time, state, retention and guarantee boundaries. |
| Reactive Java and backpressure | src.reactive-streams, src.reactor, src.webflux, src.r2dbc, src.mutiny, src.vertx, src.rxjava | Demand, cancellation, execution model, context propagation and blocking calls. |
| Virtual threads versus reactive execution | src.jep444, src.jep491, src.jdk24-release-notes, src.jdk25-virtual-threads, src.boot-virtual, src.quarkus | Pinning depends on JDK; CPU, DB connections and downstream capacity stay bounded. |
| PostgreSQL relational design | src.postgresql, src.postgres-concurrency, src.postgres-indexes, src.postgres-wal, src.postgres-logical | MVCC, anomalies, plans, WAL, replication, durability, vacuum and schema evolution. |
| Relational, distributed SQL, document, wide-column and OLAP stores | src.mysql, src.sqlite, src.cockroachdb, src.foundationdb, src.mongodb, src.cassandra, src.clickhouse | Data/transaction boundaries, workload fit, operational cost and model limitations. |
| Sharding and partitioning | src.citus, src.vitess, src.mongo-sharding, src.cassandra, src.ddia | Key skew, hot partitions, joins, uniqueness, resharding, rebalancing and failure isolation. |
| Pooling and admission control | src.pgbouncer, src.hikaricp, src.hikari-pool-sizing, src.netty, src.resilience4j | Connection/thread/buffer pools differ; queues, timeouts and total cross-instance budgets matter. |
| Distributed and local caching | src.redis, src.valkey, src.hazelcast, src.infinispan, src.caffeine, src.memcached | Ownership, TTL, invalidation, stampede, consistency, hot keys, failover and recovery. |
| Lexical/full-text search | src.ir-introduction, src.sicar, src.lucene, src.postgres-fts, src.solr, src.elasticsearch | Tokenization, inverted indexes, ranking, refresh, partitioning and relevance evaluation. |
| Vector, ANN and hybrid search | src.hnsw, src.pgvector, src.faiss, src.qdrant, src.milvus, src.weaviate, src.opensearch, src.vespa | Exact versus ANN, pre/post-filtering, recall, fusion/reranking, updates and isolation. |
| Graph data and traversal | src.neo4j, src.ddia | Graph traversal, document links and vector similarity are distinct retrieval models. |
| API descriptions, RPC and events | src.openapi, src.asyncapi, src.cloudevents, src.grpc | Schema compatibility, deadlines, streaming and version evolution. |
| High load and architecture under load | src.tail-at-scale, src.little-law, src.usl, src.brendan-method, src.performance-modeling, src.ddia | User counts alone are insufficient; workload and measured bottlenecks drive decisions. |
| Queueing, saturation and overload | src.sre-overload, src.sre-cascading, src.aws-backoff, src.reactive-streams | Bounded queues, load shedding, rate limits, retry budgets and backpressure. |
| Load generation and benchmark validity | src.k6, src.gatling, src.wrk2, src.hdrhistogram, src.jmh, src.tpc | Open/closed models, coordinated omission, warmup, percentiles and representativeness. |
| Deployment topology and infrastructure | src.kubernetes, src.docker, src.helm, src.opentofu, src.lambda, src.envoy, src.istio | VM/bare-metal/container/serverless are research axes; do not assume Kubernetes is universal. |
| CI/CD and supply-chain provenance | src.continuous-delivery-book, src.dora, src.github-actions, src.gitlab-ci, src.jenkins, src.tekton, src.slsa, src.sigstore | Build/test/release/deploy separation, reproducibility, artifacts, permissions and provenance. |
| GitOps and progressive deployment | src.opengitops, src.argocd, src.flux, src.argo-rollouts, src.k8s-deployments | Recreate/rolling/blue-green/canary, analysis gates, rollback and reconciliation. |
| Safe database evolution during deployment | src.flyway, src.liquibase, src.postgresql | Expand/contract, compatibility windows, online migration and rollback limits. |
| Scaling, placement and capacity | src.k8s-hpa, src.keda, src.usl, src.aws-static-stability, src.sre | Horizontal/vertical scaling, stateless/stateful constraints, autoscaling delay and headroom. |
| Multi-zone, multi-region and recovery | src.aws-dr, src.aws-static-stability, src.spanner, src.sre-workbook | Active/passive versus active/active, RPO/RTO, split brain and restoration tests. |
| Metrics architecture | src.otel-metrics-model, src.otel-collector, src.prometheus, src.prometheus-storage, src.mimir, src.thanos, src.victoriametrics, src.prom-alerting | Pull/push, temporality, histograms, cardinality, TSDB, remote write, retention, downsampling and alerting. |
| Distributed traces and context | src.otel, src.trace-context, src.baggage, src.jaeger, src.micrometer | Sampling, asynchronous boundaries, correlation, privacy, loss and cost. |
| Traceability, audit and lineage | src.openlineage, src.slsa, src.secure-reliable, src.trace-context | Data lineage, build provenance, audit trails and requirements traceability are distinct; dedicated audit/requirements sources remain a gap. |
| Security and verification | src.owasp-asvs, src.oauth-security, src.secure-reliable, src.testcontainers, src.tla | Threat models, identity, isolation, applicable tests and explicit proof boundaries. |

## Mandatory anchors

Kafka, reactive Java, virtual threads and PostgreSQL are first-class research tracks. CI/CD, deployment, sharding, pooling, scaling, high-load design, workload modelling and metrics architecture are required coverage, not optional appendices.
