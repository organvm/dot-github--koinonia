# Activation Audit: GH-organvm-vi-koinonia-github-12

- **Repository:** `organvm-vi-koinonia/.github`
- **Issue:** <https://github.com/organvm-vi-koinonia/.github/issues/12>
- **Audit date:** 2026-06-18
- **Frozen state:** actually-live
- **Ship decision:** ship-now

## Identity

This is the ORGAN-VI Koinonia organization meta-repo. It owns:

- the public GitHub organization profile in `profile/README.md`
- default community health files for the organization
- issue and pull request templates
- the `seed.yaml` orchestration contract
- org-level automation workflows

## Shipped Evidence

- The organization profile renders from `profile/README.md` at <https://github.com/organvm-vi-koinonia>.
- The activation verifier for issue #12 reported the organization profile as HTTP 200 during the audit run.
- The profile links the live `community-hub` flagship portal and public process reference.
- The repo includes community health defaults: `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, and `SECURITY.md`.
- The repo includes intake defaults under `.github/ISSUE_TEMPLATE/` and `.github/PULL_REQUEST_TEMPLATE.md`.
- The repo includes operational workflows for CI, dispatch receiving, V-to-VI essay intake, VI-to-VII community milestone dispatch, service monitoring, keepalive pings, and Dependabot maintenance.

## Local Verification

Run from the repository root:

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

## Notes

The local development environment could not reach `api.github.com`, so the live HTTP result above is recorded from the issue #12 verifier context rather than re-probed locally.
