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
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-28"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-21"
content_verified_at: null
---

# Request-Reply Messaging

**Decision.** Use messaging Request-Reply when a request and its reply travel as separate
messages and the requestor can wait or handle a callback. In the Synchronous Block case, the
request thread waits for the reply, which implies one outstanding request or a reply channel
private to the requesting thread. In the Asynchronous Callback case, the source states that
multiple outstanding requests can share a single reply channel; Tycho synthesis: carry a
Correlation Identifier and match each reply to its request, because the bound page does not
serve correlation mechanics. Prefer a direct synchronous Remote Procedure Invocation when the
responder is reachable within the caller's request budget and blocking is acceptable.

**Identity.** Request-Reply Messaging; family Messaging and event-driven integration; kind
integration-pattern; priority core.

**Decision question.** Should a request and response travel as a pair of messages on separate
channels rather than one blocking call?

**Good-fit conditions.** A requestor can wait for a reply; separate request and reply channels
exist; in the Synchronous Block case, at most one request is outstanding or the reply channel
is private to the requesting thread. Tycho guidance, not a served source claim: a Correlation
Identifier scopes reply matching when multiple requests share a reply channel; the source
states that Asynchronous Callback enables that sharing but not the correlation mechanics.

**Hard contraindications.** Reject when a direct synchronous Remote Procedure Invocation meets
the availability and latency target and the caller can block, or when no reply channel can be
established. Tycho synthesis: a blocking caller thread alone is not a contraindication,
because the source's Synchronous Block approach also waits for a reply.

**Competing alternative.** Tycho synthesis: a direct synchronous Remote Procedure Invocation
is the alternative when the responder is reachable within the request budget and blocking is
acceptable. The bound source states only that an RPC caller's thread must block while it waits
for the response, not that RPC is the decision alternative.

**Failure and recovery.** A crashed requestor can restart the reply thread; the callback must
re-establish the caller's context. Tycho guidance, not a served source claim: bound retries,
time out unresolved requests, and treat duplicate replies as idempotent outcomes.

**Technical owner.** [Request-Reply Messaging](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/request-reply-messaging.md#request-reply-messaging) — separate request and reply channels, one-outstanding or private reply channel, callback recovery and limits are bounded; this is not a complete request-reply contract.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-request-reply.2026-10-21: Problem and Solution are
unheaded; the served page also has Synchronous Block and Asynchronous Callback
approaches, including the callback statement that multiple outstanding requests
can share a reply channel; the page is publisher-abridged and has no Example
section; correlation mechanics and timeout text are not served. The source is a
public pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Correlation Identifier (Tycho path for multiple outstanding requests; the
source does not serve the mechanics); Asynchronous Request-Reply; API Gateway; Timeout.
