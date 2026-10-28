---
metadata_version: 1
id: "tycho.page.cd2585308f28ccb08b55c4b00e42925b"
kind: "page"
parent_id: "tycho.chapter.419769c372ccaa569796954878e3bef9"
canonical_path: "book/volumes/v11-pattern-atlas/c11-security-operations/federated-identity.md"
title: "Federated Identity"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
summary: "Decision card for Federated Identity; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should identity be asserted by a trusted issuer and accepted across"
  prerequisites:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  related_ids:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed."
  keywords:
    - "pattern atlas"
    - "federated-identity"
evidence_scope:
  source_ids:
    - "src.oauth-security"
    - "src.openid-federation"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; source binding remains in the owner unit."
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
# Federated Identity

**Identity.** Federated Identity; family Security, isolation and operational architecture;
kind security-pattern; priority core.

**Decision question.** Should trust be mediated by a multilateral federation rather than bilateral
direct trust?

**Good-fit conditions.** A federation authority can mediate trust; entities publish signed Entity
Statements; access tokens are audience-bound.

**Hard contraindications.** Reject when no federation authority exists and bilateral direct trust
is impractical.

**Competing alternative.** Bilateral direct trust between two organizations when multilateral
mediation is impractical.

**Failure and recovery.** Entity Configuration expiration controls federation key refresh;
expired metadata must be refreshed.

**Technical owner.** [Identity and workload trust](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/identity-authorization-and-isolation.md#federated-identity) — federation trust and token validation are bounded; IdP lifecycle is owner-specific.

**Sources.** [src.oauth-security](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-rfc9700.2026-10-21: all 78 numbered sections read;
the prior 100,000-character truncation is superseded.
[src.openid-federation](../../../../edition/patterns/reading-ledger.v1.json)
read record read.openid-federation.2026-10-26: all 25 top-level sections and
199 headings read. OpenID Federation supports trust anchors, Entity Statements, trust
chains, metadata refresh and key rollover. It defines revocation status data for keys
and trust marks, but no revocation process; federation-specific replay and revocation
mechanics are synthetic, not source claims.
The source is a public pattern/specification unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Zero Trust Architecture; Workload Identity / mTLS; Least Privilege;
RBAC / ABAC.
