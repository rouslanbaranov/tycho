---
metadata_version: 1
id: "tycho.page.a6cac42ca5b94af1acdfebbda52de94a"
kind: "page"
parent_id: "tycho.chapter.e996607f707421ca388796732547cafd"
canonical_path: "book/volumes/v11-pattern-atlas/c01-application-boundaries/database-per-service.md"
title: "Database per Service"
topic_ids:
  - "application-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Database per Service; bounded owner evidence and explicit
  limits.
route_hints:
  questions:
    - >-
      Should each service own its authoritative data and expose only a
      contract, rather than share one database across services?
  prerequisites:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  related_ids:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "database per service"
    - "data ownership"
evidence_scope:
  source_ids:
    - "src.microservices-patterns"
    - "src.monolith-first"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-30"
updated_at: "2026-10-30"
source_inspection_date: "2026-10-30"
content_verified_at: null
---
# Database per Service

**Identity.** Database per Service; family Application architecture and boundaries; kind
pattern; priority core.

**Decision question.** Should each service own its authoritative data and expose only a
contract, rather than share one database across services?

**Good-fit conditions.** Service ownership is real; schemas must evolve independently;
failure isolation matters; duplication and eventual consistency are acceptable; each
service can own its queries and migrations.

**Hard contraindications.** Reject the claim when strong cross-service transactions are
unavoidable, when reporting requires one shared schema, when one team owns all services
with a shared release cadence and a shared database is cheaper, or when "database per
service" is implemented as one server with shared tables.

**Competing alternative.** A shared database with enforced module ownership is simpler when
one team releases the modules together. The Shared database page lists "A single database is
simpler to operate" and familiar ACID transactions as benefits, but warns of "Development time
coupling" and "Runtime coupling"; the Database per Service page calls it "The Shared Database
anti-pattern". The enforced-ownership condition is Tycho synthesis, not the page's free
cross-service access. Reverse the choice when cross-service consistency, independent scaling or
reporting cost exceed the autonomy benefit.

**Failure and recovery.** Database per Service's "Resulting context" names cross-service
transactions and joins as the hard cases and routes them to Saga, API Composition and CQRS.
The Transactional outbox page states the atomic update-and-send requirement directly: a
command "must atomically update the database and send messages in order to avoid data
inconsistencies and bugs", yet a message sent after commit can be lost if the service crashes. Its
outbox stores the message with the local transaction and a relay publishes it; because the relay
"might publish a message more than once", "a message consumer must be idempotent". The Saga
page adds compensating transactions for failed steps. Replica lag is not established by these
pages; "verify replica freshness before joining" and the "reconciliation" repair loop are Tycho
guidance. The technical owner section states the exact quotes, sections and revisions.

**Technical owner.** [Ownership, isolation and boundary validation](../../v02-application-boundaries-and-contracts/c02-domain-boundaries-data-ownership-and-contracts/ownership-isolation.md#database-per-service) — The section owns state authority and shared-database selection, not a dedicated schema-per-service recipe.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.microservices-database-per-service.2026-10-21`, with the Saga and
Transactional Outbox pages read 2026-10-21 and the Shared database page read 2026-10-30.
[src.monolith-first](../../../../edition/patterns/reading-ledger.v1.json)
record `read.monolith-first.2026-10-21` supplies the team-simplicity and modularity
context. Exact quotes, sections and revisions are in the technical owner section.
These are pattern pages and one article, not comparative studies or benchmarks.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Microservices Architecture; Domain-Driven Design / Bounded Context;
Transactional Outbox; CQRS.
