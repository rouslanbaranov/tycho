---
metadata_version: 1
id: "tycho.page.4ed3324a562c4b2fadc7b94ee5665abe"
kind: "page"
parent_id: "tycho.chapter.94b4b6d9e2e1490abd0055a5265141ff"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c03-vms-containers-orchestration-and-serverless/immutable-infrastructure.md"
title: "Immutable Infrastructure"
topic_ids:
  - "deployment-architecture"
perspectives:
  - "architecture"
  - "operations"
summary: "Bounded technical ownership note for Immutable Infrastructure; replacement, drift and rollback limits."
route_hints:
  questions:
    - "Should infrastructure be replaced rather than mutated in place?"
  prerequisites:
    - "tycho.chapter.94b4b6d9e2e1490abd0055a5265141ff"
  related_ids:
    - "tycho.chapter.94b4b6d9e2e1490abd0055a5265141ff"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "immutable infrastructure"
    - "owner note"
evidence_scope:
  source_ids:
    - "src.ibm-immutable-infrastructure"
  claim_ids: []
  status: "source-linked"
  notes: "Moved verbatim from the control planes, placement and reversibility page; the bound source claims and limits remain in the owner unit."
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

# Immutable Infrastructure

> **Pattern atlas:**
> [Immutable Infrastructure](../../v11-pattern-atlas/c10-deployment-modernization/README.md#immutable-infrastructure) — decision conditions and contraindications.

This page owns the bounded technical note moved from the
[control planes, placement and reversibility page](static-stability.md#immutable-infrastructure)
on 2026-10-29. The static-stability walkthrough remains on the chapter page.

Immutable infrastructure replaces instances from a versioned image or definition instead of mutating
running hosts, so each instance is reproducible from a recorded artifact. Every running instance
must be reproducible from a recorded artifact digest, and drift must be detected rather than
tolerated.

A rebuilt image that no longer matches the deployed artifact turns replacement into an uncontrolled
change; record digests and test the rebuild path. Configuration management on long-lived hosts is
cheaper when state locality dominates; choose immutable replacement when reproducibility, an
automated replacement path and artifact rollback speed matter.

**Limits.** Immutable replacement is not a backup: data, secrets and external effects still need
lifecycle ownership, toolchain and base-image provenance must be reproducible, and a rollback
restores an artifact, not necessarily compatible data. Rebuild time and image size are
operational costs, not proofs of reproducibility.

## Navigation

| Route | Destination |
|---|---|
| Parent chapter | [V08/C03 — VMs, containers, orchestration and serverless](README.md) |
| Atlas card | [Immutable Infrastructure](../../v11-pattern-atlas/c10-deployment-modernization/README.md#immutable-infrastructure) |
| Originating page | [Control planes, placement and reversibility](static-stability.md#immutable-infrastructure) |
