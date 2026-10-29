---
metadata_version: 1
id: "tycho.page.5187d0a69bc343f388225f9be0ee2ffa"
kind: "page"
parent_id: "tycho.chapter.0a5e430b39094337aa6a211d9b5b4bd0"
canonical_path: "book/volumes/v10-decision-support-and-modernization/c05-target-architecture-versus-transition-states/controlled-cutover.md"
title: "Controlled Cutover"
topic_ids:
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "migration"
summary: "Bounded technical ownership note for Controlled Cutover; gates, no-return and fallback limits."
route_hints:
  questions:
    - "Should authority switch during a planned downtime only after writes pause, replication drains and data freshness reaches zero?"
  prerequisites:
    - "tycho.chapter.0a5e430b39094337aa6a211d9b5b4bd0"
  related_ids:
    - "tycho.chapter.0a5e430b39094337aa6a211d9b5b4bd0"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "controlled cutover"
    - "owner note"
evidence_scope:
  source_ids:
    - "src.gcp-spanner-cutover"
    - "src.fowler-strangler"
  claim_ids: []
  status: "source-linked"
  notes: "Moved verbatim from the migration mechanisms and no-return gates page; the bound source claims and limits remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: null
content_verified_at: null
---

# Controlled Cutover

> **Pattern atlas:**
> [Controlled Cutover](../../v11-pattern-atlas/c10-deployment-modernization/controlled-cutover.md#controlled-cutover) — decision conditions and contraindications.

This page owns the bounded technical note moved from the
[migration mechanisms and no-return gates page](cutover-gates.md#controlled-cutover)
on 2026-10-29. The branch-by-abstraction walkthrough remains on the chapter page.

A controlled cutover drains the write pipeline and verifies that source changes replicate before
switching writes. Verify pipeline health and DLQ state before cutover. Resolve DLQ errors before pausing writes. Verify the forward replication pipeline has no permanent errors and wait
for the data freshness metric to reach zero before switching. A contingency fallback pathway can be configured before cutover using reverse replication. The procedure assumes the target schema is deployed and the
backfill job is complete. Verify active CDC replication before pausing writes. Pause Datastream and
confirm that no replication events pass through the stream, then update connection strings and start
application services against the target. Monitor reverse replication errors after cutover. The
fallback path requires an active reverse pipeline before cutover starts. Strangler Fig replacement
moves authority incrementally through seams.

## Navigation

| Route | Destination |
|---|---|
| Parent chapter | [V10/C05 — Target architecture versus transition states](README.md) |
| Originating page | [Migration mechanisms and no-return gates](cutover-gates.md#controlled-cutover) |
