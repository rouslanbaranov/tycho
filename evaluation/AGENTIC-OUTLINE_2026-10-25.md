# Outline and topic planning - 2026-10-25

> Issue [#411](https://github.com/rouslanbaranov/tycho/issues/411), E18-06.
> **Status:** implemented and tested; not answer-quality acceptance and not
> independent review. No file under `book/` was modified.

## What changed

Added `tycho_outline`:

- accepts a topic or a relative path prefix;
- ranks canonical metadata entries through the validated route index;
- returns paths, titles, summaries, route questions, evidence status and a
  reading order;
- applies a hard `max_chars` budget;
- reports gaps when nothing matches;
- never returns full page text or claims complete coverage.

## Evidence

Unit and HTTP-facing tests cover canonical citations, bounded entries, absence
of full content and the extractive notice. The tool uses the same route-index
snapshot as search and refuses a route/index snapshot mismatch.

No dedicated outline-quality benchmark was run; this is a planning primitive,
not a retrieval-quality claim.

## Limits

- Ranking is metadata overlap, not semantic planning.
- No pattern-family-specific outline benchmark.
- No final answer, remote run, human review or independent review.
- `human_review: not-performed; sufficient: 0`.
