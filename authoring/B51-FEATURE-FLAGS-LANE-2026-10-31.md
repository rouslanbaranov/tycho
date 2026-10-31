# B51 — Feature Flags / Feature Toggles four-dimension lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 1/4 at the parent HEAD: mechanism was supported; invariant,
failure/recovery and alternative were partial. This lane binds all four
dimensions to public OpenFeature, LaunchDarkly, Microsoft Azure App
Configuration and AWS AppConfig units plus retained Fowler and AWS branch
records, and labels the authorization, staleness, audit, fail-safe,
kill-switch and choice rules as Tycho. The card remains inline in V11/C10.
The lane commit edits only the two book files and this note.

## Lane coordinates

- Parent HEAD: 683a76853e008c2419d396075ab3cefef0b7db43 (683a7685).
- Branch: b51-feature-flags; worktree:
  /Users/rbaranov/Projects/tycho-worktrees/b51-feature-flags.
- Scope: the owner section "### Feature Flags-Feature Toggles" in the V08/C04
  page and the inline V11/C10 card "### Feature Flags-Feature Toggles".
- Owner path (concatenate):

      book/volumes/v08-delivery-deployment-and-recovery/
      c04-gitops-rollout-and-progressive-delivery/configuration-rollout.md

- Card path:
  book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md.
- Exactly three files change: the owner page, the inline card and this note.
  No shared JSON file is edited.
- The task brief named V11/C07 or C10 for the inline card. The registered
  tycho.pattern.feature-flags-feature-toggles card is in V11/C10 (deployment
  and legacy modernization); V11/C07 is resilience and does not own this
  entry. This lane edits the registered C10 card and does not touch C07.
- Existing source ids: src.appconfig-rollout, src.appconfig-validation,
  src.fowler-feature-toggles and src.aws-branch.
- New source ids proposed: src.openfeature-spec, src.launchdarkly-flags and
  src.azure-app-configuration. They are not added to the shared register.
- New ledger records proposed: 12, listed below.
- Retained records reused unchanged:
  read.batch5-fowler-feature-toggles.2026-10-21 and
  read.aws-branch.2026-10-29.
- Baseline line-length and boundary checks pass before and after the edit.

## Baseline and gap

edition/patterns/owner-units.v1.json records mechanism as supported and the
other three dimensions as partial. The recorded reasons are:

- mechanism: "Defines the flag mechanism." (Fowler Categories of toggles).
- invariant: "Fowler text has no authorization-check rule; Permissioning
  Toggles only expose groups."
- failure/recovery: "Text names carrying cost and a public deployment
  incident but no evaluation-failure default."
- alternative: "Text treats canary as a flag application; no
  branch-by-abstraction recommendation."

The base owner page is the reviewed representation: SHA-256
91bd632c3de357254db72da9a509c0ef432f286ba80111990dbc1f59360362e3. It matches
the page_sha256 in the sufficient-candidates review record. The base card
SHA-256 is ca9f17e7795c178b18fa6433b83c70080d30e1cabaf6571996abd5c89761e7a3.

The gap was evidential: the owner section already stated Tycho rules but no
exact public quote, section and representation hash were bound to the
authorization, staleness, audit, fail-safe, kill-switch and alternative
claims. Shared metadata still shows 1/4 until the integrator applies the
proposals below.

## Candidate evaluation

- OpenFeature specification (selected). The Flag Evaluation API page states
  vendor-independent evaluation, the default-value contract and the
  abnormal-execution rule; the Types page defines the STALE provider status
  and the non-authoritative STALE reason. Primary source for the fail-safe
  default and one half of the snapshot-age rule.
- LaunchDarkly documentation (selected). Kill switch flags, change history,
  technical debt and server-side evaluation rules state the permanent
  operational flag, the audit log, the offline fallback and the
  temporary/permanent lifecycle. Primary source for the kill switch and
  audit trail.
- Microsoft Azure App Configuration documentation (selected). The feature
  management overview states the deployment/activation decoupling, the
  instant kill switch and the percentage-based canary; the .NET reference
  states the disabled default when no filter matches; the Entra ID page
  places authorization of configuration requests in a separate control.
  Primary source for the authorization boundary and the canary alternative.
- AWS AppConfig documentation (selected). Deploying feature flags, deployment
  strategies and deploying a configuration state the deployed-data cache,
  the gradual strategy, the bake time and automatic rollback. Primary source
  for the rollback and canary mechanics.
- Martin Fowler, "Feature Toggles (aka Feature Flags)" (retained, not newly
  read). Supports the mechanism and lifecycle context; it does not support
  the authorization, staleness or evaluation-failure rules.
- AWS Prescriptive Guidance, "Branch by abstraction pattern" (retained, not
  newly read). Supports the branch-by-abstraction distinction, the
  toggle-combination rule and cleanup; it is not an AppConfig page.
- Rejected or bounded: LaunchDarkly marketing pages, OpenFeature blog posts,
  the Azure DevOps progressive-experimentation page and third-party
  feature-flag blogs were not used as support. AWS AppConfig has no official
  "kill switch" page in the selected unit; the kill-switch claim uses
  LaunchDarkly and Microsoft instead. No origin claim is made.

## Source units and revisions

All fetches were public HTTPS GETs on 2026-10-31. Canonical text was extracted
with scripts/source_content_hash.py; raw HTML SHA-256 is also recorded. HTTP
dates are UTC and byte counts are the downloaded response bodies.

### R1 — OpenFeature Flag Evaluation API

- Record: read.openfeature-flag-evaluation.2026-10-31 (proposed).
- Source: src.openfeature-spec (proposed).
- URL: https://openfeature.dev/specification/sections/flag-evaluation/
- Label/type: "Flag Evaluation API — OpenFeature specification";
  documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T15:09:00Z; 119,564 bytes;
  text/html; charset=UTF-8; ETag
  "938b8bbaea8d456d382099fc5e6de091-ssl"; no Last-Modified; raw HTML
  SHA-256 01ca619d6724133c28f67cd02fdb4ad70b2ede0298af35dee22910809f3ab2ed;
  canonical text 25,590 characters / 3,751 words, SHA-256
  d724a522d5164572df123630304c552d8657eef12773de050e2b9ed8c7de07d6.
- Sections read: "Overview", "1.4. Detailed Flag Evaluation",
  "1.7. Provider Lifecycle Management".
- Sections not read: "1.1. API Initialization and Configuration",
  "1.2. Client Usage", "1.3. Flag Evaluation", "1.6. Shutdown",
  "1.8. Isolated API Instances", linked pages and code samples.
- Claims supported: Q1, Q11, Q12, Q13.
- Limits: living "current" specification with no version selector; no SDK
  was executed and no flag was evaluated. The canonical digest pins the
  representation, not a release tag.

### R2 — OpenFeature Types and Data Structures

- Record: read.openfeature-types.2026-10-31 (proposed).
- Source: src.openfeature-spec (proposed).
- URL: https://openfeature.dev/specification/types/
- Label/type: "Types and Data Structures — OpenFeature specification";
  documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T15:11:30Z; 46,985 bytes;
  text/html; charset=UTF-8; ETag
  "8ee0e774e511bad384ffc3d406da079e-ssl"; no Last-Modified; raw HTML
  SHA-256 2a318b0dc7e05c25b4ec3acd494459dce7ae85bb04b99caa1505b310b7d0dc94;
  canonical text 7,517 characters / 1,159 words, SHA-256
  e2741a640b15b7eb7ee13640a383f342f0aaa8f9f96a2483cf3fe09581622ff6.
- Sections read: "Evaluation Details", "Provider Status".
- Sections not read: primitive type sections, "Error Code", "Evaluation
  Context", "Provider Events", linked pages and code samples.
- Claims supported: Q6, Q7.
- Limits: the STALE status and reason are table cells; they describe a
  provider state and a resolution reason, not an application policy.

### R3 — LaunchDarkly kill switch flags

- Record: read.launchdarkly-killswitch.2026-10-31 (proposed).
- Source: src.launchdarkly-flags (proposed).
- URL: https://launchdarkly.com/docs/home/flags/killswitch/ (308 to
  /docs/home/flags/killswitch).
- Label/type: "Kill switch flags — LaunchDarkly documentation";
  documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T15:09:00Z; 311,224 bytes;
  text/html; charset=utf-8; Last-Modified 2026-10-31T09:00:46Z; no ETag;
  x-served-version dpl_4RHMRqtvdHvKgaEfTTjFqjzja3B6; raw HTML SHA-256
  4217089d538b560117a8b581e6ab291edd0f8d564382a7579dad4057ec518496;
  canonical text 77,659 characters / 2,535 words, SHA-256
  3499a8319235aa640944935aa9404b2a25339b323efa27d5d08df09325533159.
- Sections read: "About kill switch flags".
- Sections not read: "Create kill switch flags", "Modify the kill switch
  flag template", linked pages and images.
- Claims supported: Q16, Q17, Q18.
- Limits: product-specific terminology. The page treats kill switch flags as
  permanent; Tycho does not generalize that lifetime to every toggle.

### R4 — LaunchDarkly change history

- Record: read.launchdarkly-change-history.2026-10-31 (proposed).
- Source: src.launchdarkly-flags (proposed).
- URL: https://launchdarkly.com/docs/home/releases/change-history
- Label/type: "Change history — LaunchDarkly documentation";
  documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T15:09:00Z; 327,016 bytes;
  text/html; charset=utf-8; Last-Modified 2026-10-31T02:21:36Z; no ETag;
  x-served-version dpl_4RHMRqtvdHvKgaEfTTjFqjzja3B6; raw HTML SHA-256
  0cb35f78b8cf76b5c44fed1dcf043c037ab55f7e5e397a46cae2163457f74020;
  canonical text 83,670 characters / 2,654 words, SHA-256
  1b35ea724252ceb84244f3dc6d0d8576f12d0771ce87423480bbdcd5d695fc44.
- Sections read: "View the change history", "View a change entry".
- Sections not read: "Filter the change history", "Actions recorded in the
  change history", linked API pages and images.
- Claims supported: Q8, Q9, Q10.
- Limits: retention differs by plan; no change event was produced and no
  audit export was inspected.

### R5 — LaunchDarkly technical debt

- Record: read.launchdarkly-technical-debt.2026-10-31 (proposed).
- Source: src.launchdarkly-flags (proposed).
- URL: https://launchdarkly.com/docs/guides/flags/technical-debt/ (308 to
  /docs/guides/flags/technical-debt).
- Label/type: "Reducing technical debt from feature flags — LaunchDarkly
  documentation"; documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T15:09:01Z; 267,231 bytes;
  text/html; charset=utf-8; Last-Modified 2026-10-31T00:39:11Z; no ETag;
  x-served-version dpl_4RHMRqtvdHvKgaEfTTjFqjzja3B6; raw HTML SHA-256
  08ed1f577e37799db68910469dd74734f65fc52d2fbff75151e1bfc062a5f5c1;
  canonical text 95,892 characters / 8,037 words, SHA-256
  c31b76fe87176abfe55141f28905c9892cfdd986f457326e22dc99a7e8dc7b99.
- Sections read: "Temporary and permanent flags", "Include flags in your
  workflow’s definition of “done”".
- Sections not read: naming, tagging, views, archive checks, deprecation,
  review scheduling and code-reference sections; linked pages and images.
- Claims supported: Q25, Q26.
- Limits: product guidance; no flag inventory or lifecycle audit was run.

### R6 — LaunchDarkly flag evaluation rules

- Record: read.launchdarkly-flag-evaluation-rules.2026-10-31 (proposed).
- Source: src.launchdarkly-flags (proposed).
- URL: https://launchdarkly.com/docs/sdk/concepts/flag-evaluation-rules
- Label/type: "Flag evaluation rules in server-side SDKs — LaunchDarkly
  documentation"; documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T15:09:00Z; 216,761 bytes;
  text/html; charset=utf-8; Last-Modified 2026-10-31T03:35:07Z; no ETag;
  x-served-version dpl_4RHMRqtvdHvKgaEfTTjFqjzja3B6; raw HTML SHA-256
  8e384341fee22df9ec80fe78d08fad4bcc32c47922664e75ac06a447063c8608;
  canonical text 85,425 characters / 5,673 words, SHA-256
  2509b3e8b236ee079ed330a0b9aa6c8c8d22e2f3c754bfc1c73b03e1e12e327b.
- Sections read: "Preliminary checks".
- Sections not read: prerequisite, individual-targeting and rule-check
  algorithms, clauses, segments, percentage rollouts and fallthrough;
  linked pages.
- Claims supported: Q15.
- Limits: one SDK algorithm description; no SDK was run and no evaluation
  context was exercised.

### R7 — Microsoft Azure App Configuration feature management overview

- Record: read.azure-feature-management-overview.2026-10-31 (proposed).
- Source: src.azure-app-configuration (proposed).
- URL: https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-feature-management
- Label/type: "Feature management overview — Azure App Configuration";
  documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T15:09:01Z; 59,230 bytes;
  text/html; Last-Modified 2026-08-23T22:13:23Z; ETag
  "hgGfEw7u90+kqiK/uSLIdLKDDfc="; raw HTML SHA-256
  ff46be3ab752370a221577d54b18a24402a45b355c883bbec7b23dab2003596e;
  canonical text 8,213 characters / 1,279 words, SHA-256
  7c503850c57f7d1258b98f94991cf6a21addedaca19431d2bc090d19656e7eb2.
- Sections read: "Feature management overview", "Switch (On/Off)",
  "Rollout".
- Sections not read: "Experiment", "Monitor and analyze impact",
  "Next steps", linked quickstarts and code samples.
- Claims supported: Q2, Q22, Q23.
- Limits: product overview; no App Configuration store or feature flag was
  created.

### R8 — Microsoft .NET feature management reference

- Record: read.azure-feature-management-dotnet.2026-10-31 (proposed).
- Source: src.azure-app-configuration (proposed).
- URL (concatenate):
  https://learn.microsoft.com/en-us/azure/azure-app-configuration/
  feature-management-dotnet-reference
- Label/type: ".NET feature management — Azure App Configuration";
  documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T15:09:01Z; 129,094 bytes;
  text/html; Last-Modified 2026-08-23T22:13:21Z; ETag
  "5LDawI8XGzL62z8tYdqC1hhrl/k="; raw HTML SHA-256
  b5b8621cb903ad141dd71a1528d4f6a2bd9a5cbcab4ad5bf51868af30eac19e4;
  canonical text 58,094 characters / 8,387 words, SHA-256
  882b33ac3b545a0cbed56a90b88a0158ea0d4fd4236f65a99b247832bd9aa4d2.
- Sections read: "Feature filters", "Caching".
- Sections not read: declaration schema, dependency injection, ASP.NET Core
  integration, built-in filters, targeting, variants, telemetry and custom
  providers; code samples.
- Claims supported: Q14. The "Caching" section was read for the
  request-scoped snapshot distinction but is not used as a dimension
  binding.
- Limits: library reference; no application was run.

### R9 — Microsoft Azure App Configuration authorization

- Record: read.azure-appconfig-rbac.2026-10-31 (proposed).
- Source: src.azure-app-configuration (proposed).
- URL: https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-enable-rbac
- Label/type: "Access Azure App Configuration using Microsoft Entra ID —
  Azure App Configuration"; documentation-page.
- Representation: HTTP/2 200 on 2026-10-31T15:10:47Z; 74,331 bytes;
  text/html; Last-Modified 2026-08-23T22:13:17Z; ETag
  "8TdHyZ7LECm+aERvuRjTl/htwFc="; raw HTML SHA-256
  5ba34c3aac8b6e7789015e0b0ee2ddb77373c99d334100917d7974ee3cedbea3;
  canonical text 19,469 characters / 2,472 words, SHA-256
  2859050bc696e227793fba413cd43b288ec3a4955644ef9596a338ee40a076f2.
- Sections read: "Overview".
- Sections not read: built-in roles, token credentials, audience
  configuration, next steps and linked pages.
- Claims supported: Q4, Q5.
- Limits: the page authorizes requests to an App Configuration store; it
  does not state that flags are authorization. The extension to every
  protected action is Tycho synthesis.

### R10 — AWS AppConfig deploying feature flags

- Record: read.aws-appconfig-feature-flags.2026-10-31 (proposed).
- Source: src.appconfig-rollout (existing).
- URL: https://docs.aws.amazon.com/appconfig/latest/userguide/deploying-feature-flags.html
- Label/type: "Deploying feature flags and configuration data in AWS
  AppConfig"; documentation-page.
- Representation: HTTP/1.1 200 on 2026-10-31T15:09:01Z; 15,734 bytes;
  text/html; Last-Modified 2026-10-31T03:34:00Z; ETag
  "40QizKKu3eMQY018lkLIX28a+fA="; raw HTML SHA-256
  d6e54525b2fa4b4139bfaf793aa8554d5392eb10a7dbfa54d59083e4f0a2a579;
  canonical text 3,267 characters / 499 words, SHA-256
  07b1d0eefcbeb5e0d7eb4c38bb0f653c5e7cf8fb02b0ffe43219ab2c168101cf.
- Sections read: "Deploying feature flags and configuration data in AWS
  AppConfig".
- Sections not read: linked deployment-strategy, rollback and agent pages.
- Claims supported: Q3, Q20.
- Limits: AWS-specific deployment; no deployment was run.

### R11 — AWS AppConfig deployment strategies

- Record: read.aws-appconfig-deployment-strategies.2026-10-31 (proposed).
- Source: src.appconfig-rollout (existing).
- URL (concatenate):
  https://docs.aws.amazon.com/appconfig/latest/userguide/
  appconfig-creating-deployment-strategy.html
- Label/type: "Working with deployment strategies — AWS AppConfig";
  documentation-page.
- Representation: HTTP/1.1 200 on 2026-10-31T15:09:02Z; 20,998 bytes;
  text/html; Last-Modified 2026-10-31T03:33:58Z; ETag
  "OBNQ7Y0vs3mLhrV3uLZImwvtsZw="; raw HTML SHA-256
  c5a7eb774b5be80e7e90b8192265e5a8f0133cab7e3b0f22e30d9b3bfa50d2d9;
  canonical text 4,137 characters / 648 words, SHA-256
  aa782c44b9f35ccdfc65375300bc8c890e03da158164a5e7b108bdbd6f56e0c6.
- Sections read: "Working with deployment strategies".
- Sections not read: predefined strategies, custom-strategy creation, linked
  agent and rollback pages.
- Claims supported: Q21, Q24.
- Limits: strategy mechanics; no deployment or alarm was run.

### R12 — AWS AppConfig deploying a configuration

- Record: read.aws-appconfig-deploying.2026-10-31 (proposed).
- Source: src.appconfig-rollout (existing).
- URL: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-deploying.html
- Label/type: "Deploying a configuration — AWS AppConfig";
  documentation-page.
- Representation: HTTP/1.1 200 on 2026-10-31T15:09:02Z; 25,208 bytes;
  text/html; Last-Modified 2026-10-31T03:33:58Z; ETag
  "2av1x6gJFA0HzDwrITIEcHhI+dM="; raw HTML SHA-256
  3eba9fa47731e61d435e3d1f02117e58fe3b2b9a5b4d126b1092f4f278586518;
  canonical text 9,471 characters / 1,277 words, SHA-256
  ccfead7e9b3e6f469232f0d47ad71a281fec033296d6e61b9fa65cd6207e067b.
- Sections read: "Deploying a configuration".
- Sections not read: console and command-line procedure subsections, linked
  rollback and monitoring pages.
- Claims supported: Q19.
- Limits: deployment mechanics; no deployment was run.

## Selected exact quotes

Quotes reproduce the served prose; line breaks inside a quote are editorial
wrapping. Each was checked as a whitespace-normalized substring of the named
representation on 2026-10-31. The binding revision is the canonical-text
SHA-256 in the record above. Curly quotes are preserved where the source uses
them. Tycho-labelled sentences in the book are not source quotes.

### Mechanism

- Q1, OpenFeature Flag Evaluation API, "Overview":

      The evaluation API allows for the evaluation of feature flag values,
      independent of any flag control plane or vendor.

- Q2, Microsoft feature management overview, "Feature management overview":

      Feature management is a software-development practice that decouples
      feature release from code deployment and enables quick changes to
      feature availability on demand.

- Q3, AWS AppConfig deploying feature flags, "Deploying feature flags and
  configuration data in AWS AppConfig":

      Caches a copy of the data so it is ready to be retrieved by your
      application. This cached copy is called the deployed data.

### Invariant

- Q4, Microsoft App Configuration authorization, "Overview":

      Azure App Configuration supports authorization of requests to App
      Configuration stores using Microsoft Entra ID.

- Q5, Microsoft App Configuration authorization, "Overview":

      With Microsoft Entra ID, you can leverage Azure role-based access
      control (Azure RBAC) to grant permissions to security principals, which
      can be user principals, managed identities, or service principals.

- Q6, OpenFeature Types, "Provider Status":

      The provider's cached state is no longer valid and may not be up-to-date
      with the source of truth.

- Q7, OpenFeature Types, "Evaluation Details":

      The resolved value is non-authoritative or possibly out of date

- Q8, LaunchDarkly change history, "View the change history":

      LaunchDarkly keeps a running log of changes made to feature flags and
      other resources in each environment.

- Q9, LaunchDarkly change history, "View a change entry":

      the member that made the change

- Q10, LaunchDarkly change history, "View a change entry":

      a diff of the changes

### Failure and recovery

- Q11, OpenFeature Flag Evaluation API, "1.4. Detailed Flag Evaluation":

      Methods, functions, or operations on the client MUST NOT throw
      exceptions, or otherwise abnormally terminate. Flag evaluation calls
      must always return the default value in the event of abnormal
      execution.

- Q12, OpenFeature Flag Evaluation API, "1.4. Detailed Flag Evaluation":

      If the value returned by the underlying provider implementation does
      not match the expected type, it's to be considered abnormal execution,
      and the supplied default value should be returned.

- Q13, OpenFeature Flag Evaluation API, "Overview":

      In the absence of a provider the evaluation API uses the "No-op
      provider", which simply returns the supplied default flag value.

- Q14, Microsoft .NET feature management, "Feature filters":

      If no feature filter indicates that the feature should be enabled, it's
      considered disabled.

- Q15, LaunchDarkly flag evaluation rules, "Preliminary checks":

      If the SDK is offline, return the provided fallback value with the
      ERROR evaluation reason and the corresponding error code.

- Q16, LaunchDarkly kill switch flags, "About kill switch flags":

      Kill switch flags, sometimes called circuit breaker flags, are
      permanent boolean flags with two variations: “Enabled” (true) and
      “Disabled” (false).

- Q17, LaunchDarkly kill switch flags, "About kill switch flags":

      These flags are permanent safety mechanisms that you can use to turn
      off non-core functionality or third-party tools in an emergency.

- Q18, LaunchDarkly kill switch flags, "About kill switch flags":

      You can use these flags to quickly turn off functionality when needed.

- Q19, AWS AppConfig deploying a configuration, "Deploying a
  configuration":

      If a distribution fails, then AWS AppConfig rolls back the
      configuration.

- Q20, AWS AppConfig deploying feature flags, "Deploying feature flags and
  configuration data in AWS AppConfig":

      After you configure CloudWatch, if one or more alarms go into the alarm
      state during a deployment, AWS AppConfig automatically rolls back your
      configuration data to the previous version.

- Q21, AWS AppConfig deployment strategies, "Working with deployment
  strategies":

      Bake time This setting specifies the amount of time AWS AppConfig
      monitors for Amazon CloudWatch alarms after the configuration has been
      deployed to 100% of its targets, before considering the deployment to
      be complete. If an alarm is triggered during this time, AWS AppConfig
      rolls back the deployment.

### Alternative

- Q22, Microsoft feature management overview, "Rollout":

      Percentage-based gradual release

- Q23, Microsoft feature management overview, "Rollout":

      Percentage-based gradual release – expose a feature to a small
      percentage of traffic and increase it over time (canary or staged
      rollout) to reduce risk

- Q24, AWS AppConfig deployment strategies, "Working with deployment
  strategies":

      A deployment strategy enables you to slowly release changes to all
      targets or specific segments over minutes or hours

- Q25, LaunchDarkly technical debt, "Temporary and permanent flags":

      Flags are either temporary or permanent. A temporary flag has a limited
      lifespan. Once the flag has fulfilled its business purpose, remove it
      from the codebase.

- Q26, LaunchDarkly technical debt, "Include flags in your workflow’s
  definition of “done”":

      If the flag you use for a release will convert to a permanent flag, the
      definition of done should be when the setting on the flag changes to
      indicate it is permanent.

- Q27, AWS branch by abstraction, "Branch by abstraction pattern":

      The branch by abstraction pattern is often confused with feature
      toggles

- Q28, AWS branch by abstraction, "Branch by abstraction pattern":

      Branch by abstraction is a development technique and can be combined
      with feature toggles to switch between the old and new implementation

- Q29, AWS branch by abstraction, "Branch by abstraction pattern":

      remove any switching feature flag that you might have implemented

## Dimension mapping

- Mechanism. Primary: retained Fowler record
  read.batch5-fowler-feature-toggles.2026-10-21, section "Categories of
  toggles", revision
  d4e1a56d2d8c96cdcb278ec7fa16caf9805397e6a91fb862bf8642292a270e8d.
  Supporting: Q1 (OpenFeature evaluation API), Q2 (Microsoft feature
  management) and Q3 (AWS AppConfig deployed-data cache). Tycho reading: the
  flag service owns the runtime decision, not the release artifact.
- Invariant. Primary: Q4, record
  read.azure-appconfig-rbac.2026-10-31, section "Overview", revision
  2859050bc696e227793fba413cd43b288ec3a4955644ef9596a338ee40a076f2.
  Supporting: Q5 (Entra ID/RBAC permissions), Q6 and Q7 (OpenFeature STALE
  status and reason), Q8-Q10 (LaunchDarkly change history). Tycho rule:
  a flag may gate a feature but never grants a permission; record version,
  scope, default, reason and snapshot age; audit every override.
- Failure and recovery. Primary: Q11, record
  read.openfeature-flag-evaluation.2026-10-31, section "1.4. Detailed Flag
  Evaluation", revision
  d724a522d5164572df123630304c552d8657eef12773de050e2b9ed8c7de07d6.
  Supporting: Q12 and Q13 (OpenFeature type-mismatch and no-provider
  defaults), Q14 (Microsoft disabled default), Q15 (LaunchDarkly offline
  fallback), Q16-Q18 (LaunchDarkly kill switch), Q19-Q21 (AWS AppConfig
  rollback and bake time). Tycho runbook: safe branch first; distinguish
  error from deliberate off; bound snapshot age; use an owned kill switch;
  recover with a higher compatible version and re-observe it.
- Alternative. Primary: Q23, record
  read.azure-feature-management-overview.2026-10-31, section "Rollout",
  revision
  7c503850c57f7d1258b98f94991cf6a21addedaca19431d2bc090d19656e7eb2.
  Supporting: Q22 (Microsoft canary label), Q24 (AWS gradual strategy),
  Q25-Q26 (LaunchDarkly temporary/permanent lifecycle), Q27-Q29 (AWS branch
  by abstraction and cleanup). Tycho choice rule: canary for exposure risk;
  branch by abstraction for an internal implementation seam; permanent
  toggles become owned configuration; remove the toggle after rollout.

## Book edits

- Owner page (concatenate):

      book/volumes/v08-delivery-deployment-and-recovery/
      c04-gitops-rollout-and-progressive-delivery/configuration-rollout.md

  - Frontmatter adds existing ids src.fowler-feature-toggles and
    src.aws-branch; advances reviewed_at, updated_at and source_inspection_date
    to 2026-10-31; reviewer becomes "Automated authoring agent".
  - The owner section gains four labelled paragraphs (mechanism, invariant,
    failure/recovery, alternative), a source-boundary paragraph and six source
    bullets. The Tycho rules are labelled in the paragraph headings.
  - Page 272 lines; 2,493 words; owner heading line 155.
  - SHA-256:
    88c48d1dbf0169ac37bb008afa50f5a5356f70d57daea9b29ea53166a48daae7.
- Inline card: book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md.
  - Frontmatter adds src.appconfig-rollout and src.aws-branch; advances
    reviewed_at to 2026-10-31.
  - "Good-fit conditions", "Hard contraindications", "Competing alternative",
    "Failure and recovery" and "Sources" are expanded with the same bindings
    and revisions; the owner link and anchor are unchanged.
  - Card heading line 158; chapter 342 lines; 1,654 words.
  - SHA-256:
    bd95711019800a3d15f055cf05bb4d85864ea1b96f90fb942ef6b67e0624505a.
- No other book file, edition JSON, promotion or generated file is changed.

## Metadata needs (integrator)

The following changes are not in the lane commit. They are required before the
owner unit can move to 4/4 supported and before atlas hash checks pass.

### Source register sources/register.json

Set updated to 2026-10-31; source count moves 307 to 310.

- Add src.openfeature-spec: title "OpenFeature specification"; publisher
  "OpenFeature (CNCF)"; kind official-docs; URL
  https://openfeature.dev/specification/sections/flag-evaluation/; topics
  software-delivery and deployment-architecture; priority core; admission
  admitted-for-research; access public-web-or-author-download; reading status
  full-public-page-inspected; version note with the 2026-10-31 canonical
  hashes d724a522... and e2741a64..., raw hashes 01ca619d... and 2a318b0d...,
  ETags and byte counts from R1-R2; access and content-verified dates
  2026-10-31; license note "Public specification; cite short excerpts and
  paraphrase; do not mirror."; verification scope names the evaluation API,
  default-value contract, abnormal-execution rule, STALE status and STALE
  reason; observed title "Flag Evaluation API | OpenFeature".
- Add src.launchdarkly-flags: title "LaunchDarkly feature flag documentation";
  publisher "LaunchDarkly"; kind official-docs; URL
  https://launchdarkly.com/docs/home/flags/killswitch; topics
  software-delivery and deployment-architecture; priority core; admission
  admitted-for-research; reading status full-public-page-inspected; version
  note with x-served-version
  dpl_4RHMRqtvdHvKgaEfTTjFqjzja3B6 and the four canonical hashes 3499a831...,
  1b35ea72..., c31b76fe... and 2509b3e8...; access and content-verified dates
  2026-10-31; verification scope names kill switch, change history, temporary
  and permanent flags, and server-side evaluation rules; observed title
  "Kill switch flags - LaunchDarkly".
- Add src.azure-app-configuration: title "Azure App Configuration feature
  management documentation"; publisher "Microsoft"; kind official-docs; URL
  https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-feature-management;
  topics software-delivery and deployment-architecture; priority core;
  admission admitted-for-research; reading status full-public-page-inspected;
  version note with the three canonical hashes 7c503850..., 882b33ac... and
  2859050b..., raw hashes ff46be3a..., b5b8621c... and 5ba34c3a..., ETags and
  Last-Modified dates from R7-R9; access and content-verified dates
  2026-10-31; verification scope names feature management, the disabled
  default, canary rollout and Entra ID/RBAC authorization; observed title
  "Understand feature management using Azure App Configuration".
- Update src.appconfig-rollout: reading status full-public-page-inspected;
  access_checked and content_verified 2026-10-31; append the deployment
  strategies canonical hash aa782c44..., the deploying-feature-flags canonical
  hash 07b1d0ee... and the deploying canonical hash ccfead7e... to version;
  extend verification scope to deployment strategies, bake time, automatic
  rollback, deployed-data cache and feature-flag deployment; no deployment
  was run.
- src.fowler-feature-toggles and src.aws-branch: no change. Their retained
  records are reused byte-for-byte.

### Reading ledger edition/patterns/reading-ledger.v1.json

Add 12 records; records move 235 to 247. Each record is status read, reviewer
"Automated authoring agent", access_date 2026-10-31, unit_type
documentation-page, and uses the URL, label, content_sha256, sections and
limitations in R1-R12. R1-R2 use source_id src.openfeature-spec; R3-R6 use
src.launchdarkly-flags; R7-R9 use src.azure-app-configuration; R10-R12 use
src.appconfig-rollout. The retained read.batch5-fowler-feature-toggles.2026-10-21
and read.aws-branch.2026-10-29 records stay unchanged.

### Source plan edition/patterns/source-plan.v1.json

Append 12 units to tycho.pattern.feature-flags-feature-toggles after the
existing Fowler unit, in R1-R12 order. Every unit is status read and
blocked_reason null. Replace the entry notes with "Mechanism, invariant,
failure/recovery and alternative bound 2026-10-31 to OpenFeature, LaunchDarkly,
Microsoft Azure App Configuration and AWS AppConfig, with retained Fowler and
AWS branch context; no runtime test or sufficiency claim." Summary counters:
required_units 283 to 295, read_units 282 to 294, ledger_records 235 to 247;
planned_units 0 and blocked_units 1 stay unchanged.

### Owner units edition/patterns/owner-units.v1.json

For tycho.pattern.feature-flags-feature-toggles:

- mechanism: keep state supported and the existing quote "A runtime,
  versioned value scoped by tenant, user or cohort separates exposure from
  deployment, with a default and kill switch."; keep the Fowler binding
  unchanged; add supporting bindings Q1, Q2 and Q3.
- invariant: set state supported; keep quote "Flags never replace an
  authorization check."; primary binding Q4, source src.azure-app-configuration,
  record read.azure-appconfig-rbac.2026-10-31, section "Overview", revision
  2859050bc696e227793fba413cd43b288ec3a4955644ef9596a338ee40a076f2; add
  supporting bindings Q5-Q10. Reason: Microsoft places authorization of
  configuration requests in Entra ID/RBAC, OpenFeature exposes non-authoritative
  STALE values, and LaunchDarkly records each change with actor and diff; the
  rule that a flag never replaces an authorization decision is Tycho.
- failure_recovery: set state supported; keep quote "on evaluation failure the
  default must be the safe branch, not a silent enable."; primary binding Q11,
  source src.openfeature-spec, record
  read.openfeature-flag-evaluation.2026-10-31, section "1.4. Detailed Flag
  Evaluation", revision
  d724a522d5164572df123630304c552d8657eef12773de050e2b9ed8c7de07d6; add
  supporting bindings Q12-Q21. Reason: OpenFeature returns defaults on
  abnormal execution, Microsoft treats no matching filter as disabled,
  LaunchDarkly returns a fallback on offline evaluation and defines the kill
  switch, and AWS AppConfig rolls back on failure or alarm; the runbook
  ordering is Tycho.
- alternative: set state supported; keep quote "A canary or
  branch-by-abstraction is preferable when the toggle would become permanent
  configuration."; primary binding Q23, source src.azure-app-configuration,
  record read.azure-feature-management-overview.2026-10-31, section "Rollout",
  revision
  7c503850c57f7d1258b98f94991cf6a21addedaca19431d2bc090d19656e7eb2; add
  supporting bindings Q22 and Q24-Q29. Reason: Microsoft names canary or
  staged rollout, AWS AppConfig supplies a gradual strategy with bake time,
  LaunchDarkly separates temporary from permanent flags, and AWS Prescriptive
  Guidance contrasts branch by abstraction with toggles; the reversal rule is
  Tycho.
- technical_coverage: partial to partial-bounded; decision_coverage stays
  partial-bounded.
- source_support: primary Fowler record with auxiliary records R1-R12 and the
  retained AWS branch record; notes name the 2026-10-31 binding.
- Counters: invariant_supported 81 to 82; failure_recovery_supported 76 to 77;
  alternative_supported 81 to 82; mechanism_supported stays 117;
  technical_partial_bounded 15 to 16; technical_partial 66 to 65.

### Other shared metadata

- Registry: add 12 source_units; technical_owner state partial to
  partial-bounded; coverage technical partial to partial-bounded and overall
  partial to partial-bounded; decision stays partial-bounded; update notes.
- Card batches: add card_path
  book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md to the
  entry; keep ledger_record read.batch5-fowler-feature-toggles.2026-10-21 as
  the primary citation.
- Card frontmatter: this lane already adds src.appconfig-rollout and
  src.aws-branch. When the three proposed source ids are registered, add
  src.openfeature-spec, src.launchdarkly-flags and
  src.azure-app-configuration to evidence_scope.source_ids as well; preflight
  requires every binding source to be declared on the card.
- coverage-map, sufficient-candidates, sufficient-review-records,
  atlas-manifest (registry_sha256), content-revisions (owner page and README
  historical-view hashes), inventory, page-census, route and section indexes,
  qrels and delivery-evidence: usual recomputation. The existing
  sufficient-candidates review record pins the old page hash
  91bd632c3de357254db72da9a509c0ef432f286ba80111990dbc1f59360362e3; it is
  stale for the edited page and cannot be treated as a review pass.
- The owner page's claim_ids stay empty; no claim registry is introduced.

## Validation

- python3 scripts/check_markdown_line_length.py: PASS; 145 exact owner-link
  exceptions. The card's only long line is the existing "Technical owner"
  exception.
- python3 scripts/check_boundary.py: PASS; independent-origin review remains
  required.
- python3 scripts/validate_book_metadata.py: PASS; 505 documents.
- python3 scripts/validate_pattern_cards.py: PASS; 11 batches, 145 entries.
- python3 scripts/validate_pattern_registry.py: PASS; 145 entries, 11 families.
- python3 scripts/validate_edition.py: FAIL with
  "directory-baseline-payload-drift". The changed owner page needs a
  content-revisions entry before this baseline check can pass; no shared JSON
  is edited by this lane.
- python3 scripts/validate_directory_migration.py: FAIL with the same
  "directory-baseline-payload-drift" condition and the same integration need.
- python3 scripts/validate_pattern_atlas.py: FAIL with "atlas-document-sha".
  The edited V11/C10 README no longer matches the hash pinned in the atlas
  manifest and semantic audit. This is expected until the integrator refreshes
  those shared records; no atlas JSON is edited by this lane.
- python3 scripts/validate_book_navigation.py: FAIL with four unchanged
  missing local anchors in dark-launching-shadow-traffic.md and rbac-abac.md;
  neither file is touched by this lane. The same four issues were recorded in
  the B50 integration note.
- python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.feature-flags-feature-toggles: FAIL as expected without shared
  metadata; it reports invariant, failure_recovery and alternative still
  partial and card_path missing. This is the pre-integration state, not a book
  defect.
- Quotes: 29 exact quotes checked as whitespace-normalized substrings of the
  12 representations; all 29 passed. The owner section contains 28 quoted
  fragments, all matched; the card contains six, all matched.
- Owner page: every new line is at most 100 characters. Existing long
  frontmatter, table, navigation and source-link lines are unchanged.
- git diff --check: no whitespace errors.
- Raw SHA-256 after the book edits:
  owner page
  88c48d1dbf0169ac37bb008afa50f5a5356f70d57daea9b29ea53166a48daae7;
  card bd95711019800a3d15f055cf05bb4d85864ea1b96f90fb942ef6b67e0624505a.
- The lane note has no tab characters and every line is at most 100
  characters.

## Limits

- Shared metadata is not updated. The generated owner units, registry, source
  plan, ledger, card batches and indexes still show the entry as 1/4 or
  partial until an integrator applies the proposals above.
- No promotion, owner acceptance, coverage sufficiency or independent AI
  review is claimed. The book/atlas review gate remains outstanding, and the
  existing review hash is stale for the edited page.
- No benchmark, production observation, flag evaluation, deployment, canary,
  kill switch or rollback was executed.
- OpenFeature, LaunchDarkly, Microsoft Learn and AWS AppConfig pages are
  living product documentation with no release selector. Their raw and
  canonical digests pin the 2026-10-31 representations; they are not release
  tags.
- The OpenFeature page is versioned as "current" by its own metadata; the
  specification's GitHub source is not pinned to a commit in this lane.
- LaunchDarkly pages are served through a deployment version
  (dpl_4RHMRqtvdHvKgaEfTTjFqjzja3B6) with no ETag; the deployment id,
  Last-Modified dates and canonical digests are the revision evidence.
- Microsoft Learn and AWS pages use Last-Modified and ETag values; future
  re-fetches must compare the canonical digest before reusing a quote.
- The claim that flags never replace authorization is a Tycho rule. The
  Microsoft source authorizes App Configuration requests, not feature-flag
  decisions; the extension to every protected action is synthesis, not a
  source claim.
- The owner page is in V08, so the repository line-length checker covers only
  the V11 card; the owner page was checked directly for new-line length.
- The card remains inline in V11/C10, not the V11/C07 location named in the
  task brief.
