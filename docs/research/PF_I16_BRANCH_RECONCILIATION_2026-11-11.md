# PF-I16 branch reconciliation and proof-frontier review

**Review date:** 2026-11-11  
**Reviewed source branch:** `audit/pf-i16-local-interacting-vacuum-2026-11-08`  
**Integration destination:** `architecture/source-compatible-spectral-spine-2026-11-11`  
**Status:** research contribution and proof limitations identified; source files remain to be imported and independently replayed before the integration PR is merged. This note is not a theorem certification.

## 1. Why the branch is not merged wholesale

The PF-I16 branch is divergent from `main`: 53 commits ahead and 138 behind, with 46 branch-only files (26 research reports, 17 scripts, and 3 later theorem/verification files; exact path inventory is the compare result). A merge of its historical commit chain would pull in a stale ancestor history and risk reintroducing old generated files and superseded statements. The safe operation is content-level reconciliation onto the current architecture branch, preserving every distinct report and verifier while correcting superseded claims.

The branch is scientifically material and must not be discarded. Its work is on the authentic five-direction accepted [0m\(\mathbb Z^5\) Penrose–Fibonacci rhombus complex and original-link SU(2) variables, with explicitly chosen auxiliary electric and magnetic coefficients. It is not a source-derived physical Hamiltonian or time normalization.

## 2. Contributions that survive the review

### Exact finite-source results

1. **Independent face-center sign duality.** Free-face collapse to a graph gives the stated finite-complex surjectivity of the mod-2 face coboundary. Central link translations implement arbitrary independent face-sign flips, so the centered finite ground-energy germ is even separately in each face coupling. This removes every monomial with an odd exponent in any face coupling. It is a parameter duality, not a fixed-coupling gauge symmetry.

2. **Exact low-order connected energy.** For a genuine pair of accepted rhombi sharing one original link, the unit-auxiliary-coefficient mixed quartic coefficient is (-1/8424). The two-face sixth-order mixed coefficient is recorded and independently checked in the source dossier. For the authenticated three-face trivalent motif, the first fully linked coefficient is
   [
   C_{222}=-4909/7569469440.
   ]
   It is obtained from exact original-link SU(2) recoupling / Haar-Poisson calculations and reproduced in two spanning-tree gauges. A distinct four-valent motif has the same sixth-order (C_{222}); the first reported distinction between these two motifs occurs at eighth order. These are finite auxiliary Hamiltonian coefficients with all exterior face couplings set to zero when extracting the stated multivariate coefficient.

3. **Four-face finite-support results.** The Ngrid=7 connected four-face census reports 18,900 supports in seven marked graph classes. Exact representative (C_{2222}) coefficients and an aggregate for that archived crop are reported. The report itself records an important qualification: the aggregate is conditional on representative coefficient transport across every support; the earlier full decorated-isomorphism pass did not complete for every one of the 18,900 supports. The later seven-class audit claims a completed marked-isomorphism certificate, but explicitly does not freshly rerun the private SHA-pinned source generator. Preserve the result as a finite Ngrid=7 result with its inherited source provenance, not as a refinement-uniform theorem.

4. **Electric spectral and local-response results.** The branch establishes finite-source electric inverse bounds and exact one-loop / two-loop spin-network spectral facts. It also establishes a local (L^2) conditional regularity bound for (K^{-1}P_0\Gamma_K(F,G)) in terms of (D_4(F)D_4(G)). These do not give the corresponding (D_4) bound on the output.

5. **Exact one-face dressing identity.** Allocating each original-link electric coefficient among its incident faces yields an exact ground-state conjugation identity. The residual is supported only on links shared by at least two accepted faces; a degree-one face link contributes zero residual. The stated support and norm estimates are conditional on a uniform isolated-face derivative bound. The note does not prove that derivative/Hessian estimate or the subsequent dressed-diffusion Poincaré and residual-stability steps.

6. **Explicit infrared obstruction.** A smooth positive finite-rhombus countermodel shows that bounded local kinetic energy / conditional information alone does not force a Poincaré gap. A separate exact finite auxiliary potential realizes arbitrarily small gaps, but its potential is not the fixed bounded-coefficient Wilson potential; it is a proof-strategy counterexample, not a counterexample to the target Wilson model.

### Valuable negative results

- The inverse electric operator is not Hilbert–Schmidt on the authenticated three-face motif (threshold (p>3)); on the seven four-face classes the threshold is (p>9/2). Therefore the earlier two-face Hilbert–Schmidt inversion cannot simply be iterated to larger clusters.
- A direct (D_4\times D_4\to D_4) nonlinear estimate fails on one fixed authentic three-face source graph by a local concentration/scaling argument. This blocks that proposed iterative proof route; it does not imply divergence of the true perturbation series or a gapless interacting vacuum.
- The fixed-support Cauchy estimate grows like (k^{2k}), so combining it with exponential connected-support counting does not produce a convergent polymer expansion. Its failure is a limitation of the estimate, not proof of divergence of the actual expansion.
- The exact one-loop (L^1\to L^2) convolution estimate does not extend unchanged to two independent holonomies. This is distinct from the gauge-invariant two-rhombus theta-graph Hilbert–Schmidt result; the two operator statements are not contradictory.

## 3. Incidence correction — supersedes the optimistic degree-four generalization

The 2026-11-10 correction is the governing statement for source-uniform counting:

- The elementary five-direction inventory gives at most **eight candidate coordinate rhombi per original link**.
- Eight explicitly replayed finite crops show no edge with more than two accepted-face incidences. That is a finite-crop observation, not yet a theorem for every source region/refinement.
- Without a proof of the stronger all-source acceptance fact, the universal face-overlap graph degree bound is
  [
  \Delta\le 4(8-1)=28,
  ]
  and the safe rooted connected-support count is (784^{k-1}), not (16^{k-1}).
- The geometric-series implication is conditional on a separate quantum activity estimate (|\zeta_G(S)|\le A q^{|S|}); with the safe count it requires (784q<1). No such uniform activity estimate is proved.

Accordingly, the earlier `PF_I16_UNIFORM_CONNECTED_CYCLE_MIXING_GATE_2026_11_10.md` statement using a universal degree-four bound must be marked **superseded in its incidence input** by `PF_I16_CONNECTED_SUPPORT_INCIDENCE_CORRECTION_2026_11_10.md`. Its conditional combinatorial argument remains valid if the stronger degree-four hypothesis is separately established; it cannot be used as the general source-volume bound today.

## 4. Exact dressing is a promising route, not a completed gap proof

The shared-link residual construction is the strongest late-stage structural advance: repeated insertions confined to a single face are absorbed into an exact isolated-face ground state, leaving a quadratic-order residual only on shared links. Its useful bounds rely on a one-face derivative estimate (|\nabla s_f|_\infty\le C_1 b_f/A_f). The report explicitly leaves open:
1. a uniform isolated-face derivative/Hessian estimate;
2. a volume-uniform curvature/Poincaré estimate for the dressed diffusion;
3. local-potential stability / connected-cumulant control for the extensive residual family.

A global Kato norm of the extensive residual is not an acceptable substitute. The D4 noniterability theorem also means a naive repetition of the earlier (D_4) estimate cannot close item 1 or 3.

## 5. Reproducibility and source qualifications

The branch contains 17 executable Python verifiers across `research/scripts/` and `research/verification/`. Their reports describe exact rational / symbolic identities, finite enumerations, and numerical corroborations. The present review has inspected the source reports and their declared verification scope; it has **not yet rerun all 17 scripts from a clean environment**. The private original generator `paper6_extend_local.py` remains outside the public repository; PF-I9's recovered copy is hash-pinned in the prior source audit, but a hash is not source publication or independent re-execution.

No source file in this branch should be described as independently source-certified beyond the exact crop and provenance scope its own report states. No finite coefficient, local estimate, or conditional reference bound closes the physical refinement, interacting-vacuum, uniform Poincaré, infrared, or continuum gate.

## 6. Canonical disposition for mainline

**Preserve and integrate:** all distinct PF-I16 reports and verifiers, retaining their auxiliary-model labels, source witnesses, exact coefficients, and negative results.

**Correct during integration:** use the conservative incidence correction; annotate the earlier degree-four theorem accordingly; retain the incomplete four-face census caveat wherever the seven-class result is summarized; retain the distinction between one-loop convolution, two-loop Hilbert–Schmidt, and multi-loop noniterability.

**Do not promote:** any physical kinetic/time normalization, all-orders cluster convergence, interacting Poincaré inequality, uniform infrared gap, continuum/OS reconstruction, or four-dimensional Yang–Mills mass gap.

**Next mathematical gate:** prove a source-volume-uniform iterable weighted-resolvent / local polymer estimate for the dressed shared-link residual, controlling the full SU(2) Peter–Weyl tower and preserving connected cancellations. In parallel, the source-authenticated physical observer/real-time structure and regulator refinement must be resolved; PF-I16 does not supply those missing S0/S1 inputs.

## 7. Branch-only source inventory

The branch-only content consists of the following reports and executable checks (preserve exact paths when importing):

- `research/geometry/PF_I16_*.md` — finite source geometry, exact low-order linked coefficients, motif topology, Schatten thresholds, high-spin/resolvent analysis, information bounds, and infrared gates.
- `research/theorems/PF_I16_CONNECTED_SUPPORT_INCIDENCE_CORRECTION_2026_11_10.md`
- `research/theorems/PF_I16_LOCAL_DRESSING_SHARED_LINK_RESIDUAL_2026_11_10.md`
- `research/theorems/PF_I16_UNIFORM_CONNECTED_CYCLE_MIXING_GATE_2026_11_10.md`
- `research/scripts/verify_pf_i16_*.py`
- `research/verification/verify_pf_i16_*.py`

The complete exact file list remains available from the Git comparison of the named source branch against main; no file is to be dropped merely because it is a verifier, a negative result, or a finite auxiliary calculation.
