---
metadata_version: 1
id: "tycho.page.066e7bd31c33fd91500bda7e55a3dedb"
kind: "page"
parent_id: "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
canonical_path: "book/volumes/v11-pattern-atlas/c10-deployment-modernization/parallel-run.md"
title: "Parallel Run"
topic_ids:
  - "deployment-architecture"
perspectives:
  - "architecture"
summary: "Decision card for Parallel Run; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should old and new implementations process the same work"
  prerequisites:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  related_ids:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed."
  keywords:
    - "pattern atlas"
    - "parallel-run"
evidence_scope:
  source_ids:
    - "src.minimumcd-parallel-run"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; source binding remains in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-27"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-27"
updated_at: "2026-10-27"
source_inspection_date: "2026-10-21"
content_verified_at: null
---
# Parallel Run

**Identity.** Parallel Run; family Deployment and legacy modernization; kind
modernization-pattern; priority core.

**Decision question.** Should old and new implementations process the same work
concurrently for comparison?

**Good-fit conditions.** Outputs are side-effect-free and comparable; the old path remains
authoritative until cutover.

**Hard contraindications.** Reject for side-effecting operations, when comparison is
meaningless, or when cost is prohibitive.

**Competing alternative.** Branch by abstraction with a smaller, monitored rollout.

**Failure and recovery.** A candidate failure must never affect the response; keep the old
authority until cutover.

**Technical owner.** [Parallel Run](../../v10-decision-support-and-modernization/c05-target-architecture-versus-transition-states/authority-states.md#parallel-run) — parallel run is bounded to coexistence/authority states.

**Sources.** [src.fowler-strangler](../../../../edition/patterns/reading-ledger.v1.json)
read record read.fowler-strangler.2026-10-21: sections "Strangler Fig", "Further Reading";
context for the transition narrative.
[src.minimumcd-parallel-run](../../../../edition/patterns/reading-ledger.v1.json)
read record read.minimumcd-parallel-run.2026-10-26: all eight served
headings read. MinimumCD supports dual execution, background
comparison and harness removal. Mismatch thresholds, sampling and cost bounds are synthetic.
The sources are public articles, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Dark Launching; Strangler Fig; Controlled Cutover; Reconciliation.
