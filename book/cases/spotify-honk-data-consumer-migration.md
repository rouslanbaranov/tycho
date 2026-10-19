# Spotify — Honk: why data-lineage context and tests determine safe AI migration scope

**Case ID:** `case.spotify.honk-dataset-consumer-migration` | **Owner:** M9 E16-05 #118 | **Status:** first-party evidence-backed draft; independent reviewer pending.  
**Primary:** SP03, Devon Edwards Joseph, [Spotify Engineering, 2026-04-22](https://www.engineering.atspotify.com/2026/4/background-coding-agents-dataset-migrations-honk-part-4), sections **Dataset migrations can be painful**, **Simplifying fleet migrations with Backstage**, **With Honk, context is key**, **What did we learn for the future**. Secondary context: SP02, [Honk Part 1](https://www.engineering.atspotify.com/2025/11/spotifys-background-coding-agent-part-1), Nov 6, 2025. These report distinct populations and dates.

## Original migration and constraints

Spotify planned to deprecate two heavily used datasets to release richer replacements. Its lineage graph indicated approximately **1,800 direct downstream data pipelines**, and several thousand indirect dependencies, spanning **BigQuery Runner, dbt and Scio**. The manual work estimate was about **10 engineering weeks**. That estimated baseline is *not* an independently controlled timer.

The engineering team used Backstage endpoint lineage/Codesearch to identify affected repositories and Fleetshift to orchestrate changes. Honk could create code PRs, but it did not have the feature-rich tools and external context retrieval options now often assumed for coding agents. This made precise per-framework field mappings critical. [SP03, background and platform sections].

## Iteration: three failure boundaries

The first attempt to derive migration instructions from a human-oriented guide let the agent infer wrong field mappings. The team corrected this by writing **explicit mapping tables** and by telling the agent to **leave ambiguous business-meaning transformations unchanged**, inserting comments for a human owner. That is an important *positive use of refusal* in code migration.

Scio pipelines were too varied for a general instruction set; the team **stopped attempting to automate that framework's migration in this wave**. BigQuery Runner and dbt were more standardized and could be handled with narrower context. However, many of those repositories had **little or no build-time unit testing**. Consequently, Honk could not verify itself using its usual correction loop; pipeline owners had to perform manual tests before merging changes. [SP03, "With Honk, context is key"].

```mermaid
flowchart TD
  A[Deprecated dataset] --> B[Backstage dependency lineage]
  B --> C[Find consumer repositories]
  C --> D{Framework / documented mapping}
  D -->|Scio or semantics ambiguous| H[Human-owned migration / stop automation]
  D -->|dbt or BigQuery Runner| E[Honk + explicit mapping contract]
  E --> F[Reviewable migration PRs]
  F --> G{Automated tests available?}
  G -->|yes| I[Run deterministic checks + owner review]
  G -->|no| J[Owner tests manually before merge]
  I --> K[Accepted changes, documented evidence]
  J --> K
```

**Text alternative:** lineage identifies affected data consumers. A framework/semantic gate excludes variable Scio or ambiguous mappings; the remaining standardized cohorts get agent-generated PRs. Tests determine whether validation can be automated; missing tests route changes to explicit human-owner verification. The graph is original and does not claim all consumer pipelines were completed.

## Quantitative claims and why they cannot be mixed

| Period / source | Publisher-reported number | Correct interpretation |
|---|---|---|
| SP03 April 2026 | **~1,800** direct downstream pipelines | Original potential migration scope for two deprecated datasets |
| SP03 April 2026 | **240** automated migration PRs **rolled out** | Rollout metric; **not** proof of 240 merges or of 1,800 migrations complete |
| SP03 April 2026 | **~10 engineering weeks** | Hypothetical estimated manual effort; not measured savings or quality |
| SP02 Nov 2025 | **>1,500 AI-generated PRs merged** across Spotify | Earlier cross-fleet background-agent total; **not** identical to SP03's 240 targeted PRs |
| SP02 Nov 2025 | **60–90% estimated development time saving** on described migrations | Self-reported estimate; no claim of independently audited defect rate |

## Counterevidence and decision transfer

An agent is not automatically safe because its input is 'structured'. Missing field semantics produced wrong assumptions until explicit mapping tables were written. Even then, the target repositories lacked automatic tests, so *human verification remained necessary*. The scalable architecture here is **lineage + bounded transformation context + supervised PR workflow**, not unattended SQL code generation.

For another organization, test one standardized framework cohort, pin dataset schema versions and source-lineage snapshot, require a field-level oracle and detect missing test coverage before expansion. Mark untestable or ambiguous cases for owners; if data governance cannot define equivalence, the correct agent output is *insufficient evidence*, not a speculative mapping. A failed mapping, deferred framework or PR still awaiting merge is a first-class result.

## Source and review limits

All performance and adoption counts are attributed to Spotify and their publication dates. The company did not report in this article a controlled escaped-defect benchmark or complete migration rate across all consumers. Agent-produced code or internal prompts cannot be imported into Tycho without rights. Case remains a **draft pending #114 per-claim admission and #121 independent review**; avoid introducing private employer examples.
