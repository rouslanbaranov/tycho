# Final qrels v4 regression — 2026-10-30

Status: post-cache/semaphore/artifact verification. AI qrels; no human review,
CI, owner acceptance or sufficient coverage.

## Result

All qrels v4 mode/split metrics match the recorded production baseline:

- BM25 page .593/.847/.953; section .480/.700/.793;
- margin .05 page .620/.833/.940; section .513/.700/.800;
- best page .567/.833/.947; section .453/.687/.787.

No quality drift after:

- validated-manifest cache;
- in-process concurrency semaphore;
- query cache key fix;
- query-aware artifact ranking;
- volume-only artifact fix.

## Verification

- final evaluator run at margin .05;
- 730 tests and premerge PASS;
- healthcheck remains ok.

## Limits

- AI qrels; pool-relative.
- No human review, CI, owner acceptance or sufficient coverage.
