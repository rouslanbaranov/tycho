# Tests and coverage

Tycho's tests are behavioral and artifact-oriented. They check contracts,
navigation, hashes, schemas, replay and tool behavior. They do not replace human
review, and a test count is not line coverage.

## Inventory

| Suite | Files | Test definitions |
|---|---:|---:|
| Core tests | 99 | 709 |
| MCP tests | 10 | 123 |
| V12 engine tests | 1 | 21 |

The V12 engine tests are a subset of the core suite. The 123 MCP definitions are
additional MCP-specific tests.

The last full-suite result recorded in
[current state](../authoring/STATE.md) is 709/709 at commit `9615845d`. That is a
historical local result, not a fresh run and not CI.

## What is tested

### Content and metadata

- strict frontmatter and document metadata;
- stable IDs, parent and related links;
- route and section-index consistency;
- book navigation and landing-page structure;
- source and claim references;
- edition inventory and directory migration.

### Evidence and promotion

- source-register structure and reading states;
- source-plan and ledger consistency;
- promotion records and hashes;
- owner-unit and card coverage;
- pattern-source and pattern-owner validators;
- review-report and acceptance records.

### V12

- model and scenario schemas;
- deterministic seeded runs;
- request conservation and invariants;
- convergence and sensitivity checks;
- rollback and censoring behavior;
- committed-run replay hashes.

### MCP

- protocol and schema contracts;
- stdio and HTTP transports;
- search, read, page, outline, context and pattern tools;
- evidence resolution;
- snapshot and index freshness;
- limits, negative inputs and client fixtures.

### Delivery and repository

- boundary and independence checks;
- link and Markdown checks where enforced;
- deployment configuration;
- issue-branch and PR policy tests;
- generated-artifact freshness.

## How to run

Use Python 3.15.0 and install:

```sh
python3 -m pip install -r requirements-validation.txt \
  -r scripts/requirements-routing.txt
```

Run the core suite:

```sh
python3 -m unittest discover -s tests -p 'test_tycho*.py' -v
```

Run MCP tests:

```sh
python3 -m unittest discover -s mcp/tests -p 'test_*.py' -v
```

Run the V12 engine tests:

```sh
python3 -m unittest tests.test_tycho_v12_engine -v
```

Run the repository premerge:

```sh
python3 scripts/premerge_check.py \
  --branch <branch> \
  --issue-title '<exact issue title>'
```

The premerge runs boundary, source, edition, V12 and the core test suite. It does
not run the entire MCP suite unless the relevant checks are included.

## Coverage: what the number means

There is no claimed line-coverage percentage. A test definition count answers
"how many checks are declared", not "how much behavior is covered".

The stronger coverage signals are:

- every canonical page has route metadata;
- every pattern owner is linked to a unit;
- every promotion has a review record and hashes;
- every V12 run replays to the same result hash;
- every MCP tool has an input and output schema;
- every generated index has a freshness check.

These are structural coverage signals. They still do not prove semantic
correctness, source completeness or production behavior.

## Test gaps

- Some tests depend on generated indexes that are not committed.
- Source-register freshness can fail before the test suite runs.
- V12 replay is sensitive to interpreter and hash drift; Python 3.15.0 is pinned.
- MCP tests do not prove HTTP security, OAuth or multi-tenant isolation.
- There is no continuous per-PR CI; milestone verification is separate.
- No line or branch coverage report is published.
- The evidence layer has more entries than independent reviews.

## CI policy

GitHub Actions is milestone-only. It does not run on push, pull request or a
schedule. A green local premerge is evidence, not CI. A merged PR is not CI.
A skipped workflow is not a pass.

## Reading the test result

When reading a test report, ask:

1. Which commit and Python version?
2. Were dependencies installed?
3. Was the index rebuilt?
4. Which suite ran: core, MCP, V12 or all?
5. Were any tests skipped or deselected?
6. Was the result local or CI?

A count without those answers is not enough.
