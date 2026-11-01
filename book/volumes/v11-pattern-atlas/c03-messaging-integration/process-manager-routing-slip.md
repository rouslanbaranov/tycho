---
metadata_version: 1
id: tycho.page.325f2fd7732b9a3d258dc1c3ec37d255
kind: page
parent_id: tycho.chapter.a4b31346a691566550633efe0cf2693e
canonical_path: book/volumes/v11-pattern-atlas/c03-messaging-integration/process-manager-routing-slip.md
title: Process Manager / Routing Slip
topic_ids:
- messaging
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Process Manager / Routing Slip.
route_hints:
  questions:
  - Should a durable coordinator or a routing-slip itinerary own a multi-step message
    flow and its recovery?
  prerequisites:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  related_ids:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - process manager routing slip
evidence_scope:
  source_ids:
  - src.enterprise-integration
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

# Process Manager / Routing Slip

**Identity.** Process Manager / Routing Slip; family Messaging and event-driven
integration; kind integration-pattern; priority advanced.

**Decision question.** Should a durable coordinator or a routing-slip itinerary own a
multi-step message flow and its recovery?

**Good-fit conditions.** Steps span services; progress must survive failure; a central
durable state or a fixed itinerary can carry progress; the workflow state has an owner.

**Hard contraindications.** Reject when one local transaction suffices, when no one owns
workflow state, or when the itinerary cannot be made durable.

**Competing alternative.** Saga/choreography or a simple pipeline. Reverse the choice when
central coordination becomes a bottleneck or the itinerary cannot be fixed.

**Failure and recovery.** Stuck workflows, lost dispatch, duplicate steps and ambiguous
effects are common; verify recorded dispatch intent in the owner section.

**Technical owner.**
 [Process Manager-Routing
Slip](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/saga-workflows.md#process-manager-routing-slip)
— process-manager and routing-slip coordination is bounded, not a full engine specification.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-process.2026-10-21: two H2 vendor examples; Problem
and Solution are unheaded, and the page is publisher-abridged. The
source is a public pattern/documentation
unit, not a benchmark. The cited source supports the process-manager concept; the
routing-slip variant is bounded to the owner section's original design guidance, not this
source.

**Decision state.** applicable-under-conditions.

**Related entries.** Saga; Idempotent Receiver; Correlation Identifier; Workflow Failure.

## Chapter result and counterexample

Twenty cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: a durable subscriber that replays an unbounded history without an owner
is not evidence for the durable-subscriber card's retention conditions.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C02](../c02-api-communication/README.md).
- Next: [V11/C04](../c04-consistency-events/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 20 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated EIP pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.
