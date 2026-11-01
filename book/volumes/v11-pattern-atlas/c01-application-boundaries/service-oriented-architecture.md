---
metadata_version: 1
id: "tycho.page.1a22dabeec74779dfeb28fadc98ade4a"
kind: "page"
parent_id: "tycho.chapter.e996607f707421ca388796732547cafd"
canonical_path: >-
  book/volumes/v11-pattern-atlas/c01-application-boundaries/service-oriented-architecture.md
title: "Service-Oriented Architecture (SOA)"
topic_ids:
  - "application-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Service-Oriented Architecture (SOA); bounded owner evidence
  and explicit limits.
route_hints:
  questions:
    - >-
      Should independently governed services and contracts be composed across
      organizational boundaries, rather than designed as one application or one
      microservice estate?
  prerequisites:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  related_ids:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
    - "tycho.page.acb452608a8b42898aae7482c27f5f04"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "service-oriented architecture"
    - "application architecture and boundaries"
evidence_scope:
  source_ids:
    - "src.microservices"
    - "src.soa-model"
    - "src.microsoft-service-orientation"
    - "src.microsoft-dotnet-soa"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.microservices-article.2026-10-21,
    read.soa-rm.2026-11-01, read.microsoft-service-orientation.2026-11-01 and
    read.microsoft-dotnet-soa.2026-11-01; owner section and limits are bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-11-01"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-11-01"
updated_at: "2026-11-01"
source_inspection_date: "2026-11-01"
content_verified_at: null
---
# Service-Oriented Architecture (SOA)

**Identity.** Service-Oriented Architecture; alias SOA; family Application architecture
and boundaries; kind architecture-style; priority core.

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
mismatch are common. Microsoft reports that "large central brokers, central orchestrators
at the organization level, and the Enterprise Service Bus (ESB)" are typical SOA
features, and that "in most cases, these are anti-patterns in the microservice
community"; Fowler and Lewis note that ESB products "often include sophisticated
facilities for message routing, choreography, transformation, and applying business
rules." Tycho synthesis: size, observe and fail over a shared mediation path. Recovery
requires contract ownership and mediation observability; the linked owner section states
the remaining limits.

**Technical owner.** [Service-Oriented Architecture (SOA)](../../v02-application-boundaries-and-contracts/c04-soa-microservices-and-distributed-boundaries/service-orientation-microservices-and-distribution.md#service-oriented-architecture-soa) — The section explicitly owns SOA and microservice boundary choices.

**Sources.** [src.microservices](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-article.2026-10-21: Microservices, all twenty-four
headings read, including "Smart endpoints and dumb pipes" and "Many languages, many
options"; revision
`a29812554151c3ca90c22a81aef80ea271ae1ee80bf6ca90fb8d9d78281338f8`.
OASIS SOA Reference Model v1.0, §2.1, §3.3.1 and §3.3.2.2; representation revision
`69a28ce6d4337c11c4ecebd45219adefa1fd9915d07c476b2662440a7cbd2924`.
Microsoft service-oriented architectural style, "Service-Oriented Architectural Style";
raw HTML revision
`f84461f8c3b6c14a9e9404eff4bfcf8b4c58ff2a265f936f3e530c552a08f320`.
Microsoft .NET service-oriented architecture guidance; raw HTML revision
`f54a1ae99d25994eb2e48af4f0fe56bd49f00bb4894c0326c4bff8dd8966d7af`.
The OASIS model is technology-neutral and does not mandate a bus or a service
granularity.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Microservices Architecture; Modular Monolith; Anti-Corruption
Layer; Canonical Data Model.
