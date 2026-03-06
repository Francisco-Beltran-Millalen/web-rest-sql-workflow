# Export Log Skill

Export the current conversation to a log file in `docs/logs/`.

## Arguments

- Stage identifier:
  - `0` for meta-workflow
  - `diagram` for diagram-assistant
  - `import` for import-artifact
  - `knowledge` for knowledge-tester
  - `teacher` for teacher
  - `git` for git-assistant
  - `<phase>-<stage>` for regular stages (e.g., `2-1` for Phase 2 Stage 1)

## Process

1. Find the current session's transcript file — location is tool-specific, defined in the CLI adapter
2. Run the tool-specific converter script to convert it to readable text
3. Save to `docs/logs/` using the naming convention below

**Naming format:** `stage-<identifier>-<name>-<YYYYMMDD>-<HHMMSS>.txt`

Examples:
- `stage-00-meta-workflow-20260203-091500.txt`
- `stage-2-1-entity-ui-sketching-20260203-143022.txt`

## Stage Names

### On-Demand Stages
- 0 → `00-meta-workflow`
- diagram → `diagram-assistant`
- import → `import-artifact`
- knowledge → `knowledge-tester`
- teacher → `teacher`
- git → `git-assistant`

### Phase 1: Discovery + Tech Selection
- 1-1 → `1-1-project-definition`
- 1-2 → `1-2-knowledge-audit`
- 1-3 → `1-3-research`
- 1-4 → `1-4-use-case-discovery`
- 1-5 → `1-5-tech-selection`
- 1-6 → `1-6-consolidation`

### Phase 2: Sketching & Data Modeling
- 2-1 → `2-1-entity-ui-sketching`
- 2-2 → `2-2-data-modeling`
- 2-3 → `2-3-endpoint-design`
- 2-4 → `2-4-consolidation`

### Phase 3: UI Polish
- 3-1 → `3-1-visual-design`
- 3-2 → `3-2-core-app-views`
- 3-3 → `3-3-user-views`
- 3-4 → `3-4-auth-views`
- 3-5 → `3-5-consolidation`

### Phase 4: Prototype Implementation
- 4-1 → `4-1-project-setup`
- 4-2 → `4-2-implementation-loop`
- 4-3 → `4-3-learning-guide`
- 4-4 → `4-4-refactor`

### Phase 5: Deployment
- 5-1 → `5-1-deployment`
