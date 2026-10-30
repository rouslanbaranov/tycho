---
metadata_version: 1
id: "tycho.page.37ee8969c224c7b336487c02aff9149c"
kind: "page"
parent_id: "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
canonical_path: "book/volumes/v11-pattern-atlas/c05-caching-retrieval/stale-while-revalidate.md"
title: "Stale-While-Revalidate"
topic_ids:
  - "performance-engineering"
  - "data-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Stale-While-Revalidate with bounded owner evidence."
route_hints:
  questions:
    - "Should a stale response be served while a refresh runs in the background?"
  prerequisites:
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
  related_ids:
    - "tycho.chapter.87e52392e206a451ea5c79a4194c384b"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved card."
  keywords:
    - "pattern atlas"
    - "stale-while-revalidate"
    - "caching"
evidence_scope:
  source_ids:
    - "src.rfc5861"
    - "src.rfc9111-enrichment"
    - "src.mdn-cache-control"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch3-rfc5861.2026-10-21, read.rfc9111-stale.2026-10-30 and
    read.mdn-cache-control.2026-10-30; owner section and limits are bounded.
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
# Stale-While-Revalidate

**Identity.** Stale-While-Revalidate; family Caching and retrieval; kind caching-pattern;
priority advanced.

**Decision question.** Should a stale response be served while a refresh runs in the
background?

**Good-fit conditions.** The contract tolerates bounded staleness; the stale window is
explicit; revalidation can run in the background; failure can fall back to a blocking read.

**Hard contraindications.** Reject when read-after-write is mandatory, when stale data
would mislead a decision, or when refresh cannot be bounded.

**Competing alternative.** Blocking refresh or TTL-only expiry. Reverse the choice when
stale responses violate a business contract.

**Failure and recovery.** A failed or inconclusive revalidation may keep serving stale only
inside the window; after the bound, the next request blocks and is handled normally. A single
refresh owner and refresh-failure telemetry are Tycho guidance, not RFC requirements; the
owner section separates them from the HTTP rules.

**Technical owner.** [Stale fills and regeneration ownership](../../v06-caching-indexing-and-retrieval/c02-hot-keys-cache-stampedes-and-read-amplification/stale-fill.md#stale-while-revalidate) — stale-fill ownership is bounded, not a full HTTP cache specification.

**Sources.** [src.rfc5861](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.batch3-rfc5861.2026-10-21`: sections "3. The
stale-while-revalidate Cache-Control Extension" and "3.1. Example"; the bounded
window, the SHOULD NOT continuation and the inconclusive-validation fallback.
[src.rfc9111-enrichment](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.rfc9111-stale.2026-10-30`: sections "4.2.4. Serving Stale
Responses" and "5.5. Warning"; stale only when explicitly permitted, and
Warning obsoleted while Age remains.
[src.mdn-cache-control](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.mdn-cache-control.2026-10-30`: the `stale-while-revalidate`
section and the Age definition. The sources are public specification and
documentation units, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Cache Invalidation; TTL-Based Expiration; Cache Stampede Protection;
CDN / Edge Caching.
