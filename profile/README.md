# ORGAN-VI: Koinonia — Community

_Community infrastructure and facilitation tools_

[![ORGAN-VI: Koinonia](https://img.shields.io/badge/ORGAN--VI-Koinonia-4a148c?style=flat-square)](https://github.com/organvm-vi-koinonia)

> The gathering space for the organvm system — salons, reading groups, and collaborative encounters where theory meets practice through shared inquiry.

**4 apps · 1 shared library · 266 app tests (382 total)**

[Purpose](#purpose) | [Philosophy](#philosophy) | [Current Status](#current-status) | [Planned Initiatives](#planned-initiatives) | [Connection to the Eight-Organ System](#connection-to-the-eight-organ-system)

---

## Purpose

ORGAN-VI houses the community infrastructure for the [organvm eight-organ system](https://github.com/meta-organvm). Where other organs produce theory (I), art (II), products (III), governance (IV), documentation (V), and outreach (VII), ORGAN-VI creates the conditions for *encounter* — structured spaces where contributors, collaborators, and curious observers engage with the system's ideas through dialogue rather than consumption.

The community organ operates on the principle that a creative-institutional system is incomplete without a participatory layer. Salons, reading groups, and collaborative workshops are not marketing activities (that's ORGAN-VII) or documentation (that's ORGAN-V) — they are generative spaces where the system's theoretical commitments are tested, challenged, and extended by people other than the original author.

## Philosophy

The name *Koinonia* (κοινωνία) is drawn from classical Greek, where it denotes fellowship, communion, and shared participation in a common life. In Aristotle's political philosophy, koinonia describes the bonds that make a community more than a collection of individuals — it is the active practice of holding something in common. In early Christian usage, the term carried the weight of mutual obligation: participants in koinonia are not audience members but co-creators of the space they inhabit.

ORGAN-VI applies this concept to creative-institutional practice. Community here is not an afterthought bolted onto a production system. It is *infrastructure* — as essential as the governance layer (ORGAN-IV) or the theoretical foundations (ORGAN-I). The conviction is that ideas sharpened only by their author become brittle. Salons and reading groups introduce the friction of other perspectives, the generosity of collaborative interpretation, and the accountability that comes from explaining your work to someone who did not build it.

This is community as creative infrastructure: the deliberate construction of spaces where encounter is possible.

## Current Status

ORGAN-VI is **operational**. The shared database layer is built with models, migrations, and seed data running on Neon PostgreSQL. CI pipelines (with PostgreSQL service containers) run across all repos. The FastAPI flagship portal (`community-hub`) integrates the salon archive, curricula browser, contributor profiles, full-text search, adaptive syllabi, Atom feeds, and WebSocket live rooms into a single service. **266 tests** across 4 app repos (382 total including the shared library).

> **Note:** `community-hub` is deployed on Render's free tier. The service sleeps after inactivity and may take 30-60 seconds to respond on first request (cold start). The keep-alive workflow is currently paused, so cold starts may occur after inactivity.

**Repositories:**

**App repos:**

| Repo | Role | Status |
|------|------|--------|
| [`community-hub`](https://github.com/organvm-vi-koinonia/community-hub) | FastAPI portal — salon archive, curricula, search, feeds, live rooms, adaptive syllabus | PUBLIC_PROCESS (flagship) — [deployed](https://community-hub-8p8t.onrender.com) |
| [`salon-archive`](https://github.com/organvm-vi-koinonia/salon-archive) | Transcription pipeline, taxonomy, session archival | PUBLIC_PROCESS |
| [`reading-group-curriculum`](https://github.com/organvm-vi-koinonia/reading-group-curriculum) | Multi-week reading programs with discussion guides | PUBLIC_PROCESS |
| [`adaptive-personal-syllabus`](https://github.com/organvm-vi-koinonia/adaptive-personal-syllabus) | AI-personalized learning paths across organ domains | PUBLIC_PROCESS |

**Shared library:** [`koinonia-db`](https://github.com/organvm-vi-koinonia/koinonia-db) — SQLAlchemy models, Alembic migrations, seed data (PUBLIC_PROCESS)

## Planned Initiatives

### Salon Series

Recurring events organized around themes that cross organ boundaries. Each salon pairs a theoretical concern (ORGAN-I) with a practical demonstration (ORGAN-II or III), creating a structured space for discussion that is neither lecture nor open-ended conversation. The salon format draws from the European tradition of curated intellectual gathering: a prepared provocation, a demonstration or reading, and a structured exchange that produces documented outcomes rather than evaporating after the event.

### Reading Groups

Collaborative close reading of the system's foundational documents, academic references, and related work. Planned formats include:

- **Internal readings** — Close examination of the organvm system's own documents (genesis transcripts, specifications, architectural decisions)
- **External readings** — Engagement with the academic and creative traditions the system draws from (systems theory, institutional design, recursive epistemology)
- **Cross-organ readings** — Joint sessions where participants from different organ contexts read the same material through their respective disciplinary lenses

## Connection to the Eight-Organ System

The organvm system spans 101 repositories across 8 organizations.

| Organ | Relationship to ORGAN-VI |
|-------|--------------------------|
| I (Theory) | Provides intellectual content for salons and reading groups |
| II (Art) | Supplies demonstrations, performances, and experiential material |
| III (Commerce) | Potential venue for user feedback sessions and product community |
| IV (Orchestration) | Defines governance rules for community participation |
| V (Public Process) | Documents community outcomes and methodology |
| VII (Marketing) | Amplifies community events and outcomes |
| VIII (Meta) | ORGAN-VI reports to the meta-org umbrella |

**Dependency direction:** ORGAN-VI consumes from I, II, III (no back-edges). Community activities respond to what the system produces; they do not dictate upstream organ priorities.

> **Read the public process:** [organvm-v-logos.github.io/public-process](https://organvm-v-logos.github.io/public-process/)

---

**Organization:** [organvm-vi-koinonia](https://github.com/organvm-vi-koinonia)
**System:** [organvm eight-organ system](https://github.com/meta-organvm)
**Author:** [@4444J99](https://github.com/4444J99)

*ORGAN-VI Status Update 2026-02-24 — Promoted to PUBLIC_PROCESS (System-Wide Activation Sprint)*

*Activation Audit 2026-06-18 — actually-live; ship-now; org profile re-probed HTTP 200*
