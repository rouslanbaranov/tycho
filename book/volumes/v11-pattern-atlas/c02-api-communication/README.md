---
metadata_version: 1
id: "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c02-api-communication/README.md"
title: "V11/C02 — API and service communication"
topic_ids:
  - "application-architecture"
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "All 12 C02 cards with bounded owner links; decision coverage partial."
route_hints:
  questions:
    - "Which API and discovery patterns fit the trust boundary?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.e996607f707421ca388796732547cafd"
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  excludes:
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "api and service communication"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.microservices-patterns"
    - "src.microsoft-cloud-patterns"
    - "src.microsoft-api-design"
    - "src.aws-bff"
    - "src.envoy"
    - "src.kubernetes"
    - "src.aws-api-gateway"
    - "src.azure-api-management"
  claim_ids: []
  status: "source-linked"
  notes: "12 cards cite read units; owner links are bounded."
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
# V11/C02 — API and service communication

**Owning question:** Which API and discovery patterns fit the trust boundary?

## Purpose and mission

This chapter is the atlas entry point for **API and service communication**. It owns
the conditional decision route for 12 catalog entries, not the deep mechanism
explanations. Read the exact owner section before applying a mechanism claim.

All 12 entries have a self-checked card. Their owner sections are bounded: a gateway
page may own the edge boundary and aggregation mechanics without owning every BFF
mechanism.

## Pages and reasoning route

Page count is content-dependent. This chapter uses a landing page plus dedicated card
pages; a later split is an editorial change, not a plan failure. Start with the card,
check its conditions and contraindications, then read the exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### API Gateway

See the [dedicated API Gateway card](api-gateway.md).

### Gateway Routing

See the [dedicated Gateway Routing card](gateway-routing.md).

### Gateway Aggregation

See the [Gateway Aggregation](gateway-aggregation.md) card.

### Gateway Offloading

See the [Gateway Offloading](gateway-offloading.md) card.

### Backend for Frontend (BFF)

See the [dedicated Backend for Frontend (BFF) card](backend-for-frontend.md).

### API Composition

See the [dedicated API Composition card](api-composition.md).

### Reverse Proxy

See the [Reverse Proxy](reverse-proxy.md) card.

### Service Discovery

See the [dedicated Service Discovery card](service-discovery.md).

### Client-Side Discovery

See the [Client-Side Discovery](client-side-discovery.md) card.

### Server-Side Discovery

See the [dedicated Server-Side Discovery card](server-side-discovery.md).

### Asynchronous Request-Reply

See the [dedicated Asynchronous Request-Reply card](async-request-reply.md).

### Gatekeeper

See the [dedicated Gatekeeper card](gatekeeper.md).

## Chapter result and counterexample

Twelve cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: an API gateway that validates a token but forwards an untrusted tenant
header to every backend is not evidence for the gatekeeper or offloading cards.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C01](../c01-application-boundaries/README.md).
- Next: [V11/C03](../c03-messaging-integration/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 12 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated pattern manuscripts.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.
