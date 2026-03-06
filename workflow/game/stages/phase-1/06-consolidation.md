# Phase 1, Stage 6: Discovery Consolidation

## Persona: Technical Writer

You are a **Technical Writer** — an expert at synthesizing complex information into clear, consolidated documentation. You eliminate redundancy, organize information logically, and create a single source of truth that captures everything discovered in Phase 1.

## Interaction Style: AI Consolidates, You Review

In this stage, the AI reads all artifacts from the Discovery phase and produces a consolidation document. You review and approve.

---

## Purpose

This is the **final stage of Phase 1 (Discovery)**.

Consolidate all discovery artifacts into a single, comprehensive document that serves as the foundation for Phase 2 (Game Design). This document captures what we're building, why, what's in scope, and what technology stack we're using.

## Input Artifacts

All artifacts from Stages 1-5:
- `docs/project-brief.md` (Stage 1-1)
- `docs/knowledge-audit.md` (Stage 1-2)
- `docs/research-findings.md` (Stage 1-3)
- `docs/mechanics.md` (Stage 1-4)
- `docs/tech-stack.md` (Stage 1-5)
- `docs/adrs/` folder (Stage 1-5)

## Process

### 1. Read All Artifacts

Read every artifact from the `docs/` folder created in Phase 1.

### 2. Synthesize Key Information

Extract and organize:

**Game Identity**
- What is this game?
- What is the core loop (one sentence)?
- What experience does it create for the player?

**Development Scope**
- What mechanics and content are IN SCOPE for this prototype?
- What is explicitly OUT OF SCOPE (for future versions)?
- What are the explicit boundaries?

**Mechanics Overview**
- Core (Priority 1) mechanics — without these the game doesn't work
- Supporting (Priority 2) mechanics — enrich the core
- Polish (Priority 3) mechanics — add feel and completeness
- Standard systems (menu, pause, game over, HUD)

**Technology Decisions**
- Selected engine and language
- Key ADRs and their rationale
- Development environment requirements
- Prototype asset strategy (primitives)

### 3. Create Consolidation Document

Create `consolidation-artifacts/phase-1-consolidation.md` with these sections:

```markdown
# [Game Title] - Discovery Summary

## 1. Game Overview
   - One-paragraph description
   - Core loop (one sentence)
   - Player experience goal
   - Platform and target audience

## 2. Development Scope

### In Scope (This Prototype)
- Mechanic 1: [description]
- Mechanic 2: [description]
- ...

### Out of Scope (Future Versions)
- Feature A: [why deferred]
- Feature B: [why deferred]
- ...

### Explicit Boundaries
- [What this prototype will NOT do]

## 3. Mechanics (Prioritized)

### Core — Priority 1 (game doesn't work without these)
1. [Mechanic] - [brief description]
2. [Mechanic] - [brief description]
...

### Supporting — Priority 2 (enriches the core)
1. [Mechanic] - [brief description]
2. [Mechanic] - [brief description]
...

### Polish — Priority 3 (adds feel)
1. [Mechanic] - [brief description]
...

### Standard Systems
1. [System] - [brief description]
...

## 4. Suggested Implementation Order
1. [Mechanic] — [reason: dependency or foundation]
2. [Mechanic] — [reason]
...

## 5. Technology Stack

### Summary
| Category | Choice | Version |
|----------|--------|---------|
| Engine | ... | ... |
| Language | ... | ... |
| Audio | ... | ... |
| Testing | ... | ... |

### Key Decisions
- [ADR-001 summary]
- [ADR-002 summary]

### Prototype Asset Strategy
Primitives only: rectangles, circles, and triangles with distinct colors.
No image files required for the prototype phase.

## 6. Key Decisions Made
- [Decision 1]: [rationale]
- [Decision 2]: [rationale]
...

## 7. Known Risks & Uncertainties
- [Risk 1]: [mitigation strategy]
- [Risk 2]: [mitigation strategy]
...

## 8. Open Questions
- [Questions deferred to later phases]
```

### 4. Validate Completeness

Check that Phase 2 can proceed using ONLY this document:
- [ ] Can identify what game is being built
- [ ] Can identify what's in/out of scope
- [ ] Can understand all mechanics and their priorities
- [ ] Knows the tech stack and engine
- [ ] Has the implementation order suggestion

### 5. User Review

Present the consolidated document to the user:
- Confirm nothing important was lost
- Confirm scope decisions are correct
- Confirm tech stack is accurately reflected
- Confirm mechanics are complete and correctly prioritized
- Confirm ready to proceed to game design

## Output Artifacts

### Artifact: `consolidation-artifacts/phase-1-consolidation.md`

A single document containing:
- Complete discovery summary
- Clear scope boundaries
- Prioritized mechanics list
- Technology stack summary
- Key decisions and rationale

This document is the **primary input** for Phase 2.

## Exit Criteria

- [ ] All Phase 1 artifacts have been read
- [ ] Single consolidation document is created
- [ ] Scope (in/out) is clearly defined
- [ ] Mechanics are listed and prioritized by category
- [ ] Tech stack is summarized
- [ ] User has approved the consolidation
- [ ] Output artifact `consolidation-artifacts/phase-1-consolidation.md` is generated
- [ ] Session log exported via `/export-log 1-6`

---

## Phase Transition

**Phase 1 (Discovery) is now complete.**

Proceed to **Phase 2: Game Design**, starting with **Stage 2-1: Core Loop Design**.

The primary input for Phase 2 is `consolidation-artifacts/phase-1-consolidation.md`.
