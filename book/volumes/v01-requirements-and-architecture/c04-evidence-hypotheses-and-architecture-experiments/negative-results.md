---
metadata_version: 1
id: "tycho.page.dff5d6affea243cca3c426d04d290802"
kind: "page"
parent_id: "tycho.chapter.ee2cd95003ab4018a9d49e2ff0b6b2f4"
canonical_path: "book/volumes/v01-requirements-and-architecture/c04-evidence-hypotheses-and-architecture-experiments/negative-results.md"
title: "Negative evidence and stopping rules"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "When should an attractive candidate be rejected or research stop?"
route_hints:
  questions:
    - "When should an attractive candidate be rejected or research stop?"
  prerequisites:
    - "tycho.page.3a5cdaf97d0b4e51ae5828507f033dd0"
  related_ids:
    - "tycho.chapter.ee2cd95003ab4018a9d49e2ff0b6b2f4"
    - "tycho.page.a2cd4465792a4740aa5150ad248fd420"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "negative"
    - "results"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.a2cd4465792a4740aa5150ad248fd420; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Negative evidence and stopping rules

**Owning question:** When should an attractive candidate be rejected or research stop?

This page belongs to [V01/C04 — Evidence, hypotheses and architecture experiments](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.a2cd4465792a4740aa5150ad248fd420:5 -->
## 5. Negative evidence and the stopping condition

The outcomes **MEASURE_FIRST**, **INSUFFICIENT_EVIDENCE**, and **REJECTED_BY_GATE** are legitimate engineering conclusions. They are preferable to asserting “proven architecture” because a diagram, retrieved paragraph or synthetic example looked plausible.

Examples of stopping conditions:
- the load generator fails to emit the intended traffic;
- a critical metric excludes timed-out requests without disclosure;
- the source describes a different runtime major version;
- a test uses different application/data revisions between contenders;
- an authorization/consistency invariant fails;
- a supposedly reversible change wrote a state that the old version cannot read;
- the expected benefit is smaller than documented measurement noise;
- there is no known owner authorized to accept the changed service contract.

A negative test should be designed to challenge the conclusion, not merely satisfy a checklist. When the result is insufficient, record the narrowest next source, measurement or owner decision needed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.a2cd4465792a4740aa5150ad248fd420:6 -->
## 6. Evidence-first research does not mean evidence-free certainty

[arc42 §10 Quality Requirements](https://docs.arc42.org/section-10/) asks for concrete quality scenarios; [arc42 §9 Architecture Decisions](https://docs.arc42.org/section-9/) stresses options and reasons. These support a decision method but do not specify a universal statistical test. A user-facing latency SLO should count operations at a clear boundary and explain which timeout/rejection populations enter its denominator; [Google SRE SLO Workbook](https://sre.google/workbook/implementing-slos/) offers publicly documented SLI/SLO selection and trade-offs.

A source supporting "service X can enforce a retry limit" does not establish "our app is safe under retries." The second claim needs exact configuration/behavior and effect-identity testing. Source-to-claim provenance prevents this common inference error.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](experiment-contract.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](architecture-evidence-hypotheses-and-experiments.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
