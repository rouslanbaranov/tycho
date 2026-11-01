---
metadata_version: 1
id: "tycho.page.523433bb7da14cc48558302d7dc322f9"
kind: "page"
parent_id: "tycho.chapter.a4b31346a691566550633efe0cf2693e"
canonical_path: "book/volumes/v11-pattern-atlas/c03-messaging-integration/correlation-identifier.md"
title: "Correlation Identifier"
topic_ids:
  - "integration-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Correlation Identifier; bounded owner evidence and limits."
route_hints:
  questions:
    - >-
      Should related messages carry an explicit identifier so replies and
      follow-ups can be matched?
  prerequisites:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  related_ids:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
    - "tycho.page.b21078a397214496a24305a2f016b021"
  excludes:
    - "No owner acceptance is claimed for this card."
  keywords:
    - "pattern atlas"
    - "correlation-identifier"
    - "messaging integration"
evidence_scope:
  source_ids:
    - "src.enterprise-integration"
    - "src.azure-service-bus"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch2-correlation.2026-10-21 and
    read.azure-service-bus-messages.2026-11-01; owner section and limits are
    bounded.
content_review:
  status: "independent-reviewed"
  reviewed_at: "2026-11-01"
  reviewer: "DeepSeek Reviewer"
  proof_uri: "https://github.com/rouslanbaranov/tycho/blob/466d9044/authoring/ai-reviews/2026-11-01-correlation-identifier-deepseek.md"
authored_at: "2026-11-01"
updated_at: "2026-11-01"
source_inspection_date: "2026-11-01"
content_verified_at: "2026-11-01"
---
# Correlation Identifier

**Identity.** Correlation Identifier; family Messaging and event-driven integration; kind
integration-pattern; priority core.

**Decision question.** Should related messages carry an explicit identifier so replies and
follow-ups can be matched?

**Good-fit conditions.** Flows span multiple messages or services; the identifier is
stable per logical operation; retention and collision policy are defined.

**Hard contraindications.** Reject when one synchronous call carries the whole exchange,
when identifiers are reused across operations, or when the receiver cannot retain
correlation state.

**Competing alternative.** Transport-level request IDs only, or a synchronous call.
Reverse the choice when correlation state and retention cost exceed the routing benefit.

**Failure and recovery.** Identifier collisions or premature expiry break matching; verify
scope and retention in the owner section.

**Technical owner.** [Correlation identifiers and workflow failure gates](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/workflow-failure.md#correlation-identifier) — workflow failure gates are bounded, not a complete request-reply contract.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-correlation.2026-10-21: served problem/solution; publisher-abridged.
The source is a public pattern/documentation
unit, not a benchmark.
[src.azure-service-bus](../../../../edition/patterns/reading-ledger.v1.json)
read record read.azure-service-bus-messages.2026-11-01: Message properties read; the owner
section binds the CorrelationId context, MessageId uniqueness and duplicate detection.
Public documentation, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Request-Reply Messaging; Idempotency Key; Distributed Tracing;
Process Manager.
