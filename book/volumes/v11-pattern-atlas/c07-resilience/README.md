---
metadata_version: 1
id: "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c07-resilience/README.md"
title: "V11/C07 — Resilience and fault tolerance"
topic_ids:
  - "performance-engineering"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "operations"
summary: "All 16 C07 cards with bounded owner links; decision coverage partial."
route_hints:
  questions:
    - "Which resilience mechanisms bound failure without amplifying it?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.22fa23c6c7a6b0c29a52137bc67a00c9"
    - "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
  excludes:
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "resilience and fault tolerance"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.resilience4j"
    - "src.sre-cascading"
    - "src.sre-overload"
    - "src.grpc-deadlines"
    - "src.grpc-protocol"
    - "src.microsoft-cloud-patterns"
    - "src.aws-sqs"
    - "src.rabbitmq"
    - "src.morning-paper-tail-at-scale"
    - "src.kubernetes"
  claim_ids: []
  status: "source-linked"
  notes: >-
    16 cards cite read units; owner links are bounded. Hedged Requests moved to a
    dedicated page on 2026-10-31 with Google SRE, Tail at Scale, gRPC and AWS
    units. Failover/Failback moved to a dedicated page on 2026-10-31 with AWS
    Route 53, Azure Site Recovery, PostgreSQL 17 and Google SRE units. The
    Priority Queue card moved to a dedicated page on 2026-10-31 with RabbitMQ
    priority, the Azure Priority Queue pattern, Service Bus AMQP mapping and SQS
    queue-type and fair-queue units.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# V11/C07 — Resilience and fault tolerance

**Owning question:** Which resilience pattern fits the failure and recovery contract?

## Purpose and mission

This chapter is the atlas entry point for **Resilience and fault tolerance**. It owns
the conditional decision route for 16 catalog entries, not the deep mechanism
explanations. Read the exact owner section before applying a mechanism claim.

All 16 entries have a self-checked card. Owner sections are bounded: an overload or
deadline page may own the failure contract without owning every resilience mechanism.

## Pages and reasoning route

Page count is content-dependent. This chapter currently uses one landing page plus
dedicated card pages for moved entries; a later split is an editorial change, not a plan
failure. Start with the card, check its conditions and contraindications, then read the
exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Circuit Breaker

See the [dedicated Circuit Breaker card](circuit-breaker.md).

### Bulkhead

See the [Bulkhead](bulkhead.md) card.

### Retry with Exponential Backoff

See the [Retry with Exponential Backoff](retry-with-exponential-backoff.md) card.

### Retry with Jitter

See the [Retry with Jitter](retry-with-jitter.md) card.

### Timeout

See the [Timeout](timeout.md) card.

### Deadline Propagation

See the [dedicated Deadline Propagation card](deadline-propagation.md).

### Fallback

See the [Fallback](fallback.md) card.

### Graceful Degradation

See the [dedicated Graceful Degradation card](graceful-degradation.md).

### Load Shedding

See the [Load Shedding](load-shedding.md) card.

### Throttling

See the [Throttling](throttling.md) card.

### Rate Limiting

See the [Rate Limiting](rate-limiting.md) card.

### Queue-Based Load Leveling

See the [dedicated Queue-Based Load Leveling card](queue-based-load-leveling.md).

### Priority Queue

See the [dedicated Priority Queue card](priority-queue.md).

### Hedged Requests

See the [dedicated Hedged Requests card](hedged-requests.md).

### Health Endpoint Monitoring

See the [dedicated Health Endpoint Monitoring card](health-endpoint-monitoring.md).

### Failover / Failback

See the [dedicated Failover / Failback card](failover-failback.md).

## Chapter result and counterexample

Sixteen cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: retrying a non-idempotent write without a key is not evidence for the
retry card's contraindications.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C06](../c06-database-storage/README.md).
- Next: [V11/C08](../c08-coordination/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 16 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.
