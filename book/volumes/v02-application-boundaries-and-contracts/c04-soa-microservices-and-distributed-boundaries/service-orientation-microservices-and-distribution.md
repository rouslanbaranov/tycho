---
metadata_version: 1
id: "tycho.page.acb452608a8b42898aae7482c27f5f04"
kind: "page"
parent_id: "tycho.chapter.a7cb3581936b46ab9fd3a49c17e9cc6c"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c04-soa-microservices-and-distributed-boundaries/service-orientation-microservices-and-distribution.md"
title: "Service orientation, microservices and distributed boundaries"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Integrated decision and bounded source limits for SOA, microservices and distributed boundaries. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "When is independent deployment justified by measured coordination cost?"
  prerequisites: []
  related_ids:
    - "tycho.page.c226850223614886b61b7cb36c7d5032"
    - "tycho.page.77b512c4e2e946bd92d70b4a714600c8"
    - "tycho.page.4681b3ba9e234c46bdb4b5993634b0e3"
    - "tycho.page.a06fd146f96b4b17a754f4d3b608ebdf"
    - "tycho.page.8d28a6e14a1c49d6b67bf9cb5bfb242f"
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.be90d29e1bc04524b2ea41ee9beaab0f"
    - "tycho.page.47ffb5c160bd4b10aff27101414c2133"
    - "tycho.page.cf0ce38c73e44950aec5a9c2869bee63"
    - "tycho.page.4e0e4db7547b45469f36915886473750"
    - "tycho.page.cdb86c0b91a6489f979689ab08efad35"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Service"
    - "orientation"
    - "microservices"
    - "and"
    - "distributed"
    - "boundaries"
evidence_scope:
  source_ids:
    - "src.soa-model"
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
<!-- tycho-question-source:tycho.page.acb452608a8b42898aae7482c27f5f04:-1 -->

# Service orientation, microservices and distributed boundaries

> **Canonical integrated decision page — V02/C04**, 2026-10-19. Source boundary: public OASIS SOA Reference Model v1.0 and Fowler/Lewis' 2014 microservices discussion. Examples and tests are original fictional material. No service topology was deployed, team structure observed or empirical architecture comparison performed. The content_review field retains the decomposition-era draft state; no independent acceptance is asserted.

<!-- /tycho-question-source -->

> **Pattern atlas:** [Microservices Architecture](../../v11-pattern-atlas/c01-application-boundaries/README.md#microservices-architecture) — decision conditions and contraindications.
> [Service-Oriented Architecture](../../v11-pattern-atlas/c01-application-boundaries/README.md#service-oriented-architecture-soa) — decision conditions and contraindications.
<!-- tycho-question-source:tycho.page.acb452608a8b42898aae7482c27f5f04:0 -->
## Purpose and mission

A service is a published capability with an interaction contract; a microservice architecture is a particular set of design and operational choices around smaller independently deployable capabilities. **SOA and microservices are not simply opposite network protocols**, and neither should be selected solely because a codebase has many modules.

The primary architecture question is: **which capabilities need independent deployment, failure containment, state ownership and life cycles strongly enough to justify the remote communication and coordination costs?**

The [OASIS SOA Reference Model v1.0](https://docs.oasis-open.org/soa-rm/v1.0/soa-rm.html) defines visibility, interaction and effect as core service ideas; it does not prescribe a mandatory message bus, SOAP transport or service deployment granularity. [Fowler and Lewis, *Microservices* (2014)](https://www.martinfowler.com/articles/microservices.html) describe independently deployable services organized around business capabilities, as a characterized style rather than a universal threshold for how small a service must be.

**SOA and microservice mechanisms.** SOA emphasizes published capabilities, explicit
contracts and governed interaction across independent owners. Microservices emphasize
independently deployable capabilities with their own data and lifecycle. Both must name
visibility, contract, authority and failure behavior rather than assuming a bus, protocol or
container count supplies them.

**Invariant and failure.** Each capability needs a single authoritative owner for its data
and invariant, and independent deployment must be real rather than a container label.
Shared databases, synchronized releases and chatty remote calls can recreate a distributed
monolith; retries, version skew and partial failure are common. Detect shared authority and
release coupling, then consolidate or split the boundary deliberately. A modular monolith
or layered application may be preferable when independent deployment and failure containment
are not measured requirements.

<!-- /tycho-question-source -->

## Bounded pattern ownership notes

### Microservices Architecture

Microservices emphasize independently deployable capabilities with their own data and lifecycle.
The unit of independence is the deployable service plus its data ownership, not the number of
repositories.

Each capability needs a single authoritative owner for its data and invariant, and independent
deployment must be real rather than a container label. Shared databases, synchronized releases and
chatty remote calls can recreate a distributed monolith; retries, version skew and partial failure
are common. Define the contract, the failure budget and the local transaction boundary before
splitting the deployment.

A modular monolith or layered application may be preferable when independent deployment and failure
containment are not measured requirements. Microservices are a fit when separate ownership,
independent release cadence and failure isolation justify the remote-call and data-consistency cost.

### Service-Oriented Architecture (SOA)

SOA emphasizes published capabilities, explicit contracts and governed interaction across
independent owners. The governance model and contract lifecycle are the mechanism; a service bus or
registry alone does not create ownership.

Each capability needs a single authoritative owner for its data and invariant, and independent
deployment must be real rather than a container label. Shared databases, synchronized releases and
chatty remote calls can recreate a distributed monolith; retries, version skew and partial failure
are common. A published contract needs a version, a consumer inventory and a deprecation path.

A modular monolith or layered application may be preferable when independent deployment and failure
containment are not measured requirements. SOA is a fit when many owners must integrate through
stable contracts and the governance cost buys real autonomy.

## Integrated decision and reading route

Justify a remote boundary through independent ownership or deployment needs while accounting for communication and recovery costs.

Separate containers can still require synchronized releases and share one fragile datastore; deployment count does not demonstrate independence.

The detailed pages separate the mechanisms that make this decision conditional:

- [Independent deployment and its costs](service-independence.md) — Which coordination costs justify introducing a remote boundary?
- [Service contracts and failure evaluation](service-contracts.md) — What must be tested when a capability moves into another process?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
