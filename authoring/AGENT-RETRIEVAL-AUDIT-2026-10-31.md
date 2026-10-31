# External-agent retrieval audit — 2026-10-31

Status: AI-adjudicated only. No default change. Not human review, CI, owner
acceptance or sufficient coverage.

## Scope

- 100 stratified tasks: 50 book, 25 atlas, 25 v12;
- top-10 candidate retrieval, fixed v5 snapshot;
- page qrels v5.3 and section qrels v5.5;
- AI spot-check of 20 top results.

## Recall@k (offline FTS)

| Level | R@5 | R@10 | R@20 | R@50 |
|---|---:|---:|---:|---:|
| page v5.3 | .334 | .471 | .585 | **.703** |
| section v5.5 | .322 | .445 | .528 | **.618** |

Recall is the main weakness: top-5 precision is much better than long-tail
evidence coverage.

## Agent retrieval modes

| Mode | section R@10 | page R@10 | citation precision | zero results |
|---|---:|---:|---:|---:|
| abstain=false | **.471** | **.576** | **.416** | **0 / 100** |
| abstain=true | .387 | .473 | .340 | **21 / 100** |

abstain=true suppresses 21 answerable tasks. Off-topic probes: 0 / 20
abstained. The current evidence gate is therefore uncalibrated for agent use:
it gives false abstention on answerable queries and does not reject off-topic
probes.

## Diversity / snippets / snapshot

- search already uses result_scope=best-section-per-document;
- non-empty top-10 has 10 unique paths, mean 3.0 volumes;
- each result has section_key, path, heading, title, citation, excerpt, and
  next_actions;
- response carries a snapshot id and citation_scheme.

No separate MMR was added; page dedupe is already the default scope.

## Agent cost

- abstain=false: ~596 approx tokens per 10 results;
- latency p50 ~51 ms, p95 ~55 ms in this warmed local run;
- latency includes cache effects.

## AI spot-check

20 top results: 3 direct / 15 partial / 2 unsupported. Excerpts were
truncated, so many partial labels reflect unseen text. This is not human
review.

## Recommendations

1. Agent-facing retrieval should use abstain=false and treat abstention as
   metadata, not as suppression.
2. Recalibrate the evidence gate before using abstain=true as a default:
   21% false abstention and 0% off-topic rejection is unsafe.
3. Add task-level citation/answer support evaluation; retrieval recall alone is
   insufficient.
4. Optimize R@20/50, not only P@5.
5. Keep page dedupe; add volume diversity only if evaluations show a need.
6. Human spot-check remains outstanding.

## Limits

- Pool-relative qrels, AI labels, no human review.
- Recall uses raw FTS, not rerank or hybrid.
- Citation precision uses qrels accepted sets, not answer correctness.
- No CI, owner acceptance, sufficient coverage or production benchmark.
