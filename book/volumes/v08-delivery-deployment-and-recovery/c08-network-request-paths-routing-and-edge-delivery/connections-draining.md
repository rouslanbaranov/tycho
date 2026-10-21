---
{
  "metadata_version": 1,
  "id": "tycho.page.1278bbadfc82b8cd481e94b6bd7f7633",
  "kind": "page",
  "parent_id": "tycho.chapter.8a86707018773def410689efbc79cf94",
  "canonical_path": "book/volumes/v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/connections-draining.md",
  "title": "Connection lifetimes, HTTP/2 shutdown and retry outcomes",
  "topic_ids": [
    "network-architecture"
  ],
  "perspectives": [
    "architecture",
    "operations",
    "evaluation"
  ],
  "summary": "What does a transport shutdown establish about an in-flight application operation?",
  "route_hints": {
    "questions": [
      "What does a transport shutdown establish about an in-flight application operation?"
    ],
    "prerequisites": [],
    "related_ids": [
      "tycho.chapter.8a86707018773def410689efbc79cf94"
    ],
    "excludes": [
      "No executed product experiment or independent acceptance is claimed."
    ],
    "keywords": [
      "what",
      "does",
      "transport",
      "shutdown",
      "establish",
      "about",
      "in-flight",
      "application",
      "operation"
    ]
  },
  "evidence_scope": {
    "source_ids": [
      "src.rfc9113-enrichment",
      "src.http-semantics"
    ],
    "claim_ids": [],
    "status": "source-linked",
    "notes": "Exact selected passages and source limitations are recorded in the page ledger and dated enrichment inspection record. Synthetic protocols are original design reasoning."
  },
  "content_review": {
    "status": "self-checked",
    "reviewed_at": "2026-10-20",
    "reviewer": "Codex enrichment author; execution gates pending",
    "proof_uri": null
  },
  "authored_at": "2026-10-20",
  "updated_at": "2026-10-20",
  "source_inspection_date": "2026-10-20",
  "content_verified_at": null
}
---

# Connection lifetimes, HTTP/2 shutdown and retry outcomes

**Owning question:** What does a transport shutdown establish about an in-flight application operation?

## Name the affected layer

A connection, an HTTP/2 stream, one request attempt and a logical business operation have different identities. A connection may carry several streams; an operation may have several attempts. Record which layer emitted the error before interpreting a client message such as GOAWAY.

RFC 9113 sections 6.8 and 8.7 define a shutdown boundary using the last stream identifier. Streams above that boundary were not processed by the sending endpoint; streams at or below it may have been processed. A missing response is not evidence that the application rolled back. An intermediary's boundary applies to that hop, not automatically to a downstream side effect.

## Original trace: graceful shutdown with an ambiguous write

A fictional client uses streams 3, 5 and 7. The server sends GOAWAY with last-stream ID 5. Treat stream 7 as not processed at that peer and establish a replacement connection. Stream 5, a command to publish an object, may already have committed. Its correct recovery lookup uses the same logical operation identity.

~~~mermaid
sequenceDiagram
    participant C as Client
    participant P as Proxy
    participant S as Service
    participant D as State owner
    C->>P: Publish operation K
    P->>S: Forward attempt with K
    S->>D: Commit effect for K
    S--xP: Response lost during shutdown
    P-->>C: Attempt outcome unknown
    C->>S: Resolve K on a usable route
    S->>D: Read authoritative result for K
    D-->>S: Existing authoritative result
    S-->>C: Existing result for K
~~~

Text alternative: losing the response after commit requires resolving the existing operation, even if a new connection is healthy. The sketch is synthetic; clients resolve the result through the service, not direct database access.

Connection pooling reduces repeated setup work but couples many requests to one transport failure. HTTP/2 multiplexing does not remove TCP-level loss effects or unlimited application buffering. Flow-control windows constrain transport data; an application may still accumulate decoded requests, tasks or retained response objects.

## A bounded drain procedure

1. Mark the instance ineligible for new work through the actual selector.
2. Start protocol-appropriate graceful shutdown; preserve enough time for route caches and active work.
3. Allow admitted work to finish within its declared budget. Cancel only where cancellation semantics permit.
4. Record unresolved operation IDs before forced termination and expose a reconciliation path.
5. Remove the instance after the drain condition or explicit bounded timeout.

This is a proposed procedure. The exact proxy/runtime determines signal ordering, propagation and stream behavior. A hard shutdown deadline may leave unknown effects; it cannot manufacture atomic cancellation.

## Diagnose before changing pool settings

Separate name-resolution, connect, handshake, queue, first-byte, transfer and application-effect time. Compare connection ages, active streams, close reasons, GOAWAY code/boundary, retry volume and operation outcomes. Avoid logging credentials or raw untrusted debug fields.

Keepalive, idle timeout and maximum connection lifetime address different contracts. Increasing all values may hide leaked resources or retain endpoints through maintenance. Excessively short lifetimes can create setup storms. Pick values using measured traffic and actual peer behavior rather than a universal duration.

## Evidence and review

[RFC 9113](https://www.rfc-editor.org/rfc/rfc9113.html#section-6.8) supports GOAWAY and [section 8.7](https://www.rfc-editor.org/rfc/rfc9113.html#section-8.7) supports request reliability. The trace and drain procedure are original reasoning. Test receipt of GOAWAY before and after downstream commit, peer close without GOAWAY, and forced drain expiration. No network/client execution or syntax rendering is claimed.

## Navigation

Parent: [network chapter](README.md). Previous: [selection](discovery-balancing.md). Next: [trust boundaries](tls-gateway-boundaries.md). Read [effect identity](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/effect-identity.md) and [deadlines](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/deadlines-retries.md).
