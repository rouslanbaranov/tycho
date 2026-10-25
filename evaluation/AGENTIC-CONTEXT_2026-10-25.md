# Agentic context bundle - 2026-10-25

> Issue [#408](https://github.com/rouslanbaranov/tycho/issues/408), E18-03.
> **Status:** implementation and one-call benchmark evidence; not answer-quality
> acceptance, not independent review and not a production measurement.
> No file under `book/` was modified.

## What changed

Added `tycho_context`. It returns one bounded, citation-bearing bundle:

- sections grouped as overview, definition/evidence, trade-off, failure,
  decision or example;
- section keys, canonical citations, excerpts and why-this-section;
- explicit gaps when the policy abstains or query terms are unknown;
- next actions for deeper reading;
- a hard `max_chars` budget with `returned_chars` and `truncated`;
- an optional `include_evidence` mode for registered evidence metadata.

The tool is extractive. It never returns a final answer, recommendation or
verdict. Weak sections are marked and the response carries the calibrated
answerability block.

## Benchmark method

The frozen 40-task E18-01 benchmark was run with one `tycho_context` call per
task, default `max_chars=6000`, snapshot `547c44e5...`. The runner treats
weak sections as visible candidates but not confident results.

## Results

| Metric | context bundle | exploratory search | strict search |
|---|---:|---:|---:|
| Recall@10 | 0.625 | 0.9375 | 0.125 |
| nDCG@10 | 0.371077 | 0.503445 | 0.074816 |
| MRR | 0.505208 | 0.567485 | 0.084375 |
| Top-1 hit | 0.40625 | 0.40625 | 0.0625 |
| Path precision | 0.25 | 0.1375 | 0.15 |
| Mean context bytes | 5,601 | 21,493 | 4,036 |
| Mean tool calls | 1.0 | 1.0 | 1.0 |
| Policy abstain | 0.875 | 0.875 | 0.875 |
| False confident answers | 0 | 0 | 0 |
| p50 latency, overall | 1,038.6 ms | 718.6 ms | 741.4 ms |

Raw report: `evaluation/agentic-context.json`.

## Interpretation

- One context call carries roughly 74% less context than unbounded
  exploratory search, but loses recall (0.625 vs 0.9375).
- Path precision improves (0.25 vs 0.1375), because the bundle is capped and
  grouped rather than dumping ten sections.
- The bundle remains exploratory on 28/32 answerable tasks because the policy
  confidence is still zero. Grouping does not fix calibration.
- These are retrieval and cost measurements; no final-answer correctness was
  measured.

## Checks

~~~sh
/tmp/tycho-e18-venv/bin/python -m unittest discover -s tests \
  -p 'test_tycho_mcp*.py' -v
~~~

The tests cover the tool contract, extractive notice, non-empty grouped
sections, citation presence and the byte budget.

## Limits

- 40 author-labelled tasks; one snapshot and local stdio.
- Exploratory/strict latency columns are historical E18-02 runs on snapshot
  b425cc63; context metrics use the current 547c44e5 snapshot.
- No remote Vercel run, query log, human answer key or independent review.
- Grouping is heuristic from headings and excerpts; it is not a semantic
  classifier.
- `human_review: not-performed; sufficient: 0`.
