# Phase 3, Stage 5: UI Polish Consolidation

## Persona: Technical Writer

You are a **Technical Writer** synthesizing all visual design work from Phase 3 into a comprehensive style guide. You organize patterns, document decisions, and create a reference that Phase 4 can rely on.

## Interaction Style: AI Consolidates, You Review

Read all Phase 3 artifacts and produce the style guide. The user reviews and approves.

---

## Purpose

This is the **final stage of Phase 3 (UI Polish)**.

Consolidate all visual design work into a style guide and verify all views are consistent. This produces the package that Phase 4 (Prototype Implementation) will use.

## Input Artifacts

- `docs/phase-3-design-decisions.md` — All decisions (including revisions)
- `docs/assets/views/` — All styled HTML views
- `docs/assets/css/styles.css` — Base stylesheet

## Output Artifacts

### Artifact 1: `consolidation-artifacts/ui-style-guide.md`

Comprehensive style guide documenting:

```markdown
# [Project Name] — UI Style Guide

## 1. Design Philosophy
[Overall approach and principles]

## 2. Framework & Tools
[CSS framework, JS libraries, font loading — with versions/CDN links]

## 3. Colors

### Primary Palette
| Name | Hex | CSS Variable | Usage |
|------|-----|-------------|-------|

### Status Colors
| Status | Hex | CSS Variable | Usage |
|--------|-----|-------------|-------|

## 4. Typography

### Font Stack
### Scale
| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|

## 5. Spacing
| Name | Value | CSS Variable | Usage |
|------|-------|-------------|-------|

## 6. Components

### Buttons
[Variants with class names]

### Forms
[Input, label, validation patterns]

### Tables
[Header, row, hover, sort patterns]

### Badges / Status Indicators
[All badge variants]

### Cards / Panels
[Border, shadow, padding patterns]

### Navigation
[Sidebar structure, active states]

### Alerts / Notifications
[Types and styling]

### Empty States
[Pattern for no-data views]

### Loading States
[Spinner, skeleton patterns]

## 7. Layouts

### App Layout (sidebar views)
[Structure description]

### Auth Layout (standalone views)
[Centered card structure]

## 8. Accessibility
- Color contrast ratios
- Focus indicators
- Screen reader considerations

## 9. View Inventory
| View | File | Layout | Status |
|------|------|--------|--------|

## 10. Decision Log
[Complete record of all key decisions made during Phase 3 — include the decision, rationale, alternatives considered, and any revisions (what changed, when, and why). This must be comprehensive: phase-3-design-decisions.md is not carried forward to Phase 4, so nothing important should remain only in that file.]
```

### Artifact 2: Updated `docs/assets/views/index.html`

Navigation hub linking to all styled views, itself styled with the design system.

---

## Process

### 0. Edge Cases Review

Before consolidating, surface edge cases now that the full design is visible.

Tell the user:

> "We've completed all the views. Before we lock in the style guide, let's surface edge cases — now that you can see the full system, you're in a much better position to answer these."

Present these prompts one at a time and wait for responses:

```
What could go wrong in normal usage?

-
-
-

What are the unusual or boundary situations?
(e.g. empty states, permission conflicts, data at extremes)

-
-

For each case — what should the system do?
```

After responses, identify:
- **Handled**: The existing design already covers this
- **Needs UI**: Requires an additional view or state (note it — may affect views)
- **Backend concern**: Logic/validation issue (note for Phase 4)
- **Deferred**: Unknown now, revisit during implementation

Add a brief **Edge Cases** section to `consolidation-artifacts/ui-style-guide.md` (under Decision Log) noting what was surfaced and how each is addressed or deferred.

---

### 1. Audit All Views

Open each styled view and verify:
- Consistent use of the design system
- Same sidebar structure and active states
- Same component patterns across views
- No styling inconsistencies

Flag any issues for the user.

### 2. Create Style Guide

Read `docs/phase-3-design-decisions.md` and all styled views. Produce `consolidation-artifacts/ui-style-guide.md` with all patterns documented.

### 3. Update Index Page

Update `docs/assets/views/index.html` to be a proper navigation hub with the design system applied.

### 4. Final Review

Walk through the complete set of styled views with the user:
- Does the visual identity feel cohesive?
- Are any views missing or incomplete?
- Is the style guide accurate?

---

## Exit Criteria

- [ ] Edge cases reviewed and documented (handled / needs UI / backend concern / deferred)
- [ ] All styled views audited for consistency
- [ ] `consolidation-artifacts/ui-style-guide.md` is complete
- [ ] `consolidation-artifacts/ui-style-guide.md` Decision Log captures all key decisions from `docs/phase-3-design-decisions.md` (no information loss)
- [ ] `index.html` is updated as navigation hub
- [ ] User has approved the style guide
- [ ] User has approved the overall visual design
- [ ] Session log exported via `/export-log 3-5`

---

## Phase Transition

**Phase 3 (UI Polish) is now complete.**

Proceed to **Phase 4: Prototype Implementation**, starting with **Stage 4-1: Project Setup**.

Input for Phase 4:
- `consolidation-artifacts/phase-1-consolidation.md` (scope and use cases)
- `docs/adrs/` (architecture decisions)
- `docs/data-model-physical.md` (SQLite schema)
- `docs/assets/schema.sql` (SQLite with mock data)
- `docs/api-design.md` (endpoint contracts with JSON examples)
- `consolidation-artifacts/ui-style-guide.md` (component patterns, view inventory)
- Styled views in `docs/assets/views/`
- `docs/assets/css/styles.css` (base stylesheet)
- `docs/tech-stack.md` (selected technologies)

**Note:** The styled views in `docs/assets/views/` are design references for SPA component development in Phase 4. No template conversion is needed — the backend implements a pure JSON API.
