---
metadata_version: 1
id: "tycho.page.b21078a397214496a24305a2f016b021"
kind: "page"
parent_id: "tycho.chapter.a4b31346a691566550633efe0cf2693e"
canonical_path: "book/volumes/v11-pattern-atlas/c03-messaging-integration/\
  request-reply-messaging.md"
title: "Request-Reply Messaging"
topic_ids:
  - "integration-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Request-Reply Messaging; bounded owner evidence and limits."
route_hints:
  questions:
    - "Should a request and response travel as a pair of messages on
      separate channels rather than one blocking call?"
  prerequisites:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  related_ids:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  excludes:
    - "provider-specific channel implementations"
  keywords:
    - "pattern atlas"
    - "request-reply-messaging"
evidence_scope:
  source_ids:
    - "src.enterprise-integration"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; source binding remains in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-28"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-28"
updated_at: "2026-10-28"
source_inspection_date: "2026-10-21"
content_verified_at: null
---

# Request-Reply Messaging

**Identity.** Request-Reply Messaging; family Messaging and event-driven integration; kind
integration-pattern; priority core.

**Decision question.** Should a request and response travel as a pair of messages on separate
channels rather than one blocking call?

**Good-fit conditions.** A requestor can wait for a reply; separate request and reply channels
exist.

**Hard contraindications.** Reject when the caller must block on a Remote Procedure Invocation
or no reply channel exists.

**Competing alternative.** A synchronous Remote Procedure Invocation blocks the caller's thread
while it waits for the response.

**Failure and recovery.** A crashed requestor can restart the reply thread; the callback must
re-establish the caller's context.

**Technical owner.** [Request-Reply Messaging](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/request-reply-messaging.md#request-reply-messaging) — separate request and reply channels and recovery limits are bounded, not a complete request-reply contract.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-request-reply.2026-10-21: Problem and Solution are
unheaded; the page is publisher-abridged and has no Example
section. The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Correlation Identifier; Asynchronous Request-Reply; API Gateway;
Timeout.
