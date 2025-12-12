# Baseline (2025-12-12)

## Snapshot
- Repo URL: https://github.com/IotA-asce/influencer-manager (cloned locally; no remote configured)
- Default branch: work (only existing branch prior to this chore branch)
- Commit count / last commit: 1 commit; 9484e1a Initial commit
- Files present (top-level list): .gitignore, LICENSE, README.md (no code directories yet)
- License: MIT

## What exists today
- Code: none
- Tooling: none detected (no dependency files or scripts)
- CI: none
- Tests: none

## Gaps vs our target system
- What we need to add in upcoming steps (brief bullets), including:
  - Python project scaffolding
  - Gemini image generation module
  - Instagram Publishing API module (container -> publish flow)
  - Storage for image URLs
  - Scheduler + logs + retries

## Open decisions (must decide before/within Step 2–4)
- Python version target: Recommend Python 3.12 for current long-term support, performance, and library compatibility.
- Dependency manager: Recommend uv for fast installs, lockfile support, and compatibility with standard Python tooling; poetry is an alternative if we need built-in project metadata workflows.
- Storage approach for generated images: Recommend S3-compatible object storage (e.g., AWS S3 or MinIO) with a local directory fallback for development to simplify URL persistence and portability.
- Secrets strategy: Use dotenv for local development (.env and .env.example) and environment variables in CI/CD with a secrets manager (e.g., GitHub Actions secrets) to avoid committing sensitive values.

## Risks / constraints
- Instagram Publishing API access requires appropriate account permissions (e.g., Business account), app review, and rate limits; lacking these could block publishing until resolved.

## Next step pointer
- Proceed to Step 2: Architecture blueprint & module boundaries
