# Third focused AI re-review hand-off — #535

Status: prepared for a focused independent AI re-review. Not a review or acceptance.

- Branch: `feature/TYCHO-535-read-the-155-pattern-source-plan-units-in-full`
- Second-review HEAD: `d1011099`
- Current remediation HEAD: `b147cfc1`
- Second report: `authoring/ai-reviews/2026-10-26-remediation-rereview-codex.md`
- Second report SHA-256: `430d30bbb689e5ad15127f7790eb2a0e0cc4b39fd663602ccde854cc7bfbb2f7`

## Scope

Verify only the second-review findings:

- R-04 regression: ten source-scope misbindings;
- R-03a: Aggregator ledger absence statement;
- R-05a: FS-10 in the Chapter 4+ range.

Confirm that R-01, R-02, R-06, R-07 and R-08 remain resolved. Do not repeat the full
155-unit reading.

## Expected state

- 155 entries matched by `(pattern_id, source_id, unit)`;
- zero section differences;
- Aggregator limitation distinguishes incomplete-set handling from duplicate handling;
- RESOLUTIONS lists eleven Chapter 4+ IDs and FS-10 separately;
- counts: 15 partially-supported, 5 unconfirmed, 2 contradicted, 1 resolved.

## Exact prompt

```text
You are an independent AI reviewer from a different vendor and harness than the
DeepSeek Harness authoring agent. Perform a focused read-only re-review of Tycho #535
remediation round 3. Do not edit, commit, open a PR or change configuration.

Repository: /Users/rbaranov/Projects/tycho
Checkout: current branch HEAD; record `git rev-parse HEAD`.
Second-review snapshot: d1011099.
Current remediation HEAD: b147cfc1.
Second report: authoring/ai-reviews/2026-10-26-remediation-rereview-codex.md
Second report SHA-256: 430d30bbb689e5ad15127f7790eb2a0e0cc4b39fd663602ccde854cc7bfbb2f7
Claims: research/full-source-confirmation/claims.v1.json
Results: research/full-source-confirmation/results.v1.json
Reading plan: edition/patterns/full-unit-reading-plan.v1.json
Source plan: edition/patterns/source-plan.v1.json

Verify only R-04 regression, R-03a and R-05a, and confirm R-01, R-02, R-06, R-07
and R-08 remain resolved. Derive counts from artifacts. Use public sources only.

Required checks:
1. 155 entries match by (pattern_id, source_id, unit); report unmatched count.
2. Zero section differences between the reading plan and source plan.
3. Aggregator ledger limitation distinguishes supported incomplete-set handling from
   unconfirmed duplicate handling.
4. RESOLUTIONS lists the eleven Chapter 4+ IDs and FS-10 separately.
5. Counts: 15 partially-supported, 5 unconfirmed, 2 contradicted, 1 resolved.
6. Run the eight validators plus check_boundary; record exact exit statuses.

Return one Markdown report with: harness/vendor, model/version, session id, timestamp,
repository path, review HEAD, reviewed snapshot, exact scope, verdict
(pass / pass-with-findings / reject), findings by severity with paths and evidence,
limits, and `ai_review: performed` only if the checks ran. State `sufficient: 0`.
Do not claim owner acceptance, CI or merge permission.
```

The author saves the returned report verbatim in `authoring/ai-reviews/` and records its
SHA-256 in the index.
