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
summary: "Phase 3 cards for four entries; eight Phase 1 inventories."
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
    - "Four cards only; no technical sufficiency, complete family coverage or independent review."
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
  claim_ids: []
  status: "source-linked"
  notes: "Four cards cite exact read ledger units; eight entries remain Phase 1 inventories."
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

Four entries have a Phase 3 decision card below. Eight remain Phase 1 inventories.
A card is decision guidance, not a technical manuscript and not proof of fit.

## Pages and reasoning route

Page count is content-dependent. This chapter currently uses one landing page for all
entries; a later split is an editorial change, not a plan failure. Start with the card,
check its conditions and contraindications, then read the exact technical owner section
before choosing a mechanism.

## Entry inventory

Each level-three heading is a stable atlas anchor. Candidate areas and pages are
provisional unless a card names an exact technical owner. The four cards below are
self-checked; none claims sufficient coverage.

### Layered Architecture

**Catalog problem:** Separate responsibilities into layers with controlled dependency
direction.

**Candidate area:** V02/C01 (provisional; not audited). **Candidate page:** layered,
hexagonal and ports-and-adapters architecture (weak candidate).

**State:** inventory only; full card pending. Source reading is recorded in the
registry; no card claim is implied.

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

**Technical owner.** [Modular monolith architecture and internal domain events](../../v02-application-boundaries-and-contracts/c03-modular-monolith-and-internal-events/modular-monolith-and-internal-events.md#modular-monolith-architecture-and-internal-domain-events).

**Sources.** [src.monolith-first](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.monolith-first.2026-10-21`: Monolith First, sections "Monolith
First", "Microservices Guide", "Further Reading", "Notes". The source is architectural
guidance, not a benchmark.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Layered Architecture; Hexagonal Architecture; Microservices
Architecture; Domain-Driven Design / Bounded Context.

### Microservices Architecture

**Catalog problem:** Independently deploy bounded business capabilities with explicit
distributed costs.

**Candidate area:** V02/C04 (provisional; not audited). **Candidate page:** service
orientation, microservices and distributed boundaries (weak candidate).

**State:** inventory only; full card pending. Source reading is recorded in the
registry; no card claim is implied.

### Service-Oriented Architecture (SOA)

**Catalog problem:** Compose independently governed service contracts and integrations.

**Candidate area:** V02/C04 (provisional; not audited). **Candidate page:** no strong or
medium candidate yet; see the coverage map.

**State:** inventory only; full card pending. Source reading uses a bounded comparison,
not a dedicated owner audit.

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

**Technical owner.** [Layered, hexagonal and ports-and-adapters architecture](../../v02-application-boundaries-and-contracts/c01-layered-modular-and-ports-and-adapters-design/layered-hexagonal-ports-and-adapters.md#layered-hexagonal-and-ports-and-adapters-architecture).

**Sources.** [src.aws-hexagonal](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.aws-hexagonal.2026-10-21`: AWS Prescriptive Guidance, sections
"Hexagonal architecture pattern", "Intent", "Motivation", "Applicability", "Issues and
considerations", "Implementation", "High-level architecture". This is a vendor pattern
page, not a comparative study.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Layered Architecture; Clean / Onion Architecture; Anti-Corruption
Layer; Modular Monolith.

### Clean / Onion Architecture

**Catalog problem:** Direct dependencies inward toward domain policies.

**Candidate area:** V02/C01 (provisional; not audited). **Candidate page:** no strong or
medium candidate yet; see the coverage map.

**State:** inventory only; full card pending. No dedicated technical owner is asserted.

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

**Technical owner.** [Domain semantics and authoritative ownership](../../v02-application-boundaries-and-contracts/c02-domain-boundaries-data-ownership-and-contracts/domain-authority.md#domain-semantics-and-authoritative-ownership).

**Sources.** [src.fowler-bounded-context](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.fowler-bounded-context.2026-10-21`: Bounded Context, sections
"Bounded Context", "Further Reading", "Notes". The article is a definition and
boundary argument, not a full DDD reference.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Modular Monolith; Anti-Corruption Layer; Microservices
Architecture; Database per Service.

### Database per Service

**Catalog problem:** Give each service independent authoritative data ownership.

**Candidate area:** V02/C02 (provisional; not audited). **Candidate page:** no strong or
medium candidate yet; see the coverage map.

**State:** inventory only; full card pending. No dedicated technical owner is asserted.

### Self-Contained Service

**Catalog problem:** Reduce synchronous cross-service dependencies within a capability
boundary.

**Candidate area:** V02/C04 (provisional; not audited). **Candidate page:** no strong or
medium candidate yet; see the coverage map.

**State:** inventory only; full card pending. No dedicated technical owner is asserted.

### Sidecar

**Catalog problem:** Add auxiliary runtime behavior in a colocated process/container.

**Candidate area:** V08/C03 (provisional; not audited). **Candidate page:** no strong or
medium candidate yet; see the coverage map.

**State:** inventory only; full card pending. No dedicated technical owner is asserted.

### Ambassador

**Catalog problem:** Mediate client-side network capabilities through a local proxy.

**Candidate area:** V08/C03 (provisional; not audited). **Candidate page:** no strong or
medium candidate yet; see the coverage map.

**State:** inventory only; full card pending. No dedicated technical owner is asserted.

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

**Technical owner.** [Anti-corruption adapters: semantic translation and safe coexistence](../../v02-application-boundaries-and-contracts/c06-integration-adapters-and-anti-corruption-boundaries/anti-corruption-adapters-and-coexistence.md#anti-corruption-adapters-semantic-translation-and-safe-coexistence).

**Sources.** [src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.microsoft-acl.2026-10-21`: Anti-Corruption Layer pattern, sections
"Anti-Corruption Layer pattern", "Context and problem", "Solution", "Problems and
considerations", "When to use this pattern", "Workload design", "Example". This is a
vendor pattern page, not a comparative study.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Domain-Driven Design / Bounded Context; Hexagonal Architecture;
Strangler Fig; Adapter.

## Chapter result and counterexample

Four cards establish a conditional decision route; eight entries remain inventories.
The cards do not establish technical sufficiency, and a matching name or a passing
structural check is not evidence that a pattern fits a workload.

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

- Four cards cite read ledger units; four technical-owner links and backlinks are
  self-checked.
- Eight entries remain Phase 1 inventories and make no card claim.
- No entry claims `sufficient` technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.
