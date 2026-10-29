---
metadata_version: 1
id: "tycho.page.840c65c6698344ba8ed13f1f10038b5c"
kind: "page"
parent_id: "tycho.chapter.8a86707018773def410689efbc79cf94"
canonical_path: "book/volumes/v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/static-content-hosting.md"
title: "Static Content Hosting"
topic_ids:
  - "network-architecture"
perspectives:
  - "architecture"
  - "operations"
  - "evaluation"
summary: "Bounded technical ownership note for Static Content Hosting; origin, purge and rollback limits."
route_hints:
  questions:
    - "Should static content be served from a dedicated store or edge rather than the application origin?"
  prerequisites:
    - "tycho.chapter.8a86707018773def410689efbc79cf94"
  related_ids:
    - "tycho.chapter.8a86707018773def410689efbc79cf94"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "static content hosting"
    - "owner note"
evidence_scope:
  source_ids:
    - "src.microsoft-cloud-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Moved verbatim from the edge cache and origin page; the bound source claims and limits remain in the owner unit."
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

# Static Content Hosting

> **Pattern atlas:**
> [Static Content Hosting](../../v11-pattern-atlas/c09-scalability/static-content-hosting.md#static-content-hosting) — decision conditions and contraindications.

This page owns the bounded technical note moved from the
[edge cache and origin page](edge-cache-origin.md#static-content-hosting) on 2026-10-29.
The CDN and origin walkthrough remains on the chapter page.

Static content hosting places static resources in a storage service that serves them directly,
reducing load on the application compute that handles other requests.

The host must own upload validation, origin protection and prewarming for a release. A retained
version is the rollback path, so garbage collection may delete old objects only after the rollback
window; a deleted object needs a tombstone or purge proof. Configure cache keys and cache
lifetimes deliberately, and keep the authorization boundary explicit, especially for private
assets signed at the edge. Changing, deleting, or restricting access to origin content
doesn't invalidate cached copies. Purge caches when you
need to, but account for propagation time and remember that CDN purges don't clear browser
caches.

Source: `read.static-content-hosting.2026-10-26` (Microsoft static content hosting pattern).

Retained versions and edge copies carry storage, egress and purge cost; a second origin or
duplicated manifest needs one version authority, or the rollback path becomes ambiguous.

The alternative is to serve static content dynamically from the application origin. The source
notes that using an application platform to deliver static content is generally not cost-effective.

## Navigation

| Route | Destination |
|---|---|
| Parent chapter | [V08/C08 — Network request paths, routing and edge delivery](README.md) |
| Originating page | [Edge caching, private content and origin recovery](edge-cache-origin.md#static-content-hosting) |
