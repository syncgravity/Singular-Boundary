# R3-IR — Exact reflection-sector cancellation of a physical Wilson three-source response

**Date:** 2026-10-28. **Research type:** independently checked finite-graph nonlinear SU(2) selection theorem, authentic canonical three-rhombus Penrose seed automorphism, sharp abstract response-spike obstruction, and conditional second-response criterion. **Does not close the general Penrose low/intermediate spectral-window estimate or the physical mass gap.** No Monte Carlo was performed.

## Provenance and limited claim

The input theorem notes were read from the current repository audit branch, notably `R3_IR_THREE_SOURCE_ENERGY_WINDOW_2026-10-28.md` (EW-1/EW-2), `R3_IR_REFINED_CURVATURE_WEIGHTED_ALIGNED_RESPONSE_2026-10-28.md` (RR), `R3_IR_CURVATURE_WEIGHTED_FSUM_2026-10-28.md` (FS), and `R3_IR_MESOSCOPIC_INTERIOR_CURVATURE_2026-10-28.md` (MI). The three-rhombus canonical seed labels were inspected directly through the historical fixture preserved in the project. The original Stage 7/Stage 26 coefficient identification is **still not fully independently authenticated**.

We do not treat a mirror symmetry of the three-face seed as a symmetry of a generic finite Penrose patch or its exterior. All claims requiring symmetry assume explicit coefficient invariance on the exact graph being studied.

## SC-1. An exact involution-sector nonlinear response theorem

Let G be a finite connected oriented spatial gauge graph; let r be an involutive graph automorphism taking oriented edges to oriented edges or their inverses and permuting the set of Wilson faces. Consider

`H=Σ_e a_e(-Δ_e)+Σ_f b_f(1−p(W_f))`

on the full link L²(SU(2)^E), with `a_e>0`, `b_f≥0`, and reflection-symmetric coefficients `a_{r(e)}=a_e`, `b_{r(f)}=b_f`. The gauge-invariant physical subspace is preserved. The induced unitary `R` is a permutation/inversion of link coordinates; Haar and the SU(2) Casimir are invariant. Reflection reverses some Wilson face orientations, but `p(U^{-1})=p(U)` for SU(2), hence `[R,H]=0`.

At finite volume the heat kernel is positivity improving; the ground Ω is simple, strictly positive and even under R. Put `K=H−E0`, `Q=I−|Ω><Ω|`. Let A be any bounded real gauge-invariant multiplication observable odd under reflection: `RAR^{-1}=−A`. In particular `<Ω,AΩ>=0` and `QAΩ` is odd. Conversely `Q A²Ω` is even. Since the spectral projectors `P_I(K)` and the vacuum-orthogonal inverse `K^{-1}Q` commute with R, their odd/even sectors are orthogonal. Therefore, for **every Borel spectral window** I contained in positive energy,

**`<Q A²Ω, K^{-1}P_I(K) QAΩ> = 0`.**

This is exact for arbitrary positive finite couplings, arbitrary finite graph size, and for I=[0,Λ], I=(Λ,∞), or the full positive spectrum. It does **not** assume spectral mixing, Gaussian approximation, or a regulator-uniform gap. It is a *symmetry-sector cancellation at one symmetric coupling*, not an estimate for general observables.

If `H(t)=H+tV` is a source-aligned family with `RVR^{-1}=−V`, then `RH(t)R^{-1}=H(−t)`. The vacuum variance of A obeys `V_A(t)=V_A(−t)` and `V_A'(0)=0`. The symmetry is broken for t≠0, so no smallness over a fixed interval follows from the selection rule.

## SC-2. Authenticate the reflection on the original three-rhombus canonical seed

Use the common Z⁵ vertex label `z=(-1,-1,-1,-1,-1)` and its coordinate unit vectors `e_0,...,e_4`. The three recovered faces are:

- `f0`: `[z,z+e0,z+e3,z+e0+e3]`;
- `f1`: `[z,z+e2,z+e3,z+e2+e3]`;
- `f2`: `[z,z+e0,z+e1,z+e0+e1]`.

The coordinate permutation `r=(0 3)(1 2)` with `4` fixed maps `f0` to itself and interchanges `f1,f2`. It preserves the ten-edge canonical Z⁵ graph exactly, as the deterministic verifier checks. Under the standard five-direction planar projection `u_i=(cos(2πi/5),sin(2πi/5))`, it is the Euclidean reflection across the axis at 108 degrees. The two exchanged rhombi have equal thick area factor sin(2π/5). The fixed center face has thin factor sin(π/5). The graph therefore admits a *reflection-symmetric Wilson Hamiltonian* whenever coefficients on the induced edge and face orbits agree. The source

**`A=p_{f1}−p_{f2}`**

is gauge invariant and exactly odd; SC-1 proves its complete three-source response is zero at the symmetric physical coupling. The result is an authentic finite three-seed geometry computation, **not** an authentication of original temporal Q14, nor a claim that the entire Stage 26 simulation graph has this involution.

## SC-3. Conditional fivefold-symmetry generalization

If a finite Penrose patch and its Wilson coefficients are invariant under a genuine order-five rotation `R5`, let A be a real component of a pure two-dimensional C5 character sector of nonzero charge k=1 or k=2 (e.g. orbit weights `cos(2πkj/5)`). The complex charges in AΩ are ±k. Those in A²Ω are 0,±2k. Since neither ±2k nor 0 equals ±k mod 5, the two subspaces are orthogonal under K^{-1}P_I; the same **exact zero** follows for the full and every projected three-source response at the symmetric point. No assertion that the original Penrose Q14 supports a global C5 automorphism is made. This is geometric symmetry plus dynamics-preserving intertwining, *not* an excitation-gap result from C5 alone.

## SC-4. Exact obstruction: even variance at the physical point may still form a sharp spike

Consider the strictly positive, real, two-state Hamiltonian on C²

`H_h(t)=δ(I−σ_x)+K_h(I+tσ_z),  |t|≤1,  δ>0`, `K_h=h^(−5/2)`.

Both summands are positive semidefinite. With reflection unitary R=σ_x, `RH(t)R=H(−t)` and the fixed source `A=−σ_z` is odd. The simple ground has gap `Δ_h(t)=2sqrt(δ²+K_h²t²)≥2δ`, uniformly positive. The source is exactly aligned with the deformation for α=3/2: `A=−h^(5/2) ∂_tH_h`.

The exact variance and first energy moment are

`V_h(t)=δ²/(δ²+K_h²t²)`,
`M1_h(t)=2δ²/sqrt(δ²+K_h²t²)≤2δ`.

Thus `V_h(0)=1`, `V_h'(0)=0` and **the entire projected three-source inverse-energy response vanishes at t=0**, consistently with SC-1. Nonetheless at `t_h=δ/K_h=δh^(5/2)` the physical excitation energy is `2sqrt(2)δ`, inside any window `[0,h^(−1−ε)]` for small h, while the exact source-response is

**`R_{2,≤h^(−1−ε)}(t_h)=−1/(4δ)`**

for small h. It is not `o(h^(1/2))`. The integrated squared variance is asymptotic to `(πδ/2)h^(5/2)` over any fixed symmetric interval, consistent with the nonlinear SU(2) *upper* bound `O(h²)` but without satisfying the actual model. The second derivative at zero is `V_h''(0)=−2δ^(−2)h^(−5)`. This is an **abstract finite-dimensional obstruction**, not a Penrose gauge model. It certifies that a symmetric-point exact cancellation, a uniform spectral gap, positivity, and the available first-moment/integrated-response bounds do not prove the required **uniform-in-t** response control.

## SC-5. Conditional second-derivative criterion for reflection-odd sources

Let V_h(t)≥0 be C² on `[-τ,τ]`, with `V_h'(0)=0`, and let `I_h=∫V_h(t)²dt ≤C h^p`, p>0. Write `v=V_h(0)` and `M_h=sup_{|t|≤τ}|V_h''(t)|`. Taylor's theorem implies `V_h(t)≥v−M_ht²/2`. On the interval `|t|≤r=min(τ,sqrt(v/M_h))` (taking r=τ if M_h=0), `V_h(t)≥v/2`, hence

`I_h≥(v²/2)min(τ,sqrt(v/M_h))`.

Consequently, **if `M_h=o(h^(−2p))`, then `V_h(0)→0`**. Equivalently, persistent `V_h(0)≥v0>0` forces `M_h=Ω(h^(−2p))` when h is sufficiently small. For the α=3/2 variance family, `p=2`, so the sufficient second-response criterion is

**`sup_{|t|≤τ}|V_{h,3/2}''(t)|=o(h^(−4))` (OPEN for the nonlinear SU(2) model).**

The two-state witness has `V''(0)=−2δ^(−2)h^(−5)`, so it is consistent with this threshold. Requiring uniform `V''` is **not** a substitute for proof: higher derivatives contain further inverse-energy connected source terms; the criterion remains conditional.

## Evidence and next obligation

- **Independently proved**: SC-1 parity-sector source-response identity, SC-2 canonical 3-face Z⁵ reflection automorphism, SC-4 exact two-state obstruction, SC-5 mathematical implication.
- **Conditionally proved**: SC-3 C5 case only when an actual finite graph and coefficients admit the named rotation, and physical alpha=3/2 variance collapse if the SC-5 second-response bound is *independently* established.
- **Open**: generic Penrose nonlinear low/intermediate three-source response uniformly for |t|≤τ, response at nonsymmetric physical sources and nonsymmetric graph boundary conditions, the nonlinear field variance, positive physical mass gap, and quantum continuum.

**Research priority:** symmetry decomposes the nonlinear physical Hilbert space into exact response-selection sectors, but a generic model-derived bound on the *even and mixed sectors* or a uniform coupling response remains necessary. A legitimate next certificate should analyze the symmetry-even source or the first nonzero even derivative in a **physically regularized finite Penrose family**, without importing gap-strength decay. The answer cannot be inferred from the C5/J geometric covariance alone.