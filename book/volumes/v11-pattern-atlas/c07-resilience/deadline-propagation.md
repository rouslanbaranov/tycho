---
metadata_version: 1
id: "tycho.page.364e2c08af2a47249d9d3431346f046c"
kind: "page"
parent_id: "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
canonical_path: "book/volumes/v11-pattern-atlas/c07-resilience/deadline-propagation.md"
title: "Deadline Propagation"
topic_ids:
  - "performance-engineering"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "operations"
summary: "Decision card for Deadline Propagation with bounded owner evidence."
route_hints:
  questions:
    - "Should the caller’s remaining time budget be passed through downstream calls?"
  prerequisites:
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
  related_ids:
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved card."
  keywords:
    - "pattern atlas"
    - "deadline propagation"
    - "resilience"
evidence_scope:
  source_ids:
    - "src.grpc-deadlines"
    - "src.grpc-protocol"
    - "src.sre-cascading"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.grpc-deadlines.2026-10-30, read.grpc-protocol.2026-10-30 and
    read.batch4-sre-cascading.2026-10-21; owner section and limits are bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-30"
updated_at: "2026-10-30"
source_inspection_date: "2026-10-30"
content_verified_at: null
---
# Deadline Propagation

**Identity.** Deadline Propagation; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should the caller’s remaining time budget be passed through
downstream calls?

**Good-fit conditions.** The full request path can carry the remaining budget as a
relative duration; each hop enforces expiry before more work; expiration is observable.

**Hard contraindications.** Reject when downstream work must outlive the caller request,
when only absolute wall-clock deadlines are available across hosts with unbounded skew,
or when no hop enforces expiry.

**Competing alternative.** Independent per-hop timeouts with a parent budget. Reverse the
choice when propagation complexity exceeds the benefit of end-to-end bounds.

**Failure and recovery.** Clock skew, a lost timeout header and a hop that ignores
expiry are common. gRPC converts the absolute deadline to a relative timeout with elapsed
time deducted, removing the clock-synchronization dependency; an omitted `grpc-timeout`
header means an infinite timeout, so a lost header silently removes the bound. The server
cancels on expiry and the client fails with `DEADLINE_EXCEEDED`, but the application must
still stop spawned work. Requiring a deadline at ingress, defining a bounded skew for
absolute timestamps, and recording cancellation outcomes are Tycho guidance.

**Technical owner.** [Deadline Propagation](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/deadlines-retries.md#deadline-propagation) — gRPC relative-timeout conversion, SRE per-stage enforcement and platform-specific skew bounds.

**Sources.** [src.sre-cascading](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-sre-cascading.2026-10-21, section "Latency and Deadlines";
[src.grpc-deadlines](../../../../edition/patterns/reading-ledger.v1.json) record
read.grpc-deadlines.2026-10-30, sections "Deadlines on the Client", "Deadlines on the
Server" and "Deadline Propagation";
[src.grpc-protocol](../../../../edition/patterns/reading-ledger.v1.json) record
read.grpc-protocol.2026-10-30, section "Requests". The guides do not test an
implementation or define a numeric skew bound.

**Decision state.** applicable-under-conditions.

**Related entries.** Timeout; Retry with Exponential Backoff; Request-Reply; Async
Request-Reply.
