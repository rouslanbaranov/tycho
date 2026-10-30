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

## A01

HEAD `9deabb77a011911b3f7c7ecc1688205cb3d834ca`; snapshot `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`. 15 atlas queries; cards by chapter: C01 Ambassador, Sidecar; C02 Asynchronous Request-Reply, Service Discovery; C03 Splitter, Claim Check; C04 Transactional Outbox, Saga; C05 TTL-Based Expiration, Cache Invalidation; C06 Sharding, Backup/PITR/Restore; C07 Circuit Breaker, Bulkhead; C08 Fencing Tokens. 15 distinct cards across 8 chapters, at most 2 per chapter. Page candidates 60; section candidates 60. Page grades {0: 18, 1: 26, 2: 16}; section grades {0: 18, 1: 26, 2: 16}.

Questions and grades were created from read cards and related book sections, without rankings; section identities are read from the sections table. Standalone cards use overview, while embedded H3 cards use the broader H2 Entry inventory. Validator passed. Candidate pools are incomplete and individual card relevance may be broader at section level. AI-adjudicated only; not human review, CI, owner acceptance or sufficient coverage. No question rejected.

## A02

HEAD `9deabb77a011911b3f7c7ecc1688205cb3d834ca`; snapshot `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`. 15 atlas queries; cards by chapter: C01 Anti-Corruption Layer, Self-Contained Service; C02 Gateway Aggregation, Backend for Frontend; C03 Message Filter, Resequencer; C04 CDC, Materialized View; C05 Cache-Aside, Write-Through; C06 Read Replicas, Partitioning; C09 Static Content Hosting; C10 Parallel Run, Dark Launching. 15 distinct cards, 11 owning pages, 8 chapters, at most 2 per chapter. Page candidates 60; section candidates 60. Page grades {0: 17, 1: 28, 2: 15}; section grades {0: 17, 1: 28, 2: 15}.

Questions and grades were created from read cards and related book sections, without rankings; section identities are read from the sections table. Standalone cards use overview, while embedded H3 cards use the broader H2 Entry inventory. Validator passed. Candidate pools are incomplete and individual card relevance may be broader at section level. AI-adjudicated only; not human review, CI, owner acceptance or sufficient coverage. No question rejected.

## V01

HEAD `9deabb77a011911b3f7c7ecc1688205cb3d834ca`; snapshot `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`. 15 V12 queries; owning chapters C01 Foundations 2, C02 Contracts 3, C03 Deterministic and DES 3, C04 Monte Carlo 3, C05 Decision integration 2, C07 Validation and limits 2. Page candidates 60; section candidates 60. Page grades {0: 16, 1: 24, 2: 20}; section grades {0: 16, 1: 24, 2: 20}.

Questions and judgments were made from V12 book-page bodies, with exact H2 identities read from the sections table and no ranking data. The V12 index was inspected for structure only; artifact records were not individually adjudicated. Validator passed. Synthetic models and incomplete candidate pools limit coverage. AI-adjudicated only; not human review, CI, owner acceptance or sufficient coverage. No question rejected.

## V02

HEAD `6f6e242dd26a98bd77b37cb1268ca3104a3082bb`; snapshot `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`. 15 V12 queries; owning chapters C02 Contracts 3, C03 Deterministic and DES 3, C04 Monte Carlo 3, C06 Migration simulation 3, C07 Validation and limits 3. Page candidates 60; section candidates 60. Page grades {0: 15, 1: 22, 2: 23}; section grades {0: 15, 1: 22, 2: 23}.

Questions and judgments were made from V12 book-page bodies, with exact H2 identities read from the sections table and no ranking data. One preliminary question was replaced to maintain chapter coverage. Validator passed. Synthetic model assumptions and incomplete candidate pools limit coverage; artifact records were not individually adjudicated. AI-adjudicated only; not human review, CI, owner acceptance or sufficient coverage.

## B01–B03 broad-coverage rework

HEAD `1a84cc5a024af558192e43342039e84c1057094e`; section snapshot `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`. These entries supersede the earlier narrow B01–B03 entries.

- B01: 15 queries, 5 numbered volumes and 5 chapter topics; 3 questions per topic (V01/C04, V02/C03, V03/C06, V04/C07, V05/C05). 60 page candidates and 60 section candidates; page grades {0: 16, 1: 25, 2: 19}, section grades {0: 16, 1: 25, 2: 19}. Batch validator passed.
- B02: 15 queries, 5 numbered volumes and 5 chapter topics; 3 questions per topic (V06/C07, V07/C05, V08/C01, V09/C05, V10/C02). 60 page candidates and 60 section candidates; page grades {0: 15, 1: 29, 2: 16}, section grades {0: 15, 1: 29, 2: 16}. Batch validator passed.
- B03: 15 queries, 5 numbered volumes and 5 chapter topics; 3 questions per topic (V11/C10, V12/C06, V01/C05, V05/C04, V08/C07). 60 page candidates and 60 section candidates; page grades {0: 18, 1: 27, 2: 15}, section grades {0: 18, 1: 27, 2: 15}. Batch validator passed.

Overall: 45 queries, 12 distinct numbered volumes and 15 distinct chapter topics, with at most 3 queries per topic. Twelve questions have a direct grade-2 published case page: B004 Shopify, B007 Netflix GC, B010 LinkedIn Kafka, B013 Netflix Cassandra; B016 Discord indexing, B019 Uber Cinnamon, B022 Airbnb Bazel, B025 Netflix Data Projects; B031 Meta ingestion, B037 Netflix cloud migration, B040 Discord message storage, B043 Netflix Chaos Kong. Case pages are under book/cases rather than a numbered volume; their topic assignments above use related numbered-volume material, which may be graded as background rather than a direct answer. Independently, grade-2 candidates include pages from all 12 numbered volumes and 15 distinct numbered chapters.

Questions and candidate judgments were authored from the read page and case bodies, with exact H2 or indexed overview identities from the read-only sections table; no current search ranking or old narrow labels were used. No question was rejected. The 12 case questions describe publisher-reported historical examples and should not be generalized to current deployments. Relevance pools are small and non-exhaustive; the validator checks consistency, not judgment accuracy. AI-adjudicated only: not human review, CI, owner acceptance or sufficient coverage. No merge was performed. Earlier batches record different HEADs; a future merge requires resolving the commit mismatch.
