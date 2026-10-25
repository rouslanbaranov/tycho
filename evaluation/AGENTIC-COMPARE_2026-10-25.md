# Extractive comparison primitive - 2026-10-25

> Issue [#410](https://github.com/rouslanbaranov/tycho/issues/410), E18-05.
> **Status:** implemented and tested; not answer-quality acceptance and not
> independent review. No file under `book/` was modified.

## What changed

Added `tycho_compare`:

- accepts two to five options, patterns or approaches;
- performs one bounded search per option;
- returns citation-bearing cells grouped by dimension (overview, evidence,
  trade-off, failure, decision, example);
- marks cells weak when the calibrated policy is not confident;
- reports uncertainties for missing or weak options;
- applies a hard `max_chars` budget;
- returns no winner, ranking or recommendation.

The response carries an explicit extractive notice. The final comparison and
decision remain with the calling agent or human.

## Evidence

The tool is covered by unit and HTTP-facing tests:

- cited cells and dimensions;
- no winner field;
- weak cells when policy confidence is absent;
- budget truncation;
- error handling for invalid option counts and duplicates.

No separate quality benchmark was run because the current agentic set does not
contain paired-option tasks. This is a limitation, not evidence of comparative
answer quality.

## Checks

~~~sh
/tmp/tycho-e18-venv/bin/python -m unittest discover -s tests \
  -p 'test_tycho_mcp*.py' -v
~~~

## Limits

- Extraction and grouping are heuristic from search headings and excerpts.
- No paired-option or decision-quality benchmark yet.
- No final recommendation, semantic ranking, remote run or independent review.
- `human_review: not-performed; sufficient: 0`.
