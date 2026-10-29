# Top-1 adjudication packet — 2026-10-29

Status: **review pending**. No adjudication has been performed.

For each item, mark whether the BM25 top-1 is a defensible answer
even if it is absent from the original accepted set.

- valid: top-1 is a correct and useful answer;
- invalid: top-1 is wrong;
- uncertain: needs source reading.

## v2 Q001

Query:

Registered users are numerous, but the service sees only a modest request rate. What
must a capacity estimate include besides user count?

- Top-1: book/volumes/v09-observability-security-and-operations/c01-slis-slos-and-error-
budgets/service-level-indicators-objectives-and-alerts.md#engineering-walkthrough-
what-does-a-green-slo-say-about-rejected-business-operations
- Heading: Engineering walkthrough — What does a green SLO say about rejected business
operations?
- BM25 score: 14.546599
- Accepted rank: 3
- Accepted pages:
  - book/volumes/v01-requirements-and-architecture/c02-workload-and-demand-
models/arrivals-population.md#
  - book/volumes/v01-requirements-and-architecture/c02-workload-and-demand-
models/demand-skew.md#
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## v2 Q002

Query:

A team says the system must be both fast and durable. How should that preference
become a testable quality requirement?

- Top-1: book/volumes/v10-decision-support-and-modernization/c01-architecture-requirement-
and-workload-profiles/requirements-and-workload-architecture-profiles.md#purpose-
and-mission
- Heading: Purpose and mission
- BM25 score: 14.64903
- Accepted rank: 3
- Accepted pages:
  - book/volumes/v01-requirements-and-architecture/c03-quality-attributes-and-trade-
offs/quality-scenarios.md#
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## v2 Q003

Query:

A client times out after sending a write and retries. The server cannot tell whether
the first attempt committed. How can it avoid applying the effect twice?

- Top-1: book/volumes/v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-
compatibility/http-rpc-contracts-and-compatibility.md#engineering-walkthrough-mixed-
clients-and-an-unacknowledged-committed-post
- Heading: Engineering walkthrough — Mixed clients and an unacknowledged committed POST
- BM25 score: 15.521506
- Accepted rank: 3
- Accepted pages:
  - book/distributed/transactional-outbox-and-idempotency.md#
  - book/volumes/v04-distributed-coordination-and-events/c04-retries-idempotency-and-
duplicate-effects/retries-idempotency-and-ambiguous-effects.md#
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## v2 Q005

Query:

Adding worker threads made tail latency worse instead of raising throughput. What
saturation effect should be investigated first?

- Top-1: book/volumes/v03-execution-concurrency-and-flow-control/c06-memory-gc-cpu-and-
blocking-diagnostics/cpu-memory-gc-and-blocking-diagnostics.md#purpose-and-mission
- Heading: Purpose and mission
- BM25 score: 14.223716
- Accepted rank: not in top-5
- Accepted pages:
  - book/volumes/v03-execution-concurrency-and-flow-control/c05-thread-connection-and-
buffer-pools/fleet-budgets.md#
  - book/volumes/v07-performance-scale-and-resilience/c04-tail-latency-fan-out-and-time-
budgets/tail-latency-fanout-and-deadline-budgets.md#
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## v2 Q010

Query:

An index speeds up one query but slows another. What evidence should be collected
before keeping or removing it?

- Top-1: book/data/postgresql-mvcc-indexes-and-query-plans.md#purpose-and-mission
- Heading: Purpose and mission
- BM25 score: 12.924353
- Accepted rank: not in top-5
- Accepted pages:
  - book/volumes/v05-data-models-engines-and-lifecycle/c03-query-planning-indexes-and-
access-paths/postgresql-indexes-statistics-and-query-plans.md#
  - book/volumes/v05-data-models-engines-and-lifecycle/c03-query-planning-indexes-and-
access-paths/query-counterexamples.md#
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## v2 Q011

Query:

A hot tenant must move to a new shard while writes continue. What can go wrong, and
what must the migration prove before cutover?

- Top-1: book/volumes/v08-delivery-deployment-and-recovery/c06-high-availability-and-failure-
domain-placement/cells-shuffle-sharding.md#worked-failure-poison-request-and-
migration
- Heading: Worked failure: poison request and migration
- BM25 score: 15.117446
- Accepted rank: 5
- Accepted pages:
  - book/volumes/v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-
rebalancing/resharding-transition.md#
  - book/volumes/v05-data-models-engines-and-lifecycle/c05-partitioning-sharding-and-
rebalancing/shard-keys-hotspots-and-resharding.md#
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## v2 Q012

Query:

A popular cache entry expires and many clients miss at once. What mechanism prevents
every request from rebuilding the same value?

- Top-1: book/scaling/local-distributed-caching-and-invalidation.md#4-stampede-hot-keys-and-
failure-admission
- Heading: 4. Stampede, hot keys and failure admission
- BM25 score: 13.316624
- Accepted rank: 2
- Accepted pages:
  - book/volumes/v06-caching-indexing-and-retrieval/c01-local-and-distributed-
caching/cache-acceptance.md#
  - book/volumes/v06-caching-indexing-and-retrieval/c02-hot-keys-cache-stampedes-and-
read-amplification/cache-invalidation-stampede-and-hot-keys.md#
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## v2 Q014

Query:

Why can an approximate nearest-neighbor index return a different top-k after a
rebuild, and what should be measured before trusting it?

- Top-1: book/volumes/v06-caching-indexing-and-retrieval/c04-vector-embeddings-and-nearest-
neighbor-retrieval/README.md#purpose-and-mission
- Heading: Purpose and mission
- BM25 score: 23.23515
- Accepted rank: 2
- Accepted pages:
  - book/volumes/v06-caching-indexing-and-retrieval/c04-vector-embeddings-and-nearest-
neighbor-retrieval/exact-ann.md#
  - book/volumes/v06-caching-indexing-and-retrieval/c07-retrieval-evaluation-and-index-
lifecycle/retrieval-evaluation-and-index-lifecycle.md#
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## v2 Q015

Query:

Throughput is stable but backlog grows. What does Little’s Law imply about residence
time, and which boundary must be measured?

- Top-1: book/volumes/v07-performance-scale-and-resilience/c01-queueing-littles-law-and-
measurement-boundaries/README.md#pages-and-reasoning-route
- Heading: Pages and reasoning route
- BM25 score: 25.565707
- Accepted rank: 2
- Accepted pages:
  - book/volumes/v07-performance-scale-and-resilience/c01-queueing-littles-law-and-
measurement-boundaries/measurement-boundary.md#
  - book/volumes/v07-performance-scale-and-resilience/c01-queueing-littles-law-and-
measurement-boundaries/queueing-littles-law.md#
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## v2 Q016

Query:

Why can automatic retries during overload delay recovery instead of helping it?

- Top-1: book/volumes/v12-modeling-simulation-and-decision-validation/c02-contracts/model-
specification.md#why-a-contract-instead-of-a-diagram
- Heading: Why a contract instead of a diagram
- BM25 score: 12.155993
- Accepted rank: 5
- Accepted pages:
  - book/volumes/v07-performance-scale-and-resilience/c01-queueing-littles-law-and-
measurement-boundaries/queue-recovery.md#
  - book/volumes/v07-performance-scale-and-resilience/c05-overload-protection-and-
graceful-degradation/dependency-isolation.md#
  - book/volumes/v07-performance-scale-and-resilience/c05-overload-protection-and-
graceful-degradation/overload-admission-control-and-graceful-degradation.md#
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## v2 Q017

Query:

A column changes meaning while old and new application versions run. What must the
migration prove before the old version is removed?

- Top-1: book/volumes/v08-delivery-deployment-and-recovery/c05-backward-compatible-database-
change/reader-writer-matrix.md#1-check-the-real-combinations-including-old-readers
- Heading: 1. Check the real combinations, including old readers
- BM25 score: 13.280404
- Accepted rank: 4
- Accepted pages:
  - book/volumes/v05-data-models-engines-and-lifecycle/c06-schema-evolution-data-
migration-and-retention/semantic-compatibility.md#
  - book/volumes/v08-delivery-deployment-and-recovery/c05-backward-compatible-database-
change/mixed-version-database-compatibility-and-online-ddl.md#
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## v2 Q018

Query:

After a regional failover, two sites have accepted writes. How should the team
reconcile them without silently choosing a winner?

- Top-1: book/cases/netflix-chaos-kong-regional-failover.md#write-authority-and-the-recovery-
contradiction
- Heading: Write authority and the recovery contradiction
- BM25 score: 13.637228
- Accepted rank: 5
- Accepted pages:
  - book/volumes/v04-distributed-coordination-and-events/c02-replication-consensus-and-
leader-changes/quorum-envelope.md#
  - book/volumes/v08-delivery-deployment-and-recovery/c07-multi-region-recovery-and-
data-reconciliation/authority-failback.md#
  - book/volumes/v08-delivery-deployment-and-recovery/c07-multi-region-recovery-and-
data-reconciliation/disaster-recovery-and-recovery-objectives.md#
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## p3 T1-A01

Query:

In the cache-aside pattern, what does an application do on a cache hit and on a
cache miss, and how does this differ from read-through caching?

- Top-1: book/volumes/v06-caching-indexing-and-retrieval/c01-local-and-distributed-
caching/refresh-semantics.md#3-local-cache-eviction-and-refresh-are-different-
actions
- Heading: 3. Local cache eviction and refresh are different actions
- BM25 score: 21.477476
- Accepted rank: 5
- Accepted pages:
  - book/volumes/v06-caching-indexing-and-retrieval/c01-local-and-distributed-
caching/local-and-distributed-cache-design.md#bounded-pattern-ownership-notes
  - book/volumes/v06-caching-indexing-and-retrieval/c01-local-and-distributed-
caching/refresh-semantics.md#4-cache-aside-is-a-sequence-not-a-consistency-theorem
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## p3 T1-A04

Query:

Why can a popular cached item produce a cache stampede when its TTL expires, even if
request volume has not increased?

- Top-1: book/volumes/v11-pattern-atlas/c05-caching-retrieval/ttl-based-
expiration.md#overview
- Heading: TTL-Based Expiration
- BM25 score: 25.184731
- Accepted rank: not in top-5
- Accepted pages:
  - book/volumes/v06-caching-indexing-and-retrieval/c02-hot-keys-cache-stampedes-and-
read-amplification/stampede-protection.md#2-stampede-at-a-synchronized-expiry
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## p3 T1-A05

Query:

How does request coalescing or a per-key cache lock prevent a stampede, and what can
requests that do not acquire the lock do?

- Top-1: book/scaling/local-distributed-caching-and-invalidation.md#4-stampede-hot-keys-and-
failure-admission
- Heading: 4. Stampede, hot keys and failure admission
- BM25 score: 21.827287
- Accepted rank: not in top-5
- Accepted pages:
  - book/volumes/v06-caching-indexing-and-retrieval/c02-hot-keys-cache-stampedes-and-
read-amplification/stampede-protection.md#2-stampede-at-a-synchronized-expiry
  - book/volumes/v06-caching-indexing-and-retrieval/c02-hot-keys-cache-stampedes-and-
read-amplification/stampede-protection.md#5-cache-loss-and-source-protection-policy
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## p3 T2-A05

Query:

A team inserts a queue between a bursty producer and a consumer that processes at a
fixed rate. What does the producer now wait for, and what happens if the producer's
long-run average rate stays above the consumer's? Name two responses the Azure
guidance recommends.

- Top-1: book/volumes/v12-modeling-simulation-and-decision-validation/c03-deterministic-and-
des/queue-and-resource-models.md#overview
- Heading: Queue and resource models
- BM25 score: 15.622571
- Accepted rank: not in top-5
- Accepted pages:
  - book/volumes/v04-distributed-coordination-and-events/c06-messaging-families-and-
delivery-contracts/message-selection.md#1-first-identify-what-a-consumer-must-own
  - book/volumes/v07-performance-scale-and-resilience/c01-queueing-littles-law-and-
measurement-boundaries/queue-recovery.md#partial-failure-saturation-and-recovery
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## v12 Q601

Query:

Which three model families does V12 use, and what does each represent?

- Top-1: book/volumes/v12-modeling-simulation-and-decision-validation/README.md#what-this-
volume-does-and-does-not-do
- Heading: What this volume does and does not do
- BM25 score: 11.705995
- Accepted rank: not in top-5
- Accepted pages:
  - book/volumes/v12-modeling-simulation-and-decision-validation/c01-foundations/stock-
and-flow-vs-stock-to-flow.md#
  - book/volumes/v12-modeling-simulation-and-decision-validation/c03-deterministic-and-
des/reference-engine-architecture.md#
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## v12 Q602

Query:

What must a V12 model specification declare before a run?

- Top-1: book/volumes/v12-modeling-simulation-and-decision-
validation/c02-contracts/README.md#pages-and-reasoning-route
- Heading: Pages and reasoning route
- BM25 score: 14.937046
- Accepted rank: 3
- Accepted pages:
  - book/volumes/v12-modeling-simulation-and-decision-validation/c02-contracts/model-
specification.md#
  - book/volumes/v12-modeling-simulation-and-decision-validation/c02-contracts/scenario-
specification.md#
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## v12 Q603

Query:

How does V12 keep source, calibration and simulation evidence separate?

- Top-1: book/volumes/v12-modeling-simulation-and-decision-validation/README.md#five-
evidence-layers
- Heading: Five evidence layers
- BM25 score: 18.771181
- Accepted rank: 5
- Accepted pages:
  - book/volumes/v12-modeling-simulation-and-decision-
validation/c01-foundations/evidence-and-validation-vocabulary.md#
  - book/volumes/v12-modeling-simulation-and-decision-validation/c07-validation-and-
limits/validation-gates.md#
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

## v12 Q606

Query:

How is a stored V12 run bound to its model, scenario and engine?

- Top-1: book/volumes/v12-modeling-simulation-and-decision-
validation/c02-contracts/README.md#purpose-and-mission
- Heading: Purpose and mission
- BM25 score: 16.48525
- Accepted rank: 3
- Accepted pages:
  - book/volumes/v12-modeling-simulation-and-decision-validation/c02-contracts/run-and-
result-provenance.md#
  - book/volumes/v12-modeling-simulation-and-decision-validation/c07-validation-and-
limits/reproducibility-and-replay.md#
- Verdict: [ ] valid  [ ] invalid  [ ] uncertain
- Notes:

