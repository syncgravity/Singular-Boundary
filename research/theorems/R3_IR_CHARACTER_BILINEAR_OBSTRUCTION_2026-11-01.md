# R3-IR — Exact SU(2) character obstruction to L² bilinear Poisson closure

Date: 2026-11-01. **Proved:** failure of L²×L²→L² boundedness of the free-electric bilinear operator on one SU(2) link; not divergence of the physical perturbation series.

Let K=−Σ_k X_k², Γ_K(f,g)=Σ_k(X_kf)(X_kg), and P₀=I−P_Haar. For the normalized SU(2) characters χ_n(U)=U_n(Re U), Kχ_n=λ_nχ_n with λ_n=n(n+2)/4 and ||χ_n||₂=1.

Clebsch–Gordan gives χ_n²=Σ_{j=0}^n χ_{2j}. From K(fg)=fKg+gKf−2Γ_K(f,g),

K⁻¹P₀Γ_K(χ_n,χ_n)=Σ_{j=1}^n(λ_n/λ_{2j}−1/2)χ_{2j}.

The fixed χ₂ coefficient is n(n+2)/8−1/2. Character orthogonality implies ||K⁻¹P₀Γ_K(χ_n,χ_n)||₂≥|n(n+2)/8−1/2|→∞, though both input norms equal 1. Thus there is no bounded extension of this polynomial bilinear map L²×L²→L².

This does **not** contradict the previously proved linear one-derivative resolvent bound, nor exclude holomorphic or Sobolev algebra estimates. Exact SymPy checks passed for n=1,...,16. Companion detailed report, checker, execution log, SHA-256 manifest are preserved in /The Singular Boundary/Proof Audits in Library.

Next obligation: find an analytic/Sobolev algebra scale controlling high×high→low Clebsch–Gordan transfers and connected-support multiplicity, while keeping derivative losses manageable. Interacting λ=1 and continuum mass gaps remain open.
