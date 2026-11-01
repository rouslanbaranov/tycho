---
metadata_version: 1
id: "tycho.page.df51f8d69e7e4fa6beb678a5256a4f61"
kind: "page"
parent_id: "tycho.chapter.e996607f707421ca388796732547cafd"
canonical_path: "book/volumes/v11-pattern-atlas/c01-application-boundaries/bounded-context.md"
title: "Domain-Driven Design / Bounded Context"
topic_ids:
  - "application-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Domain-Driven Design / Bounded Context; bounded owner
  evidence and explicit limits.
route_hints:
  questions:
    - >-
      Should models and ownership be separated by bounded context rather than
      forced into one shared enterprise model?
  prerequisites:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  related_ids:
    - "tycho.chapter.e996607f707421ca388796732547cafd"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "bounded context"
    - "domain-driven design"
evidence_scope:
  source_ids:
    - "src.fowler-bounded-context"
    - "src.microsoft-ddd"
    - "src.ddd-reference"
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
# Domain-Driven Design / Bounded Context

**Identity.** Domain-Driven Design / Bounded Context; aliases DDD, Bounded Context;
family Application architecture and boundaries; kind architecture-style; priority core.

**Decision question.** Should models and ownership be separated by bounded context
rather than forced into one shared enterprise model?

**Good-fit conditions.** Several business meanings or languages coexist; ownership
and change cadence differ; domain experts co-create the vocabulary and can challenge
terms that hide different meanings; translation between models can be owned; context
maps clarify integration rather than mandate a graph.

**Hard contraindications.** Reject the claim when one stable model has a single
accountable owner; when no domain expertise is available to validate meaning; when DDD
is used as a synonym for microservices; or when the proposed boundary cannot be enforced
in code, data or team ownership.

**Competing alternative.** One shared model or a modular monolith with explicit module
contracts. Reverse the choice when translation cost exceeds the value of model
separation, or when one owner can govern the shared model.

**Failure and recovery.** Common failures are conflating authority with storage,
turning a context map into a mandatory graph, and drawing boundaries around teams
rather than business meaning. A shared term that changes meaning is a model change:
Evans says to "Recognize that a change in the language is a change to the model."
Microsoft says service boundaries "don't remain fixed." Recovery starts by
revisiting model behavior and ownership with the domain expert before a boundary
moves, then checking translation cost in the technical owner. The sequenced expert
review is Tycho guidance, not a quoted Microsoft or Evans rule.

**Technical owner.** [Domain-Driven Design / Bounded Context](../../v02-application-boundaries-and-contracts/c02-domain-boundaries-data-ownership-and-contracts/domain-authority.md#domain-driven-design-and-bounded-context).

**Sources.**
[src.fowler-bounded-context](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.fowler-bounded-context.2026-10-21`: Bounded Context, sections
"Bounded Context", "Further Reading", "Notes"; a definition and boundary argument,
not a full DDD reference.
[src.microsoft-ddd](../../../../edition/patterns/reading-ledger.v1.json) read
record `read.microsoft-ddd.2026-10-30`: "Use domain analysis to model
microservices", sections "Introduction", "Analyze the domain", "Define bounded
contexts"; living Microsoft Learn page, canonical revision `62191a60...`.
[src.ddd-reference](../../../../edition/patterns/reading-ledger.v1.json) read
record `read.ddd-reference-bounded-context.2026-10-30`: DDD Reference, sections
"Definitions", "Bounded Context", "Ubiquitous Language"; 2015-03 PDF, raw
revision `cf82dc7b...`.

**Decision state.** `applicable-under-conditions`.

**Related entries.** Modular Monolith; Anti-Corruption Layer; Microservices
Architecture; Database per Service.
