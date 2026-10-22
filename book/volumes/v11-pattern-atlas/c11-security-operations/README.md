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
  reviewed_at: "2026-10-21"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-21"
updated_at: "2026-10-21"
source_inspection_date: "2026-10-21"
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

**Technical owner.** [Identity and workload trust](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/identity-authorization-and-isolation.md#federated-identity) — identity/authorization is bounded, not a complete security control catalogue.

**Sources.** [src.oauth-security](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-rfc9700.2026-10-21: sections "Token Handling", "Redirect URI",
"PKCE", "Sender-Constrained Tokens". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Zero Trust Architecture; Workload Identity / mTLS; Least Privilege;
RBAC / ABAC.

### Zero Trust Architecture

**Identity.** Zero Trust Architecture; family Security, isolation and operational
architecture; kind security-pattern; priority core.

**Decision question.** Should every access be authenticated and authorized at the
resource, rather than trusted because it is inside a network?

**Good-fit conditions.** Resource-level policy is enforceable; identity is strong;
telemetry is available; legacy paths can be segmented.

**Hard contraindications.** Reject when a trusted local boundary is genuinely sufficient,
when policy enforcement cannot reach the resource, or when the migration would break
critical flows.

**Competing alternative.** Perimeter security with explicit compensating controls. Reverse
the choice when zero-trust policy complexity exceeds the trust-boundary risk.

**Failure and recovery.** Policy gaps, legacy bypasses and identity-provider outages are
common; deny by default, test indirect paths and keep a bounded audited break-glass path.

**Technical owner.** [Authorization policy and least privilege](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/authorization-policy-and-least-privilege.md#zero-trust-architecture) — identity/authorization is bounded, not a complete security control catalogue.

**Sources.** [src.owasp-asvs](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-asvs.2026-10-21: sections "Application Security Verification
Standard", "Verification Requirements", "Levels". The source is a public
pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Federated Identity; Least Privilege; RBAC / ABAC; Workload Identity /
mTLS.

### Least Privilege

**Identity.** Least Privilege; family Security, isolation and operational architecture;
kind security-pattern; priority core.

**Decision question.** Should each identity and workload hold only the permissions needed
for its current task?

**Good-fit conditions.** Permissions are enumerable; scope is time/task-bound; revocation
is possible; audit exists.

**Hard contraindications.** Reject when broad permissions are unavoidable for a bounded
migration, when no owner can review scope, or when least privilege would block recovery.

**Competing alternative.** Role-based broad access with monitoring. Reverse the choice
when permission granularity creates unmanageable operational overhead.

**Failure and recovery.** Permission creep and orphaned grants are common; verify review
in the owner section.

**Technical owner.** [Authorization policy and least privilege](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/authorization-policy-and-least-privilege.md#least-privilege) — identity/authorization is bounded, not a complete security control catalogue.

**Sources.** [src.owasp-asvs](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-asvs.2026-10-21: sections "Application Security Verification
Standard", "Verification Requirements". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** RBAC / ABAC; Zero Trust; Valet Key; Multitenant Isolation.

### RBAC / ABAC

**Identity.** RBAC / ABAC; family Security, isolation and operational architecture; kind
security-pattern; priority core.

**Decision question.** Should access be decided by roles or attributes rather than ad hoc
checks?

**Good-fit conditions.** A policy model exists; roles/attributes have owners; decisions
are auditable; conflicts are resolved.

**Hard contraindications.** Reject when access is purely static and tiny, when attributes
are untrusted, or when policy complexity cannot be tested.

**Competing alternative.** Direct capability checks or a simpler role model. Reverse the
choice when policy administration cost exceeds access-control benefit.

**Failure and recovery.** Role explosion and stale attributes are common; verify model in
the owner section.

**Technical owner.** [Authorization policy and least privilege](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/authorization-policy-and-least-privilege.md#rbac-abac) — identity/authorization is bounded, not a complete security control catalogue.

**Sources.** [src.owasp-asvs](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-asvs.2026-10-21: sections "Application Security Verification
Standard", "Verification Requirements". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Least Privilege; Zero Trust; Multitenant Isolation; Federated
Identity.

### Workload Identity / mTLS

**Identity.** Workload Identity / mTLS; family Security, isolation and operational
architecture; kind security-pattern; priority advanced.

**Decision question.** Should workloads authenticate each other with cryptographic
identities rather than network location?

**Good-fit conditions.** A workload identity issuer exists; certificate rotation is
automated; policy can bind identity to service.

**Hard contraindications.** Reject when network location is the only available identity,
when rotation cannot be automated, or when identity sprawl is unowned.

**Competing alternative.** Network policy plus service accounts, or a gateway boundary.
Reverse the choice when mTLS operational cost exceeds lateral-movement risk.

**Failure and recovery.** Certificate expiry and identity mismatch are common; verify
rotation in the owner section.

**Technical owner.** [Identity and workload trust](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/identity-authorization-and-isolation.md#workload-identity-mtls) — identity/authorization is bounded, not a complete security control catalogue.

**Sources.** [src.istio](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-istio.2026-10-21: sections "Workload Identity", "Mutual TLS",
"Authorization". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Zero Trust; Federated Identity; Least Privilege; Service Mesh.

### Valet Key

**Identity.** Valet Key; family Security, isolation and operational architecture; kind
security-pattern; priority advanced.

**Decision question.** Should a client receive a scoped, time-limited credential for
direct resource access?

**Good-fit conditions.** The resource can issue scoped tokens; expiry/revocation are
enforced; the client cannot escalate scope.

**Hard contraindications.** Reject when every access must be mediated, when the resource
cannot enforce scope, or when token leakage would be catastrophic.

**Competing alternative.** Mediated access through a gateway or backend. Reverse the
choice when direct access offload is not worth credential risk.

**Failure and recovery.** Token leakage and scope confusion are common; verify boundaries
in the owner section.

**Technical owner.** [Token and credential boundaries](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/object-credentials.md#valet-key) — object credentials are bounded, not a complete key-management guide.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-valet.2026-10-21: sections "Valet Key pattern", "Context and
problem", "Solution". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Least Privilege; Federated Identity; Object Credentials; API Gateway.

### Multitenant Isolation

**Identity.** Multitenant Isolation; family Security, isolation and operational
architecture; kind security-pattern; priority core.

**Decision question.** Should tenants be isolated in compute, data, identity and network
layers rather than share one trusted pool?

**Good-fit conditions.** Tenant identity is trustworthy; isolation can be enforced at each
layer; noisy-neighbor and data-leak risks are material.

**Hard contraindications.** Reject when one tenant exists, when isolation would strand
capacity, or when the resource cannot enforce tenant scope.

**Competing alternative.** Shared pool with per-tenant authorization and quotas. Reverse
the choice when isolation cost exceeds residual risk.

**Failure and recovery.** Cross-tenant leakage and quota bypass are common; verify layers
in the owner section.

**Technical owner.** [Multitenant isolation](../../v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/multitenant-isolation.md#multitenant-isolation) — identity/authorization is bounded, not a complete security control catalogue.

**Sources.** [src.owasp-asvs](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-asvs.2026-10-21: sections "Application Security Verification
Standard", "Verification Requirements". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Zero Trust; Least Privilege; Tenant-Based Resource Isolation;
Cell-Based Architecture.

### Distributed Tracing

**Identity.** Distributed Tracing; family Security, isolation and operational
architecture; kind observability-pattern; priority core.

**Decision question.** Should requests carry a trace context so spans across services can
be correlated?

**Good-fit conditions.** Context propagation is possible; sampling policy is explicit;
sensitive data is excluded; storage/retention are owned.

**Hard contraindications.** Reject when one service suffices, when context cannot cross a
boundary, or when trace data would leak sensitive payloads.

**Competing alternative.** Structured logs with request IDs. Reverse the choice when
cross-service latency diagnosis justifies trace infrastructure.

**Failure and recovery.** Broken context and sampling bias are common; verify propagation
in the owner section.

**Technical owner.** [Distributed tracing: context propagation, sampling and causal limits](../../v09-observability-security-and-operations/c03-distributed-tracing-and-propagation/distributed-tracing-context-and-sampling.md#purpose-and-mission) — tracing is bounded, not an SDK implementation.

**Sources.** [src.otel](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-otel-traces.2026-10-21: sections "Traces", "Spans", "Context
Propagation", "Sampling". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Structured Logging; Audit Trail; SLI/SLO; Sampling.

### Structured Logging

**Identity.** Structured Logging; family Security, isolation and operational architecture;
kind observability-pattern; priority core.

**Decision question.** Should logs be emitted as structured events with stable fields
rather than free text?

**Good-fit conditions.** Fields are stable; redaction is defined; retention/cost are
owned; correlation IDs are available.

**Hard contraindications.** Reject when logs contain unredactable sensitive data, when
schema churn is unowned, or when volume overwhelms storage.

**Competing alternative.** Metrics/traces or minimal audit events. Reverse the choice when
structured logging cost exceeds diagnostic benefit.

**Failure and recovery.** PII leakage and schema drift are common; verify redaction in the
owner section.

**Technical owner.** [Structured logging, authoritative audit and data lineage](../../v09-observability-security-and-operations/c04-logging-audit-and-lineage/logs-audit-and-data-lineage.md#structured-logging) — logging/audit is bounded, not a logging platform manual.

**Sources.** [src.otel](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-otel-logs.2026-10-21: sections "Logs", "Log Records",
"Attributes", "Correlation". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Distributed Tracing; Audit Trail; OpenLineage; Retention.

### Audit Trail

**Identity.** Audit Trail; family Security, isolation and operational architecture; kind
observability-pattern; priority core.

**Decision question.** Should security-relevant actions be recorded in an append-only,
attributable log?

**Good-fit conditions.** The audited events are defined; identity/time/source are
captured; retention and access are controlled.

**Hard contraindications.** Reject when logs are mutable/deletable by the actor, when
events cannot be attributed, or when audit data is excessive/unused.

**Competing alternative.** Application logs with stricter retention or external SIEM.
Reverse the choice when audit completeness cannot be evidenced.

**Failure and recovery.** Tampering and missing events are common; verify authority in the
owner section.

**Technical owner.** [Structured logging, authoritative audit and data lineage](../../v09-observability-security-and-operations/c04-logging-audit-and-lineage/logs-audit-and-data-lineage.md#engineering-walkthrough-one-approved-business-change-three-incompatible-records) — logging/audit is bounded, not a logging platform manual.

**Sources.** [src.openlineage](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-openlineage.2026-10-21: sections "About OpenLineage", "Events",
"Namespaces and Datasets". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Structured Logging; Distributed Tracing; Least Privilege; Retention.

### SLI / SLO and Error Budgets

**Identity.** SLI/SLO and Error Budgets; family Security, isolation and operational
architecture; kind operations-pattern; priority core.

**Decision question.** Should service health be governed by user-visible indicators,
objectives and an explicit error budget?

**Good-fit conditions.** An SLI measures a meaningful journey; SLO target/window are
agreed; error budget drives action.

**Hard contraindications.** Reject when metrics are not user-visible, when targets are
arbitrary, or when budget breach has no consequence.

**Competing alternative.** Synthetic checks or raw infrastructure metrics alone. Reverse
the choice when measurement cost exceeds decision value.

**Failure and recovery.** Gaming and window mismatch are common; verify decisions in the
owner section.

**Technical owner.** [User-visible service indicators, objectives and error-budget decisions](../../v09-observability-security-and-operations/c01-slis-slos-and-error-budgets/service-level-indicators-objectives-and-alerts.md#engineering-walkthrough-what-does-a-green-slo-say-about-rejected-business-operations) — SLOs are bounded, not a complete measurement system.

**Sources.** [src.sre](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-sre-slo.2026-10-21: sections "Service Level Objectives",
"Indicators", "Objectives", "Error Budgets". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Synthetic Monitoring; Alerting; Incident Response; Health Checks.

### Synthetic Monitoring

**Identity.** Synthetic Monitoring; family Security, isolation and operational
architecture; kind operations-pattern; priority advanced.

**Decision question.** Should probes exercise user-visible behavior from outside the
service rather than rely only on internal metrics?

**Good-fit conditions.** A representative journey can be probed; coverage/locations are
known; false positives are triaged.

**Hard contraindications.** Reject when probes cannot authenticate safely, when they test
only shallow endpoints, or when alert noise exceeds signal.

**Competing alternative.** Real-user monitoring or internal SLOs. Reverse the choice when
synthetic coverage cost exceeds detection benefit.

**Failure and recovery.** Probe blindness and credential leakage are common; verify
journey coverage in the owner section.

**Technical owner.** [Burn-rate and alerts are actions, not decorations](../../v09-observability-security-and-operations/c01-slis-slos-and-error-budgets/budget-actions.md#synthetic-monitoring) — synthetic monitoring is bounded to alert/action reasoning.

**Sources.** [src.sre-workbook](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch6-sre-workbook-monitoring.2026-10-21: sections "Monitoring Systems
with Advanced Analytics", "Synthetic Monitoring", "Alerting". The source is a public
pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** SLI/SLO; Health Checks; Incident Response; Alerting.

### Health, Readiness and Liveness Checks

**Identity.** Health, Readiness and Liveness Checks; family Security, isolation and
operational architecture; kind operations-pattern; priority core.

**Decision question.** Should the runtime distinguish process liveness, traffic readiness
and startup completion?

**Good-fit conditions.** Probes have different failure meanings; dependencies are not
conflated; restart/traffic removal are separate.

**Hard contraindications.** Reject when one probe is used for every failure, when a
liveness probe restarts healthy processes on a shared dependency, or when startup is
ignored.

**Competing alternative.** External journey monitoring plus process supervision. Reverse
the choice when probe complexity causes false restarts.

**Failure and recovery.** False positives and shared-dependency coupling are common;
verify semantics in the owner section.

**Technical owner.** [Practice response before production failure](../../v09-observability-security-and-operations/c06-incident-response-and-operational-change/incident-practice.md#health-readiness-and-liveness-checks) — health checks are bounded to recovery readiness.

**Sources.** [src.kubernetes](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-k8s-probes.2026-10-21: sections "Liveness", "Readiness",
"Startup". The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Synthetic Monitoring; Failover/Failback; Incident Response; SLI/SLO.

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
