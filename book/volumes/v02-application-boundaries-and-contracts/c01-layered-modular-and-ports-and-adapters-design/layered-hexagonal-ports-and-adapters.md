---
metadata_version: 1
id: "tycho.page.77b512c4e2e946bd92d70b4a714600c8"
kind: "page"
parent_id: "tycho.chapter.c5f8456752f34dd6a5b6b5c7e3e14715"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c01-layered-modular-and-ports-and-adapters-design/layered-hexagonal-ports-and-adapters.md"
title: "Layered, hexagonal and ports-and-adapters architecture"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Layered, modular and ports-and-adapters design. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How are dependencies directed and replaceable?"
  prerequisites: []
  related_ids:
    - "tycho.page.c226850223614886b61b7cb36c7d5032"
    - "tycho.page.a06fd146f96b4b17a754f4d3b608ebdf"
    - "tycho.page.4681b3ba9e234c46bdb4b5993634b0e3"
    - "tycho.page.acb452608a8b42898aae7482c27f5f04"
    - "tycho.page.aa810dd152884b35a84f0f4cbe4369e9"
    - "tycho.page.8d28a6e14a1c49d6b67bf9cb5bfb242f"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.be90d29e1bc04524b2ea41ee9beaab0f"
    - "tycho.page.47ffb5c160bd4b10aff27101414c2133"
    - "tycho.page.f375bfcea48045d2a5d1f46014ca7758"
    - "tycho.page.65f9616c034643f9bf5f297037f027e4"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Layered"
    - "hexagonal"
    - "and"
    - "ports-and-adapters"
    - "architecture"
evidence_scope:
  source_ids:
    - "src.hexagonal"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.77b512c4e2e946bd92d70b4a714600c8:-1 -->

# Layered, hexagonal and ports-and-adapters architecture

> **Tycho book manuscript — V02/C01.** Prepared 2026-10-19 from independent public architecture
> references. All case studies, diagrams and proposed tests are original. This is not a
> representation of a deployed system; no module-boundary checker, integration fixture, production
> trace or editorial peer review was executed. The combined earlier [architecture-styles
> research](../../../application/architecture-styles-and-module-boundaries.md) remains available
> until source/claim reconciliation.
>
> The content_review field retains the decomposition-era draft state; no independent
> acceptance is asserted.

<!-- /tycho-question-source -->

> **Pattern atlas:** [Layered Architecture](../../v11-pattern-atlas/c01-application-boundaries/README.md#layered-architecture) — decision conditions and contraindications.
> [Clean / Onion Architecture](../../v11-pattern-atlas/c01-application-boundaries/README.md#clean--onion-architecture) — decision conditions and contraindications.

> **Pattern atlas:** [Hexagonal Architecture](../../v11-pattern-atlas/c01-application-boundaries/README.md#hexagonal-architecture--ports-and-adapters) — decision conditions and contraindications.
<!-- tycho-question-source:tycho.page.77b512c4e2e946bd92d70b4a714600c8:0 -->
## Purpose and decision question

Application structure determines which source changes can be made without rewriting unrelated business rules, whether storage or interface technologies can be replaced, and which dependencies must be present during a test. **Layering** groups responsibilities by abstraction and allowed call direction. **Hexagonal architecture (ports and adapters)** makes the application's interaction contracts explicit and keeps technological drivers and integrations outside the domain's core.

Neither style determines the number of processes or servers. The question is not “Which architecture sounds cleaner?” but **which change boundaries are supported by enforceable dependencies and correspond to real quality requirements**.

The original [Cockburn Hexagonal Architecture paper, 2005](https://alistair.cockburn.us/hexagonal-architecture) frames an application that can be driven by a user, script or test, without depending on one UI or database. This chapter explains that mechanism; separate chapters own [modular monolith and internal events](../c03-modular-monolith-and-internal-events/modular-monolith-and-internal-events.md), [domain authority](../c02-domain-boundaries-data-ownership-and-contracts/domain-boundaries-data-ownership-and-contracts.md), and [SOA/microservice deployment decisions](../c04-soa-microservices-and-distributed-boundaries/service-orientation-microservices-and-distribution.md).

**Layer mechanism.** Layering groups responsibilities by abstraction and restricts source
dependencies to an allowed direction. A layer may call only declared inward interfaces; the
rule is enforced by build/dependency tests, not by a diagram. The inner domain must not
depend on a UI, database or transport adapter.

**Failure and alternative.** Dependency bypass, cyclic imports and a layer that becomes a
pass-through are common; detect them in the build and fail the change. Hexagonal/clean
architecture or a modular monolith may be preferable when explicit ports or module ownership
add more value than layer count. Reverse the layering choice when the layers add indirection
without a real change boundary.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.77b512c4e2e946bd92d70b4a714600c8:10 -->
## Engineering walkthrough — The same adapter error in local and remote architectures

**Original synthetic equipment booking.** The application defines an `InventoryPort.reserve(unitId, interval, operationId)` capability. One JDBC adapter implements the port with a database transaction. An HTTP adapter might instead talk to a remote inventory service. Neither implementation changes the *domain invariant*: a confirmed reservation must have one authoritative result for its logical operation. The port is a **source dependency direction and semantic contract**, not automatically a network port.

| Boundary | Normal execution | Failure or incorrect assumption |
|---|---|---|
| Domain and use case | Validate authorized unit, interval and exclusive booking rule | Unit tests with a fake adapter prove domain decisions only under the fake's assumptions |
| JDBC adapter | Map domain types, commit under declared isolation and uniqueness constraints | SQL timeout after commit is not proof of no booking |
| Remote adapter | Serialize versioned operation ID, use deadlines and resolve uncertain effect | New RPC does not make the former transaction globally atomic |
| Composition root | Wire concrete adapters and compatible versions | Dependency-inversion in source alone does not prove deploy-time isolation |

When a unique constraint rejects a competing booking, the adapter must translate the database exception into an explicit domain conflict, not a generic retry. A fake repository test cannot demonstrate concurrent DB constraints, credential scope, real connection cancellation or remote transport semantics. Conversely, a full integration test cannot substitute for a clear domain invariant. **Proposed test (not run):** inject concurrent booking, lost database reply and unexpected remote response while asserting the same domain-visible classifications for both adapters. If the application will always have one simple persistence choice, avoid a hierarchy of adapters that adds indirection without needed substitution. Follow the existing Cockburn hexagonal architecture source for the boundary principle, not as evidence that this implementation works.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.77b512c4e2e946bd92d70b4a714600c8:11 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Shopify — Packwerk boundaries](../../../cases/shopify-packwerk-boundary-evolution.md)**. **Relevant mechanism or architectural contrast:** Automated dependency checking and gradually tightened boundaries can make modularity executable. **Not established by this report/playbook:** Reference checks alone do not establish business-domain cohesion, latency isolation or independent deployability.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Direct source dependencies through application contracts while keeping runtime failure boundaries explicit.

Replacing a local adapter with a remote call changes deadlines and ambiguous outcomes even if the port signature is unchanged.

The detailed pages separate the mechanisms that make this decision conditional:

- [Dependency direction and application ports](dependencies-ports.md) — What does a port isolate and which runtime failure boundary remains?
- [Adapter substitution and falsification](adapter-scenarios.md) — How do local and remote adapter replacements change the tests and operational obligations?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is not the main subject of
this page. They are synthetic design guidance, not measured evidence, and they do not create a new
source claim.

### Layered Architecture

Layering is a dependency rule: presentation may call application, application may call domain, and
domain calls neither. Put that rule in build checks, not only in a diagram.

The owner of each layer names its public surface and the test that catches a bypass. A layer that
only forwards calls, a cyclic import, or shared mutable data crossing the boundary is evidence that
the layer is not a real change boundary. Detect these in the build and fail the change.

Limits: layers are not deployment units, and a domain model already spread across layers is not
rescued by renaming folders. Choose hexagonal ports or a clear modular monolith when explicit substitution
or module ownership adds more value than layer count.

### Hexagonal Architecture and Ports and Adapters

Hexagonal architecture makes substitution a domain decision. A port names the capability the
application needs; an adapter maps a technology to it. For reservations, define
reserve(unitId, interval, operationId), then implement it with a local transaction or a remote call.

The domain owns the contract: a confirmed reservation has one authoritative result for the
operation, and a uniqueness conflict becomes an explicit domain conflict. Adapter-specific errors,
timeouts and retries stay at the edge; they do not become domain states.

Domain code must not depend on adapter or technology types; dependencies point inward. Keep the
boundary only where substitution or testing justifies it. A distributed split is a
separate decision: if the adapter calls another service, it must own remote failure, latency and
versioned contracts, not merely rename a network call a port. A layered or modular-monolith
structure can be simpler when one persistence choice is stable.

### Clean-Onion Architecture

Clean and onion styles place domain rules at the centre and let source dependencies point inward
only, with application services coordinating use cases and outer layers supplying technology
adapters. The dependency rule, not the number of drawn rings, is the mechanism. No domain module may
import a framework, transport or storage dependency, and an automated build check must enforce the
direction rather than a diagram.

Convenience imports erode the boundary until the domain must change for a technology reason; the
remedy is an enforceable dependency test and a deliberate adapter, not another layer name. Hexagonal
ports and adapters expresses the same inward rule with explicit application ports; prefer the
simpler layering when the port indirection adds no tested change benefit.

**Boundary data.** Domain entities stay inside the boundary; data crossing it is a DTO or
port contract with an owned mapper. The adapter validates transport input, the domain refuses
framework types, and mapping tests preserve meaning rather than only field names.

**Limits.** A static dependency check proves imports, not runtime coupling: reflection, a
service locator or generated wiring can still bind the domain to a framework. Clean/onion is
the wrong choice when mapping overhead dominates a small CRUD application or when ports have
no genuinely different implementations; prefer simpler layering then.
