---
metadata_version: 1
id: tycho.page.fa9d574516d3b4567b580168e72676cf
kind: page
parent_id: tycho.chapter.a4b31346a691566550633efe0cf2693e
canonical_path: book/volumes/v11-pattern-atlas/c03-messaging-integration/content-based-router.md
title: Content-Based Router
topic_ids:
- messaging
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Content-Based Router.
route_hints:
  questions:
  - Should routing be decided from message content rather than a fixed destination?
  prerequisites:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  related_ids:
  - tycho.chapter.a4b31346a691566550633efe0cf2693e
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - content based router
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

# Content-Based Router

**Identity.** Content-Based Router; family Messaging and event-driven integration; kind
integration-pattern; priority core.

**Decision question.** Should routing be decided from message content rather than a fixed
destination?

**Good-fit conditions.** Routing rules are explicit and testable; message content is
trustworthy; rule changes can be versioned; the router can expose unmatched messages.

**Hard contraindications.** Reject when a fixed route suffices, when routing depends on
untrusted fields, or when rules become domain workflow without ownership.

**Competing alternative.** Static routing or a workflow/orchestrator. Reverse the choice
when content rules become a hidden process engine.

**Failure and recovery.** Rule drift and unmatched messages are common; verify rule
ownership and fallback in the owner section.

**Technical owner.**
 [Content-Based
Router](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#content-based-router)
— predicate ownership, fallback and rule versioning are bounded, not every EIP mechanism.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-cbr.2026-10-21: only the Camel example is an H2;
Problem and Solution are unheaded, and the page is publisher-abridged. The
source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Message Filter; Pipes and Filters; Process Manager; Message Broker.
