---
metadata_version: 1
id: "tycho.page.77358ffa634cea630d04103c13c58086"
kind: "page"
parent_id: "tycho.chapter.419769c372ccaa569796954878e3bef9"
canonical_path: "book/volumes/v11-pattern-atlas/c11-security-operations/rbac-abac.md"
title: "RBAC / ABAC"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
summary: "Decision card for RBAC / ABAC; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should access be decided by roles or attributes rather than ad hoc"
  prerequisites:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  related_ids:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed."
  keywords:
    - "pattern atlas"
    - "rbac-abac"
evidence_scope:
  source_ids:
    - "src.owasp-asvs"
    - "src.nist-sp-800-162"
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
# RBAC / ABAC

**Identity.** RBAC / ABAC; family Security, isolation and operational architecture; kind
security-pattern; priority core.

**Decision question.** Should access be decided by roles or attributes rather than identity
ACLs?

**Good-fit conditions.** Access requirements are finer than identity ACLs; roles or
attributes are available and can be administered.

**Hard contraindications.** Reject when identity ACLs suffice or when attribute-policy
administration costs more than the access-control benefit.

**Competing alternative.** Object ACLs use identity; RBAC uses roles.

**Decision basis.** The good-fit and rejection conditions are original decision inferences from NIST ACL/RBAC/ABAC comparisons, not normative NIST rules.

**Failure and recovery.** In ACL/IBAC systems, failure to remove or revoke access over time
accumulates privileges.

**Technical owner.** [RBAC-ABAC](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/rbac-abac.md#rbac-abac) — role/attribute model and decision point are bounded; policy administration is platform-specific.

**Sources.** [src.owasp-asvs](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-asvs.2026-10-21: full 120-page ASVS 5.0.0 PDF read;
V1-V17 and appendices A-E.
[src.nist-sp-800-162](../../../../edition/patterns/reading-ledger.v1.json)
read record read.nist-sp-800-162.2026-10-26: full 47-page PDF read; appendices A-B.
ASVS provides verification framing; NIST supports PDP/PEP/PIP/PAP and policy
administration. Revocation mechanics, role explosion and attribute-freshness guidance
remain synthetic. The sources are public standards, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Least Privilege; Zero Trust; Multitenant Isolation; Federated
Identity.
