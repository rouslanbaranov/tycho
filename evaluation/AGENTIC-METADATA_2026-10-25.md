# Metadata-aware snippets and fallback - 2026-10-25

> Issue [#409](https://github.com/rouslanbaranov/tycho/issues/409), E18-04.
> **Status:** implementation and measured fallback evidence; not answer-quality
> acceptance, not independent review and not a production measurement.
> No file under `book/` was modified.

## What changed

- Search results now carry `metadata_snippet` only when the matched excerpt
  does not contain a query term; the snippet is the canonical page summary.
- When a query has no FTS candidates and `mode=exploratory` is requested,
  the search falls back to the validated route-index metadata (title, summary,
  route questions and keywords) and returns explicitly weak sections with
  `match_source=route-metadata` and `metadata_expanded=true`.
- The fallback never marks those sections confident and never turns a policy
  abstention into an answer.
- Route metadata is cached by file identity, not by a mutable global query
  cache.

The normal ranking and the strict/default response are unchanged.

## Benchmark

The 40-task E18-01 benchmark was rerun on snapshot `7df007da...` with the
metadata-aware search. Retrieval is unchanged versus the E18-01 baseline:

| Metric | metadata-aware | E18-01 baseline |
|---|---:|---:|
| Recall@10 | 0.9375 | 0.9375 |
| nDCG@10 | 0.503445 | 0.503445 |
| MRR | 0.567485 | 0.567485 |
| Top-1 hit | 0.40625 | 0.40625 |
| Path precision | 0.1375 | 0.1375 |
| Mean context bytes | 21,500 | 16,818 |
| Mean tool calls | 1.0 | 1.0 |
| Mean latency | 1,133 ms | 594 ms |
| Policy abstain rate | 0.875 | 0.875 |
| False confident answers | 0 | 0 |

The metadata summary fields increase context and latency in this diagnostic
run; no ranking improvement is claimed for this 40-task set. The fallback is
covered by a separate synthetic metadata-only query in the unit tests because
the current benchmark has no zero-FTS-result answerable task.

Raw report: `evaluation/agentic-metadata.json`.

## Checks

~~~sh
/tmp/tycho-e18-venv/bin/python -m unittest discover -s tests \
  -p 'test_tycho_mcp*.py' -v
~~~

The tests cover normal metadata snippets, the route-metadata fallback, weak
labeling, and maintenance of the strict/no-result behavior.

## Limits

- 40 author-labelled tasks; no dedicated zero-result benchmark yet.
- Metadata snippets increase context bytes and latency in this run.
- Synthetic fallback coverage is not a real-query prevalence measurement.
- No final-answer correctness, remote run, human review or independent review.
- `human_review: not-performed; sufficient: 0`.
