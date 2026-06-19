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

## Live Surfaces

- Organization profile: <https://github.com/organvm-vi-koinonia>
- Flagship community portal: <https://community-hub-8p8t.onrender.com>
- Public process reference: <https://organvm-v-logos.github.io/public-process/>

## Local Validation

```bash
python3 - <<'PY'
from pathlib import Path
import yaml

for path in sorted(Path(".").glob("**/*.yml")) + sorted(Path(".").glob("**/*.yaml")):
    if ".git" not in path.parts:
        yaml.safe_load(path.read_text())
        print(f"valid YAML: {path}")
PY

git grep -nP 'sk-[a-zA-Z0-9]{20,}|ghp_[a-zA-Z0-9]{36}|AKIA[A-Z0-9]{16}' -- ':!.github' || true
```
