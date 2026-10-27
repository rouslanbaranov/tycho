---
metadata_version: 1
id: "tycho.chapter.419769c372ccaa569796954878e3bef9"
kind: "chapter"
parent_id: "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
canonical_path: "book/volumes/v11-pattern-atlas/c11-security-operations/README.md"
title: "V11/C11 — Security, isolation and operational architecture"
topic_ids:
  - "security-architecture"
  - "observability"
perspectives:
  - "architecture"
  - "security"
  - "operations"
summary: "All 13 C11 cards with bounded owner links; decision coverage partial."
route_hints:
  questions:
    - "Which security and operational patterns enforce the trust boundary?"
  prerequisites:
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
  related_ids:
    - "tycho.volume.fe327f72cf81df0237ce47b841e8aef5"
    - "tycho.chapter.b20625a099bc4c82b7d547c32c7da28a"
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
    - "tycho.chapter.bee261b76181706235dd8fa7ccde01a9"
  excludes:
    - "Bounded owner links; no sufficient coverage or independent review."
  keywords:
    - "pattern atlas"
    - "security isolation and operations"
    - "decision layer"
evidence_scope:
  source_ids:
    - "src.oauth-security"
    - "src.owasp-asvs"
    - "src.istio"
    - "src.microsoft-cloud-patterns"
    - "src.otel"
    - "src.openlineage"
    - "src.sre"
    - "src.sre-workbook"
    - "src.kubernetes"
  claim_ids: []
  status: "source-linked"
  notes: "13 cards cite read units; owner links are bounded."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-26"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-26"
source_inspection_date: "2026-10-26"
content_verified_at: null
---
# V11/C11 — Security, isolation and operational architecture

**Owning question:** Which security and operational patterns enforce the trust boundary?

## Purpose and mission

This chapter is the atlas entry point for **Security, isolation and operational
architecture**. It owns the conditional decision route for 13 catalog entries, not the
deep mechanism explanations. Read the exact owner section before applying a mechanism
claim.

All 13 entries have a self-checked card. Owner sections are bounded: an identity,
logging or SLO page may own the trust/evidence contract without owning every pattern.

## Pages and reasoning route

Page count is content-dependent. This chapter currently uses one landing page for all
entries; a later split is an editorial change, not a plan failure. Start with the card,
check its conditions and contraindications, then read the exact owner section.

## Entry inventory

Each level-three heading is a stable atlas anchor. Owner links are bounded sections;
none claims sufficient technical or decision coverage.

### Federated Identity

See the [dedicated Federated Identity card](federated-identity.md).
### Zero Trust Architecture

See the [dedicated Zero Trust Architecture card](zero-trust-architecture.md).
### Least Privilege

See the [dedicated Least Privilege card](least-privilege.md).
### RBAC / ABAC

See the [dedicated RBAC / ABAC card](rbac-abac.md).
### Workload Identity / mTLS

See the [dedicated Workload Identity / mTLS card](workload-identity-mtls.md).
### Valet Key

See the [dedicated Valet Key card](valet-key.md).

### Multitenant Isolation

See the [dedicated Multitenant Isolation card](multitenant-isolation.md).
### Distributed Tracing

See the [dedicated Distributed Tracing card](distributed-tracing.md).
### Structured Logging

See the [dedicated Structured Logging card](structured-logging.md).
### Audit Trail

See the [dedicated Audit Trail card](audit-trail.md).
### SLI / SLO and Error Budgets

See the [dedicated SLI / SLO and Error Budgets card](sli-slo-and-error-budgets.md).
### Synthetic Monitoring

See the [dedicated Synthetic Monitoring card](synthetic-monitoring.md).
### Health, Readiness and Liveness Checks

See the [dedicated Health, Readiness and Liveness Checks card](health-readiness-and-liveness-checks.md).
## Chapter result and counterexample

Thirteen cards establish a conditional decision route. Owner sections are bounded; none
establishes technical sufficiency.

Counterexample: a gateway that authenticates a caller but forwards an unchecked tenant
header is not evidence for the zero-trust card's enforcement conditions.

## Navigation and prerequisites

- Parent: [V11](../README.md).
- Previous: [V11/C10](../c10-deployment-modernization/README.md).
- Prerequisite: V10/C03 — pattern applicability and contraindications.
- Registry: [pattern registry](../../../../edition/patterns/registry.v1.json).
- Card batch: [card batches](../../../../edition/patterns/card-batches.v1.json).
- Coverage map: [candidate coverage](../../../../edition/patterns/coverage-map.v1.json).

## Evidence and known limits

- All 13 cards cite read ledger units; owner links and backlinks are self-checked.
- Owner links are bounded sections, not dedicated pattern pages.
- No entry claims sufficient technical or decision coverage.
- No independent editorial review, benchmark, production observation or runtime test
  is asserted.
