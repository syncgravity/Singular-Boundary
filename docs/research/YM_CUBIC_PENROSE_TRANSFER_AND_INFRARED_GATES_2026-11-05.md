# Constructive SU(2) Yang–Mills: cubical infrared obligations and transfer to quasicrystalline geometry

**Research audit, November 5, 2026.** Proposed theorem-integration and proof-hygiene record; **not a mass-gap theorem**. Independent review is required. This document is organized entirely around mathematical physics, models, proofs and missing hypotheses. Historical manuscripts remain immutable provenance, not graph labels or acceptance criteria.

## 1. Two questions must remain separate

**YM existence and mass gap.** Construct a nontrivial, reflection-positive/OS-reconstructible interacting 4D SU(2) theory whose physical Hamiltonian has a unique vacuum and `spec(H) subset {0} union [M,infinity)`, with `M>0` independent of lattice spacing and spatial volume. A proof on one cubic regulator alone would be a major mathematical objective. A regulator-independence theorem would still be required to identify the resulting theory on a different spatial model.

**Quasicrystalline spectral quantum gravity.** Define a mathematically and physically justified Penrose/Fibonacci/cut-and-project spectral operator and the gravitational fluctuation operator and measure. Test whether the spectral geometry changes ultraviolet behavior, and separately prove any claimed finiteness or renormalized limit. A cubic YM gap, even if proved, does **not** establish gravitational UV finiteness or the correct gravity dynamics.

**Model identities:** 2D Penrose/P3 and area-matched square are the authentic **2+1D SU(2) experimental comparison**; dyadically refining cubic three-space is a later **3+1D gauge control**; the proposed coupled-ℤ⁵ spatial/time construction and extruded 3D prism are independent hypotheses without proven regulator equivalence. Distinguish every source operator and limit.

## 2. Exact current status on cubic 3D (source audit)

- **R3-IR-586:** cubic oriented cellular complex, `∂₁∂₂=0`, `∂₂∂₃=0`, genuine fixed-domain dyadic refinement. **Geometric theorem only**.
- **R3-IR-587:** finite, open cubical original-link `SU(2)` Hilbert space `L²(SU(2)^E)^{SU(2)^V}`, closed positive electric form and bounded Wilson magnetic potential. **Finite quantum model**.
- **R3-IR-589:** the entire finite Gauss-invariant Hilbert space has an exact **free electric threshold** of 3 in the specified dimensionless Casimir normalization, and an interacting *sufficient* min–max lower bound. **Not uniform in h or volume**.
- **R3-IR-590 / later P0 audit:** finite symmetric positive heat-kernel transfer and its fixed-spatial-lattice Hamiltonian limit. The chosen anisotropic temporal heat-kernel action is **not proved equivalent to the isotropic 4D Wilson action** in the continuum.
- **R3-IR 3D Yarotsky audit:** an independent volume-uniform small-magnetic-coupling stability theorem applies to appropriate periodic cubic hypotheses only, with an unspecified positive small-coupling constant. **Its parameter regime is incompatible with the weak-bare-coupling limit needed for asymptotic freedom.**
- **P-77/P-78:** exact MPO, nuclear response and local spectral moment results apply to a separate straight-strip original-link model; they are **not yet the 3D interacting theorem**.

**Conclusion: the cubic mass-gap proof is not nearly complete.** The current cut set is (i) physical `g₀(h)` trajectory and uniform interacting construction, (ii) a renormalization mechanism controlling physical low energies at all scales and volumes, and (iii) a nontrivial 4D OS reconstruction with a dense set of gauge-invariant observables. No existing result on its own bridges these obligations.

## 3. Quantitative regime separation: a finite bound cannot be extrapolated

Take an open `n×n×n` cubical mesh of fixed physical side length one, `h=1/n`, `F=3n²(n+1)` elementary faces, with Casimir eigenvalues `j(j+1)`. The finite model has

```
K = [g₀²/(2h)] sum_e C_e
V = [2/(g₀² h)] sum_f (1 - 1/2 tr U_f).
```

By the original-link Gauss law, any nonconstant physical spin-network has a nonzero leafless spin subgraph, hence a cycle of at least four cubic edges and free electric energy at least `3 g₀²/(2h)`. Since `V>=0`, min–max gives `E₁(H)>=3g₀²/(2h)`. The Haar-constant trial vector has `E₀(H)<=2F/(g₀²h)` because the Haar expectation of a nontrivial plaquette character vanishes. Thus the repository's pre-existing finite estimate reads

```
Delta_n(H) >= [3g₀²/2 - 2F/g₀²]/h.
```

It is strictly positive by this certificate when

```
g₀^4 > 4F/3 = 4n²(n+1),
```

so `g₀ > [4n²(n+1)]^(1/4) ~ sqrt(2)n^(3/4)` as `n->infinity`. This certificate requires **increasing** bare coupling, not the `g₀(h)->0` expected in asymptotically free 4D Yang–Mills. It is a failure of **this sufficient lower bound**, not a theorem that the true gap vanishes. The independent weak-interaction periodic stability bound uses `z=4/g₀⁴` and `16|z|<βY`, again not the `z->infinity` continuum trajectory.

Exact-arithmetic cell counts and thresholds for `n=1,2,4,8,16,32,64` are reproduced by `research/scripts/verify_cubic_penrose_gate_boundaries_2026_11_05.py` and `docs/evidence/YM_CUBIC_PENROSE_GATE_CHECKS_2026-11-05.json`. They confirm known analytical inequalities, not an interacting spectrum computation.

## 4. Cubic-to-Penrose transfer: six independently checkable interfaces

**T0 — Physical 3D geometry:** supply a genuine fixed-volume refinement family of 3D *quasicrystalline* spatial complexes, with scale `h->0`, oriented incidence `∂∂=0`, controlled local geometry, boundary conventions, and honest identification with the intended model-set/hidden-coordinate construction. An extruded planar graph or formal `h=1/M` across fixed-size patches is not enough. A standard 3D Penrose analogue may require a distinct cut-and-project construction (for example higher-dimensional model sets); equivalence to coupled ℤ⁵ must be proved, not named.

**T1 — Gauss-invariant 3D action:** on each quasicrystalline mesh, define the original-link `SU(2)` physical space, local electric quadratic form, magnetic Wilson loops, reflection-compatible time transfer, and all geometric weights and adjoint transports from one consistent action. Compare domains and physical energy units with the cubic control. Naive holonomy subdivision does *not* intertwine bare Hamiltonians, as the existing P0 audit demonstrates.

**T2 — Renormalized observable dictionary:** specify a dense, gauge-invariant algebra of physically supported, suitably renormalized/smeared observables `F`; construct consistent `F_{h,R}^{cube}` and `F_{h,R}^{qc}`. Match their supports, symmetries, coupling scales, cutoffs and vacuum-centering conventions. Identical source IDs, matching graph areas or finite spectral moments are not sufficient.

**T3 — Uniform interacting comparison:** prove a scale/volume/time bound for the *actual interacting* connected positive-time self-correlations. For some common `M>0` and each physical `F`, a sufficient (very strong) condition is

```
0 <= C_cube,h,R^F(t) <= A_F exp(-M t),
|C_qc,h,R^F(t)-C_cube,h,R^F(t)| <= B_F exp(-M t),
```

with finite `A_F,B_F` **independent of h,R**, at all sufficiently large physical times `t`; any volume-dependent boundary errors need independent control. Then `C_qc,h,R^F(t) <= (A_F+B_F)exp(-Mt)`. This is an elementary implication, not an established correlation comparison. It is permissible that both theories have different UV quantities even if their infrared behavior matches; full universality is a stronger and separate claim.

**T4 — Nontrivial common-time continuum:** establish tightness/convergence of complete renormalized Euclidean Schwinger functions along compatible box, mesh and time limits, reflection positivity, covariance, clustering, and the appropriate OS reconstruction for the quasicrystalline model. Finite transfer positivity alone is not continuum OS construction. Show nonzero created states and density in the vacuum-orthogonal physical space; otherwise one cannot infer the gap for all physical excitations.

**T5 — Physical mass gap and independent gravity question:** apply the positive spectral-measure Laplace lemma to the dense set of continuum OS vectors, obtaining a mass gap `>=M` in fixed physical units (subject to vacuum isolation and nontriviality). Any quasicrystalline gravitational UV claim requires its own operator/spectral measure and a proved relation to a physically defined gravitational path integral. A YM gap never proves it by itself.

### Why an unweighted numerical comparison cannot carry a gap

Consider two positive Laplace-transform two-point functions, for `0<m<M` and any `0<η<1`:

```
C_cube(t) = exp(-Mt),
C_qc(t)   = (1-η) exp(-Mt) + η exp(-mt).
```

For **all** `t>=0`, `|C_qc(t)-C_cube(t)| <= η` (arbitrarily small in the usual uniform sup norm), yet the second positive spectral measure is `(1-η) δ_M + η δ_m`: its gap is `m`, not `M`. Therefore even uniformly small unweighted differences do **not** preserve the cubic gap. A large-time exponentially weighted comparison, or an independent spectral-exclusion argument, is essential. This counterexample is mathematical and model-agnostic; it is **not** a Penrose Yang–Mills correlation function.

## 5. Direct cubic gates to pursue without confusing the models

| Gate | Current rigor | Missing decisive certificate | May it transfer to quasicrystal? |
|---|---|---|---|
| P0 | Cubic 3D geometric h-refinement; finite SU(2) Hamiltonian/action | Physical coupling trajectory and one-action continuum regulator | Only after T0 and T1 |
| P1 | Finite Gauss-invariant original-link operators | Domain/scale compatibility, physical composite observables | T1 and T2 |
| P2 | Strip local analytic/MPO results, finite cubic interaction | Uniform 3D interacting multiscale construction on weak-bare-coupling path | A new locality/operator comparison; NOT automatic |
| P3 | Penrose-route signed-current candidates | Source-specific interacting 3D Wilson estimate | Route-specific; not mandatory for cubic YM |
| P4 | Finite cubic positive gap; strip spectral sum rules | Uniform physical-time IR exclusion and dense gauge-invariant probes | T2–T4 |
| P5 | Finite transfer positivity | Nontrivial 4D OS/Wightman construction and physical mass gap | T4–T5 |

**Near-term order:** (a) define a cubic multiscale observable whose physical diameter does not shrink with h; (b) prove the smallest nontrivial *interacting* renormalized two-scale estimate for that observable under the actual `g₀(h)` and geometry; (c) investigate whether the same observable/estimate survives a source-certified quasicrystalline 3D cell family; (d) build larger scales only after verifying uniform constants. A two-scale numerical match is evidence, not a mathematical conclusion. No timeframe to complete the mass-gap theorem is asserted.

## 6. Evidence discipline and publication-facing map

The interactive Observatory nodes now use mathematical-physics titles and claim-scoped explanatory summaries rather than source-document chapter numbers. Original papers, reports and data remain **provenance objects** with SHA-256 and immutable Library custody; their titles/files are not automatically theorem certificates. Unknown proof edges must have status `open`, `conditional` or `obstruction` rather than `proved`. Graph counters report curated records, **not** fractions of the final theorem proved. The user-editable review annotations never modify canonical theorem status. 740 historical theorem paths and 78 earlier candidate paths are separately preserved and cannot be silently recounted.

**Principal source paths:**
- `research/theorems/R3_FIXED_DOMAIN_CUBICAL_CHAIN_REFINEMENT_2026-10-31.md`
- `research/theorems/R3_CUBICAL_SU2_GAUSS_HAMILTONIAN_REFERENCE_2026-10-31.md`
- `research/theorems/R3_CUBICAL_SU2_FULL_PHYSICAL_STRONG_COUPLING_GAP_2026-10-31.md`
- `research/theorems/R3_CUBICAL_SU2_FINITE_TRANSFER_POSITIVITY_2026-10-31.md`
- `research/theorems/R3_IR_3D_QUANTITATIVE_THRESHOLD_AND_CONTINUUM_SCALING_AUDIT_2026-11-04.md`
- `research/audits/P0_CUBIC_HEAT_KERNEL_TRANSFER_CERTIFICATE_2026-11-04.md`
- `docs/research/UNIFORM_INTERACTING_THEOREM_BRIDGE_2026-11-04.md`
- `docs/research/P0_MODEL_HIERARCHY_PENROSE_CONTROL_AUDIT_2026-11-05.md`

**Status:** no Yang–Mills continuum mass-gap theorem, Penrose transfer theorem, or quantum-gravity finiteness theorem is claimed. No canonical main-branch promotion or public publication is authorized by this review draft.
