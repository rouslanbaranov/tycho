---
metadata_version: 1
id: "tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1"
kind: "page"
parent_id: "tycho.chapter.8605018cb9224f99bea9dd49be2b79e3"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c02-baseline-analysis-for-existing-software/legacy-baseline-and-modernization-evidence.md"
title: "Legacy system baseline and modernization evidence: deciding what to keep"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Integrated question, original scenario and transfer limits for Baseline analysis for existing software. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which observed limitations justify changing the architecture?"
  prerequisites: []
  related_ids:
    - "tycho.page.81add4a0d86b4053ae77f9301fd2281d"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.b656116463d9480f83199d8202b127a4"
    - "tycho.page.868027aee4884210bea1d8a6542fbfb0"
    - "tycho.page.47ffb5c160bd4b10aff27101414c2133"
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
    - "tycho.page.210134080fac4c09bebb593befd0cb25"
    - "tycho.page.19145078d87143b28387ab187d345c32"
    - "tycho.page.fbf4c3d642d14ce2a69f009efd17b1a8"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Legacy"
    - "system"
    - "baseline"
    - "and"
    - "modernization"
    - "evidence"
    - "deciding"
    - "what"
    - "keep"
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
<!-- tycho-question-source:tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1:-1 -->

# Legacy system baseline and modernization evidence: deciding what to keep

> **Tycho book chapter draft:** proposed V10/C02, 2026-10-19. This is an original, industry-neutral teaching example based on admissible public modernization literature. It is not a description, reconstruction, measurement or modernization plan for an actual employer, application or production system. Its companion [legacy-profile authoring model](../../../../authoring/models/legacy-modernization-profile.md) is an information-gathering tool, not a replacement for this chapter.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1:0 -->
## Purpose and mission

Modernization starts with a contradiction: engineers need to replace or improve something, but parts of its behavior may be undocumented and still essential to users. An attractive target diagram can therefore be less informative than a map of **what is actually owned, what must not break and how existing and new behavior can coexist**.

The answer to "which architecture should replace a legacy system?" may legitimately be **retain and stabilize**, **upgrade in place**, **modularize without distributing**, or **incrementally replace a bounded capability**. This chapter develops a versioned baseline, turns uncertain legacy claims into research tasks, evaluates options against transition constraints, and demonstrates why moving the deployment boundary is not equivalent to transferring data ownership. The independent [Patterns of Legacy Displacement, Cartwright/Horn/Lewis (2024)](https://martinfowler.com/articles/patterns-legacy-displacement/) emphasizes desired outcomes and incremental delivery; [Fowler's Strangler Fig update (2024)](https://martinfowler.com/bliki/StranglerFigApplication.html) explains staged substitution. Neither source proves which option is right for the synthetic case used here.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1:10 -->
## Engineering walkthrough — Observed legacy baseline versus hypothetical future benefit

**Original fictional estate:** a Java catalogue imports vendor records nightly to PostgreSQL while exposing lookup APIs. A planned microservice extraction claims it will shorten imports; yet no current SQL timing, lock and pool profile, startup time, replay correctness or team release-lead-time data has been collected.

| Baseline question | Required observation | Candidate assumption, not yet fact |
|---|---|---|
| Why nightly import is slow | Batch sizes, explain plans, lock/pool waits and retries | A queue/service split will improve processing |
| Who owns item identity | Mapping, invariant, reader/writer and partner versions | New datastore can replace old authority |
| What failure means | Commit and checkpoint positions, partial updates, replay | New workflow is restart-safe |
| Why deployments are expensive | Actual collaboration/approval and release history | Autonomous service saves meaningful effort |

**Counterexample:** a measured query plan later exposes one expensive scan; an index or staged batch repair meets the latency goal while retaining the same transaction and interface. That falsifies the *performance* case for extraction. Conversely, externally imposed fault isolation or independently owned data may still justify a new boundary, but it must carry compatibility and recovery obligations.

**Proposed test, not run:** pin identical vendor snapshots, apply equivalent offered import work and compare retained+optimized versus separated-worker paths under interrupted backfill and old partner clients. A target diagram is **hypothesis**, original measurements would be **observations**, while Fowler's Strangler/displacement sources describe candidate methods. No modernization or benchmark is asserted.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1:11 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Netflix — Cloud rearchitecture](../../../cases/netflix-seven-year-cloud-rearchitecture.md)**. **Relevant mechanism or architectural contrast:** A datacenter failure and multiyear gradual change illustrate staged removal of concentrated dependencies. **Not established by this report/playbook:** An historical cloud migration does not prove microservices or cloud would improve a different monolith's TCO or reliability.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Describe observed legacy behavior and limitations before assigning expected benefits to a target architecture.

Old technology is not itself evidence of a defect; retaining and improving the baseline must remain a real alternative.

The detailed pages separate the mechanisms that make this decision conditional:

- [Observed legacy behavior and baseline ownership](legacy-observation.md) — Which existing behavior must be measured and preserved before change is justified?
- [Modernization alternatives and transition obligations](modernization-options.md) — How do retained, replaced and incrementally migrated options differ in required proof?
- [Migration failure tests and decision reversal](migration-falsification.md) — Which recovery observation would reject the attractive target?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
