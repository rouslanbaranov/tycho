---
metadata_version: 1
id: "tycho.page.4a302aa608d645288756076e9fcdd6b0"
kind: "page"
parent_id: "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
canonical_path: "book/volumes/v11-pattern-atlas/c10-deployment-modernization/controlled-cutover.md"
title: "Controlled Cutover"
topic_ids:
  - "deployment-architecture"
  - "software-delivery"
perspectives:
  - "architecture"
  - "migration"
summary: "Decision card for Controlled Cutover with bounded owner evidence."
route_hints:
  questions:
    - "Should authority switch only after writes pause and replication drains?"
  prerequisites:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  related_ids:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "controlled cutover"
    - "migration"
evidence_scope:
  source_ids:
    - "src.gcp-spanner-cutover"
    - "src.fowler-strangler"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-26"
content_verified_at: null
---

# Controlled Cutover

**Identity.** Controlled Cutover; family Deployment and legacy modernization; kind
modernization-pattern; priority core.

**Decision question.** Should authority switch during a planned downtime only after writes pause,
replication drains and data freshness reaches zero?

**Good-fit conditions.** A downtime window is available; schema and backfill are complete; CDC
replication is active; a reverse fallback can be configured.

**Hard contraindications.** Reject when writes cannot be paused or replication completeness cannot
be verified.

**Competing alternative.** Strangler Fig replacement moves authority incrementally through seams.

**Failure and recovery.** A contingency fallback pathway can be configured before cutover
using reverse replication.

**Technical owner.** [Cutover gates](../../v10-decision-support-and-modernization/c05-target-architecture-versus-transition-states/controlled-cutover.md#controlled-cutover) — bounded to the Spanner cutover procedure, not a generic no-return contract.

**Sources.** [src.gcp-spanner-cutover](../../../../edition/patterns/reading-ledger.v1.json)
read record read.gcp-spanner-cutover.2026-10-26: all ten served headings read.
[src.fowler-strangler](../../../../edition/patterns/reading-ledger.v1.json)
read record read.fowler-strangler.2026-10-21: Strangler Fig alternative.
The sources are public documentation/articles, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Strangler Fig; Expand-and-Contract; Blue/Green; Rollback Limits.
