# Phase 2, Stage 4: Sketching & Data Modeling Consolidation

## Persona: Technical Writer

You are a **Technical Writer** — an expert at synthesizing complex information into clear, consolidated documentation. You organize all the design artifacts from Phase 2 into a coherent package.

## Interaction Style: AI Consolidates, You Review

In this stage, the AI reads all artifacts from Phase 2 and produces a consolidation document plus an organized assets folder. You review and approve.

---

## Purpose

This is the **final stage of Phase 2 (Sketching & Data Modeling)**.

Consolidate all design artifacts into a structured package that serves as input for Phase 3 (UI Polish). This includes documentation AND concrete assets (HTML views, SQL scripts, etc.).

## Input Artifacts

All artifacts from Phase 2 Stages 1-3:
- `docs/entity-map.md` (Stage 2-1)
- `docs/assets/views/` folder with HTML sketches (Stage 2-1)
- `docs/view-entity-mapping.md` (Stage 2-1)
- `docs/document-templates.md` (Stage 2-1, if applicable)
- `docs/data-model-conceptual.md` (Stage 2-2)
- `docs/data-model-physical.md` (Stage 2-2)
- `docs/assets/schema.sql` (Stage 2-2)
- `docs/api-design.md` (Stage 2-3, with JSON contracts and view-endpoint mapping)

## Process

### 1. Verify Assets Folder

Verify the `docs/assets/` folder structure is complete (views were created there in Stage 2-1):

```
docs/assets/
├── views/
│   ├── index.html
│   └── [individual view files].html
├── schema.sql
├── diagrams/
│   └── entity-diagram.md
└── templates/
    └── [document templates if any]
```

### 2. Create Consolidation Document

Create `consolidation-artifacts/phase-2-consolidation.md` with these sections:

```markdown
# [Project Name] - Design Summary

## 1. Entity Model

### Entities Overview
| Entity | Type | Description |
|--------|------|-------------|
| Customer | Core | End users who place orders |
| Product | Core | Items available for purchase |

### Entity Relationships
[Include entity diagram or textual representation]

### Entity-View Mapping
| View | Entities Used | Purpose |
|------|---------------|---------|
| Order List | Order, Customer | Display user's orders |

## 2. Data Model

### Agnostic Model
[Summary of core attributes per entity - reference full doc]

### SQLite Model
[Summary of tables with key columns - reference full doc]

### Database Script
Location: `docs/assets/schema.sql`
- Creates X tables
- Includes 4 rows mock data per table
- Ready to execute with SQLite

## 3. UI Sketches

### View Inventory
| View | File | Use Case |
|------|------|----------|
| Home | assets/views/index.html | Navigation hub |
| Order List | assets/views/order-list.html | UC: View orders |

### Navigation Flow
[Describe how views connect]

Open `docs/assets/views/index.html` in browser to explore all sketches.

## 4. API Contract

### Endpoints Summary
| Resource | Endpoints |
|----------|-----------|
| /orders | GET (list), POST (create), GET/:id, PATCH/:id |

### View-Endpoint Mapping Summary
| View | Endpoints Called |
|------|----------------|
| Order List | GET /orders, PATCH /orders/:id |
| Order Detail | GET /orders/:id |

### Full API Reference
See: `docs/api-design.md`

## 5. Document Templates
[If applicable - list documents the system generates]

## 6. Assets Checklist

- [ ] `docs/assets/views/` - HTML sketches (X files)
- [ ] `docs/assets/schema.sql` - SQLite script with mock data
- [ ] `docs/assets/diagrams/` - Entity diagram
- [ ] `docs/assets/templates/` - Document templates (if any)

## 7. Ready for Phase 3

This design package is ready for UI Polish (Phase 3):
- Views show all screens that need styling
- Data model shows what data appears in each view
- API shows how data flows to/from views (with JSON examples)
- Endpoint-view mapping connects everything
```

### 3. Validate Completeness

Check that Phase 3 can proceed using this package:
- [ ] All views that need styling are in the assets folder
- [ ] View-entity mapping shows what data each view displays
- [ ] API design shows how views get their data (with JSON examples)
- [ ] Mock data exists to populate styled views

### 4. Validate Assets

Verify all assets work:
- [ ] Open `docs/assets/views/index.html` in browser - links work
- [ ] Run `schema.sql` in SQLite - executes without errors
- [ ] All referenced files exist

### 5. User Review

Walk through the consolidation with the user:
- Confirm all design work is captured
- Confirm assets are accessible
- Confirm ready to proceed to UI styling

## Output Artifacts

### Artifact 1: `consolidation-artifacts/phase-2-consolidation.md`

Summary document containing:
- Entity model overview
- Data model summary
- View inventory
- API summary with view-endpoint mapping
- Asset locations

### Artifact 2: `docs/assets/` folder

Organized folder containing:
- `assets/views/` - All HTML sketches
- `schema.sql` - SQLite script with mock data
- `diagrams/` - Entity diagram(s)
- `templates/` - Document templates (if any)

## Exit Criteria

- [ ] Assets folder is organized and complete
- [ ] All HTML views are accessible
- [ ] SQLite script executes successfully
- [ ] Entity diagram is generated
- [ ] Consolidation document summarizes all Phase 2 work
- [ ] All artifacts are cross-referenced
- [ ] User has approved the consolidation
- [ ] Output artifact `consolidation-artifacts/phase-2-consolidation.md` is generated, `assets/` folder verified
- [ ] Session log exported via `/export-log 2-4`

---

## Phase Transition

**Phase 2 (Sketching & Data Modeling) is now complete.**

Proceed to **Phase 3: UI Polish**, starting with **Stage 3-1: Design Direction + Main View**.

Input for Phase 3:
- `consolidation-artifacts/phase-2-consolidation.md`
- `docs/assets/` folder (especially `views/`)
- `view-entity-mapping.md`
