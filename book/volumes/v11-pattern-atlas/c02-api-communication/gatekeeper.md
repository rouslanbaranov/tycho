---
metadata_version: 1
id: "tycho.page.e709abf2484148c4a0d0fe76321a09b6"
kind: "page"
parent_id: "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
canonical_path: "book/volumes/v11-pattern-atlas/c02-api-communication/gatekeeper.md"
title: "Gatekeeper"
topic_ids:
  - "application-architecture"
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Gatekeeper with bounded owner evidence."
route_hints:
  questions:
    - "Should a narrow gatekeeper validate requests before they reach a sensitive backend?"
  prerequisites:
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  related_ids:
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "gatekeeper"
    - "security"
evidence_scope:
  source_ids:
    - "src.microsoft-cloud-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
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

# Gatekeeper

**Identity.** Gatekeeper; family API and service communication; kind security pattern;
priority advanced.

**Decision question.** Should a narrow gatekeeper validate and shape requests before
they reach a sensitive backend, rather than exposing the backend directly?

**Good-fit conditions.** A small validation surface can reject malformed or
unauthorized requests; the gatekeeper can authenticate and forward trusted context;
the backend retains object-level authorization; the gatekeeper is highly available.

**Hard contraindications.** Reject the claim when the gatekeeper would become the only
authorization check; when it forwards unchecked identity or tenant headers; when its
outage blocks all access; when validation logic needs backend domain state.

**Competing alternative.** Backend-side validation and authorization, or an API gateway
with a narrow policy. Reverse the choice when gatekeeper complexity and blast radius
exceed the reduced attack surface.

**Failure and recovery.** The gatekeeper can be a single point of failure (SPoF);
to minimize the impact, consider deploying redundant instances and using autoscaling
to ensure capacity and availability. Redundancy does not repair a stale policy or an
undeclared direct path; stale-policy and bypass checks remain separate acceptance
conditions.

**Technical owner.** [Authorization boundaries and multitenancy: domain ownership and isolation](../../v02-application-boundaries-and-contracts/c07-authorization-boundaries-and-multitenancy/authorization-boundaries-and-multitenancy.md#gatekeeper) — authorization boundary; gatekeeper mechanics are bounded to the linked section.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-gatekeeper.2026-10-21: all nine served headings
read. Failure and recovery uses the SPoF and redundant-instance advice
in "Problems and considerations"; the stale-policy and bypass checks are
Tycho acceptance conditions. Served page SHA-256
`5af11b967b9ffe814df508afa3f4cd4d3797bdb6f280b78d1be61db8a53a28f0`. Vendor
pattern page, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** API Gateway; Gateway Offloading; Zero Trust Architecture; Valet
Key.
