# AGENTS.md - Project Instructions

## Workflow System

This project uses a structured **Web Workflow** — a specialized workflow for building web applications with REST endpoints, separated Backend and Frontend, and SQL persistence.

### Branching Architecture

**Phase 1 is generic** — it works for any software project (discovery, knowledge audit, research, use cases, tech selection, consolidation).

**At Phase 2, the workflow branches by project type.** Choose the branch that matches what you're building:

| Branch | Status | Path |
|--------|--------|------|
| **Web (SPA + REST + SQL)** | Active | `workflow/web/` |
| **Game development** | Active | `workflow/game/` |
| CLI development | Planned | — |
| Mobile development | Planned | — |
| Desktop development | Planned | — |

Both Web and Game branches are documented below.

### Web Branch Phases

The Web workflow has **five phases**:

1. **Phase 1: Discovery + Tech Selection** (6 stages) — Understand what to build and pick the stack *(generic — applies to any branch)*
2. **Phase 2: Sketching & Data Modeling** (4 stages) — Design entities, data, endpoints, and UI sketches
3. **Phase 3: UI Polish** (5 stages) — Style the views
4. **Phase 4: Prototype Implementation** (3 stages: setup + alternating implementation loop) — Build it, use case by use case
5. **Phase 5: Deployment** (skeleton) — Deploy the prototype to a real environment

**This workflow produces a working prototype.** Phase 5 handles deployment; a separate "Correctness Workflow" (future) takes the prototype to production quality.

### Game Branch Phases

The Game workflow has **five phases**:

1. **Phase 1: Discovery + Tech Selection** (6 stages) — Understand what to build and pick the engine *(largely generic — Stage 1-4 adapted for mechanics)*
2. **Phase 2: Game Design** (4 stages) — Core loop, entities, level design (optional), consolidation
3. **Phase 3: Visual & Audio Design** (3 stages) — Primitive visual specs, audio plan, consolidation
4. **Phase 4: Prototype Implementation** (4 stages: setup + alternating implementation loop) — Build mechanic by mechanic
5. **Phase 5: Distribution** (skeleton) — Package and share the prototype

**This workflow produces a playable game prototype using geometric primitives (rectangles, circles, triangles) for all visual assets.** Real asset production strategy is defined separately.

**Before doing any work, identify which stage we're in and read the corresponding stage file.**

## Conversation Logging

Each stage session should produce one final log file.

### Logging Strategy

- **During session**: Auto-export runs every 5 minutes for crash protection (temporary)
- **On stage completion**: Export the final log using `/export-log <phase>-<stage>`
- **Off-stage conversations**: No logs kept (can be reviewed manually if needed)

### Exporting Logs

At the end of each stage session:

```bash
/export-log 2-1
```

This creates: `docs/logs/stage-2-1-entity-ui-sketching-20260203-143022.txt`

### Log Naming Convention

Format: `stage-<phase>-<stage>-<name>-<YYYYMMDD>-<HHMMSS>.txt`

Examples:
- `stage-00-meta-workflow-20260203-091500.txt`
- `stage-1-4-use-case-discovery-20260203-143022.txt`
- `stage-2-1-entity-ui-sketching-20260204-101530.txt`

## Stage Files

### On-Demand Stages

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 0 | `workflow/web/stages/phase-0/00-meta-workflow.md` | Workflow Engineer | `workflow-changelog.md` |
| diagram | `workflow/web/stages/phase-0/01-diagram-assistant.md` | Visual Communicator | `assets/diagrams/*.md` |
| import | `workflow/web/stages/phase-0/02-import-artifact.md` | Artifact Importer | `imported-artifacts/*-imported.md` |
| knowledge | `workflow/web/stages/phase-0/03-knowledge-tester.md` | Interview Coach | No artifacts (preparation only) |
| teacher | `workflow/web/stages/phase-0/04-teacher.md` | Patient Teacher | No artifacts (learning sessions) |
| git | `workflow/web/stages/phase-0/05-git-assistant.md` | Version Control Engineer | No artifacts (operational) |

**On-demand stages** are not part of the phase cycle. Invoke them anytime:
- **Stage 0** (`/start-stage 0`) — Fix workflow issues
- **Stage diagram** (`/start-stage diagram`) — Generate diagrams and visual aids from artifacts
- **Stage import** (`/start-stage import`) — Import external artifacts and adapt them to workflow format
- **Stage knowledge** (`/start-stage knowledge`) — Pre-meeting knowledge check (quiz yourself on all decisions)
- **Stage teacher** (`/start-stage teacher`) — Socratic teaching sessions (explain concepts, rubber duck mode)
- **Stage git** (`/start-stage git`) — Git and version control operations

### Phase 1: Discovery + Tech Selection

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 1-1 | `workflow/web/stages/phase-1/01-project-definition.md` | Project Initiator | `project-brief.md` |
| 1-2 | `workflow/web/stages/phase-1/02-knowledge-audit.md` | Knowledge Auditor | `knowledge-audit.md` |
| 1-3 | `workflow/web/stages/phase-1/03-research.md` | Research Analyst | `research-findings.md` |
| 1-4 | `workflow/web/stages/phase-1/04-use-case-discovery.md` | Use Case Analyst | `use-cases.md` |
| 1-5 | `workflow/web/stages/phase-1/05-tech-selection.md` | Tech Lead | `tech-stack.md`, `adrs/` |
| 1-6 | `workflow/web/stages/phase-1/06-consolidation.md` | Technical Writer | **`consolidation-artifacts/phase-1-consolidation.md`** |

### Phase 2: Sketching & Data Modeling

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 2-1 | `workflow/web/stages/phase-2/01-entity-ui-sketching.md` | Domain Modeler + UI Sketcher | `entity-map.md`, `assets/views/*.html`, `view-entity-mapping.md` |
| 2-2 | `workflow/web/stages/phase-2/02-data-modeling.md` | Data Architect | `data-model-conceptual.md`, `data-model-physical.md`, `assets/schema.sql`, `assets/diagrams/entity-diagram.md` |
| 2-3 | `workflow/web/stages/phase-2/03-endpoint-design.md` | API Designer | `api-design.md` (with JSON contracts + view-endpoint mapping) |
| 2-4 | `workflow/web/stages/phase-2/04-consolidation.md` | Technical Writer | **`consolidation-artifacts/phase-2-consolidation.md`**, `assets/` |

### Phase 3: UI Polish

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 3-1 | `workflow/web/stages/phase-3/01-visual-design.md` | UI Designer | Main view styled, `phase-3-design-decisions.md`, `assets/css/styles.css` |
| 3-2 | `workflow/web/stages/phase-3/02-core-app-views.md` | UI Designer | Core app views styled |
| 3-3 | `workflow/web/stages/phase-3/03-user-views.md` | UI Designer | User views styled |
| 3-4 | `workflow/web/stages/phase-3/04-auth-views.md` | UI Designer | Auth views styled |
| 3-5 | `workflow/web/stages/phase-3/05-consolidation.md` | Technical Writer | **`consolidation-artifacts/ui-style-guide.md`**, updated `index.html` |

**`phase-3-design-decisions.md`** is a living artifact shared across all Phase 3 stages.

### Phase 4: Prototype Implementation

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 4-1 | `workflow/web/stages/phase-4/01-project-setup.md` | Senior Developer | Architecture pattern + rules, implementation roadmap, `prototype-code/` (working skeleton), `consolidation-artifacts/implementation-decisions.md` |
| 4-2 | `workflow/web/stages/phase-4/02-implementation-loop.md` | Senior Developer | Working prototype, `implementation-decisions.md` |
| 4-3 | `workflow/web/stages/phase-4/03-learning-guide.md` | Code Mentor | Working prototype, `implementation-decisions.md` |
| 4-4 | `workflow/web/stages/phase-4/04-refactor.md` | Senior Architect | Refactored prototype, `implementation-decisions.md` (refactoring section) |

### Phase 5: Deployment

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 5-1 | `workflow/web/stages/phase-5/01-deployment.md` | Deployment Engineer | Deployed prototype |

**Phase 5 is a skeleton** — the process is minimal and will be expanded as deployment experience grows.

---

## Game Branch Stage Files

### On-Demand Stages (Game)

Same on-demand stages as Web. All on-demand stage files exist under `workflow/game/stages/phase-0/`.

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 0 | `workflow/game/stages/phase-0/00-meta-workflow.md` | Workflow Engineer | `workflow-changelog.md` |
| diagram | `workflow/game/stages/phase-0/01-diagram-assistant.md` | Visual Communicator | `assets/diagrams/*.md` |
| import | `workflow/game/stages/phase-0/02-import-artifact.md` | Artifact Importer | `imported-artifacts/*-imported.md` |
| knowledge | `workflow/game/stages/phase-0/03-knowledge-tester.md` | Interview Coach | No artifacts |
| teacher | `workflow/game/stages/phase-0/04-teacher.md` | Patient Teacher | No artifacts |
| git | `workflow/game/stages/phase-0/05-git-assistant.md` | Version Control Engineer | No artifacts |

### Phase 1: Discovery + Tech Selection (Game)

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 1-1 | `workflow/game/stages/phase-1/01-project-definition.md` | Project Initiator | `project-brief.md` |
| 1-2 | `workflow/game/stages/phase-1/02-knowledge-audit.md` | Knowledge Auditor | `knowledge-audit.md` |
| 1-3 | `workflow/game/stages/phase-1/03-research.md` | Research Analyst | `research-findings.md` |
| 1-4 | `workflow/game/stages/phase-1/04-mechanic-discovery.md` | Mechanic Analyst | `mechanics.md` |
| 1-5 | `workflow/game/stages/phase-1/05-tech-selection.md` | Tech Lead | `tech-stack.md`, `adrs/` |
| 1-6 | `workflow/game/stages/phase-1/06-consolidation.md` | Technical Writer | **`consolidation-artifacts/phase-1-consolidation.md`** |

### Phase 2: Game Design

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 2-1 | `workflow/game/stages/phase-2/01-core-loop-design.md` | Game Designer | `core-loop.md` |
| 2-2 | `workflow/game/stages/phase-2/02-entity-design.md` | Game Designer + Systems Designer | `entity-design.md` |
| 2-3 | `workflow/game/stages/phase-2/03-level-design.md` | Level Designer | `level-design.md` *(optional — skip if no levels)* |
| 2-4 | `workflow/game/stages/phase-2/04-consolidation.md` | Technical Writer | **`consolidation-artifacts/phase-2-consolidation.md`** |

### Phase 3: Visual & Audio Design

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 3-1 | `workflow/game/stages/phase-3/01-visual-design.md` | Visual Designer | `visual-design.md` |
| 3-2 | `workflow/game/stages/phase-3/02-audio-design.md` | Audio Designer | `audio-design.md` |
| 3-3 | `workflow/game/stages/phase-3/03-consolidation.md` | Technical Writer | **`consolidation-artifacts/phase-3-consolidation.md`** |

### Phase 4: Prototype Implementation (Game)

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 4-1 | `workflow/game/stages/phase-4/01-project-setup.md` | Senior Developer | Architecture pattern, implementation roadmap, `prototype-code/` skeleton, `implementation-decisions.md` |
| 4-2 | `workflow/game/stages/phase-4/02-implementation-loop.md` | Senior Developer | Working prototype, `implementation-decisions.md` |
| 4-3 | `workflow/game/stages/phase-4/03-learning-guide.md` | Code Mentor | Working prototype, `implementation-decisions.md` |
| 4-4 | `workflow/game/stages/phase-4/04-refactor.md` | Senior Architect | Refactored prototype, `implementation-decisions.md` (refactoring section) |

### Phase 5: Distribution (Game)

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 5-1 | `workflow/game/stages/phase-5/01-distribution.md` | Deployment Engineer | Distributed prototype |

**Phase 5 is a skeleton** — distribution process will be expanded with real game projects.

**Stage 4-2 and 4-3 are alternatives** — use 4-2 (AI implements, you review) or 4-3 (you implement, AI guides) per mechanic. Both repeat until all mechanics are complete, following the architectural rules from Stage 4-1.

**Stage 4-4** runs once after all mechanics are implemented. Audits the codebase, proposes a refactor roadmap (loop purity, input abstraction, constants, entity patterns, state management, audio decoupling), then refactors one area at a time.

---

**Stage 4-1** establishes the architecture pattern (Ports & Adapters, Layered, or Clean Architecture), its binding rules, and the approved use case implementation order — before any code is written.

**Stage 4-2 and 4-3 are alternatives** — use 4-2 (AI writes, you review) or 4-3 (you write, AI guides) per use case. Both repeat until all use cases are complete, following the architectural rules and order established in Stage 4-1. `implementation-decisions.md` is a shared persistence document — read at the start of every session, updated after every completed use case (checkpoint).

**Stage 4-4** runs once after all use cases are implemented. It audits the codebase, proposes a refactor roadmap (error handling, input validation, security basics, layer enforcement), then refactors one area at a time with a plan approved before each change. Ends with a 5-question comprehension check on what was changed and why.

## Critical Rules

1. **ALWAYS read the stage file** before starting work
2. **ALWAYS adopt the persona** defined in the stage file
3. **ALWAYS use `/start-stage`** to start stages — it automatically runs the Existing Artifact Protocol, which detects prior runs and asks how to proceed before any work begins
4. **In Phase 3: ALWAYS read `docs/phase-3-design-decisions.md` first** — it persists decisions across sessions
5. **In Phase 4: ALWAYS read `implementation-decisions.md` first** — it tracks progress and decisions across sessions
6. **Follow stage order** within each phase
7. **Complete each phase before starting the next**

## Architectural Assumptions

This workflow is scoped to a specific application type:
- **Web application** (browser-based UI)
- **SPA frontend** (single-page application — React, Vue, Svelte, etc.)
- **REST API** (JSON over HTTP, stateless)
- **JWT authentication** (Bearer token — stateless, no server-side sessions)
- **Separated frontend and backend**
- **SQL database** (relational persistence)
- **SQLite for prototyping** (always, regardless of production DB)

The architecture is not a decision point — it's a given. Tech selection (Stage 1-5) picks the specific technologies within this archetype.

## Phase Handoffs

### Phase 1 → Phase 2

Stage 1-6 produces `consolidation-artifacts/phase-1-consolidation.md` (includes tech stack summary) — the **primary input** for Phase 2.

### Phase 2 → Phase 3

Stage 2-4 consolidates Phase 2 work into `consolidation-artifacts/phase-2-consolidation.md` — the primary artifact forwarded to Phase 3. Also forwarded: `docs/view-entity-mapping.md` (Stage 2-1), `docs/api-design.md` (Stage 2-3, includes view-endpoint mapping with JSON contracts), and the `docs/assets/` folder.

### Phase 3 → Phase 4

Stage 3-5 consolidates all Phase 3 work into `consolidation-artifacts/ui-style-guide.md` — a comprehensive style guide whose Decision Log captures everything from `phase-3-design-decisions.md` (the Phase 3 working document, which is not forwarded to Phase 4). Phase 4 uses all prior artifacts: styled views, endpoint contracts, SQLite schema, and tech stack.

The styled HTML views from Phase 3 are **design references** for SPA component development in Phase 4. The backend implements a pure JSON API — no template conversion is needed.

### Phase 4 → Phase 5: Deployment

Phase 4 produces a refactored working prototype: all use cases implemented, all tests passing, architecture cleaned up (Stage 4-4). Phase 5 deploys it to a real environment. The process is minimal now and will be expanded as deployment experience grows.

### Phase 5 → Correctness Workflow (Future)

The Correctness Workflow (not yet designed) takes the deployed prototype and adds production-grade architecture, security, logging, and observability.

## How to Determine Current Stage

Check `docs/` for existing artifacts:

**Phase 1 (Discovery + Tech Selection):**
- No artifacts → Stage 1-1
- `project-brief.md` → Stage 1-2
- `knowledge-audit.md` → Stage 1-3
- `research-findings.md` → Stage 1-4
- `use-cases.md` → Stage 1-5
- `tech-stack.md` → Stage 1-6
- `consolidation-artifacts/phase-1-consolidation.md` → Phase 1 complete

**Phase 2 (Sketching & Data Modeling):**
- `consolidation-artifacts/phase-1-consolidation.md` exists but no `entity-map.md` → Stage 2-1
- `entity-map.md` → Stage 2-2
- `data-model-physical.md` → Stage 2-3
- `api-design.md` → Stage 2-4
- `consolidation-artifacts/phase-2-consolidation.md` → Phase 2 complete

**Phase 3 (UI Polish):**
- `consolidation-artifacts/phase-2-consolidation.md` exists but no `phase-3-design-decisions.md` → Stage 3-1
- `phase-3-design-decisions.md` + styled main view → Stage 3-2
- Core app views styled → Stage 3-3
- User views styled → Stage 3-4
- Auth views styled → Stage 3-5
- `consolidation-artifacts/ui-style-guide.md` → Phase 3 complete

> To detect Phase 3 sub-stages: read `docs/phase-3-design-decisions.md` → View Decisions section. First check the **Main View (reference implementation)** entry — if it is still plain HTML, Stage 3-1 is incomplete; continue Stage 3-1. Otherwise, views marked INCLUDE that still have plain HTML (no CSS framework classes applied) indicate the current unfinished stage based on their category: core app views → still in 3-2, user views → still in 3-3, auth views → still in 3-4.

**Phase 4 (Prototype Implementation):**
- `consolidation-artifacts/ui-style-guide.md` exists but no `consolidation-artifacts/implementation-decisions.md` → Stage 4-1
- `consolidation-artifacts/implementation-decisions.md` exists (use cases not all complete) → Stage 4-2 or 4-3 (user's choice per use case)
- `consolidation-artifacts/implementation-decisions.md` with all use cases complete but no `## Refactoring` section → Stage 4-4
- `consolidation-artifacts/implementation-decisions.md` with `## Refactoring` section and refactoring incomplete → Stage 4-4 (resume)
- `consolidation-artifacts/implementation-decisions.md` with all refactor areas complete → **Prototype refactored → Stage 5-1**

## Quick Commands

### Slash Commands (Skills)

- `/start-stage <phase>-<stage>` → Start a specific stage (e.g., `/start-stage 2-1`)
- `/start-stage 0` → Meta-Workflow (fix workflow issues)
- `/start-stage diagram` → Diagram Assistant (visualize artifacts)
- `/start-stage import` → Import an external artifact into workflow format
- `/start-stage knowledge` → Knowledge Tester (pre-meeting quiz)
- `/start-stage teacher` → Teacher (Socratic learning sessions)
- `/start-stage git` → Git Assistant (version control operations)
- `/export-log <phase>-<stage>` → Export conversation to docs/logs/

### Natural Language

- "Start stage 0" → Meta-Workflow (fix workflow issues)
- "Start stage 2-1" → Entity & UI Sketching
- "What stage are we in?" → Check docs/ for artifacts
- "Export the log" → Save conversation

### Built-in Claude Code Commands

- `/export <file>` → Export conversation
- `/compact` → Compress long conversations
- `/context` → See context usage
- `/cost` → See token usage

## Project Structure

```
project-root/
├── AGENTS.md                    ← You are here (project instructions — canonical)
├── CLAUDE.md                    ← Claude Code redirect to AGENTS.md
├── GEMINI.md                    ← Gemini redirect to AGENTS.md
├── .claude/
│   ├── settings.json            ← Hooks configuration
│   └── skills/                  ← Custom slash commands
│       ├── start-stage/         ← /start-stage <phase>-<stage>
│       └── export-log/          ← /export-log <phase>-<stage>
├── .agent-utils/
│   └── skills/                  ← Canonical, tool-agnostic skill content
│       ├── start-stage/
│       └── export-log/
├── imported-artifacts/          ← Raw imports + adapted *-imported.md files (Stage I)
├── consolidation-artifacts/     ← Phase milestone documents (committed to git)
├── prototype-code/              ← Working prototype code (committed to git)
├── docs/
│   ├── logs/                    ← Conversation logs
│   ├── assets/                  ← Views, CSS, SQL, diagrams
│   ├── adrs/                    ← Architecture Decision Records
│   └── *.md                     ← Working design artifacts
└── workflow/
    ├── web/                     ← ACTIVE WORKFLOW (Web: SPA + REST + SQL)
    │   └── stages/
    │       ├── phase-0/         ← Meta-workflow (on-demand)
    │       ├── phase-1/         ← Discovery + Tech Selection (generic)
    │       ├── phase-2/         ← Sketching & Data Modeling
    │       ├── phase-3/         ← UI Polish
    │       ├── phase-4/         ← Prototype Implementation
    │       └── phase-5/         ← Deployment (skeleton)
    ├── templates/               ← Output templates
    └── scripts/                 ← Automation scripts
```

## Artifact Storage

- Phase milestone documents: `consolidation-artifacts/`
- Working prototype code: `prototype-code/`
- Working design artifacts: `docs/`
- Assets (views, CSS, SQL): `docs/assets/`
- Architecture decisions: `docs/adrs/`
- Conversation logs: `docs/logs/`
- Workflow changelog: `docs/workflow-changelog.md`
- Stage files: `workflow/web/stages/phase-N/`

## Project Status

> Current phase and stage are determined by checking `docs/` for existing artifacts — see "How to Determine Current Stage" above.

### Meta Artifacts
- [ ] `workflow-changelog.md` ← Workflow fixes log

### Phase 1: Discovery + Tech Selection
- [ ] `project-brief.md`
- [ ] `knowledge-audit.md`
- [ ] `research-findings.md`
- [ ] `use-cases.md`
- [ ] `tech-stack.md`
- [ ] `adrs/` (decision records)
- [ ] **`consolidation-artifacts/phase-1-consolidation.md`** ← Phase 1 complete

### Phase 2: Sketching & Data Modeling
- [ ] `entity-map.md`
- [ ] `assets/views/` (plain HTML)
- [ ] `view-entity-mapping.md`
- [ ] `data-model-conceptual.md` (agnostic)
- [ ] `data-model-physical.md` (SQLite)
- [ ] `assets/schema.sql` (SQLite with mock data)
- [ ] `assets/diagrams/entity-diagram.md`
- [ ] `api-design.md` (with JSON contracts + view-endpoint mapping)
- [ ] **`consolidation-artifacts/phase-2-consolidation.md`** ← Phase 2 complete

### Phase 3: UI Polish
- [ ] `phase-3-design-decisions.md` ← Living decisions file (all stages read/update)
- [ ] `assets/css/styles.css`
- [ ] Styled main view ← Stage 3-1 complete
- [ ] Styled core app views ← Stage 3-2 complete
- [ ] Styled user views ← Stage 3-3 complete
- [ ] Styled auth views ← Stage 3-4 complete
- [ ] **`consolidation-artifacts/ui-style-guide.md`** ← Phase 3 complete

### Phase 4: Prototype Implementation
- [ ] `prototype-code/` created ← Stage 4-1 complete
- [ ] `consolidation-artifacts/implementation-decisions.md` initialized ← Stage 4-1 complete
- [ ] Design Priority 1 use cases implemented + tested
- [ ] Design Priority 2 use cases implemented + tested
- [ ] Design Priority 3 use cases implemented + tested
- [ ] **All tests passing** ← Prototype complete (4-2/4-3 done)
- [ ] Refactor roadmap approved ← Stage 4-4 started
- [ ] All refactor areas complete + comprehension check passed ← Stage 4-4 complete

### Phase 5: Deployment
- [ ] Prototype deployed to a real environment ← Phase 5 complete

## Final Output

The Web Workflow produces a **deployed working prototype** with:
- Implemented REST endpoints for all use cases
- SQLite database with mock data
- Automated tests (unit + integration)
- Styled HTML views
- Complete design documentation
- Deployment to a real environment

The **Correctness Workflow** (future, separate) takes this prototype to production quality.
