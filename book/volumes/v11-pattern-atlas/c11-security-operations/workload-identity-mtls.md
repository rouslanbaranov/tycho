---
metadata_version: 1
id: "tycho.page.e18ec327be0da89802c1b579dfbd6044"
kind: "page"
parent_id: "tycho.chapter.419769c372ccaa569796954878e3bef9"
canonical_path: "book/volumes/v11-pattern-atlas/c11-security-operations/workload-identity-mtls.md"
title: "Workload Identity / mTLS"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
summary: "Decision card for Workload Identity / mTLS; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should workloads authenticate each other with cryptographic"
  prerequisites:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  related_ids:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed."
  keywords:
    - "pattern atlas"
    - "workload-identity-mtls"
evidence_scope:
  source_ids:
    - "src.istio"
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
# Workload Identity / mTLS

**Identity.** Workload Identity / mTLS; family Security, isolation and operational
architecture; kind security-pattern; priority core.

**Decision question.** Should workloads authenticate each other with cryptographic
identities rather than network location?

**Good-fit conditions.** A workload identity issuer exists; certificate rotation is
automated; policy can bind identity to service.

**Hard contraindications.** Reject when network location is the only available identity,
when rotation cannot be automated, or when identity sprawl is unowned.

**Competing alternative.** Permissive mTLS mode accepts plaintext and mutual TLS traffic
during migration; use strict mTLS once clients support it.

**Failure and recovery.** Certificate expiry must be monitored; rotate certificates and
keys periodically.

**Technical owner.** [Identity and workload trust](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/identity-authorization-and-isolation.md#workload-identity-mtls) — workload identity binding and mTLS trust are bounded; credential issuance is platform-specific.

**Sources.** [src.istio](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-istio.2026-10-21: all thirty-four served headings read.
The supported subset is: Istio identity; Identity and certificate management;
Authentication; Mutual TLS authentication; Secure naming; Peer authentication;
Authorization; Authorization policies. These support workload identity binding,
certificate rotation, mTLS and authorization policy. Certificate revocation,
trust-root bootstrapping, key storage and lifetime policy are outside those headings
and remain synthetic. The source is official documentation, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Zero Trust; Federated Identity; Least Privilege; Service Mesh.
