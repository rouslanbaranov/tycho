# Qrels v4 batch report

Codex appends one short entry per batch:

```text
Batch: B01
Split: book
IDs: V4-B001–V4-B015
HEAD:
Snapshot:
Page candidates:
Section candidates:
Outcome:
Limitations:
```

Do not claim human review, CI, owner acceptance or sufficient coverage.
# Batch report

## B01

HEAD `a6d962ce9c87931480722038ad335ba8c0f116a1`; snapshot `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`. 15 book queries; 66 page and 66 section candidates. Page grades {0: 20, 1: 26, 2: 20}; section grades {0: 21, 1: 25, 2: 20}.

Questions and judgments were created from directly read cache pages and their H2 sections; the section keys were looked up in the read-only sections table. Validator: PASS. Limited to one chapter and synthetic examples; AI-adjudicated only, not human review, CI, owner acceptance, or sufficient coverage. One overlapping question was replaced before completion.

## B02

HEAD `a6d962ce9c87931480722038ad335ba8c0f116a1`; snapshot `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`. 15 book queries; 64 page and 64 section candidates. Page grades {0: 19, 1: 21, 2: 24}; section grades {0: 19, 1: 21, 2: 24}.

Questions and judgments were created from directly read pages on streams, replay and task lifetimes; section identities came from the read-only sections table. Validator: PASS. Synthetic examples and one topic area limit coverage; AI-adjudicated only, not human review, CI, owner acceptance, or sufficient coverage. No question was rejected.

## B03

HEAD `a6d962ce9c87931480722038ad335ba8c0f116a1`; snapshot `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`. 15 book queries; 68 page and 68 section candidates. Page grades {0: 20, 1: 27, 2: 21}; section grades {0: 20, 1: 27, 2: 21}.

Questions and judgments were created from directly read vector retrieval pages and their H2 sections; section identities came from the read-only sections table. Validator: PASS. Synthetic examples and one chapter limit coverage; AI-adjudicated only, not human review, CI, owner acceptance, or sufficient coverage. No question was rejected.
