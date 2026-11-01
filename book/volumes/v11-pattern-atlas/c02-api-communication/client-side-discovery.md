---
metadata_version: 1
id: tycho.page.0644f3d65c76da81fbbb89e1d5e9fc33
kind: page
parent_id: tycho.chapter.9825cb82eb2142754c638aea1ba8d845
canonical_path: book/volumes/v11-pattern-atlas/c02-api-communication/client-side-discovery.md
title: Client-Side Discovery
topic_ids:
- api
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Client-Side Discovery.
route_hints:
  questions:
  - Should the caller own service lookup and backend selection, rather than delegating
    both to an intermediary?
  prerequisites:
  - tycho.chapter.9825cb82eb2142754c638aea1ba8d845
  related_ids:
  - tycho.chapter.9825cb82eb2142754c638aea1ba8d845
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - client side discovery
evidence_scope:
  source_ids:
  - src.microservices-patterns
  claim_ids: []
  status: source-linked
  notes: Source-level bindings remain in the owner unit.
content_review:
  status: self-checked
  reviewed_at: '2026-11-01'
  reviewer: Automated authoring agent
  proof_uri: null
authored_at: '2026-11-01'
updated_at: '2026-11-01'
source_inspection_date: '2026-10-21'
content_verified_at: null
---

# Client-Side Discovery

**Identity.** Client-Side Discovery; family API and service communication; kind
discovery pattern; priority advanced.

**Decision question.** Should the caller own service lookup and backend selection,
rather than delegating both to an intermediary?

**Good-fit conditions.** Clients can maintain membership, backoff and observability;
the client platform is controlled; selection policy is stable; stale membership can be
detected and bounded.

**Hard contraindications.** Reject the claim when clients cannot be upgraded; when
discovery logic would be duplicated across many runtimes; when the client cannot observe
backend health; when selection policy must be centrally governed.

**Competing alternative.** Server-side discovery through a proxy or load balancer.
Reverse the choice when client complexity and inconsistent policies exceed the
resolution benefit.

**Failure and recovery.** Registry outage, stale caches, divergent client policies and
retry storms are common. Keep a last-known set for reads, detect staleness and bound retries.

**Technical owner.**
 [Client-Side
Discovery](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/discovery-balancing.md#client-side-discovery)
— discovery and selection; client-specific policy is bounded to the linked section.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-client-discovery.2026-10-21: Client-side service
discovery, sections "Context", "Problem", "Forces", "Solution", "Examples", "Resulting
context", "Related patterns". Pattern page, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Service Discovery; Server-Side Discovery; Gateway Routing; Reverse
Proxy.
