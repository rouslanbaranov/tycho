---
metadata_version: 1
id: "tycho.page.c6b05f1a6f65430f97a3e219732ff713"
kind: "page"
parent_id: "tycho.chapter.e996607f707421ca388796732547cafd"
canonical_path: "book/volumes/v11-pattern-atlas/c01-application-boundaries/modular-monolith.md"
title: "Modular Monolith"
topic_ids:
  - "application-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Modular Monolith; bounded owner evidence and explicit
  limits.
route_hints:
  questions:
    - >-
      Should a bounded capability remain one deployable with enforced module
      boundaries, rather than split into independently deployed services?
  prerequisites:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  related_ids:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "modular monolith"
    - "module boundaries"
evidence_scope:
  source_ids:
    - "src.monolith-first"
    - "src.spring-modulith"
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
# Modular Monolith

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
shared data, synchronous call chains and one deployment blast radius. Spring Modulith
1.3.12 documents synchronous event publication and warns that more triggered
functionality "will widen the transaction boundary". Its module verification rejects
references to internal packages and undeclared dependencies; its event page also warns
that an asynchronous listener can lose the event without a safety net. Recovery starts
with explicit module ownership, contract tests and a rollback path; event durability
and transaction semantics must be verified in the technical owner. The deployment
blast radius and the "distributed monolith" label remain Tycho analysis; the sources
do not measure them.

**Technical owner.** [Modular Monolith](../../v02-application-boundaries-and-contracts/c03-modular-monolith-and-internal-events/modular-monolith-and-internal-events.md#modular-monolith).

**Sources.** [src.monolith-first](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.monolith-first.2026-10-21`: all five served headings read.
Spring Modulith 1.3.12 "Verifying Application Module Structure", "Fundamentals" and
"Working with Application Events", source `src.spring-modulith`, accessed 2026-10-30;
exact quotes, sections and canonical revisions are in the owner section. The sources
are documentation and architectural guidance, not a benchmark.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Layered Architecture; Hexagonal Architecture; Microservices
Architecture; Domain-Driven Design / Bounded Context.
