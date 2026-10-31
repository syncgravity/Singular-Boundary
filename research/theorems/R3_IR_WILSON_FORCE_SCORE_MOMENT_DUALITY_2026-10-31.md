# R3-IR: Exact Wilson force–score spectral moment duality

Date: 2026-10-31. **Finite original-link Wilson theorem.** Does not prove a uniform low-energy or collar-current estimate.

## Setting and exact identities
On the full SU(2) product-link Hilbert space, let H = K + V_- be the positive-coupling deleted-face Wilson Hamiltonian, Ω its strictly positive normalized ground state and E0 its energy. Write A=H-E0≥0. Fix original edge e and left-invariant orthonormal Lie derivatives X_a=iσ_a/2, a=1,2,3. Let w_a=X_a Ω and F_a=(X_a V_-)Ω. Derivatives commute with K, so differentiating HΩ=E0Ω gives **A w_a = −F_a**. As X_a are skew-adjoint and Ω is real, w_a is orthogonal to Ω. With the spectral measures of A on w_a, this gives for k=0,1,2 (all finite at fixed volume):

S0=Σ_a ||w_a||², S1=Σ_a ⟨w_a,A w_a⟩, S2=Σ_a ||A w_a||²=Σ_a ||F_a||².

S1=½ E_ν[Σ_a X_a²V_-] = (3/8) Σ_{g≠f:e∈∂g} b_g E_ν[p_g], the previously established local Wilson f-sum; the sign follows from −Δ_ep_g=3p_g/4. For a deleted-face boundary edge with exactly one retained adjacent plaquette g, the exact force-squared identity is

**S2=(b_g²/4) E_ν[1−p_g²]**,

using Σ_a(X_a p_g)²=(1−p_g²)/4. It is not a pointwise force-sign statement. With no adjacent retained plaquette, S1=S2=0 and A w_a=0; uniqueness of the positive ground state and w_a⊥Ω imply w_a=0 (the private-edge case).

Cauchy–Schwarz on the combined Hilbert direct sum of three score directions gives **S1²≤S0 S2**. If S2>0, then

**S0≥(9/16) (E_ν p_g)² / E_ν(1−p_g²).**

Hence an aligned neighboring plaquette with E p_g near 1 and small E(1−p_g²) forces a *large* link-score L² norm, rather than allowing it to be uniformly discarded. This lower bound does not determine a gap or center-current sign. With two or more retained incident plaquettes, the exact second moment retains cross correlations Σ_{g,k} b_g b_k E[∇_e p_g·∇_e p_k], which cannot be omitted.

The force spectral measure is λ² times the score spectral measure; therefore S1=Σ∫ λ^{-1}dμ_F(λ), S0=Σ∫ λ^{-2}dμ_F(λ) on the nonzero spectrum, and S2=Σ∫ dμ_F(λ). The inverse moments are finite at fixed finite volume but **not uniformly bounded by S1,S2**: an abstract positive spectrum λ=ε with w=ε^{-1/2} gives S1=1, S2=ε→0, S0=1/ε→∞. This is a logical low-energy obstruction, not a Wilson counterexample.

## Provenance and scope
Depends on `R3_IR_WILSON_FORCE_POISSON_2026-10-31.md` and `R3_IR_LOCAL_WILSON_RESPONSE_FSUM_2026-10-31.md`. The k=2 moment and the sharp score-norm *lower* bound are additions. No Hamiltonian identification is made from historical Stage26 Euclidean beta. Does **not** bound the conditional one-sided current or prove anti-depletion, connected covariance or the Yang–Mills mass gap.

## Independent checks
`verify.py` evaluates all three spectral moment identities in a finite positive-matrix model with an exactly imposed A w=−F relation, and tests the SU(2) edge force-squared identity using fixed-seed Haar quaternions and Pauli matrix generators. Checks are algebraic diagnostics, not numerical Wilson ground-state computations.