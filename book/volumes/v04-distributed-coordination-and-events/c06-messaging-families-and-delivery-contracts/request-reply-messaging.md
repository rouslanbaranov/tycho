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
summary: "Bounded Request-Reply note; separate channels, callback, RPI alternative and limits."
route_hints:
  questions:
    - "Should a request and its reply travel as separate messages on separate channels,
      invoking the responder indirectly rather than directly, when both approaches block
      the caller?"
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
    - "src.microservices-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Moved page; bound claims, RPI alternative and limits remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-29"
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

In the Synchronous Block approach, the requestor sends the request message, blocks to wait for
the reply, then processes it. The request thread awaiting the response implies that there is only
one outstanding request, or that the reply channel for this request is private for this thread.
In the Asynchronous Callback approach, the source states: "This approach enables
multiple outstanding requests to share a single reply channel, and a single reply thread to
process replies for multiple request threads." Tycho synthesis: treat both the Synchronous Block messaging approach and direct RPI as
blocking the caller's thread; the choice is indirect
messaging versus direct invocation. Tycho synthesis: carry a Correlation Identifier and match
each reply to its request; the bound page does not serve correlation mechanics.

If the requestor crashes, it can recover by simply restarting the reply thread. An added
complexity, however, is the callback mechanism that must re-establish the caller's context.

**Alternative.** The bound Messaging page names the RPI pattern as an alternative and records
messaging's loose runtime coupling and buffered availability against the added broker complexity
and more complex request/reply communication. The page states: "The RPI pattern is an alternative
pattern". It records messaging's benefits, "Loose runtime coupling since it decouples the message
sender from the consumer" and "Improved availability since the message broker buffers messages until the consumer
is able to process them", against its costs, "Additional complexity of message broker, which
must be highly available" and "Request/reply-style communication is more complex". Tycho
synthesis: prefer direct RPI when both parties can be available for the request, the call fits the
request budget and no broker is justified; prefer messaging request-reply when loose runtime
coupling or buffered availability matters.

**Limits.** The primary bound page is publisher-abridged. It supports the separate request and
reply channels, the one-outstanding-request or private-reply-channel implication of the
Synchronous Block case, and the Synchronous Block and Asynchronous Callback descriptions. It does not present Block messaging and RPI as compared decision alternatives; Tycho synthesis
treats both as blocking. The alternative binds the microservices.io Messaging page:
"The RPI pattern is an alternative pattern"; that page records messaging's benefits and costs
but does not state a request-budget or blocking rule, so the selection conditions are Tycho
synthesis. The primary page does not serve correlation-identifier mechanics, reply timeouts,
duplicate-reply handling or a complete callback contract; matching across multiple outstanding
requests, deadline enforcement and duplicate suppression are Tycho guidance that needs
implementation evidence. A callback must re-establish the caller's context, but the bound text
does not define its contract. This page is not a complete request-reply contract.

**Sources.** Primary:
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-request-reply.2026-10-21, page
https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html,
revision 6d79d9ec15c68a7547682feb84c4adaea407795c64a69c98b6fed273eb2cea5f;
the page is publisher-abridged. Alternative:
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-communication-messaging.2026-10-29, page
https://microservices.io/patterns/communication-style/messaging.html, revision
491719296be7ab61e96cf8c59c35dab87a8d9a6d0f4d5d8641f235e61bf5369d; the
record covers Context, Forces, Problem, Solution, Examples, Resulting context,
Related patterns and See also; examples were not executed.

## Navigation

| Route | Destination |
|---|---|
| Parent chapter | [V04/C06 — Messaging families and delivery contracts](README.md) |
| Originating page | [Workflow state and messaging failure gates](workflow-failure.md#request-reply-messaging) |
| Source ledger | [Chapter source ledger](README.md#chapter-source-ledger) |
