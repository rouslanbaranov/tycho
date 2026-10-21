---
metadata_version: 1
id: "tycho.chapter.5de52a840c14448c946a65c924f28487"
kind: "chapter"
parent_id: "tycho.volume.7e8f5fd0c9d94504b6dc74b9ae6c30f3"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c03-modular-monolith-and-internal-events/README.md"
title: "V02/C03 — Modular monolith and internal events"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which coupling and deployment constraints fit an in-process architecture? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Which coupling and deployment constraints fit an in-process architecture?"
  prerequisites:
    - "tycho.chapter.7031445877fb4f8d831d962d170521c8"
  related_ids:
    - "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
    - "tycho.page.a06fd146f96b4b17a754f4d3b608ebdf"
    - "tycho.page.4365dbae044244c1b82751a39704e292"
    - "tycho.page.07bb1f96bdd94195ac8e31644527a217"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# V02/C03 — Modular monolith and internal events

## Purpose and mission

Which coupling and deployment constraints fit an in-process architecture? This chapter owns that question within application boundaries and interaction contracts. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Use enforced module contracts to retain useful local transactions and make internal event durability explicit.

An after-commit callback is not a durable external delivery mechanism; process death can separate a committed change from its notification. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](modular-monolith-and-internal-events.md) | Which coupling and deployment constraints fit an in-process architecture? |
| [Module boundaries and deployment choice](module-enforcement.md) | How can one deployable enforce ownership without imitating remote services? |
| [Internal events and transaction timing](events-transactions.md) | What can happen between local commit, event handling and process death? |

## Boundaries and further reading

- [V04/C05 — Outbox, inbox, sagas and durable workflows](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V02 — Application boundaries and interaction contracts](../README.md) |
| Previous | [V02/C02 — Domain boundaries, data ownership and contracts](../c02-domain-boundaries-data-ownership-and-contracts/README.md) |
| Next | [V02/C04 — SOA, microservices and distributed boundaries](../c04-soa-microservices-and-distributed-boundaries/README.md) |
| Prerequisite | [V02/C02 — Domain boundaries, data ownership and contracts](../c02-domain-boundaries-data-ownership-and-contracts/README.md) |
| Source reading | [Page-local evidence and versions](modular-monolith-and-internal-events.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.a06fd146f96b4b17a754f4d3b608ebdf:7 -->
## 7. Source ledger and limits

| Independent source inspected | Narrow support | Not established |
|---|---|---|
| [Spring Modulith events](https://docs.spring.io/spring-modulith/reference/events.html) | Module event publication, listener registry and incomplete-publication recovery concepts | Actual project configuration or guarantee in all library versions |
| [Spring Framework transaction-bound events](https://docs.spring.io/spring-framework/reference/7.1/data-access/transaction/event.html) | Listener phases relative to commit/rollback | Automatically durable after-commit processing |
| [Tycho architecture styles](../../../application/architecture-styles-and-module-boundaries.md) | Independently researched module and service boundaries | Compiled/enforced module graph for fictional app |
| [Tycho distributed outbox](../../../distributed/transactional-outbox-and-idempotency.md) | Commit/pub ambiguity, deduplication limits | An implemented event registry or exactly-once external effect |

All modules, diagrams, events and failure cases are original invented teaching materials. No real source code, build output, dependency checker, distributed test or human domain approval was used. The final book volume/chapter/page edition has not been assembled.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.a06fd146f96b4b17a754f4d3b608ebdf:8 -->
## Navigation

Proposed owner **V02/C03** in [planned table of contents](../../../PROPOSED-STRUCTURE.md), [application landing](../../../application/README.md). Start with [bounded contexts and ownership](../c02-domain-boundaries-data-ownership-and-contracts/domain-boundaries-data-ownership-and-contracts.md), then [module/service styles](../../../application/architecture-styles-and-module-boundaries.md), [internal vs external outbox](../../../distributed/transactional-outbox-and-idempotency.md) and [safe extraction](../../../application/architecture-evolution-and-extraction.md).

<!-- /tycho-question-source -->
