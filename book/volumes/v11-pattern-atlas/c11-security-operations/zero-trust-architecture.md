---
metadata_version: 1
id: "tycho.page.12f7ef77f1f7271ddf7a1571a72be9a6"
kind: "page"
parent_id: "tycho.chapter.419769c372ccaa569796954878e3bef9"
canonical_path: "book/volumes/v11-pattern-atlas/c11-security-operations/zero-trust-architecture.md"
title: "Zero Trust Architecture"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
summary: "Decision card for Zero Trust Architecture with sufficient owner evidence."
route_hints:
  questions:
    - "Should every access be authenticated and authorized at the resource?"
  prerequisites:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  related_ids:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "No owner acceptance is claimed for this card."
  keywords:
    - "pattern atlas"
    - "zero-trust-architecture"
evidence_scope:
  source_ids:
    - "src.owasp-asvs"
    - "src.nist-sp-800-207"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; source binding remains in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-11-01"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-27"
updated_at: "2026-11-01"
source_inspection_date: "2026-10-21"
content_verified_at: null
---
# Zero Trust Architecture

**Identity.** Zero Trust Architecture; family Security, isolation and operational
architecture; kind security-pattern; priority core.

**Decision question.** Should every access be authenticated and authorized at the
resource, rather than trusted because it is inside a network?

**Good-fit conditions.** Resource-level policy is enforceable; identity is strong;
telemetry is available; legacy paths can be segmented.

**Hard contraindications.** Reject when a trusted local boundary is genuinely sufficient,
when policy enforcement cannot reach the resource, or when the migration would break
critical flows.

**Competing alternative.** Hybrid zero-trust/perimeter operation, network segmentation, VPN or
mTLS-only service identity when legacy enforcement is impossible. Reverse the choice when policy
complexity exceeds the trust-boundary risk; the preference rule is Tycho guidance.

**Failure and recovery.** NIST binds component-failure cascade risk. Tycho guidance: policy gaps,
legacy bypasses and identity-provider outages are possible; deny by default, test indirect paths
and keep a bounded audited break-glass path.

**Technical owner.** [Authorization policy and least privilege](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/authorization-policy-and-least-privilege.md#zero-trust-architecture) — policy enforcement points and trust assumptions are bounded; network architecture is owner-specific.

**Sources.** [src.owasp-asvs](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-asvs.2026-10-21: full 120-page ASVS 5.0.0 PDF read;
V1-V17 and appendices A-E. NIST SP 800-207 (`read.nist-sp-800-207.2026-11-01`)
binds hybrid perimeter operation and component-failure cascade. The sources are public
pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Federated Identity; Least Privilege; RBAC / ABAC; Workload Identity /
mTLS.
