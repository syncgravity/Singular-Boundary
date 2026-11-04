# Observatory historical-source double investigation — 2026-11-04

**Purpose:** distinguish source-derived historical evidence from current theorem certification, and provide the v0.2 research-map source annotations.

## Pass A — uploaded primary materials (local runtime)

- Inspected four large supplied conversation Markdown transcripts by heading range and latest checkpoints. These overlap substantially; textual duplication is not independent corroboration.
- Opened the compressed `Sharpe_dissertation_v10.7.tar.gz`; its primary dissertation PDF is **23 pages**, titled *The Singular Boundary: Quasicrystalline Geometry from the Planck Scale to Consciousness*, draft dated March 8, 2026. This predates the October–November physical original-link corrections and is **not** automatically equivalent to the later construction.
- Inspected eight Stage 26 checkpoint ZIPs: four Penrose and four square, seeds 101, 211, 307, 419. Each has **100 NPZ checkpoints**, total **800**. In each ZIP the final `latest.json` `record_sha256` matches the exact archived last record bytes (8/8).
- Inspected eight `*_sweep10000_multihit.npz` files, with seed, geometry, sweep=10000, and `source_checkpoint_sha256` fields; each source hash prefix and full scalar value matches the respective run manifest's `source_sha256` (8/8). Data arrays were loadable and the tested direct/multihit values finite.
- The Penrose seed 101 full ZIP carries a large restart NPZ beyond its 100 checkpoints. It was not promoted to independently certified model incidence.

**Scope:** These are checks of archived structure, hash linkage, and limited numerical representation; not full replay of simulation, source-catalog byte recovery, 3D geometry certification, or proof of continuum gap.

## Pass B — GitHub research and discrepancy audit

Compared Pass A with canonical `README.md`, `docs/research/CURRENT_CHECKPOINT.md`, `docs/research/PROOF_DEPENDENCIES.md`, `docs/research/REPOSITORY_REVIEW_AND_P0_OBJECTIVE_2026-11-04.md`, `docs/research/EVIDENCE_PROTOCOL.md`, `docs/research/BRANCH_CONSOLIDATION_COMPLETED_2026-11-04.md`, and selected theorem bodies.

1. Theorem index now covers **740** Markdown theorem paths after incorporation of 202 previously branch-only theorem paths. Source path inventory is not an independent audit of all 740 bodies.
2. All ten historical branch heads are ancestors of main, but historical claim collisions (notably `R3-IR-373`–`390`) and missing original-byte custody remain unresolved.
3. Corrected original-link physical operators must not inherit older face-reduced results without explicit orientation and normalization checks.
4. The weak-magnetic volume-uniform gap theorem is a legitimate finite-volume route *under the imported stability hypotheses*, but in 3+1D KS units `z=4/g_0^4` diverges as the asymptotically free bare coupling vanishes. Hence that theorem cannot directly close the continuum gap.
5. The fixed-domain cubic family supplies a genuine geometric refinement control, while the six nominally refining prism candidates retain roughly constant numbers of edges; neither fact establishes a source-certified Penrose 3D regulator.
6. Connected-history fusion must retain physically nontrivial disconnected-support output; a naive quotient fails. The anchored full-Wigner same-weight norm has an explicit high-spin counterexample, which cannot be promoted to a no-go result for the Gauss-invariant sector.
7. The Penrose signed-current bound is a *sufficient proposed route*, not necessary for every possible proof; the true interacting-vacuum estimate remains open.

## Research decision and restrictions

Treat P0 regulator identity and action-coherent refinement as the first unresolved scientific acceptance gate. Use the Observatory to target nonduplicative dependencies; do not claim any current record proves a nontrivial four-dimensional SU(2) continuum mass gap. Preserve countermodels, contradicted historical formulas, and source-qualified claim IDs.

**What was not done:** no full equation-by-equation review of 740 theorem bodies, no complete dissertation mathematical audit, no Monte Carlo replay, no independent verification of all raw source bytes, and no external peer review.

**Repository baseline:** `main` tree `fd1c1c1c8db078f8ec9d591d182059bd1635b164`; Observatory draft branch `feature/research-observatory-2026-11-04`.
