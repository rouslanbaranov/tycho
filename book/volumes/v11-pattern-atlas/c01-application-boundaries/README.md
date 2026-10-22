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
    - "src.aws-hexagonal"
    - "src.fowler-bounded-context"
    - "src.microsoft-cloud-patterns"
    - "src.fowler-layering"
    - "src.microservices"
    - "src.clean-architecture"
    - "src.microservices-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "All 12 cards cite read units; eight use bounded owner sections and remain partial."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-21"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-21"
source_inspection_date: "2026-10-21"
content_verified_at: null
---
# V11/C01 — Application architecture and boundaries

**Owning question:** Which application patterns fit a bounded ownership model?

## Purpose and mission

This chapter is the atlas entry point for **Application architecture and boundaries**.
It owns the conditional decision route for 12 catalog entries, not the deep mechanism
explanations. Read the candidate technical owner before applying a mechanism claim.

All 12 entries have a Phase 3 decision card below. Four have a dedicated owner section;
eight use bounded sections that own part of the mechanism. A card is decision guidance,
not a technical manuscript and not proof of fit.

## Pages and reasoning route

Page count is content-dependent. This chapter currently uses one landing page for all
entries; a later split is an editorial change, not a plan failure. Start with the card,
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
sections "Presentation Domain Data Layering", "Further Reading", "Notes". This is a
definitional article, not a comparative study.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Hexagonal Architecture; Clean / Onion Architecture; Modular
Monolith; Microservices Architecture.

### Modular Monolith

**Identity.** Modular Monolith; alias Modular monolith; family Application architecture
and boundaries; kind architecture-style; priority core.

**Decision question.** Should a bounded capability remain one deployable with enforced
module boundaries, rather than split into independently deployed services?

**Good-fit conditions.** The capability has one accountable owner or a small group with
a shared release cadence; module contracts and data ownership can be enforced by build
or review checks; local transactions are valuable; independent runtime scaling or
failure isolation is not yet required.

**Hard contraindications.** Reject the claim when modules need independent deployment,
scaling or failure isolation; when no team can enforce boundary ownership; when a
regulatory or trust boundary requires separate runtime isolation; or when "modular"
is used to describe shared tables with no enforced contract.

**Competing alternative.** Microservices or a decomposed service boundary. Reverse the
choice when release cadence, independent scaling or blast-radius isolation becomes the
binding constraint, or when module boundaries cannot be enforced.

**Failure and recovery.** The common failure is a distributed monolith in disguise:
shared data, synchronous call chains and one deployment blast radius. Recovery starts
with explicit module ownership, contract tests and a rollback path; event durability
and transaction semantics must be verified in the technical owner.

**Technical owner.** [Modular Monolith](../../v02-application-boundaries-and-contracts/c03-modular-monolith-and-internal-events/modular-monolith-and-internal-events.md#modular-monolith).

**Sources.** [src.monolith-first](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.monolith-first.2026-10-21`: Monolith First, sections "Monolith
First", "Microservices Guide", "Further Reading", "Notes". The source is architectural
guidance, not a benchmark.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Layered Architecture; Hexagonal Architecture; Microservices
Architecture; Domain-Driven Design / Bounded Context.

### Microservices Architecture

**Identity.** Microservices Architecture; alias Microservices; family Application
architecture and boundaries; kind architecture-style; priority core.

**Decision question.** Should bounded business capabilities be independently deployable
services with explicit distributed costs, rather than one deployable with module
boundaries?

**Good-fit conditions.** Multiple teams need independent release cadence; capabilities
have separate scaling or failure isolation needs; automation, observability and
contract testing exist; data ownership can be separated; the organization accepts
network and consistency costs.

**Hard contraindications.** Reject the claim when there is one small team with a shared
release cadence, no operational platform, unavoidable cross-service transactions, or
shared authoritative data. A service count is not evidence of autonomy.

**Competing alternative.** Modular monolith with enforced modules. Reverse the choice
when distribution cost outweighs the autonomy benefit, or when boundaries cannot be
owned independently.

**Failure and recovery.** Partial failure, retry amplification, latency and data
consistency are normal; recovery requires timeouts, idempotency and observability.
The linked owner section states the remaining limits.

**Technical owner.** [Microservices Architecture](../../v02-application-boundaries-and-contracts/c04-soa-microservices-and-distributed-boundaries/service-orientation-microservices-and-distribution.md#microservices-architecture) — The section explicitly owns SOA and microservice boundary choices.

**Sources.** [src.microservices](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-article.2026-10-21: Microservices, sections
"Characteristics of a Microservice Architecture", "Microservices and SOA",
"Decentralized Data Management", "Design for failure", "Microservice Trade-Offs".
This is an architectural article, not a benchmark.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Service-Oriented Architecture; Modular Monolith; Database per
Service; Self-Contained Service.

### Service-Oriented Architecture (SOA)

**Identity.** Service-Oriented Architecture; alias SOA; family Application architecture
and boundaries; kind architecture-style; priority advanced.

**Decision question.** Should independently governed services and contracts be composed
across organizational boundaries, rather than designed as one application or one
microservice estate?

**Good-fit conditions.** Heterogeneous systems have separate governance; contracts and
mediation are explicit; integration spans ownership boundaries; service lifecycle and
versioning can be governed; the organization accepts integration overhead.

**Hard contraindications.** Reject the claim for one team and one deployable, when no
service governance exists, when SOA is used as a synonym for an enterprise bus, or when
contracts cannot be versioned and owned.

**Competing alternative.** Microservices for independent product capabilities, or a
modular monolith for one ownership boundary. Reverse the choice when governance and
mediation overhead exceeds the integration benefit.

**Failure and recovery.** Contract drift, a centralized bus bottleneck and semantic
mismatch are common. Recovery requires contract ownership and mediation observability;
the linked owner section states the remaining limits.

**Technical owner.** [Service-Oriented Architecture (SOA)](../../v02-application-boundaries-and-contracts/c04-soa-microservices-and-distributed-boundaries/service-orientation-microservices-and-distribution.md#service-oriented-architecture-soa) — The section explicitly owns SOA and microservice boundary choices.

**Sources.** [src.microservices](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-article.2026-10-21: Microservices, section
"Microservices and SOA" plus the surrounding trade-off discussion. This is a bounded
comparison, not an OASIS SOA reference.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Microservices Architecture; Modular Monolith; Anti-Corruption
Layer; Canonical Data Model.

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

**Technical owner.** [Hexagonal Architecture / Ports and Adapters](../../v02-application-boundaries-and-contracts/c01-layered-modular-and-ports-and-adapters-design/layered-hexagonal-ports-and-adapters.md#hexagonal-architecture-ports-and-adapters).

**Sources.** [src.aws-hexagonal](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.aws-hexagonal.2026-10-21`: AWS Prescriptive Guidance, sections
"Hexagonal architecture pattern", "Intent", "Motivation", "Applicability", "Issues and
considerations", "Implementation", "High-level architecture". This is a vendor pattern
page, not a comparative study.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Layered Architecture; Clean / Onion Architecture; Anti-Corruption
Layer; Modular Monolith.

### Clean / Onion Architecture

**Identity.** Clean / Onion Architecture; aliases Clean Architecture, Onion
Architecture; family Application architecture and boundaries; kind architecture-style;
priority advanced.

**Decision question.** Should dependencies point inward toward domain policies, with
frameworks and delivery mechanisms at the outside?

**Good-fit conditions.** Domain rules are the main asset; several delivery mechanisms or
frameworks are plausible; dependency direction can be enforced; tests need to isolate
policy from infrastructure.

**Hard contraindications.** Reject the claim for a CRUD surface with little domain
behavior, a framework-centric application, or a team that cannot maintain boundary
mapping. Drawing circles as team boundaries is not sufficient.

**Competing alternative.** Hexagonal ports and adapters or layered architecture. Reverse
the choice when the dependency rule stops protecting changes or mapping layers dominate.

**Failure and recovery.** Boundary erosion and DTO/mapping complexity are common.
Recovery requires dependency checks and explicit use-case boundaries; the technical
owner section states the remaining limits.

**Technical owner.** [Layered, hexagonal and ports-and-adapters architecture](../../v02-application-boundaries-and-contracts/c01-layered-modular-and-ports-and-adapters-design/layered-hexagonal-ports-and-adapters.md#clean-onion-architecture) — The section owns dependency direction and ports; Clean/Onion vocabulary is bounded to that mechanism.

**Sources.** [src.clean-architecture](../../../../edition/patterns/reading-ledger.v1.json)
read record read.clean-architecture.2026-10-21: The Clean Architecture, sections
"The Dependency Rule", "Entities", "Use Cases", "Interface Adapters", "Frameworks and
Drivers", "Crossing boundaries". This is an author article, not a comparative study.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Hexagonal Architecture; Layered Architecture; Modular Monolith;
Domain-Driven Design / Bounded Context.

### Domain-Driven Design / Bounded Context

**Identity.** Domain-Driven Design / Bounded Context; aliases DDD, Bounded Context;
family Application architecture and boundaries; kind modeling-discipline; priority core.

**Decision question.** Should models and ownership be separated by bounded context
rather than forced into one shared enterprise model?

**Good-fit conditions.** Several business meanings or languages coexist; ownership and
change cadence differ; translation between models can be owned; domain experts can
validate boundaries; context maps clarify integration rather than mandate a graph.

**Hard contraindications.** Reject the claim when one stable model has a single
accountable owner; when no domain expertise is available to validate meaning; when DDD
is used as a synonym for microservices; or when the proposed boundary cannot be enforced
in code, data or team ownership.

**Competing alternative.** One shared model or a modular monolith with explicit module
contracts. Reverse the choice when translation cost exceeds the value of model
separation, or when one owner can govern the shared model.

**Failure and recovery.** Common failures are conflating authority with storage,
turning a context map into a mandatory graph, and drawing boundaries around teams
rather than business meaning. Recovery starts by revisiting model behavior, ownership
and translation cost in the technical owner.

**Technical owner.** [Domain-Driven Design / Bounded Context](../../v02-application-boundaries-and-contracts/c02-domain-boundaries-data-ownership-and-contracts/domain-authority.md#domain-driven-design-bounded-context).

**Sources.**
[src.fowler-bounded-context](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.fowler-bounded-context.2026-10-21`: Bounded Context, sections
"Bounded Context", "Further Reading", "Notes". The article is a definition and
boundary argument, not a full DDD reference.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Modular Monolith; Anti-Corruption Layer; Microservices
Architecture; Database per Service.

### Database per Service

**Identity.** Database per Service; family Application architecture and boundaries; kind
data-ownership-pattern; priority core.

**Decision question.** Should each service own its authoritative data and expose only a
contract, rather than share one database across services?

**Good-fit conditions.** Service ownership is real; schemas must evolve independently;
failure isolation matters; duplication and eventual consistency are acceptable; each
service can own its queries and migrations.

**Hard contraindications.** Reject the claim when strong cross-service transactions are
unavoidable, when reporting requires one shared schema, when one team owns all services,
or when "database per service" is implemented as one server with shared tables.

**Competing alternative.** Shared database with a modular monolith, or a deliberately
governed shared read model. Reverse the choice when cross-service consistency and
reporting cost exceed the autonomy benefit.

**Failure and recovery.** Dual writes, stale replicas and cross-service queries are
common. Recovery requires outbox/idempotency and explicit data contracts; the technical
owner section states the remaining limits.

**Technical owner.** [Ownership, isolation and boundary validation](../../v02-application-boundaries-and-contracts/c02-domain-boundaries-data-ownership-and-contracts/ownership-isolation.md#database-per-service) — The section owns state authority and shared-database selection, not a dedicated schema-per-service recipe.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-database-per-service.2026-10-21: Database per
Service, sections "Context", "Problem", "Forces", "Solution", "Example", "Resulting
context", "Related patterns". This is a pattern page, not a comparative study.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Microservices Architecture; Domain-Driven Design / Bounded Context;
Transactional Outbox; CQRS.

### Self-Contained Service

**Identity.** Self-Contained Service; family Application architecture and boundaries;
kind service-decomposition-pattern; priority advanced.

**Decision question.** Should a service reduce synchronous dependencies by owning or
duplicating the data and behavior it needs, rather than calling other services on every
request?

**Good-fit conditions.** Latency and availability coupling are material; the capability
can own a local read model; duplication and reconciliation are acceptable; the service
boundary is stable enough to absorb change.

**Hard contraindications.** Reject the claim when strong consistency is mandatory, when
data cannot be duplicated for legal or ownership reasons, or when the "self-contained"
service still hides synchronous calls behind a local cache.

**Competing alternative.** API composition or orchestration with explicit latency
budgets. Reverse the choice when duplication and invalidation cost exceed the coupling
benefit.

**Failure and recovery.** Stale local data, hidden coupling and complex invalidation are
common. Recovery requires reconciliation and clear ownership; the bounded owner section
describes hidden shared state and orchestration/BFF alternatives.

**Technical owner.** [Independent deployment and its costs](../../v02-application-boundaries-and-contracts/c04-soa-microservices-and-distributed-boundaries/service-independence.md#self-contained-service) — The section owns remote-boundary costs and local-transaction alternatives.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-self-contained.2026-10-21: Self-contained service,
sections "Context", "Problem", "Forces", "Solution", "Example", "Resulting Context",
"Related patterns". This is a pattern page, not a comparative study.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Microservices Architecture; API Composition; Database per Service;
CQRS.

### Sidecar

**Identity.** Sidecar; family Application architecture and boundaries; kind
deployment-pattern; priority core.

**Decision question.** Should auxiliary runtime behavior run in a colocated
process/container beside the main workload, rather than inside it or in a separate
remote service?

**Good-fit conditions.** Cross-cutting behavior is reusable across heterogeneous
runtimes; the platform can schedule and manage sidecars; independent lifecycle and
failure isolation are useful; resource overhead is acceptable.

**Hard contraindications.** Reject the claim for a simple application without a
sidecar-capable platform, when startup ordering and resource limits cannot be managed,
or when the sidecar becomes a hidden monolith with tightly coupled lifecycle.

**Competing alternative.** An in-process library, an ambassador proxy or a node agent.
Reverse the choice when sidecar overhead and operational complexity exceed reuse.

**Failure and recovery.** Resource contention, startup ordering and version skew are
common. Recovery requires health checks and explicit lifecycle ownership; the technical
owner section states the remaining limits.

**Technical owner.** [Service mesh and traffic intermediaries](../../v08-delivery-deployment-and-recovery/c03-vms-containers-orchestration-and-serverless/static-stability.md#sidecar) — The section owns proxies and sidecar data planes, not a dedicated sidecar lifecycle page.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-sidecar.2026-10-21: Sidecar pattern, sections "Context
and problem", "Solution", "Problems and considerations", "When to use this pattern",
"Workload design", "Example". This is a vendor pattern page, not a comparative study.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Ambassador; Service Mesh; Modular Monolith; Deployment Stamps.

### Ambassador

**Identity.** Ambassador; family Application architecture and boundaries; kind
deployment-pattern; priority advanced.

**Decision question.** Should a local proxy mediate a client's network capabilities,
rather than embedding connectivity logic in the client or centralizing it remotely?

**Good-fit conditions.** A legacy client cannot be changed easily; connectivity behavior
such as retries, TLS or routing is shared; the proxy lifecycle can be owned; an extra
network hop is acceptable.

**Hard contraindications.** Reject the claim when the client can use a library, when no
operational owner exists for the proxy, when latency or resource constraints forbid an
extra hop, or when the proxy becomes a single point of failure.

**Competing alternative.** A sidecar, service mesh or in-process client library. Reverse
the choice when the proxy adds a hop without providing a needed capability.

**Failure and recovery.** Proxy outage, configuration drift and retry amplification are
common. Recovery requires health checks and bounded retries; the bounded owner section
covers traffic intermediaries, not a dedicated ambassador lifecycle page.

**Technical owner.** [Service mesh and traffic intermediaries](../../v08-delivery-deployment-and-recovery/c03-vms-containers-orchestration-and-serverless/static-stability.md#ambassador) — The section owns traffic intermediaries, not a dedicated ambassador lifecycle page.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-ambassador.2026-10-21: Ambassador pattern, sections
"Context and problem", "Solution", "Problems and considerations", "When to use this
pattern", "Workload design", "Example". This is a vendor pattern page, not a comparative
study.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Sidecar; Service Mesh; Gateway Routing; Anti-Corruption Layer.

### Anti-Corruption Layer

**Identity.** Anti-Corruption Layer; alias ACL, translation layer; family Application
architecture and boundaries; kind integration-pattern; priority core.

**Decision question.** Should a translation layer protect the domain model from a
legacy or external model with different semantics?

**Good-fit conditions.** The external model has different meanings or invariants; the
domain must remain independent of vendor or legacy types; coexistence is transitional;
the mapping and its errors can be owned and tested.

**Hard contraindications.** Reject the claim when the models already align; when the
layer adds no semantic translation; when latency or data duplication violates a hard
constraint; when the mapping has no owner; or when the ACL would become a second domain
model.

**Competing alternative.** Direct integration against a shared contract. Reverse the
choice when the external model stabilizes and aligns semantically, or when the ACL
becomes a permanent duplicate domain.

**Failure and recovery.** Lossy translation, dual writes and stale mappings are the
main failure modes. Recovery requires contract tests, versioned mappings and an
explicit cutover path; verify those mechanics in the technical owner.

**Technical owner.** [Anti-Corruption Layer](../../v02-application-boundaries-and-contracts/c06-integration-adapters-and-anti-corruption-boundaries/anti-corruption-adapters-and-coexistence.md#anti-corruption-layer).

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.microsoft-acl.2026-10-21`: Anti-Corruption Layer pattern, sections
"Anti-Corruption Layer pattern", "Context and problem", "Solution", "Problems and
considerations", "When to use this pattern", "Workload design", "Example". This is a
vendor pattern page, not a comparative study.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Domain-Driven Design / Bounded Context; Hexagonal Architecture;
Strangler Fig; Adapter.

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
