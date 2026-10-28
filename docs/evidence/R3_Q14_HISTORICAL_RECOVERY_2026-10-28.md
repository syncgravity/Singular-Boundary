# R3-Q14 historical source recovered — 2026-10-28

**Read-only archive audit; no historical MCMC or source programs rerun.** Full report and original-byte excerpts are preserved in local handoff `singular_boundary_q14_recovery_checkpoint_2026_10_28.zip` (SHA-256 `c000b1fa56206a47e51dcac4285c32b57850d17cb6b13f41b7e562a698e6c5bf`). The eight uploaded ZIPs are not yet imported as GitHub blobs.

## Original construction actually located

`R3_recovered_original_2026_10_27_bundle.zip` contains `cavity_audit.py`, `verify_bianchi.py`, `construct_surgery.py`, `direct_cut_project.py`, and `HISTORICAL_Q14_CANONICAL.json` (the latter SHA-256 `bd9db7bb5bcfd03ecbbdea0f1204668fe5add1b4add967c09b6d365388f6d8c5`).

The historical Q14 is selected by three original spatial seed Penrose rhombi and their temporal edge-face supports in slabs 0 and 1 of a *three-periodic-time* direct-Z5 rhombus disk. It contains **14 inserted temporal faces Q**, **36 incident links H**, **62 retained faces touching H**, **54 retained Bianchi-fill faces**, with **10 fill faces outside the 62-face affected set**. The latter implies the earlier shortcut `F subset A(H)` was false.

The `R3_historical_wordlevel_2026_10_27_bundle.zip` file `historical_Q_labels.json` has SHA-256 `735c77f32b43808b9110a9e130a407b5c98a821cb1ee69a1dcc33db7d99583f0` and contains *exactly the same* 14 canonical temporal-slab/Z5-endpoint labels as the original canonical JSON. All four saved word certificates at radii 5, 6.5, 8 and 10 have valid hashes against their manifests. Their exact Q, H and Bianchi-fill lists equal the corresponding lists in `R3_Q14_full_cover_2026_10_27_bundle.zip`. The source scripts `cavity_audit.py`, `construct_surgery.py`, `verify_bianchi.py` and `direct_cut_project.py` also have identical SHA-256 bytes in the Q14-cover and original-recovery archives.

The original Q14 word-level H stars have **84** pair-staple words. The *different*, later selection of **40** cover links has **225** reduced pair-staple words, each of length six. These are different inventories, not a contradiction.

## Exact rational certificate independently checked

Each of the four full-cover JSON files contains a 54-by-101 face-link incidence matrix, 101 primal and 54 dual rational weights. Reading the stored witnesses, exact rational arithmetic verifies `M w >= 1`, `M^T y <= 1` and `sum w = sum y = 22` at all four radii. The optimal fractional-cover weight is **22**. Forty links have positive weights; their complete retained stars reach **103** faces, **49 outside** the 54-fill set.

Therefore the recorded SU(2) conditional Ward calculation gives
```
lambda E_R S_fill <= 33 + lambda sum_(40 cover links e) w_e E_R m_e.
```
The additive 33 is established; the staple-minimum expectation on the right is **not** controlled uniformly. The historical Bianchi record reports `S_Q <= 44 S_fill`, with a 14-face prism peeling and 54 retained faces. This review did not independently reconstruct every conjugated nonabelian based-group-word derivation; preserve it as a source-supplied mathematical certificate requiring full proof review.

The elementary 62-by-62 influence matrix has diagonal entries 1 (hence spectral radius at least one), and its saved spectral radius is approximately 4. **It does not close R3.** Neither the optimal cover nor 225 loop words imply Gibbs suppression on their own.

## Two archival false negatives now superseded

`R3_word_incidence_2026_10_28_bundle.zip` is an explicitly declared **illustrative** support, with Q14 but H35, A53 and unsuccessful simple peeling. Its face labels **differ** from the original (set symmetric difference eight). Do not substitute it.

`R3_incidence_forensic_2026_10_28.zip` and `R3_Penrose_contraction_next_bundle.zip` report the original Q14 missing in their respective sessions, because those sources were not mounted then. With this new upload, the source-absence assessment is superseded; their scientific cautions and conditional matrix criteria still hold.

## Distinction that remains unresolved

The historical Q14 is a **three-seed-rhombus / fourteen-temporal-face** source-defined insertion. It is *not shown identical* to the older separately described **four-spatial-face, three-step, twelve-prism / 37-independent-link** insertion. Exact correspondence, all fixed/integrated exterior boundary conventions, arbitrary-nonstationary Gibbs bounds and implications for Hamiltonian R3-IR remain **open**.

**Next:** import original Q14 source bytes; inspect full retained incidence for peelability without redoing MCMC; prove nonabelian loop inequalities with exterior leakage or an annealed correlated-Gibbs estimate. No mass-gap theorem is claimed.
