---
metadata_version: 1
id: "tycho.landing.3870e6370654489c949e098b9acd1840"
kind: "landing"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/security/README.md"
title: "Security architecture and trust-boundary decisions"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
  - "security"
summary: "Reader entry for Security architecture and trust-boundary decisions. Scope includes Canonical book chapters; Routes to adjacent material."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Security architecture and trust-boundary decisions?"
  prerequisites: []
  related_ids:
    - "tycho.page.dde63373c50f4f4a80e727b6e160def5"
    - "tycho.page.0ae1aabac3b64c2f924cc427684bdbab"
    - "tycho.page.6b9a3f5c7bae455ab4f56f151f17b406"
    - "tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9"
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Security"
    - "architecture"
    - "and"
    - "trust-boundary"
    - "decisions"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---

# Security architecture and trust-boundary decisions

## Purpose and mission

Connect authenticated identities, authorization, protected business objects and resource isolation to specific, testable system invariants. Security controls must be verified at the authority where the protected effect occurs, not only at ingress.

## Canonical book chapters

- [Threat boundaries, identity, authorization and service isolation](../volumes/v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/identity-authorization-and-isolation.md) — threat worksheet, authentication versus authorization, policy enforcement, object-level access and multi-tenant boundaries, OAuth token audiences, service identity, failure matrix and original synthetic access-control scenario.
- [Safe agent-accessible knowledge and bounded authority](../volumes/v09-observability-security-and-operations/c07-safety-isolation-and-privacy-in-agent-accessible-services/safe-agent-access-and-knowledge-isolation.md) — V09/C07 untrusted retrieval, least-privilege tools, per-document authorization, citation isolation, privacy and negative tests; conceptual book chapter, not deployed MCP.
- [Security architecture: identity, authorization and isolation][security-detail] —
  detailed canonical chapter behind the V09/C05 overview; it does not replace that overview.

[security-detail]: identity-authorization-threat-models-and-isolation.md

## Routes to adjacent material

- [Audit and trace correctness](../observability/trace-context-lineage-and-audit.md) — why best-effort logs and sampled traces do not replace authoritative audit.
- [Cross-domain modernization and ADRs](../volumes/v10-decision-support-and-modernization/c07-cross-domain-worked-comparisons-and-unresolved-cases/cross-domain-modernization-and-adr-examples.md) — security/isolation constraints as hard architecture gates.
- [Safe release](../delivery/progressive-delivery-and-schema-evolution.md) — policy/config version changes and mixed-version compatibility.

**Status:** original source-linked E14-12 security chapter plus an unreviewed V09/C07 manuscript draft; not a deployed policy, observed threat test, independent audit or proof of complete V09 coverage.
