---
metadata_version: 1
id: "tycho.page.b2c3d4e5f60718293a4b5c6d7e8f9012"
kind: "page"
parent_id: "tycho.chapter.419769c372ccaa569796954878e3bef9"
canonical_path: "book/volumes/v11-pattern-atlas/c11-security-operations/valet-key.md"
title: "Valet Key"
topic_ids:
  - "security-architecture"
perspectives:
  - "security"
summary: "Should a client receive a scoped, time-limited credential for direct access?"
route_hints:
  questions:
    - "Should a client receive a scoped, time-limited credential for direct resource access?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved card."
  keywords:
    - "pattern atlas"
    - "valet key"
    - "security"
evidence_scope:
  source_ids:
    - "src.microsoft-cloud-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Card cites read.batch6-valet.2026-10-21; owner section is bounded."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-27"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-27"
updated_at: "2026-10-27"
source_inspection_date: "2026-10-21"
content_verified_at: null
---
# Valet Key

**Identity.** Valet Key; family Security, isolation and operational architecture; kind
security-pattern; priority core.

**Decision question.** Should a client receive a scoped, time-limited credential for
direct resource access?

**Good-fit conditions.** Access is limited in scope and duration; the key can be revoked or
disabled.

**Hard contraindications.** Reject when access must be mediated.

**Competing alternative.** Gateway Routing with proxied access to storage.

**Failure and recovery.** A leaked key unlocks the target during its validity period; revoke
or disable it.

**Technical owner.** [Valet Key](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/object-credentials.md#valet-key)
— scoped credential issuance, enforcement and revocation are bounded, not a
key-management guide.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-valet.2026-10-21: all nine served headings read.
The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Least Privilege; Federated Identity; Object Credentials; API Gateway.
