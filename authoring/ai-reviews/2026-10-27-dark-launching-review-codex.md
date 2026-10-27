# External AI review — Dark Launching / Shadow Traffic

- Reviewer harness: Codex CLI 0.163.0-alpha.11.2 (separate OpenAI harness)
- Vendor/model: OpenAI / gpt-5.6-sol
- Reviewed HEAD: 6b548d8ef72e971ea344287387b271a830f01ddf
- Scope: tycho.pattern.dark-launching-shadow-traffic
- Access: read-only; no repository writes

## Verbatim report

```json
{"verdict":"fail","technical":"fail","decision":"pass","entries_reviewed":1,"findings":[{"severity":"major","pattern_id":"tycho.pattern.dark-launching-shadow-traffic","dimension":"technical.failure_recovery","path":"edition/patterns/owner-units.v1.json:9241","evidence":"The owner and atlas card claim that inspecting mirrored-service access logs detects failures, but the bound quote only states that mirrored responses are discarded. The ledger separately says mirrored requests appear in access logs; it does not establish failure detection. The claimed dimension also provides no recovery or containment action. Therefore the exact quote does not support the full claim, and the four technical dimensions do not jointly establish the recorded support.","required_remediation":"Bind an exact passage from the pinned admitted revision that supports access-log failure detection and a recovery or containment action. Otherwise narrow the text to the supported observation that mirrored requests appear in logs, mark failure/recovery unsupported, and remove the source-plan readiness assertion that all four dimensions are bound."}],"limits":"Read-only review of committed artifacts at exact HEAD 6b548d8ef72e971ea344287387b271a830f01ddf. The supplied owner-unit SHA-256 e1c99301f5663779b995734139c8b6c320e95931f885c48ed962a3c429a63a9d and source-plan SHA-256 4b7bf999960494b7e8eba445e6aa10b85217c8285216ed541212a87a4ebc9917 matched. Hidden invocation, the discarded-response invariant, and the canary alternative have matching source-plan units, ledger records, sections, revisions, and quote-supported claims. The decision card remains conditional and discloses synthetic limits without circular reliance on the owner page. Current authoritative state is partial-bounded, candidate-for-independent-review, with no promotion record or owner acceptance. Untracked deliverables were excluded. Live sources were not retrieved, so source text was assessed only through committed bindings, ledger metadata, hashes, and source-reading records."}
```
