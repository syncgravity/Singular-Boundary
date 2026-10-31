# R3-IR — Exact horizontal–transverse conditional Wilson kinetic decomposition

Date 2026-10-31. Exact original-link finite-volume identity; not a regulator-uniform current theorem.

Let H^-_f be the SU(2) deleted-face original-link Hamiltonian, Ω=Ψ(u)Φ its exact normalized factorization, A_f=Σ_(e∈∂f)a_e and u=arccos p_f in (0,π). Write X_i for all link Lie derivatives, a_i for their electric weights, and G=Γ(u,u)=Σ_i a_i(X_i u)^2=A_f/4. Define Y=G^(-1)Σ_i a_i(X_i u)X_i, so Yu=1. The conditional state satisfies E_μ[Φ²|u]=1 and E_(ν_u)[Y logΦ]=0, ν_u=Φ²μ_u. Set k=Σ_i a_i(X_i logΦ)^2.

**Theorem HK-1 (exact kinetic splitting):** pointwise on the open regular face-coordinate region,

Σ_i a_i(X_i Φ)^2 = G(YΦ)^2 + Σ_i a_i(X_i Φ−(X_i u)YΦ)^2.

Proof: expand the right hand side, use Σ_i a_i(X_i u)X_iΦ=G YΦ, and Σ_i a_i(X_i u)^2=G. The same identity applies to h=logΦ. Thus E_(ν_u)(Yh)^2 ≤ G^(-1)E_(ν_u)k = (4/A_f)E_(ν_u)k. The mean of Yh vanishes by differentiating conditional normalization using the archived exact angular transport identity; this proves

Var_(ν_u)(YlogΦ) ≤ (4/A_f)E_(ν_u)k.

**Theorem HK-2 (controlled covariance factor):** With ε=k+V_- and exact nonadiabatic remainder R(u)=E_(ν_u)[Yk]+2Cov_(ν_u)(ε,YlogΦ),

|2Cov_(ν_u)(ε,YlogΦ)| ≤ (4/√A_f) sqrt(Var_(ν_u)ε · E_(ν_u)k).

Consequently [-R(u)]_+ ≤ E_(ν_u)|Yk|+(4/√A_f)sqrt(Var ε · E k). Together with the archived maximum principle, this provides a conditional sufficient criterion, not a numerical bound on the physical vacuum. In particular no uniform control is known for Var ε, the material derivative Yk, or the local direct magnetic bound B_f^inc at candidate refinement scaling.

**Verification:** independent 5,000 random positive weighted tangent vectors satisfy the exact orthogonal projection identity with maximum relative algebraic residual 7.402800141877366e-16 and no positive violations. This checks the algebra, not the interacting vacuum or Penrose geometry. Script verify.py and results.json are included.

**Open:** Wilson-specific control of E|Yk| and Var(k+V_-) on the face collar, signed current sup_f T_(f,h)=o(h^(-1/4)), connected covariance and continuum Yang–Mills mass gap.