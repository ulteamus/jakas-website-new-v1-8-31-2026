# Implementation Plan: Git Repository Initialization — `jakas-website-new-v1-8-31-2026`

## Overview

Initialize a clean Git working copy at `D:\property-broker-chatbot`, standardize the project layout, ensure stack-appropriate ignore rules, and publish to GitHub (`ulteamus/jakas-website-new-v1-8-31-2026`) on the `main` branch.

**Source of truth:** Canonical development tree on `E:\property-broker-chatbot` (already committed and pushed 2026-08-31). This task establishes the **D: drive** working copy for the current machine (`asw`).

## Architecture Decisions

- **Clone over fresh init:** Remote repo already existed with 707 tracked files and one initial commit. Cloning preserves history and avoids force-push to `main`.
- **Docs consolidation:** Root-level planning/report markdown moved to `docs/` to keep the repository root focused on runnable code and config.
- **`.gitignore` expansion:** Added OS artifacts, broader `data/` coverage, and SQLite extensions — no change to secrets or deploy-critical tracked assets.
- **No UI/template changes:** Per project rule, frontend files remain untouched.

## Task List

### Phase 1: Foundation
- [x] Task 1: Verify source project (`E:\property-broker-chatbot`) and GitHub remote exist
- [x] Task 2: Clone `https://github.com/ulteamus/jakas-website-new-v1-8-31-2026.git` → `D:\property-broker-chatbot`
- [x] Task 3: Confirm `origin` remote and `main` branch tracking

### Checkpoint: Foundation
- [x] Clone complete (707 files)
- [x] `git status` clean on `main`

### Phase 2: Structure & Hygiene
- [x] Task 4: Create `docs/` and move planning markdown from repo root
- [x] Task 5: Harden `.gitignore` for Python/Flask/Supabase/Vercel stack
- [x] Task 6: Create `tasks/` planning artifacts (this file + `todo.md`)

### Checkpoint: Structure
- [x] Commit structure changes (`73ffec0`)
- [x] Push to `origin/main`

### Phase 3: Verify
- [x] Task 7: Confirm GitHub repo URL and default branch
- [x] Task 8: Document local setup path in `tasks/todo.md`

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| `D:\` path did not exist | High | Clone creates directory; verified post-clone |
| E: drive dubious git ownership | Med | Used clone from GitHub instead of copying `.git` from E: |
| Force-push needed | Med | Avoided — remote already matched E: `main` |
| Secrets in commit | High | `.env` / `.env.local` remain gitignored; not copied |

## Open Questions

- None — repo name, path, and account (`ulteamus`) confirmed via `gh auth status`.

## Repository Details

| Field | Value |
|-------|-------|
| **Local path** | `D:\property-broker-chatbot` |
| **Remote** | `https://github.com/ulteamus/jakas-website-new-v1-8-31-2026.git` |
| **Default branch** | `main` |
| **Stack** | Python 3.11+ / Flask 3 / Supabase / Vercel serverless |
