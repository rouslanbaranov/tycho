# Length-controlled A/B: v2 vs v3-concise — 2026-11-01

Status: 20 paired dev questions, two independent AI judges per pair. AI-only;
no human review; no holdout claim.

## Design

- Same 20 dev questions as the first A/B.
- v2 baseline: existing answers.
- v3-concise: the v3 answers rewritten to 150-220 words with the same core
  claims, boundaries and citations.
- Mean words: v2 178.2; v3-concise 214.3 (1.2x, versus 8.1x for full v3).
- Answer order randomized; judges saw answer_1/answer_2, not version.
- Two judges per five-pair group.

## Result

| Metric | v2 | v3-concise |
|---|---:|---:|
| consensus wins | 0 | **20** |
| judge votes | 0 | **40 / 40** |
| judge agreement | 20/20 pairs | — |
| mean words | 178.2 | 214.3 |
| mean citations | 3.9 | 12.55 |
| retrieval calls | 12.65 mean | 45.0 mean |

v3-concise won every pair in book, atlas and modeling-and-simulation.

## Interpretation

The first A/B showed a 19/20 v3 win but v3 was 8x longer. This controlled run
keeps the answer near v2 length and v3-concise still wins 20/20 with perfect
judge agreement. Within this AI-judged dev experiment, the gain is not explained
by answer length alone.

The cost remains real: v3-concise still costs about 3.6x retrieval calls and
3.2x citations. The quality-per-call trade-off is not yet measured.

## Limits

- judges are AI-only and did not read evidence;
- v2 baseline is an earlier run, not a same-session control;
- concise answers were rewritten from v3 answers, so some advantage may come
  from the rewrite stage;
- 20 dev questions, no human adjudication;
- no token or latency accounting;
- no fresh holdout.

## Decision

A fresh holdout is now justified, but only with:

1. new questions (v4 and the previous holdout are consumed);
2. prompt v3 with a concise 150-220 word output target;
3. two judges plus adjudication;
4. token/call reporting.
