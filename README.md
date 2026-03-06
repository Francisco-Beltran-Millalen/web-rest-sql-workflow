# Web Workflow (SPA + REST + SQL)

A structured, AI-collaborative workflow for building web application prototypes — from raw idea to working code, one stage at a time.

---

## What This Is

This is not a tool. It is a **process**.

A sequence of stages, each with a defined goal, a persona, concrete input artifacts, and concrete output artifacts. You run it with an LLM CLI (Claude Code, Gemini CLI, or any tool that supports `AGENTS.md`). The AI plays a role in each stage — asking questions, proposing designs, writing code — and you approve, adjust, and steer.

The workflow is specialized for a specific type of software: **web applications with REST endpoints, a separated backend and frontend, and a SQL database**. But the underlying philosophy is generic and can be adapted to any domain.

---

## Core Philosophies

These are the ideas that make this workflow work. They are transferable to any workflow you build on top of this foundation.

### 1. Collaborative by Design — AI Proposes, You Approve

Every significant decision goes through a propose-approve loop. The AI suggests a data model, an endpoint signature, a function contract, a design direction. You say yes, no, or adjust. Nothing is implemented without your sign-off.

This keeps you in control without requiring you to drive every detail. You stay oriented — you understand every piece of the system being built — without doing all the work.

### 2. Personas Per Stage — Not a Generic Assistant

Each stage has a defined persona with a specific responsibility:

- **Project Initiator** — asks questions until the idea is clear
- **Knowledge Auditor** — surfaces what you know and what you don't
- **Data Architect** — turns entities into database schemas
- **Senior Developer** — implements one use case at a time
- **Workflow Engineer** — fixes the workflow itself

The persona frames what the AI pays attention to and what it ignores. A Knowledge Auditor does not write code. A Senior Developer does not redesign the data model. The role prevents scope creep and keeps sessions focused.

### 3. Artifacts as Context Bridges

Every stage consumes specific input artifacts and produces specific output artifacts. The output of one stage is the input of the next.

This means:
- Sessions can end at any time — the artifacts capture the state
- New sessions start by reading artifacts, not by relying on conversation memory
- Handoffs between phases are explicit and verifiable

The workflow does not depend on a continuous conversation thread. It depends on files.

### 4. Phase 0 — The Workflow Improves Itself

Stage 0 (Meta-Workflow) is a dedicated stage for fixing the workflow itself. When a stage instruction is unclear, a script fails, or the AI behaves unexpectedly, you invoke Stage 0. A Workflow Engineer persona diagnoses the problem, applies a fix, and logs the change to `docs/workflow-changelog.md`.

Every workflow improvement is documented. The system gets better over time and the history of changes is searchable.

### 5. Prototype Mindset

The workflow produces a **working prototype** — not production code. The goal is to validate the design by building something real. Speed and correctness are in tension; this workflow resolves it by choosing speed first.

Phase 5 deploys the prototype. A separate "Correctness Workflow" (not included here) takes it to production quality.

This separation matters because prototyping decisions (SQLite instead of Postgres, no caching, no deployment config) are different from production decisions. Mixing them slows the prototype phase without improving the design.

### 6. Logs as Institutional Memory

Every stage session is exported as a human-readable transcript. The log captures what was discussed, what was decided, and why. Over the course of a project, the logs become a record of the design process — not just the design.

Auto-export runs every 5 minutes during a session (crash protection). A final export is made at the end of each stage.

### 7. Tool-Agnostic by Design

The canonical workflow instructions live in `AGENTS.md` — the standard adopted by Claude Code, Gemini CLI, GitHub Copilot, Cursor, and others (Linux Foundation / Agentic AI Foundation, December 2025). Tool-specific configuration (`.claude/`, `.gemini/`) contains only thin wrappers that delegate to the canonical layer in `.agent-utils/`.

Adding support for a new LLM tool requires:
1. A tool-specific skill wrapper for `start-stage`
2. A tool-specific skill wrapper for `export-log` (with the tool's transcript path and a converter script)
3. A converter script extending `workflow/scripts/convert_transcript_generic.py`

---

## This Workflow: Web (SPA + REST + SQL)

The `web` workflow is a specialization for building web applications with:
- A **SPA frontend** (single-page application — React, Vue, Svelte, etc.)
- A **REST API** (JSON over HTTP, stateless)
- **JWT authentication** (Bearer token — no server-side sessions)
- A **separated frontend and backend**
- A **SQL database** (SQLite for prototyping, any relational DB for production)

**Note:** Server-rendered templates and hybrid approaches (HTMX, etc.) are out of scope for this workflow.

### The Five Phases

| Phase | Goal | Stages |
|-------|------|--------|
| **Phase 1: Discovery + Tech Selection** | Understand what to build and pick the stack *(generic — applies to any workflow branch)* | 6 stages |
| **Phase 2: Sketching & Data Modeling** | Design entities, data model, endpoints, and UI sketches | 4 stages |
| **Phase 3: UI Polish** | Style the plain HTML views into a working interface | 5 stages |
| **Phase 4: Prototype Implementation** | Build it, refactor it | 4 stages (setup + alternating loop + refactor) |
| **Phase 5: Deployment** | Deploy the prototype to a real environment | 1 stage (skeleton) |

### On-Demand Stages

Six stages run outside the phase cycle, whenever needed:

| Stage | Purpose |
|-------|---------|
| **Stage 0** — Meta-Workflow | Fix the workflow itself |
| **Stage diagram** — Diagram Assistant | Visualize any artifact as a Mermaid diagram |
| **Stage import** — Artifact Importer | Bring in an external artifact (Swagger spec, SQL schema, project doc) and adapt it to the workflow's format |
| **Stage knowledge** — Knowledge Tester | Pre-meeting quiz on all decisions made so far |
| **Stage teacher** — Teacher | Socratic learning sessions and rubber duck debugging |
| **Stage git** — Git Assistant | Version control operations |

### What It Produces

- A working prototype with real endpoints and a real database
- Automated tests (unit + integration) for every implemented use case
- Styled HTML views
- Complete design documentation (`project-brief.md`, `use-cases.md`, `api-design.md`, `ui-style-guide.md`, and more)
- Architecture Decision Records for all significant tech choices

---

## Prerequisites

See [`PREREQUISITES.md`](PREREQUISITES.md) for the full list with installation instructions.

**Required:**
- An LLM CLI that supports `AGENTS.md` (Claude Code recommended)
- Python 3 (workflow scripts)
- bash (hook scripts)
- SQLite CLI (schema validation in Phase 2)
- A web browser (reviewing HTML views in Phases 2 and 3)

**Quick check:**
```bash
echo "Python 3:  $(python3 --version 2>/dev/null || echo 'NOT FOUND')"
echo "bash:      $(bash --version 2>/dev/null | head -1 || echo 'NOT FOUND')"
echo "sqlite3:   $(sqlite3 --version 2>/dev/null || echo 'NOT FOUND')"
```

---

## Quick Start

1. **Clone this repo** into your new project directory
   ```bash
   git clone <repo-url> my-project
   cd my-project
   ```

2. **Open the project** in your LLM CLI
   ```bash
   claude  # or: gemini, cursor, etc.
   ```

3. **Start Stage 1-1** to begin Discovery
   ```bash
   /start-stage 1-1
   ```

4. **Follow the stage**. The AI will adopt the Project Initiator persona and ask about your idea. Answer, discuss, and at the end of the session, export the log:
   ```bash
   /export-log 1-1
   ```

5. **Continue stage by stage.** Each stage reads the outputs of the previous one. The workflow guides you.

---

## Project Structure

```
project-root/
├── AGENTS.md                    ← Canonical workflow instructions (read by all LLM tools)
├── CLAUDE.md                    ← Claude Code redirect → AGENTS.md
├── GEMINI.md                    ← Gemini CLI redirect → AGENTS.md
├── README.md                    ← You are here
├── PREREQUISITES.md             ← Tool installation requirements
├── .claude/
│   ├── settings.json            ← Hook configuration (auto-export, session start)
│   └── skills/                  ← Claude Code slash commands (thin wrappers)
│       ├── start-stage/
│       └── export-log/
├── .agent-utils/
│   └── skills/                  ← Canonical, tool-agnostic skill content
│       ├── start-stage/
│       └── export-log/
├── imported-artifacts/          ← Raw imports + adapted *-imported.md files (Stage I)
├── consolidation-artifacts/     ← Phase milestone documents (committed to git)
├── prototype-code/              ← Working prototype code (committed to git)
├── docs/
│   ├── logs/                    ← Conversation logs (one per stage session)
│   ├── assets/                  ← Views (HTML), CSS, SQL schema, diagrams
│   ├── adrs/                    ← Architecture Decision Records
│   └── *.md                     ← Working design artifacts (project-brief.md, use-cases.md, etc.)
└── workflow/
    ├── web/                     ← The active workflow (SPA + REST + SQL)
    │   └── stages/              ← Stage files (one per stage, organized by phase)
    ├── templates/               ← Output templates
    └── scripts/                 ← Automation scripts (log export, auto-export)
```

---

## Slash Commands

| Command | What it does |
|---------|-------------|
| `/start-stage 1-1` | Start a specific stage (Phase 1, Stage 1) |
| `/start-stage 0` | Start the Meta-Workflow (fix workflow issues) |
| `/start-stage diagram` | Start the Diagram Assistant |
| `/start-stage import` | Start the Artifact Importer |
| `/export-log 1-1` | Export the current session log for Stage 1-1 |

---

## Building Your Own Workflow

The `web` specialization lives in `workflow/web/`. The philosophy it runs on is generic.

If you wanted to build a `game` workflow or a `cli` workflow, the structure would be the same:

1. **Define your phases** — what are the natural checkpoints from idea to working prototype?
2. **Define stages within each phase** — what is the goal, the persona, the inputs, the outputs?
3. **Write stage files** following the same pattern: Persona → Purpose → Input Artifacts → Process → Output Artifacts → Exit Criteria → Next Stage
4. **Keep Stage 0** — the Meta-Workflow is universal. Every workflow needs a way to fix itself.
5. **Keep the log strategy** — export every session, auto-export for crash protection.

The core ideas that transfer to any workflow:
- Phases create clean checkpoints (you finish one before starting the next)
- Artifacts eliminate dependency on conversation memory
- The propose-approve loop keeps you oriented
- Personas prevent scope creep
- Stage 0 makes the workflow self-correcting

The `web` specialization is one application of these ideas. Build the next one on the same foundation.

---

## The Workflow Changelog

Every change to the workflow itself is logged in [`docs/workflow-changelog.md`](docs/workflow-changelog.md). This file is the record of how the workflow evolved — what problems were found, what was fixed, and why.

If you fork this workflow and improve it, the changelog is where you track those improvements.
