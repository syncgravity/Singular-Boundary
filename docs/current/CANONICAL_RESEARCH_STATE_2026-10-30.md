# Canonical research state — 2026-10-30

**Read this first.** Git `main` is the canonical research record. Conversational outputs and Library ZIPs are **sources to reconcile**, not authoritative proof or completed repository imports. The historical audit branch was fast-forwarded to main; 245 additional commits were preserved without rewriting existing history.

## What the repository currently proves or records

The original archived R3-PRISM, R3-IR, D1, R2 tracks remain logically distinct. The repository contains extensive original Stage 7–35 numerical/provenance audits, many finite-volume SU(2) theorems, counterexamples, and conditional comparison arguments. None constitutes a complete nonperturbative continuum Yang–Mills mass-gap proof. Read specific statements in `research/theorems/` and their corresponding entries in `research/claims/CLAIM_LEDGER.csv`; do not infer universal results from file titles alone.

The 2026-10-30 handoff's **CI-1/CI-2** (now `research/theorems/CONDITIONAL_HAAR_INCOMPLETE_CAGE_CI1_CI2_2026-10-30.md`) is an exact finite-volume result for *incomplete* cages: the deleted target trace is Haar and independent of retained traces; bounded retained components have a conditional defect bound of order (M b^{-1/2}). It does not apply to a completed connected magnetic cage. Its source companion scripts and certificates still require archival reconciliation.

The 2026-10-30 `COMPLETED_CAGE_CUT_COMPARISON_2026-10-30.md` proves a **small perturbation** comparison under (2sbc_r<\gamma_0), with rare-cap denominator loss. It does not cover generic strong-coupling completion.

A prior branch records an **exact** signed radial-score identity and a *sufficient conditional gate* for downstream comparisons:
[
\mathfrak T_{f,h}=\frac4{A_f}\int_0^{\pi/2}\frac{[-C_{f,h}(\cos u)]_+}{\sin u}\,du,
\qquad \sup_{f\in D_R}\mathfrak T_{f,h}=o(h^{-1/4}).
]
The uniform physical interacting-vacuum estimate on the right **is open**; neither a Gaussian sign, a harmonic argument, nor a spatially averaged defect bound closes it.

## Prioritized proof dependency map

1. **Completed-cage nonlinear target response:** derive an angle-uniform or suitable one-sided score-current bound for the actual Gauss-invariant Wilson vacuum, with the target-dependent kinetic metric, low collective energy and boundary/volume constants retained. No fast-mode gap may be presumed.
2. **Bulk comparison:** only after step 1, establish the declared magnetic-deletion/cap survival bounds and fixed-support Wilson-angle comparisons with full coefficients and uniformity.
3. **Connected correlations / R3-IR:** independently control the required source-inserted low-energy sector and connected covariance. The Oct 29 repository review identifies a different low-energy spectral response gate at cutoff (Lh^{-11/8}); it has NOT been proved equivalent to the radial-current gate. Track both.
4. **R3-PRISM:** source-locate the original twelve-prism insertion and complete its fixed/integrated-boundary comparison. Its logical connection to the Hamiltonian approach is not established.
5. **D1/R2 and reconstruction:** finish production-action normalization, physical temporal/spatial limits, positivity and continuum spectral reconstruction before any continuum mass-gap claim.

## The next proof experiment

On a minimal completed-cage original-link disk, formulate the target-angle conditional quadratic form and score-current Ward identity without taking positive parts prematurely. Compare cut/open and completed support as a *finite volume* theorem and quantify exactly where the global spectral-gap cut estimate fails. Attempt a local signed comparison with constants explicit in (h), component diameter, and boundary conditions. Run deterministic tests as diagnostics, not proofs. A viable proof must address arbitrarily large complete Penrose interiors.

## Repository integrity gaps (OPEN)

- Historical `README.md` and `docs/current/STATUS.md` were frozen at 2026-10-28 and should be read as historical snapshots, not the latest proof.
- Earlier review said 75 theorem reports and 67 audit scripts. The live 2026-10-30 tree has **85 theorem files and 79 scripts across the scripts subtree** (different counting scope); counts are provenance indicators, not proof certification.
- The repository is not the complete prepared 602-source import; historical source text, binary assets, and Oct 29–30 ZIP deliverables still need verified source-by-source reconciliation.
- Source `PROJECT_HANDOFF.md` refers to a full verification bundle, but its embedded tests/certificates have not all been checked against Git.
- ChatGPT cannot assume access to every chat in a Project. Only actually surfaced transcripts, Library materials, and mounted files can be inventoried. Missing histories must be marked unavailable, not silently reconstructed.

## Rules

Every new theorem must have a precise source, hypotheses, evidence status, and claim-ledger mapping. New research changes should be committed to `main`, verified by re-reading GitHub, and mentioned by full SHA. Preserve historical records; avoid destructive renames and force-pushes. For large binary data use an explicit archival transfer and compare byte hashes.
