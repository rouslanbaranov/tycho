# Architecture concepts and implementation families

This is a research map, not a recommended production stack or a feature-parity claim. Links and IDs refer to the public [catalogue](CATALOG.md). Exact releases, deployment modes, code licenses and operational constraints must be assessed during research.

| Design mechanism | Implementations / source IDs | Comparison required |
|---|---|---|
| Modular monolith | Spring Modulith — src.spring-modulith | Module verification, events, transaction boundaries and independent deployment needs. |
| SOA and message integration | Apache Camel — src.camel; gRPC — src.grpc | Routing/integration versus transport contracts; avoid confusing broker and orchestrator. |
| Reactive execution | Reactor/WebFlux, RxJava, Mutiny, Vert.x, Netty — src.reactor, src.webflux, src.rxjava, src.mutiny, src.vertx, src.netty | Backpressure, cancellation, blocking boundaries and context propagation. |
| Virtual-thread execution | OpenJDK, Spring Boot, Quarkus — src.jdk-code, src.jdk25-virtual-threads, src.boot-virtual, src.quarkus | Workload fit, version differences and bounded downstream resources. |
| Resilience and admission | Resilience4j, Envoy — src.resilience4j, src.envoy | Circuit breaking, concurrency bulkheads, rate limits, retries and timeout budgets. |
| Durable log and processing | Kafka, Kafka Streams, Flink — src.kafka, src.kafka-streams, src.flink | Ordering, state, recovery, event time and transactions across boundaries. |
| Messaging | RabbitMQ, Pulsar, NATS — src.rabbitmq, src.pulsar, src.nats | Delivery, persistence, consumer state and backpressure. |
| Outbox / CDC | Debezium — src.debezium-outbox | Atomic local writes, CDC lag, duplicate publication and consumer responsibility. |
| Durable workflow | Temporal — src.temporal | Replay, workflow history, retries, compensation and side effects. |
| Relational / distributed transactions | PostgreSQL, MySQL, CockroachDB, FoundationDB — src.postgresql, src.mysql, src.cockroachdb, src.foundationdb | Transaction, consistency, partition and failure contracts. |
| Sharded relational storage | Citus, Vitess — src.citus, src.vitess | Shard key, routing, joins, rebalance and global constraints. |
| Connection pooling | HikariCP, PgBouncer — src.hikaricp, src.pgbouncer | Client versus server pooling, transaction/session compatibility and total capacity. |
| Cache / data grid | Redis, Valkey, Hazelcast, Infinispan, Memcached — src.redis, src.valkey, src.hazelcast, src.infinispan, src.memcached | Replication, expiry, persistence, cache authority and failure recovery. |
| Local cache | Caffeine — src.caffeine | Admission/eviction, local coherence, refresh and memory budget. |
| Lexical and hybrid retrieval | Lucene, Solr, Elasticsearch, OpenSearch, Vespa — src.lucene, src.solr, src.elasticsearch, src.opensearch, src.vespa | Index topology, relevance, refresh, reranking and resource cost. |
| Vector retrieval | pgvector, Faiss, Qdrant, Milvus, Weaviate — src.pgvector, src.faiss, src.qdrant, src.milvus, src.weaviate | Library versus database boundary, filtering, recall and replication. |
| Metric pipelines and storage | OpenTelemetry Collector, Prometheus, Mimir, Thanos, VictoriaMetrics — src.otel-collector, src.prometheus-storage, src.mimir, src.thanos, src.victoriametrics | State, cardinality, temporality, durable ingestion and query cost. |
| Tracing and instrumentation | OpenTelemetry, Jaeger, Micrometer — src.otel, src.jaeger, src.micrometer | Collection, sampling, propagation and backend boundaries. |
| CI pipeline execution | GitHub Actions, GitLab CI, Jenkins, Tekton — src.github-actions, src.gitlab-ci, src.jenkins, src.tekton | Execution isolation, dependency graphs, artifacts and credentials. |
| GitOps and rollout | Argo CD, Flux, Argo Rollouts — src.argocd, src.flux, src.argo-rollouts | Desired-state reconciliation versus progressive traffic delivery. |
| Database migration | Flyway, Liquibase — src.flyway, src.liquibase | Versioned change application versus backward-compatible online evolution. |
| Infrastructure and autoscaling | OpenTofu, Helm, Kubernetes, KEDA — src.opentofu, src.helm, src.kubernetes, src.keda | Infrastructure planning, packaging, scheduling and event scaling are different layers. |
| Load and component tests | k6, Gatling, wrk2, JMH, Testcontainers — src.k6, src.gatling, src.wrk2, src.jmh, src.testcontainers | End-to-end capacity, microbenchmarks and integration correctness are distinct. |

Source repositories for Kafka, PostgreSQL, Reactor and OpenJDK are explicitly registered. Other maintainer repositories will be added only when a bounded implementation question requires them; documentation discovery is not code inspection. No source repository has been cloned, built or tested in this pass.
