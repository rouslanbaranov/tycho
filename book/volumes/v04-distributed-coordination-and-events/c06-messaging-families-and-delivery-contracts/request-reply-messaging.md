---
metadata_version: 1
id: "tycho.page.7327a6422143416f8ff012e5c168ed5a"
kind: "page"
parent_id: "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/request-reply-messaging.md"
title: "Request-Reply Messaging"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
summary: "Bounded Request-Reply Messaging owner note; separate channels, Synchronous Block and Asynchronous Callback, recovery and limits."
route_hints:
  questions:
    - "Should a request and response travel as a pair of messages on separate channels rather than one blocking call?"
  prerequisites:
    - "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
  related_ids:
    - "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "request-reply messaging"
    - "owner note"
evidence_scope:
  source_ids:
    - "src.enterprise-integration"
  claim_ids: []
  status: "source-linked"
  notes: "Moved verbatim from the workflow state and messaging failure gates page; the bound source claims and limits remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-21"
content_verified_at: null
---

# Request-Reply Messaging

> **Pattern atlas:**
> [Request-Reply Messaging](../../v11-pattern-atlas/c03-messaging-integration/request-reply-messaging.md#request-reply-messaging) — decision conditions and contraindications.

This page owns the bounded technical note moved from the
[workflow state and messaging failure gates page](workflow-failure.md#request-reply-messaging)
on 2026-10-29. The other ownership notes remain on the chapter page.

Send a pair of Request-Reply messages, each on its own channel. The requestor sends a request and
waits for a reply; the replier receives the request and responds. The request channel and reply
channel are separate. The requestor waits for the reply; the replier processes the request and
sends the response.

In the Synchronous Block approach, the request thread awaiting the response implies that there
is only one outstanding request, or that the reply channel for this request is private for this
thread. In the Asynchronous Callback approach, the source states: "This approach enables
multiple outstanding requests to share a single reply channel, and a single reply thread to
process replies for multiple request threads." Tycho synthesis: carry a Correlation Identifier
and match each reply to its request; the bound page does not serve correlation mechanics.

If the requestor crashes, it can recover by simply restarting the reply thread. An added
complexity, however, is the callback mechanism that must re-establish the caller's context.

**Alternative.** The bound page states that when a caller performs a Remote Procedure Invocation,
the caller's thread must block while it waits for the response. Tycho synthesis: a direct
synchronous Remote Procedure Invocation is the alternative when the responder is reachable within
the caller's request budget and blocking is acceptable; the bound page does not present RPC as a
decision alternative.

**Limits.** The bound page is publisher-abridged. It supports the separate request and reply
channels, the one-outstanding-request or private-reply-channel implication of the Synchronous
Block case, and the Synchronous Block and Asynchronous Callback descriptions. It states:
"This approach enables multiple outstanding requests to share a single reply channel, and a
single reply thread to process replies for multiple request threads." It does not serve
correlation-identifier mechanics, reply timeouts, duplicate-reply handling or a complete
callback contract; matching across multiple outstanding requests, deadline enforcement and
duplicate suppression are Tycho guidance that needs implementation evidence. A
callback must re-establish the caller's context, but the bound text does not define its
contract. This page is not a complete request-reply contract.

## Navigation

| Route | Destination |
|---|---|
| Parent chapter | [V04/C06 — Messaging families and delivery contracts](README.md) |
| Originating page | [Workflow state and messaging failure gates](workflow-failure.md#request-reply-messaging) |
| Source ledger | [Chapter source ledger](README.md#chapter-source-ledger) |
