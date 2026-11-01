---
metadata_version: 1
id: "tycho.page.3950620546fc4c09a829132bd19bb69a"
kind: "page"
parent_id: "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
canonical_path: >-
  book/volumes/v11-pattern-atlas/c10-deployment-modernization/branch-by-abstraction.md
title: "Branch by Abstraction"
topic_ids:
  - "deployment-architecture"
  - "software-delivery"
perspectives:
  - "architecture"
  - "migration"
summary: >-
  Decision card for Branch by Abstraction; all four dimensions are source-bound,
  coverage remains partial-bounded and no promotion is claimed.
route_hints:
  questions:
    - >-
      Should an internal abstraction seam allow old/new implementations to
      coexist in one deployable?
  prerequisites:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  related_ids:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "branch by abstraction"
    - "deployment and legacy modernization"
evidence_scope:
  source_ids:
    - "src.fowler-branch"
    - "src.aws-branch"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch5-fowler-branch.2026-10-21 and
    read.aws-branch.2026-10-29; the owner section is bounded and coverage remains
    partial-bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-11-01"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-11-01"
updated_at: "2026-11-01"
source_inspection_date: "2026-10-29"
content_verified_at: null
---

# Branch by Abstraction

**Identity.** Branch by Abstraction; family Deployment and legacy modernization; kind
modernization-pattern; priority core.

**Decision question.** Should an internal abstraction seam allow old/new implementations to
coexist in one deployable?

**Good-fit conditions.** The seam can be introduced without breaking callers; both
implementations preserve the same contract; removal date and reversible switch are owned.

**Hard contraindications.** Reject when no internal seam exists, when the abstraction adds
no substitution value, when the old implementation cannot coexist, or when data consistency
is involved.

**Competing alternative.** Strangler Fig, a façade or a parallel run. Reverse the choice
when abstraction cost exceeds incremental change benefit.

**Failure and recovery.** Keep each increment reversible and backward compatible, and use an
easily flipped switch so the team can return to the old functionality if problems appear. An
intermediate verification step that calls both new and old functionality can implement a
fallback. A named removal owner and date remain Tycho review conditions, not source claims.

**Technical owner.** [Branch by Abstraction](../../v10-decision-support-and-modernization/c05-target-architecture-versus-transition-states/cutover-gates.md#branch-by-abstraction) — branch by abstraction is bounded to internal interface replacement.

**Sources.** [src.fowler-branch](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-fowler-branch.2026-10-21: sections "Branch By Abstraction",
"Further Reading", "Acknowledgements", "Notes".
Failure and recovery also uses
[src.aws-branch](../../../../edition/patterns/reading-ledger.v1.json) read record
read.aws-branch.2026-10-29: the public AWS Prescriptive Guidance page "Branch by
abstraction pattern", accessed 2026-10-29; canonical text revision
`618648d7274e985f417915ecd4eeffe83e6c7db8b2ee1d0691293aee04f09d1c`.
The page supports reversible, backward-compatible increments, fallback verification,
switch-back recovery and the data-consistency limit.
The sources are public documentation/articles, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Strangler Fig; Parallel Run; Feature Flags; Controlled Cutover.

**Limits.** Coverage remains partial-bounded and self-checked; no promotion or owner
acceptance is claimed. The owner section is bounded to the internal-interface replacement
mechanism, and the source pages are documentation rather than runtime evidence.
