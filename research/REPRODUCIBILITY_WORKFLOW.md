# Reproducible research handoff (Git-first)

This is an incremental fix based on **main**, not another unreviewed commit to the diverged research branch.

## Current repository state (2026-10-30)
- Default branch: `main`.
- Research branch: `audit/2026-10-28-independent-reconstruction`.
- GitHub compare: research branch is **331 commits ahead and 359 behind main** (diverged). Do **not** merge indiscriminately or force-push it.
- Review the research branch's `research/claims/CLAIM_LEDGER.csv` and `research/HANDOFF_AND_DATA_PROVENANCE.md` as historical records, **not** authoritative evidence of merged work.
- The currently generated `singular_boundary_handoff_core.zip` and `singular_boundary_handoff_full.zip` exist only as conversation artifacts until placed in persistent storage. The repository does **not** currently track their contents or the large historical numerical dataset.

## Workflow
1. Use `main` (or its next reviewed integration branch) as a base; create a focused topic branch.
2. Commit source code, small reproducible fixtures, manifests, tests and docs together. Avoid one file per independent commit unless separately reviewable.
3. Store large and immutable numerical artifacts in release assets, Git LFS, or object storage; track their **SHA-256**, size, producer, input dataset hashes, licensing/privacy, and exact retrieval URI in Git.
4. Treat every science claim as conditional until script + inputs + outputs can be reproduced. In particular, `m5_whitney_candidate_2026-10-30.npz` is **not** the historical `global_whitney_11face.npz`.
5. Open a PR, inspect its diff and CI, then merge only after review. Do not claim a branch's research files are on main.
6. In a new conversation, check out the reviewed ref, retrieve immutable binary inputs, run the SHA-256 verifier, then execute the documented scientific regression.

## Verifying portable archives
```bash
python research/scripts/verify_research_handoff.py singular_boundary_handoff_full.zip
python research/scripts/verify_research_handoff.py /path/to/extracted-package
```
The manifest contains the **original** `/mnt/data` path; the verifier intentionally ignores it. An archive may include only a subset of manifest files; in that case the verifier reports missing entries instead of claiming a complete recovery. Generate a *bundle-specific* manifest for any subset: the old global inventory is not automatically a valid core-bundle manifest.

## Required follow-up
- Reconcile the diverged research branch using small cherry-picked PRs, retaining original commit attribution and full scientific caveats.
- Regenerate bundle-specific manifests and rerun the verifier against each exported ZIP; do not assume previous ZIP CRC checks imply all files match the manifest.
- Establish persistent external storage for the experiment data and historical original matrix.
- Run and record the full repository test suite and CI, which have **not** been run by this PR.

No result here proves the uniform Penrose center-cap claim or continuum Yang–Mills mass gap.
