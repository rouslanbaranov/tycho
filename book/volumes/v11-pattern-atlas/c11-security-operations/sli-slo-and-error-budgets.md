---
metadata_version: 1
id: "tycho.page.b8f80e03e8346a4ba26e9d692a38945d"
kind: "page"
parent_id: "tycho.chapter.419769c372ccaa569796954878e3bef9"
canonical_path: >-
  book/volumes/v11-pattern-atlas/c11-security-operations/sli-slo-and-error-budgets.md
title: "SLI / SLO and Error Budgets"
topic_ids:
  - "security-architecture"
perspectives:
  - "architecture"
summary: "Decision card for SLI / SLO and Error Budgets; bounded owner evidence and
explicit limits."
route_hints:
  questions:
    - "Should service health be governed by user-visible indicators,"
  prerequisites:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  related_ids:
    - "tycho.chapter.419769c372ccaa569796954878e3bef9"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed."
  keywords:
    - "pattern atlas"
    - "sli-slo-and-error-budgets"
evidence_scope:
  source_ids:
    - "src.sre"
    - "src.sre-workbook"
    - "src.prometheus"
    - "src.openslo"
  claim_ids: []
  status: "source-linked"
  notes: >-
    2026-10-31 four-dimension binding to Google SRE Workbook, Google SRE Book,
    OpenSLO and Prometheus. src.openslo is proposed; exact records and digests
    are in the lane note and owner section.
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
# SLI / SLO and Error Budgets

**Identity.** SLI/SLO and Error Budgets; family Security, isolation and operational
architecture; kind operations-pattern; priority core.

**Decision question.** Should service health be governed by user-visible indicators,
objectives and an explicit error budget?

**Good-fit conditions.** An SLI measures a ratio of good events to total events; the SLO
target and window are agreed; the error budget drives action. The Workbook states that "the
SLO is a target percentage and the error budget is 100% minus the SLO", and the Book asks
teams to "standardize on common definitions for SLIs." **Tycho condition:** the team can
name the eligible population, the good outcome, the denominator, the window and the action
owner before the first measurement.

**Hard contraindications.** Reject when metrics are not user-visible, when targets are
arbitrary, or when budget breach has no consequence. The Book warns teams to start with
"what your users care about, not what you can measure." **Tycho rule:** a target without an
owner, window or action is a dashboard number, not an SLO.

**Competing alternative.** Synthetic checks or raw infrastructure metrics alone remain a
simpler alternative when the journey is not measurable. For the SLO definition, OpenSLO is a
vendor-agnostic alternative to bespoke per-tool rules: it aims at "a common, vendor–agnostic
approach to tracking and interfacing with SLOs", while "Platform-specific implementation
details are purposefully excluded from the scope of this specification." Prometheus recording
and alerting rules are the executable alternative. **Tycho choice rule:** use OpenSLO for
portability; use Prometheus rules for executable queries and alert routing. Reverse when
translation cost exceeds portability benefit or the platform-specific rule is the contract.

**Failure and recovery.** The Workbook defines "Burn rate" as "how fast, relative to the SLO,
the service consumes the error budget" and recommends the "multiwindow, multi-burn-rate
alerting technique." Prometheus supplies `for` and `keep_firing_for` for hysteresis, and
`rule_group_iterations_missed_total` for blind-spot detection. **Tycho runbook:** window
mismatch, flapping alerts and missing evaluations are common; budget breach must trigger a
written action. Alert on user-visible burn, bound alert reset, treat skipped evaluations as a
monitoring gap and execute the budget policy without inventing a retrospective exclusion.

**Technical owner.** [SLI / SLO and Error Budgets](../../v09-observability-security-and-operations/c01-slis-slos-and-error-budgets/service-level-indicators-objectives-and-alerts.md#sli-slo-and-error-budgets) — SLOs are bounded, not a complete measurement system.

**Sources.** Six proposed records, not yet in the
[shared reading ledger](../../../../edition/patterns/reading-ledger.v1.json):

- `read.sre-workbook-implementing-slos.2026-10-31` (src.sre-workbook), sections
  "What to Measure: Using SLIs", "Choosing an Appropriate Time Window" and
  "Establishing an Error Budget Policy"; revision `9e2c7000...`.
- `read.sre-workbook-alerting-on-slos.2026-10-31` (src.sre-workbook), sections
  "Alerting Considerations", "4: Alert on Burn Rate", "6: Multiwindow, Multi-Burn-Rate
  Alerts" and "Conclusion"; revision `2defa7d7...`.
- `read.sre-book-slo.2026-10-31` (src.sre), sections "Indicators", "Objectives",
  "Aggregation", "Standardize Indicators" and "Control Measures"; revision `ef9a19e4...`.
- `read.prometheus-alerting-rules.2026-10-31` (src.prometheus), sections "Defining alerting
  rules", "Inspecting alerts during runtime" and "Sending alert notifications"; revision
  `5c41ec67...`.
- `read.prometheus-recording-rules.2026-10-31` (src.prometheus), sections "Recording rules",
  "Limiting alerts and series" and "Failed rule evaluations due to slow evaluation";
  revision `4b472352...`.
- `read.openslo-specification.2026-10-31` (src.openslo, proposed), sections "Introduction",
  "Specification / Goals", "General Schema" and "Object Types / SLO"; revision
  `0bc001c9...` at source commit `e0259752...`.
The units are public living pages, not benchmarks or production observations. No SLO, alert
rule or monitoring deployment was created or run.

**Decision state.** applicable-under-conditions.

**Related entries.** Synthetic Monitoring; Alerting; Incident Response; Health Checks.
