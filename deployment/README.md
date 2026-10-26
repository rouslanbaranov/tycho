# Vercel release marker

Automatic Vercel production builds are gated on
`deployment/vercel-release`. A merge to `main` builds only when that file
changes; every other merge skips the Vercel build. This keeps normal book and
code merges out of the deployment allowance and stops one container image per
merge from filling the Hobby container-registry limit.

## Make a release

1. Confirm the container registry has room for one more image; clean up old
   images when it is near the Hobby limit.
2. Replace the contents of `deployment/vercel-release` with a new UTC
   timestamp or release identifier.
3. Include that change in the release pull request and merge it.
4. Check the Vercel status on the merge commit and verify `/ready`.

The first gated release added the marker on 2026-10-26. A merge that does not
add or change it produces no Vercel deployment.

## Container registry cleanup

The Hobby plan allows 50 images per repository. Each container build pushes a
new image tagged with the commit SHA. Inspect the `dockerfile` repository and
delete old images before the next release. Keep the image used by the live
deployment and at least one rollback candidate; do not delete the repository.

```sh
npx vercel login
npx vercel link
npx vercel vcr image ls dockerfile --limit 100
npx vercel vcr image rm dockerfile <image-id> --yes
```

The cleanup is an owner action because it requires Vercel authentication and
permanently deletes images. A release build is not evidence that the registry
issue is resolved; check the build status and `/ready`.

## Preview deployments

Preview deployments remain disabled by `git.deploymentEnabled` in
`vercel.json`. A manual preview is a separate owner action and is not part of
the normal issue-branch flow.
