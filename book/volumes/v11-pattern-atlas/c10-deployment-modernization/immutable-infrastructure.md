---
metadata_version: 1
id: "tycho.page.f1083bfaf6f74ba53bdc746c3cd78866"
kind: "page"
parent_id: "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
canonical_path: >-
  book/volumes/v11-pattern-atlas/c10-deployment-modernization/immutable-infrastructure.md
title: "Immutable Infrastructure"
topic_ids:
  - "deployment-architecture"
  - "software-delivery"
perspectives:
  - "architecture"
  - "migration"
summary: "Decision card for Immutable Infrastructure; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should infrastructure be replaced rather than mutated in place?"
  prerequisites:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  related_ids:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "immutable infrastructure"
    - "deployment"
evidence_scope:
  source_ids:
    - "src.ibm-immutable-infrastructure"
    - "src.aws-immutable-infrastructure"
    - "src.hashicorp-immutable-vms"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch5-ibm-immutable.2026-10-21 and
    read.ibm-immutable.2026-10-30, read.aws-immutable-infrastructure.2026-10-30
    and read.hashicorp-immutable-vms.2026-10-30; owner section and limits are
    bounded.
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
# Immutable Infrastructure

**Identity.** Immutable Infrastructure; family Deployment and legacy modernization; kind
delivery-pattern; priority core.

**Decision question.** Should infrastructure be replaced rather than mutated in place?

**Good-fit conditions.** Images/artifacts are versioned and recorded; drift is
detected and remediated; state is externalized; replacement, rebuild and
rollback are automated.

**Hard contraindications.** Reject when in-place state cannot be externalized,
when replacement is too slow, when drift is invisible, or when artifact
identity and the rebuild path cannot be tested.

**Competing alternative.** Mutable servers with configuration management. Reverse the
choice when replacement cost exceeds drift/recovery benefit.

**Failure and recovery.** A rebuilt image can differ from the deployed artifact;
record digests, test the rebuild path and roll back to the previous artifact.
AWS treats unmanaged drift as something to detect and remediate; HashiCorp
describes rebuilding and redeploying the previous image and recording build
metadata; IBM documents tested, reproducible changes and rollback. Comparing
rebuilt and deployed digests remains Tycho guidance.

**Technical owner.** [Immutable Infrastructure](../../v08-delivery-deployment-and-recovery/c03-vms-containers-orchestration-and-serverless/immutable-infrastructure.md#immutable-infrastructure) — immutable replacement and drift are bounded, not a cloud product.

**Sources.**
[src.ibm-immutable-infrastructure](../../../../edition/patterns/reading-ledger.v1.json)
read records read.batch5-ibm-immutable.2026-10-21 and
read.ibm-immutable.2026-10-30;
[src.aws-immutable-infrastructure](../../../../edition/patterns/reading-ledger.v1.json)
read record read.aws-immutable-infrastructure.2026-10-30;
[src.hashicorp-immutable-vms](../../../../edition/patterns/reading-ledger.v1.json)
read record read.hashicorp-immutable-vms.2026-10-30. The sources are public
documentation, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** GitOps; Blue/Green; Rolling Deployment; Infrastructure as Code.
