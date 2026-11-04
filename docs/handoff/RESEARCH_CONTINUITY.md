# Research continuity: start here (2026-10-30)

## Canonical storage and truth

This private GitHub repository is the durable **text/code/proof ledger**. A ChatGPT conversation, `/mnt/data` path, automatically mounted upload, unpublished local Git checkout, and downloadable chat ZIP are **ephemeral** and may disappear across turns, branches or runtimes. They are NOT substitutes for a committed Git object. The research must stop treating a URL-shaped note or a remembered file path as verified availability.

The checked remote branch is `audit/2026-10-28-independent-reconstruction`. At the start of any new conversation, ask the assistant to open this file, `docs/current/STATUS.md`, `research/claims/CLAIM_LEDGER.csv`, and `data/RESEARCH_ASSET_REGISTRY.csv` directly through the GitHub connector. If a file is not available, report missing bytes and STOP dependent reconstruction; do not manufacture an equivalent dataset or treat a newly assembled matrix as an original.

## What persists / what does not

1. **Remote GitHub commits**: markdown proof notes and scripts committed to the remote are durable, subject to repository retention/access. Each branch is its own ref; commits are not necessarily on `main`.
2. **Large numerical inputs**: original NPZ, ZIP, Stage 26 checkpoint and unpublished intermediate arrays are not yet known to be stored on the remote. Their presence in chat attachments or temporary container does not guarantee future availability. See registry with states `REMOTE_COMMITTED`, `REGENERABLE`, `EPHEMERAL_ONLY`, `UNAVAILABLE`.
3. **Exact reproducibility**: each required dataset needs origin, sha256, committed generator code, input hash, CLI, environment/versions, and preferably independent validation. A generator is NOT a substitute for immutable historical bytes when comparing original computations.
4. **Branch switching**: use the actual committed SHA as a handoff anchor. Never assume an unpushed local checkout on a prior conversation can be reached from a different environment.
5. **Chat attachments**: no archive dumps or large downloadable ZIPs in chat. Share brief GitHub links to committed files only.

## Existing gap / action plan

The repository's `sources/source-manifests/IMPORT_STATUS.md` says the 602-item prepared historical source tree was **NOT completely imported**; `data/README.md` says raw scientific binaries were **NOT committed**, and Git LFS is unverified. This is the root cause of the repeated historical Whitney matrix loss and conflicting reconstructions; it is a missing-persistence problem, not evidence of corruption in the GitHub checkout.

**Phase A**: commit the original small archive-derived source Python files, byte-for-byte, to `sources/historical/penrose_2p1/` and add their SHA-256 values. Do not replace them with rewritten scripts. Complete the outstanding text/source import from a fresh checkout based on the remote branch; never force-push the unrelated 602-file local Git root.

**Phase B**: for binaries pick a durable immutable provider (Git LFS if independently verified or versioned content-addressed object storage). Upload once. Confirm fresh-download hash matches. Store object URI/size/sha256 in registry. If storage is unavailable, mark `EPHEMERAL_ONLY` rather than `BACKED_UP`. Do not put private signed URLs or secrets in the repo.

**Phase C**: make each new result atomic: Git commit of note + regression + data manifest change, check resulting remote SHA. For computational artifacts store input identities and deterministic generation steps. Record exact software versions, seed, dimensionality, and array keys. Record state explicitly if only local validation was performed.

## Current matrix conflict

The historically reported `global_whitney_11face.npz` is **UNAVAILABLE** in the current runtime and not known to be remotely persisted. Historical edge-13 diagonal ≈0.7778590281 and eigenvalues ≈0.14317415/1.10465934 are *reported diagnostics*, not a substitute for the 30×30 entries. The newly defined candidate `m5_whitney_candidate_2026-10-30.npz` has a different convention and sha256 (see registry); it is **NOT** the historical inverse-Whitney matrix. Never use it to silently confirm R3-IR-528/529 numbers.

## Reuse prompt for future conversations

“Continue The Singular Boundary from `syncgravity/singular-boundary`, branch `audit/2026-10-28-independent-reconstruction`. First read `docs/handoff/RESEARCH_CONTINUITY.md`, `data/RESEARCH_ASSET_REGISTRY.csv`, `docs/current/STATUS.md`, and the end of `research/claims/CLAIM_LEDGER.csv`. Verify that input data are available by hashes before computations. Do not attach archives to chat. Commit each verified result to GitHub and report precise gaps.”

## Next research task

Finish source import and original historical 30×30 matrix recovery/verification **before** any physically interpreted actual-matrix two-tree Hamiltonian comparison. Continuum gap and refinement-uniform center-cap results remain OPEN.
