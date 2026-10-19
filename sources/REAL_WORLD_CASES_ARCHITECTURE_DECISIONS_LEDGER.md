# M9 / E16-01 — Source Admission Wave 04: Ownership Boundaries and Online Migration

**Verified:** 2026-10-19, directly against six original first-party blog publications. **Evidence class:** the original publisher's design narrative, with some dated quantitative context; not an independent performance experiment, archival license or 2026 deployment inventory. This wave covers **U01, U02, SH01, SH02, SP01 and ST01** and preserves source-specific sections and historical time windows.

| ID | First-party author/date | Original link | Historical context |
|---|---|---|---|
| U01 | Adam Gluck; Uber Engineering; **2020-07-23** | [Introducing Domain-Oriented Microservice Architecture](https://www.uber.com/us/en/blog/microservice-architecture/) | DOMA after large multi-team service sprawl |
| U02 | René W. Schmidt; Uber Engineering; **2015-07-28** | [Project Mezzanine: The Great Migration](https://www.uber.com/us/en/blog/mezzanine-codebase-data-migration/) | 2014 trip-store migration |
| SH01 | Kirsten Westeinde; Shopify Engineering; **2019-02-21** | [Deconstructing the Monolith](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity) | Initial modular-monolith decision |
| SH02 | Philip Müller; Shopify Engineering; **2020-09-16** | [Under Deconstruction](https://shopify.engineering/shopify-monolith) | Follow-up describing unfinished componentization |
| SP01 | Saunak 'Jai' Chakrabarti and Jenni Lee; Spotify Engineering; **2020-06-25** | [Tech Migrations, the Spotify Way](https://engineering.atspotify.com/2020/6/tech-migrations-the-spotify-way) | Pre-LLM fleet-change governance |
| ST01 | Jacqueline Xu Atlas; Stripe Engineering; **2017-02-02** | [Online migrations at scale](https://stripe.com/blog/online-migrations) | Active subscription data-model rewrite |

## Specific bounded claims and contradictory lessons

| Claim ID | Exact original section | Admissible conclusion | Rejection / limits |
|---|---|---|---|
| U01.001 | 'Introduction' | Uber described ~**2,200 critical microservices** by 2020 and attempted to manage complexity with domains | Historical scale report, **not** a universal minimum viable service count |
| U01.002 | 'Motivations' / 'The evolution of Uber's microservice architecture' | An incident spanned ~**50 services / 12 teams**; domains/gateways/layers were introduced to restore comprehensible ownership | One observed complexity anecdote; **do not** imply every request fans out 50 services |
| U01.003 | 'Domain-Oriented Microservice Architecture' and 'Layering' | DOMA organizes existing services behind domain-owned interfaces and explicit layers | Opposes claim that DOMA requires every domain to become one service |
| U02.001 | 'Background' | In early 2014, roughly **100** backend services still relied heavily on one PostgreSQL trip store while trips grew ~**20% monthly** | Company context/period, not a transaction-volume benchmark |
| U02.002 | 'From SQLAlchemy to Schemaless' | Migration milestones: IDs→UUIDs, new trip model, backfill, mirrored writes, query rewrite, repeated validation | Company *reported sequence*, not one-click storage driver replacement |
| U02.003 | 'Execution' | Final concentrated cutover push took **six weeks**; completed roughly **one month before Halloween 2014** without the predicted production outage | Historical anecdote, not guarantee of no downtime for every scheme |
| U02.004 | 'The New Trip Store' | Schemaless was Uber's **own sharded datastore built over MySQL**, not an off-the-shelf managed NoSQL engine | A common oversimplification; source describes operational requirements and API limits |
| SH01.001 | 'Modular Monoliths' | Shopify chose defined domain boundaries **within one deployable application**, avoiding additional network hops and deployment overhead | Valid alternative to premature microservices under different team/transaction conditions |
| SH01.002 | 'Shopify’s Implementation of the Modular Monolith: Componentization' | Early 2017 code organization transition from Rails MVC folder types toward business-domain components | Not proof all components were already isolated in 2019 |
| SH02.001 | 'The Status Quo' | In September 2020 Shopify explicitly said architectural changes were **far from finished** and the concrete implementation had evolved | Contradicts simplistic 'Shopify completed modularization' claims |
| SH02.002 | 'What We Learned So Far' / 'Status Quo' | Enforced dependency rules and **exceptions ownership** were gradual; constraints raised developer design awareness | Does not guarantee cross-domain transactional isolation |
| SH02.003 | 'Outlook' | Storefront rendering was split due to independent read-only high-throughput needs; credit-card vaulting separate for sensitive data boundary | **One company can combine modular monolith and selected services**; false binary forbidden |
| SP01.001 | 'Adieu, long tail — 1. Ruthlessly prioritize' | Spotify coordinated migrations through TAG-negotiated priorities, cost/owner/deadline map and Backstage | Company-wide governance and ownership intervention |
| SP01.002 | '2. Product-ify migrations' | Internal platform PM owns adoption; alpha/beta migration gates, Tech Insights visibility and long-tail support | Goal of 100% adoption is a policy, not independently audited measured achievement |
| SP01.003 | '3. Automate, automate, and move up the stack' / 'Going forward' | Automated PRs and hiding **99% of migrations** are discussed; the **99% was a goal** | **Not** 2020 production proof of AI-agent completion or 99% hidden changes |
| ST01.001 | 'A pattern for online migrations' and Parts 1–4 | Sequence: **dual write old/new → switch all reads → switch all writes → remove legacy data** | Ordering is important; use end-to-end invariant checks and rollback before retirement |
| ST01.002 | 'Part 1: Dual writing' and 'Part 2: Changing all read paths' | Stripe used phased rollout, backfill and read-comparison mechanisms such as GitHub Scientist | Company-authored method, not proof that all domains are byte-identical |
| ST01.003 | 'Our example migration: Subscriptions' | The transition separated embedded subscription representation from Customer to own subscription rows | Do not conflate Stripe's Customer/Subscription model with Uber's separate MySQL-backed Schemaless trip store |

## Decision-transfer corrections

- **Netflix N01 versus Shopify SH01/SH02:** choosing cloud-native services or component-enforced monolith is context-dependent. Shopify also extracted select high-throughput/sensitive responsibilities; 'Shopify never uses services' is false.
- **Uber U01 versus U02:** U02 covers a **2014 transactional data-store scaling** migration; U01 addresses **2018–2020 coordination** in thousands of microservices. Do not collapse into one timeline/state.
- **Spotify 2020 SP01 versus 2025/2026 SP02/SP03:** three separate historical periods. Earlier platform PR automation does not establish LLM use before later reports.
- **Stripe ST01:** a passing migration must preserve the intended data semantics at every authority switch; a simple total-row count is insufficient.
- **Copyright:** link the original section/URL/author; no reuse of original proprietary production schematics, screenshots or full text. Diagrams in `book/cases/` are newly authored abstractions.

## Status and remaining admissions

This is a **bounded first-party source review**, not a reread of every sentence of the six articles or reproduction of internal results. In combination with wave 01 (5 sources), wave 02 (3), and wave 03 (5), **19/43** sources now have at least one explicitly anchored historical claim. **24** candidates still need direct scoped claims or a documented exclusion decision. Inaccessible primary bodies N14/N15 remain unresolved. #114 and independent cross-case review #121 remain open.
