---
metadata_version: 1
id: "tycho.chapter.a4b31346a691566550633efe0cf2693e"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c03-messaging-integration/README.md"
title: "V11/C03 — Messaging and event-driven integration"
topic_ids:
  - "integration-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "All 20 C03 cards with bounded owner links; decision coverage partial."
route_hints:
  questions:
    - "Which messaging pattern fits the delivery and ownership contract?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  excludes:
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "messaging integration"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.enterprise-integration"
    - "src.camel"
    - "src.aws-scatter-gather"
    - "src.microsoft-cloud-patterns"
    - "src.aws-sqs-dlq"
    - "src.azure-service-bus-dlq"
    - "src.hookdeck-dlq-alternatives"
  claim_ids: []
  status: "source-linked"
  notes: "All 20 cards cite read units; owner links are bounded sections, not dedicated EIP pages."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-11-01"
source_inspection_date: "2026-10-30"
content_verified_at: null
---
# V11/C03 — Messaging and event-driven integration

**Owning question:** Which messaging pattern fits the delivery and ownership contract?

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C02](../c02-api-communication/README.md).
- Next: [V11/C04](../c04-consistency-events/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Purpose and mission

This chapter is the atlas entry point for **Messaging and event-driven integration**.
It owns the conditional decision route for 20 catalog entries, not the deep mechanism
explanations. Read the exact owner section before applying a mechanism claim.

All 20 entries have a self-checked card. Owner sections are bounded: a messaging-family
or workflow page may own the delivery contract without owning every EIP mechanism.

## Pages and reasoning route

Page count is content-dependent. This chapter uses a landing page plus dedicated card
pages for entries prepared for independent review; a later split is an editorial change, not
a plan failure. Start with the card, check its conditions and contraindications, then read the
exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Publish / Subscribe

See the [Publish/Subscribe](publish-subscribe.md) card.

### Point-to-Point Queue

See the [Point-to-Point Queue](point-to-point-queue.md) card.

### Competing Consumers

See the [Competing Consumers](competing-consumers.md) card.

### Event-Driven Consumer

See the [Event-Driven Consumer](event-driven-consumer.md) card.

### Request-Reply Messaging

See the [dedicated Request-Reply Messaging card](request-reply-messaging.md).

### Correlation Identifier

See the [dedicated Correlation Identifier card](correlation-identifier.md).

### Content-Based Router

See the [Content-Based Router](content-based-router.md) card.

### Message Filter

See the [dedicated Message Filter card](message-filter.md).

### Pipes and Filters

See the [dedicated Pipes and Filters card](pipes-and-filters.md).

### Splitter

See the [dedicated Splitter card](splitter.md).

### Aggregator

See the [dedicated Aggregator card](aggregator.md).

### Scatter-Gather

See the [dedicated Scatter-Gather card](scatter-gather.md).

### Dead Letter Channel / DLQ

See the [dedicated Dead Letter Channel / DLQ card](dead-letter-channel.md).

### Durable Subscriber

See the [Durable Subscriber](durable-subscriber.md) card.

### Idempotent Receiver

See the [dedicated Idempotent Receiver card](idempotent-receiver.md).

### Resequencer

See the [dedicated Resequencer card](resequencer.md).

### Claim Check

See the [dedicated Claim Check card](claim-check.md).

### Message Broker / Messaging Bridge

See the [Message Broker / Messaging Bridge](message-broker-messaging-bridge.md) card.

### Canonical Data Model

See the [Canonical Data Model](canonical-data-model.md) card.

### Process Manager-Routing Slip

See the [Process Manager / Routing Slip](process-manager-routing-slip.md) card.

## Evidence and known limits

- All 20 cards cite read ledger units; owner links and backlinks are self-checked.
- Decision coverage is partial; no independent review or owner acceptance is claimed.
