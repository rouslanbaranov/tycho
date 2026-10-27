# Focused AI re-review hand-off — sufficient R2 residuals

Status: prepared for a focused independent external AI re-review. Not a review,
promotion or sufficient-coverage claim.

- Issue: #540
- Prior report: `authoring/ai-reviews/2026-10-27-sufficient-r2-codex.md`
- Prior report SHA-256: `3997c55722125ca28477b4a0e07feb57437710ed334708595187effb1ded5278`
- Prior reviewed HEAD: `55649c3a`
- Current remediation HEAD: `eea4d891`
- Policy: `governance/SUFFICIENT-COVERAGE.md`
- Manifest: `research/sufficient-pilot-540/manifest.json`
- Outcome: `research/sufficient-pilot-540/REVIEW-OUTCOME.md`

## Scope

Review only the R2-01 through R2-04 residuals for the same six entries. No entry is
promoted; all six remain rejected and blocked. Do not repeat the 155-unit reading.

## What changed after R2

- **R2-01:** ASVS manifest URL/label now point to the 5.0.0 PDF; the stale overview
  claim was removed from the ledger record.
- **R2-02:** Spanner now records a canonical article-text SHA-256 computed by
  `scripts/source_content_hash.py`, not a mutable raw-HTML hash.
- **R2-03:** the four stale manifest `current_coverage` fields were synchronized.
- **R2-04:** the mTLS card now names the eight supporting headings.

## Required checks

1. Reproduce the Spanner canonical hash with the committed script and compare.
2. Verify ASVS manifest URL/label and ledger claim are consistent with the PDF.
3. Verify manifest current coverage for dark, RBAC, cutover and parallel.
4. Verify the mTLS card names eight real headings and keeps synthetic limits.
5. Confirm promotions=0, sufficient=0, six rejected/blocked.
6. Run the validators and record exact exit statuses.

## Exact prompt

```text
You are an independent AI reviewer from a different vendor and harness than the
DeepSeek Harness authoring agent. Perform a focused read-only re-review of the #540
sufficient-pilot R2 residuals. Do not edit, commit, open a PR or change configuration.

Repository: /Users/rbaranov/Projects/tycho
Checkout: current branch HEAD; record `git rev-parse HEAD`.
Prior reviewed HEAD: 55649c3a.
Current remediation HEAD: eea4d891 (record the actual checked-out HEAD).
Prior report: authoring/ai-reviews/2026-10-27-sufficient-r2-codex.md
Prior report SHA-256: 3997c55722125ca28477b4a0e07feb57437710ed334708595187effb1ded5278
Policy: governance/SUFFICIENT-COVERAGE.md
Manifest: research/sufficient-pilot-540/manifest.json
Outcome: research/sufficient-pilot-540/REVIEW-OUTCOME.md

Review only R2-01 through R2-04. Verify that all six entries remain rejected and
blocked and that the promotion allowlist is empty and sufficient is zero. Check the
ASVS URL/label and stale-claim removal, the manifest current-coverage fields, the
mTLS named subset, and reproduce the Spanner canonical article-text hash with
scripts/source_content_hash.py. Use public sources only.

Return one Markdown report with: reviewer harness/vendor, model/version, session id,
timestamp, repository path, review HEAD, prior reviewed HEAD, per-entry technical and
decision verdicts, findings by severity with paths and evidence, limits, and
`sufficient: 0`. Do not claim owner acceptance, CI or merge permission.
```

The author saves the returned report verbatim under `authoring/ai-reviews/` and indexes
its SHA-256. Promotion waits for a separate pass and owner decision.
