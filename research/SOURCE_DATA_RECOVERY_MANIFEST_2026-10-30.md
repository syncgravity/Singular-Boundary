# Source data recovery and integrity manifest — 2026-10-30

**Canonical binary location:** ChatGPT Library folder `/The Singular Boundary/Source/`. Binary .npz/.zip/.tar.gz data belong in Library, **not Git**; do not add binary research datasets to Git without Git LFS. This repo cannot depend on conversation context or uncommitted /mnt/data files.

The Library contains 24 original or generated source archives plus `singular_boundary_source_manifest.json` (24 filenames, exact byte lengths and SHA-256 hashes). Library uploads reported success for all 25 objects. In future chats, search the Library folder, materialize the desired file into the active runtime, and verify its SHA-256 against this manifest. Do not infer that a file is absent merely because it is not mounted in /mnt/data.

**Authoritative Whitney matrix:** `global_whitney_11face.npz`, 8,448 bytes, SHA-256 `d7bd716dcfa5ef640aabb824099ad614b4d64bfb781a3cbf4cc484bb8e902fbf`. Arrays `matrix (30,30)`, `edge_ids (30,)`, `eigenvalues (30,)`; reconstructed eig bounds approximately 0.14317415 and 1.10465934. This is the original archived matrix, not the candidate.

**Distinct candidate, NOT a replacement:** `m5_whitney_candidate_2026-10-30.npz`, 1,836 bytes, SHA-256 `55a0d1b731355b59d64ce5535d029913b72fe1bcea595e2375d1f90b98d47334`; eigenvalues approximately 0.19615504 to 2.27751671. R3-IR-537 mismatch remains a historical assembly prescription/reproducibility issue, not missing data.

All other data persisted in Library: `Archive 4.zip`, `Sharpe_dissertation_v10.7.tar.gz`, `penrose_seed101_stage26_full.zip`; `singular_boundary_handoff_full.zip`, `singular_boundary_handoff_core.zip`, `singular_boundary_handoff_core_R3-IR-539.zip`; for both penrose and square at seeds 101,211,307,419: `*_stage26.zip` and `*_sweep10000_multihit.npz`.

**Recovery procedure:**
1. List or search ChatGPT Library at `/The Singular Boundary/Source`.
2. Obtain `singular_boundary_source_manifest.json` from Library; it holds full exact hashes for all 24 archives.
3. Materialize only the required raw files in a new runtime.
4. Verify SHA-256 before loading; verify NPZ key names, array dimensions, edge order and SPD.
5. Read this repo's claims ledger and most recent theorem notes; distinguish source historical matrix and alternative candidate. Never push raw NPZ/ZIP/TAR.GZ to Git without approved LFS or another intentional binary-storage facility.
6. At each checkpoint, update Git with a **text-only** methods/results note and Library manifest with any new binary artifacts; make checkpoint/handoff independent of any single chat context.

**Research status:** R3-IR-537's mass assembly mismatch is not resolved by the appearance of this binary; it establishes availability of the original array for direct comparisons. Its original generating code/convention is still an independent question. No refinement-uniform center-cap theorem or continuum Yang–Mills mass gap is claimed.
