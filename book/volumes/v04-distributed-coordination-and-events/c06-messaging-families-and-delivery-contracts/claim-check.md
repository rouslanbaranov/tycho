---
metadata_version: 1
id: "tycho.page.d44c30621fd941318453e3ff995a3e93"
kind: "page"
parent_id: "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/claim-check.md"
title: "Claim Check"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
summary: "Bounded Claim Check owner note; payload store, token ordering, lifecycle and retrieval failure limits."
route_hints:
  questions:
    - "Should a large or sensitive payload travel outside the message and be retrieved through a claim check?"
  prerequisites:
    - "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
  related_ids:
    - "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "claim check"
    - "owner note"
evidence_scope:
  source_ids:
    - "src.enterprise-integration"
    - "src.microsoft-cloud-patterns"
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
source_inspection_date: "2026-10-28"
content_verified_at: null
---

# Claim Check

> **Pattern atlas:**
> [Claim Check](../../v11-pattern-atlas/c03-messaging-integration/claim-check.md#claim-check) — decision conditions and contraindications.

This page owns the bounded technical note moved from the
[workflow state and messaging failure gates page](workflow-failure.md#claim-check)
on 2026-10-29. The other ownership notes remain on the chapter page.

**Decision.** Store a large or sensitive payload outside the messaging system and send a
claim check only when payload size, sensitivity or repeated serialization justifies the
extra store and retrieval hop, when payload lifecycle and failure handling have owners, and
when authorization can remain an independent interaction between producer or consumer systems
and the store. Keep the payload inline when it fits the transport and latency budget.

**Mechanism.** A sending application writes the full payload to an external data store and
sends a reference to that payload through the messaging system. Receiving applications use the
reference to retrieve the payload directly from the data store. The source describes the
sequence as saving the payload, generating the reference after a successful save, publishing
it, and letting the receiver retrieve the payload before processing.

**Invariant.** Publish the token only after the payload write succeeds. Payload write and token
publication occur in separate systems and are not atomic, so a token published before its
payload is retrievable leaves consumers with references they cannot resolve; a payload
written without a published token is orphaned. The source requires defining which component
owns payload deletion, requires coordination between message expiration and payload retention
so a valid claim check does not point to deleted data, and leaves authorization as an
independent interaction between producer or consumer systems and the data store. Tycho
guidance: keep the token bound to the stored payload it names and do not treat the claim check
as an authorization token.

**Failure and recovery.** The source names six failure cases: an orphaned payload, an
unresolvable token, a duplicate claim check, an integrity mismatch, a store outage, and data
loss. Publish the token only after the payload write succeeds, use an idempotent consumer for
duplicate claim checks, define a disposition for integrity mismatches, and keep the store
available and durable for the retention period. Tycho guidance: expire and garbage-collect
claims, and fail closed when retrieval is impossible.

**Alternative.** The source states: "When payloads stay within a transport's supported limit
and don't create unacceptable throughput or latency, send them inline to avoid the
external-store dependency." Compression or a compact serializer can reduce inline size. Reverse
the choice when retrieval and storage complexity exceed the savings.

**Limits.** A claim check adds an external store, a retrieval hop and a second consistency
boundary; it is not a payload catalogue or a security token. The source requires defining
which component owns payload deletion and coordinating message expiration and payload
retention; Tycho guidance, not a source claim, adds tenant binding and a cleanup path for
claims.

**Evidence.** The Microsoft Learn Claim Check pattern page (accessed 2026-10-28, canonical
text SHA-256 391b162aaa47634d8898bf971471f8d9f19b69e08973a3277ffe4ef1463a0bfe) supports the
mechanism, payload lifecycle ownership, the write-before-publish invariant, the orphaned
payload, unresolvable token, duplicate claim check, integrity mismatch, store outage and data
loss failure cases, the inline alternative, and compression or compact-serializer guidance.
The public Enterprise Integration Patterns Claim Check page (read.batch2-claim.2026-10-21)
supports the stored-payload and claim-token description; it is publisher-abridged and does not
state the failure or alternative policy.

## Navigation

| Route | Destination |
|---|---|
| Parent chapter | [V04/C06 — Messaging families and delivery contracts](README.md) |
| Originating page | [Workflow state and messaging failure gates](workflow-failure.md#claim-check) |
| Source ledger | [Chapter source ledger](README.md#chapter-source-ledger) |
