# Task Checklist: Git Init & GitHub Publish

## Task 1: Verify source and remote

**Description:** Confirm the canonical project exists and the target GitHub repository is reachable.

**Acceptance criteria:**
- [x] Source tree found at `E:\property-broker-chatbot`
- [x] GitHub repo `ulteamus/jakas-website-new-v1-8-31-2026` exists
- [x] `gh` authenticated as `ulteamus`

**Verification:**
- [x] `gh repo view ulteamus/jakas-website-new-v1-8-31-2026` succeeds

**Dependencies:** None  
**Estimated scope:** XS

---

## Task 2: Clone to D: drive

**Description:** Create `D:\property-broker-chatbot` from the GitHub remote.

**Acceptance criteria:**
- [x] `D:\property-broker-chatbot` exists
- [x] `.git` present; `origin` points to GitHub
- [x] On branch `main`, tracking `origin/main`

**Verification:**
- [x] `git -C D:\property-broker-chatbot status -sb` → `## main...origin/main`

**Dependencies:** Task 1  
**Estimated scope:** S

---

## Task 3: Standardize directory structure

**Description:** Move non-runtime documentation to `docs/`; keep code directories at repo root.

**Acceptance criteria:**
- [x] `docs/` contains planning/report markdown
- [x] `README.md`, `app.py`, `vercel.json` remain at root
- [x] No changes to `templates/`, `static/`, or UI files

**Verification:**
- [x] `git status` shows renames under `docs/`

**Dependencies:** Task 2  
**Files touched:**
- `docs/ACCEPTANCE_REPORT.md` (moved)
- `docs/CONTEXT.md` (moved)
- `docs/IMPLEMENTATION_PLAN.md` (moved)
- `docs/PROJECT_CONTEXT.md` (moved)
- `docs/RELEASE_RUNBOOK.md` (moved)
- `docs/SHIP_CHECKLIST.md` (moved)

**Estimated scope:** S

---

## Task 4: Harden `.gitignore`

**Description:** Ensure ignore rules cover Python, Flask, Supabase, Vercel, secrets, and OS artifacts.

**Acceptance criteria:**
- [x] `.env` and `.venv/` ignored
- [x] `uploads/`, `*.log`, `.vercel/` ignored
- [x] OS junk (`Thumbs.db`, `.DS_Store`) ignored
- [x] `data/` and SQLite files ignored

**Verification:**
- [x] Review `.gitignore` diff

**Dependencies:** Task 2  
**Estimated scope:** XS

---

## Task 5: Commit and push

**Description:** Stage all changes, commit, and push to `main`.

**Acceptance criteria:**
- [x] All intended files staged
- [x] Commit message describes structure/gitignore changes
- [x] `git push origin main` succeeds

**Verification:**
- [x] `gh repo view` shows updated `pushed_at`
- [x] GitHub default branch is `main`

**Dependencies:** Tasks 3–4  
**Estimated scope:** XS

---

## Checkpoint: Complete

- [x] Local repo at `D:\property-broker-chatbot` ready for development
- [x] Remote `main` up to date
- [x] Planning docs in `tasks/` committed
