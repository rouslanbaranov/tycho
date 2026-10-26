# Full-unit reading contract — B1

Date: 2026-10-26. Refs #535, #532, #225.

## Scope

Read the **155 source-plan units** for the 145 pattern entries in full at their exact unit
scope. The 211 other registered sources are outside this contract.

## Definitions

- **Unit**: the exact sections named in `edition/patterns/source-plan.v1.json`.
- **Full**: the whole unit was read without truncation; this is not a claim about the whole book.
- **Exact #225 reuse**: same source, same revision/content hash, same section scope and same
  status. A changed page, a different section, a partial or blocked record is not reusable.
- **Blocked**: lawful access or representation unavailable; never promoted.

## Workflow

1. Match each unit to an #225 reading by source, URL, unit and sections.
2. Verify revision/hash and complete section coverage.
3. Reuse only exact matches; otherwise read the unit.
4. Record full, partial or blocked with exact evidence.
5. Re-run structural validators and focused tests.

## Initial crosswalk

- 155 units from 64 sources.
- 19 reuse candidates requiring scope/revision check.
- 57 units with no #225 record.
- 59 units with a scope mismatch.
- 19 units with a partial #225 record.
- 1 blocked unit.

No sufficient or independent-AI-review claim.
