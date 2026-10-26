# Workload failure-path remediation — 2026-10-26

> Evidence record. Not human review, owner acceptance, sufficient coverage, CI or
> merge permission.

- Reviewer preset: `reviewer`; child `ee7a784f-df7c-496f-ba65-6ca1027ecdc9`
- HEAD: `1f5bfbba` plus uncommitted remediation.
- Verdict: PASS.
- The unsupported "revoke" wording was removed from the failure path; "rotate, isolate and test
  an unauthorized peer" is supported by the rotation/identity/AuthorizationPolicy claims.
- Revocation remains synthetic in the source boundary.
- Workload's four technical dimensions are now supported; it becomes sufficient-ready.
- Rebind: Workload section is bound to the current identity page hash.
