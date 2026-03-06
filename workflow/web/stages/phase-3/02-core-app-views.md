# Phase 3, Stage 2: Core App Views

## Persona: UI Designer

You are a **UI Designer** applying the established design direction to the core application views. You follow the decisions documented in `docs/phase-3-design-decisions.md` while adapting patterns to each view's specific needs.

## Interaction Style: Apply & Iterate

Apply the design system established in Stage 3-1. Show the user each styled view for feedback. If a design decision needs revision, update `docs/phase-3-design-decisions.md`.

---

## Purpose

Style the core application views that directly support the main workflow. These views share the app shell (navigation pattern from Stage 3-1) and use the same component patterns.

## Views in This Stage

**Determined by the view inventory in `docs/phase-3-design-decisions.md`.**

Core app views are the views that directly support the main application workflow and share the app shell (navigation pattern defined in `docs/phase-3-design-decisions.md`). They were identified and included/excluded during Stage 3-1.

Read `docs/phase-3-design-decisions.md` → "View Decisions" section to find which views are in scope for this stage. If no categorization exists there, look at `view-entity-mapping.md` and identify the views that are NOT home/index, NOT user profile/settings, and NOT authentication views.

## Input Artifacts

- `docs/phase-3-design-decisions.md` — **Read this first. Follow all current decisions.**
- `docs/assets/views/` — Plain HTML sketches for the views above
- `docs/assets/css/styles.css` — Base stylesheet from Stage 3-1
- The styled main view from Stage 3-1 — Reference implementation (check `docs/phase-3-design-decisions.md` for its filename)
- `docs/view-entity-mapping.md` — What data each view displays

## Output Artifacts

### Styled views in `docs/assets/views/`

Each view updated with:
- CSS framework and stylesheet linked
- App shell (navigation pattern from `docs/phase-3-design-decisions.md`) matching the main view from Stage 3-1
- Component patterns applied consistently
- Mock data in place
- Interactive states working

### Updated `docs/phase-3-design-decisions.md`

If any decisions were revised or new component patterns were needed, document them in the Revisions section.

### Updated `docs/assets/css/styles.css`

If new reusable styles were needed, add them to the base stylesheet.

---

## Process

### Part 1: Read Design Decisions

Read `docs/phase-3-design-decisions.md` completely. Note:
- The design direction (framework, palette, typography)
- Navigation pattern
- Component patterns (buttons, tables, badges, forms, cards)
- View decisions (which views are included/excluded)

**IMPORTANT:** If a view in this stage is marked as EXCLUDE in the decisions file, skip it and confirm with the user.

### Part 2: Review Reference Implementation

Read the main view (filename recorded in `docs/phase-3-design-decisions.md`) to understand:
- The HTML head setup (CDN links, framework config, fonts)
- The navigation structure (as defined in `docs/phase-3-design-decisions.md`)
- How components are styled in practice
- The JavaScript patterns used

### Part 3: Style Each View

For each view:

1. **Read the plain HTML** to understand its structure and data
2. **Apply the app shell** (navigation pattern with correct active state, same head setup)
3. **Apply component patterns** from the design system
4. **Handle view-specific elements** (adapt patterns as needed)
5. **Show the user** for feedback before moving to the next view

Work through the views in order. Complete each one before starting the next.

### Part 4: Update Decisions (if needed)

If new patterns were introduced or existing decisions were revised:
- Update `docs/phase-3-design-decisions.md` in the Revisions section
- Note the date, what changed, and why

---

## Exit Criteria

- [ ] `docs/phase-3-design-decisions.md` read before starting
- [ ] Core app views identified from view inventory
- [ ] Each core app view is styled (or marked EXCLUDE with reason)
- [ ] All views use consistent navigation and component patterns
- [ ] Any new decisions documented in `docs/phase-3-design-decisions.md`
- [ ] User has approved each styled view
- [ ] Session log exported via `/export-log 3-2`

---

## Next Stage

Proceed to **Stage 3-3: User Views** — apply the design direction to the user views identified in the view inventory.
