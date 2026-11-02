# R3-IR — Exact local plaquette dressing and shared-link residual (2026-11-01)

**Status:** Exact finite-volume conjugation identity and isolated-plaquette perturbative verification. No chain-uniform convergence or interacting gap claim.

For an open straight square SU(2) strip, take K=−Σ_{e,k}X_{e,k}² with generators normalized by imaginary quaternion/2, H_b=K−bΣ_f p_f, p_f=Re(U_f), Γ_K(F,G)=Σ_{e,k}(X_e,k F)(X_e,k G). A single face's four original link Casimirs act on class functions as K_f=−(∂_u²+2cot(u)∂_u), p=cos u, K_f χ_n=n(n+2)χ_n and K_f p=3p.

Define the unique positive isolated ground state ψ_b(p), eigenvalue ε(b), of (K_f−b p)ψ_b=ε(b)ψ_b and choose Haar(ψ_b)=1. This is an exact Sturm–Liouville definition, not an elementary closed form. The isolated zero eigenbranch is analytic in |b|<3/2 in the L² spectral sense by a resolvent contour |z|=3/2, gap 3 and ||p||op≤1; positivity is for real b.

Let s_f=log ψ_b(p_f), Φ=exp(S)=∏_f ψ_b(p_f), S=Σ_f s_f. The exact finite-chain identity is
Φ⁻¹(H_b−Σ_f ε(b))Φ=K−2Γ_K(S,·)+W_b, W_b=−2Σ_{f<g}Γ_K(s_f,s_g).
Nonadjacent faces have disjoint original links so W_b has only adjacent-face terms. The drift K−2Γ_K(S,·) is nonnegative and symmetric in Φ² dHaar. Φ is not claimed to be the interacting ground state.

The character recursion pχ_j=(χ_{j+1}+χ_{j−1})/2 (χ_{−1}=0), λ_j=j(j+2), ψ=Σ b^n ψ_n (Haar ψ_n=0 for n>0) gives ε_n=−[pψ_{n−1}]_{χ₀} and K_f ψ_n=pψ_{n−1}+Σ_{k=1}^n ε_k ψ_{n−k}. Exact Fraction checks through order 10 yield ε(b)=−b²/12+5b⁴/3456−289b⁶/4976640+..., ψ_b=1+(b/6)χ₁+(b²/96)χ₂+.... Thus s_f=b p_f/3+O(b²) and W_b=−(2b²/9)Σ_adj Γ_K(p_f,p_g)+O(b³). Keep Γ symbolic until the previous shared-link orientation discrepancy is settled.

This exactly absorbs the original bare single-face potentials, but repeated adjacent-pair insertions and the dressed inverse remain uncontrolled. No all-orders connected polymer summability, λ=1 interacting gap, or continuum Yang–Mills mass gap has been proved. Detailed report, verifier, execution log, SHA-256 manifest: Library /The Singular Boundary/Proof Audits.