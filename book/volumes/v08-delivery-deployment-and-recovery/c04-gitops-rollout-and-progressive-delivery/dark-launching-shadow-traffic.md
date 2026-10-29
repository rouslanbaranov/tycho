---
metadata_version: 1
id: "tycho.page.b1318da570f746bb8126e863b97d8eb3"
kind: "page"
parent_id: "tycho.chapter.5e4761e1a3e34c2f8023ec8ac4fa81d5"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c04-gitops-rollout-and-progressive-delivery/dark-launching-shadow-traffic.md"
title: "Dark Launching-Shadow Traffic"
topic_ids:
  - "software-delivery"
perspectives:
  - "architecture"
  - "operations"
summary: "Bounded technical ownership note for Dark Launching and Shadow Traffic; mirroring, effects and comparison limits."
route_hints:
  questions:
    - "Should new behavior receive mirrored or hidden traffic before it becomes authoritative?"
  prerequisites:
    - "tycho.chapter.5e4761e1a3e34c2f8023ec8ac4fa81d5"
  related_ids:
    - "tycho.chapter.5e4761e1a3e34c2f8023ec8ac4fa81d5"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "dark launching"
    - "shadow traffic"
    - "owner note"
evidence_scope:
  source_ids:
    - "src.fowler-dark-launching"
    - "src.istio-traffic-mirroring"
  claim_ids: []
  status: "source-linked"
  notes: "Moved verbatim from the GitOps, rolling, blue/green and canary page; the bound source claims and limits remain in the owner unit."
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

# Dark Launching-Shadow Traffic

> **Pattern atlas:**
> [Dark Launching / Shadow Traffic](../../v11-pattern-atlas/c10-deployment-modernization/dark-launching.md#dark-launching--shadow-traffic) — decision conditions and contraindications.

This page owns the bounded technical note moved from the
[GitOps and progressive delivery page](gitops-canary-and-progressive-rollout.md#dark-launching--shadow-traffic)
on 2026-10-29. The rolling, blue/green and canary walkthrough remains on the chapter page.

Dark launching calls new or changed back-end behavior from existing user requests without
showing the result. Shadow traffic
copies live requests to a mirrored service while the old path remains authoritative.

Mirrored requests are fire-and-forget: their responses are discarded, so they do not affect the
primary response. Their Host/Authority headers carry a `-shadow` suffix. The new path still
needs a side-effect boundary and a load budget; these are synthetic design conditions.

Mirrored responses are discarded, so they do not affect the primary response. A worrying performance impact can be switched off with a feature flag before users notice.
A canary release is the alternative when the decision depends on a user choice.

**Source boundary.** The
[read.fowler-dark-launching.2026-10-26](../../../../edition/patterns/reading-ledger.v1.json)
record supports hidden invocation, load assessment, feature-flag rollback and old/new
comparison; the
[read.batch7-istio-mirroring.2026-10-26](../../../../edition/patterns/reading-ledger.v1.json)
record supports request mirroring, fire-and-forget responses and fractional mirroring.
Neither source supplies a measurement method, side-effect suppression or a capacity bound;
those remain synthetic.

**Limits.** Shadow traffic is not a user-behavior sample; comparison coverage and data
sensitivity bound what it can prove.

## Navigation

| Route | Destination |
|---|---|
| Parent chapter | [V08/C04 — GitOps, rollout and progressive delivery](README.md) |
| Originating page | [GitOps, rolling, blue/green and canary release architecture](gitops-canary-and-progressive-rollout.md#dark-launching--shadow-traffic) |
