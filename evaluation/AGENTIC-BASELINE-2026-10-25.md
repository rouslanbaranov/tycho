# Agentic MCP retrieval baseline - 2026-10-25

> Issue [#406](https://github.com/rouslanbaranov/tycho/issues/406), E18-01.
> **Status:** reproducible baseline on one snapshot; not answer-quality
> acceptance, not independent review and not a production measurement.
> No file under `book/` was modified.

## Purpose

Measure how well the current read-only MCP search serves bounded agent tasks
before changing retrieval or analysis behavior. The benchmark records
retrieval, policy confidence, tool calls, context bytes and latency. It does
not ask the server to produce a final answer or a verdict.

## Dataset

The frozen dataset reuses 40 questions and accepted paths from the existing
author-labelled corpus qrels. Selection is deterministic and stratified by the
existing categories.

| Property | Value |
|---|---|
| Dataset | `evaluation/agentic-qrels.v1.json` |
| Source | `evaluation/corpus-qrels.v2.json` |
| Source SHA-256 | `535b22b5c34f5437ee55f5c1452c10b7b97c1f1ca254026d38c00a456475a0f7` |
| Dataset SHA-256 | `56b2f0f6c24bc8930b4991b2b7e1d5cefe275e84441fc1a8f3127d58fe596c82` |
| Tasks | 40 |
| Task mix | 10 fact, 5 failure, 5 tradeoff, 5 synthesis, 4 change, 3 contradiction, 8 no-answer |
| Snapshot | `b425cc6343e9f6cf3c39d4edaecece7fefcec8c02b3817242f9aef77d2679514` |
| Baseline HEAD | `750be0cdf50fb463a10d9848cddc0a08e3b44d0c` |

The source labels are author-labelled and agent-adjudicated qrels, not human
review and not a complete answer key.

## Method

The runner starts one stdio MCP server and measures two strategies:

- `search-once`: one `tycho_search` call per task.
- `search-read`: `tycho_search` plus one `tycho_read` of the first result.

Search is called with `abstain=False` so retrieval candidates are visible and
the calibrated policy signal is recorded separately. This avoids reporting a
zero-recall result merely because the default would hide all candidates.

## Results

| Metric | search-once | search-read |
|---|---:|---:|
| Answerable tasks | 32 | 32 |
| Recall@10 | 0.9375 | 0.9375 |
| nDCG@10 | 0.503445 | 0.503445 |
| MRR | 0.567485 | 0.567485 |
| Top-1 hit | 0.40625 | 0.40625 |
| Path precision | 0.1375 | 0.1375 |
| Policy abstain rate, answerable | 0.875 | 0.875 |
| Policy confident rate, answerable | 0.0 | 0.0 |
| Mean tool calls, answerable | 1.0 | 2.0 |
| Mean context bytes, answerable | 16,817.8 | 19,499.8 |
| Mean latency, answerable (ms) | 593.8 | 1,178.6 |
| p50 latency, overall (ms) | 592.1 | 1,171.5 |
| p95 latency, overall (ms) | 608.5 | 1,302.0 |
| Unanswerable tasks | 8 | 8 |
| Abstention rate, unanswerable | 0.875 | 0.875 |
| False confident answers | 0 | 0 |

Raw reports:

- `evaluation/agentic-baseline-search-once.json`
- `evaluation/agentic-baseline-search-read.json`

## What the baseline says

- Retrieval usually places an accepted page in the top 10 (0.9375), but the
  correct page is first only 40.6% of the time and the top-10 contains many
  unrelated pages (path precision 0.1375).
- The current calibrated policy would abstain on 28 of 32 answerable tasks and
  is confident on none of them. That is strong evidence that the existing
  policy is not yet useful as an agent-facing default, even though it avoids
  false confident answers on this small unanswerable set.
- Reading the first result doubles tool calls and adds about 2.7 KB of context,
  but does not improve retrieval metrics. This is the gap the context bundle
  should address.
- These are retrieval and policy observations, not evidence that an agent can
  answer correctly. No answer-quality judgment was performed.

## Reproduce

~~~sh
/tmp/tycho-e18-venv/bin/python scripts/section_fts_index.py build --full
/tmp/tycho-e18-venv/bin/python scripts/build_agentic_benchmark.py
/tmp/tycho-e18-venv/bin/python scripts/evaluate_agentic.py \
  --strategy search-once \
  --json evaluation/agentic-baseline-search-once.json
/tmp/tycho-e18-venv/bin/python scripts/evaluate_agentic.py \
  --strategy search-read \
  --json evaluation/agentic-baseline-search-read.json
~~~

The environment path is local; the committed commands are the runner and
dataset. A clean environment must install the repository validation/routing
requirements first.

## Limits

- 40 author-labelled tasks; not a human-adjudicated answer set.
- One snapshot and one local stdio server; no Vercel or HTTP measurement.
- No query log and no external agent trace.
- No final-answer correctness, citation completeness or user satisfaction.
- No independent reviewer or owner acceptance.
- `human_review: not-performed; sufficient: 0`.
