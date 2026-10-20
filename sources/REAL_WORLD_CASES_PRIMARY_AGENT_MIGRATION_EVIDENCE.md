# E16-01 — Source Admission Wave 02: First-party AI-assisted Modernization Reports

**Recorded 2026-10-19.** This document *corrects* a false negative from the 43-link first-pass access audit. Access failure in one reader is not proof of a missing source. src.m9-sh04, src.m9-sp02 and src.m9-sp03 were subsequently read through their first-party publishers. Their content is source-reported historical evidence, **not** independent proof that AI-agent work is correct. Original copyright, screenshots, charts, full transcripts and internal code are not licensed for incorporation into Tycho.

## Source identity, dates, exact claim locations

| ID | Creator / venue / original date | Primary original | Disposition |
|---|---|---|---|
| src.m9-sh04 | Talha Naqvi, Shopify Engineering, **2026-09-21** | [Helix — native app migration](https://shopify.engineering/helix) | **Admitted as a bounded historical engineering report** for the checkpoint-and-gate procedure; not a blanket proof of safety |
| src.m9-sp02 | Max Charas and Marc Bruggmann, Spotify Engineering, **2025-11-06** | [1,500+ PRs Later — Honk Part 1](https://www.engineering.atspotify.com/2025/11/spotifys-background-coding-agent-part-1) | **Admitted for self-reported merged PR count, process and estimated savings**; independent defect rate unknown |
| src.m9-sp03 | Devon Edwards Joseph, Spotify Engineering, **2026-04-22** | [Background Coding Agents — Dataset Migration, Honk Part 4](https://www.engineering.atspotify.com/2026/4/background-coding-agents-dataset-migrations-honk-part-4) | **Admitted for scoped rollout and explicit failed approaches**, not the claim all 1,800 dependencies were migrated |

## Claim anchors and limits

| Claim ID | Source section / proof | Statement bounded to the article | Mandatory limitation |
|---|---|---|---|
| evidence.m9-sh04.001 | 'The loop at a glance' | Helix checkpoints generate tests, compare the reference app, enforce two adversarial code reviews, and require human approval by default | Publisher's process description; no independently measured correctness rate |
| evidence.m9-sh04.002 | 'Gate 1: Behavior', 'The UI review gate', 'An engineer closes the loop' | For each checkpoint, behavior tests and visual equivalence checks gate subsequent work; engineer sign-off can be required | Screenshot/visual equivalence is not proof of full functional or security coverage |
| evidence.m9-sh04.003 | 'Helix can also run autonomously' | Engineers can choose to skip approval for bounded runs while keeping quality gates in place | Optional autonomous setting is a design property, not externally audited production guarantee |
| evidence.m9-sh04.004 | Introductory application status | Shopify reports **Shop** shipped natively after a 12-week rebuild; the separate **Shopify App** remained under migration | Do not conflate shipped Shop with Shopify App, or claim all mobile apps done |
| evidence.m9-sp02.001 | Intro and deployment/PR figures discussion | Spotify reports **more than 1,500 agent-generated pull requests were merged** to its production codebase by the 2025 report | Count alone says nothing about rollback, escaped bug rate, or contribution quality |
| evidence.m9-sp02.002 | Impact paragraph | Company estimates **60–90% time savings** for the described migration work | Self-estimate; lacks independently controlled cost/defect study; no guarantee for other teams |
| evidence.m9-sp02.003 | 'New challenges with background agents' | Safety, cost, sandboxing, runtime predictability and validation remain explicit unsolved operational challenges | Do not call merged PR count 'fully safe autonomous deployment' |
| evidence.m9-sp03.001 | 'Dataset migrations can be painful' | The two deprecated datasets had about **1,800 direct downstream pipelines**, plus more indirect dependencies | This is the *scope*, not the number proven automatically migrated |
| evidence.m9-sp03.002 | 'With Honk, context is key' | Scio variation made a universal prompt impractical, so the team **excluded Scio** from that rollout | Negative decision; it materially narrows any 'thousands of pipelines automated' claim |
| evidence.m9-sp03.003 | 'With Honk, context is key' | Missing field-mapping detail caused wrong assumptions; explicit mapping tables and 'leave ambiguous fields unchanged' guidance improved output | Human-authored context and exception routing are essential |
| evidence.m9-sp03.004 | 'With Honk, context is key' | The team **rolled out 240 automated migration PRs** for BigQuery Runner/dbt consumers | *Rolled out PRs* ≠ *240 confirmed merged*: do not conflate |
| evidence.m9-sp03.005 | 'With Honk, context is key' | Most targeted dbt/BigQuery repositories had little automated build-time testing; owners had to perform manual verification before merge | No unattended correctness guarantee for that cohort |
| evidence.m9-sp03.006 | 'What did we learn for the future' | Better schema/test standardization and richer agent context are **planned enablers**, not already validated fleet features | Keep proposal/roadmap separate from deployed functionality |

## Modernization contrasts that become evidence-backed

- **Spotify 2020 (src.m9-sp01) versus 2025–2026 (src.m9-sp02/src.m9-sp03):** 2020 discusses automation as a platform-migration capability; subsequent first-party reports give actual AI-assisted PR experience and its failure conditions. Do not label 2020 data 'LLM-agent results'.
- **Shopify src.m9-sh04 versus Spotify src.m9-sp03:** Shopify reports four mandatory gates and default human review for a mobile UI migration; Spotify found absent unit tests and therefore depended on owner verification for many data-pipeline changes. Both are valid responses to different testing oracles, not interchangeable recipes.
- **Stripe src.m9-st01 / Netflix src.m9-n11:** old/new behavioral comparison and shadow output equivalence remain domain-specific correctness mechanisms; a passing PR or visual gate is not a substitute for billing consistency.
- **Private-source boundary:** These sources are public accounts only. Do not copy the companies' private code, metrics telemetry, schemas or prompt files into Tycho.

## src.m9-n14 / src.m9-n15 status

src.m9-n14 Netflix Conductor (2026-10-14): original [Netflix-hosted URL](https://netflixtechblog.com/netflix-conductor-the-next-chapter-41ad21067649) failed direct retrieval in this session; an [attributed syndication](https://noise.getoto.net/2026/10/14/netflix-conductor-the-next-chapter/) contains the article, including the internal fork/OSS distinction, Cassandra/Timestone data plane, terminal partition precedence and async evaluation, but this is **secondary carriage of a named first-party article**, not direct-source review or independent validation. Record as **corroborated publisher attribution, direct article verification pending**. Do not rehost or quote the syndication in full.

src.m9-n15 'Chaos Engineering Upgraded': original Medium article timed out; original text/sections were **not inspected** this run. Leave **unadmitted** rather than assume the company still follows a 2015 test topology.

This wave records the publication dates and bounded source sections but does not validate every unrelated claim in the 43-candidate register. It remains an input to issue #114's acceptance gate. **Independent technical review pending #121.**
