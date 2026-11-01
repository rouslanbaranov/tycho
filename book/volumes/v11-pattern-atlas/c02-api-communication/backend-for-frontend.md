---
metadata_version: 1
id: "tycho.page.6b75e10be102574cdc7351525ebabac9"
kind: "page"
parent_id: "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
canonical_path: "book/volumes/v11-pattern-atlas/c02-api-communication/backend-for-frontend.md"
title: "Backend for Frontend (BFF)"
topic_ids:
  - "application-architecture"
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Backend for Frontend (BFF); bounded owner evidence and
  explicit limits.
route_hints:
  questions:
    - >-
      Should each client population get a tailored server contract, rather
      than share one general-purpose API?
  prerequisites:
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  related_ids:
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "backend for frontend"
    - "client experience"
evidence_scope:
  source_ids:
    - "src.microsoft-cloud-patterns"
    - "src.microservices-patterns"
    - "src.aws-bff"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
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
# Backend for Frontend (BFF)

**Identity.** Backend for Frontend; alias BFF; family API and service communication;
kind integration pattern; priority core.

**Decision question.** Should each client population get a tailored server contract,
rather than share one general-purpose API?

**Good-fit conditions.** The BFF composes several owner APIs for one client experience;
client populations have materially different interaction needs; a team can own each
BFF; shared domain services remain authoritative; duplicated client-specific composition
is acceptable; cross-cutting policy stays outside the BFF.

**Hard contraindications.** Reject the claim when one client contract is adequate; when
BFFs would duplicate domain logic; when no team owns a BFF lifecycle; when the split
multiplies deployments without a measured client benefit.

**Competing alternative.** A shared API with client-side selection when the differences
are small. Reverse the choice when BFF maintenance and duplication exceed the client fit
benefit.

**Failure and recovery.** The pages document per-client malfunction isolation and
independent service lifecycles; they do not document drift, composition versioning or
client-contract tests. Tycho reading: independent BFF and domain-service lifecycles
create release-alignment risk. Tycho guidance, not a source claim: treat BFF/domain
divergence as drift, version the composition and test the client contract; verify the
API contract boundary in the owner section.

**Technical owner.** [HTTP and RPC contracts: compatibility, deadlines and retry safety](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/http-rpc-contracts-and-compatibility.md#backend-for-frontend-bff) — BFF tailoring has a dedicated owner section; it is bounded, not a complete API contract guide.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
record `read.microsoft-bff.2026-10-30` (supersedes
`read.microsoft-bff.2026-10-21`): sections "Solution" and "Problems and
considerations"; canonical revision
`0210c2a7732bf3e43621e28c82c284f78fe7f9e02ef2a50328b9d44bcebd353f`.
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
record `read.microservices-api-gateway.2026-10-21`, section "Variation: Backends for
frontends"; raw revision
`e94bf7ae68567226222138dc2836247873d5908b63bf07ca05207377a9999d4d`.
[src.aws-bff](../../../../edition/patterns/reading-ledger.v1.json) record
`read.aws-bff.2026-10-30`, section "The BFF pattern"; canonical revision
`bfab5e7c99406c982f8bddbe077d4e2d5fc3494c6e7ef6762d82d0f3a746280c`.
Vendor pattern pages and a vendor blog, not a benchmark; exact quotes are in the owner
section.

**Decision state.** applicable-under-conditions.

**Related entries.** API Gateway; Gateway Aggregation; API Composition; Reverse Proxy.
