---
metadata_version: 1
id: "tycho.chapter.e996607f707421ca388796732547cafd"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c01-application-boundaries/README.md"
title: "V11/C01 — Application architecture and boundaries"
topic_ids:
  - "application-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "All 12 C01 cards with bounded technical-owner links; decision coverage partial."
route_hints:
  questions:
    - "Which application patterns fit a bounded ownership model?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  excludes:
    - "Owner links are bounded; no sufficiency, complete family audit or independent review."
  keywords:
    - "pattern atlas"
    - "application architecture and boundaries"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.monolith-first"
    - "src.spring-modulith"
    - "src.aws-hexagonal"
    - "src.fowler-bounded-context"
    - "src.ddd-reference"
    - "src.microsoft-ddd"
    - "src.microsoft-cloud-patterns"
    - "src.fowler-layering"
    - "src.microservices"
    - "src.soa-model"
    - "src.microsoft-service-orientation"
    - "src.microsoft-dotnet-soa"
    - "src.clean-architecture"
    - "src.microservices-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "All 12 cards cite read units; eight use bounded owner sections and remain partial."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-30"
source_inspection_date: "2026-10-30"
content_verified_at: null
---
# V11/C01 — Application architecture and boundaries

**Owning question:** Which application patterns fit a bounded ownership model?

## Purpose and mission

This chapter is the atlas entry point for **Application architecture and boundaries**.
It owns the conditional decision route for 12 catalog entries, not the deep mechanism
explanations. Read the candidate technical owner before applying a mechanism claim.

All 12 entries have a Phase 3 decision card in this chapter. Four have a dedicated owner section;
eight use bounded sections that own part of the mechanism. A card is decision guidance,
not a technical manuscript and not proof of fit.

## Pages and reasoning route

Page count is content-dependent. This chapter uses a landing page plus dedicated card
pages; a later split is an editorial change, not a plan failure. Start with the card,
check its conditions and contraindications, then read the exact technical owner section
before choosing a mechanism.

## Entry inventory

Each level-three heading is a stable atlas anchor. Candidate areas and pages are
provisional unless a card names an exact technical owner. All cards are self-checked;
twelve are owner-linked and eight use bounded sections. None claims sufficient
coverage.

### Layered Architecture

**Identity.** Layered Architecture; family Application architecture and boundaries;
kind architecture-style; priority core.

**Decision question.** Should responsibilities be grouped into layers with an enforced
dependency direction, rather than organized around ports or independently deployed
services?

**Good-fit conditions.** The application has distinct presentation, application and
domain concerns; one dependency direction can be enforced; layer boundaries correspond
to real change or test boundaries; independent deployment and scale are not required.

**Hard contraindications.** Reject the claim when domain logic is already spread across
layers, when layers are used as deployment units, when shared mutable data crosses all
layers, or when layering adds ceremony without protecting a real change boundary.

**Competing alternative.** Hexagonal architecture with explicit ports and adapters, or
a modular monolith with module contracts. Reverse the choice when technology adapters
dominate or the dependency rule cannot be enforced.

**Failure and recovery.** Layer leakage, transaction boundaries that span layers and
anemic domain models are common. Recovery starts with dependency checks, explicit
contracts and a review of the change boundary; the linked owner section states the
remaining limits.

**Technical owner.** [Layered Architecture](../../v02-application-boundaries-and-contracts/c01-layered-modular-and-ports-and-adapters-design/layered-hexagonal-ports-and-adapters.md#layered-architecture) — The section owns layering and dependency direction; it is not a dedicated layering manuscript.

**Sources.** [src.fowler-layering](../../../../edition/patterns/reading-ledger.v1.json)
read record read.fowler-layering.2026-10-21: Presentation Domain Data Layering,
sections "Presentation Domain Data Layering", "Further Reading", "Acknowledgements",
"Notes". This is a definitional article, not a comparative study.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Hexagonal Architecture; Clean / Onion Architecture; Modular
Monolith; Microservices Architecture.

### Modular Monolith

See the [dedicated Modular Monolith card](modular-monolith.md).

### Microservices Architecture

See the [dedicated Microservices Architecture card](microservices-architecture.md).

### Service-Oriented Architecture (SOA)

See the [dedicated Service-Oriented Architecture (SOA) card](service-oriented-architecture.md).

### Hexagonal Architecture / Ports and Adapters

**Identity.** Hexagonal Architecture / Ports and Adapters; aliases Ports and Adapters;
family Application architecture and boundaries; kind architecture-style; priority core.

**Decision question.** Should domain logic be isolated from input/output technology
through explicit ports and adapters?

**Good-fit conditions.** The domain has behavior worth protecting; more than one adapter
or technology is plausible; tests need to run without external systems; a legacy or
vendor boundary is being replaced incrementally.

**Hard contraindications.** Reject the claim for a trivial CRUD surface with one stable
adapter; when no domain behavior exists to isolate; when the team cannot own mapping and
contract tests; or when ports are used to justify a distributed service split without
operational need.

**Competing alternative.** Layered architecture without ports, or a modular monolith
with direct adapters. Reverse the choice when adapter variability disappears or the
abstraction cost exceeds the isolation benefit.

**Failure and recovery.** Ports can leak technology types, adapter errors can be mapped
inconsistently, and mapping layers can hide latency. Recovery requires contract tests,
explicit error translation and a review of the adapter boundary in the technical owner.

**Technical owner.** [Hexagonal Architecture / Ports and Adapters](../../v02-application-boundaries-and-contracts/c01-layered-modular-and-ports-and-adapters-design/layered-hexagonal-ports-and-adapters.md#hexagonal-architecture-and-ports-and-adapters).

**Sources.** [src.aws-hexagonal](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.aws-hexagonal.2026-10-21`: all sixteen served headings read.
This is a vendor pattern
page, not a comparative study.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Layered Architecture; Clean / Onion Architecture; Anti-Corruption
Layer; Modular Monolith.

### Clean / Onion Architecture

See the [dedicated Clean / Onion Architecture card](clean-onion-architecture.md).

### Domain-Driven Design / Bounded Context

See the [dedicated Domain-Driven Design / Bounded Context card](bounded-context.md).

### Database per Service

See the [dedicated Database per Service card](database-per-service.md).

### Self-Contained Service

See the [dedicated Self-Contained Service card](self-contained-service.md).

### Sidecar

See the [dedicated Sidecar card](sidecar.md).

### Ambassador

See the [dedicated Ambassador card](ambassador.md).

### Anti-Corruption Layer

See the [dedicated Anti-Corruption Layer card](anti-corruption-layer.md).
## Chapter result and counterexample

Twelve cards establish a conditional decision route. Four have dedicated owners and
eight use bounded sections. The cards do not establish technical sufficiency, and a
matching name or a passing structural check is not evidence that a pattern fits a
workload.

Counterexample: a modular monolith with shared tables and no enforceable module contract
is not evidence for the card's good-fit conditions, even if it deploys as one unit.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Next: [V11/C02](../c02-api-communication/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 12 cards cite read ledger units; twelve owner links and backlinks are
  self-checked.
- Eight owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.
