# Atlas auto-routing experiment — 2026-10-30

Status: negative. No default change. AI qrels; pool-relative; not human review,
CI, owner acceptance or sufficient coverage.

## Method

A structural router compared query-term overlap with atlas card metadata versus
non-atlas route metadata. On an atlas match it used `volume=v11`.

## Results

| Router | Routed | Page hit@1/3/5 | Section |
|---|---:|---|---|
| thresholds 1–4 | 7/150 | .600/.840/.940 | .487/.693/.780 |
| oracle atlas routing | 30/150 | **.707/.880/.960** | **.593/.733/.800** |

Baseline global: .593/.847/.953 page, .480/.700/.793 section.

## Interpretation

- Metadata overlap routes only 7 queries and hurts top-3/top-5.
- Oracle routing shows the available upside, but the structural classifier is
  not accurate enough.
- Keep explicit `volume=v11` for atlas-layer queries; do not auto-route.
- No default change.

## Limits

- Simple metadata overlap; AI qrels.
- No human review, CI, owner acceptance or sufficient coverage.
