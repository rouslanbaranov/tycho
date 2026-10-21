---
metadata_version: 1
id: "tycho.volume.7e8f5fd0c9d94504b6dc74b9ae6c30f3"
kind: "volume"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/README.md"
title: "V02 — Application boundaries and interaction contracts"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Map ownership and interface semantics before splitting deployment: modular monolith, services and adapters are conditional alternatives; tenancy crosses every boundary."
route_hints:
  questions:
    - "Map ownership and interface semantics before splitting deployment: modular monolith, services and adapters are conditional alternatives; tenancy crosses every boundary."
  prerequisites:
    - "tycho.chapter.9d4f989ec9304e418f60f1ad7248094a"
    - "tycho.chapter.3d34f0b431814c9fa879a355029af2a9"
    - "tycho.chapter.bbfd14751d274868b152ba431dc904c9"
  related_ids:
    - "tycho.chapter.c5f8456752f34dd6a5b6b5c7e3e14715"
    - "tycho.chapter.7031445877fb4f8d831d962d170521c8"
    - "tycho.chapter.5de52a840c14448c946a65c924f28487"
    - "tycho.chapter.a7cb3581936b46ab9fd3a49c17e9cc6c"
    - "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
    - "tycho.chapter.4f7542e57fb74052a4a31cd4c4dce46a"
    - "tycho.chapter.5426707ddf264b758016aafe71f342b7"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.hexagonal"
    - "src.http-semantics"
    - "src.soa-model"
  claim_ids: []
  status: "source-linked"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# V02 — Application boundaries and interaction contracts

## Purpose and mission

Decide responsibilities and system boundaries before distributing them.

The outcome of this volume is: Map ownership and interface semantics before splitting deployment: modular monolith, services and adapters are conditional alternatives; tenancy crosses every boundary.

## A worked cross-chapter synthesis

A fictional workshop keeps booking and catalogue behavior in one deployable. Different owners need different release cadences, but bookings still require an authoritative availability check. Splitting processes changes the failure and compatibility contracts; it does not, by itself, decide who owns availability.

Draw module dependencies and domain state ownership first. Compare an enforced modular design with remote services using the same outcome and operating constraints. Specify the port or API's deadline, authorization, version and unknown-result behavior. An adapter must preserve meaning, including explicit rejection of values that cannot be translated.

## Questions and chapters

| Chapter | Owning question |
|---|---|
| [V02/C01 — Layered, modular and ports-and-adapters design](c01-layered-modular-and-ports-and-adapters-design/README.md) | How are dependencies directed and replaceable? |
| [V02/C02 — Domain boundaries, data ownership and contracts](c02-domain-boundaries-data-ownership-and-contracts/README.md) | When should business capabilities form module or service boundaries? |
| [V02/C03 — Modular monolith and internal events](c03-modular-monolith-and-internal-events/README.md) | Which coupling and deployment constraints fit an in-process architecture? |
| [V02/C04 — SOA, microservices and distributed boundaries](c04-soa-microservices-and-distributed-boundaries/README.md) | When is independent deployment justified by measured coordination cost? |
| [V02/C05 — Public APIs, HTTP/RPC and compatibility](c05-public-apis-http-rpc-and-compatibility/README.md) | How do deadlines, versioning, retries and API contracts evolve? |
| [V02/C06 — Integration adapters and anti-corruption boundaries](c06-integration-adapters-and-anti-corruption-boundaries/README.md) | How can incompatible domains and legacy contracts coexist? |
| [V02/C07 — Authorization boundaries and multitenancy](c07-authorization-boundaries-and-multitenancy/README.md) | What must be isolated between clients, organizations and data owners? |

## Choosing a reading route

For a first reading, follow the chapter order. For diagnosis, connect the observed outcome to its authority and failure boundary using: [V02/C02](c02-domain-boundaries-data-ownership-and-contracts/README.md), [V02/C03](c03-modular-monolith-and-internal-events/README.md), [V02/C04](c04-soa-microservices-and-distributed-boundaries/README.md), [V02/C05](c05-public-apis-http-rpc-and-compatibility/README.md), [V02/C07](c07-authorization-boundaries-and-multitenancy/README.md). Return to the exact page-local source ledger before making a version-specific claim.

Prerequisite context: V01/C01, C03, C06.

Read [V01/C01](../v01-requirements-and-architecture/c01-problem-framing/README.md), [V01/C03](../v01-requirements-and-architecture/c03-quality-attributes-and-trade-offs/README.md), [V01/C06](../v01-requirements-and-architecture/c06-capacity-operational-constraints-and-total-cost/README.md) for the named entry assumptions.

### Reasoning boundaries

This original conceptual map separates competing inputs rather than promising a universal solution.

~~~mermaid
flowchart TD
    Q["V02/C02 — Domain boundaries, data ownership and contracts"] --> M["V02/C03 — Modular monolith and internal events"]
    Q --> E["Evidence and unknown inputs"]
    M --> D{"Meets the declared constraints?"}
    E --> D
    D -->|Supported| R["V02/C07 — Authorization boundaries and multitenancy"]
    D -->|Unresolved| U["Measure, revise or retain the baseline"]
~~~

Text alternative: establish domain boundaries, data ownership and contracts, compare modular monolith and internal events with the available evidence, and either carry a supported result forward or return to unresolved inputs. The figure describes a reasoning route, not observed runtime behavior.

## Counterexample and handoff

An internal event may be convenient coordination without being durable delivery. A tenant identifier may help routing without authorizing an object. Carry those distinctions into execution and distributed semantics: moving code across a network creates recovery obligations that source-level dependency inversion alone cannot discharge.

## Navigation and source boundaries

| Route | Destination |
|---|---|
| Parent | [Book contents](../../README.md) |
| Previous volume | [V01](../v01-requirements-and-architecture/README.md) |
| Next volume | [V03](../v03-execution-concurrency-and-flow-control/README.md) |
| Historical applications | [Casebook and synthetic playbooks](../../cases/README.md) |

## Evidence and known limits

The scenario is original synthetic reasoning. The chapters contain the accepted manuscript and its published evidence; no synthetic number or historical result is a measured prediction for another system. This new synthesis is editorially self-checked, not independently certified. Source-access restrictions, unexecuted technology experiments and original case denominators remain explicit in their owning pages. Product-specific adoption still requires compatible versions and the target workload.
