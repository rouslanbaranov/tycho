---
metadata_version: 1
id: "tycho.page.77e5d6cab6c083335efb7fc74b423809"
kind: "page"
parent_id: "tycho.chapter.419769c372ccaa569796954878e3bef9"
canonical_path: "book/volumes/v11-pattern-atlas/c11-security-operations/synthetic-monitoring.md"
title: "Synthetic Monitoring"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
summary: "Decision card for Synthetic Monitoring; four bound public units and explicit limits."
route_hints:
  questions:
    - >-
      Should probes exercise user-visible behavior from outside the service
      rather than rely only on internal metrics?
  prerequisites:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  related_ids:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed."
  keywords:
    - "pattern atlas"
    - "synthetic-monitoring"
evidence_scope:
  source_ids:
    - "src.sre"
    - "src.prometheus"
    - "src.aws-cloudwatch-synthetics"
    - "src.azure-app-insights-availability"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Four public units inspected 2026-10-31: Google SRE, "Monitoring
    Distributed Systems"; Prometheus, "Blackbox exporter"; AWS, "Synthetic
    monitoring (canaries)"; and Azure, "Application Insights availability
    tests". The Azure source id is proposed pending registration. No
    promotion, sufficient coverage or owner acceptance is claimed.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-27"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# Synthetic Monitoring

**Identity.** Synthetic Monitoring; family Security, isolation and operational
architecture; kind operations-pattern; priority core.

**Decision question.** Should probes exercise user-visible behavior from outside the
service rather than rely only on internal metrics?

**Good-fit conditions.** A representative journey can be probed; coverage/locations are
known; false positives are triaged. The probe identity, target, locations, frequency and
success criteria should be explicit. These are Tycho conditions.

**Hard contraindications.** Reject when probes cannot authenticate safely, when they test
only shallow endpoints, or when alert noise exceeds signal. These are Tycho
contraindications.

**Competing alternative.** Real-user monitoring or internal SLOs. Reverse the choice when
synthetic coverage cost exceeds detection benefit. Google SRE contrasts black-box with
white-box monitoring; Azure directs operators of "nonpublic endpoints" to "monitor an
internal health signal from inside the network and create log or metric alerts on that
signal." **Tycho choice rule:** prefer a synthetic probe only when no real traffic
exercises the journey; prefer internal or real-user signals when the probe cannot reach
or safely authenticate to the path.

**Failure and recovery.** Azure retries a failed availability test and reports "only if
three successive attempts fail", while noting that "about 80% of failures disappear on
retry"; AWS says canaries let you "discover issues before your customers do"; Prometheus
exposes `probe_success` and debug output. Probe blindness and credential leakage are
common; verify journey coverage in the owner section. **Tycho runbook:** page on
product-visible failure, keep credential-expiry alerts distinct from product alerts, and
re-run with debug before declaring an outage.

**Technical owner.** [Burn-rate and alerts are actions, not decorations](../../v09-observability-security-and-operations/c01-slis-slos-and-error-budgets/budget-actions.md#synthetic-monitoring) — synthetic monitoring is bounded to alert/action reasoning.

**Sources.** Google SRE, "Monitoring Distributed Systems"
(`read.sre-book-blackbox-monitoring.2026-10-31`); Prometheus, "Blackbox exporter"
(`read.prometheus-blackbox-exporter.2026-10-31`); AWS, "Synthetic monitoring
(canaries)" (`read.aws-synthetics-canaries.2026-10-30`, retained); and Azure,
"Application Insights availability tests"
(`read.azure-app-insights-availability.2026-10-31`, proposed). All four are public
documentation, not benchmarks or production observations; exact URLs, revisions and
quotes are in the lane note and owner section. No probe, canary or availability test
was run.

**Decision state.** applicable-under-conditions.

**Related entries.** SLI/SLO; Health Checks; Incident Response; Alerting.
