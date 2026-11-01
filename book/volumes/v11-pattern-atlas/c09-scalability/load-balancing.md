---
metadata_version: 1
id: "tycho.page.6f2a1c9d4b7e4a0c8d3f5b2e1a7c9d43"
kind: "page"
parent_id: "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
canonical_path: "book/volumes/v11-pattern-atlas/c09-scalability/load-balancing.md"
title: "Load Balancing"
topic_ids:
  - "scalability"
perspectives:
  - "architecture"
  - "operations"
  - "evaluation"
summary: "Decision card for Load Balancing with sufficient decision evidence; owner page remains self-checked."
route_hints:
  questions:
    - "Should requests be distributed across equivalent backends by a resolver or proxy?"
  prerequisites:
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
  related_ids:
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
  excludes:
    - "No owner acceptance is claimed for this card."
  keywords:
    - "pattern atlas"
    - "load balancing"
    - "scalability"
evidence_scope:
  source_ids:
    - "src.sre-frontend-enrichment"
    - "src.sre-balancing-enrichment"
  claim_ids: []
  status: "source-linked"
  notes: "Source-level bindings remain in the owner unit; claim ids are not mapped."
content_review:
  status: "independent-reviewed"
  reviewed_at: "2026-11-01"
  reviewer: "DeepSeek Reviewer"
  proof_uri: "https://github.com/rouslanbaranov/tycho/blob/5649803b/authoring/ai-reviews/2026-11-01-load-balancing-deepseek.md"
authored_at: "2026-11-01"
updated_at: "2026-11-01"
source_inspection_date: "2026-10-23"
content_verified_at: "2026-11-01"
---

# Load Balancing

**Identity.** Load Balancing; family Scalability and load distribution; kind
scalability-pattern; priority core.

**Decision question.** Should requests be distributed across equivalent backends by a
resolver or proxy?

**Good-fit conditions.** Multiple eligible backends exist; health/selection signals are
available; membership freshness is observable; the client or proxy can retry safely.

**Hard contraindications.** Reject when one backend can serve the load, when backends are
not equivalent, or when selection would amplify a hot spot.

**Competing alternative.** Client-side selection or a single backend. Reverse the choice
when balancing complexity and stale membership exceed availability benefit. Among policies,
round-robin, random choice, least-active requests and affinity compete; affinity is Tycho guidance.

**Failure and recovery.** An unhealthy backend can return errors in milliseconds, so a
least-loaded selector sends it more traffic; the source calls this sinkholing. When backends
do not share connection state, removing one from a modulo-N pool remaps almost every key and
resets connections. **Tycho guidance:** consistent hashing, lame-duck draining and testing
under the real cost distribution.

**Technical owner.** [Load Balancing](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/discovery-balancing.md#load-balancing).

**Sources.** [src.sre-frontend-enrichment](../../../../edition/patterns/reading-ledger.v1.json)
read.batch5-sre-frontend.2026-10-21 and
[src.sre-balancing-enrichment](../../../../edition/patterns/reading-ledger.v1.json)
read.sre-balancing.2026-10-23. SRE chapters, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Server-Side Discovery, Horizontal Scaling, Vertical Scaling,
Autoscaling.
