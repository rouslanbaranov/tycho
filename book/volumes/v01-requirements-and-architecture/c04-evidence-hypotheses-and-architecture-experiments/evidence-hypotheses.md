---
metadata_version: 1
id: "tycho.page.d8118d40313143e4ac47323274fbb594"
kind: "page"
parent_id: "tycho.chapter.ee2cd95003ab4018a9d49e2ff0b6b2f4"
canonical_path: "book/volumes/v01-requirements-and-architecture/c04-evidence-hypotheses-and-architecture-experiments/evidence-hypotheses.md"
title: "Evidence classes and competing hypotheses"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Which evidence class supports a claim and which alternative explanation remains possible?"
route_hints:
  questions:
    - "Which evidence class supports a claim and which alternative explanation remains possible?"
  prerequisites:
    - "tycho.page.a2cd4465792a4740aa5150ad248fd420"
  related_ids:
    - "tycho.chapter.ee2cd95003ab4018a9d49e2ff0b6b2f4"
    - "tycho.page.a2cd4465792a4740aa5150ad248fd420"
    - "tycho.page.3a5cdaf97d0b4e51ae5828507f033dd0"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "evidence"
    - "hypotheses"
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
# Evidence classes and competing hypotheses

**Owning question:** Which evidence class supports a claim and which alternative explanation remains possible?

This page belongs to [V01/C04 — Evidence, hypotheses and architecture experiments](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.a2cd4465792a4740aa5150ad248fd420:1 -->
## 1. Five evidence classes are not substitutes

| Evidence class | What can be concluded | What remains unknown |
|---|---|---|
| Requirement | Desired outcome and hard gate from an authorized owner | Whether current or proposed implementation achieves it |
| Primary public specification | Documented semantics at version/scope | Actual deployment configuration and compliance |
| Versioned source/config observation | A particular revision expresses an implementation/configuration | Which revision is running and what happens under load |
| Reproducible experiment | Observed behavior within tested fixture, inputs, population and limits | Universal performance/correctness of untested conditions |
| Analytical model | Conditional mathematical relationship given assumptions | Whether the assumptions represent the target system |

A proposed design diagram is a **sixth state: a proposal**, not evidence that the depicted services or fault controls are implemented. Citations must attach to the actual proposition they support, not merely to a file containing related keywords.

For important claims, record: exact question, boundary, statement, evidence type, source revision/section, date, assumptions, conflicting observations, unknowns, and decision significance.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.a2cd4465792a4740aa5150ad248fd420:2 -->
## 2. Competing hypotheses beat single-cause stories

An original fictional public trail directory serves a list of trail descriptions and shows increased p99 after a software release.

Possible explanations:
- H1: a database query plan regressed after data distribution changed;
- H2: an application connection pool waits longer under the same offered rate;
- H3: a new external enrichment request is now on the critical path;
- H4: clients retry more after ambiguous errors, multiplying demand.

“Add caching” is not a diagnosis. It might help repeated reads under H1 but worsen freshness and stampede behavior, and it may have no effect on H3's external timeout.

A hypothesis becomes useful only with a **discriminator**:

| Hypothesis | Observation that supports it | Observation that weakens it |
|---|---|---|
| H1: query plan | Query plan, table stats and DB time differ at same input mix | Plan and measured DB time unchanged |
| H2: pool wait | Queue/pool wait dominates parent critical path | Pool acquisition negligible during affected traces |
| H3: enrichment | Optional span now serially blocks response | Span remains out of required path |
| H4: retries | Attempts per logical operation rise, especially after errors | Logical arrivals and attempt multiplicity unchanged |

None of these observations proves a cause in isolation. A changed index plan can coexist with retry amplification. A valid experiment must compare alternatives and control for correlated variables.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](architecture-evidence-hypotheses-and-experiments.md) |
| Next | [Continue the reasoning](experiment-contract.md) |
| Integrated question | [Original scenario and limits](architecture-evidence-hypotheses-and-experiments.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
