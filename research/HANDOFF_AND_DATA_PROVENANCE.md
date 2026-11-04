# Durable research handoff — The Singular Boundary

**Current checkpoint:** R3-IR-537, 2026-10-30. **GitHub branch:** `audit/2026-10-28-independent-reconstruction`. **Primary record:** `research/claims/CLAIM_LEDGER.csv`.

## Recovery checklist for a new conversation
1. Read this document and the claims ledger. Check the latest claims R3-IR-528 through R3-IR-537, particularly qualifications and retractions.
2. Request the portable `singular_boundary_handoff_core.zip` generated in the current ChatGPT session; it includes `penrose_restore/src`, a *candidate* 30×30 Whitney matrix, the current regression scripts, `README_HANDOFF.md`, and `FILE_MANIFEST.json`.
3. If reproducing Stage 26 experiments, read `FILE_MANIFEST.json` and request the `singular_boundary_handoff_full.zip`, or original independently stored experimental uploads. The very large source archives ARE NOT included in GitHub; do not assume a path such as `/mnt/data` persists between conversations.
4. Verify SHA-256 file digests and archive inventories. `zipfile.ZipFile(...).testzip()` passed when both archives were created; inspect all file provenance and executable dependencies before trusting any result.
5. Treat `m5_whitney_candidate_2026-10-30.npz` as a NEW matrix, not the historical `global_whitney_11face.npz`: its eigenvalue and diagonal diagnostics disagree. Do not silently repair or conflate.
6. Resume by reconciling the historical Whitney integration convention and checking the two rooted-tree SU(2) electric quadratic forms on actual gauge-invariant M5 Wilson observables. Physical refinement and relative double-center cap remain open. No Yang–Mills mass gap proof exists.

## Persistence policy
- GitHub tracks **small source, proofs, scripts, and claims**; all research results should identify exact inputs and source hashes.
- Binary study uploads and datasets require a persistent user-managed location (ChatGPT Project files, a versioned cloud drive, or object storage). Generating a sandbox file or attaching it to a chat is not a guarantee of permanent cross-conversation access.
- Preserve two immutable named bundles: core for day-to-day handoff and full for archival recovery. Download and store them independently; store a SHA-256 manifest alongside both.
- Recompute the manifest upon changes; do not silently overwrite a prior version. A new checkpoint should update the ledger and the handoff status, and include any newly generated binary artifacts in the bundle.
- On a new conversation, do not invent paths or GitHub commits. Validate each source actually available in that environment.

## Status
Verified within the session: 53-file SHA-256 inventory; integrity-tested core ZIP (35 entries) and full ZIP (56 entries). The core ZIP is roughly 258 KB and the full ZIP roughly 137 MB. Their exact contents and original source digests are in the included `FILE_MANIFEST.json`.

**Scientific distinction:** R3-IR-528–529 are conditional finite-regulator arguments under a selected root-tree connection. R3-IR-537's reconstructed matrix is a mismatching alternative candidate. Uniform shrinking-center cap estimates and the continuum Yang–Mills mass gap are OPEN.
