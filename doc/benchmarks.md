# Benchmarks and metrics

Tycho has several benchmark families, each answering a different question. They
must not be combined into a single "quality score". Most are AI-adjudicated,
pool-relative and not production measurements.

## Benchmark families

| Family | Question | Artifacts |
|---|---|---|
| V12 simulation | What do the models imply under declared assumptions? | `edition/v12/runs/` |
| Qrels v4 | Are page and section relevance labels coherent? | `evaluation/qrels-v4/` |
| Qrels v5-dense | How do dense candidate pools change judgments? | `evaluation/qrels-v5-dense/` |
| Search quality v5 | How do ranking profiles score? | `evaluation/search-quality-v5/` |
| Agent retrieval v5 | Hit-at-k and recall | `evaluation/agent-retrieval-v5/` |
| Agent sessions | Do scripted tool sessions execute? | `evaluation/agent-session/` |
| MCP smokes | Do stdio and HTTP transports work? | `mcp/tests/smoke/` |

## V12 simulation metrics

V12 uses 30 replications and reports a mean plus a normal-approximation
confidence interval. The metrics are conditional on synthetic inputs.

| Metric | Meaning |
|---|---|
| `success_rate` | Completed successes / offered requests |
| `latency_mean` | Mean successful-request latency |
| `latency_p95`, `p99` | Tail latency |
| `cost_per_1k_success` | Synthetic cost per 1,000 successes |
| `rejection_rate` | Explicit rejections / offered |
| `timeout_rate` | Deadline misses / offered |
| `retry_amplification` | Attempts per offered request |
| `throughput` | Completed requests per second |
| `server_utilization` | Busy server fraction |
| `max_queue_length`, `mean_queue_length` | Queue occupancy |

Checkout candidates under the declared 20 requests/second workload:

| Candidate | Success | p95 (s) | Cost / 1k | Timeout |
|---|---:|---:|---:|---:|
| A: synchronous | 0.9218 | 0.8703 | 1.8095 | 0.0778 |
| B: bounded queue | 0.9996 | 1.2059 | 1.3356 | 0.0041 |
| C: partitioned | 0.9679 | 1.7692 | 3.6260 | 0.1110 |

The decision recommends B under the declared constraints. C violates the cost
and p95 constraints. This is a model result, not a production benchmark.

The modernization decision is `insufficient-evidence`: rollback completes in
10% of replications within the horizon, and the dual-write assumptions are not
measured.

## Qrels v4

Qrels v4 contains 150 queries:

- 90 book;
- 30 atlas;
- 30 V12.

| Level | Candidates | Accepted | Direct |
|---|---:|---:|---:|
| Page | 610 | 447 | 188 |
| Section | 610 | 447 | 188 |

The labels were built from read-only pages, cards and V12 artifacts. The
candidate pools are 4-10 items and are not exhaustive. AI-adjudicated only.

## Qrels v5-dense

The dense pool uses 30 candidates per query and 30 batches:

- 4,500 page judgments;
- 4,500 section judgments;
- 997 accepted pages;
- 996 accepted sections.

The pool is still relative to 498 pages and 3,075 sections. It is not an
exhaustive relevance judgment.

## Search quality

Selected `3,2,1` profile:

| Level | P@5 | R@5 | MRR | nDCG@5 |
|---|---:|---:|---:|---:|
| Page | 0.4387 | 0.3489 | 0.8360 | 0.6160 |
| Section | 0.2867 | 0.2363 | 0.7138 | 0.4698 |

Agent retrieval hit rates:

| Level | hit@1 | hit@3 | hit@5 |
|---|---:|---:|---:|
| Page | 0.9333 | 0.9933 | 0.9933 |
| Section | 0.8933 | 0.9867 | 0.9933 |

The hit rate asks whether at least one accepted item appears in the top k. It
does not measure whether the answer is complete or correct.

## Agent sessions

Four scripted sessions produced 133 entries:

| Session | Entries | OK | Failed |
|---|---:|---:|---:|
| S1 | 32 | 28 | 4 |
| S2 | 35 | 31 | 4 |
| S3 | 32 | 26 | 6 |
| S4 | 34 | 34 | 0 |
| **Total** | **133** | **119** | **14** |

These are tool-execution checks, not answer-quality scores.

## MCP benchmarks

The MCP suite includes:

- stdio and HTTP smoke tests;
- client compatibility fixtures;
- multi-process benchmark;
- retrieval diagnostics for default, section and dense modes.

The verifier checks six end-to-end conditions. It does not measure throughput,
latency distribution or security.

## How to read a metric

1. What is the unit: page, section, artifact or answer?
2. What is the pool: exhaustive, top-k, or synthetic?
3. Who labelled it: rule, model, AI reviewer or human?
4. Is the split dev or holdout?
5. Is the result conditional on a snapshot and commit?
6. Is it a local run or CI?

A metric without those answers is not a production claim.

## Limits

- Most relevance labels are AI-adjudicated, not human.
- Candidate pools are finite and not exhaustive.
- V12 is uncalibrated and synthetic.
- Search metrics do not establish answer correctness.
- Agent-session counts do not establish reasoning quality.
- No latency, availability or cost benchmark of a production deployment exists.
