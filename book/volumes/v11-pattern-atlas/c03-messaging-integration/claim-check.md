---
metadata_version: 1
id: "tycho.page.a684d25ff3d94fd1930186b57b5d3703"
kind: "page"
parent_id: "tycho.chapter.a4b31346a691566550633efe0cf2693e"
canonical_path: "book/volumes/v11-pattern-atlas/c03-messaging-integration/claim-check.md"
title: "Claim Check"
topic_ids:
  - "integration-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Claim Check; bounded owner evidence and limits."
route_hints:
  questions:
    - >-
      Should a large or sensitive payload travel outside the message and be
      retrieved through a claim check?
  prerequisites:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  related_ids:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  excludes:
    - "payload-store implementations"
  keywords:
    - "pattern atlas"
    - "claim-check"
evidence_scope:
  source_ids:
    - "src.enterprise-integration"
    - "src.microsoft-cloud-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-28"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-28"
content_verified_at: null
---

# Claim Check

**Decision.** Store a large or sensitive payload outside the message and send a claim check
only when payload size, sensitivity or repeated serialization justifies the extra store and
retrieval hop, when payload lifecycle and failure handling have owners, and when
authorization can remain an independent interaction between producer or consumer systems and
the store. Sensitivity and repeated serialization are source-stated use conditions. Keep the
payload inline when it fits the transport and latency budget and no sensitivity, retention or
repeated-serialization reason applies; the retention reason is Tycho synthesis, not a source
claim.

**Identity.** Claim Check; family Messaging and event-driven integration; kind
messaging-pattern; priority advanced.

**Decision question.** Should a large or sensitive payload travel outside the message and be
retrieved through a claim check?

**Good-fit conditions.** Payloads regularly exceed the transport limit, consume
disproportionate broker resources, need sensitive content kept out of the messaging path with
dedicated access controls in a secured store, or cross routing hops that repeatedly serialize
them. The payload lifecycle has an owner and a retention policy; the token is published only
after the payload write succeeds; retrieval latency and failure disposition are bounded; the
external store applies access controls independently of the messaging system. Tycho guidance,
not a source claim: keep the token bound to the stored payload it names.

**Hard contraindications.** Reject when the payload fits the transport and latency budget and
no sensitivity, retention or repeated-serialization reason applies (sensitivity and repeated
serialization are source-stated use conditions; retention is Tycho synthesis), when the extra
retrieval hop cannot meet the latency target, when payload lifecycle or failure handling has
no owner, or when authorization cannot remain an independent interaction with the store.

**Competing alternative.** Inline payload when it stays within the transport's supported limit
and does not create unacceptable throughput or latency; compression or a compact serializer can
reduce inline size. Tycho guidance, not a source claim: reverse the choice only when the
payload fits inline, no sensitivity, retention or repeated-serialization reason applies, and
retrieval and storage complexity exceed the savings.

**Failure and recovery.** The non-atomic write and publish pair can leave an orphaned payload
or a token that consumers cannot resolve; the source also names duplicate claim checks,
integrity mismatches, store outages and data loss. Use an idempotent consumer for duplicate
claim checks. Tycho guidance, not a source claim: expire and garbage-collect claims, and fail
closed when retrieval is impossible.

**Technical owner.** [Claim Check](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/claim-check.md#claim-check) — payload lifecycle, claim-token ordering, retrieval and failure policy are bounded; authorization remains an independent interaction with the store, and this is not a payload-store catalogue.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-claim.2026-10-21: the public pattern page is publisher-abridged and
supports the stored-payload and claim-token description, not the failure or alternative
policy. [src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-claim-check.2026-10-28: the Claim Check pattern page supports the
mechanism, payload lifecycle ownership, write-before-publish invariant, independent
authorization, the six failure cases, the sensitive-payload and repeated-serialization use
conditions, the inline alternative and compression or compact-serializer guidance.
Canonical text SHA-256: 391b162aaa47634d8898bf971471f8d9f19b69e08973a3277ffe4ef1463a0bfe.
The source is public documentation, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Message Broker; Dead Letter Channel; Valet Key; Pipes and Filters;
Idempotent Receiver.
