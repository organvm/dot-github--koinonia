# organvm-vi-koinonia/.github

Org-level infrastructure for [ORGAN-VI: Koinonia](https://github.com/organvm-vi-koinonia).

This repository owns the GitHub organization profile, default community health files, and org-level automation workflows for the community organ of the organvm system.

## Activation Status

- **Frozen state:** actually-live
- **Ship decision:** ship-now
- **Audit issue:** [organvm-vi-koinonia/.github#12](https://github.com/organvm-vi-koinonia/.github/issues/12)
- **Last validated:** 2026-06-18

The shipped surface is the organization profile at <https://github.com/organvm-vi-koinonia>, backed by [`profile/README.md`](profile/README.md). The issue verifier re-probed the profile during the activation audit and reported HTTP 200.

## Repository Role

- [`profile/README.md`](profile/README.md) renders as the public organization profile.
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), [`CONTRIBUTING.md`](CONTRIBUTING.md), and [`SECURITY.md`](SECURITY.md) provide organization-wide community health defaults.
- [`seed.yaml`](seed.yaml) records the orchestration contract for this meta-repo.
- [`.github/workflows/`](.github/workflows/) contains the minimal CI, dispatch receivers, keepalive pings, service monitoring, and cross-organ handoff workflows.
- [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/) and [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) provide default issue and PR intake.
- [`README_STANDARDS.md`](README_STANDARDS.md) defines local README standards as an overlay on the system-wide canonical policy.

## Live Surfaces

- Organization profile: <https://github.com/organvm-vi-koinonia>
- Flagship community portal: <https://community-hub-8p8t.onrender.com>
- Public process reference: <https://organvm-v-logos.github.io/public-process/>

## Local Validation

```bash
make test
```
