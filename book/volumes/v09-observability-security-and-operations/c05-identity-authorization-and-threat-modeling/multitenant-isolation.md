---
{
  "metadata_version": 1,
  "id": "tycho.page.1db0a6e1679448e392ee8422eb5a3beb",
  "kind": "page",
  "parent_id": "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2",
  "canonical_path": "book/volumes/v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/multitenant-isolation.md",
  "title": "Multitenant isolation",
  "topic_ids": [
    "security-architecture"
  ],
  "perspectives": [
    "architecture",
    "operations",
    "evaluation"
  ],
  "summary": "How are tenant data and effects kept separate across every access path?",
  "route_hints": {
    "questions": [
      "How are tenant data and effects kept separate across every access path?"
    ],
    "prerequisites": [],
    "related_ids": [
      "tycho.chapter.3563624d13ca4430aa77abea4f8f0bc2"
    ],
    "excludes": [
      "No executed product experiment or independent acceptance is claimed."
    ],
    "keywords": [
      "tenant",
      "isolation",
      "multitenancy",
      "quota",
      "scope"
    ]
  },
  "evidence_scope": {
    "source_ids": [
      "src.owasp-rest-enrichment",
      "src.aws-saas-lens",
      "src.kubernetes",
      "src.postgresql",
      "src.microsoft-multitenant"
    ],
    "claim_ids": [],
    "status": "source-linked",
    "notes": "Tenant-based card binds four public sources read 2026-10-31; self-checked."
  },
  "content_review": {
    "status": "self-checked",
    "reviewed_at": "2026-10-31",
    "reviewer": "Automated authoring agent",
    "proof_uri": null
  },
  "authored_at": "2026-10-22",
  "updated_at": "2026-10-31",
  "source_inspection_date": null,
  "content_verified_at": null
}
---

# Multitenant isolation

**Owning question:** How are tenant data and effects kept separate across every access path?

Tenant isolation is a property of every query, cache key, queue consumer and credential,
not a deployment label. The tenant scope must come from authenticated context and be enforced
centrally. OWASP REST guidance treats object-level authorization as part of access control;
it does not prescribe this isolation design.

> **Pattern atlas:**
> [Multitenant Isolation](../../v11-pattern-atlas/c11-security-operations/multitenant-isolation.md#multitenant-isolation) — decision conditions and contraindications.
> [Tenant-Based Resource Isolation](../../v11-pattern-atlas/c09-scalability/README.md#tenant-based-resource-isolation) — decision conditions and contraindications.

## Tenant-Based Resource Isolation

Tenant-based isolation assigns each tenant a bounded share of compute, storage and quota, with
routing and credentials that keep the tenant scope explicit. No query, cache key, queue consumer
or credential may cross a tenant boundary without an explicit shared-resource contract.

**Bounded share.** Kubernetes treats a namespace as the management unit for a tenant workload, which
"helps segment a tenant's workload into a logical and distinct management unit", and uses
ResourceQuotas so that "a tenant cannot monopolize a cluster's resources or overwhelm its control
plane"; a container's limits are "the upper bound for the amount of resources that a container can
consume". A namespaced PersistentVolumeClaim and a StorageClass bound storage; if a class is shared,
Kubernetes recommends a `Delete` reclaim policy "to ensure that a PersistentVolume cannot be reused
across different namespaces". Azure's multitenant guidance frames the same choice as sharing "every
resource" versus deploying "isolated resources for every tenant" across compute, storage and data,
networking and identity, with trade-offs in scale, isolation, cost and manageability. AWS's
pool-isolation page describes shared storage as "a table indexed by individual tenant identifiers".
**Tycho reading:** the bounded share is a per-resource contract, not a deployment label; a quota
that the resource does not enforce is not isolation.

**Tenant boundary.** AWS's SaaS Lens states that a multi-tenant environment must "ensure that each
tenant is prevented from accessing another tenant's resources" and that "Crossing this boundary in
any form would represent a significant and potentially unrecoverable event". PostgreSQL row security
restricts, "on a per-user basis, which rows can be returned by normal queries or inserted, updated,
or deleted"; if no policy exists it applies "a default-deny policy", and the expression "will be
evaluated for each row prior to any conditions or functions coming from the user's query".
Kubernetes scopes credentials and reachability through RBAC, namespaced NetworkPolicies and
namespaced PersistentVolumeClaims. AWS's serverless pool example exchanges JWT-supplied tenant
context for "tenant-scoped credentials" before storage access. **Tycho rule:** derive the tenant
from authenticated context; require it in every query, cache key, queue consumer and credential;
enforce it centrally and never trust an arbitrary caller field alone. AWS states the boundary
principle but does not enumerate the query, cache, queue and credential paths; PostgreSQL and
Kubernetes bind the query and credential/network paths, and cache/queue scoping remains Tycho
synthesis.

**Leakage and capacity theft.** A shared cache or background worker leaks one tenant's data or
consumes another's capacity; scope keys by tenant and test indirect paths with a foreign identifier.
Kubernetes warns that "Quotas cannot protect against all kinds of resource sharing, such as network
traffic", that a shared StorageClass without a `Delete` reclaim policy can let a volume be "reused
across different namespaces", and that under node isolation the kubelet and API service are "still
shared services" from which an attacker can "move laterally". A compute quota alone therefore does
not bound network effects. AWS's pool-isolation page records the capacity consequence: "The more
resources are shared, the more chances there are for one tenant to impact the experience of
another", and an outage "will likely impact all the tenants"; it asks for an environment that can
"gracefully recover from failures". AWS's shared-function example also warns that the pooled
execution role "does push part of the isolation model into the code". PostgreSQL adds that
superusers and roles with `BYPASSRLS` "always bypass the row security system", that table owners
normally bypass it unless `FORCE ROW LEVEL SECURITY` is set, and that whole-table operations such as
`TRUNCATE` and `REFERENCES` "are not subject to row security"; `row_security = off` makes a query
error when its results would be filtered rather than silently omitting rows. **Tycho runbook:**
default-deny network paths between tenants; scope cache keys and queue partitions by tenant;
partition or dedicate workers; set `Delete` reclaim on shared storage classes; force row security
where the tenant is the database principal; test indirect paths with a foreign tenant identifier;
monitor per-tenant consumption; fail closed when tenant scope is missing.

**Alternatives.** A shared pool with tenant-scoped predicates is cheaper at low scale; choose
dedicated resources when noisy-neighbour or compliance risk dominates. Azure's Deployment Stamps
guidance says a single-tenant stamp provides "the highest level of isolation and helps to avoid the
noisy neighbor problem", while a multitenant stamp still needs extra patterns and "the noisy
neighbor problem still might occur"; its main drawback is infrastructure cost that "can't be shared
with other tenants". AWS contrasts the shared pool with the silo model, and Kubernetes frames
"Namespace per tenant" against "Virtual control plane per tenant". **Tycho choice rule:** use a
shared pool only when tenant scope is enforced on every path and fairness is observable; move a
tenant to a dedicated stamp when measured noisy-neighbour cost, compliance constraints or a bypass
path dominates the operational saving.

**Bound source limits.** Four public sources (six units) were inspected on 2026-10-31: AWS
Well-Architected SaaS Lens, *Tenant isolation*, *Pool isolation* and *Preventing cross tenant
access*; Kubernetes, *Multi-tenancy*, content commit `56db43a0`; PostgreSQL 18.6, *Row Security
Policies*; and Microsoft Learn, *Architectural approaches for a multitenant solution*. The
Kubernetes page treats "hard" and "soft" multi-tenancy as a spectrum, not a guarantee; PostgreSQL
row security is bypassed by superusers and roles with `BYPASSRLS`, by table owners unless `FORCE ROW
LEVEL SECURITY` is set, and does not apply to `TRUNCATE` or `REFERENCES`; the AWS and Azure pages
are documentation, not measurements. Read records: `read.aws-saas-lens-tenant-isolation.2026-10-31`,
`read.aws-saas-lens-pool-isolation.2026-10-31`,
`read.aws-saas-lens-preventing-cross-tenant.2026-10-31`, `read.k8s-multitenancy.2026-10-31`,
`read.postgres-rowsecurity.2026-10-31` and `read.ms-multitenant-approaches.2026-10-31`. Coverage is
self-checked, not independently reviewed.

**Limits.** Per-tenant quotas, noisy-neighbour isolation and cross-tenant test paths are costs; a
shared pool needs explicit fairness and escape hatches. A shared pool can also strand capacity or
fail to enforce quotas; those are reversal conditions, not deployment details. Dedicated resources
are justified only when measured noisy-neighbour cost exceeds their operational cost.

## Multitenant Isolation

Multitenant isolation keeps tenant data and effects separate inside a shared application by
deriving tenant scope from authenticated context at every access path. The tenant identifier
must be derived from authentication and authorization, never accepted from an arbitrary caller
field alone.

A missing tenant predicate in a query, cache or background task exposes another tenant's
records; test indirect paths and enforce the predicate centrally. A tenant-per-deployment
boundary removes shared-code risk at higher cost; share a deployment only when scoping is
enforced consistently across every path.

**Limits.** Central tenant predicates add coupling and migration cost; a missing predicate in one
background path defeats the shared-deployment saving. Per-tenant encryption, backup and deletion are part of
the isolation contract, not only query predicates.

## Navigation

Parent: [identity chapter](README.md). Previous: [authorization policy](authorization-policy-and-least-privilege.md).
Next: [threat models](threat-identity.md).
