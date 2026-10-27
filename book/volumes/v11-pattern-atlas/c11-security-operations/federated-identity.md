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

**Decision question.** Should identity be asserted by a trusted issuer and accepted across
services, rather than locally re-authenticated?

**Good-fit conditions.** Issuer/audience/expiry are validated; federation trust is
explicit; revocation and key rotation are handled.

**Hard contraindications.** Reject when one local identity store suffices, when issuer
trust cannot be established, or when token replay/revocation cannot be controlled.

**Competing alternative.** Local authentication or a gateway-only identity check. Reverse
the choice when federation trust and revocation cost exceed single-sign-on benefit.

**Failure and recovery.** Audience confusion and stale trust are common; verify token
validation in the owner section.

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
