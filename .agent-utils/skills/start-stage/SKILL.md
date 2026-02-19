# Start Stage Skill

Start the specified workflow stage.

## Arguments

- Stage identifier:
  - `0` for meta-workflow
  - `d` for diagram assistant
  - `<phase>-<stage>` for regular stages (e.g., `2-1` for Phase 2 Stage 1)

## Instructions

1. Parse the stage identifier:
   - If `0`: Read `workflow/web-rest-sql/stages/phase-0/00-meta-workflow.md`
   - If `d`: Read `workflow/web-rest-sql/stages/phase-0/01-diagram-assistant.md`
   - If `i`: Read `workflow/web-rest-sql/stages/phase-0/02-import-artifact.md`
   - If `<phase>-<stage>`: Read `workflow/web-rest-sql/stages/phase-<phase>/0<stage>-*.md`
2. Adopt the persona defined in the stage file
3. Check `docs/` for existing artifacts
4. Follow the stage process

## Stage Mapping

### On-Demand Stages
- 0: meta-workflow (fix workflow issues)
- d: diagram-assistant (visualize artifacts)
- i: import-artifact (import and adapt external artifacts)

### Phase 1: Discovery + Tech Selection
- 1-1: project-definition
- 1-2: knowledge-audit
- 1-3: research
- 1-4: use-case-discovery
- 1-5: tech-selection
- 1-6: consolidation

### Phase 2: Sketching & Data Modeling
- 2-1: entity-ui-sketching
- 2-2: data-modeling
- 2-3: endpoint-design
- 2-4: consolidation

### Phase 3: UI Polish
- 3-1: visual-design (Design Direction + Main View)
- 3-2: core-app-views
- 3-3: user-views
- 3-4: auth-views
- 3-5: consolidation

### Phase 4: Prototype Implementation
- 4-1: project-setup
- 4-2: implementation-loop (repeats per use case)

## Example Usage

```
/start-stage 0
```
Starts Stage 0 (Meta-Workflow) with the Workflow Engineer persona.

```
/start-stage 2-1
```
Starts Phase 2, Stage 1 (Entity & UI Sketching) with the Domain Modeler + UI Sketcher persona.

```
/start-stage 4-2
```
Starts Phase 4, Stage 2 (Implementation Loop) with the Senior Developer persona.
