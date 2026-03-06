# Workflow Changelog

---

## 2026-03-06: Game development branch — full workflow design (Phases 0–5)

**Problem:** The workflow had no game development branch. Only the Web branch (SPA + REST + SQL) existed. The Branching Architecture section listed "Game development" as Planned with no path.

**Cause:** The game branch was planned from the start but had not been designed. This session produced the full design.

**Fix:** Created `workflow/game/` with all stage files (25 files across 6 phases). Design decisions:
- Phase 0 (on-demand tools): copied from web with game-specific adaptations (import heuristics, knowledge tester categories, diagram types)
- Phase 1: largely same structure as web; Stage 1-4 replaced `use-case-discovery` with `mechanic-discovery` (core loop → player mechanics ping-pong → world mechanics 3-by-3 → standard systems)
- Phase 2 (Game Design): new — core-loop-design (states, win/lose conditions), entity-design (properties, behaviors, primitive visuals, interaction matrix), level-design (optional/conditional), consolidation
- Phase 3 (Visual & Audio Design): simplified for prototype era — visual-design (color palette, entity → shape/color/size, HUD, menus, animation descriptions), audio-design (SFX event map, music mood, source plan skeleton), consolidation
- Phase 4 (Implementation): adapted from web; implementation loop per **mechanic** instead of per use case; architecture options are Simple OOP vs ECS (not fixed like web's REST pattern); "health check" = window opens + player primitive visible; refactor audit dimensions are game-specific (loop purity, input abstraction, constants, entity patterns, state management, audio decoupling)
- Phase 5 (Distribution): skeleton matching web's approach
- Prototype asset strategy: all visual assets use geometric primitives (rectangles, circles, triangles + colors) — no image files required
- Level design (Stage 2-3): optional/conditional — skip if game has no distinct levels
- Updated `start-stage` SKILL.md to detect active branch from AGENTS.md before resolving paths (supports both `workflow/web/` and `workflow/game/`)

**Files modified:**
- `workflow/game/stages/` (25 new files)
- `AGENTS.md` (game branch table, game branch phases, game stage files tables)
- `.agent-utils/skills/start-stage/SKILL.md` (branch detection + game branch stage mapping)
- `docs/workflow-changelog.md`

---

## 2026-03-06: Stage 4-4: Refactor — plan-first architecture cleanup before deployment

**Problem:** After Phase 4 implementation, the prototype works but may have inconsistent error handling, missing input validation, security basics not enforced, and layer rule violations. There was no structured stage to address this before deployment.

**Cause:** The "Correctness Workflow" was listed as a future concept but never designed. Stage 4-4 replaces it for the architecture/cleanup concern (not full production hardening, which remains future work).

**Fix:** Created `workflow/web/stages/phase-4/04-refactor.md` — a new iterative stage that:
- Audits the codebase across 5 dimensions (error handling, validation, security, layer rules, config)
- Proposes a refactor roadmap, approved by the user before any code is touched
- Iterates one area at a time: plan → approve → implement → verify tests pass
- Ends with a 5-question comprehension check on what was changed and why (AI explains wrong answers)

Updated "How to Determine Current Stage" in AGENTS.md to detect Stage 4-4 from the presence/absence of `## Refactoring` in `implementation-decisions.md`.

**Files modified:**
- `workflow/web/stages/phase-4/04-refactor.md` (new)
- `workflow/web/stages/phase-4/02-implementation-loop.md` (updated "What Comes Next")
- `workflow/web/stages/phase-4/03-learning-guide.md` (updated "What Comes Next")
- `AGENTS.md`
- `.agent-utils/skills/start-stage/SKILL.md`
- `README.md`
- `docs/workflow-changelog.md`

---

## 2026-03-06: Web workflow restructuring — branching architecture, improved tech selection, Phase 5

**Problem:** The workflow was named `spa-rest-sql` with no branching concept. Phase 1 is generic (works for any project type), but this was not documented. The tech selection stage (1-5) lacked structure — no format for trade-off tables, no prioritization step before selection, and all categories were presented as a flat list without confirmation gates. There was no deployment phase.

**Cause:** The workflow was designed as a single linear path. As it matures, it needs to branch at Phase 2 by project type, and extend beyond prototype implementation into deployment.

**Fix:**
1. Renamed `workflow/spa-rest-sql/` → `workflow/web/` — the current workflow is a web specialization
2. Updated `AGENTS.md` with a branching architecture section: Phase 1 is generic; Phase 2+ branches by project type (Web active; Game/CLI/Mobile/Desktop planned)
3. Improved `workflow/web/stages/phase-1/05-tech-selection.md`: added Step 0 (decision priorities), structured comparison table format, and one-category-at-a-time confirmation rule
4. Created `workflow/web/stages/phase-5/01-deployment.md` — skeleton stage for deployment (to be expanded with experience)
5. Updated all path references in `AGENTS.md` and `.agent-utils/skills/start-stage/SKILL.md`

**Files modified:**
- `workflow/spa-rest-sql/` → renamed to `workflow/web/`
- `AGENTS.md`
- `.agent-utils/skills/start-stage/SKILL.md`
- `workflow/web/stages/phase-1/05-tech-selection.md`
- `workflow/web/stages/phase-5/01-deployment.md` (new)
- `docs/workflow-changelog.md`
- `memory/MEMORY.md`

---

## 2026-03-06: Windows compatibility, new stages, descriptive stage identifiers

**Problem 1:** Hooks (`SessionStart`/`SessionEnd`) failed on Windows — `.sh` files are not executable without an explicit shell prefix.

**Problem 2:** The `export-log` skill used `pwd | sed 's|/|-|g'` to locate the Claude projects directory. This broke in two ways: (a) on Windows with Git Bash, `pwd` returns `/c/Users/...` which encodes differently from what Claude uses (`C--Users-...`); (b) when Claude Code is working inside a project subdirectory (common in Phase 4), `pwd` returns the subdirectory path — causing a lookup in the wrong project directory entirely. Relative paths in the converter command had the same CWD-sensitivity problem.

**Problem 3:** New on-demand stages Teacher (`04-teacher.md`) and Git Assistant (`05-git-assistant.md`) were created but not registered in SKILL.md files or AGENTS.md.

**Problem 4:** On-demand stage identifiers (`d`, `i`, `t`, `e`, `g`) were single letters with no mnemonic value — hard to remember without consulting documentation.

**Problem 5:** Python detection used `command -v python3 || command -v python || command -v py`. On Windows, `python3` resolves to a Microsoft Store stub that exits with code 49 — `command -v` succeeds but running it fails, so the detection returned a broken command.

**Cause:**
- Hooks: missing `bash` prefix in `.claude/settings.json`
- `export-log`: CWD-relative path logic; Unix-only path encoding; `python3` assumed
- New stages: stage files created without updating skill registration or AGENTS.md
- Identifiers: single-letter convention inherited from initial design, never revisited
- Python detection: `command -v` only checks existence, not whether the command actually runs

**Fix:**
1. **Hooks** — Added `bash` prefix to both hook commands in `.claude/settings.json`
2. **`export-log` skill** — Rewrote path resolution: Python script searches upward from CWD for `AGENTS.md` to anchor the project root (works from any subdirectory, any OS); encodes path using `os.sep` to avoid backslash escaping issues; uses absolute paths for converter script and output file
3. **`session-start.sh`** — Applied same project-root and Python detection fixes
4. **Stage registration** — Registered `teacher` and `git` in both SKILL.md files and AGENTS.md (arguments list, stage mapping, on-demand stages table, quick commands)
5. **Stage identifier rename** — Replaced single-letter identifiers with descriptive words across all stage files, both SKILL.md files, and AGENTS.md:
   - `d` → `diagram`, `i` → `import`, `t` → `knowledge`, `e` → `teacher`, `g` → `git`
6. **Python detection** — Replaced `command -v` chain with a probe-and-test loop that verifies each candidate actually runs before selecting it; tries `python3`, `python`, `py` in order

**Files:** `.claude/settings.json`, `.claude/skills/export-log/SKILL.md`, `.agent-utils/skills/start-stage/SKILL.md`, `.agent-utils/skills/export-log/SKILL.md`, `AGENTS.md`, `workflow/scripts/session-start.sh`, `workflow/spa-rest-sql/stages/phase-0/01-diagram-assistant.md`, `workflow/spa-rest-sql/stages/phase-0/02-import-artifact.md`, `workflow/spa-rest-sql/stages/phase-0/03-knowledge-tester.md`, `workflow/spa-rest-sql/stages/phase-0/04-teacher.md`, `workflow/spa-rest-sql/stages/phase-0/05-git-assistant.md`

---

## 2026-03-01: Full audit — docs/ prefix, persona name, AGENTS.md references

**Problem:** Full audit of all 20 stage files revealed a systemic issue: 14 stages listed input artifacts without the `docs/` prefix, meaning an AI reading those lists could look for files in the project root instead of `docs/`. Additionally, body text "Read X" instructions in Phase 3 and 4-1 had the same omission. Two read instructions in AGENTS.md referenced `phase-3-design-decisions.md` without `docs/`. Stage 2-1 used `&` instead of `+` in the persona name (inconsistent with AGENTS.md table).

**Cause:** The `docs/` prefix issue was identified in the previous audit for two instances (Stage 4-2/4-3, `use-cases.md`) but was not applied systematically across all stages. No prior audit had checked body text or AGENTS.md read instructions.

**Fix:**
1. **Input Artifacts `docs/` prefix** — Added `docs/` prefix to all affected input artifact lists: stages 1-2, 1-3, 1-4, 1-5, 1-6, 2-2, 2-3, 2-4, 3-2, 3-3, 3-4, 4-1, 4-2, 4-3.
2. **Body text `docs/` prefix** — Fixed `Read 'phase-3-design-decisions.md'` and navigation-pattern references in stages 3-2, 3-3, 3-4; fixed `Read 'tech-stack.md'` and schema reference in Stage 4-1.
3. **Exit criteria** — Updated `phase-3-design-decisions.md` references in exit criteria of 3-2, 3-3, 3-4 to include `docs/`.
4. **AGENTS.md** — Fixed Critical Rule #4 and the Phase 3 detection note to use `docs/phase-3-design-decisions.md`.
5. **Stage 2-1 persona** — Changed `Domain Modeler & UI Sketcher` → `Domain Modeler + UI Sketcher` (matches AGENTS.md table).

**Files:** stages 1-2, 1-3, 1-4, 1-5, 1-6, 2-1, 2-2, 2-3, 2-4, 3-1, 3-2, 3-3, 3-4, 3-5, 4-1, 4-2, 4-3, `AGENTS.md`

**Follow-up fixes (same session):**
- Stage 3-1 Input Artifacts: `view-entity-mapping.md` was also missing `docs/`
- Stage 3-5 Input Artifacts and body text: `phase-3-design-decisions.md` was also missing `docs/`
- AGENTS.md Phase 2→3 handoff: said "Stage 2-4 produces `view-entity-mapping.md`" which was factually wrong (Stage 2-1 produces it). Reworded to accurately describe what each stage contributes.

---

## 2026-03-01: Add comprehension check at end of each use case (Stage 4-2 and 4-3)

**Problem:** After implementing a use case, the user moved straight to the next one without narrating what was built. No mechanism ensured understanding before continuing.

**Cause:** Stage 4-2 and 4-3 had no explicit comprehension verification step after tests passed.

**Fix:**
- **Stage 4-2**: Added Step 7 "Comprehension Check" between Verify and Checkpoint. AI asks 5 questions (functions written, inputs/outputs, purpose, architecture layer, data flow). Up to 3 attempts — AI corrects mistakes and asks again. After 3 failed attempts, AI lists the unresolved concepts and tells the user to study them independently, then proceeds to checkpoint. Old Step 7 renumbered to Step 8.
- **Stage 4-3**: Added Step 6 "End-to-End Narration" between Verify and Checkpoint. Since the user already explained each function before writing it, this step asks for a holistic walkthrough — full data flow from HTTP request to response. Same 3-attempt rule applies. Old Step 6 renumbered to Step 7.
- Both stages: added corresponding exit criterion.

**Files:**
- `workflow/spa-rest-sql/stages/phase-4/02-implementation-loop.md`
- `workflow/spa-rest-sql/stages/phase-4/03-learning-guide.md`

---

## 2026-03-01: Pre-commit audit — 5 fixes in template, Stage 4-2/4-3, and SKILL.md

**Problem:** Pre-commit audit found 5 issues (2 medium, 3 low) introduced or left unresolved by the previous audit session.

**Cause/Fix (by issue):**

1. **M1 — `implementation-decisions.md` template heading mismatch.** Template used `## Next Session Starts With` but Stage 4-1's initialization inline uses `## Next Session`, and Stage 4-2's Checkpoint instructions explicitly say "Update 'Next Session' section." The template heading was wrong relative to the authoritative source. Fix: renamed to `## Next Session`.

2. **M2 — Template section order contradicted Stage 4-1 inline.** Template placed "Next Session Starts With" before Decisions/Discoveries/Deferred. Stage 4-1's inline puts "Next Session" at the end. Fix: reordered template to match Stage 4-1's inline (Decisions → Discoveries → Deferred → Next Session).

3. **L1 — Template had `## Session History` section not created by Stage 4-1.** Stage 4-1's initialization inline didn't include it and Stage 4-2/4-3 don't reference it in their checkpoint instructions — making it a dead section that would never appear in the actual document. Fix: removed from template.

4. **L2 — Stage 4-2 and 4-3 Input Artifacts listed `use-cases.md` without `docs/` prefix.** The previous audit (M2) fixed Stage 4-1 to use `docs/use-cases.md` but missed Stage 4-2 and 4-3. Fix: updated both to `docs/use-cases.md`.

5. **L3 — SKILL.md `(not 0, D, I, T)` used uppercase for on-demand stage identifiers.** Stage identifiers throughout SKILL.md use lowercase (`d`, `i`, `t`). Fix: corrected to `(not 0, d, i, t)`.

6. **L4 — Stage 3-2 Part 2 hardcoded "Tailwind config".** Stages 3-3 and 3-4 say "framework config" (generic). Stage 3-2 said "Tailwind config" (tech-specific). Fix: changed to "framework config".

**Files:**
- `workflow/templates/ai/implementation-decisions.md`
- `workflow/spa-rest-sql/stages/phase-4/02-implementation-loop.md`
- `workflow/spa-rest-sql/stages/phase-4/03-learning-guide.md`
- `.agent-utils/skills/start-stage/SKILL.md`
- `workflow/spa-rest-sql/stages/phase-3/02-core-app-views.md`

---

## 2026-02-28: Final stability audit — 7 fixes across Phases 1–4 and templates

**Problem:** Full audit of all 23 stage files, AGENTS.md, skills, templates, and existing artifact protocol revealed 7 issues (2 critical, 3 medium, 2 low).

**Cause/Fix (by issue):**

1. **C1 — `implementation-decisions.md` template outdated.** The template was never updated when Stage 4-1 was expanded (Audit 6) to include Architecture and Implementation Roadmap sections. Template still used P1/P2/P3 Design Priority groupings — directly contradicting Stage 4-2's rule that implementation order is dependency-driven. Fix: rewrote template to match Stage 4-1's initialization format (Architecture section, Architectural Rules, Folder Mapping, Implementation Roadmap, flat use case progress list).

2. **C2 — Stage 1-5 presented JWT vs sessions as a choice.** The workflow's Architectural Assumptions (in AGENTS.md) declare JWT as fixed, but Stage 1-5's fixed-architecture list only included 5 items (no JWT) and its Authentication section said "JWT vs sessions." Fix: added `**JWT authentication**` to the fixed list; reframed Authentication section as "mechanism is fixed, decide the library and expiration strategy."

3. **M1 — AGENTS.md Phase 4 stage detection said "→ Stage 4-2" only.** The "How to Determine Current Stage" entry for an in-progress Phase 4 pointed only to Stage 4-2, ignoring Stage 4-3 as an alternative. Fix: changed to "→ Stage 4-2 or 4-3 (user's choice per use case)."

4. **M2 — Stage 4-1 Input Artifacts missing `docs/use-cases.md`.** Part 2 Step 3 of Stage 4-1 explicitly says to read `docs/use-cases.md` to build the implementation roadmap, but it wasn't listed as an Input Artifact. Fix: added `docs/use-cases.md` to the Input Artifacts section.

5. **M3 — Stage 4-2 and 4-3 stage-complete exit criteria used Design Priority groupings.** Both stages say "All use cases are implemented by dependency order, not Design Priority" — but their stage-complete checklists used P1/P2/P3 groups. Fix: replaced all three priority rows with "All use cases from the Implementation Roadmap are implemented and tested."

6. **L1 — Stages 3-3 and 3-4 missing "Review Reference Implementation" step.** Stage 3-2 had an explicit Part 2 to read the main view before styling. Stages 3-3 and 3-4 only mentioned "already-styled views" in input lists — insufficient to ensure head setup and component patterns are followed. Fix: added Part 2 "Review Reference Implementation" to Stage 3-3 (renumbered Parts 2→3, 3→4); added equivalent Part 2 to Stage 3-4 with auth-specific note (renumbered Parts 2→3, 3→4, 4→5). Added corresponding exit criteria items to both.

7. **L2 — Stage T exit criteria missing optional log export.** Every other stage has a log export item in exit criteria. Stage T only mentioned it in the Logging section. Fix: added `- [ ] Session log optionally exported via /export-log t`.

**Files:**
- `workflow/templates/ai/implementation-decisions.md`
- `workflow/spa-rest-sql/stages/phase-1/05-tech-selection.md`
- `AGENTS.md`
- `workflow/spa-rest-sql/stages/phase-4/01-project-setup.md`
- `workflow/spa-rest-sql/stages/phase-4/02-implementation-loop.md`
- `workflow/spa-rest-sql/stages/phase-4/03-learning-guide.md`
- `workflow/spa-rest-sql/stages/phase-3/03-user-views.md`
- `workflow/spa-rest-sql/stages/phase-3/04-auth-views.md`
- `workflow/spa-rest-sql/stages/phase-0/03-knowledge-tester.md`

---

## 2026-02-28: Audit 6 fixes — Stage 2-4 false protocol trigger, AGENTS.md stale rule and missing Stage 4-1 info

**Problem:** Three issues found during full Phase 1/2 and AGENTS.md audit:
1. Stage 2-4's Output Artifacts include `docs/assets/` folder, which is created by Stage 2-1 and always pre-exists when Stage 2-4 runs for the first time. The Existing Artifact Protocol would trigger on first run, falsely asking "why are we revisiting this?" — same issue found earlier in Phase 3 stages 3-2/3-3/3-4.
2. AGENTS.md Critical Rule 3 said "ALWAYS check for existing artifacts in `docs/`" — the old vague instruction that predated the Existing Artifact Protocol. Now stale and potentially confusing.
3. AGENTS.md Stage 4-1 summary row and the Stage 4-2/4-3 note didn't reflect the new architecture and implementation roadmap additions from earlier in this session.

**Cause:**
1. Same root cause as Phase 3 issue — stage updates a shared artifact folder that pre-exists from an earlier stage.
2. Critical Rule 3 was never updated when the Existing Artifact Protocol was introduced.
3. AGENTS.md Stage 4-1 description was not updated when Stage 4-1 was expanded.

**Fix:**
- Added Stage 2-4 special case to `00-existing-artifact-protocol.md`: only `consolidation-artifacts/phase-2-consolidation.md` is the trigger indicator — `docs/assets/` pre-exists and should be ignored.
- Updated AGENTS.md Critical Rule 3 to: "ALWAYS use `/start-stage` — it automatically runs the Existing Artifact Protocol."
- Updated AGENTS.md Stage 4-1 row to include architecture and roadmap in the output description.
- Added a new note below the Phase 4 table explaining what Stage 4-1 establishes before code is written.

**Files:**
- `workflow/spa-rest-sql/stages/00-existing-artifact-protocol.md`
- `AGENTS.md`

---

## 2026-02-28: Audit 5 fixes — Protocol false trigger for 3-2/3-3/3-4, Stage 3-1 "Other" gap, architecture compliance checkpoint

**Problem:** Three issues found:
1. Stages 3-2, 3-3, and 3-4 update shared Phase 3 artifacts (`phase-3-design-decisions.md`, `styles.css`, `docs/assets/views/`) that are created by Stage 3-1. The Existing Artifact Protocol would always trigger for these stages even on their first run — asking "why are we revisiting this?" when the user just wants to run Stage 3-2 normally.
2. Stage 3-1 Part 1 listed four protocol reasons but was missing the fifth ("Other"), leaving it unhandled.
3. Stage 4-2's architecture enforcement existed only as a note in the persistence document section, not as a formal step in the implementation cycle. An AI could propose a signature that violates layer rules without checking. Stage 4-3 had no architecture check in its code review step either.

**Cause:**
1. The protocol was designed with standalone-artifact stages in mind. Sequential stages that update shared artifacts were an unanticipated case.
2. "Other" was omitted when Stage 3-1 Part 1 was written.
3. The compliance check was positioned as a passive reminder, not an active step.

**Fix:**
- Added special case to `00-existing-artifact-protocol.md` for Stages 3-2, 3-3, 3-4: skip the protocol entirely — shared artifacts pre-existing means Stage 3-1 ran, not that the current stage ran before.
- Added "Other" bullet to Stage 3-1 Part 1.
- Added explicit architecture compliance verification block to Stage 4-2 Step 1 (Plan the Slice): before presenting the plan, verify each piece respects the layer rules and revise if not.
- Added architecture compliance to Stage 4-3 Step 3 "Things to check" list (code review).

**Files:**
- `workflow/spa-rest-sql/stages/00-existing-artifact-protocol.md`
- `workflow/spa-rest-sql/stages/phase-3/01-visual-design.md`
- `workflow/spa-rest-sql/stages/phase-4/02-implementation-loop.md`
- `workflow/spa-rest-sql/stages/phase-4/03-learning-guide.md`

---

## 2026-02-28: Audit 4 fixes — Stage 3-1 Part 1 conflict with protocol, protocol missing closing instruction

**Problem:** Two issues found during audit of 2026-02-28 changes:
1. Stage 3-1 Part 1 only correctly handled the "Iteration" reason from the Existing Artifact Protocol. For "Project direction change" it contradicted the protocol by saying "restore context and respect all decisions." For "Error correction" and "Technology stack change" it had no guidance at all.
2. `00-existing-artifact-protocol.md` ended without telling the AI to continue with the stage process after completing the protocol, making the handoff implicit.

**Cause:** Stage 3-1 Part 1 was written before the full protocol was designed, so it only anticipated one re-run scenario (Iteration). The protocol file relied on SKILL.md's structure to imply continuation, which is fragile.

**Fix:**
- Rewrote Stage 3-1 Part 1 to explicitly branch on all four protocol reasons (Iteration, Error correction, Technology stack change, Project direction change), with correct behavior for each.
- Added closing line to `00-existing-artifact-protocol.md`: "After completing this protocol, continue with the stage process (Step 4 of `start-stage`)."

**Files:**
- `workflow/spa-rest-sql/stages/phase-3/01-visual-design.md`
- `workflow/spa-rest-sql/stages/00-existing-artifact-protocol.md`

---

## 2026-02-28: Stage 4-1 — Architecture selection, rules, and implementation roadmap

**Problem:** Phase 4 had no upfront architectural decision. The implementation loop (Stage 4-2/4-3) improvised structure per use case, with no agreed rules (e.g., "never call the database without going through the domain layer"). The implementation order was also deferred to the first session of Stage 4-2, which meant no one had approved it before code was written.

**Cause:** Stage 4-1 focused only on project scaffolding (skeleton + health check). Architecture and planning were omitted.

**Fix:**
- Added **Part 2: Architecture & Implementation Plan** to Stage 4-1, between stack review and skeleton creation. Covers:
  - Architecture pattern selection (Ports & Adapters, Layered, Clean Architecture) with options, trade-offs, and pattern-specific rules
  - Folder structure proposal that reflects the chosen pattern
  - Implementation roadmap: approved use-case order based on dependencies
- Updated `implementation-decisions.md` template to include Architecture (pattern + rules + folder mapping) and Implementation Roadmap sections
- Removed implementation-order step from Stage 4-2 and 4-3 Session Start (now done in 4-1)
- Added "architectural rules are binding" note to Stage 4-2 and 4-3 persistence document sections, so the AI enforces the chosen pattern during implementation

**Files:**
- `workflow/spa-rest-sql/stages/phase-4/01-project-setup.md`
- `workflow/spa-rest-sql/stages/phase-4/02-implementation-loop.md`
- `workflow/spa-rest-sql/stages/phase-4/03-learning-guide.md`

---

## 2026-02-28: Existing Artifact Protocol — handle stage re-runs and iterations

**Problem:** When a stage's output artifact already exists (e.g., re-running a stage after a project direction change or to iterate on an earlier decision), stages had no defined behavior for how to handle it. The `start-stage` skill said "check `docs/` for existing artifacts" but gave no instructions on what to do. Stage 3-1 had an ad-hoc partial handler but it didn't ask why the stage was being re-run or define different behaviors per reason.

**Cause:** The workflow was originally designed as a linear sequence (each stage runs once). Iteration and re-runs were not explicitly designed for, leaving the AI to improvise — sometimes overwriting existing work, sometimes ignoring it.

**Fix:**
- Created `workflow/spa-rest-sql/stages/00-existing-artifact-protocol.md` — a shared protocol defining the standard behavior when a stage's output artifacts already exist: read them, show a summary, ask why (iteration / project direction change / technology stack change / error correction / other), and proceed accordingly per reason.
- Updated `.agent-utils/skills/start-stage/SKILL.md` step 3 to trigger the protocol for Phase 1–4 stages (not on-demand stages 0, D, I, T) whenever output artifacts are found.
- Simplified Stage 3-1 Part 1 (previously an ad-hoc artifact check) to integrate cleanly with the new protocol instead of duplicating it.

**Files:**
- `workflow/spa-rest-sql/stages/00-existing-artifact-protocol.md` (new)
- `.agent-utils/skills/start-stage/SKILL.md`
- `workflow/spa-rest-sql/stages/phase-3/01-visual-design.md`

---

## 2026-02-28: Audit 3 fixes — Stage T header case, Stage 4-1 next stage, Stage 3-4 EXCLUDE note

**Problem:** Three issues found during a full workflow audit:
1. `03-knowledge-tester.md` header said `# Stage t:` (lowercase) — all other on-demand stages use uppercase (`# Stage D:`, `# Stage I:`); AGENTS.md table also uses `| T |`.
2. `01-project-setup.md` "Next Stage" section only mentioned Stage 4-2 (Implementation Loop), omitting Stage 4-3 (Learning Guide) as an alternative. AGENTS.md clearly states they are alternatives chosen per use case.
3. `04-auth-views.md` Part 1 was missing the "IMPORTANT: If a view is marked EXCLUDE, skip it" note that appears in the equivalent Part 1 of Stage 3-2 and Stage 3-3.

**Cause:** Item 1 was a copy-paste oversight when Stage T was authored. Item 2 was an omission when Stage 4-1 was written — the "Next Stage" pointed only to 4-2. Item 3 was an inconsistency introduced when Stage 3-4 was authored.

**Fix:**
- `03-knowledge-tester.md`: Changed `# Stage t:` → `# Stage T:`
- `01-project-setup.md`: Replaced single-stage "Next Stage" with both alternatives (4-2 and 4-3), noting they are chosen per use case and share the persistence document
- `04-auth-views.md`: Added EXCLUDE note to Part 1 to match Stage 3-2 and 3-3

**Files:**
- `workflow/spa-rest-sql/stages/phase-0/03-knowledge-tester.md`
- `workflow/spa-rest-sql/stages/phase-4/01-project-setup.md`
- `workflow/spa-rest-sql/stages/phase-3/04-auth-views.md`

---

## 2026-02-28: Audit 2 fixes — Phase 4-1 step numbering, missing `/start-stage t`, Phase 4 count, Phase 3 `## Next` header

**Problem:** Four issues found during a full workflow audit:
1. `01-project-setup.md` Part 2 step numbering jumped from 3 to 5 (no step 4), then 6 — copy-paste error.
2. `AGENTS.md` Quick Commands section listed `/start-stage 0`, `d`, `i` but omitted `/start-stage t` (Knowledge Tester), which was added in a prior session.
3. `AGENTS.md` Phase 4 overview description said "(2 stages, one loops)" — there are 3 stages (4-1, 4-2, 4-3).
4. Phase 3 stage files (3-1, 3-2, 3-3, 3-4) used `## Next` as the section header; all Phase 1 and 2 stages use `## Next Stage`.

**Cause:** Items 1, 2, 3 were editing/copy-paste oversights. Item 4 was inconsistency introduced when Phase 3 stages were authored.

**Fix:**
- `01-project-setup.md`: Renumbered Part 2 steps: 5→4, 6→5
- `AGENTS.md`: Added `/start-stage t` to Quick Commands; fixed Phase 4 count to "(3 stages: setup + alternating implementation loop)"
- Phase 3 stage files: Changed `## Next` → `## Next Stage` in 3-1, 3-2, 3-3, 3-4

**Files:**
- `workflow/spa-rest-sql/stages/phase-4/01-project-setup.md`
- `AGENTS.md`
- `workflow/spa-rest-sql/stages/phase-3/01-visual-design.md`
- `workflow/spa-rest-sql/stages/phase-3/02-core-app-views.md`
- `workflow/spa-rest-sql/stages/phase-3/03-user-views.md`
- `workflow/spa-rest-sql/stages/phase-3/04-auth-views.md`

---

## 2026-02-28: Audit fixes — Knowledge Tester registration and Arguments docs

**Problem:** Three issues found during a Stage 0 audit of the v1.1 changes:
1. `03-knowledge-tester.md` used `/export-log 0` in its Logging section, which would produce a `stage-00-meta-workflow-*.txt` filename instead of the correct `stage-0t-knowledge-tester-*.txt`.
2. `AGENTS.md` On-Demand Stages table and description omitted Stage T (Knowledge Tester).
3. Both `start-stage/SKILL.md` and `export-log/SKILL.md` Arguments sections listed `0` and `d` but not `i` and `t`.

**Cause:** Items 2 and 3 were oversights during the v1.1 session that created Stage T. Item 1 was a copy-paste error from the Stage 0 template.

**Fix:**
- `03-knowledge-tester.md`: Changed `/export-log 0` → `/export-log t`; removed the now-incorrect parenthetical note
- `AGENTS.md`: Added Stage T row to On-Demand Stages table; added Stage T bullet to the description
- `start-stage/SKILL.md`: Added `i` and `t` to the Arguments identifier list
- `export-log/SKILL.md`: Added `i` and `t` to the Arguments identifier list

**Files:**
- `workflow/spa-rest-sql/stages/phase-0/03-knowledge-tester.md`
- `AGENTS.md`
- `.agent-utils/skills/start-stage/SKILL.md`
- `.agent-utils/skills/export-log/SKILL.md`

---

## 2026-02-27: SPA+JWT specialization — rename web-rest-sql to spa-rest-sql

**Problem:** The workflow supported multiple frontend approaches (SPA, server-rendered, hybrid/HTMX) with conditional branches throughout every phase-4 stage. In practice, every project run used SPA+JWT. The server-rendered paths added noise, conditional complexity, and confusion.

**Fix:** Specialized the workflow exclusively to SPA (single-page application) + stateless JWT authentication. Renamed the workflow directory, removed all server-rendered/template-engine content, and prescribed JWT (Bearer token) as the only auth pattern.

**Changes:**
1. Renamed `workflow/web-rest-sql/` → `workflow/spa-rest-sql/`
2. Phase 1, Stage 5 (`05-tech-selection.md`): removed "Server-rendered templates" and "Hybrid (HTMX)" frontend options; removed entire "Template Engine" selection section; SPA is now the required frontend approach
3. Phase 1, Stage 6 (`06-consolidation.md`): removed "Template Engine" row from stack summary table
4. Phase 2, Stage 3 (`03-endpoint-design.md`): removed server-rendered auth pattern (form POST → 302 redirect + session cookie); kept only SPA pattern (JSON + Bearer token)
5. Phase 3, Stage 5 (`05-consolidation.md`): removed "views become server-side templates in Phase 4" note; views are now design references for SPA component development
6. Phase 4, Stage 1 (`01-project-setup.md`): removed `templates/` and `static/` from project structure; removed "Template Setup" section entirely; removed 4 server-rendered exit criteria checkboxes; removed "Pre-converted Templates" section from `implementation-decisions.md` template
7. Phase 4, Stage 2 (`02-implementation-loop.md`): removed template step from Plan the Slice; removed server-rendered route signature variant; removed "Step 4: Update Template" section; renumbered remaining steps; removed 2 template exit criteria checkboxes
8. Phase 4, Stage 3 (`03-learning-guide.md`): same template removals as Stage 4-2
9. `AGENTS.md`: renamed workflow references; updated Architectural Assumptions to include SPA and JWT explicitly; updated Phase 3→4 handoff note; added Stage 4-3 to Phase 4 table
10. `README.md`: renamed to "SPA REST SQL Workflow"; updated "This Workflow" section with SPA/JWT scope note
11. `.agent-utils/skills/start-stage/SKILL.md`: updated all path references

**Files:** `workflow/spa-rest-sql/stages/` (all phase-4 files, phase-1/05, phase-1/06, phase-2/03, phase-3/05, phase-0/00, phase-0/02), `AGENTS.md`, `README.md`, `.agent-utils/skills/start-stage/SKILL.md`

---

## 2026-02-27: Test involvement, test skills, and git-commit skill

**Problem 1:** In Stage 4-2, the AI wrote tests and the user just ran them — no engagement with what the tests should cover or why.
**Fix:** Added Step 5 "Design Tests" before the writing step. AI proposes Scenario / Input / Expected Output for each unit and integration test. User must approve the design before code is written. Renumbered old steps 5→6 (Write Tests), 6→7 (Verify), 7→8 (Checkpoint). Added exit criterion: "Test scenarios approved by user before writing."
**Files:** `workflow/web-rest-sql/stages/phase-4/02-implementation-loop.md`

---

**Problem 2:** Stage 4-3 (Learning Guide) had the same passive test approach as 4-2 — just prompting the user to write tests without guiding the design process.
**Fix:** Replaced the test section with a guided design loop: AI asks what scenarios to cover, corrects omissions with questions (not answers), user articulates input/expected output, then writes the test. AI reviews. Added exit criterion: "Test scenarios designed together."
**Files:** `workflow/web-rest-sql/stages/phase-4/03-learning-guide.md`

---

**Problem 3:** No skill to run tests — users had to manually type test commands or remember the framework-specific syntax.
**Fix:** Created two test skills:
- `/run-all-tests`: reads `tech-stack.md`, determines the correct command for the framework, runs the full suite in `prototype-code/`, reports pass/fail.
- `/run-stage-tests`: reads `implementation-decisions.md` to identify the current use case, runs only the tests for that use case using framework-appropriate filtering. Falls back to asking if context is unclear.
**Files:** `.agent-utils/skills/run-all-tests/SKILL.md` (new), `.agent-utils/skills/run-stage-tests/SKILL.md` (new), `.claude/skills/run-all-tests/SKILL.md` (new), `.claude/skills/run-stage-tests/SKILL.md` (new)

---

**Problem 4:** No skill for git — users had to write all git commands manually, with no stage-aware commit messages.
**Fix:** Created `/git-commit` skill. Walks through the full commit workflow one command at a time: `git status` → `git add [files]` → `git diff --staged --stat` → `git commit` → optional `git push`. For each command: shows the command, gives a plain-English explanation, asks "Run this? [yes / no / explain more]". Never runs a command without approval. Commit messages are stage-aware (feat/chore/design/docs/workflow prefix based on current stage and use case).
**Files:** `.agent-utils/skills/git-commit/SKILL.md` (new), `.claude/skills/git-commit/SKILL.md` (new)

---

**Also:** Updated `.agent-utils/skills/export-log/SKILL.md` with new stage names: `t → 0t-knowledge-tester`, `4-3 → 4-3-learning-guide`.

---

## 2026-02-27: Three workflow improvements

**Problem 1:** The EDGE CASES & EXCEPTIONS section in Stage 1-2 was consistently unanswerable during discovery — too early in the process to know what could go wrong. Users couldn't fill it out on any of the four systems the workflow has been used on.
**Cause:** Edge cases require a full picture of the system (data model, UI flows, business rules) that only exists at the end of Phase 3.
**Fix:** Removed the EDGE CASES & EXCEPTIONS prompt section from Stage 1-2. Added an "Edge Cases Review" as Step 0 in Stage 3-5 consolidation — before the style guide work, after all views are complete. Added a corresponding exit criterion.
**Files:** `workflow/web-rest-sql/stages/phase-1/02-knowledge-audit.md`, `workflow/web-rest-sql/stages/phase-3/05-consolidation.md`

---

**Problem 2:** No way to prepare for client or boss meetings by testing your own knowledge of the system you built.
**Cause:** The workflow had no "pre-meeting" on-demand stage.
**Fix:** Created Stage t (Knowledge Tester) — an on-demand phase-0 stage. The Interview Coach persona reads all available artifacts (including `prototype-code/`) and quizzes the user with targeted questions about project decisions, business rules, data model, API design, UI decisions, and code structure. Ends with a readiness assessment and gap list.
**Files:** `workflow/web-rest-sql/stages/phase-0/03-knowledge-tester.md` (new), `.agent-utils/skills/start-stage/SKILL.md`

---

**Problem 3:** Stage 4-2 (Senior Developer) writes the code and the user reviews it — good for shipping, but not for learning. Users with weaker technical skills don't build understanding by approving code they didn't write.
**Cause:** Phase 4 had only one implementation mode.
**Fix:** Created Stage 4-3 (Learning Guide) — a parallel alternative to Stage 4-2. The Code Mentor persona guides the user to write the code themselves: asks what the code should do before they write it, corrects misunderstandings, lets the user write, then reviews. Shares the same `implementation-decisions.md` persistence document with Stage 4-2 so both can be used on the same project.
**Files:** `workflow/web-rest-sql/stages/phase-4/03-learning-guide.md` (new), `.agent-utils/skills/start-stage/SKILL.md`

---

## 2026-02-19: Added consolidation-artifacts/ and prototype-code/ folders

**Problem:** The workflow had no clear separation between committed project artifacts and working/intermediate files. All artifacts lived in `docs/`, which was gitignored in the workflow template repo. Starting a real project required no changes to the gitignore but left no clean answer for "what gets committed?" The workflow also had no specified location for the actual project code produced in Phase 4.

**Fix:**
- Added `consolidation-artifacts/` — home for the four phase-end milestone documents that get committed to git in every project: `phase-1-consolidation.md`, `phase-2-consolidation.md`, `ui-style-guide.md`, `implementation-decisions.md`. These are the canonical outputs of the four dedicated consolidation stages.
- Added `prototype-code/` — home for the working prototype code produced in Phase 4. All project code (src/, templates/, static/, tests/, etc.) lives here.
- Updated all stage files to write consolidation docs to `consolidation-artifacts/` and read them from there.
- Updated Stage 4-1 project structure example and template-copy steps to reference `prototype-code/`.
- Updated AGENTS.md: stage table outputs, phase handoffs, stage detection, project structure, artifact storage, and project status checklist.
- Updated README.md project structure.

**Files:**
- `consolidation-artifacts/` (new folder with `.gitkeep`)
- `prototype-code/` (new folder with `.gitkeep`)
- `workflow/web-rest-sql/stages/phase-1/06-consolidation.md`
- `workflow/web-rest-sql/stages/phase-2/01-entity-ui-sketching.md`
- `workflow/web-rest-sql/stages/phase-2/02-data-modeling.md`
- `workflow/web-rest-sql/stages/phase-2/03-endpoint-design.md`
- `workflow/web-rest-sql/stages/phase-2/04-consolidation.md`
- `workflow/web-rest-sql/stages/phase-3/01-visual-design.md`
- `workflow/web-rest-sql/stages/phase-3/05-consolidation.md`
- `workflow/web-rest-sql/stages/phase-4/01-project-setup.md`
- `workflow/web-rest-sql/stages/phase-4/02-implementation-loop.md`
- `AGENTS.md`
- `README.md`

---

## 2026-02-19: Published to GitHub + README + .gitignore

**Problem:** The workflow had no README explaining its philosophy, no .gitignore, and was not version controlled — making it impossible to share, back up, or reuse across projects.

**Fix:**
- `README.md` — Written from scratch. Covers: what this is (a process, not a tool), the 7 core philosophies (collaborative style, personas, artifacts as context bridges, Phase 0, prototype mindset, logs, tool-agnostic design), the web-rest-sql specialization, prerequisites, quick start, project structure, slash commands, and a section on building new workflow specializations.
- `.gitignore` — Ignores project-generated artifacts (`docs/*.md` except `workflow-changelog.md`, session logs, `imported-artifacts/` content, Python bytecode, `settings.local.json`). Preserves folder structure via `.gitkeep` files.
- Git initialized, initial commit made (54 files), pushed to GitHub.
**Files:** `README.md` (new), `.gitignore` (new), `PREREQUISITES.md` (Git moved from Planned to Required)

---

## 2026-02-19: Twelfth audit — Quick Commands slash command list completed

**Problem:** AGENTS.md Quick Commands listed `/start-stage i` but omitted `/start-stage d` and `/start-stage 0`. All three on-demand commands were documented in the On-Demand Stages section, but the Quick Commands list was inconsistent — someone scanning it for "how do I start the diagram assistant?" wouldn't find `/start-stage d` there.

**Fix:** Added `/start-stage 0` and `/start-stage d` to the Slash Commands list in Quick Commands.

**Files:** `AGENTS.md`

---

## 2026-02-19: Eleventh audit — 3 stale Design Priority labels fixed

**Problem:** The Design Priority rename (10th audit) was not applied everywhere. Three locations kept the old "P1/P2/P3" or "build first/second/last" language:
1. Stage 1-4 exit criteria: `Priorities are assigned (P1/P2/P3)` and `Implementation order is suggested`
2. Stage 1-6 Step 2 synthesis guide: "Core business use cases (build first) / Supporting (build second) / Administrative (build last)"
3. Stage 4-2 stage-complete exit criteria: `All P1/P2/P3 use cases implemented and tested`

**Fix:**
- Stage 1-4: `Priorities are assigned (P1/P2/P3)` → `Design Priority is assigned (1/2/3)`; `Implementation order is suggested` → `Design order is suggested`
- Stage 1-6: "build first/second/last" → "Design Priority 1/2/3" in Step 2 synthesis guidance
- Stage 4-2: `All P1/P2/P3 use cases` → `All Design Priority 1/2/3 use cases`

**Files:** `workflow/web-rest-sql/stages/phase-1/04-use-case-discovery.md`, `workflow/web-rest-sql/stages/phase-1/06-consolidation.md`, `workflow/web-rest-sql/stages/phase-4/02-implementation-loop.md`, `AGENTS.md` (Stage 4-2 table description: "priority order" → "dependency order")

---

## 2026-02-19: Added Stage I — Artifact Importer

**Problem:** No way to bring existing artifacts (from previous workflow iterations or external tools like Swagger specs, SQL schemas, project docs) into the workflow without starting from scratch.

**Fix:** Added Stage I (on-demand, like Stage 0 and Stage D). The Artifact Importer persona reads a file from `imported-artifacts/`, detects which stage it maps to by reading AGENTS.md and the relevant stage file, reformats it to the workflow's output standard, fills gaps with `[PLACEHOLDER]` markers, adds an IMPORTANT NOTE at the top identifying the target stage, and saves the result as `[artifact-name]-imported.md` in `imported-artifacts/`. The imported file is context for the stage session — the stage still runs its full collaborative process and produces the canonical artifact in `docs/`.

**Files:**
- `workflow/web-rest-sql/stages/phase-0/02-import-artifact.md` (new)
- `imported-artifacts/` folder (new)
- `.agent-utils/skills/start-stage/SKILL.md` (added `i` identifier and stage mapping)
- `.agent-utils/skills/export-log/SKILL.md` (added `i → 0i-import-artifact`)
- `AGENTS.md` (added Stage I to on-demand table, quick commands, project structure)

---

## 2026-02-19: Design Priority labels + dependency-driven implementation order

**Problem:** The P1/P2/P3 priority labels were defined in Phase 1 as design-phase exploration priorities, but Stage 4-2 told the AI to follow them as implementation sequence. Auth use cases are Design Priority 3 (standard, well-known patterns — not worth design exploration), but they are often prerequisites for core features and must be implemented early in Phase 4. Blindly following P3-last would produce a system where P1 features can't be tested until the very end.

**Cause:** The labels were introduced in Stage 1-4 with "Build First/Second/Last" language that conflated design priority with implementation order. Stage 4-2 inherited this framing.

**Fix:**
- Stage 1-4 Step 5: Renamed labels to "Design Priority 1/2/3" with clarified definitions (design exploration depth, not implementation order). Removed "Must have / Should have / Nice to have" definitions that misrepresented Design Priority 3 (auth is required, not optional).
- Stage 1-4 Step 7: Renamed from "Determine Implementation Order" to "Suggest Design Order". Added a note that Phase 4 uses dependency-driven ordering, not this sequence.
- Stage 1-4 artifact description: Updated "Priority marked (P1/P2/P3)" to "Design Priority marked (1/2/3)".
- Stage 1-6 template: Renamed section headers from "P1 - Build First / P2 - Build Second / P3 - Build Last" to "Design Priority 1 / 2 / 3".
- Stage 4-2 Session Start: Added step 3 — first session proposes dependency-driven implementation order for user approval before starting.
- Stage 4-2 "Use Case Priority" section: Replaced P1→P2→P3 sequence instruction with explanation that Design Priority labels are design-phase context only; Phase 4 order is dependency-driven and agreed with user upfront.
- AGENTS.md: Updated Phase 4 checklist from "P1/P2/P3 use cases" to "Design Priority 1/2/3 use cases".

**Files:** `workflow/web-rest-sql/stages/phase-1/04-use-case-discovery.md`, `workflow/web-rest-sql/stages/phase-1/06-consolidation.md`, `workflow/web-rest-sql/stages/phase-4/02-implementation-loop.md`, `AGENTS.md`

---

## 2026-02-18: Tenth audit — 2 fixes (skipped 2 nitpicks)

**Problem 1:** Stage 4-2 Step 1 "Plan the Slice" example listed "Template" and a server-rendered route description without any SPA conditional. Steps 2 and 4 already had explicit SPA conditionals; Step 1 didn't. An AI on an SPA project would include the template step in the plan, then be corrected when reaching Step 4.
**Fix:** Added SPA conditional to the Route and Template items in the Step 1 example.
**Files:** `workflow/web-rest-sql/stages/phase-4/02-implementation-loop.md`

---

**Problem 2:** The Phase 3 stage detection guidance note explained how to detect between Stages 3-2, 3-3, and 3-4 (by view category), but said nothing about the "Stage 3-1 incomplete" case. If `phase-3-design-decisions.md` exists but the main view is still plain HTML, the note would incorrectly suggest Stage 3-2 (core app views plain HTML) when Stage 3-1 hasn't finished.
**Fix:** Added "First check the Main View entry — if still plain HTML, Stage 3-1 is incomplete" before the category-based logic.
**Files:** `AGENTS.md`

---

---

## 2026-02-18: Ninth audit — Phase 2 artifact naming + 2 SPA qualifier gaps

**Problem 1:** Stages 2-1, 2-2, 2-3, and 2-4 exit criteria all had generic "Output artifacts are generated" without naming the specific file(s). The 8th audit applied the same fix to Phase 1 stages 1-2 through 1-5, but Phase 2 stages were not updated. Stages 2-1 and 2-4 produce multiple artifacts, 2-2 produces four, 2-3 produces one — all unnamed.
**Fix:** Named specific artifacts in each exit criterion: `entity-map.md`, `assets/views/` folder, `view-entity-mapping.md` (2-1); `data-model-conceptual.md`, `assets/diagrams/entity-diagram.md`, `data-model-physical.md`, `assets/schema.sql` (2-2); `api-design.md` (2-3); `phase-2-consolidation.md`, `assets/` folder (2-4).
**Files:** `workflow/web-rest-sql/stages/phase-2/01-entity-ui-sketching.md`, `workflow/web-rest-sql/stages/phase-2/02-data-modeling.md`, `workflow/web-rest-sql/stages/phase-2/03-endpoint-design.md`, `workflow/web-rest-sql/stages/phase-2/04-consolidation.md`

---

**Problem 2:** Stage 4-2 exit criterion `- [ ] View renders correctly in browser (if applicable)` was missing an SPA qualifier. The adjacent criterion (`Template updated with real data`) was fixed in the 8th audit to say `(server-rendered / hybrid only; skip for SPA)`, but this sibling criterion was left with the ambiguous `(if applicable)` — which doesn't exclude SPA projects where the backend never renders views.
**Fix:** Changed to `(server-rendered / hybrid only; if use case has a view)`.
**Files:** `workflow/web-rest-sql/stages/phase-4/02-implementation-loop.md`

---

**Problem 3:** Stage 4-1 proposed project structure included `templates/` and `static/` with server-rendered annotations but no SPA conditional. Step 3 (Template Setup) already has a proper `"If SPA: skip this step"` conditional, but Step 2 (Propose Project Structure) didn't. An AI on an SPA project would propose these folders unnecessarily, then be told to skip creating them.
**Fix:** Added `(server-rendered / hybrid only)` to both folder comments in the example structure.
**Files:** `workflow/web-rest-sql/stages/phase-4/01-project-setup.md`

---

## 2026-02-18: Eighth audit — SPA exit criteria + Phase Transition completeness + artifact naming

**Problem 1:** Stage 4-1 exit criteria had 4 template-related items with no SPA qualifier: "Template engine is configured", "Phase 3 views are copied to the `templates/` folder", "Static assets (CSS) are copied to the `static/` folder", and "At least one view renders real data from the database via the server". The process step (Part 2, Step 3 "Template Setup") correctly conditionals with "If SPA: skip this step" (7th audit fix), but the exit criteria didn't mirror this — an AI on an SPA project would check boxes that don't apply.
**Fix:** Added `(server-rendered / hybrid only)` qualifier to all 4 template-related exit criteria items.
**Files:** `workflow/web-rest-sql/stages/phase-4/01-project-setup.md`

---

**Problem 2:** Stage 4-2 per-use-case exit criterion `- [ ] Template updated with real data (if use case renders a view)` used an ambiguous qualifier. "If use case renders a view" doesn't exclude SPA projects — SPAs also render views client-side. Step 4 says "SPA frontends: Skip this step entirely" but the exit criterion didn't mirror this.
**Fix:** Changed qualifier to `(server-rendered / hybrid only; skip for SPA)`.
**Files:** `workflow/web-rest-sql/stages/phase-4/02-implementation-loop.md`

---

**Problem 3:** AGENTS.md Phase 2→3 handoff description said "Stage 2-4 produces `phase-2-consolidation.md` and `assets/` folder". `view-entity-mapping.md` lives in `docs/` (not `docs/assets/`) so it wasn't covered. The 6th audit added it to Stage 2-4's Phase Transition input list but didn't update this AGENTS.md description. Stages 3-1, 3-2, and 3-3 all require it as an explicit input.
**Fix:** Added `view-entity-mapping.md` to the Phase 2→3 handoff description.
**Files:** `AGENTS.md`

---

**Problem 4:** Stage 3-5 Phase Transition listed "All previous consolidation documents" (vague) and was missing `adrs/` and `data-model-physical.md` as Phase 4 inputs. Both are explicitly listed as Stage 4-1 input artifacts. "All previous consolidation documents" was also imprecise — Stage 4-1 needs `phase-1-consolidation.md` specifically, not `phase-2-consolidation.md`.
**Fix:** Replaced "All previous consolidation documents" with `phase-1-consolidation.md`. Added `adrs/` and `data-model-physical.md`. Reordered the list to match Stage 4-1's input artifact order.
**Files:** `workflow/web-rest-sql/stages/phase-3/05-consolidation.md`

---

**Problem 5:** Stages 1-2, 1-3, 1-4, and 1-5 exit criteria all had generic "Output artifact is generated" without naming the specific file. Stages 1-1 and 1-6 correctly name their artifacts (e.g., "`project-brief.md` is generated"). The middle stages were inconsistent.
**Fix:** Named specific artifacts in each exit criterion: `knowledge-audit.md` (1-2), `research-findings.md` (1-3), `use-cases.md` (1-4), `` `tech-stack.md` and `adrs/` `` (1-5).
**Files:** `workflow/web-rest-sql/stages/phase-1/02-knowledge-audit.md`, `workflow/web-rest-sql/stages/phase-1/03-research.md`, `workflow/web-rest-sql/stages/phase-1/04-use-case-discovery.md`, `workflow/web-rest-sql/stages/phase-1/05-tech-selection.md`

---

## 2026-02-18: Seventh audit — SPA/server-rendered split in Phase 4 + 4 smaller fixes

**Problem 1:** Stage 4-2 Step 2 "Approve Signatures" showed a route example that assumed SPA/JSON patterns: `auth token` as auth input and `200 → OrderDetailsResponse as JSON` as output. For server-rendered apps (the primary workflow target), view-rendering routes return HTML via the template engine and authenticate via session cookie, not Bearer token.
**Fix:** Replaced the single route signature block with a conditional (matching Stage 2-3's auth section pattern): server-rendered/hybrid shows session auth + HTML output; SPA shows Bearer token + JSON output.
**Files:** `workflow/web-rest-sql/stages/phase-4/02-implementation-loop.md`

---

**Problem 2:** Stage 4-1 Template Setup and Stage 4-2 Step 4 "Update Template" assumed server-rendered with no conditional. If the user chose SPA in Stage 1-5, these steps are wrong: Phase 4 would implement a pure REST JSON API, and Phase 3 views would serve as design references for SPA components — not server-side templates.
**Fix:** Added SPA conditional to Stage 4-1 Template Setup ("If SPA: skip this step…") and to Stage 4-2 Step 4 ("SPA frontends: skip this step entirely. Routes return JSON; the SPA handles rendering.").
**Files:** `workflow/web-rest-sql/stages/phase-4/01-project-setup.md`, `workflow/web-rest-sql/stages/phase-4/02-implementation-loop.md`

---

**Problem 3:** Stage 4-1 Input Artifacts didn't list `docs/assets/css/styles.css`, even though Part 2 Step 3 (Template Setup) explicitly copies it to `static/css/`. The file was referenced in the process but not declared as an input (the fifth audit added it to Stage 3-5's Phase Transition output, but never to Stage 4-1's input list).
**Fix:** Added `docs/assets/css/styles.css (base stylesheet — copied to static/css/ in this stage)` to Stage 4-1's Input Artifacts.
**Files:** `workflow/web-rest-sql/stages/phase-4/01-project-setup.md`

---

**Problem 4:** AGENTS.md Phase 3→4 handoff said "Stage 3-5 produces `ui-style-guide.md` and finalized `phase-3-design-decisions.md`". This framing implied `phase-3-design-decisions.md` is a Stage 3-5 output artifact and might be forwarded to Phase 4 — when in fact it's the Phase 3 working document, explicitly not forwarded (its content is captured in `ui-style-guide.md`'s Decision Log per the fifth audit).
**Fix:** Rewrote the sentence to clarify that Stage 3-5 consolidates into `ui-style-guide.md`, whose Decision Log captures everything from `phase-3-design-decisions.md`, which is not forwarded to Phase 4.
**Files:** `AGENTS.md`

---

**Problem 5:** AGENTS.md Project Status Phase 4 checklist had "Working project skeleton ← Stage 4-1 complete" — a non-file state marker. The sixth audit replaced "Working project skeleton" as the stage detection signal with `implementation-decisions.md`, but this stale checklist entry was left behind. The detection logic and the checklist were inconsistent.
**Fix:** Removed the "Working project skeleton" line and merged with `implementation-decisions.md`: `- [ ] implementation-decisions.md initialized ← Stage 4-1 complete`.
**Files:** `AGENTS.md`

---

## 2026-02-18: Removed project-specific content from Phase 3 stage files

**Problem:** Stage 3-1 and 3-2 contained hardcoded view names from a prior project (Chilean tax/SII system: dte-detail, tiendas, sii-credentials). This would cause the AI to attempt to style views that don't exist in any new project.

**Cause:** Stage files were written during an active project session and not cleaned up before being committed as the canonical workflow template.

**Fix:**
- Stage 3-1 `## Next` section: replaced hardcoded view names with a generic description ("core app views identified in the view inventory")
- Stage 3-2 `## Views in This Stage`: replaced project-specific view list with instructions to read the view inventory from `phase-3-design-decisions.md`
- Stage 3-2 Exit Criteria: replaced specific file checks with generic "each core app view is styled or marked EXCLUDE"

**Files modified:**
- `workflow/web-rest-sql/stages/phase-3/01-visual-design.md`
- `workflow/web-rest-sql/stages/phase-3/02-core-app-views.md`

---

## 2026-02-18: Unified views folder location to `docs/assets/views/`

**Problem:** Stage 2-1 created views in `docs/views/`, but the pre-created directory structure and all Phase 3 stages expected them at `docs/assets/views/`. Stage 2-4 had a redundant "Organize Assets Folder" step to move them. This created an unnecessary intermediate location and potential confusion about where views lived.

**Cause:** Stage 2-1 was designed with a temporary `docs/views/` folder, expecting Stage 2-4 consolidation to move them. The `.gitkeep` files already pre-created `docs/assets/views/`, making the intermediate location unnecessary.

**Fix:**
- Stage 2-1: Changed all references from `docs/views/` to `docs/assets/views/` (4 locations: process step, index creation, artifact definition, next stage reference)
- Stage 2-4: Changed "Create/verify the assets folder" to "Verify the assets folder" — views are already there from Stage 2-1
- CLAUDE.md: Updated project status checklist from `views/ (plain HTML)` to `assets/views/ (plain HTML)`

**Files modified:**
- `workflow/web-rest-sql/stages/phase-2/01-entity-ui-sketching.md`
- `workflow/web-rest-sql/stages/phase-2/04-consolidation.md`
- `CLAUDE.md`

---

## 2026-02-18: Removed hardcoded `home.html` reference from Stage 3-2

**Problem:** Stage 3-2 referenced `home.html` as the main view reference implementation in three places. If the main view was named differently by the user during Stage 3-1's view inventory, the AI would look for a file that doesn't exist.

**Cause:** `home.html` was assumed as the canonical main view name instead of reading the actual decision from `phase-3-design-decisions.md`.

**Fix:** Replaced all three hardcoded `home.html` references with instructions to check `phase-3-design-decisions.md` for the actual main view filename.

**Files modified:**
- `workflow/web-rest-sql/stages/phase-3/02-core-app-views.md`

---

## 2026-02-18: Removed misleading Project Status placeholders from CLAUDE.md

**Problem:** CLAUDE.md had `**Current Phase**: [ ]` and `**Current Stage**: [ ]` placeholders that no stage file ever updated. They implied someone was tracking stage manually, which was never implemented.

**Cause:** Placeholder fields left over from an earlier design that was superseded by the artifact-based stage detection system.

**Fix:** Replaced placeholders with a note pointing to the "How to Determine Current Stage" section, which is the actual mechanism used.

**Files modified:**
- `CLAUDE.md`

---

## 2026-02-18: Added missing artifacts to CLAUDE.md checklist and stage table

**Problem:** `docs/assets/diagrams/entity-diagram.md` (produced by Stage 2-2) was absent from the Phase 2 project status checklist. The Phase 2 stage table also still showed the old `views/*.html` path instead of `assets/views/*.html`.

**Cause:** Checklist and table not updated when the entity diagram artifact was added to Stage 2-2, and when the views path was changed.

**Fix:** Added `assets/diagrams/entity-diagram.md` to the Phase 2 checklist. Updated Stage 2-1 output in the stage table to `assets/views/*.html`.

**Files modified:**
- `CLAUDE.md`

---

## 2026-02-18: Removed hardcoded sidebar assumption and project-specific content from Stage 3-2 and 3-3

**Problem:** Stages 3-2 and 3-3 hardcoded "sidebar" as the navigation pattern in multiple places, bypassing the navigation decision made in Stage 3-1. Additionally, Stage 3-3 had the same project-specific view names issue as Stage 3-2 (including "DTE emissions" in the notification description), and both stages had hardcoded view names in their `## Next` sections and process descriptions.

**Cause:** Same root cause as the Stage 3-2 view names issue — stage files were edited during a specific project session and not cleaned up.

**Fix:**
- Stage 3-2: Replaced all 5 "sidebar" references with "navigation pattern from `phase-3-design-decisions.md`". Fixed `## Next` to be generic.
- Stage 3-3: Replaced hardcoded view list and Exit Criteria with generic view inventory instructions. Replaced "sidebar" references with navigation pattern references. Removed project-specific process hints. Fixed `## Next` to be generic.

**Files modified:**
- `workflow/web-rest-sql/stages/phase-3/02-core-app-views.md`
- `workflow/web-rest-sql/stages/phase-3/03-user-views.md`

---

## 2026-02-18: Full workflow audit — 12 mismatches fixed

**Problem:** Comprehensive audit identified 12 mismatches across CLAUDE.md and stage files. Issues fell into three categories: leftover `views/` paths from a previous fix, leftover `home.html` hardcoding from previous fixes, and missing/incomplete information in stage tables and exit criteria.

**Cause:** Previous targeted fixes (views path, home.html references) were applied to specific stages but not propagated to every location that referenced the same data. CLAUDE.md stage tables and some stage files were not fully updated.

**Fix:**

*Stage 2-4 (`04-consolidation.md`) — 4 locations fixed:*
- Input Artifacts: `views/` → `assets/views/`
- Consolidation template example: `views/index.html` → `assets/views/index.html`, `views/order-list.html` → `assets/views/order-list.html`
- Validate Assets step: `views/index.html` → `docs/assets/views/index.html`
- Output Artifact description: `views/` → `assets/views/`

*CLAUDE.md — 6 locations fixed:*
- Stage table 3-1 Output: `home.html styled` → `Main view styled`; `styles.css` → `assets/css/styles.css`
- Stage table 2-2 Output: added missing `assets/diagrams/entity-diagram.md`; fixed `schema.sql` → `assets/schema.sql`
- Stage table 4-1 Output: added missing `implementation-decisions.md`
- Phase 3 stage detection: `styled home.html` → `styled main view`
- Phase 2 stage detection: added explicit entry for Stage 2-1 (`phase-1-consolidation.md` exists but no `entity-map.md`)

*Stage 3-4 (`04-auth-views.md`) — same fix as previously applied to 3-2 and 3-3:*
- "Views in This Stage": replaced hardcoded `login.html`, `register.html`, `reset-password.html` with instructions to read the view inventory from `phase-3-design-decisions.md`
- Exit Criteria: replaced specific file checks with generic "each auth view is styled or marked EXCLUDE"

*Stage 3-5 (`05-consolidation.md`):*
- Phase Transition "Input for Phase 4": added missing `docs/assets/css/styles.css`

*Stage D (`01-diagram-assistant.md`):*
- Exit Criteria: added missing `Session log exported via /export-log d`

*Stage 3-1 (`01-visual-design.md`):*
- Two occurrences of "typically home.html" replaced with "identified in the view inventory" / "determined in view inventory"

**Files modified:**
- `workflow/web-rest-sql/stages/phase-2/04-consolidation.md`
- `workflow/web-rest-sql/stages/phase-3/01-visual-design.md`
- `workflow/web-rest-sql/stages/phase-3/04-auth-views.md`
- `workflow/web-rest-sql/stages/phase-3/05-consolidation.md`
- `workflow/web-rest-sql/stages/phase-0/01-diagram-assistant.md`
- `CLAUDE.md`

---

## 2026-02-18: Fixed frontend-backend connection gap (server-rendered templates)

**Problem:** Phase 4 treated the backend in isolation. The styled HTML views from Phase 3 existed in `docs/assets/views/` but the workflow never said: move them to the project, set up a template engine, and wire them to the handlers. Additionally, Stage 1-5 had no explicit Template Engine selection category — server-rendered frontend approach was listed but the specific engine was not captured in the tech stack.

**Cause:** Workflow was designed with the backend implementation cycle in mind and assumed the frontend connection would be figured out implicitly. The "separated frontend and backend" constraint was treated as an implementation detail rather than something the workflow needed to orchestrate.

**Fix:**

*Stage 1-5 (`05-tech-selection.md`):*
- Added "Template Engine" as an explicit tech selection category (conditional on server-rendered or hybrid approach)
- Added examples per language (Java: Thymeleaf/Qute/FreeMarker, Rust: Tera/Askama/MiniJinja, etc.)
- Added Template Engine row to the `tech-stack.md` summary table template

*Stage 4-1 (`01-project-setup.md`):*
- Added `ui-style-guide.md` and `docs/assets/views/` to Input Artifacts
- Added `templates/` and `static/` folders to the project structure example
- Added new Step 3 "Template Setup": configure engine, copy Phase 3 views to `templates/`, copy CSS to `static/`, convert main view to real template variables as proof of concept
- Renumbered old steps 3→4, 4→5, 5→6
- Added 3 new exit criteria: template engine configured, views copied, at least one view renders real data

*Stage 4-2 (`02-implementation-loop.md`):*
- Updated Step 1 "Plan the Slice" example to include template as a piece of the slice
- Added new Step 4 "Update Template": replace mock data with template variables for each use case's view
- Renumbered old steps 4→5 (Write Tests), 5→6 (Verify), 6→7 (Checkpoint)
- Added 2 new per-use-case exit criteria: template updated, view renders in browser

*Stage 3-5 (`05-consolidation.md`):*
- Added note to Phase Transition clarifying that Phase 3 views become server-side templates in Phase 4

*CLAUDE.md:*
- Updated Phase 3→4 handoff description to explain the template conversion

**Files modified:**
- `workflow/web-rest-sql/stages/phase-1/05-tech-selection.md`
- `workflow/web-rest-sql/stages/phase-3/05-consolidation.md`
- `workflow/web-rest-sql/stages/phase-4/01-project-setup.md`
- `workflow/web-rest-sql/stages/phase-4/02-implementation-loop.md`
- `CLAUDE.md`

---

## 2026-02-18: Four fixes from second workflow audit

**Problem 1:** CLAUDE.md Stage 2-1 output table was missing `view-entity-mapping.md`, which is a documented output artifact of Stage 2-1 and appears in the project status checklist.
**Fix:** Added `view-entity-mapping.md` to the Stage 2-1 output column in the phase table.
**Files:** `CLAUDE.md`

---

**Problem 2:** Stage 2-2 Mermaid relationship syntax guide documented only 3 variants (`||--||`, `||--o{`, `}o--o{`) but the example above it used 4 variants including `||--|{` and `}o--||`. The guide didn't explain the difference between optional (`o{`) and required (`|{`) many-sides, which could cause the AI to produce imprecise ER diagrams.
**Fix:** Rewrote the syntax guide to explain the four endpoint markers independently (`||`, `o|`, `|{`, `o{`), then listed 5 common combinations with examples.
**Files:** `workflow/web-rest-sql/stages/phase-2/02-data-modeling.md`

---

**Problem 3:** SQLite disables foreign key enforcement by default (`PRAGMA foreign_keys = OFF`). Stage 2-2's "Validate Mock Data" step instructed the AI to verify "foreign key relationships work" without mentioning this, meaning FK validation could silently pass even with broken references. Stage 4-1 had the same omission — application code must set this pragma on every connection.
**Fix:** Added PRAGMA warning + validation command to Stage 2-2's validate step. Added PRAGMA requirement to Stage 4-1's database setup step. Also noted that `schema.sql` should include a comment reminding application code of this.
**Files:** `workflow/web-rest-sql/stages/phase-2/02-data-modeling.md`, `workflow/web-rest-sql/stages/phase-4/01-project-setup.md`

---

**Problem 4:** Stage 4-2's "Session End" section said "Export the log" without specifying the command. Every other stage specifies `/export-log X-Y` inline. The command was in the exit criteria but not where the AI encounters it during the session flow.
**Fix:** Changed "Export the log" to "Export the log via `/export-log 4-2`".
**Files:** `workflow/web-rest-sql/stages/phase-4/02-implementation-loop.md`

---

## 2026-02-18: Generic script architecture + .agent-utils/ for multi-tool support

**Problem:** The workflow was Claude Code-specific. All scripts, skills, and conventions lived in `.claude/`. To support other LLM CLI tools (Gemini CLI, Codex, future tools), the workflow needed a tool-agnostic layer. `AGENTS.md` is now the Linux Foundation / Agentic AI Foundation standard (December 2025) adopted by Claude Code, Gemini CLI, GitHub Copilot, Cursor, and others — making it the right canonical file.

**Cause:** The workflow was designed before multi-tool conventions were established. Skills and scripts were written Claude-first with no abstraction layer.

**Fix:**

*Generic script template pattern:*
- Created `workflow/scripts/convert_transcript_generic.py` — abstract base class defining the output contract (header, format_output, convert, main). Tool-specific subclasses implement `tool_name()` and `parse_transcript()`.
- Created `workflow/scripts/convert_transcript_claude.py` — Claude implementation extending the generic base. Parses Claude Code's JSONL schema (`type`, `message.content` fields with `text` and `tool_use` blocks).
- Deleted `workflow/scripts/convert-transcript.sh` — superseded by the new Claude-specific script.
- Updated `workflow/scripts/auto-export.sh` to call `convert_transcript_claude.py`.

*`.agent-utils/` canonical skill layer:*
- Created `.agent-utils/skills/start-stage/SKILL.md` — canonical, tool-agnostic skill instructions.
- Created `.agent-utils/skills/export-log/SKILL.md` — canonical naming convention and stage names (no tool-specific paths or scripts).
- Updated `.claude/skills/start-stage/SKILL.md` — thin wrapper: delegates to `.agent-utils` canonical content.
- Updated `.claude/skills/export-log/SKILL.md` — thin wrapper: delegates to `.agent-utils` for naming, adds Claude-specific transcript path and converter script.

*Adding a new tool in the future:*
1. Create `workflow/scripts/convert_transcript_<tool>.py` extending `TranscriptConverter`
2. Create `.<tool>/skills/export-log/SKILL.md` with tool-specific transcript path + converter call
3. Create `.<tool>/skills/start-stage/SKILL.md` delegating to `.agent-utils`

**Files modified:**
- `workflow/scripts/convert_transcript_generic.py` (new)
- `workflow/scripts/convert_transcript_claude.py` (new)
- `workflow/scripts/convert-transcript.sh` (deleted)
- `workflow/scripts/auto-export.sh`
- `.agent-utils/skills/start-stage/SKILL.md` (new)
- `.agent-utils/skills/export-log/SKILL.md` (new)
- `.claude/skills/start-stage/SKILL.md`
- `.claude/skills/export-log/SKILL.md`

---

## 2026-02-18: Three fixes from fourth workflow audit

**Problem 1:** Stage 3-1's `phase-3-design-decisions.md` template had no dedicated field for the main view filename. Stages 3-2, 3-3, and 3-4 all instruct the AI to "check `phase-3-design-decisions.md` for the actual main view filename", but the template only had generic `[View name]: [INCLUDE/EXCLUDE]` entries — forcing the AI to guess which one was the reference implementation.
**Fix:** Added `- **Main View (reference implementation)**: [filename]` as the first entry in the View Decisions section of the template.
**Files:** `workflow/web-rest-sql/stages/phase-3/01-visual-design.md`

---

**Problem 2:** Two related issues with the tech stack tables. (a) Stage 1-5's `tech-stack.md` Backend table labeled the row `ORM`, implying that an ORM is always required. The stage itself correctly frames this as "ORM / Database Access" (full ORM vs query builder vs raw SQL), but the table label didn't match. (b) Stage 1-6's `phase-1-consolidation.md` tech stack summary table was missing the Template Engine row — added in the previous audit to Stage 1-5 — making the consolidation incomplete for server-rendered projects.
**Fix:** (a) Renamed `| ORM |` to `| DB Access |` in Stage 1-5's summary table. (b) Added `| Template Engine | ... or N/A if SPA | ... |` to Stage 1-6's summary table. ORM/DB Access was intentionally not added to the consolidation — Phase 2 and 3 don't need it, and Phase 4 reads `tech-stack.md` directly.
**Files:** `workflow/web-rest-sql/stages/phase-1/05-tech-selection.md`, `workflow/web-rest-sql/stages/phase-1/06-consolidation.md`

---

**Problem 3:** Stage 1-5 exit criteria had no check for Template Engine selection, even though it was added as an explicit selection category (with its own process step and table row) in a previous audit.
**Fix:** Added `- [ ] Template engine selected (or confirmed N/A if SPA approach)` after the Frontend approach check.
**Files:** `workflow/web-rest-sql/stages/phase-1/05-tech-selection.md`

---

## 2026-02-18: Fifth audit — phase-3-design-decisions.md role clarified + Stage 4 template coordination fix

**Problem 1:** Stage 3-5 exit criteria had no check to verify `phase-3-design-decisions.md` decisions were preserved before Phase 4. The check was needed on the output artifact (`ui-style-guide.md`), not on the working document.
**Fix:** Added `- [ ] ui-style-guide.md Decision Log captures all key decisions from phase-3-design-decisions.md (no information loss)` to Stage 3-5 exit criteria.
**Files:** `workflow/web-rest-sql/stages/phase-3/05-consolidation.md`

---

**Problem 2:** Stage 3-5's `ui-style-guide.md` template described the Decision Log as a `[Summary of key decisions]`. A summary implies information loss. `phase-3-design-decisions.md` is a Phase 3 working document — it is not carried forward to Phase 4. If the style guide only summarizes, decisions are lost.
**Fix:** Changed the Decision Log description to require a complete record: all decisions, rationale, alternatives considered, and revisions. Made explicit that nothing important should remain only in the decisions file.
**Files:** `workflow/web-rest-sql/stages/phase-3/05-consolidation.md`

---

**Problem 3:** Stage 3-5 Phase Transition listed `phase-3-design-decisions.md` as a Phase 4 input, but Stage 4-1 didn't list it as an input artifact. The decisions file is a Phase 3 working document — `ui-style-guide.md` (once its Decision Log is comprehensive) is the sole authoritative source for Phase 4.
**Fix:** Removed `phase-3-design-decisions.md` from Stage 3-5's Phase Transition input list.
**Files:** `workflow/web-rest-sql/stages/phase-3/05-consolidation.md`

---

**Problem 4:** Stage 4-1 converts the main view from static mock data to real template variables as a proof of concept, but this was not recorded in `implementation-decisions.md`. When Stage 4-2 processes the use case corresponding to the main view, it would try to convert a template that was already converted — with no way to know this from the persistence document.
**Fix:** Added a "Pre-converted Templates (Stage 4-1)" section to the `implementation-decisions.md` template in Stage 4-1, so Stage 4-2 can check before attempting conversion.
**Files:** `workflow/web-rest-sql/stages/phase-4/01-project-setup.md`

---

**Problem 5:** Stage 4-2 Step 4 "Update Template" had no instruction to check whether the template was already converted in Stage 4-1 before starting.
**Fix:** Added step 1: check `implementation-decisions.md` → "Pre-converted Templates" section. If already converted, verify and complete rather than convert from scratch. Renumbered old steps 1–4 to 2–5.
**Files:** `workflow/web-rest-sql/stages/phase-4/02-implementation-loop.md`

---

**Problem 6:** CLAUDE.md Phase 3 stage detection listed "Core app views styled → Stage 3-3" etc. but gave no mechanism for how to determine this. The AI had to figure out which views were styled with no guidance.
**Fix:** Added a note below the Phase 3 detection block pointing to the mechanism: read `phase-3-design-decisions.md` → View Decisions section; views marked INCLUDE with plain HTML indicate the current unfinished stage based on their category.
**Files:** `CLAUDE.md`

---

## 2026-02-18: Sixth audit — AGENTS.md canonical + 4 stage detection and contract fixes

**Problem 1:** `AGENTS.md` was a redirect to `CLAUDE.md`, when it should be the other way around. `AGENTS.md` is the Linux Foundation / Agentic AI Foundation standard (December 2025), adopted by Claude Code, Gemini CLI, GitHub Copilot, and others. The canonical workflow content should live there; tool-specific files (`CLAUDE.md`, `GEMINI.md`) should redirect to it.
**Fix:** Moved all content from `CLAUDE.md` to `AGENTS.md`. Rewrote `CLAUDE.md` and `GEMINI.md` as thin redirects. Updated the project structure tree inside `AGENTS.md` to reflect the new roles.
**Files:** `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`

---

**Problem 2:** `AGENTS.md` Phase 3 stage detection had no entry for Stage 3-1. The list started at Stage 3-2, leaving no path from "Phase 2 complete" to "start Stage 3-1". Every other phase/stage transition had an explicit artifact-based entry.
**Fix:** Added `- \`phase-2-consolidation.md\` exists but no \`phase-3-design-decisions.md\` → Stage 3-1` as the first entry in the Phase 3 detection block.
**Files:** `AGENTS.md`

---

**Problem 3:** `AGENTS.md` Phase 4 stage detection used "Working project skeleton → Stage 4-2" — not a file-based signal (can't be globbed or detected). Stage 4-1 had no entry at all. `implementation-decisions.md` is the correct artifact boundary: Stage 4-1 creates it, Stage 4-2 reads it first.
**Fix:** Replaced with: `\`ui-style-guide.md\` exists but no \`implementation-decisions.md\` → Stage 4-1` and `\`implementation-decisions.md\` exists (use cases not all complete) → Stage 4-2`.
**Files:** `AGENTS.md`

---

**Problem 4:** Stage 2-4 Phase Transition listed only `phase-2-consolidation.md` and `docs/assets/` folder as Phase 3 inputs. `view-entity-mapping.md` lives in `docs/` (not `docs/assets/`), so it was not covered — yet Stages 3-1, 3-2, and 3-3 all explicitly list it as a required input.
**Fix:** Added `view-entity-mapping.md` to the Phase Transition input list in Stage 2-4.
**Files:** `workflow/web-rest-sql/stages/phase-2/04-consolidation.md`

---

**Problem 5:** Stage 2-3 Part 5 "Authentication Mechanism" only showed a Bearer token / JSON example (SPA pattern). For server-rendered apps (the primary case — Stage 4 converts views to server-side templates), auth uses form POST → 302 redirect + session cookie. An AI designing endpoints for a server-rendered project would produce the wrong auth contract.
**Fix:** Replaced the single example with a conditional block: server-rendered pattern (form POST → redirect) vs SPA pattern (JSON → token), with a note to use the one matching the chosen frontend approach.
**Files:** `workflow/web-rest-sql/stages/phase-2/03-endpoint-design.md`

---

## 2026-02-18: Replaced jq dependency with Python 3 in workflow scripts

**Problem:** `convert-transcript.sh` and `session-start.sh` both depended on `jq` for JSON parsing. `jq` is not pre-installed on Debian or macOS, causing the export log skill to silently fail on any new machine.

**Cause:** Scripts were written assuming `jq` would be available, without documenting it as a prerequisite or providing a fallback.

**Fix:**
- `convert-transcript.sh`: Fully rewritten as a Python 3 script (same filename, same interface). Uses only the standard library (`json`, `sys`, `datetime`). No external dependencies.
- `session-start.sh`: Replaced the single `jq` call with a `python3 -c` one-liner.
- `PREREQUISITES.md`: Created to document all workflow prerequisites (Python 3, bash, sqlite3, web browser, LLM CLI).

**Files modified:**
- `workflow/scripts/convert-transcript.sh`
- `workflow/scripts/session-start.sh`
- `PREREQUISITES.md` (new file)
