---
metadata_version: 1
id: tycho.page.869312869a4188515a74a6d189b6d316
kind: page
parent_id: tycho.chapter.e996607f707421ca388796732547cafd
canonical_path: book/volumes/v11-pattern-atlas/c01-application-boundaries/layered-architecture.md
title: Layered Architecture
topic_ids:
- application-architecture-and-boundaries
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Layered Architecture.
route_hints:
  questions:
  - Should responsibilities be grouped into layers with an enforced dependency direction,
    rather than organized around ports or independently deployed services?
  prerequisites:
  - tycho.chapter.e996607f707421ca388796732547cafd
  related_ids:
  - tycho.chapter.e996607f707421ca388796732547cafd
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - layered architecture
evidence_scope:
  source_ids:
  - src.fowler-layering
  - src.fowler-anemic-domain-model
  claim_ids: []
  status: source-linked
  notes: Source-level bindings remain in the owner unit.
content_review:
  status: self-checked
  reviewed_at: '2026-11-02'
  reviewer: Automated authoring agent
  proof_uri: null
authored_at: '2026-11-01'
updated_at: '2026-11-02'
source_inspection_date: '2026-11-02'
content_verified_at: null
---

# Layered Architecture

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
anemic domain models are the failure modes. Recovery starts with dependency checks,
explicit contracts and a review of the change boundary; the linked owner section
states the remaining limits.

**Technical owner.**
 [Layered
Architecture](../../v02-application-boundaries-and-contracts/c01-layered-modular-and-ports-and-adapters-design/layered-hexagonal-ports-and-adapters.md#layered-architecture)
— The section owns layering and dependency direction; it is not a dedicated layering manuscript.

**Sources.** [src.fowler-layering](../../../../edition/patterns/reading-ledger.v1.json)
read record read.fowler-layering.2026-10-21: Presentation Domain Data Layering, sections
"Presentation Domain Data Layering", "Further Reading", "Acknowledgements", "Notes". This
is a definitional article, not a comparative study. The anemic-domain failure also cites
read.fowler-anemic.2026-11-02, sections "Anemic Domain Model", "Transaction".

**Decision state.** `applicable-under-conditions`.

**Related entries.** Hexagonal Architecture; Clean / Onion Architecture; Modular
Monolith; Microservices Architecture.
