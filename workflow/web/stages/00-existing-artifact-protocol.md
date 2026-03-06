# Existing Artifact Protocol

When starting a Phase 1–4 stage, the `start-stage` skill checks whether the stage's output artifacts already exist. This protocol defines what to do when they do.

**Does not apply to on-demand stages (0, D, I, T).**

---

## Step 1: Identify Which Artifacts Exist

Look at the stage file's `## Output Artifacts` section. Check if any of the listed files (or folders) already exist.

**Special cases:**

- **Stages 4-2 and 4-3** are designed for multiple sessions. If `consolidation-artifacts/implementation-decisions.md` exists with **some but not all use cases complete**, this is normal resumption — skip this protocol entirely and use the stage's own Session Start process. Apply this protocol only if **all use cases are already marked complete** (stage was previously finished).
- **Stages 3-2, 3-3, and 3-4** update shared Phase 3 artifacts (`phase-3-design-decisions.md`, `styles.css`, `docs/assets/views/`) that are created by Stage 3-1. These files pre-existing is normal and expected — it means Stage 3-1 ran, not that the current stage ran before. **Skip this protocol entirely for these stages.** Each stage reads the current state of those shared files in its own Part 1 process.
- **Stage 2-4**: The `docs/assets/` folder (Artifact 2) is created in Stage 2-1 and always pre-exists when Stage 2-4 runs. Do not treat it as a trigger indicator. Use only `consolidation-artifacts/phase-2-consolidation.md` to determine whether Stage 2-4 has run before.
- **Stage 3-1**: `phase-3-design-decisions.md` is a living document that spans all Phase 3 stages. If it exists, this protocol applies.
- **Stage 2-1**: Check for `docs/entity-map.md` and `docs/view-entity-mapping.md` as primary indicators. The `docs/assets/views/` folder may already contain HTML files from a previous run.

---

## Step 2: Read and Summarize

For each existing artifact:

1. **Read it**
2. **Show a brief summary** — 2–5 bullet points covering the key content and decisions made

---

## Step 3: Ask Why We're Revisiting

Ask the user why this stage is being run again, and present these options:

> "This stage's output already exists (summary above). Why are we revisiting it?"

- **Iteration** — Refine, expand, or improve the existing work
- **Project direction change** — Goals or scope have shifted; some or all of this may no longer apply
- **Technology stack change** — Different technology choices were made; tech-specific content needs updating
- **Error correction** — Something in the artifact is factually wrong and needs fixing
- **Other** — User describes another reason

---

## Step 4: Proceed Based on the Reason

| Reason | How to Proceed |
|--------|----------------|
| **Iteration** | Load as current state. Build on it. Do not restart from scratch. |
| **Project direction change** | Start fresh. Keep existing artifact as historical reference only — do not be bound by prior decisions. |
| **Technology stack change** | Update in place. Focus changes on tech-specific sections. Structural and domain decisions remain unless the user changes them. |
| **Error correction** | Load the artifact, identify the specific error, fix it. Update in place. |
| **Other** | Ask for more context, then decide together how to proceed. |

---

After completing this protocol, continue with the stage process (Step 4 of `start-stage`).
