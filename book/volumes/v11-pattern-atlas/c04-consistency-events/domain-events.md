---
metadata_version: 1
id: tycho.page.37d533ab765e6385613062c94a6e1f54
kind: page
parent_id: tycho.chapter.e9c650012060143639af44b0cfdc4236
canonical_path: book/volumes/v11-pattern-atlas/c04-consistency-events/domain-events.md
title: Domain Events
topic_ids:
- consistency
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Domain Events.
route_hints:
  questions:
  - Should a meaningful state change be published as an event that other owners can
    react to?
  prerequisites:
  - tycho.chapter.e9c650012060143639af44b0cfdc4236
  related_ids:
  - tycho.chapter.e9c650012060143639af44b0cfdc4236
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - domain events
evidence_scope:
  source_ids:
  - src.microservices-patterns
  claim_ids: []
  status: source-linked
  notes: Source-level bindings remain in the owner unit.
content_review:
  status: self-checked
  reviewed_at: '2026-11-01'
  reviewer: Automated authoring agent
  proof_uri: null
authored_at: '2026-11-01'
updated_at: '2026-11-01'
source_inspection_date: '2026-10-21'
content_verified_at: null
---

# Domain Events

**Identity.** Domain Events; family Data consistency, transactions and event sourcing;
kind integration-pattern; priority core.

**Decision question.** Should a meaningful state change be published as an event that
other owners can react to?

**Good-fit conditions.** The event represents a committed business fact with identity,
version and causation; consumers own their reactions; publication reliability and ordering
are explicit.

**Hard contraindications.** Reject when the event is only a command in disguise, when
publication is not tied to the state change, or when consumers need a shared transaction.

**Competing alternative.** Synchronous call or a command message. Reverse the choice when
event fan-out and eventual consistency exceed the decoupling benefit.

**Failure and recovery.** Duplicate, late, out-of-order and schema-evolved events are
common; deduplicate by identity, preserve aggregate order and keep an unknown/repair state
when publication is not atomic with the state change.

**Technical owner.**
 [Domain Events](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/cqrs-event-sourcing-and-read-projections.md#domain-events) — the
distinction is bounded, not a domain-event catalogue.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-domain-event.2026-10-21: sections "Context", "Problem", "Solution",
"Related patterns", "See also". The page has no Forces/Example/Resulting context sections; event
identity, ordering and reliability are synthetic guidance, not source claims. The source is a
public pattern/specification unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Event Sourcing; Transactional Outbox; Saga; CQRS.
