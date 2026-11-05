# The Singular Boundary — P0 cubic transfer-action certificate and shortest-route audit

**Research date:** November 4, 2026 (America/Denver). **Scope:** one explicit, independently checkable *finite-spatial-regulator* cubic SU(2) construction and a proof-strategy decision. **Overall P0: OPEN. Four-dimensional continuum Yang–Mills existence/mass gap: OPEN.** This is a candidate lattice regularization, not a new solution or a claim of priority for established lattice-gauge transfer constructions.

## 1. The shortest *defensible* target path, as opposed to a guaranteed proof method

The Proof Atlas exposes a small logical cut set: **(A)** one genuine 3D spatial refinement family and action, **(B)** nonperturbative control of the interacting vacuum, Schwinger functions and a *common low-energy exclusion estimate* along its physical bare-coupling trajectory, and **(C)** a nontrivial 4D OS/physical reconstruction. In addition, all intermediate estimates must refer to the **same gauge-invariant observable algebra, normalization, volume/refinement limits, and model**. This is a sufficient architecture, not a proof that a method for (B) exists.

- **Model decision:** use the existing exact cubic refinement (R3-IR-586) and finite SU(2) original-link Hamiltonian (R3-IR-587) as the primary proof benchmark. The historical coupled-Z5, extruded prism and 1D strip are independent, optionally useful comparison/lemma laboratories. A Penrose–cubic equivalence theorem and the Penrose-specific P3 signed-current mechanism are **not universal prerequisites** for a cubic SU(2) construction.
- **Immediate finite P0 subcertificate:** explicitly select a single local Euclidean time-slice action whose transfer generates the cubic electric + magnetic operators, with gauge projection, correct units and finite-time reflection form. The result below closes only *the finite heat-kernel-action-to-KS-Hamiltonian interface for this chosen action*, not the complete P0 action/continuum gate.
- **Decisive new mathematics after this subcertificate:** 3D gauge-invariant multiscale control of the interacting theory at the required weak-bare-coupling trajectory, including compatible renormalized observables, common physically normalized exponential decay **and** nontrivial Schwinger limits. Existing electric-dominated stability bounds do not extend automatically: z=4/g0^4 tends to infinity along g0(h)→0.
- **Publication route:** the finite source-audited regulator is publishable, if independently reviewed, as a finite constructive/method paper; the 4D Yang–Mills existence-and-gap claim must remain a separately unproved dissertation objective until all hypotheses are satisfied.

## 2. Input geometry, gauge Hilbert space and physical coefficients

Let Λ_{h,R} be a finite open cubical subdivision of the spatial box [0,R]^3, with edge length h=R/n and oriented vertices V, edges E and plaquettes F; exact subdivision chain maps and h→0 are already covered in R3-IR-586 for the fixed-domain benchmark. SU(2) variables U_e reside on positively oriented edges, with U_{−e}=U_e^{-1}. The spatial gauge group G=SU(2)^V acts by (a·U)_e=a_{s(e)} U_e a_{t(e)}^{-1}; P denotes Haar projection onto H_phys=L²(SU(2)^E)^G. SU(2) Haar is probability normalized.

For each edge e, let C_e=−Δ_e be the nonnegative bi-invariant Casimir with eigenvalue c_j=j(j+1) in spin j∈{0,1/2,1,...}. Fix a **finite, positive, scale-dependent parameter g0(h)**; its nonperturbative trajectory has *not* been obtained. The conventional cubic Kogut–Susskind coefficient choice is

    α_h = g0(h)²/(2h),      β_h = 2/[g0(h)² h],
    K_h = α_h ∑_{e∈E} C_e,
    V_h(U) = β_h ∑_{f∈F} [1 − (1/2) tr U_f],
    H_h = K_h + V_h on H_phys.

Here the plaquette word U_f is the cyclic oriented product of its four *original* SU(2) links. The electric sum is essentially self-adjoint on the finite tensor-product Peter–Weyl core and the finite-face magnetic potential is bounded and nonnegative; hence the form sum is positive self-adjoint on the physical reducing subspace. These finite-graph facts are consistent with and are not presented as independent invention beyond existing R3-IR-587/R3-IR-590.

**Boundary/normalization scope:** the displayed coefficients specify one Hamiltonian convention, not an action-level derivation of the historical Penrose inverse-Whitney operator and not a theorem about uniqueness of spatial regulator. Spatial cube boundary conditions, any physical counterterms and finite-R surface effects must be retained explicitly.

## 3. One explicit 3+1-dimensional *time-discrete* action (temporal heat kernel, spatial Wilson)

For t>0, define the **central normalized SU(2) heat kernel** κ_t(g) on SU(2), with Haar mass one and Peter–Weyl expansion

    κ_t(g) = ∑_{j∈{0,1/2,...}} (2j+1)e^(−t j(j+1)) χ_j(g).

This series is absolutely smooth for t>0; κ_t(g)>0, ∫κ_t=1, κ_t=κ_t(g^{-1}) and κ_s∗κ_t=κ_{s+t}. Choose a Euclidean time step ε>0, and write t_{h,ε}=ε α_h. For neighboring spatial configurations U and U′, and one temporal SU(2) variable a_v at each vertex, set

    W_{h,ε}(U′,U;a)
      = exp[−ε(V_h(U′)+V_h(U))/2]
        × ∏_{e∈E} κ_{ε α_h}( U′_e [a_{s(e)} U_e a_{t(e)}^(−1)]^(−1) ).

The finite Euclidean cylinder partition kernel (or trace over periodic time) integrates each a_v and each slice U against normalized Haar. This is a **specified anisotropic heat-kernel-temporal / Wilson-spatial lattice gauge action**, not the isotropic four-dimensional Wilson-plaquette action. The difference must be kept explicit. Under separate gauge changes b_v at time k and b′_v at k+1, U→b·U, U′→b′·U′, a_v→b′_v a_v b_v^(−1); each heat-kernel argument conjugates by b′_{s(e)}, proving exact gauge invariance.

The corresponding transfer on the *full* L² space is

    T_{h,ε} = M_{exp(−ε V_h/2)} · P exp(−ε K_h) P · M_{exp(−ε V_h/2)}.

On H_phys, this is precisely T=e^{−ε V_h/2}e^{−ε K_h}e^{−ε V_h/2}. The displayed gauge-integrated heat-kernel W is its configuration-space integral kernel. Thus the electric, magnetic and temporal factors are all coefficients of **the same specified finite time-slice action**.

### Finite-regulator proposition and proof

**Proposition (scope: each fixed h,R,g0(h)>0,ε>0).** T_{h,ε} is gauge-preserving, bounded, nonnegative as an operator, self-adjoint and trace class on H_phys. It has the finite temporal-link reflection-positive transfer form. On the physical Hilbert space, for every fixed physical Euclidean time τ≥0,

    s-lim_{ε→0} [T_{h,ε}]^{floor(τ/ε)} = exp[−τ H_h].

*Proof.* The bi-invariant SU(2) heat semigroup has eigenvalues e^(−εα_h Σ_e j_e(j_e+1))>0 on tensor-product Peter–Weyl sectors, is a positive self-adjoint trace-class operator on the compact finite edge product, and commutes with all vertex gauge transformations. P is an orthogonal projection commuting with K_h; the spatial magnetic multiplier commutes with P and is bounded and strictly positive. Hence T=M(P e^{−εK}P)M and ⟨f,Tf⟩=‖e^{−εK/2} PM f‖²≥0; it is self-adjoint, trace class, and gauge-preserving. The positive transfer gives the usual finite-time reflection sesquilinear form (the reflected-half evolution becomes a nonnegative quadratic form in T). Because V_h is bounded on each finite graph, the symmetric Trotter product converges strongly to e^{−τ(K_h+V_h)} as ε→0 at fixed h,R. The normalized central heat-kernel spectral expansion supplies the displayed configuration kernel and temporal gauge covariance. ∎

**What was already known:** R3-IR-590 already records the finite positive symmetric transfer for the cubic Hamiltonian. The added specificity is an **explicit local temporal heat-kernel action and matching gauge-integrated kernel**, with a checkable same-action parameter dictionary and time-step domain, not a new nonperturbative gap theorem. Reflection positivity at *finite* time slicing here is **not** proof of the full four-dimensional continuum Osterwalder–Schrader axioms, Euclidean covariance, or Wilson-action universality.

## 4. Executed finite regression, not proof by numerical sampling

The companion Python checker tests the κ_t character Fourier spectrum in normalized SU(2) Haar measure via high-precision-in-weight Jacobi quadrature, and independent random quaternion spatial/temporal gauge transformations for n=1 and n=2 cubical boxes. Outcomes:

- n=1: (V,E,F)=(8,12,6); n=2: (27,54,36). 15 independent configurations per box; maximum gauge residual <1.1×10^−15 for all tested plaquette traces and temporal heat-kernel arguments.
- Central heat kernel normalization and first 11 spin-character convolution eigenvalues tested at t=.35,.7,1.1; maximum absolute Fourier multiplier error <1.1×10^−14.
- The pre-existing elementary 4-link Wilson-loop electric eigenvalue is 3α_h, while its dyadically subdivided 8-link pullback has eigenvalue 6α_{h/2}. The exact intertwining condition α_h=2α_{h/2} is **not** a legitimate replacement for a renormalization proof.

Exact symbolic/generator arguments above establish the finite proposition; these tests are implementation checks only. Executable: `verify_heat_kernel_p0.py`. Reproducibility outputs: `verification.json`, `verification.log`.

## 5. What remains open and what each future theorem must certify

| Certificate | Existing scope after this audit | Next mathematical acceptance test |
|---|---|---|
| **P0-G0, fixed-domain geometry** | Met for cubic (R3-IR-586), not historic coupled-ℤ⁵ 3D model | Do not repeat; protect exact chain maps and topology/source hashes |
| **P0-T0, finite same-action time interface** | Constructed for the **heat-kernel temporal + spatial Wilson** candidate at each h,R; R3-IR-590 had finite positive transfer | Independently review the kernel formula, boundary conventions, spin/coupling factors and time projection |
| **P0-T1, continuum universality/physical source** | **OPEN** | Demonstrate that the selected action/renormalized observables generate the intended interacting 4D Yang–Mills continuum; connect appropriately to the standard Wilson action or other accepted continuum definition |
| **P0-R1, scale and bare coupling** | **OPEN** | Specify and justify g0(h), counterterms, gauge-compatible blocking of smeared observables; prove joint h→0,R→∞/ε→0 tightness and uniform estimates |
| **P1/P2, interacting 3D state** | **OPEN** | Gauge-invariant physical multiscale bounds not restricted to electric-dominated regime or straight-strip geometry |
| **P4, physical common mass bound** | **OPEN** | Uniform *interacting* exponential decay of connected gauge-invariant Euclidean correlations e^(−M τ), with M>0 independent of h and R along g0(h) |
| **P5, nontrivial OS reconstruction** | **OPEN** | A compatible nonzero continuum OS field algebra, unique vacuum, and dense spectral coverage to identify the Yang–Mills QFT |

**Stop rule:** No numerical Ritz gap, positive first energy moment, bounded tensor-network bond, finite transfer positivity or bare-coupling strong-coupling gap may be relabeled `P0 closed`, `uniform interacting`, or `4D mass gap`. The difficult unsolved theorem remains the joint renormalized interacting state/infrared estimate and nontrivial OS construction.

## 6. Recommended next *decisive* experiment, not another redundant finite model

1. Choose one **exact physical gauge-invariant block map** for an h→h/2 pair of cubic boxes, and specify a smeared, fixed-physical-support Wilson-derived observable F_h. Demonstrate its temporal correlations (and counterterms) can be compared across the two regulators without assuming K_h J=J K_{h/2}. Define a signed/positive transfer-error norm whose bounds would remain meaningful at g0(h)→0.
2. Establish a quantitative one-step **interacting** renormalization comparison (correlations or effective actions) at a scale ratio two, with a summable error in the deep-UV refinement levels and independent of a growing physical box. If this first nontrivial step fails, identify the leakage mode (Bianchi, Gauss, soft transverse modes, center holonomy, boundary, or nonlinear channel).
3. Extend the successful step through a controlled multiscale scheme to obtain nontrivial limiting Schwinger functions and *common positive physical-time decay*; without this, the spectral-support conditional bridge supplies no gap.

The immediate task is therefore **not** to prove another one- or two-plaquette bound, and not to make a prettier map: it is to obtain the first rigorously scale-comparable **3D interacting, gauge-invariant correlation bound**. This is what the atlas now reveals as the actual transition to a continuum proof.

## 6A. A small conditional theorem explaining the shortest possible RG-to-gap bridge

Fix a dense *candidate* family of gauge-invariant renormalized physical observables F, whose fine-grid representatives F_{j,R} are defined by a common, source-specified blocking/renormalization prescription. Denote the **actual interacting vacuum** centered self-correlations at spatial refinement h_j=2^(−j)h_0 and physical time τ≥0 by C_{j,R}^F(τ), with the same model, chosen boundary conventions and coefficients at every j. Assume:

1. For one fixed initial resolution j=0, **uniform in physical box size R**, C_{0,R}^F(τ)≤A_F e^(−Mτ) for τ≥0, where M>0 does not depend on R or F (but A_F may depend on F).
2. There are nonnegative errors δ_{j,F} with ∑_{j=0}^∞ δ_{j,F}<∞ and a **common M>0** such that

       sup_R sup_{τ≥0} e^(Mτ) |C_{j+1,R}^F(τ) − C_{j,R}^F(τ)| ≤ δ_{j,F}.

Then, by a telescoping sum and the triangle inequality,

       0 ≤ C_{j,R}^F(τ) ≤ (A_F + ∑_k δ_{k,F}) e^(−Mτ)

for every j,R and τ≥0. Any pointwise/OS limit satisfying the separate consistency, positivity, vacuum-density and nontriviality hypotheses inherits the same physical M; the elementary spectral-support lemma in `docs/research/UNIFORM_INTERACTING_THEOREM_BRIDGE_2026-11-04.md` then excludes positive spectrum below M.

**This is a conditional bridge, not a renormalization theorem:** no δ_{j,F} or common M has been proved for the SU(2) target. Its practical role is to expose an **observable falsifiable one-step task**: compare two genuine 3D refinements in an exponentially time-weighted, gauge-invariant connected correlation norm with a summable error **and** verify a volume-uniform starting bound. The strong weighted norm is purposefully stringent; achieving it may be as hard as the continuum mass-gap problem. Convergence in unweighted finite-time norms, or with M_j→0, would not suffice.

## 7. Source provenance

Existing repository records (not replaced):
- `research/theorems/R3_FIXED_DOMAIN_CUBICAL_CHAIN_REFINEMENT_2026-10-31.md` — exact cubic chain subdivision, R3-IR-586.
- `research/theorems/R3_CUBICAL_SU2_GAUSS_HAMILTONIAN_REFERENCE_2026-10-31.md` — finite cubic Hamiltonian, R3-IR-587.
- `research/theorems/R3_CUBICAL_SU2_FINITE_TRANSFER_POSITIVITY_2026-10-31.md` — finite positive symmetric Trotter transfer, R3-IR-590.
- `research/theorems/R3_IR_REPOSITORY_REVIEW_3D_PERIODIC_CURL_SPECTRUM_2026-11-04.md` — transverse soft-mode geometry (periodic benchmark).
- `research/theorems/R3_IR_3D_QUANTITATIVE_THRESHOLD_AND_CONTINUUM_SCALING_AUDIT_2026-11-04.md` — strong-coupling/continuum regime mismatch.
- `docs/research/PROOF_DEPENDENCIES.md`; `docs/research/REPOSITORY_REVIEW_AND_P0_OBJECTIVE_2026-11-04.md`; the frozen historical claim acceptance gate.
- Draft branches/PRs #55, #56, #57, #58; they are not canonical accepted theorems.

Outside scientific problem statement: [Clay Mathematics Institute, Yang–Mills & the Mass Gap](https://www.claymath.org/millennium/yang-mills-the-maths-gap/) and [Jaffe–Witten official problem description](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf).

**Final classification:** finite action-interface certificate (subject to review), P0 not closed, 4D Yang–Mills mass-gap status OPEN.
