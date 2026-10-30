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

## B04

HEAD `7918391fe10bc3c2f91e8358b3ee768cf70fbea2`; section snapshot `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`. Fifteen book queries; coverage by owning chapter: V01/C01 3, V02/C07 3, V04/C04 3, V05/C07 3, V07/C04 3. Page candidates 70; section candidates 70. Page grade counts {0: 15, 1: 30, 2: 25}; section grade counts {0: 15, 1: 30, 2: 25}.

Questions and candidates were selected and adjudicated from read book bodies, with exact H2 identities obtained from the read-only sections table; no ranking data used. Batch validator passed. Synthetic examples and restricted candidate pools limit coverage; judgments are AI-adjudicated only, not human review, CI, owner acceptance or sufficient coverage. No questions rejected.

## B05

HEAD `7918391fe10bc3c2f91e8358b3ee768cf70fbea2`; section snapshot `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`. Fifteen book queries; coverage by owning chapter: V03/C02 3, V06/C06 3, V08/C05 3, V09/C01 3, V10/C05 3. Page candidates 60; section candidates 60. Page grade counts {0: 15, 1: 26, 2: 19}; section grade counts {0: 15, 1: 26, 2: 19}.

Questions and candidates were selected and adjudicated from read book bodies, with exact H2 identities obtained from the read-only sections table; no ranking data used. Batch validator passed. Synthetic examples and restricted candidate pools limit coverage; judgments are AI-adjudicated only, not human review, CI, owner acceptance or sufficient coverage. No questions rejected.

## B06

HEAD `7918391fe10bc3c2f91e8358b3ee768cf70fbea2`; section snapshot `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`. Fifteen book queries; coverage by owning chapter: V01/C02 3, V02/C05 3, V04/C01 3, V07/C01 3, V09/C03 3. Page candidates 60; section candidates 60. Page grade counts {0: 18, 1: 22, 2: 20}; section grade counts {0: 18, 1: 22, 2: 20}.

Questions and candidates were selected and adjudicated from read book bodies, with exact H2 identities obtained from the read-only sections table; no ranking data used. Batch validator passed. Synthetic examples and restricted candidate pools limit coverage; judgments are AI-adjudicated only, not human review, CI, owner acceptance or sufficient coverage. No questions rejected.

## Cross-batch commit note

B01–B03 record HEAD `a6d962ce9c87931480722038ad335ba8c0f116a1`; B04–B06 record HEAD `7918391fe10bc3c2f91e8358b3ee768cf70fbea2`. The section snapshot is the same. The merge script requires a single content commit across all batches, so this mismatch must be resolved before merging; no earlier batch was modified in this run.
