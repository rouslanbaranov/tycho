---
metadata_version: 1
id: "tycho.page.f39fa61013ca41abbfba82ef48250f8f"
kind: "page"
parent_id: "tycho.chapter.4166e932cbd64ce2a63fe0c6d6eb049a"
canonical_path: "book/volumes/v06-caching-indexing-and-retrieval/c01-local-and-distributed-caching/cache-acceptance.md"
title: "Cache cost, failure and acceptance"
topic_ids:
  - "scaling-mechanisms"
perspectives:
  - "architecture"
summary: "When should stale service, origin protection or no cache be preferred?"
route_hints:
  questions:
    - "When should stale service, origin protection or no cache be preferred?"
  prerequisites:
    - "tycho.page.76f6d792c80a448fa1a76001ca6699e1"
  related_ids:
    - "tycho.chapter.4166e932cbd64ce2a63fe0c6d6eb049a"
    - "tycho.page.33742c54f667446cbf57cb9f3696a533"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "cache"
    - "acceptance"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Bounded question from tycho.page.33742c54f667446cbf57cb9f3696a533; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Cache cost, failure and acceptance

**Owning question:** When should stale service, origin protection or no cache be preferred?

This page belongs to [V06/C01 — Local and distributed caching](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.33742c54f667446cbf57cb9f3696a533:5 -->
## 5. Failure/operation cost model

The effective cost of caching includes more than hit latency:
- memory bytes/entry and per-replica duplication;
- serialization/compression and CPU/GC work;
- network to shared cache, TLS, connection pools and retries;
- cache warm-up after scaling or restart;
- source demand on miss, refresh and rebuild;
- invalidation coordination and event replay;
- operating the cache availability tier and its recovery;
- data leakage/staleness consequences.

Original synthetic arithmetic: if 900 of 1,000 eligible reads hit cache, 100 misses remain **only if** each miss results in one origin read with no parallel revalidation or retries. If those 100 misses happen simultaneously for the same expensive key, peak origin load may be unacceptable despite a 90% overall hit rate. This is a model, not a measured service.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.33742c54f667446cbf57cb9f3696a533:6 -->
## 6. Choose based on the user-visible contract

A local Caffeine-style cache may be appropriate when a few instances frequently read insensitive, slowly changing descriptions and per-instance copies are tolerable. Shared Redis-style caching may help when many nodes repeat reads of the same expensive dataset and a shared failure domain is manageable.

Prefer no cache when origin read cost is below the target or correctness/authorization changes require current state. A write-through, write-behind or cache-aside design must state write ordering and possible loss; the mere cache pattern name does not create an atomic dual write.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.33742c54f667446cbf57cb9f3696a533:7 -->
## 7. Decision tests and recovery

Proposed, **not executed** experiments:
1. Verify request/tenant key isolation with same apparent resource IDs.
2. Compare local/shared/no cache with identical offered workload and origin resource budget.
3. Measure cold start, size/eviction, refresh failure and read staleness.
4. Kill the shared cache or restart every application replica; observe source pressure and correctness.
5. Revoke access during an in-flight read and confirm policy-compliant results.
6. Verify cache freshness under concurrent modification and multiple versions.

A cache is justified only if it preserves hard state/security invariants and improves the selected latency or cost objective at representative load.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](refresh-semantics.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](local-and-distributed-cache-design.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
