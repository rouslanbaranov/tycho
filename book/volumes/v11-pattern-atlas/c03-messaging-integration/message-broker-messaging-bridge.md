---
metadata_version: 1
id: tycho.page.9282bea0ffb00f6989c605b86a73ab8f
kind: page
parent_id: tycho.chapter.a4b31346a691566550633efe0cf2693e
canonical_path: book/volumes/v11-pattern-atlas/c03-messaging-integration/message-broker-messaging-bridge.md
title: Message Broker / Messaging Bridge
topic_ids:
- messaging
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Message Broker / Messaging Bridge.
route_hints:
  questions:
  - Should a broker mediate routing and delivery between producers and consumers,
    possibly bridging protocols?
  prerequisites:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  related_ids:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - message broker messaging bridge
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

# Message Broker / Messaging Bridge

**Identity.** Message Broker / Messaging Bridge; family Messaging and event-driven
integration; kind messaging-pattern; priority core.

**Decision question.** Should a broker mediate routing and delivery between producers and
consumers, possibly bridging protocols?

**Good-fit conditions.** Multiple producers/consumers need decoupling; routing and
delivery policy are owned; bridge semantics are explicit; the broker can be observed.

**Hard contraindications.** Reject when one direct call suffices, when the broker becomes
an unowned single point, or when protocol bridging hides semantic loss.

**Competing alternative.** Direct messaging or a simpler queue. Reverse the choice when
broker complexity and operational cost exceed decoupling benefit.

**Failure and recovery.** Broker outage, bridge semantic drift and duplicate or delayed crossing
are common; verify broker availability, the bridge contract, identity mapping and dead-letter
path in the owner section.

**Technical owner.**
 [Message Broker / Messaging
Bridge](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#message-broker-messaging-bridge)
— bridge contract and failure-domain ownership is the bounded owner, not a channel page.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-broker.2026-10-21: no article headings; Example is
absent and the page is publisher-abridged. The
source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Publish/Subscribe; Point-to-Point Queue; Canonical Data Model;
Gateway Routing.
