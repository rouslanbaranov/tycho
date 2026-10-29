---
metadata_version: 1
id: "tycho.page.6023770f1256fc30b9784e10d312a3da"
kind: "page"
parent_id: "tycho.chapter.419769c372ccaa569796954878e3bef9"
canonical_path: "book/volumes/v11-pattern-atlas/c11-security-operations/least-privilege.md"
title: "Least Privilege"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
summary: "Decision card for Least Privilege; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should each identity and workload hold only the permissions needed?"
  prerequisites:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  related_ids:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed."
  keywords:
    - "pattern atlas"
    - "least-privilege"
evidence_scope:
  source_ids:
    - "src.owasp-asvs"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; alternative binding and revision remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-27"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-29"
content_verified_at: null
---
# Least Privilege

**Identity.** Least Privilege; family Security, isolation and operational architecture;
kind security-pattern; priority core.

**Decision question.** Should each identity and workload hold only the permissions needed
for its current task?

**Good-fit conditions.** Permissions are enumerable; scope is time/task-bound; revocation
is possible; audit exists.

**Hard contraindications.** Reject when broad permissions are unavoidable for a bounded
migration, when no owner can review scope, or when least privilege would block recovery.

**Competing alternative.** Dual control: when no narrow role can express the task, keep a
task-capable identity and require independent approval by more than one principal before a
high-value action executes, instead of splitting the entitlement. ASVS 5.0.0 requirement
2.3.5 names multi-user approval for high-value business logic flows; using it in place of
narrower entitlements is a Tycho decision inference, not an ASVS comparison. Reverse the
choice when approval latency or approver availability would block a time-critical or
automated action, or when approvals become routine.

**Failure and recovery.** Permission creep and orphaned grants are common; verify review
in the owner section.

**Technical owner.** [Authorization policy and least privilege](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/authorization-policy-and-least-privilege.md#least-privilege) — permission scope and review cadence are bounded; entitlement catalogue is platform-specific.

**Sources.** [src.owasp-asvs](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-asvs.2026-10-21: full 120-page ASVS 5.0.0 PDF read;
V1-V17 and appendices A-E. The alternative is bound in the owner unit to requirement 2.3.5;
the pinned PDF SHA-256 is
`a2fa1bbe38f12cac86d3a0f0023327e9772201f65a7f741f282f5e785d268fc5`
(reverified 2026-10-29). The source is a public specification unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** RBAC / ABAC; Zero Trust; Valet Key; Multitenant Isolation.
