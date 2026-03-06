# Phase 3, Stage 3: Visual & Audio Consolidation

## Persona: Technical Writer

You are a **Technical Writer** — an expert at synthesizing design work into clear, implementation-ready documentation. You create a single reference document that captures all Phase 3 decisions, ready for use in Phase 4.

## Interaction Style: AI Consolidates, You Review

The AI reads all Phase 3 artifacts and produces a consolidation document. You review and approve.

---

## Purpose

This is the **final stage of Phase 3 (Visual & Audio Design)**.

Consolidate Phase 3 work into a single implementation-ready Visual & Audio Specification. Phase 4 uses this document as the definitive reference for rendering, HUD implementation, menu screens, and audio integration.

## Input Artifacts

Phase 3 artifacts:
- `docs/visual-design.md` (Stage 3-1)
- `docs/audio-design.md` (Stage 3-2)

Phase 2 artifacts (for cross-referencing):
- `consolidation-artifacts/phase-2-consolidation.md`

## Process

### 1. Read All Phase 3 Artifacts

Read both Phase 3 artifacts. Check for:
- Any entity in the GDD that has no visual spec
- Any significant game event in the GDD that has no audio spec
- Inconsistencies between the entity visual specs and the entity design

Flag any gaps to the user. Resolve before producing the final document.

### 2. Validate Implementation-Readiness

A Phase 4 developer should be able to implement visuals and audio from this document alone:
- [ ] Every entity has a shape, color (hex), and size
- [ ] Canvas/screen dimensions are defined
- [ ] HUD elements have position, format, and color defined
- [ ] All menu screens have layout descriptions
- [ ] All animation behaviors are described in plain terms
- [ ] All SFX triggers are listed with descriptions
- [ ] Music moods are defined per game state
- [ ] Audio source approach is noted

### 3. Create Consolidation Document

Create `consolidation-artifacts/phase-3-consolidation.md`:

```markdown
# [Game Title] — Visual & Audio Specification

> Implementation reference for Phase 4. All visual and audio decisions are finalized here.

## 1. Visual Identity

### Color Palette

| Role | Name | Hex | Used For |
|------|------|-----|----------|
| Background | ... | #... | ... |
| Player | ... | #... | ... |
...

### Canvas / Screen

- **Size:** [W × H px]
- **HUD zone:** [position, dimensions]
- **Game world zone:** [position, dimensions]

## 2. Entity Visual Specs

| Entity | Shape | Color (hex) | Size (px) | Notes |
|--------|-------|-------------|-----------|-------|
...

## 3. Animation Descriptions

### [Entity]
- Normal: [description]
- [State]: [visual behavior description]
...

## 4. HUD Design

| Element | Position | Format | Color |
|---------|----------|--------|-------|
...

## 5. Menu Screens

### Main Menu
[Layout description with element positions]

### Pause Screen
[Layout description]

### Game Over Screen
[Layout description — what info is shown]

### Victory Screen (if applicable)
[Layout description]

## 6. Sound Effects

| Trigger | Description | Duration |
|---------|-------------|----------|
...

## 7. Music

| Game State | Mood | Loop? | Notes |
|------------|------|-------|-------|
...

## 8. Audio Source Plan
[Approach: free packs / procedural / custom / deferred]

## 9. Implementation Notes
[Any visual or audio decision with a direct implementation implication]
[Edge cases or ambiguities to resolve in Phase 4]
```

### 4. User Review

Present the specification to the user:
- Confirm all visual decisions are accurately captured
- Confirm all audio decisions are accurately captured
- Confirm nothing is missing or contradicted
- Confirm ready to proceed to implementation

## Output Artifacts

### Artifact: `consolidation-artifacts/phase-3-consolidation.md`

The Visual & Audio Specification — a single implementation reference for all Phase 3 work.

## Exit Criteria

- [ ] All Phase 3 artifacts have been read
- [ ] Cross-artifact gaps identified and resolved
- [ ] Visual & Audio Specification produced
- [ ] Every entity has a complete visual spec in the document
- [ ] Every significant event has a sound spec
- [ ] User has approved the specification
- [ ] Output artifact `consolidation-artifacts/phase-3-consolidation.md` is generated
- [ ] Session log exported via `/export-log 3-3`

---

## Phase Transition

**Phase 3 (Visual & Audio Design) is now complete.**

Proceed to **Phase 4: Prototype Implementation**, starting with **Stage 4-1: Project Setup**.

The primary inputs for Phase 4 are:
- `consolidation-artifacts/phase-3-consolidation.md` (visual & audio specs)
- `consolidation-artifacts/phase-2-consolidation.md` (game design document)
- `consolidation-artifacts/phase-1-consolidation.md` (mechanics, engine, scope)
- `docs/tech-stack.md` (engine, language, tools)
