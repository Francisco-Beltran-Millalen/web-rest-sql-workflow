# Existing Artifact Protocol

When starting a Phase 1–4 stage, the `start-stage` skill checks whether the stage's output artifacts already exist. This protocol defines what to do when they do.

**Does not apply to on-demand stages (0, diagram, import, knowledge, teacher, git).**

---

## Step 1: Identify Which Artifacts Exist

Look at the stage file's `## Output Artifacts` section. Check if any of the listed files (or folders) already exist.

**Special cases:**

- **Stages 4-2 and 4-3** are designed for multiple sessions. If `consolidation-artifacts/implementation-decisions.md` exists with **some but not all mechanics complete**, this is normal resumption — skip this protocol entirely and use the stage's own Session Start process. Apply this protocol only if **all mechanics are already marked complete** (stage was previously finished).
- **Stage 2-3 (Level Design)** is conditional. It may not exist even after Phase 2 if the game has no distinct levels. This is expected — do not treat its absence as a problem, and do not trigger this protocol for its absence.

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
