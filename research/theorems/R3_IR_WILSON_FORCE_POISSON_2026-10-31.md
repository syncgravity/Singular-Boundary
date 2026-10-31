# Exact original-link force–Poisson identity for the deleted Wilson vacuum

Date 2026-10-31. Finite-volume theorem, not a uniform score bound.

Let H=-Σ_e a_eΔ_e+Σ_{g≠f}b_g(1-p_g) on full original-link L²(SU(2)^E), with smooth positive ground state Ω and ground energy E0. For left-invariant SU(2) Killing derivative X=X_(e,a), set v=X logΩ and ℒ=Σ_k a_k(Δ_k+2∇_k logΩ·∇_k). Since [K,X]=0 and [V,X]=-(XV), the ground-state transform gives the **exact forced score equation**

**ℒv=XV=-Σ_{g≠f:e∈∂g}b_g Xp_g.**

For a simple deleted face in an edge-to-edge rhombus disk, each of its boundary links has at most one retained incident face. Since |Xp_g|≤1/2, |ℒv|≤(1/2)Σ_{g≠f:e∈∂g}b_g. At b∼h^-2 this is not uniform. Reversibility gives **∫Γ(v,v)Ω²dμ=-∫v XV Ω²dμ≥0**, and ∫XV Ω²dμ=0. Although the source is incidence-local, the solution v involves the inverse of the complete interacting generator; an estimate uniform in mesh/refinement or vacuum size does not follow. It is not valid to equate an individual link derivative v with the conditional target-face radial score.

Analytic one-rotor normalization check: Ω=Z^-1/2exp(λp), V=λ²(1-p²)/4-3λp/4+C≥0, p=TrU/2; v=λXp satisfies ℒv=(-3λ/4-λ²p/2)Xp=XV exactly. The bundled verifier checks 328 parameter cases. This engineered rotor is not a Wilson cage. Executable and integrity manifest in Library /The Singular Boundary/Proof Audits/WILSON_FORCE_POISSON_2026-10-31.zip.

**OPEN:** regulator-uniform inverse-generator/conditional center-score control, signed current sup_f 𝔗_(f,h)=o(h^-1/4), connected covariance and continuum mass gap. Production Stage26 Euclidean β values are not identified with Hamiltonian coefficients.