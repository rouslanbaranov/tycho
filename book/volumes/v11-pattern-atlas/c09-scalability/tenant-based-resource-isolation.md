---
metadata_version: 1
id: "tycho.page.bd9428f9bf6044048c48eb0aa67d1e3f"
kind: "page"
parent_id: "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
canonical_path: "book/volumes/v11-pattern-atlas/c09-scalability/tenant-based-resource-isolation.md"
title: "Tenant-Based Resource Isolation"
topic_ids:
  - "scaling-mechanisms"
  - "security-architecture"
perspectives:
  - "architecture"
  - "operations"
summary: >-
  Decision card for Tenant-Based Resource Isolation; source-anchored on AWS SaaS
  Lens tenant, pool and serverless isolation, Kubernetes multi-tenancy,
  PostgreSQL row security and Microsoft multitenant approaches; coverage remains
  partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should tenants receive isolated compute/data/networking quotas rather than
      share one unbounded pool?
  prerequisites:
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
  related_ids:
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "tenant-based resource isolation"
    - "scalability and load distribution"
evidence_scope:
  source_ids:
    - "src.aws-saas-lens"
    - "src.kubernetes"
    - "src.postgresql"
    - "src.microsoft-multitenant"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.aws-saas-lens-tenant-isolation.2026-10-31,
    read.aws-saas-lens-pool-isolation.2026-10-31,
    read.aws-saas-lens-preventing-cross-tenant.2026-10-31,
    read.k8s-multitenancy.2026-10-31, read.postgres-rowsecurity.2026-10-31 and
    read.ms-multitenant-approaches.2026-10-31; read.batch5-ms-multitenant.2026-10-21
    is retained Deployment Stamps context; owner section and limits are bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-31"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# Tenant-Based Resource Isolation

**Identity.** Tenant-Based Resource Isolation; family Scalability and load distribution;
kind scalability-pattern; priority core.

**Decision question.** Should tenants receive isolated compute/data/networking quotas
rather than share one unbounded pool?

**Good-fit conditions.** Tenant identity is known; noisy-neighbor risk is material;
quotas/isolation can be enforced and observed.

**Hard contraindications.** Reject when one tenant exists, when isolation would strand
most capacity, or when quotas cannot be enforced at the resource.

**Competing alternative.** Shared pool with per-tenant rate limits, or a dedicated deployment stamp.
Reverse the choice when isolation cost exceeds noisy-neighbor risk.

**Failure and recovery.** Quota bypass, shared-storage reuse, row-security bypass and cross-tenant
cache or worker leaks are the common failures; deny network paths by default, set a `Delete` reclaim
policy for shared storage classes, force row security where the tenant is the database principal,
scope keys and workers by tenant, and test indirect paths with a foreign identifier in the owner
section.

**Technical owner.** [Multitenant isolation](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/multitenant-isolation.md#tenant-based-resource-isolation) — compute, storage, quota, query and credential boundaries are bounded to public guidance, not a full control catalogue.

**Sources.** AWS Well-Architected SaaS Lens (*Tenant isolation*, *Pool isolation*,
*Preventing cross tenant access*), Kubernetes *Multi-tenancy*, PostgreSQL 18.6 *Row Security
Policies* and Microsoft Learn *Architectural approaches for a multitenant solution* were read
on 2026-10-31. Read records: `read.aws-saas-lens-tenant-isolation.2026-10-31`,
`read.aws-saas-lens-pool-isolation.2026-10-31`,
`read.aws-saas-lens-preventing-cross-tenant.2026-10-31`, `read.k8s-multitenancy.2026-10-31`,
`read.postgres-rowsecurity.2026-10-31` and `read.ms-multitenant-approaches.2026-10-31`.
Source ids: `src.aws-saas-lens`, `src.kubernetes`,
`src.postgresql` and `src.microsoft-multitenant`. The sources are public
documentation, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Cell-Based Architecture; Rate Limiting; Bulkhead; Multitenant
Isolation.

**Limits.** Coverage is partial-bounded and self-checked, not independent review, promotion
or owner acceptance. The cache/worker and queue scoping rules, the quota-enforcement test
and the runbook are Tycho synthesis; no cross-tenant test, benchmark or failure drill was run.