# R3-IR — Physical Wilson-source susceptibility, spectral trichotomy and continuum two-point gate

**Date:** 2026-10-28. **Research branch:** `audit/2026-10-28-independent-reconstruction`.

**Evidence status:** Exact gauge-invariant finite-SU(2) spectral response and variational identities, and conditional subsequential spectral-measure/Euclidean two-point compactness. No uniform mass gap, physical-point variance classification, full OS field construction, quartic resolvent, or continuum Yang–Mills theory is claimed. The Stage 7/26 Monte Carlo Hamiltonian/source identity has not been authenticated. Historical source files are untouched.

## 1. Direct sources and why the target must be reassessed

Read the audit-branch reports `R3_IR_QUANTUM_MIXED_HESSIAN_WARD_GAUSS_AUDIT_2026-10-28.md`, `R3_IR_CURVATURE_WEIGHTED_FSUM_2026-10-28.md`, `R3_IR_LOCAL_VACUUM_SCORE_FORCE_2026-10-28.md`, `R3_IR_MODERATE_CURVATURE_EFFECTIVE_DRIFT_2026-10-28.md`, and `R3_IR_QUARTIC_SPECTRAL_WARD_AUDIT_2026-10-28.md`, and inspected the live claims ledger through claim 171. Earlier authors correctly distinguished α=3/2 from α=1 and proved only a first physical energy moment O(1) at α=3/2. The later repeated target `Var(Y_h)=o(h)` is equivalent to `Var(A_h)=o(1)`: that proves triviality of *this source*, not a positive mass gap. It must not be elevated to a necessary gap obligation. A gapped theory could have a nontrivial source variance.

## 2. Model, notation, and positive physical spectral measure

Consider the finite Wilson lattice Hamiltonian on a connected face-complete SU(2) rhombus disk,

`H_h = Σ_e a_e (−Δ_e)+Σ_f b_f[1−p_f]`, with `a_e>0`, `b_f≥0`, `p_f=½ReTr W_f`.

It commutes with all vertex Gauss operators; the strictly positive unique normalized ground state Ω_h is physical. Let `K_h=H_h−E_{0,h}≥0`, and let `P_G` be the physical gauge projection. Choose a bounded real face-weight function q_f supported in fixed physical interior `D_R`, and define the gauge-invariant multipliers

`Y_h=h Σ_{f∈D_R}q_f d_f`, `A_h=(Y_h−〈Y_h〉_h)/sqrt(h)`, `d_f=1−p_f`.

Then `<A_h>_h=0`, `P_G A_hΩ_h=A_hΩ_h`, and `A_hΩ_h` is perpendicular to Ω_h. Let `μ_h(I)=||1_I(K_h)A_hΩ_h||²`, for Borel `I⊂(0,∞)`. It is a *positive finite physical excitation-energy spectral measure*. Define

`v_h=μ_h((0,∞))=〈A_h²〉_h=Var(Y_h)/h`,
`m_h=∫ E μ_h(dE)=〈A_hΩ_h,K_h A_hΩ_h〉=〈Γ(A_h)〉_h`,
`χ_h=∫ E^(−1) μ_h(dE)=〈A_hΩ_h,K_{h,⊥}^(−1)A_hΩ_h〉`.

The finite graph has strictly positive first physical excitation energy Δ_h>0. Earlier VF-8 proves `0<c≤m_h≤C` for nonzero *nonnegative* macroscopic tests under electric lower bounds and physical geometry; the upper bound `m_h≤C` is available for *signed* bounded tests from the curvature-weighted Ward inequality and regional energy bound. Do not claim a lower bound for arbitrary signed weights.

## 3. Theorem PS-1: exact **physical** magnetic-source response

Let `H_h(s)=H_h−s A_h` for real s. Since A_h is real, bounded at each finite h and gauge invariant, H_h(s) is self-adjoint, preserves the Gauss sector, and has a simple strictly positive physical ground state for real s. The lowest eigenvalue E_h(s) is analytic in s near 0 (not uniformly in h). Kato perturbation theory gives

**`E_h'(0)=0`, `E_h''(0)=−2χ_h`.** (PS-1)

In particular, this is a **physical** resolvent, unlike the constant-link derivatives in the mixed-Hessian Ward identity. The full magnetic potential and the source commute as multiplication operators, but the resolvent remains dynamical.

**Exact gauge-invariant variational realization:** for real t, `ψ_t=(1+t A_h)Ω_h/sqrt(1+t²v_h)` is physical and normalized. Let `κ_{3,h}=〈A_h³〉_h`. The exact source-perturbed Rayleigh quotient is

**`〈ψ_t,(H_h(s)−E_{0,h})ψ_t〉 = [t²m_h−s(2t v_h+t²κ_{3,h})]/[1+t²v_h]`.** (PS-2)

For v_h,m_h>0, taking `t=s v_h/m_h` and s→0 gives `E_h(s)−E_h(0)≤−s² v_h²/m_h+O_h(s³)`. This uses only physical trial states, no assumed gap, and immediately implies the susceptibility lower bound

**`χ_h≥v_h²/m_h`.** (PS-3)

Alternatively, PS-3 is Cauchy–Schwarz on the positive physical spectral measure: `(∫dμ)²≤(∫E dμ)(∫E^(−1)dμ)`. For any physical Δ_h, spectral positivity also gives `v_h≤m_h/Δ_h`, `χ_h≤v_h/Δ_h`, and thus

**`v_h²/m_h≤χ_h≤v_h/Δ_h`.** (PS-4)

Every bound is finite-h and uses exactly the physical Gauss sector. No regulator-uniform lower bound for Δ_h is assumed or obtained.

## 4. Theorem PS-2: sharp three-way source spectral alternatives

Assume the established first-moment bound `m_h≤C` along a sequence of refining regulators. Then:

**(i) Vanishing source variance.** If `v_h→0`, the source vector `A_hΩ_h` vanishes in Hilbert norm. If in addition `m_h≥c>0`, then for each fixed Λ>0,

`∫_(0,Λ] E μ_h(dE)≤Λ v_h→0`, while `∫_(Λ,∞) E μ_h(dE)≥c−Λv_h`.

Hence any surviving first energy moment necessarily escapes to unbounded excitation energies. This is a source-UV escape statement, not gap positivity.

**(ii) Nonzero finite source variance.** If `0<v_0≤v_h≤v_1<∞`, then the measures μ_h have uniformly bounded total mass and first moment. For Λ>0, `μ_h((Λ,∞))≤C/Λ`, so they are tight on `[0,∞)` and admit weakly convergent subsequences μ_h⇒μ with `v_0≤μ([0,∞))≤v_1` (the zero endpoint may acquire mass). Moreover

`μ_h([0,2C/v_0])≥v_0/2`,
`χ_h≥v_0²/C`.

The limiting source spectral measure is nonzero. It is not a construction of the full quantum-continuum Hilbert space; without an independently proved uniform gap it may have a zero-energy atom.

**(iii) Diverging variance.** If `v_h→∞`, then since `m_h≥Δ_h v_h`,

**`Δ_h≤m_h/v_h≤C/v_h→0`, `χ_h≥v_h²/C→∞`.** (PS-5)

The normalized measures `μ_h/v_h` converge weakly to `δ_0`, since for each ε>0, `μ_h([ε,∞))/v_h≤C/(ε v_h)→0`. Thus source divergence is an exact spectral obstruction to a positive uniform physical gap. This does *not* establish variance divergence in the true Penrose vacuum.

## 5. Theorem PS-3: conditional nontrivial Euclidean two-point subsequence

Define the actual physical Euclidean correlation

`C_h(t)=〈A_hΩ_h,e^(−tK_h)A_hΩ_h〉=∫ e^(−tE) μ_h(dE)`, `t≥0`.

For each finite h, `C_h(0)=v_h`, `−C_h'(0)=m_h`, and

**`v_h exp(−t m_h/v_h) ≤ C_h(t) ≤ v_h`** for v_h>0, by Jensen's inequality, while **`|C_h(t)−C_h(s)|≤m_h|t−s|≤C|t−s|`.** (PS-6)

If `0<v_0≤v_h≤v_1` and m_h≤C, pass to the weakly convergent subsequence from PS-2; then `C_h(t)→C(t)=∫e^(−tE)μ(dE)` uniformly on every compact interval t∈[0,T]. Furthermore

**`v_0 e^(−Ct/v_0) ≤ C(t) ≤v_1`.** (PS-7)

The limiting kernel has **one-observable reflection positivity**: for all t_i≥0 and complex c_i,

`Σ_(i,j) conjugate(c_i)c_j C(t_i+t_j) =∫ |Σ_i c_i e^(−Et_i)|² μ(dE)≥0.` (PS-8)

If a regulator-uniform physical gap `Δ_h≥m_*>0` is independently proved, then μ is supported on `[m_*,∞)` and `C(t)≤v_1 e^(−m_*t)`. This extra gap is conditional and *not* inferred from PS-6/PS-8. One two-point kernel is not the full OS reconstruction theorem and does not control fourth moments, locality or infinite spatial volume.

## 6. Exact SU(2) reference check: positive gap and persistent physical source

For one open rhombus in the **pure electric** theory with four equal link coefficients a>0, Gauss invariance reduces the physical class functions to SU(2) characters; the vacuum is the Haar constant function. The physical first nonzero energy is `Δ=3a`, and for the gauge-invariant Wilson multiplier `A=p=(1/2)TrW`,

`v=1/4`, `m=3a/4`, `χ=1/(12a)`,
`C(t)=(1/4)e^(−3at)`, and `E_0''(0)=−1/(6a)` for the perturbation `H(s)=H−s p`.

Here `χ=v²/m` exactly, so PS-3 and Jensen's bound are sharp. This finite gauge-invariant model **simultaneously** has a positive physical gap and a nonzero source variance. It is **not** the refining strong-magnetic Penrose sequence and cannot establish a nontrivial continuum field there. It is a decisive counterexample to the *logical assertion* that mass-gap positivity requires all gauge-invariant Wilson-source variances to vanish.

## 7. Revised critical path and integrity

**Unconditionally proved at finite gauge-invariant Wilson regulators:** PS-1 exact physical source-energy response; PS-2 spectral alternatives given the previously verified first-moment bound; PS-3 Jensen and compactness implications. The nontrivial subsequence requires actual `v_0≤v_h≤v_1`, which is currently **unproved for the physical Penrose Wilson field**. No uniform mass gap or full quantum continuum is proved.

**Correction of proof priorities:** The repeated target `Var(Y_h)=o(h)` is one possible outcome, but not a necessary proof obligation for the Yang–Mills mass gap. The correct noncircular alternatives are: (1) obtain a regulator-uniform physical gap independently; (2) obtain variance tightness and nontriviality for a chosen gauge-invariant field independently; (3) control physical inverse-energy resolvents and higher-source distributions, with Stage7/26 source-level provenance checked separately. If the selected Wilson field instead collapses, it must be replaced/renormalized to construct a nontrivial observable; the theory itself need not become trivial.

**Reproducibility:** symbolic exact arithmetic and a finite SU(2) one-rhombus physical-character check, not Monte Carlo. Original three-face Z^5 Penrose spatial incidence may be checked separately; original Stage7/26 archives are untouched.