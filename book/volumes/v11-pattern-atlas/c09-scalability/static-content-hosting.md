---
metadata_version: 1
id: "tycho.page.4ee21701c36640119917d0bb900f9894"
kind: "page"
parent_id: "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
canonical_path: "book/volumes/v11-pattern-atlas/c09-scalability/static-content-hosting.md"
title: "Static Content Hosting"
topic_ids:
  - "scaling-mechanisms"
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Static Content Hosting with bounded owner evidence."
route_hints:
  questions:
    - "Should static content be served from a dedicated store or edge rather than the
      application origin?"
  prerequisites:
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
  related_ids:
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "static content hosting"
    - "edge"
evidence_scope:
  source_ids:
    - "src.microsoft-cloud-patterns"
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

# Static Content Hosting

**Identity.** Static Content Hosting; family Scalability and load distribution; kind
scalability-pattern; priority core.

**Decision question.** Should static content be served from a dedicated store or edge
rather than the application origin?

**Good-fit conditions.** Content is static/versioned; a retained version covers the
rollback window; cacheability and purge are controlled; origin protection is owned.

**Hard contraindications.** Reject when content is personalized/uncacheable, when
versioning/purge cannot meet freshness, or when edge configuration is unowned.

**Competing alternative.** Serve static content dynamically from the application origin.

**Failure and recovery.** Changing, deleting, or restricting access to origin content doesn't
invalidate cached copies. Purge caches and account for propagation time; CDN purges don't
clear browser caches.

**Technical owner.** [Static Content Hosting](../../v08-delivery-deployment-and-recovery/c08-network-request-paths-routing-and-edge-delivery/static-content-hosting.md#static-content-hosting) — static hosting is bounded to edge/origin behavior.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.static-content-hosting.2026-10-26: all nine served headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** CDN / Edge Caching; Cache Invalidation; TTL-Based Expiration; Geode.
