# CLAUDE.md

## What This Is

Org-level infrastructure repo for [organvm-vi-koinonia](https://github.com/organvm-vi-koinonia). Contains the org profile README (what visitors see on the org page) and community health files. This is **not application code** — changes here affect the org-wide GitHub presence.

## Key Files

- `profile/README.md` — Renders on `github.com/organvm-vi-koinonia`. This is the public face of ORGAN-VI.
- `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md` — Org-wide community health defaults (inherited by repos that lack their own)
- `organ-aesthetic.yaml` — Visual identity config for the organ
- `seed.yaml` — Orchestration metadata for the organvm system

## ORGAN-VI Context

ORGAN-VI (Koinonia / Community) has 5 sibling repos:

```
koinonia-db (shared DB layer — all others depend on this)
  ├── salon-archive (transcription, taxonomy, session archival)
  ├── reading-group-curriculum (multi-week reading programs)
  ├── adaptive-personal-syllabus (personalized learning paths — PROTOTYPE)
  └── community-hub (FastAPI web portal — FLAGSHIP, consumes all above)
```

Stack: Python 3.11+, SQLAlchemy 2.0+, PostgreSQL, FastAPI, Alembic.

## Editing Guidelines

- Profile README should stay in sync with actual repo count and implementation status
- Preserve the philosophical voice in Purpose and Philosophy sections — it's intentional
- System-wide stats (repo count, word count, essay count) come from `registry-v2.json` in the planning corpus

## Activation Audit

Issue [organvm-vi-koinonia/.github#12](https://github.com/organvm-vi-koinonia/.github/issues/12) classifies this repository as **actually-live** with a **ship-now** decision. The public org profile at `https://github.com/organvm-vi-koinonia` is the shipped surface, and the current audit record lives in `docs/activation-audit-2026-06-18.md`.

<!-- ORGANVM:AUTO:START -->
## System Context (auto-generated — do not edit)

**Organ:** ORGAN-I (Theory) | **Tier:** infrastructure | **Status:** LOCAL
**Org:** `unknown` | **Repo:** `.github`

### Edges
- **Produces** → `unknown`: unknown (event: `distribution-completed`)
- **Produces** → `unknown`: unknown (event: `press-release`)
- **Produces** → `unknown`: unknown (event: `grant-update`)
- **Produces** → `unknown`: unknown (event: `newsletter-published`)

### Siblings in Theory
`recursive-engine--generative-entity`, `organon-noumenon--ontogenetic-morphe`, `auto-revision-epistemic-engine`, `narratological-algorithmic-lenses`, `call-function--ontological`, `sema-metra--alchemica-mundi`, `system-governance-framework`, `cognitive-archaelogy-tribunal`, `a-recursive-root`, `radix-recursiva-solve-coagula-redi`, `nexus--babel-alexandria-`, `reverse-engine-recursive-run`, `4-ivi374-F0Rivi4`, `cog-init-1-0-`, `collective-persona-operations` ... and 4 more

### Governance
- Foundational theory layer. No upstream dependencies.

*Last synced: 2026-02-24T12:41:28Z*
<!-- ORGANVM:AUTO:END -->
