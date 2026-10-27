> Resolved 2026-10-27: AGENTS 17-21 scoped external review to book/atlas changes; PR #552 was tooling and merged without this review. This file is historical.

# External AI review request — E17-71

Status: request only. No external review has been performed.

Reviewer requirement: a different-vendor AI harness from DeepSeek Harness
(for example ChatGPT or Claude), read-only, in a fresh session. Do not use a
DeepSeek subagent or the authoring session.

## Artifact

- PR: #552
- Head: c3cbd91c95ded8d2cd80e388b7dcc7ce858174b9
- Base: origin/main
- Scope: pre-enrichment search snapshot and reindex harness.

Artifact SHA-256:

- edition/patterns/search-pre-enrichment.v1.json
  3de70da3786d781c4a741e048ae15c6cea9c9e0dc09f6ebab0a427129db49e57
- scripts/search_reindex.py
  cefe3cd00b4ff4dc508d0c9e648e8488f54966e4deca88de3f7cb82c16d787d5
- tests/test_tycho_search_reindex.py
  87e29a555dca688f3a6da614dedb724211a04a6f1e3179cb64e075adcc82ef32
- authoring/SEARCH-REINDEX-PROTOCOL.md
  cfeaee45b570596b5cb3d230990e8d5205d05db4344cb31f30231a39e72cd877

## Exact prompt

You are the external independent AI reviewer for Tycho PR #552. Use a different
vendor from DeepSeek Harness. Work read-only: do not modify, commit, push or
merge.

Repository: https://github.com/rouslanbaranov/tycho
Head: c3cbd91c95ded8d2cd80e388b7dcc7ce858174b9
Base: origin/main

Review only:
- edition/patterns/search-pre-enrichment.v1.json
- scripts/search_reindex.py
- tests/test_tycho_search_reindex.py
- authoring/SEARCH-REINDEX-PROTOCOL.md

Verify:
1. snapshot content/route/section-index hashes and counts;
2. qrels-stale handling is fail-closed and does not rewrite labels;
3. rebuild never edits book or qrels;
4. check exit behavior and test coverage;
5. no book edits in the PR;
6. no overclaim of human review, CI, sufficient coverage or quality.

The manifest intentionally records qrels v2 as stale
(4232... vs current route 06b80...). Do not treat that disclosure as a bug;
judge whether it is handled correctly.

Return:
- verdict: pass / pass-with-findings / reject;
- evidence with exact paths and hashes;
- findings by severity;
- explicit limits;
- confirmation that you are an external different-vendor AI reviewer, not
  human review, CI or owner acceptance.

Save the raw report as authoring/ai-reviews/EXTERNAL-REVIEW-E17-71.md and
provide its SHA-256.

## Nonclaims

This request is not a review, not approval, not CI, not human review, not owner
acceptance and not sufficient coverage.

