# The Singular Boundary — Publication proof map and readiness gate

**Audit date:** 2026-11-01. **Classification:** repository-wide research audit, NOT a completed Yang–Mills mass-gap proof.

## Scope
The canonical `research/claims/CLAIM_LEDGER.csv` contained **417 claim rows** when reviewed; 109 distinct direct `research/theorems/*.md` references were successfully retrieved and their scopes reviewed. Other referenced historical ZIP archives, scripts, files and provenance chains have not all been independently rerun or reproduced. Rows represent heterogeneous claims, not 417 proven independent theorems. Historical duplicate identifiers include R3-IR-378/379/380; retain aliases and audit history, rather than overwrite them.

## Dependency map

**P0 model/provenance:** Canonical original-link SU(2) Hamiltonian, gauge projection, link orientation, face/temporal Q14 identification, source normalization, mesh scaling, boundaries and Stage7/26 provenance. The three-rhombus spatial fixture is not the complete temporal Q14 nor automatically the older 12-prism/37-link geometry. **Open full identification.**

**P1 operator consistency:** Earlier two-face fourth-order operator has `Gamma(a,b)=(r-ab)/4`, `Kr=9r/2`; later three-face quadratic audit has `Gamma(a,b)=(ab-r)/4`, `Kr=15r/2`. Under identical coordinates, weights, and embeddings they contradict. The log-wavefunction convention `S=log Omega` versus `S=log Omega^2` also changes Riccati factors. Build one original-link quaternion differentiator and audit 1–4 face restrictions before using signed fourth-order cancellations. **Blocking reconciliation.**

**P2 formal linked-score:** Ordered interaction trees, finite Haar interval-hull projectors and constant-invariant-field commutator identities are proved within stated scope. The earlier all-order formal connected Gevrey-8 theorem is sharpened to Gevrey-3 and Gevrey-2, *conditional on the inherited connected recurrence/model assumptions*. Positive scalar Gevrey-2 optimality says nothing about actual signed-coefficient divergence. **No lambda=1 convergence or interacting gap proved.**

**P3 Penrose radial-current and deletion:** Finite nonlinear radial score Ward identities and conditional center-cap comparisons are established. Required uniform cycle-rich, reflection-free deleted-vacuum signed current `sup_f T_{f,h}=o(h^{-1/4})` (or a quantitatively sufficient replacement) is **open**; finite/symmetric/annular and Fisher bounds do not imply it. Even its closure would not alone establish a physical temporal gap.

**P4 physical source-visible temporal spectral channel:** Finite-temperature linked polymers, finite spectral and Euclidean cumulant identities, fixed-face strong-field gaps and several Ward/moment estimates are established in restricted settings. Missing: zero-temperature, Gauss-projected, regulator/volume uniform interacting source estimates; composite/multi-trace completeness; nonzero continuum spectral weight; a genuinely positive physical low-energy spectral threshold, without inserting the gap as a hypothesis. **Open.**

**P5 R2 continuum reconstruction:** independent volume/refinement bounds, nontrivial gauge-invariant observables, reflection positivity/OS construction, continuum dynamics and positive spectral gap transfer. **Open**; the 2+1D work must not be represented as a 3+1D Clay Yang–Mills solution.

### Noncircular dependencies
```
P0 --> P1 --> corrected finite scores --> physical-coupling majorant (open)
 |--> P3 signed current --> bulk deletion --> fixed-support covariance (open)
 |--> P4 source-inserted dynamics --> physical spectral threshold (open)
All necessary physical controls + regulator limits + continuum reconstruction --> P5 (open)
```
The radial-current condition is sufficient within one chosen approach, not universally necessary for a gap. A Gevrey bound on formal connected coefficients is not a continuum convergence theorem.

## Publication actions
1. Add a canonical physical-operator specification and exact cross-volume quaternion derivative verifier. Preserve incompatible prior files; attach explicit errata and dependency statuses.
2. Add unique immutable claim ID/alias table, assumption/source/model-scope fields and per-claim proof dependencies, with change log; flag contradictory score-theorem pairs.
3. Separate full-link finite-temperature statements from Gauss-projected zero-temperature dynamics, fixed-volume results from regulator-uniform statements, and conditional bridges from proved physical estimates.
4. Audit Stage7/26 normalization, Penrose spatial vs temporal Q14 vs historical 12-prism provenance and archived checksums.
5. Commission an independent proof and reproducibility review before publishing any mass-gap conclusion.
6. Publish scoped finite-model results as such; do not describe overall continuum gap as proved or almost solved.

## Research verdict
The finite mathematics and auditable source corpus are substantial, but the repository does **not** currently prove a nontrivial interacting Yang–Mills continuum mass gap. The immediate blocking publication task is P1 cross-volume physical-operator reconciliation, followed by the independent full-coupling/current, physical-time spectral, and continuum reconstruction obligations. This is an audit and dependency map, not a mass-gap theorem.

**Companion full report:** `SINGULAR_BOUNDARY_PUBLICATION_PROOF_MAP_2026-11-01.md` in persistent Library, `/The Singular Boundary/Proof Audits/`. The full report contains detailed theorem families, proof-gate map, repository editing protocol, source-review limits and publication sequence.