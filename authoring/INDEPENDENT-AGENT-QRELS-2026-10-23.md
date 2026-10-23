# Independent agent qrels - phase 1

Agent-adjudicated set, not human review. Frozen on 2026-10-23 before any
repository material or pre-existing qrels were consulted.

## Metadata

- Dataset: independent-agent-qrels-v1
- Label status: agent-adjudicated-not-human
- Created: 2026-10-23
- Topics: 15
- Answerable items: 60 (4 per topic)
- Unanswerable items: 20

## Topics

1. Cache-aside, write-through, write-around and write-behind caching
2. Cache invalidation, TTL, stampede protection and hot keys
3. Queue-based load leveling, backpressure and Little's Law
4. Retries, idempotency keys and duplicate effects
5. Sagas, compensating transactions, outbox and inbox patterns
6. CQRS, event sourcing and read projections
7. Quorums, leader election, consensus and fencing
8. Rate limiting, admission control, load shedding and throttling
9. Sharding, partition keys, hot partitions and rebalancing
10. Multi-region failover, replication and consistency trade-offs
11. SLIs, SLOs, error budgets and alerting
12. Distributed tracing, context propagation and sampling
13. Zero trust, least privilege and tenant isolation
14. API contracts, versioning and expand-and-contract migration
15. Canary, blue-green, rollback and progressive delivery

## Answerable questions

### I001

  Topic: Cache-aside, write-through, write-around and write-behind caching
  Question: In cache-aside, what does the application do on a read miss?
  Expected answer: The application reads the cache first and, on a miss, loads the item from the
  data store and writes it into the cache with a TTL. Writes normally update the store and
  invalidate or replace the cached copy.

Key facts:
  - Application code owns cache fill and invalidation
  - A miss costs one store read plus one cache write
  - The cache is a copy, never the system of record

Sources:
  - Cache-Aside pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside
  - Caching guidance (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/best-practices/caching

### I002

  Topic: Cache-aside, write-through, write-around and write-behind caching
  Question: How do write-through and write-behind differ in latency and durability?
  Expected answer: Write-through updates the store and the cache in one operation and returns
  after both succeed, so writes are slower but the store is always current. Write-behind
  acknowledges after the cache update and flushes later, which is faster but can lose acknowledged
  writes if the cache tier fails.

Key facts:
  - Write-through returns after store and cache both succeed
  - Write-behind flushes asynchronously to the store
  - Write-behind trades durability for write latency

Sources:
  - Caching guidance (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/best-practices/caching
  - Cache-Aside pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside
  - A hitchhiker's guide to caching patterns (Hazelcast) (accessed 2026-10-23)
  https://hazelcast.com/blog/a-hitchhikers-guide-to-caching-patterns/

### I003

  Topic: Cache-aside, write-through, write-around and write-behind caching
  Question: What is write-around, and which workload does it suit?
  Expected answer: Writes bypass the cache and go straight to the backing store, so only reads
  populate the cache. It avoids polluting the cache with data that is rarely read back, but every
  read after a write pays a cache miss.

Key facts:
  - Writes go to the store; reads fill the cache
  - Good for write-heavy, rarely re-read data
  - Cost is a guaranteed miss after each write

Sources:
  - Caching strategies and how to choose them (CodeAhoy) (accessed 2026-10-23)
  https://codeahoy.com/2017/08/11/caching-strategies-and-how-to-choose-the-right-one/
  - Cache-Aside pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside

### I004

  Topic: Cache-aside, write-through, write-around and write-behind caching
  Question: What must a cache-aside application do when the cache fails?
  Expected answer: It must treat cache errors as misses and fall back to the data store instead of
  failing the request. Because the store then absorbs the extra load, timeouts, bounded retries
  and load shedding are needed to prevent a cascading failure.

Key facts:
  - Cache outage shifts load to the backing store
  - Fallback to the store keeps requests successful
  - Timeouts and load shedding protect the store

Sources:
  - Cache-Aside pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside
  - Caching challenges and strategies (AWS Builders' Library) (accessed 2026-10-23)
  https://aws.amazon.com/builders-library/caching-challenges-and-strategies/

### I005

  Topic: Cache invalidation, TTL, stampede protection and hot keys
  Question: Why is a TTL alone not a complete invalidation strategy?
  Expected answer: A TTL bounds staleness by time, not by writes, so readers can see data that
  changed before the entry expires. Systems pair TTLs with explicit invalidation or versioned keys
  on update, and pick TTLs from the staleness the reader can tolerate.

Key facts:
  - TTL cannot react to a write before expiry
  - Pair TTL with explicit invalidation
  - Shorter TTLs raise origin load and misses

Sources:
  - Caching guidance (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/best-practices/caching
  - Caching challenges and strategies (AWS Builders' Library) (accessed 2026-10-23)
  https://aws.amazon.com/builders-library/caching-challenges-and-strategies/
  - EXPIRE command (Redis documentation) (accessed 2026-10-23)
  https://redis.io/docs/latest/commands/expire/

### I006

  Topic: Cache invalidation, TTL, stampede protection and hot keys
  Question: What is a cache stampede, and how is it prevented?
  Expected answer: A stampede happens when many clients miss the same key at once, often at
  expiry, and all recompute it against the origin. Request coalescing lets one caller refresh
  while others wait or read stale data, and early or probabilistic refresh spreads expirations.

Key facts:
  - Simultaneous misses drive duplicate origin work
  - Single-flight collapses duplicate refreshes
  - Early or probabilistic refresh avoids synchronized expiry

Sources:
  - Cache stampede (Wikipedia) (accessed 2026-10-23)
  https://en.wikipedia.org/wiki/Cache_stampede
  - Caching challenges and strategies (AWS Builders' Library) (accessed 2026-10-23)
  https://aws.amazon.com/builders-library/caching-challenges-and-strategies/

### I007

  Topic: Cache invalidation, TTL, stampede protection and hot keys
  Question: How do soft and hard TTLs keep serving during an origin brownout?
  Expected answer: A soft TTL marks when an item should be refreshed in the background while it is
  still served. A hard TTL is the absolute limit; if the origin is unavailable, the service keeps
  serving stale data until the hard TTL, with backpressure to protect the origin.

Key facts:
  - Soft TTL triggers background refresh
  - Hard TTL is the absolute staleness limit
  - Serve-stale needs backpressure to help origin recovery

Sources:
  - Caching challenges and strategies (AWS Builders' Library) (accessed 2026-10-23)
  https://aws.amazon.com/builders-library/caching-challenges-and-strategies/
  - Caching guidance (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/best-practices/caching

### I008

  Topic: Cache invalidation, TTL, stampede protection and hot keys
  Question: A single key carries most traffic: what breaks, and how is load spread?
  Expected answer: The key becomes a hot spot on one cache node or shard and a stampede when it
  expires or is evicted, so the origin sees concentrated load. Spread it with key splitting or
  suffix buckets, request coalescing, and more nodes so consistent hashing redistributes keys.

Key facts:
  - A hot key skews a single node and the origin
  - Key splitting adds pseudo-random suffix buckets
  - Consistent hashing redistributes when nodes change

Sources:
  - Consistent hashing (Wikipedia) (accessed 2026-10-23)
  https://en.wikipedia.org/wiki/Consistent_hashing
  - Caching challenges and strategies (AWS Builders' Library) (accessed 2026-10-23)
  https://aws.amazon.com/builders-library/caching-challenges-and-strategies/
  - Partition key design: using write sharding (AWS) (accessed 2026-10-23)
  https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-sharding.html

### I009

  Topic: Queue-based load leveling, backpressure and Little's Law
  Question: How does a queue decouple producer rate from consumer capacity?
  Expected answer: The producer writes a message to a durable queue and continues, while consumers
  drain the queue at their own rate. The queue absorbs bursts, but if arrivals exceed service
  capacity the backlog and wait time grow without bound.

Key facts:
  - Producer and consumer run at different rates
  - Queue depth is the buffer between them
  - Sustained overload grows latency, not throughput

Sources:
  - Queue-Based Load Leveling pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling
  - Avoiding insurmountable queue backlogs (AWS Builders' Library) (accessed 2026-10-23)
  https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/

### I010

  Topic: Queue-based load leveling, backpressure and Little's Law
  Question: What failure modes does queue-based load leveling introduce?
  Expected answer: It adds end-to-end latency and operational complexity, and it can accumulate a
  backlog that is slow to drain. Duplicate or poison messages require idempotent consumers,
  dead-letter handling and retry limits, and consumers must scale with queue depth.

Key facts:
  - Adds latency between request and completion
  - Poison messages need dead-letter queues
  - Backlog growth can outlive the traffic spike

Sources:
  - Queue-Based Load Leveling pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling
  - Avoiding insurmountable queue backlogs (AWS Builders' Library) (accessed 2026-10-23)
  https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/

### I011

  Topic: Queue-based load leveling, backpressure and Little's Law
  Question: State Little's Law and one way to use it in capacity planning.
  Expected answer: Little's Law says the average number of items in a system equals the arrival
  rate times the average time each item spends there, L = lambda x W. It links queue length,
  throughput and latency, so a rising queue length at fixed throughput means growing wait time.

Key facts:
  - L = lambda x W for a stable system
  - Holds without assumptions about distributions
  - Queue length and wait time move together at fixed rate

Sources:
  - Little's law (Wikipedia) (accessed 2026-10-23)
  https://en.wikipedia.org/wiki/Little%27s_law
  - Queue-Based Load Leveling pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling

### I012

  Topic: Queue-based load leveling, backpressure and Little's Law
  Question: How does backpressure differ from buffering or dropping work?
  Expected answer: Backpressure returns a demand signal to the producer, which must not send more
  than the consumer has requested. Instead of buffering without bound or dropping silently, the
  producer slows down or the caller receives an explicit rejection.

Key facts:
  - Consumer advertises demand, producer respects it
  - Unbounded buffering hides overload as latency
  - Explicit rejection is a form of backpressure

Sources:
  - Reactive Streams specification (reactive-streams-jvm) (accessed 2026-10-23)
  https://github.com/reactive-streams/reactive-streams-jvm
  - Back pressure (Wikipedia) (accessed 2026-10-23)
  https://en.wikipedia.org/wiki/Back_pressure
  - Avoiding insurmountable queue backlogs (AWS Builders' Library) (accessed 2026-10-23)
  https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/

### I013

  Topic: Retries, idempotency keys and duplicate effects
  Question: Why do retries need backoff, jitter and an overall cap?
  Expected answer: Transient faults often clear on retry, but synchronized immediate retries
  amplify an outage. Exponential backoff spaces attempts, jitter decorrelates clients, and a retry
  cap or budget limits total attempts so retries cannot become the outage.

Key facts:
  - Retry only transient, retryable failures
  - Jitter prevents synchronized retry waves
  - Bound attempts and total retry time

Sources:
  - Timeouts, retries and backoff with jitter (AWS Builders' Library) (accessed 2026-10-23)
  https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
  - Making retries safe with idempotent APIs (AWS Builders' Library) (accessed 2026-10-23)
  https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/
  - Retry pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/retry

### I014

  Topic: Retries, idempotency keys and duplicate effects
  Question: Which HTTP methods are idempotent, and why is POST different?
  Expected answer: GET, HEAD, PUT, DELETE, OPTIONS and TRACE are defined as idempotent, so
  repeating them has the same intended effect. POST is neither safe nor idempotent, so a retried
  create can duplicate a resource unless the API adds a deduplication key.

Key facts:
  - PUT and DELETE are idempotent; POST is not
  - Idempotence concerns effect, not response body
  - Safe methods are also idempotent

Sources:
  - RFC 9110: HTTP Semantics (IETF) (accessed 2026-10-23)
  https://datatracker.ietf.org/doc/html/rfc9110
  - Idempotence (Wikipedia) (accessed 2026-10-23)
  https://en.wikipedia.org/wiki/Idempotence
  - Idempotent requests (Stripe API documentation) (accessed 2026-10-23)
  https://docs.stripe.com/api/idempotent_requests

### I015

  Topic: Retries, idempotency keys and duplicate effects
  Question: How does a server enforce an Idempotency-Key on create requests?
  Expected answer: The client sends a unique key for each logical operation, and the server stores
  the key with a request fingerprint and the resulting response. A replay returns the stored
  result, while reuse of the key with a different payload is rejected, for a bounded retention
  period.

Key facts:
  - A key identifies a logical operation
  - Server stores key, fingerprint and outcome
  - Retention windows bound storage

Sources:
  - Idempotency-Key HTTP header field (IETF draft) (accessed 2026-10-23)
  https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/
  - Idempotent requests (Stripe API documentation) (accessed 2026-10-23)
  https://docs.stripe.com/api/idempotent_requests

### I016

  Topic: Retries, idempotency keys and duplicate effects
  Question: Why can retries create duplicate effects, and how are they removed?
  Expected answer: A retry after an ambiguous timeout may repeat a request the server already
  applied, so delivery is at least once. Consumers remove duplicates with idempotent handlers or a
  processed-message table keyed by message id and committed with the side effect.

Key facts:
  - Ambiguous failures hide whether the write applied
  - At-least-once delivery makes dedupe mandatory
  - Dedupe record must commit with the effect

Sources:
  - Making retries safe with idempotent APIs (AWS Builders' Library) (accessed 2026-10-23)
  https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/
  - Outbox and inbox patterns explained (Event-Driven.io) (accessed 2026-10-23)
  https://event-driven.io/en/outbox_inbox_patterns_and_delivery_guarantees_explained/

### I017

  Topic: Sagas, compensating transactions, outbox and inbox patterns
  Question: How does a saga preserve consistency without a distributed transaction?
  Expected answer: A saga is a sequence of local transactions linked by messages or events, each
  with a compensating action. If a step fails, completed steps are undone by compensations, which
  gives atomicity-like outcomes but not isolation, so intermediate states stay visible.

Key facts:
  - Each saga step is a local ACID transaction
  - Compensations undo earlier completed steps
  - No isolation: intermediate states are visible

Sources:
  - Pattern: Saga (microservices.io) (accessed 2026-10-23)
  https://microservices.io/patterns/data/saga.html
  - Saga distributed transactions (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/saga/saga
  - Compensating Transaction pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction

### I018

  Topic: Sagas, compensating transactions, outbox and inbox patterns
  Question: Saga orchestration versus choreography: what are the trade-offs?
  Expected answer: Choreography lets services react to each other's events, which is simple and
  decoupled but leaves the flow implicit and can create cycles. Orchestration centralizes the
  sequence in a coordinator, which is easier to reason about but adds a component and coupling.

Key facts:
  - Choreography: events, implicit flow
  - Orchestration: explicit coordinator
  - Both need idempotent steps and compensations

Sources:
  - Pattern: Saga (microservices.io) (accessed 2026-10-23)
  https://microservices.io/patterns/data/saga.html
  - Saga distributed transactions (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/saga/saga

### I019

  Topic: Sagas, compensating transactions, outbox and inbox patterns
  Question: What does a transactional outbox make atomic?
  Expected answer: It makes the state change and the event record atomic by writing both in one
  local transaction. A relay then publishes outbox rows and retries until acknowledged, which
  removes the dual-write problem at the cost of at-least-once publication.

Key facts:
  - Outbox row commits with the domain change
  - Relay publishes and marks rows sent
  - Publication is at least once, so consumers dedupe

Sources:
  - Pattern: Transactional outbox (microservices.io) (accessed 2026-10-23)
  https://microservices.io/patterns/data/transactional-outbox.html
  - CQRS pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs
  - Outbox and inbox patterns explained (Event-Driven.io) (accessed 2026-10-23)
  https://event-driven.io/en/outbox_inbox_patterns_and_delivery_guarantees_explained/

### I020

  Topic: Sagas, compensating transactions, outbox and inbox patterns
  Question: What is the inbox pattern, and why does an outbox need one?
  Expected answer: Because relays retry, a consumer can receive the same message more than once.
  The inbox stores processed message ids in the same transaction as the business effect, so a
  redelivery is detected and ignored.

Key facts:
  - Inbox records ids of processed messages
  - Record commits with the business change
  - Outbox plus inbox gives effectively-once processing

Sources:
  - Outbox and inbox patterns explained (Event-Driven.io) (accessed 2026-10-23)
  https://event-driven.io/en/outbox_inbox_patterns_and_delivery_guarantees_explained/
  - Pattern: Transactional outbox (microservices.io) (accessed 2026-10-23)
  https://microservices.io/patterns/data/transactional-outbox.html
  - CQRS pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs

### I021

  Topic: CQRS, event sourcing and read projections
  Question: What does CQRS separate, and when is that separation justified?
  Expected answer: CQRS separates the write model that validates commands from one or more read
  models optimized for queries. It pays off when read and write workloads differ sharply or
  queries need different shapes, and it costs complexity plus eventual consistency.

Key facts:
  - Write model handles commands and invariants
  - Read models are query-optimized projections
  - Justified by asymmetric load or complex queries

Sources:
  - CQRS pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs
  - Pattern: CQRS (microservices.io) (accessed 2026-10-23)
  https://microservices.io/patterns/data/cqrs.html

### I022

  Topic: CQRS, event sourcing and read projections
  Question: Which consistency and operational costs does CQRS add?
  Expected answer: Read models lag behind writes, so clients can observe stale results until
  projections catch up. The design also adds messaging, duplicate handling, projection rebuilds
  and more moving parts to operate and migrate.

Key facts:
  - Reads may be stale until projections catch up
  - Messaging and duplicate handling are required
  - Read-model rebuilds cost time and compute

Sources:
  - CQRS pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs
  - Pattern: CQRS (microservices.io) (accessed 2026-10-23)
  https://microservices.io/patterns/data/cqrs.html

### I023

  Topic: CQRS, event sourcing and read projections
  Question: How does event sourcing rebuild state, and why use snapshots?
  Expected answer: State is a fold over an append-only event stream, so replaying events rebuilds
  an aggregate. A snapshot stores materialized state at a stream position, letting replay start
  from the snapshot plus later events and bounding rebuild time.

Key facts:
  - Events are the source of truth
  - Replay reconstructs aggregate state
  - Snapshots bound replay cost

Sources:
  - Event Sourcing pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
  - Pattern: Event sourcing (microservices.io) (accessed 2026-10-23)
  https://microservices.io/patterns/data/event-sourcing.html

### I024

  Topic: CQRS, event sourcing and read projections
  Question: How are read projections built and kept correct?
  Expected answer: Projections subscribe to the event stream and apply changes to a query store,
  tracking a checkpoint. They must be idempotent and ordered per entity, and must support rebuilds
  when logic or schema changes.

Key facts:
  - Projections consume events into a read store
  - Checkpoints make progress restartable
  - Idempotent updates tolerate redelivery

Sources:
  - Event Sourcing pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
  - CQRS pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs
  - Pattern: CQRS (microservices.io) (accessed 2026-10-23)
  https://microservices.io/patterns/data/cqrs.html

### I025

  Topic: Quorums, leader election, consensus and fencing
  Question: What does R + W > N guarantee in a replicated data store?
  Expected answer: With N replicas, a read quorum R and a write quorum W whose sum exceeds N
  overlap in at least one replica, so a read observes the latest acknowledged write. Larger
  quorums strengthen consistency but raise latency and reduce availability during failures.

Key facts:
  - R + W > N forces read and write quorum overlap
  - Quorum size trades latency for consistency
  - Cassandra exposes tunable consistency levels

Sources:
  - Cassandra architecture: Dynamo-style replication and consistency (accessed 2026-10-23)
  https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html
  - Dynamo: Amazon's highly available key-value store (SOSP 2007 paper) (accessed 2026-10-23)
  https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf
  - Write concern (MongoDB manual) (accessed 2026-10-23)
  https://www.mongodb.com/docs/manual/reference/write-concern/

### I026

  Topic: Quorums, leader election, consensus and fencing
  Question: How does Raft elect a leader, and why is a majority required?
  Expected answer: A candidate asks peers for votes in a new term and becomes leader once it has a
  majority. Majorities intersect, so two leaders cannot be elected in the same term, and a log
  entry is committed only after a majority stores it.

Key facts:
  - Votes are counted per term
  - Majorities intersect, preventing two leaders
  - Committed entries are stored on a majority

Sources:
  - In search of an understandable consensus algorithm (Raft paper) (accessed 2026-10-23)
  https://raft.github.io/raft.pdf
  - etcd learning documentation (accessed 2026-10-23)
  https://etcd.io/docs/v3.5/learning/

### I027

  Topic: Quorums, leader election, consensus and fencing
  Question: Why are leases unsafe without fencing, and what is a fencing token?
  Expected answer: A client can pause after its lease expires while another client takes the lease
  and writes; when the first client resumes it may overwrite newer data. A fencing token,
  incremented on each acquisition, lets the storage reject writes from stale holders.

Key facts:
  - Pauses can outlive a lease
  - A fencing token increases on each acquisition
  - Storage rejects writes with older tokens

Sources:
  - How to do distributed locking (Martin Kleppmann) (accessed 2026-10-23)
  https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html
  - Leases (Kubernetes documentation) (accessed 2026-10-23)
  https://kubernetes.io/docs/concepts/architecture/leases/

### I028

  Topic: Quorums, leader election, consensus and fencing
  Question: What availability cost comes with strongly consistent quorum writes?
  Expected answer: A write needs acknowledgements from a majority of voting replicas, so if enough
  replicas are slow or partitioned the write stalls or fails rather than diverging. The system
  chooses consistency over availability on the minority side of a partition.

Key facts:
  - Commit requires a majority of voters
  - A minority partition cannot commit writes
  - Latency includes the slowest quorum member

Sources:
  - Spanner replication (Google Cloud documentation) (accessed 2026-10-23)
  https://cloud.google.com/spanner/docs/replication
  - CAP twelve years later (InfoQ) (accessed 2026-10-23)
  https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/
  - Cassandra architecture: Dynamo-style replication and consistency (accessed 2026-10-23)
  https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html

### I029

  Topic: Rate limiting, admission control, load shedding and throttling
  Question: Token bucket versus leaky bucket: how do bursts differ?
  Expected answer: A token bucket accumulates tokens up to a burst size, allowing short bursts
  while enforcing the average rate. A leaky bucket drains at a fixed rate, smoothing output and
  typically queueing or dropping excess traffic.

Key facts:
  - Token bucket permits bursts up to bucket size
  - Leaky bucket smooths to a constant rate
  - Both bound the long-run average rate

Sources:
  - Token bucket (Wikipedia) (accessed 2026-10-23)
  https://en.wikipedia.org/wiki/Token_bucket
  - Leaky bucket (Wikipedia) (accessed 2026-10-23)
  https://en.wikipedia.org/wiki/Leaky_bucket
  - Scaling your API with rate limiters (Stripe Engineering) (accessed 2026-10-23)
  https://stripe.com/blog/rate-limiters
  - Throttle requests to your APIs (AWS API Gateway) (accessed 2026-10-23)
  https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html

### I030

  Topic: Rate limiting, admission control, load shedding and throttling
  Question: How should a throttled service respond, and what should clients do?
  Expected answer: Reject explicitly, typically with HTTP 429 and a Retry-After hint, instead of
  silently dropping or queueing forever. Clients should honor the hint, back off with jitter and
  reduce concurrency rather than retrying immediately.

Key facts:
  - 429 plus Retry-After signals backpressure
  - Clients back off and cap concurrency
  - Immediate retries turn throttling into an outage

Sources:
  - Rate Limiting pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/rate-limiting-pattern
  - Throttle requests to your APIs (AWS API Gateway) (accessed 2026-10-23)
  https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html
  - Scaling your API with rate limiters (Stripe Engineering) (accessed 2026-10-23)
  https://stripe.com/blog/rate-limiters

### I031

  Topic: Rate limiting, admission control, load shedding and throttling
  Question: What is load shedding, and how does criticality guide it?
  Expected answer: When demand exceeds capacity, the service drops or defers low-priority work so
  that critical requests still meet their objective. Google SRE ranks traffic by criticality and
  sheds the least critical classes first, rather than letting queues fail everything.

Key facts:
  - Shed lowest-criticality traffic first
  - Shedding preserves critical-path latency
  - Unbounded queues fail all requests

Sources:
  - Handling overload (Google SRE book) (accessed 2026-10-23)
  https://sre.google/sre-book/handling-overload/
  - Scaling your API with rate limiters (Stripe Engineering) (accessed 2026-10-23)
  https://stripe.com/blog/rate-limiters

### I032

  Topic: Rate limiting, admission control, load shedding and throttling
  Question: What is admission control, and why reject work early?
  Expected answer: Admission control decides whether to accept work before it consumes resources,
  rejecting or queueing when rate, concurrency or queue limits are exceeded. Early rejection keeps
  latency bounded and protects shared dependencies from overload.

Key facts:
  - Decide admission before spending resources
  - Limits cover rate, concurrency and queue depth
  - Early rejection protects downstream capacity

Sources:
  - Avoiding insurmountable queue backlogs (AWS Builders' Library) (accessed 2026-10-23)
  https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/
  - Rate Limiting pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/rate-limiting-pattern
  - Circuit breaking (Envoy documentation) (accessed 2026-10-23)
  https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/circuit_breaking

### I033

  Topic: Sharding, partition keys, hot partitions and rebalancing
  Question: Which properties make a partition key a good choice?
  Expected answer: A good key has high cardinality, spreads reads and writes evenly, and matches
  the dominant query pattern so requests touch one partition. Low-cardinality or time-ordered keys
  concentrate load and cause cross-partition fan-out.

Key facts:
  - High cardinality avoids oversized partitions
  - Even access distribution matters more than uniqueness
  - Align the key with the main query path

Sources:
  - Best practices for partition key design (AWS DynamoDB) (accessed 2026-10-23)
  https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html
  - Shard keys (MongoDB manual) (accessed 2026-10-23)
  https://www.mongodb.com/docs/manual/core/sharding-shard-key/
  - Sharding pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/sharding

### I034

  Topic: Sharding, partition keys, hot partitions and rebalancing
  Question: Why do time-ordered keys create hot partitions, and what helps?
  Expected answer: New writes all fall into the partition that owns the newest range, so one
  partition takes the write load while others idle. Adding entropy, such as a random suffix or
  bucket prefix, spreads writes, and adaptive splitting can relieve sustained skew.

Key facts:
  - Monotonic keys concentrate new writes
  - A random suffix or bucket prefix spreads load
  - Partition limits cap per-partition throughput

Sources:
  - Partition key design: using write sharding (AWS) (accessed 2026-10-23)
  https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-sharding.html
  - DynamoDB adaptive capacity (AWS) (accessed 2026-10-23)
  https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/adaptive-capacity.html
  - Partitioning overview (Azure Cosmos DB) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview

### I035

  Topic: Sharding, partition keys, hot partitions and rebalancing
  Question: How do virtual shards or consistent hashing reduce rebalancing cost?
  Expected answer: Mapping many logical shards onto fewer physical nodes, or hashing keys onto a
  ring, means adding a node moves only a fraction of the data instead of rehashing everything.
  With consistent hashing, adding one node moves roughly one nth of the keys.

Key facts:
  - Virtual shards decouple logical and physical layout
  - Consistent hashing moves a fraction of keys
  - Less data movement means shorter rebalances

Sources:
  - Sharding pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/sharding
  - Consistent hashing (Wikipedia) (accessed 2026-10-23)
  https://en.wikipedia.org/wiki/Consistent_hashing
  - Dynamo: Amazon's highly available key-value store (SOSP 2007 paper) (accessed 2026-10-23)
  https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf

### I036

  Topic: Sharding, partition keys, hot partitions and rebalancing
  Question: What operational risks follow from a low-cardinality shard key?
  Expected answer: Few distinct values mean few shards, so some shards are oversized or hot and
  rebalancing cannot even out load. Changing the key later requires a resharding migration with
  dual writes or a controlled cutover.

Key facts:
  - Few values limit maximum parallelism
  - Hot shards cause throttling and latency
  - Resharding needs migration planning

Sources:
  - Sharding pattern (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/patterns/sharding
  - Partitioning overview (Azure Cosmos DB) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview
  - Shard keys (MongoDB manual) (accessed 2026-10-23)
  https://www.mongodb.com/docs/manual/core/sharding-shard-key/

### I037

  Topic: Multi-region failover, replication and consistency trade-offs
  Question: How do RTO and RPO drive the choice of disaster recovery strategy?
  Expected answer: RTO is the acceptable downtime and RPO the acceptable data loss window. Backup
  and restore is cheap but slow, warm standby shortens RTO, and active/active multi-site gives the
  lowest RTO and RPO at the highest cost.

Key facts:
  - RTO bounds downtime; RPO bounds data loss
  - Strategy cost rises as RTO and RPO shrink
  - Active/active needs conflict handling

Sources:
  - Disaster recovery strategies on AWS (AWS Architecture Blog) (accessed 2026-10-23)
  https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-i-strategies-for-recovery-in-the-cloud/
  - Disaster recovery planning guide (Google Cloud) (accessed 2026-10-23)
  https://cloud.google.com/architecture/dr-scenarios-planning-guide

### I038

  Topic: Multi-region failover, replication and consistency trade-offs
  Question: Synchronous versus asynchronous replication: what is the trade-off?
  Expected answer: Synchronous replication waits for remote acknowledgement before commit, giving
  near-zero RPO but adding cross-region latency and failing when the remote is slow. Asynchronous
  replication commits locally and ships later, which lowers latency but can lose the unsent tail
  on failover.

Key facts:
  - Sync replication raises commit latency
  - Async replication risks losing recent writes
  - Quorum sync needs enough standbys

Sources:
  - Warm standby and streaming replication (PostgreSQL docs) (accessed 2026-10-23)
  https://www.postgresql.org/docs/current/warm-standby.html
  - Spanner replication (Google Cloud documentation) (accessed 2026-10-23)
  https://cloud.google.com/spanner/docs/replication
  - CAP twelve years later (InfoQ) (accessed 2026-10-23)
  https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/

### I039

  Topic: Multi-region failover, replication and consistency trade-offs
  Question: What must an active/active multi-region design solve?
  Expected answer: Both regions serve traffic, so writes must be routed, partitioned or reconciled
  to avoid conflicting updates. Replication then needs consensus or conflict resolution, and
  failover becomes traffic steering while latency, cost and consistency guarantees get harder.

Key facts:
  - Concurrent writers need conflict handling
  - Consensus or partitioning avoids divergence
  - Traffic steering replaces cold failover

Sources:
  - Disaster recovery strategies on AWS (AWS Architecture Blog) (accessed 2026-10-23)
  https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-i-strategies-for-recovery-in-the-cloud/
  - Spanner replication (Google Cloud documentation) (accessed 2026-10-23)
  https://cloud.google.com/spanner/docs/replication
  - CAP twelve years later (InfoQ) (accessed 2026-10-23)
  https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/

### I040

  Topic: Multi-region failover, replication and consistency trade-offs
  Question: How can failover create split brain, and what prevents it?
  Expected answer: If two sites both believe they are primary, both accept writes and the data
  diverges. Quorum-based election lets only a majority side commit, and leases with fencing tokens
  make stale writers' operations fail at the storage layer.

Key facts:
  - Split brain means two writable primaries
  - Quorum prevents minority-side commits
  - Fencing tokens reject stale writers

Sources:
  - Spanner replication (Google Cloud documentation) (accessed 2026-10-23)
  https://cloud.google.com/spanner/docs/replication
  - How to do distributed locking (Martin Kleppmann) (accessed 2026-10-23)
  https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html
  - In search of an understandable consensus algorithm (Raft paper) (accessed 2026-10-23)
  https://raft.github.io/raft.pdf

### I041

  Topic: SLIs, SLOs, error budgets and alerting
  Question: Define SLI, SLO and SLA, and give one example SLI.
  Expected answer: An SLI is a measured indicator, such as the fraction of requests served under
  300 ms. An SLO is an internal target for that indicator over a window, and an SLA is a contract
  with consequences for missing it.

Key facts:
  - SLIs are ratios of good to valid events
  - SLOs set an internal target and window
  - SLAs carry contractual consequences

Sources:
  - Service level objectives (Google SRE book) (accessed 2026-10-23)
  https://sre.google/sre-book/service-level-objectives/
  - Alerting on SLOs (Google SRE workbook) (accessed 2026-10-23)
  https://sre.google/workbook/alerting-on-slos/

### I042

  Topic: SLIs, SLOs, error budgets and alerting
  Question: How is an error budget computed and used in release decisions?
  Expected answer: The budget is one minus the SLO, expressed as the number of bad events or time
  allowed in the window. When the budget is spent, risky releases pause and reliability work takes
  priority; when it is healthy, teams can ship faster.

Key facts:
  - Budget = 1 - SLO over the window
  - Exhausted budget freezes risky changes
  - Budget policy links reliability and delivery

Sources:
  - Embracing risk (Google SRE book) (accessed 2026-10-23)
  https://sre.google/sre-book/embracing-risk/
  - Service level objectives (Google SRE book) (accessed 2026-10-23)
  https://sre.google/sre-book/service-level-objectives/

### I043

  Topic: SLIs, SLOs, error budgets and alerting
  Question: Why alert on burn rate instead of a raw error threshold?
  Expected answer: Burn rate measures how quickly the error budget is being consumed relative to
  the SLO window. Multi-window, multi-burn-rate alerts catch fast incidents and slow erosion while
  keeping false positives low, unlike fixed thresholds.

Key facts:
  - Burn rate = error rate divided by budget rate
  - Multiple windows improve precision and detection
  - Static thresholds page too often or too late

Sources:
  - Alerting on SLOs (Google SRE workbook) (accessed 2026-10-23)
  https://sre.google/workbook/alerting-on-slos/
  - Service level objectives (Google SRE book) (accessed 2026-10-23)
  https://sre.google/sre-book/service-level-objectives/

### I044

  Topic: SLIs, SLOs, error budgets and alerting
  Question: What are the four golden signals, and why monitor them?
  Expected answer: They are latency, traffic, errors and saturation, the four signals that
  describe a request-driven service. Saturation is the leading indicator, because it warns that a
  resource is approaching its limit before users see failures.

Key facts:
  - Latency, traffic, errors, saturation
  - Measure latency separately for success and failure
  - Saturation predicts imminent degradation

Sources:
  - Monitoring distributed systems (Google SRE book) (accessed 2026-10-23)
  https://sre.google/sre-book/monitoring-distributed-systems/
  - Service level objectives (Google SRE book) (accessed 2026-10-23)
  https://sre.google/sre-book/service-level-objectives/

### I045

  Topic: Distributed tracing, context propagation and sampling
  Question: What does the W3C traceparent header carry, and who forwards it?
  Expected answer: It carries a version, trace-id, parent-id and trace-flags, so each service can
  attach its span to the same trace. Instrumentation forwards the header, plus optional
  tracestate, on every downstream call across process boundaries.

Key facts:
  - traceparent fields: version, trace-id, parent-id, flags
  - The sampled flag is carried in trace-flags
  - tracestate carries vendor-specific data

Sources:
  - W3C Trace Context recommendation (accessed 2026-10-23)
  https://www.w3.org/TR/trace-context/
  - Context propagation (OpenTelemetry documentation) (accessed 2026-10-23)
  https://opentelemetry.io/docs/concepts/context-propagation/

### I046

  Topic: Distributed tracing, context propagation and sampling
  Question: Head-based versus tail-based sampling: what do you gain and lose?
  Expected answer: Head-based sampling decides at trace start, which is cheap but cannot know the
  outcome, so rare errors may be dropped. Tail-based sampling buffers complete traces and decides
  on attributes such as errors or latency, improving debugging at the cost of buffering and
  central collection.

Key facts:
  - Head sampling is decided before the outcome is known
  - Tail sampling needs trace buffering
  - Bias affects latency and error statistics

Sources:
  - Sampling (OpenTelemetry documentation) (accessed 2026-10-23)
  https://opentelemetry.io/docs/concepts/sampling/
  - Dapper: distributed systems tracing infrastructure (Google paper) (accessed 2026-10-23)
  https://static.googleusercontent.com/media/research.google.com/en//archive/papers/dapper-2010-1.pdf

### I047

  Topic: Distributed tracing, context propagation and sampling
  Question: How do spans form a trace, and what does a parent reference mean?
  Expected answer: A trace is a tree of spans that share a trace-id, and each span has its own
  span-id plus the parent span-id of its caller. That linkage reconstructs timing and causality
  across services.

Key facts:
  - One trace-id is shared by all spans
  - Parent links encode call causality
  - Span timing shows where time is spent

Sources:
  - Dapper: distributed systems tracing infrastructure (Google paper) (accessed 2026-10-23)
  https://static.googleusercontent.com/media/research.google.com/en//archive/papers/dapper-2010-1.pdf
  - W3C Trace Context recommendation (accessed 2026-10-23)
  https://www.w3.org/TR/trace-context/
  - Context propagation (OpenTelemetry documentation) (accessed 2026-10-23)
  https://opentelemetry.io/docs/concepts/context-propagation/

### I048

  Topic: Distributed tracing, context propagation and sampling
  Question: Why is sampling necessary, and what bias can it introduce?
  Expected answer: Tracing every request is expensive in storage, CPU and network, so systems
  sample to cut overhead. Uniform sampling preserves aggregate rates but can miss rare failures,
  while attribute or adaptive sampling can distort metrics unless weights are accounted for.

Key facts:
  - Full-fidelity tracing is costly at scale
  - Sampling trades visibility for overhead
  - Weights or stratification reduce bias

Sources:
  - Sampling (OpenTelemetry documentation) (accessed 2026-10-23)
  https://opentelemetry.io/docs/concepts/sampling/
  - Dapper: distributed systems tracing infrastructure (Google paper) (accessed 2026-10-23)
  https://static.googleusercontent.com/media/research.google.com/en//archive/papers/dapper-2010-1.pdf

### I049

  Topic: Zero trust, least privilege and tenant isolation
  Question: Which access decisions does zero trust make per request?
  Expected answer: Every request is authenticated and authorized for the specific resource, using
  dynamic policy based on identity, device and context rather than network location. NIST frames
  access as granted per session with the least privileges needed.

Key facts:
  - No implicit trust from network location
  - Access is granted per session and resource
  - Dynamic policy uses identity and context

Sources:
  - NIST SP 800-207: Zero Trust Architecture (accessed 2026-10-23)
  https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf
  - Zero Trust Maturity Model (CISA) (accessed 2026-10-23)
  https://www.cisa.gov/zero-trust-maturity-model

### I050

  Topic: Zero trust, least privilege and tenant isolation
  Question: How is least privilege applied to workloads and service identities?
  Expected answer: Grant only the permissions a task needs, scope them to specific resources, and
  prefer short-lived credentials or roles over long-lived keys. Permissions should be reviewed and
  unused grants removed as the workload changes.

Key facts:
  - Scope permissions to actions and resources
  - Prefer short-lived credentials
  - Review and remove unused permissions

Sources:
  - IAM security best practices (AWS) (accessed 2026-10-23)
  https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html
  - NIST SP 800-207: Zero Trust Architecture (accessed 2026-10-23)
  https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf
  - Zero Trust Maturity Model (CISA) (accessed 2026-10-23)
  https://www.cisa.gov/zero-trust-maturity-model

### I051

  Topic: Zero trust, least privilege and tenant isolation
  Question: Compare dedicated and shared tenant isolation models.
  Expected answer: Dedicated resources give each tenant its own infrastructure and data, which
  simplifies isolation and noisy-neighbor control but costs more. Shared resources use
  tenant-scoped partitioning and authorization, which is efficient but makes correctness of tenant
  scoping critical.

Key facts:
  - Dedicated: stronger isolation, higher cost
  - Shared: efficient, scoping-critical
  - Many systems mix models by tenant tier

Sources:
  - SaaS tenant isolation strategies (AWS whitepaper) (accessed 2026-10-23)
  https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.html
  - Storage and data in multitenant solutions (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/storage-data

### I052

  Topic: Zero trust, least privilege and tenant isolation
  Question: How can one tenant read another tenant's data, and which controls prevent it?
  Expected answer: Leakage happens when a query, cache key or connection lacks tenant scoping, or
  when authorization checks identity but not tenant. Prevent it with tenant ids in every key and
  query, centralized enforcement, row-level or per-tenant encryption, and cross-tenant tests.

Key facts:
  - Missing tenant scope leaks rows
  - Enforce tenant checks centrally
  - Per-tenant keys limit blast radius

Sources:
  - Storage and data in multitenant solutions (Microsoft Learn) (accessed 2026-10-23)
  https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/storage-data
  - SaaS tenant isolation strategies (AWS whitepaper) (accessed 2026-10-23)
  https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.html
  - NIST SP 800-207: Zero Trust Architecture (accessed 2026-10-23)
  https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf

### I053

  Topic: API contracts, versioning and expand-and-contract migration
  Question: Which API changes are backward compatible?
  Expected answer: Adding optional fields or new endpoints and relaxing validation are compatible.
  Removing or renaming fields, changing types or semantics, or making optional fields required are
  breaking changes that need a new version or migration.

Key facts:
  - Additive optional changes are compatible
  - Removing or renaming fields breaks clients
  - Servers should tolerate unknown fields

Sources:
  - AIP-180: Backwards compatibility (accessed 2026-10-23)
  https://aip.dev/180
  - Semantic Versioning 2.0.0 (accessed 2026-10-23)
  https://semver.org/
  - Azure API design guidelines (Microsoft) (accessed 2026-10-23)
  https://github.com/microsoft/api-guidelines/blob/vNext/azure/Guidelines.md

### I054

  Topic: API contracts, versioning and expand-and-contract migration
  Question: How does expand-and-contract migrate a breaking change?
  Expected answer: Expand adds the new field or endpoint while the old one still works, and the
  system writes both. Migrate moves consumers and verifies usage with telemetry, then contract
  removes the old path once no callers remain.

Key facts:
  - Expand: add new alongside old
  - Migrate: move consumers, watch telemetry
  - Contract: remove old after usage reaches zero

Sources:
  - Parallel change, also known as expand and contract (Martin Fowler) (accessed 2026-10-23)
  https://martinfowler.com/bliki/ParallelChange.html
  - AIP-180: Backwards compatibility (accessed 2026-10-23)
  https://aip.dev/180
  - API versioning (Stripe API documentation) (accessed 2026-10-23)
  https://docs.stripe.com/api/versioning

### I055

  Topic: API contracts, versioning and expand-and-contract migration
  Question: How do URI, query or header and date-based API versioning differ?
  Expected answer: URI versioning puts the major version in the path, which is visible but changes
  URLs. Query or header parameters keep URLs stable but can be missed by caches and logs, while
  date-based versions pin behavior to a release date so providers can evolve defaults.

Key facts:
  - URI versioning is simple and explicit
  - Header versions are easy to overlook
  - Date-based versions pin behavior per date

Sources:
  - API versioning (Stripe API documentation) (accessed 2026-10-23)
  https://docs.stripe.com/api/versioning
  - Azure API design guidelines (Microsoft) (accessed 2026-10-23)
  https://github.com/microsoft/api-guidelines/blob/vNext/azure/Guidelines.md
  - AIP-185: API versioning (accessed 2026-10-23)
  https://aip.dev/185

### I056

  Topic: API contracts, versioning and expand-and-contract migration
  Question: How should a field be deprecated and removed safely?
  Expected answer: Announce the deprecation, keep the old form working while adding the
  replacement, and instrument usage. Remove only after telemetry shows no traffic and a sunset
  date has passed, and document the migration for clients.

Key facts:
  - Keep old and new forms during migration
  - Use telemetry to confirm zero usage
  - Set and communicate a sunset date

Sources:
  - Parallel change, also known as expand and contract (Martin Fowler) (accessed 2026-10-23)
  https://martinfowler.com/bliki/ParallelChange.html
  - AIP-180: Backwards compatibility (accessed 2026-10-23)
  https://aip.dev/180
  - API versioning (Stripe API documentation) (accessed 2026-10-23)
  https://docs.stripe.com/api/versioning

### I057

  Topic: Canary, blue-green, rollback and progressive delivery
  Question: How does a canary release limit the blast radius of a bad change?
  Expected answer: A canary sends a small share of traffic or a small cohort to the new version
  while the baseline keeps serving. Error rate and latency are compared, and the rollout is
  promoted gradually or aborted, so regressions affect few users.

Key facts:
  - A small traffic slice limits exposure
  - Compare canary against baseline metrics
  - Automated abort contains regressions

Sources:
  - Canary release (Martin Fowler) (accessed 2026-10-23)
  https://martinfowler.com/bliki/CanaryRelease.html
  - Canary deployments (Argo Rollouts documentation) (accessed 2026-10-23)
  https://argo-rollouts.readthedocs.io/en/stable/features/canary/
  - Canarying releases (Google SRE workbook) (accessed 2026-10-23)
  https://sre.google/workbook/canarying-releases/

### I058

  Topic: Canary, blue-green, rollback and progressive delivery
  Question: Blue-green versus canary: resource cost and rollback speed?
  Expected answer: Blue-green runs two full environments and switches all traffic once the new one
  is validated, so rollback is a fast switch back but capacity doubles. Canary uses a small slice
  and limits exposure, but needs traffic splitting and takes longer to reach full rollout.

Key facts:
  - Blue-green needs duplicate capacity
  - Rollback is a traffic switch
  - Canary reduces exposure, not resource cost

Sources:
  - Blue-green deployment (Martin Fowler) (accessed 2026-10-23)
  https://martinfowler.com/bliki/BlueGreenDeployment.html
  - Blue-green deployments (Argo Rollouts documentation) (accessed 2026-10-23)
  https://argo-rollouts.readthedocs.io/en/stable/features/bluegreen/
  - Canarying releases (Google SRE workbook) (accessed 2026-10-23)
  https://sre.google/workbook/canarying-releases/

### I059

  Topic: Canary, blue-green, rollback and progressive delivery
  Question: What is progressive delivery, and how does automated analysis gate it?
  Expected answer: Progressive delivery exposes a new version gradually and checks metrics at
  defined steps before increasing traffic. A controller such as Flagger or Argo Rollouts runs the
  analysis and aborts or rolls back when error rate, latency or custom checks fail.

Key facts:
  - Traffic increases in ordered steps
  - Analysis gates promotion
  - Failure triggers automatic rollback

Sources:
  - How Flagger works (Flagger documentation) (accessed 2026-10-23)
  https://docs.flagger.app/usage/how-it-works
  - Canary deployments (Argo Rollouts documentation) (accessed 2026-10-23)
  https://argo-rollouts.readthedocs.io/en/stable/features/canary/
  - Canarying releases (Google SRE workbook) (accessed 2026-10-23)
  https://sre.google/workbook/canarying-releases/

### I060

  Topic: Canary, blue-green, rollback and progressive delivery
  Question: What makes rollback safe when a release changes stored data?
  Expected answer: Rolling back code is unsafe if the new version wrote data the old code cannot
  read. Use backward-compatible schema changes and dual writes or reads during the transition, and
  keep the previous version deployable so traffic can be shifted back.

Key facts:
  - Schema changes must be backward compatible
  - Dual write or dual read bridges the transition
  - Keep the previous version deployable for rollback

Sources:
  - Blue-green deployment (Martin Fowler) (accessed 2026-10-23)
  https://martinfowler.com/bliki/BlueGreenDeployment.html
  - Parallel change, also known as expand and contract (Martin Fowler) (accessed 2026-10-23)
  https://martinfowler.com/bliki/ParallelChange.html
  - Blue-green deployments (Argo Rollouts documentation) (accessed 2026-10-23)
  https://argo-rollouts.readthedocs.io/en/stable/features/bluegreen/

## Unanswerable questions

### U001

  Topic: Cache-aside, write-through, write-around and write-behind caching
  Question: Which caching product gives the lowest read latency for a 100 GB working set?
  Reason: vendor-specific

### U002

  Topic: Cache-aside, write-through, write-around and write-behind caching
  Question: What does a managed cache provider charge per million reads this month?
  Reason: current-fact

### U003

  Topic: Cache invalidation, TTL, stampede protection and hot keys
  Question: What cache hit ratio did our production cluster achieve last month?
  Reason: exact-measurement

### U004

  Topic: Queue-based load leveling, backpressure and Little's Law
  Question: How many messages per second can one managed FIFO queue sustain today?
  Reason: vendor-specific

### U005

  Topic: Queue-based load leveling, backpressure and Little's Law
  Question: What was our production queue depth at peak last week?
  Reason: exact-measurement

### U006

  Topic: Retries, idempotency keys and duplicate effects
  Question: Which retry library does the latest Spring Boot release use by default?
  Reason: vendor-specific

### U007

  Topic: Sagas, compensating transactions, outbox and inbox patterns
  Question: What is the maximum saga step count in the current Camunda release?
  Reason: vendor-specific

### U008

  Topic: Sagas, compensating transactions, outbox and inbox patterns
  Question: Should our payroll system use sagas or two-phase commit?
  Reason: out-of-scope

### U009

  Topic: CQRS, event sourcing and read projections
  Question: What read-model lag does our reporting pipeline show at peak?
  Reason: exact-measurement

### U010

  Topic: Quorums, leader election, consensus and fencing
  Question: Which etcd patch release is the newest stable version this week?
  Reason: current-fact

### U011

  Topic: Quorums, leader election, consensus and fencing
  Question: How many nodes does our production etcd cluster run?
  Reason: exact-measurement

### U012

  Topic: Rate limiting, admission control, load shedding and throttling
  Question: What rate limit does our payment provider apply to the Charges API?
  Reason: vendor-specific

### U013

  Topic: Rate limiting, admission control, load shedding and throttling
  Question: What is the current price per million API Gateway requests in us-east-1?
  Reason: current-fact

### U014

  Topic: Sharding, partition keys, hot partitions and rebalancing
  Question: How many partitions does our production table currently have?
  Reason: exact-measurement

### U015

  Topic: Multi-region failover, replication and consistency trade-offs
  Question: Which region pair should our company choose for data residency?
  Reason: out-of-scope

### U016

  Topic: SLIs, SLOs, error budgets and alerting
  Question: What SLO target should our checkout service adopt?
  Reason: out-of-scope

### U017

  Topic: Distributed tracing, context propagation and sampling
  Question: What sampling rate does Google use for all production traces today?
  Reason: current-fact

### U018

  Topic: Zero trust, least privilege and tenant isolation
  Question: Does our tenant isolation design satisfy the external auditor?
  Reason: out-of-scope

### U019

  Topic: API contracts, versioning and expand-and-contract migration
  Question: When will the payment provider retire API version 2019-12-03?
  Reason: current-fact

### U020

  Topic: Canary, blue-green, rollback and progressive delivery
  Question: What canary traffic percentage does our company release policy require?
  Reason: out-of-scope

## Limits

  - Labels are agent-adjudicated, not human-reviewed; no agreement scores exist.
  - All cited URLs returned HTTP 200 when retrieved on 2026-10-23; content may change later.
  - Answer keys paraphrase the cited material and omit many exceptions and edge cases.
  - Sources were checked for the concepts they support, not sentence by sentence.
  - Source authority varies: standards and papers, vendor documentation and engineering blogs.
  - JSON lines over 100 chars are only long answer keys and URLs; JSON strings cannot wrap.
  - The Markdown mirror wraps prose at 96 characters; source URL lines may exceed 100 characters.
  - Unanswerable items cite no sources: they need private, account-specific or future data.
  - No repository, book page, search output or pre-existing qrels material was read for this set.

## Provenance

  Questions, key facts and sources were researched on the public web on 2026-10-23 and
  HTTP-checked before inclusion. The set was frozen before any mapping to a book corpus was
  attempted. Formal independent human review and owner acceptance remain separate gates.

