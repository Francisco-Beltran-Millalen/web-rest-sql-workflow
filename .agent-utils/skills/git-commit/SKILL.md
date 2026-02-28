# Git Commit Skill

Walk through a git commit workflow one command at a time. The user approves, rejects, or asks for explanation at each step.

## Interaction Pattern

For every command:

1. Show the command in a code block
2. Give a one-line plain-English explanation
3. Ask: `Run this? [yes / no / explain more]`
4. Wait for the response before proceeding

If the user says **explain more**: give a fuller explanation of what the command does and why, then ask again.
If the user says **no**: skip that step and note it, then move to the next.
If the user says **yes**: run the command and show the output before continuing.

**Never run a command without approval.**

---

## Process

### Step 1: Check What Changed

```bash
git status
```
> Shows all modified, new, and deleted files so we know what's in scope for this commit.

Run this? [yes / no / explain more]

---

### Step 2: Determine Stage Context

Read `consolidation-artifacts/implementation-decisions.md` to identify:
- Current stage (4-2, 4-3, etc.)
- Use case just completed (e.g., "UC-3: User can view order list")

If the file doesn't exist, use the stage identifier from the session context.
If context is unclear, ask: "What should I use as the commit message context?"

---

### Step 3: Stage the Files

Based on `git status` output, propose adding files relevant to the completed work.

For each logical group, show one `git add` command:

```bash
git add prototype-code/src/orders/ prototype-code/tests/test_orders.py
```
> Stages the Order service, repository, route, and tests for UC-3.

Run this? [yes / no / explain more]

If there are workflow artifacts that changed (e.g., `consolidation-artifacts/implementation-decisions.md`):

```bash
git add consolidation-artifacts/implementation-decisions.md
```
> Stages the updated implementation decisions log.

Run this? [yes / no / explain more]

---

### Step 4: Review What's Staged

```bash
git diff --staged --stat
```
> Shows a summary of exactly what will be included in the commit.

Run this? [yes / no / explain more]

---

### Step 5: Commit

Propose a commit message based on the stage context:

**Format:**
- Stage 4-2 or 4-3 (per use case): `feat: implement [use case name]`
- Stage 4-1 (project setup): `chore: project setup and scaffolding`
- Stage 3-x (UI): `design: [what was done]`
- Stage 2-x (modeling): `docs: [artifact name]`
- Stage 1-x (discovery): `docs: [artifact name]`
- Stage 0 (meta): `workflow: [what was fixed or added]`

Example:
```bash
git commit -m "feat: implement UC-3 (user can view order list)"
```
> Creates a commit with all staged changes and this message.

Run this? [yes / no / explain more]

---

### Step 6: Push (Optional)

Ask: "Do you want to push to the remote branch?"

If yes:

```bash
git push
```
> Uploads the commit to the remote repository on the current branch.

Run this? [yes / no / explain more]

If the branch has no upstream:

```bash
git push -u origin <current-branch>
```
> Pushes to remote and sets this branch to track the remote branch for future pushes.

Run this? [yes / no / explain more]
