---
metadata_version: 1
id: tycho.page.d1feeae1c67c661e5fc984c4b93514a4
kind: page
parent_id: tycho.chapter.a4b31346a691566550633efe0cf2693e
canonical_path: book/volumes/v11-pattern-atlas/c03-messaging-integration/canonical-data-model.md
title: Canonical Data Model
topic_ids:
- messaging
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Canonical Data Model.
route_hints:
  questions:
  - Should interapplication messages use a shared canonical model rather than point-to-point
    translations?
  prerequisites:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  related_ids:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - canonical data model
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

# Canonical Data Model

**Identity.** Canonical Data Model; family Messaging and event-driven integration; kind
integration-pattern; priority advanced.

**Decision question.** Should interapplication messages use a shared canonical model
rather than point-to-point translations?

**Good-fit conditions.** Multiple systems exchange the same concepts; a canonical model
has an owner; versioning and translation are funded; semantic drift is controlled.

**Hard contraindications.** Reject when only two systems integrate, when one team cannot
own the canonical model, or when translation cost exceeds reuse.

**Competing alternative.** Point-to-point message contracts or an anti-corruption layer.
Reverse the choice when canonical-model governance becomes a bottleneck.

**Failure and recovery.** Model drift and translation debt are common; verify ownership
and versioning in the owner section.

**Technical owner.**
 [Canonical Data
Model](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#canonical-data-model)
— canonical schema ownership is bounded, not every EIP mechanism.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-canonical.2026-10-21: no article headings; Example is
absent and the page is publisher-abridged.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Anti-Corruption Layer; Message Broker; Domain-Driven Design / Bounded
Context; Schema Evolution.
