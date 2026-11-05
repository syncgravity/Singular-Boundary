# P0 model-identity correction — Penrose hypothesis, periodic controls, and independent proof obligations

**2026-11-05 (America/Denver) · Proposed research audit, NOT canonical theorem acceptance.**

## Executive decision

The dissertation's primary research hypothesis concerns **quasicrystalline spectral geometry**—Fibonacci/Penrose and the coupled-Z5 extension—and its proposed consequences for ultraviolet gravitational quantities. The original reference experiment uses a **periodic comparison**, while later authentic Stage26 archives compare **Penrose versus square** controls under source-recorded simulation settings. The independent 3D **cubic** SU(2) lattice is the control/reference **extension**, not a replacement, derivation, or proven universality class of the coupled-Z5 proposal.

Preserve two distinguishable mathematical end goals: (G) gravitational spectral/quantum consistency or finiteness according to the source papers, and (YM) nontrivial 4D SU(2) Yang–Mills with a positive continuum mass gap. Neither implies the other without additional theorems. Retain SU(2) operator advances as useful but model-qualified; do not silently port them to the Penrose/coupled-Z5 construction.

## Source-level record

**Dissertation original bundle:** `Sharpe_dissertation_v10.7.tar.gz` (Library `/The Singular Boundary/Data/Original Uploads/`). Paper PDFs were read from `delivery/papers/Paper_{1..4}/`; their SHA-256 identifiers are in `pairing_audit.json`.

- **Paper 1**, *Spectral Dimension Flow and Gravitational Finiteness on the Fibonacci Lattice and the Penrose Tiling*: the Fibonacci spectral structure, Penrose P3 pentagrid and graph Laplacian are used to model spectral-dimension reduction. The graph-Laplacian-to-gravitational-fluctuation-operator implication is not certified here.
- **Paper 2**, *The Gravitational Path Integral on the Penrose Lattice: From Z5 to Minkowski Spacetime via Lapidus Complex Dimensions*: proposes a coupled-Z5 decomposition and a 2D Penrose + compact-third-coordinate + imaginary-time interpretation; reports spectral-zeta ratio and 16.7% one-loop departure versus periodic comparison. This reported number belongs to the **paper's spectral-zeta experiment**, NOT the supplied Stage26 multihit sweeps. Derivation of a Lorentzian quantum gravity with correct dynamics remains open.
- **Paper 3**, *The J-Operator and the Hidden Domain*: develops a complex-structure/hidden-domain and boundary proposal. Kinematics are not an independently proven interacting gravity dynamics or Lorentz-covariant continuum limit.
- **Paper 4**, *Conformal Boundary and Cosmological Constant*: discusses finite-lattice spectral-zeta channels and an alternative spectral-triple regularization. A finite regularized model quantity is not equivalent to full gravitational-path-integral finiteness.
- **Paper 5** is preserved in the bundle and should remain in the full publication roadmap, but Papers 1–4 define the scope of this immediate P0 correction.

**Original comparison data:** eight `*_seed*_stage26.zip` compact archives, eight `*_seed*_sweep10000_multihit.npz` files (geometries Penrose/square, seeds 101/211/307/419), the `penrose_seed101_stage26_full.zip` archive, and `global_whitney_11face.npz`. These **are not the same experiment** as Paper 2's 16.7% ζ ratio. No exact physical-model or numerical provenance equivalence across them has been proven.

### Verified present-turn checks

The accompanying `verify_penrose_square_pairing.py` opened 8 `allow_pickle=False` sweep arrays, checked geometry/seed/sweep metadata, common lag values `[4,6,8,10]`, four 600-entry `direct` and `multihit` arrays per file and 600 2-component `dx` values, 8 compact ZIP CRCs, and matching **input Stage 9 checkpoint SHA-256 metadata** against each compact archive's `latest.json`. Latest-record hashes are different objects and not conflated. All 8 compact archive JSONs describe `initial_sweep=10000`, `sweep=12000`, and `observations=100`. The **input Stage 9 checkpoint** SHA differs between square and Penrose geometry, even for the same seed. The Stage 26 runner computes this field using `sha(a.checkpoint)`; it is NOT a Python code hash. Means across four seeds are recorded as **descriptive summaries only**; dependence, estimator definition, coupling calibration, and sampling uncertainty are not established. The archives are 2+1D SU(2) lattice gauge scalar-correlation measurements with two spatial coordinates and 20 temporal slices, as confirmed by the recovered Stage 26 README. They are NOT the graph-spectral-zeta experiment of Paper 2, and cannot demonstrate gravity finiteness or a continuum mass gap.


### Source recovery during this audit: actual Stage 26 runner located

The historical Git tree already preserves the **Stage 26 source code**, nested under `sources/historical/raw/Archive_4/Penrose_YM_Stage26_Outer_First_Connected_Scalar_Campaign.zip/__nested__/stage26_outer/`. This was missed in the first review. Confirmed Git blob IDs:

- `stage26_outer.py` — `95423cfc83ba4774e160ac1e3dadc1fa964eca25`;
- `README_STAGE26.md` — `b552b9b42024a0a4dd4d577afc7d4a53a4b2b120`;
- `stage26_manager.py` — `c8c0f5d30c6269d4a0c1fec10e371c7b61b3b0a4`;
- nested `stage7_checkpointed.py` — `6d1dda48efb0e23ec0d9af6f5a61db4414a09dfd`.

The Stage 26 runner uses `setup_geometry(kind,20,3.5)`, `stage7_checkpointed.sweep`, and `stage22_shifted`/`stage24_inner_diagnostics` imports. It defines `sourcehash=sha(a.checkpoint)` when initialized from the Stage 9 checkpoint, and propagates that value into the new snapshots and latest JSON. It is therefore **incorrect to interpret the matching `source_sha256` metadata as a digest of the Python generator**. The README describes 22,808 Penrose / 22,801 square spatial anchors, 20 temporal slices, 100 outer fields per each of 8 chains, and warns that inner replicas and shifted offsets must not be counted as independent outer chains. These are *2+1D SU(2) scalar Monte Carlo* records, not a reproducing computation of the Paper 2 ζ ratio or a three-dimensional spatial refinement.

**Geometry-control design also recovered:** nested `stage7_large_torus.py` (`c747ae3584148cc0f6e8907e529e6e742962194e`) explicitly calls `build_torus(55)` for the Penrose model-set torus and `square_torus(151,151, penrose_physical_area)` to produce an **area-matched square control**; the model uses `NT=20`, `BETA=3.5` and calibrates spatial/temporal coefficients with `quadratic_weights`. This is stronger provenance than generic same-shape arrays: the control was designed to match total physical area in this *finite 2+1D SU(2) experiment*. It does **not** establish matched graph Laplacian spectra, equal degrees of freedom, identical bare action under a universality theorem, or the 3D Penrose refinement. The historical files include a separate `stage22_shifted.py` slab sampler and `stage24_inner_diagnostics.py` (whose inner replicas are explicitly not independent outer samples).

**Updated status:** original Stage 26 runner **located and read**, source Git blob pinned; actual run environment and Stage 9 checkpoint bytes not all available in supplied uploads, so this does **not** certify an independent reproduction or source-runtime identity. The previous characterization of the code as not located is superseded. Prior review notes remain preserved as dated records.

## Repository drift observations (not retroactive disproof)

1. `main/README.md` leads with Yang–Mills and omits the Penrose-vs-square experiment as an organizing principle. The project may research both, but the dissertation cannot be represented as a cubic Yang–Mills dissertation.
2. `docs/research/PROOF_DEPENDENCIES.md` presents one P0 gate, which was interpreted as if a cubic subachievement could certify the Penrose geometry. Model-indexed certificates are required.
3. `docs/research/REPOSITORY_REVIEW_AND_P0_OBJECTIVE_2026-11-04.md` explicitly lists candidate choices A (coupled Z5), B (prism), C (cubic), but frames selecting **one** as an objective. The correct scope is two coordinated tracks and a comparison or proved coupling between them, with the **original source hypothesis remaining primary**.
4. In stacked private `observatory/knowledge-graph.json` v2.27-draft, `M-CUBIC` was listed first, P0 geometry as `met` on the basis of cubic-only evidence, `D-ARCHIVE` and `D-SWEEPS` were connected to `M-Z5` even though **both include square controls**, and `W-LFS` was rendered as a mathematical blocker. `R-INDEX` was also classified as a study on `M-CUBIC` despite being a model-independent catalog.
5. Work in draft PRs #55–#59 is source-preserved but not a proof-chain merger. No 3D Penrose original-link regulator, YM/grav operator equivalence, spectral-zeta universal result, or continuum gap has been obtained by the cubic calculations.

## Corrected research hierarchy and gate acceptance

**H · Historical spectral hypothesis (primary):** Fibonacci → 2D Penrose spectral dimension → coupled-Z5 hidden-domain proposal → explicit ultraviolet gravitational operator / regularized action. Qualitative and numerical claims must be verified in their own models.

**C2 · Periodic square control:** square graph and Stage26 simulation configuration, with independently sampled observables and algorithm provenance. Compare against Penrose under matching *specified* conditions, not assumed pairing of physical sites.

**C3 · Cubic 3D quantum control:** exact oriented refinement R3-IR-586, finite Gauss SU(2) R3-IR-587, finite transfer R3-IR-590, and conditional later heat-kernel action. Their mathematical status remains scoped **to cubic**, without Penrose derivation or continuum theorem.

**P0-H (Penrose source certification):** Recover exact original coupled-Z5 generator/selection rules, candidate 3D spatial interpretation, dynamic operator definition and actual sequence of refining oriented complexes; decide if product/compact coordinate, icosahedral Z6, or another 3D physical model is required. Show geometry, topology, mesh, gauge/grav operators and one-action temporal normalization. **OPEN.**

**P0-C (control certification):** Confirm periodic square and cubic benchmark within their own declared models; finite geometry and finite actions are real subachievements. **Cubic continuum closure OPEN.**

**P0-X (comparative bridge):** Establish matchable observables, normalizations, source-code provenance, scale definitions, finite-size effects and uncertainty. To transfer a theorem, prove the relevant operator, measure, or universality relation; agreement of plots or shared seed labels is not a bridge. **OPEN.**

**G (gravitational objective):** A physically justified interacting gravitational operator/path integral, control of divergences or a precise spectral-triple result, valid Lorentzian/Euclidean relation, and a nontrivial continuum statement as actually claimed. **OPEN.**

**YM (mass-gap objective):** Independently establish nontrivial 4D SU(2) continuum Yang–Mills and positive physical gap; optional Penrose Wilson-current route may be useful but requires P0 model compatibility. **OPEN.**

## Immediate work package (proceed, without overclaiming)

**X1 (completed here):** Machine-audit paired square/Penrose sweep metadata, common lags/array shapes, source hashes, compact archive CRC and paper provenance; record only descriptive outputs.

**X2 (partially advanced):** Recover exact generator lineage, source environment, dependency inputs and the historical graph Laplacian constructions; associate each experiment and reported spectral quantity with its actual operator. Avoid equating Stage26 correlations with Paper 2 spectral zeta results.

**X3:** Reproduce the periodic-vs-Penrose *same observable* test (e.g. heat-kernel trace / spectral-dimension flow or spectral zeta) with matched physical normalization, finite-size controlled uncertainty, and rigorous operators. This is the first scientifically meaningful comparison gate.

**X4:** Derive or falsify a directly source-compatible 3D coupled-Z5 spatial refinement and correctly gauge/grav-covariant 3+1D action; document obstacles if unattainable. Use cubic 3D as a quantitative control, not a substitute.

**X5:** Only once X3/X4 are source-certified transfer interacting estimates and continuum claims with an explicit equivalence/approximation theorem.

## Governance

This is a reclassification audit, not a new physical proof. Original documents, numerical files, prior statuses and the old main Observatory catalog remain immutable. The new draft graph adds model-separated nodes and source edges. No Git LFS modification or public Pages deployment. Any closure claim needs independent mathematical review under the existing acceptance gate. Data files reside in ChatGPT Library; Git contains only hash manifests, tests and reports.
