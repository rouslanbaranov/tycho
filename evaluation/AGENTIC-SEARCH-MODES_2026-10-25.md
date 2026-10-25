# Agentic search modes - 2026-10-25

> Issue [#407](https://github.com/rouslanbaranov/tycho/issues/407), E18-02.
> **Status:** implementation and benchmark evidence; not answer-quality
> acceptance, not independent review and not a production measurement.
> No file under `book/` was modified.

## What changed

`tycho_search` now supports:

- `mode: strict | exploratory`; strict preserves calibrated abstention,
  exploratory returns candidates in a separate `weak_results` list;
- `detail: ids | snippets` for a smaller navigation response;
- `max_chars` with a hard response budget and explicit `truncated`;
- result facets, `why`, top-level and per-result `next_actions`;
- the same arguments through `GET/POST /search` on the HTTP wrapper.

The default remains `strict` with `detail=snippets` and no budget, so
existing clients keep the previous calibration and response shape.

## Benchmark method

The frozen 40-task benchmark from E18-01 is run three ways:

- `strict`: default policy visibility, one search call.
- `exploratory`: same policy but weak candidates are exposed separately.
- `exploratory-max-6000`: exploratory with a 6,000-byte response budget.

All runs use one stdio server, snapshot `b425cc63...` and 32 answerable /
8 unanswerable tasks. The runner records retrieval separately from policy
confidence and never asks the server for a final answer.

## Results

| Metric | strict | exploratory | exploratory, 6000 B |
|---|---:|---:|---:|
| Recall@10 | 0.125 | 0.9375 | 0.5625 |
| nDCG@10 | 0.074816 | 0.503445 | 0.31713 |
| MRR | 0.084375 | 0.567485 | 0.484375 |
| Top-1 hit | 0.0625 | 0.40625 | 0.40625 |
| Path precision | 0.15 | 0.1375 | 0.296875 |
| Mean context bytes | 4,036 | 21,493 | 5,952 |
| Mean tool calls | 1.0 | 1.0 | 1.0 |
| Policy abstain rate | 0.875 | 0.875 | 0.875 |
| Policy confident rate | 0.0 | 0.0 | 0.0 |
| Unanswerable abstention | 0.875 | 0.875 | 0.875 |
| False confident answers | 0 | 0 | 0 |

Raw reports:

- `evaluation/agentic-mode-strict.json`
- `evaluation/agentic-mode-exploratory.json`
- `evaluation/agentic-mode-exploratory-6000.json`

## Interpretation

- Strict mode exposes a serious agent-usability gap: the calibrated policy
  hides candidates on 28 of 32 answerable tasks, leaving recall@10 at 0.125.
- Exploratory mode recovers the retrieval signal (recall@10 0.9375) without
  changing the policy verdict. Weak results are explicitly separate and must
  not be presented as confident answers.
- A 6,000-byte budget cuts context by about 72% versus unbounded exploratory,
  but loses recall (0.5625) and improves path precision (0.2969). The budget is
  a real trade-off, not a free optimization.
- None of these runs establishes answer correctness; the server still returns
  evidence, not verdicts, and the final synthesis remains the agent's job.

## Checks

~~~sh
/tmp/tycho-e18-venv/bin/python -m unittest discover -s tests \
  -p 'test_tycho_mcp*.py' -v
~~~

The tests cover strict compatibility, exploratory weak results, id-only
responses, hard budget truncation and HTTP argument validation.

## Limits

- 40 author-labelled tasks; one snapshot and one local stdio transport.
- No answer-quality judge, query log, remote Vercel run or independent review.
- The policy confident rate remains zero on this set; this task exposes the
  problem and does not fix the calibration model.
- `human_review: not-performed; sufficient: 0`.
