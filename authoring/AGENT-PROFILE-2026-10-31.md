# Agent retrieval profile — 2026-10-31

Status: AI-adjudicated only. No book/atlas change. Not human review, CI or owner
acceptance.

## Decision

- MCP default: abstain=false.
- Strict refusal remains available with abstain=true.
- Section scope remains best-section-per-document.
- all_sections=true is not the default: it did not improve recall and reduced
  page/volume diversity.

## Measured profile

| Mode | section R@10 | page R@10 | citation precision | zero results |
|---|---:|---:|---:|---:|
| best-section, abstain=false | **.471** | **.576** | **.416** | 0/100 |
| best-section, abstain=true | .387 | .473 | .340 | 21/100 |
| all-sections, abstain=false | .465 | .482 | .405 | 0/100 |

Best-section is retained.

## Why default changed

The gate is not calibrated for agent use:

- 21/100 answerable tasks suppressed under abstain=true;
- 0/20 off-topic probes rejected;
- therefore returning candidates plus answerability metadata is safer than
  returning nothing.

This is an agent-facing MCP default change; the library and CLI keep their
explicit policy arguments. No ranking default changed.

## Cost and diversity

- ~596 approx tokens per 10 results;
- p50 ~51 ms, p95 ~55 ms in the warmed local run;
- 10 unique paths in non-empty top-10; ~3 volumes;
- each result carries section_key, path, heading, title, citation, excerpt and
  next_actions;
- response carries snapshot and citation_scheme.

## Limits

- AI qrels and AI spot-check; no human review.
- 21% false abstention is a measured defect, not fixed calibration.
- No answer-correctness or citation-correctness reader evaluation.
- No CI, owner acceptance or production benchmark.
