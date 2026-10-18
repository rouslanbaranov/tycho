# Reading and evidence acquisition plan

## First-pass result

The public inventory establishes an initial research base. Source origin and entry-page/abstract access have been checked. No complete technical book or documentation tree has been read. No implementation has been executed. Paid books are bibliography-only, never unseen evidence.

## Selection rationale

Prefer original standards and papers for definitions and guarantees; author references for pattern intent; official documentation for supported configuration and interfaces; exact-revision code/tests for implementation behavior; and independent experiments for performance. Use complementary perspectives to expose limitations. Core priority reflects expected reuse and the requested scope, not a universal best-in-world ranking.

## Work waves

1. **Foundations and workload:** freely available distributed-systems/OS/IR texts, consistency and consensus papers, workload characterization, queueing, tail latency and overload. Use the commercial books only if lawful content access is available.
2. **Mandatory technical tracks:** Kafka partitions, transactions and external effects; PostgreSQL MVCC/WAL/indexes/replication; reactive demand and cancellation; virtual-thread execution and connection budgets. Pin compatible reference versions before deep research.
3. **Architecture and operations:** monolith/SOA/microservices, caching, transactions and durable workflows, data/search options, CI/CD, deployments, sharding, pooling, autoscaling, multi-region recovery and metrics/tracing pipelines.
4. **Pilot synthesis and evaluation:** one mechanism, one end-to-end process and one recovery scenario; trace material claims to exact sections; preserve contradictory or missing evidence. Then propose the book structure and full question set.

## Workload-to-architecture research contract

For every substantive design comparison, capture these dimensions where relevant:

- Registered, daily/monthly active and simultaneously active users; do not treat them as interchangeable.
- Arrival rate in requests/events/transactions per second, sustained versus burst/peak, burst duration, seasonality and growth.
- In-flight concurrency, think time, open versus closed arrival models and queue boundaries.
- Operation mix and read/write ratio, request cost distributions, fan-out and dependent-service budgets.
- Payload/event sizes, network throughput, data volume and growth, working set, cardinality, key skew and hot partitions.
- Latency SLOs and p50/p95/p99 distributions, errors, freshness, durability and consistency requirements.
- CPU, memory, I/O, network, connections, queue capacity and dependency limits; warmup, cache hit rate and GC conditions.
- Availability target, failure-domain loss, recovery capacity, RPO/RTO, operational effort and cost envelope.

Research Little’s Law with explicit boundaries, consistent units, stationarity/finite-window limitations and uncertainty. Never substitute a percentile for a mean in the relationship. Active users do not determine RPS without behavior assumptions. Pool sizes and virtual-thread counts do not create downstream capacity. Model contention/coordination and measure the predicted bottleneck before recommending distribution or sharding.

There are no universal user-count or RPS thresholds that automatically select monoliths, microservices, caches, Kafka or sharding. A future chapter must state the workload, observed limiting resource, candidate change, downside, and the measurement that would support or refute it. Illustrative numbers must be labelled as assumptions, not empirical results.

## Pilot questions

- Under which workload and failure assumptions does a modular monolith remain adequate, and what evidence justifies splitting a boundary?
- How can a PostgreSQL write and an emitted event be coordinated without pretending the external consumer participates in the same transaction?
- Which duplicate effects can Kafka producer idempotence/transactions prevent, and which still require application deduplication?
- How do WebFlux/Reactor and virtual-thread request handling differ when the same bounded database pool is saturated?
- When do SQL full-text search, an external lexical index, exact vectors, ANN and hybrid retrieval satisfy different query/latency/recall requirements?
- How does metric cardinality, aggregation and temporality change the ingestion/storage/query design?
- What happens to pool capacity, shard placement, consumer lag and p99 latency during one failure-domain loss and a rolling deployment?
- Which evidence distinguishes a safe progressive rollout from a successful build pipeline?

These are proposed questions, not answered or benchmarked results.
