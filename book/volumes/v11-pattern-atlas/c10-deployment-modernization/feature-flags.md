---
metadata_version: 1
id: "tycho.page.69e0f95b57264cf38f279ceda2e9dadf"
kind: "page"
parent_id: "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
canonical_path: "book/volumes/v11-pattern-atlas/c10-deployment-modernization/feature-flags.md"
title: "Feature Flags-Feature Toggles"
topic_ids:
  - "deployment-architecture"
  - "software-delivery"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Feature Flags / Feature Toggles; all four dimensions
  source-bound; coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should activation be decoupled from deployment through a runtime
      toggle?
  prerequisites:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  related_ids:
    - "tycho.chapter.dabaea8f5ab426edc08683ceec89c2c0"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "feature flags"
    - "deployment and legacy modernization"
evidence_scope:
  source_ids:
    - "src.openfeature-spec"
    - "src.launchdarkly-flags"
    - "src.azure-app-configuration"
    - "src.appconfig-rollout"
    - "src.fowler-feature-toggles"
    - "src.aws-branch"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.openfeature-flag-evaluation.2026-10-31,
    read.openfeature-types.2026-10-31,
    read.launchdarkly-killswitch.2026-10-31,
    read.launchdarkly-change-history.2026-10-31,
    read.launchdarkly-technical-debt.2026-10-31,
    read.launchdarkly-flag-evaluation-rules.2026-10-31,
    read.azure-feature-management-overview.2026-10-31,
    read.azure-feature-management-dotnet.2026-10-31,
    read.azure-appconfig-rbac.2026-10-31,
    read.aws-appconfig-feature-flags.2026-10-31,
    read.aws-appconfig-deployment-strategies.2026-10-31,
    read.aws-appconfig-deploying.2026-10-31 and
    read.aws-branch.2026-10-29; owner section and limits are bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-31"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# Feature Flags-Feature Toggles

**Identity.** Feature Flags / Feature Toggles; family Deployment and legacy modernization;
kind deployment-pattern; priority core.

**Decision question.** Should activation be decoupled from deployment through a runtime
toggle?

**Good-fit conditions.** Toggle ownership, expiry, scope and kill switch are defined; the
default fails safe; evaluation is observable; snapshot age and audit trail are explicit; and
the flag is never the authorization decision for a protected action.

**Hard contraindications.** Reject when a toggle would become permanent configuration debt,
when no owner removes it, when it hides a broken deployment, or when it is asked to grant a
permission or approve an irreversible action.

**Competing alternative.** Canary release when the residual risk is exposure of a deployment
to a cohort; branch by abstraction when an internal implementation is being replaced behind a
stable interface; deploy dark code or a separate release train. Microsoft lists
"Percentage-based gradual release" that exposes "a feature to a small percentage of traffic
and increase it over time (canary or staged rollout) to reduce risk"; AWS Prescriptive Guidance
says branch by abstraction "can be combined with feature toggles to switch between the old and
new implementation." Reverse the choice when toggle lifecycle cost exceeds decoupling benefit
or the toggle becomes permanent configuration.

**Failure and recovery.** Safe default on evaluation failure, then a kill switch and a
versioned rollback. OpenFeature requires "Flag evaluation calls must always return the default
value in the event of abnormal execution"; LaunchDarkly describes kill switch flags as
"permanent safety mechanisms" that "turn off non-core functionality or third-party tools in an
emergency"; AWS AppConfig rolls back a failed distribution or an alarm-triggered deployment.
Bound snapshot age, audit overrides and remove the flag after the rollout.

**Technical owner.** [Feature Flags / Feature Toggles](../../v08-delivery-deployment-and-recovery/c04-gitops-rollout-and-progressive-delivery/configuration-rollout.md#feature-flags-feature-toggles) — flags are bounded, not a full toggle-lifecycle platform.

**Sources.** Public documentation, not benchmarks. The owner section binds the four
dimensions; this card cites the same records. OpenFeature *Flag Evaluation API* and *Types
and Data Structures*, canonical text SHA-256 `d724a522...` and `e2741a64...`, records
`read.openfeature-flag-evaluation.2026-10-31` and `read.openfeature-types.2026-10-31`
(proposed). LaunchDarkly *Kill switch flags*, *Change history*, *Reducing technical debt
from feature flags* and *Flag evaluation rules in server-side SDKs*, canonical text SHA-256
`3499a831...`, `1b35ea72...`, `c31b76fe...` and `2509b3e8...`, records
`read.launchdarkly-killswitch.2026-10-31`, `read.launchdarkly-change-history.2026-10-31`,
`read.launchdarkly-technical-debt.2026-10-31` and
`read.launchdarkly-flag-evaluation-rules.2026-10-31` (proposed). Microsoft Azure App
Configuration *Feature management overview*, *.NET feature management* and *Access Azure App
Configuration using Microsoft Entra ID*, canonical text SHA-256 `7c503850...`,
`882b33ac...` and `2859050b...`, records
`read.azure-feature-management-overview.2026-10-31`,
`read.azure-feature-management-dotnet.2026-10-31` and
`read.azure-appconfig-rbac.2026-10-31` (proposed). AWS AppConfig *Deploying feature flags and
configuration data*, *Working with deployment strategies* and *Deploying a configuration*,
canonical text SHA-256 `07b1d0ee...`, `aa782c44...` and `ccfead7e...`, records
`read.aws-appconfig-feature-flags.2026-10-31`,
`read.aws-appconfig-deployment-strategies.2026-10-31` and
`read.aws-appconfig-deploying.2026-10-31` (proposed under `src.appconfig-rollout`).
The retained `src.fowler-feature-toggles` record
`read.batch5-fowler-feature-toggles.2026-10-21` remains the mechanism context.
Tycho-labelled rules are synthesis.

**Decision state.** applicable-under-conditions.

**Related entries.** Canary Release; Dark Launching; GitOps; Configuration Rollout.
