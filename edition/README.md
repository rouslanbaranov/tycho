# Tycho 2026.10 — First Markdown Edition

Version: **2026.10.0**. Publication state: **First Markdown Edition; frozen content inventory, delivered through #214**.

## Read the book

Start with the [authoritative contents](../book/README.md). The edition has ten volumes, 69 primary chapters and 69 bounded primary technical pages. Fifty-one supporting technical/case pages and 15 existing navigation entries remain available: the complete canonical corpus contains **215 documents**. The 29 historical cases and six synthetic playbooks form one applied layer, not an eleventh volume.

Each new volume contributes a cross-chapter synthetic scenario, synthesis, counterexample, prerequisite route and evidence limits. Each chapter states its question, worked conclusion, failure counterexample, actual section route and previous/next/prerequisite/source navigation. The accepted technical explanations retain their existing opaque identities and source ledgers.

## Scope and acceptance

The owner confirmed substantive acceptance of the 69 manuscripts at `986b1ddbe985079b7c647182fcf1c2fc8911d96c`; PR #218 merged that content and PR #219 reconciled its status. This assembly starts at main `08ac0da83c30d2f2e6aea3446142ad183987f01c`.

New landing syntheses are original editorial work and are self-checked, not independently certified. The assembly changes placement, hierarchy and relative navigation; it does not rerun research or promote old metadata into fabricated signed reviews. Original source versions, access restrictions, synthetic examples, proposed experiments and historical nonclaims remain explicit in their owning pages. No benchmark or production architecture is implied.

## Reversible migration and provenance

- [Selected outline and minted landing IDs](outline.json) records all ten volume and 69 chapter identities, editorial input, original paths and final paths.
- [Migration map](migration.json) records all 69 old/new paths, unchanged page IDs, old/new parents, original metadata, baseline document/body hashes, migrated-payload hashes and unchanged external URL sets.
- `sources/document-identities.json` records live canonical paths. IDs are independent of volume numbers and paths.
- The baseline Git commit preserves the exact pre-migration payload. To reverse the assembly, use a new revert commit or restore the baseline on an isolated branch, then use the map to inspect every reverse path/parent. Never overwrite shared history or simply undo paths while retaining the newer index.
- Repository-local incoming Markdown links are rewritten to canonical destinations. Old topic-page paths are retired without duplicate canonical stubs. Existing external GitHub commit URLs remain pinned historical evidence. Consumers using an old raw path must resolve it through the migration map or use the old pinned revision; this Markdown edition does not claim HTTP redirects.

Every primary manuscript originally answered one bounded chapter question. Original bodies range from 1,373 to 3,348 whitespace-delimited words, including local evidence and examples; no page was split merely to meet a fixed count. The exact range and all hashes are emitted by the edition validator. Additional independently owned subquestions can receive new page IDs in a later edition rather than silently reusing an existing identity.

## Reproducible checks

Install the pinned-enough validation dependency ranges from the repository requirements files, then run from the repository root:

```bash
python3 scripts/route_index.py build
python3 scripts/route_index.py check
python3 scripts/validate_edition.py
python3 scripts/premerge_check.py --branch feature/TYCHO-214-assemble-and-release-the-complete-ten-volume-tycho-book --issue-title '[E14-14] Assemble and release the complete ten-volume Tycho book'
python3 scripts/validate_knowledge.py --mode strict --json
python3 scripts/validate_m9_cases.py
python3 scripts/validate_m9_cases.py --self-test
python3 -m unittest discover -s tests -p 'test_m9*.py' -v
```

For actual Mermaid syntax parsing, install the existing package lock with `npm ci --ignore-scripts` inside `tools/mermaid`, then run `node tools/mermaid/check.mjs --root .`. Syntax parsing is distinct from browser layout. Visual rendering and live MCP remain owner-cancelled, not passed. The milestone-only GitHub Actions policy is unchanged.

`scripts/assemble_edition.py` is an explicit one-time migration tool: default dry-run, deliberate `--apply`, refusal to apply twice. Reproduce assembly from the recorded baseline plus the reviewed `edition/outline.json` and assembly script. `scripts/validate_edition.py --write-inventory` deliberately freezes the resulting book/provenance/schema/index membership; ordinary validation never rewrites it.

## Freeze and limitations

The inventory records path and SHA-256 for every canonical Markdown document, source registry, schema, routing index and edition mapping/input. It excludes its own file and validation logs to avoid self-referential hashes. The named release pins the final Git commit, which also preserves the authoring reports, scripts and tests. Validation must pass on that same content tree before release.

Offline checks establish structure, retained payloads, metadata, approximate Markdown anchors and parser-valid Mermaid. They do not prove every external server currently responds, every published claim is universally true, or any example runs on a target deployment. Previously documented source-access limitations and owner waivers remain in force. Later lexical/hybrid retrieval, MCP/onboarding, shared specialist and deployment are separate workstreams.
