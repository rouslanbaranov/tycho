---
metadata_version: 1
id: "tycho.page.06d61faf8a9f48ebb03eb43d7e3dcda6"
kind: "page"
parent_id: "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
canonical_path: "book/volumes/v11-pattern-atlas/c10-deployment-modernization/canary-release.md"
title: "Canary Release"
topic_ids:
  - "deployment-architecture"
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: >-
  Decision card for Canary Release; bounded owner evidence and explicit limits.
route_hints:
  questions:
    - >-
      Should a new version receive a small traffic share before full promotion?
  prerequisites:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  related_ids:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
    - "tycho.page.b938ff1a06264492a425f2eff555ae7d"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "canary release"
    - "progressive delivery"
evidence_scope:
  source_ids:
    - "src.argo-rollouts"
    - "src.flagger-deployment-strategies"
    - "src.sre-workbook"
    - "src.aws-blue-green-deployments"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-30"
updated_at: "2026-10-30"
source_inspection_date: "2026-10-30"
content_verified_at: null
---
# Canary Release

**Identity.** Canary Release; family Deployment and legacy modernization; kind
deployment-pattern; priority core.

**Decision question.** Should a new version receive a small traffic share before full
promotion?

**Good-fit conditions.** A measurable signal exists; traffic can be split; abort/rollback
is defined; the canary is representative; shared-state compatibility is explicit; any
mirrored traffic is idempotent or can be processed twice.

**Hard contraindications.** Reject when traffic cannot be split, when metrics are too
noisy, when the canary shares hidden state with the baseline, or when mirrored writes
cannot be made idempotent or safely processed twice.

**Competing alternative.** Traffic mirroring, blue/green, feature flags or rolling
deployment. Reverse the canary choice when analysis cost exceeds risk reduction or the
cohort cannot be isolated; avoid mirroring when writes cannot be made idempotent or safely
processed twice. Blue/green costs roughly twice the resources.

**Failure and recovery.** Shared-state contamination is source-backed: a binary rollback
does not undo committed data, a mirrored write can execute twice, and a blue/green switch
still shares the data boundary. Tycho guidance, not a source claim: low-traffic blindness,
metric leakage and sample-size limits make a small cohort pass while a rare failure hides.

**Technical owner.** [Canary Release](../../v08-delivery-deployment-and-recovery/c04-gitops-rollout-and-progressive-delivery/gitops-canary-and-progressive-rollout.md#canary-release) — canary analysis and abort are bounded; metric selection is service-specific.

**Sources.** [src.argo-rollouts](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.batch5-argo-canary.2026-10-21`: all fifteen served headings read;
canary steps, analysis abort and the rolling mimic.
[src.flagger-deployment-strategies](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.flagger-deployment-strategies.2026-10-30`: deployment strategies,
canary, A/B, blue/green and mirroring; mirroring idempotency.
[src.sre-workbook](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.sre-workbook-canarying.2026-10-30`: shared infrastructure,
stateful teeing limits and feature flags.
[src.aws-blue-green-deployments](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.aws-blue-green-data.2026-10-30`: shared data stores and
backward-compatible schema changes. The sources are public documentation units,
not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Blue/Green; Rolling Deployment; Feature Flags; Dark Launching.
