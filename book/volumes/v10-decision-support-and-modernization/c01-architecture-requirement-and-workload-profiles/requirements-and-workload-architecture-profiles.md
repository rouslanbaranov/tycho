---
metadata_version: 1
id: "tycho.page.868027aee4884210bea1d8a6542fbfb0"
kind: "page"
parent_id: "tycho.chapter.289750444f8040d292a474e3876046a1"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c01-architecture-requirement-and-workload-profiles/requirements-and-workload-architecture-profiles.md"
title: "From requirements and workloads to a testable architecture profile"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Integrated question, original scenario and transfer limits for Architecture requirement and workload profiles. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "What inputs are required before comparing candidate patterns?"
  prerequisites: []
  related_ids:
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.0ce5d0aaf63f425ebf556ea97e2d24a9"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.b656116463d9480f83199d8202b127a4"
    - "tycho.page.06b70cb83d4f490ea9ef698a025e7684"
    - "tycho.page.47ffb5c160bd4b10aff27101414c2133"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.page.84fa4a7505904bb2a492be1593690ed2"
    - "tycho.page.4e96abb6d4504ef1b09cbc355485108a"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "From"
    - "requirements"
    - "and"
    - "workloads"
    - "testable"
    - "architecture"
    - "profile"
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
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.868027aee4884210bea1d8a6542fbfb0:-1 -->

# From requirements and workloads to a testable architecture profile

> **Tycho independent technical chapter draft:** proposed V10/C01. Authored 2026-10-19 using publicly accessible architecture-evaluation guidance and original synthetic examples. This chapter explains a *book-level method*; the reusable [authoring profile contract](../../../../authoring/models/requirements-workload-profile.md) remains a separate supporting tool. No actual organization, workload telemetry, approval or benchmark is represented.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.868027aee4884210bea1d8a6542fbfb0:0 -->
## Purpose and mission

The same headline requirement—"serve more users reliably"—can justify different designs when one system has a write-contention bottleneck, another has occasional bulk jobs, and a third has a downstream rate limit. An architecture recommendation should therefore begin with **an explicit contract for observable outcomes, load, invariants and resources**, rather than a technology catalogue.

The profile's job is to preserve what is *known*, what is required, what is assumed and what must be measured. Its output is not an architecture: it is a testable decision boundary in which every candidate can be rejected, conditioned or compared. [arc42 Introduction and Goals](https://docs.arc42.org/section-1/) ties architectural drivers to fundamental requirements, quality goals and stakeholders. [arc42 Quality Requirements](https://docs.arc42.org/section-10/) distinguishes usage and change scenarios with observable response measures. [SEI's Architecture Tradeoff Analysis Method](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/) describes systematic evaluation against interacting qualities. Those are methodological sources, not evidence for the invented workload below.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.868027aee4884210bea1d8a6542fbfb0:9 -->
## Engineering walkthrough — Complete intake without choosing a style first

**Original fictional platform:** 10,000 registered accounts, a short launch-day surge proposed at
120 distinct booking intents/s, one exclusive-resource invariant and partner clients that cannot all
upgrade together. "Cloud native" is not a requirement. The actual observed arrival distribution,
retry amplification, hot-key share and current release lead time are unknown.

| Kind | Assumed requirement | Gate and missing evidence |
|---|---|---|
| Functional | One confirmed allocation per physical item and interval | Concurrency, lost acknowledgment and unique state-owner tests |
| Workload | 20-second burst of 120 new intents/s | Calibrated arrivals; unknown baseline |
| Quality | Correct outcome within a bounded user deadline | Stakeholder-approved SLI/SLO and eligible population needed |
| Security/operations | Object-level tenant authorization, one maintainable state authority | Reject an unowned new privileged writer |
| Compatibility | Legacy clients/events coexist during change | Consumer inventory and retention horizon unknown |
| Economics | Account for on-call, storage and migration recovery | No valid actual price or staffing measurements provided |

**Decision:** `MEASURE_FIRST`. Preserve the current authoritative booking boundary while profiling the actual bottleneck. A queue is not an equivalent solution when the business insists on immediate *final* confirmation; a service split cannot be approved without fenced ownership transfer. The architecture may change when controlled evidence demonstrates that smaller changes fail a hard requirement and a candidate meets it with operational support.

**Proposed, not executed:** collect versioned workload/profile evidence, test a hot resource under concurrent confirmations and document allowed degraded states. The arc42 and SEI architecture evaluation references guide concern/decision structure but do not prove this fictional choice.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Capture outcome, workload, invariant, constraint and evidence inputs before comparing architecture candidates.

A complete-looking questionnaire with unknown hot-key behavior or recovery ownership still cannot support a definite recommendation.

The detailed pages separate the mechanisms that make this decision conditional:

- [Outcomes, constraints and workload intake](intake-invariants.md) — Which inputs must be explicit before candidate architectures are compared?
- [Adversarial requirements and candidate screening](evidence-screening.md) — Which missing evidence or hard gate must block a premature recommendation?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
