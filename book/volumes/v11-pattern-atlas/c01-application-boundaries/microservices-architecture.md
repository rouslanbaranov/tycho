---
metadata_version: 1
id: "tycho.page.08126ef1f30ceedd226d38928887b5b4"
kind: "page"
parent_id: "tycho.chapter.e996607f707421ca388796732547cafd"
canonical_path: >-
  book/volumes/v11-pattern-atlas/c01-application-boundaries/microservices-architecture.md
title: "Microservices Architecture"
topic_ids:
  - "application-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Microservices Architecture; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should bounded business capabilities be independently deployable services
      with explicit distributed costs, rather than one deployable with module
      boundaries?"
  prerequisites:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  related_ids:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
    - "tycho.page.acb452608a8b42898aae7482c27f5f04"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "microservices architecture"
evidence_scope:
  source_ids:
    - "src.microservices"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; source binding remains in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-29"
content_verified_at: null
---

# Microservices Architecture

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

**Failure and recovery.** Because services can fail at any time, applications must
be designed to tolerate a service failure and respond as gracefully as possible;
recovery depends on detecting failures quickly and, if possible, restoring service
automatically. The cited article's "Design for failure" section binds that claim.
Timeouts, retry identity, observability signals and recovery-time bounds remain
Tycho guidance. The linked owner section states the remaining limits.

**Technical owner.** [Microservices Architecture](../../v02-application-boundaries-and-contracts/c04-soa-microservices-and-distributed-boundaries/service-orientation-microservices-and-distribution.md#microservices-architecture) — The section explicitly owns SOA and microservice boundary choices.

**Sources.** [src.microservices](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-article.2026-10-21: Microservices, all twenty-four
headings read, including the SOA sidebar and the trade-offs card. The failure and
recovery claim binds "Design for failure" at revision
`a29812554151c3ca90c22a81aef80ea271ae1ee80bf6ca90fb8d9d78281338f8`.
This is an architectural article, not a benchmark.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Service-Oriented Architecture; Modular Monolith; Database per
Service; Self-Contained Service.
