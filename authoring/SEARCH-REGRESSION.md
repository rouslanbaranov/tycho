# Retrieval regression fingerprints

Status: diagnostic baseline. Not a quality threshold, CI, human review or
sufficiency claim.

## Purpose

Record per-query top-section fingerprints and aggregate hit/MRR metrics so a
post-enrichment rebuild has an explicit drift report.

## Usage

```sh
python3 scripts/search_regression.py --output /tmp/current.json
python3 scripts/search_regression.py \
  --baseline evaluation/search-regression-baseline.v1.json
```

`--fail-on-drift` is available for automation but is not enabled by default.

## Baseline

- Snapshot: b65285cb3ff648c32f94c5fa2d240127eda7b2fb0f5aac620bc11db35ca01873
- 174 answerable queries: 155 qrels v2, 19 filtered phase3.
- hit@1 0.3908, hit@3 0.6264, hit@5 0.7529, MRR 0.5239.
- phase3 hit@5 0.5789; v2 hit@5 0.7742.

These are pre-enrichment diagnostics, not a ranking target.

## Limits

- qrels are author/agent labelled, not human review.
- qrels v2 route snapshot is stale; labels remain pre-enrichment evidence.
- Fingerprints change when content changes; drift is expected after enrichment.
- No quality, capacity or sufficient-coverage inference.
