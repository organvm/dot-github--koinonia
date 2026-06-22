# Discovery: organvm/dot-github--koinonia

**Repo:** `organvm/dot-github--koinonia` (`organvm-vi-koinonia/.github`)
**Date:** 2026-06-22
**Decision:** PROMOTE — real, reusable, estate-wide latent value found.

## Value Thesis

On its surface this is the ORGAN-VI "Koinonia" org-infrastructure repo — it owns
the public organization profile (`profile/README.md`, shipped and HTTP-200), the
community-health defaults, and issue/PR templates. That is its _visible_ value.
Its _highest latent_ value is the asset hiding in `.github/workflows/`: a **tested,
gated cross-organ event-routing mesh** built entirely on typed GitHub Actions
`repository_dispatch` edges. It implements the V→VI essay-intake edge
(`essay-to-community.yml`: dispatch-driven with a daily-poll fallback and
duplicate-issue dedup), the VI→VII milestone-promotion edge
(`community-to-kerygma.yml`: dispatch gated on a 7-day RFC age _and_ a
`quality-threshold` label), and a centralized `dispatch-receiver.yml` board that
fans eight event types into tracking issues — plus cold-start-tolerant service
monitoring and keepalive. Crucially, it ships a **Python test harness**
(`tests/test_essay_to_community_workflow.py`) that extracts the workflows' inline
shell/python `run:` blocks and executes them against a mocked `gh` CLI — i.e. it
actually _unit-tests Actions logic_, a discipline almost no `.github` repo
practices. The gated-edge pattern is the connective pub/sub tissue the whole
145-repo estate depends on, and both the edge workflows and the testing harness
are directly portable to the seven sibling organ `.github` repos. This is not
archival infrastructure; it is a reusable orchestration-and-verification standard
that currently lives in exactly one org.

## Highest-Value Capability

A **reusable, test-verified "organ edge" workflow pattern** — typed dispatch with
gating (RFC age, quality labels), dedup, and dispatch+poll fallback — together
with a harness that unit-tests the Actions `run:` logic. Estate-wide reuse target:
every organ-level `.github` repo (8 organs) that needs reliable cross-org pub/sub.

## Best Concrete First Task

Extract the gated-edge workflows and the `run:`-block test harness into a
parameterized, reusable form — a `reusable-edge.yml` GitHub Actions reusable
workflow plus a documented testing recipe — so the other organ `.github` repos
can adopt one verified standard instead of re-deriving dispatch wiring per org.
Start by factoring `essay-to-community.yml` + its test into the reusable workflow
and proving it green here before publishing the template.
