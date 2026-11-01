# Entry promotion rules

Status: active. Applies to every pattern-atlas entry promoted to `sufficient`.

This document defines the only permitted workflow, the evidence gate, promotion and
rebind rules, bookkeeping, and the chat report templates. `AGENTS.md` rule 39 requires
this workflow.

## 1. One entry at a time

Work on exactly one entry until it is promoted, merged and reflected in bookkeeping.
Do not start the next entry while the current one is in review, rebind or merge.

An entry is closed only when all of these are true:

1. its promotion record exists and validates;
2. the PR/MR is merged into `main`;
3. timing and forecast are updated;
4. charts are regenerated and shown only after promotion;
5. STATE and handoff reflect the new count.

If review fails, fix the same entry. Do not park it and start another.

## 2. Roles and boundaries

- **Lane** owns the owner section, inline card, lane note and lane-local commit. It
  must not edit shared JSON, run review, promote or start another entry.
- **Integrator** owns metadata, card split, refresh, preflight, full suite and branch
  push. It must not claim review pass, promotion or acceptance.
- **Independent reviewer** owns the verdict, evidence findings and rebind approval. It
  must not edit the repository or waive its own gate.
- **Parent** owns the promotion record, rebind, PR/MR merge, bookkeeping and charts. It
  must not claim a pass without a saved report.

The lane prepares content only. The integrator prepares a reviewable candidate. The
reviewer decides. The parent records the decision. No role may skip the next one.

## 3. Evidence gate

A promotion requires all four technical dimensions and the decision evidence to be
supported. Each dimension must separate source claims from Tycho synthesis.

- Bind exact public sources and revisions.
- Quote verbatim; do not paraphrase inside a binding quote.
- Label original guidance as `Tycho synthesis` in the owner section and card.
- Do not use a source for a claim it does not make.
- A related pattern with a different scope is not identity evidence.
- Decision evidence must match the card and owner text.
- If a dimension cannot be source-bound, keep it partial. Do not promote.

Promotion also requires:

1. preflight PASS for the entry and every rebind neighbour;
2. `validate_sufficient_promotions.py` PASS;
3. independent review PASS, minors allowed and recorded;
4. saved report with SHA-256 in `authoring/ai-reviews/`;
5. exact owner and card hashes at the reviewed commit.

## 4. Workflow

### 4.1 Select and inspect

- pick one remaining entry;
- identify its owner page and promoted neighbours;
- identify every promotion bound to the same page or card;
- decide whether the card must be split to a dedicated page.

### 4.2 Lane

- edit only the target owner section, its card and a lane note;
- preserve promoted sibling sections byte-for-byte;
- do not touch shared JSON, generated files or derived indexes;
- run line length and boundary checks;
- commit lane-local and report hashes, quotes and any unbound dimension.

### 4.3 Integrator

- cherry-pick the lane into a clean branch from current `main`;
- add sources, ledger records, source-plan units, registry and owner-units;
- split a shared card when a promotion-bound card still sits on a chapter page;
- preserve promoted sibling sections and cards;
- refresh artifacts, preflight, and run the full suite once under Python 3.15;
- push the branch and open a PR/MR only after the review pass.

### 4.4 Independent review

The reviewer receives a bounded packet: entry JSON, owner sections, cards, exact
hashes, and for a rebind the promotion record plus old/new section and card hashes.
The reviewer must not run tests or write to the repository.

A pass with minors is accepted. Majors and blocking findings require remediation and
a delta review. Save the report verbatim and add its SHA-256 to the index.

#### 4.4.1 Delta review

A delta review is used only after a fail and remediation of the same entry. It is
not a new full review and not a waiver of the gate.

The delta packet must contain:

- prior finding IDs, severity and the remediation for each;
- only the changed artifacts: owner section, card, evidence JSON and hash proof;
- old and new hashes for every rebind;
- a statement of what was not changed;
- the current HEAD.

The reviewer must:

- recheck each prior blocking and major finding;
- check the changed artifacts for regressions;
- mark every prior finding resolved or unresolved;
- approve or reject each rebind;
- return a verdict and explicit limits.

A delta pass allows promotion with recorded minors. A delta fail returns the same
entry to remediation: no promotion and no next entry. Save the delta report like a
full report and index its SHA-256.

### 4.5 Promotion and rebind

- append or update the promotion record with reviewed commit and exact hashes;
- rebind a promoted neighbour only when its section, card and promoted hashes are
  proven unchanged and the reviewer approved the rebind;
- never raw-update a hash without the proof and approval;
- set coverage to sufficient only after a pass;
- update registry, owner-units, delivery evidence and derived counters.

### 4.6 PR/MR and merge

- open a PR/MR from the integration branch;
- include the review report, validators and known limits;
- merge only after the promotion records validate;
- do not push directly to `main`.

### 4.7 Bookkeeping after promotion

- append the measured interval to `authoring/promotion-entry-timing-*.json`;
- recompute the forecast from all entries and actual tier counts;
- regenerate the full timing chart and the latest-15 chart;
- use only the promoted entry name as a chart label; no rebind suffixes;
- date chart filenames by the current update date;
- update STATE, HANDOFF and PROMOTION-TIMING;
- open a bookkeeping PR/MR and merge it.

Charts are produced only after promotion. Intermediate reports contain no chart
section and no chart links.

### 4.7.1 Green gate after promotion

Do not start the next entry until the full suite passes at the promotion merge
commit under Python 3.15. If any test fails, fix it in a separate green-main
change before continuing.

The green-main change must:

- update hardcoded promotion counts and the AI-review index;
- update evaluation qrels whose verbatim excerpts cite changed owner text;
- refresh V12 `protected-baseline.json` for every changed book page and
  promotion record;
- rebuild the section FTS index and the route index;
- update the V12 qrels snapshot and source-plan route snapshot;
- scan V12 links to book pages and fix broken links;
- record the full-suite result in the PR/MR;
- complete the mandatory V12 semantic review (section 4.7.2).

A promotion is not complete while the suite is red.

### 4.7.2 Mandatory V12 semantic review

Every promotion requires a V12 semantic review before the next entry starts. A
mechanical link scan, V12 schema test or protected-baseline refresh is not a
semantic review and cannot substitute for it.

The review is independent and read-only. Its packet must contain:

- the current V12 volume documents that discuss patterns or decision records;
- `edition/v12/decisions/*.json`;
- the changed owner sections and cards from the promotion;
- current counts: entries, sufficient, owner-accepted;
- the V12 protected baseline and link-scan result.

The reviewer must check:

- claims about pattern coverage, evidence, promotion and review;
- the one-way link rule and every linked pattern identifier;
- whether linked patterns are still described correctly;
- decision-record semantics and unresolved-evidence wording;
- stale counts, examples or references caused by the promotion;
- contradictions between V12 and the changed V1-V11 sections.

A pass may record minors. A fail blocks the next entry and requires a V12 fix and
delta review. Save the report and index its SHA-256 like any other review.

A reviewer may conclude that the promotion has no semantic V12 impact, but that
conclusion must be explicit in the report. Absence of a finding is not a skip.

## 5. Rebind rules

A neighbour promotion may be rebound only when all are true:

1. the promoted section and card are byte-identical;
2. the old page hash matches the promotion record;
3. the new page hash is recorded;
4. the page diff is limited to the target entry and permitted metadata;
5. the reviewer approves the rebind;
6. the new hashes are recorded in the promotion record.

If any condition fails, re-review the neighbour or leave the promotion suspended
with a recorded reason. Do not silently rebind.

## 6. Python

Use Python 3.15.0 for validation, V12 work, refresh and tests. Do not use the 3.9
interpreter for final evidence.

## 7. Chat report templates

Reports use the owner's language. Keep the section order exactly.

### 7.1 Lane started or lane complete

```text
## B<n> <Entry>: lane зафиксирован, integrator работает

### Lane

<commit, files, hashes, bindings, caveat>

### Integrator

<what the integrator is doing now>

### Текущее

| Показатель | Значение |
|---|---:|
| sufficient | **<n> / 145** |
| owner-accepted | **<a> / <n>** |
| remaining | **<r>** |
| timing entries | <t> |
| mean | **<m> min** |
| forecast | **<o> / <b> / <p>** |
| main HEAD | `<sha>` |

При review pass → **<n+1>**.
```

### 7.2 Integrator complete, review pending

```text
## B<n> <Entry>: интегрирован, review запущен

### Integrator

<branch, HEAD, metadata, card split, preflight, suite>

### Review

<packet scope and what the reviewer checks>

Verdict пока не получен.

### Текущее

<table as above>

При review pass → **<n+1>**.
```

### 7.3 Review fail and remediation

```text
## B<n> <Entry>: review fail, findings исправлены

### Review

<blocking and major findings>

### Remediation

<what changed>

### Проверки

<preflight, validators, hashes>

### Текущее

<table as above>

Delta review отправлен; promotion не выполнен.
```

### 7.4 Delta review

```text
## B<n> <Entry>: delta review

### Prior findings

- <id>: <resolved/unresolved> — <evidence>

### Changed artifacts

- <path>: old/new hash

### Delta verdict

<pass/fail>; <minor findings>

### Текущее

<table as above>

При delta pass → **<n+1>**.
```

### 7.5 Promotion complete

```text
## <n> — <Entry> промоутирован

### Compact receipt

| Поле | Значение |
|---|---|
| pattern_id | `<id>` |
| reviewed HEAD | `<sha>` |
| owner SHA-256 | `<hash>` |
| card SHA-256 | `<hash>` |
| reviewer | <vendor/model> |
| verdict | pass |
| findings | <n> minor |
| report | `<path>` |
| report SHA-256 | `<hash>` |

### Coverage

| Показатель | Значение |
|---|---:|
| sufficient | **<n> / 145** |
| owner-accepted | **<a> / <n>** |
| remaining | **<r>** |

### Timing

- entries: **<t>**;
- mean: **<m> min**;
- range: **<lo>-<hi> min**;
- forecast: **<o> / <b> / <p>**.

### Charts

![Promotion timing](<absolute-path-to-timing.png>)
![Latest promotions](<absolute-path-to-latest.png>)
![Forecast](<absolute-path-to-forecast.png>)

### Verification

- preflight PASS;
- promotions validator PASS <n>;
- full suite <result>;
- line length and boundary PASS.

### Limits

- reviewer packet-only;
- owner acceptance remains batched.

### Git

- main HEAD `<sha>`;
- promotion PR <number>;
- bookkeeping PR <number>.
```

Charts are embedded as images, never as bare links. Do not add charts to
intermediate reports.

## 8. Prohibited claims

Never claim review, promotion, acceptance, CI or human approval without a saved
report or record. A lane report is preparation, not review. A pass is not owner
acceptance. A merged PR is not CI.

