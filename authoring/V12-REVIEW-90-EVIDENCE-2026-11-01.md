# V12 review-90 evidence package

- Promotion content HEAD: 12bc74d1b0335e7b5816e4f12344b4fbc424d826
- Main after promotion: f336241a
- Counts: 145 entries; 90 technical sufficient; 90 decision sufficient; 7 owner-accepted.
- 90 is the sufficient count and coincides with the 90th promotion.
- independent_reviews is 0; it counts different-vendor per-entry promotion reviews. The Codex acceptance reports are owner-acceptance evidence, not that counter; DeepSeek fallback reviews are separate.

## Owner-accepted entries

- tycho.pattern.valet-key: technical=sufficient, decision=sufficient
- tycho.pattern.anti-corruption-layer: technical=sufficient, decision=sufficient
- tycho.pattern.parallel-run: technical=sufficient, decision=sufficient
- tycho.pattern.workload-identity-mtls: technical=sufficient, decision=sufficient
- tycho.pattern.asynchronous-request-reply: technical=sufficient, decision=sufficient
- tycho.pattern.federated-identity: technical=sufficient, decision=sufficient
- tycho.pattern.cache-invalidation: technical=sufficient, decision=sufficient

## Acceptance reports (7)

- authoring/ai-reviews/2026-10-27-valet-key-split-review6-codex.md: 9ae5b68f13ffd8fe47d410bb2010ad4e561aa2848390d3cef59692a2f38dff04
- authoring/ai-reviews/2026-10-27-anti-corruption-layer-split-review4-codex.md: 2c7c0220f0ca61cf4a75f86fda6edfbfc22e0de5265cd987a503f2d4420e4b90
- authoring/ai-reviews/2026-10-27-parallel-run-split-review2-codex.md: f4db0f3d67061885e2dc47a743d2dc5a5c6f5d66df3511f8a86e361a1e829dfa
- authoring/ai-reviews/2026-10-28-workload-identity-review6-codex.md: c7c476c3df3d76f61d2300112454956f370b8ca5f8cde26d96cc2ec8bddf6d66
- authoring/ai-reviews/2026-10-28-federated-identity-review2-codex.md: ebef99dcc833f149723cb463f09ce638d2691e65dbcc215b8ef140920325e1fd
- authoring/ai-reviews/2026-10-29-cache-invalidation-split-review-deepseek.md: 146b9cebefb66be12699ffe960e4b9e2ccba4f051ba826fb674a99f49d894dae
- authoring/ai-reviews/2026-10-28-async-request-reply-split-review-codex.md: 59b9b64d0aeed47c31263fe33cab103fa787558d85feb9326aee987d610f8fe9

## Multi-Leader rebind

Content-reviewed change, not format-only. The owner page changed because Read Replicas was rewritten; the Multi-Leader section body remained identical. The page-level content_review: draft is scoped to the V04 manuscript, not the two reviewed pattern sections; promotion binds section and page hashes. Section body hash is a48a641c...; earlier 15bd9abf... included two trailing blank lines. Reviewer session 61f90871-973f-4845-87e1-cc5c933505e3; report SHA-256 b721d8199b77fee2cdfd038bbdd33843ad6716afda8d88b6b231d6ca2869e333.

## Promotion records

```json
{
  "pattern_id": "tycho.pattern.multi-leader-replication",
  "technical": "pass",
  "decision": "pass",
  "reviewed_at": "2026-11-01",
  "reviewed_head": "12bc74d1b0335e7b5816e4f12344b4fbc424d826",
  "owner_page_sha256": "96b6d15fe7c1293dd02dd1d06b28f0e862b23e39c4f3cb084b43c6e71311fb77",
  "card_sha256": "e84ba5d090b3a4e631f95fb2bcf0943d79c8a12b617f9614e6239a68f78f2f8e",
  "reviewer": "DeepSeek Reviewer",
  "report_path": "authoring/ai-reviews/2026-11-01-read-replicas-multi-leader-deepseek.md",
  "report_sha256": "b721d8199b77fee2cdfd038bbdd33843ad6716afda8d88b6b231d6ca2869e333"
}
```
```json
{
  "pattern_id": "tycho.pattern.read-replicas",
  "technical": "pass",
  "decision": "pass",
  "reviewed_at": "2026-11-01",
  "reviewed_head": "12bc74d1b0335e7b5816e4f12344b4fbc424d826",
  "owner_page_sha256": "96b6d15fe7c1293dd02dd1d06b28f0e862b23e39c4f3cb084b43c6e71311fb77",
  "card_sha256": "3f517a5477de11db06816f3290ec0cb29298de3126ba0b185126921fefce5a4c",
  "reviewer": "DeepSeek Reviewer",
  "report_path": "authoring/ai-reviews/2026-11-01-read-replicas-multi-leader-deepseek.md",
  "report_sha256": "b721d8199b77fee2cdfd038bbdd33843ad6716afda8d88b6b231d6ca2869e333"
}
```
