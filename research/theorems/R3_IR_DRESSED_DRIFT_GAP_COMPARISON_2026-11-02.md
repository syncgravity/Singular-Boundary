# R3-IR — Dressed drift finite-volume gap and uniformity barrier (2026-11-02)

**Status:** Exact weighted Dirichlet identity, finite-volume gap and resolvent comparison. No uniform-in-volume gap or nonlinear convergence proved.

Let K=−Σ_{e,k}X_{e,k}² on SU(2)^E with quaternion generators /2 and normalized Haar gap 3/4. Let ψ_b(p)>0 be the exact isolated four-link plaquette ground state from the prior local-dressing theorem and set S_b=Σ_{f=1}^N log ψ_b(p_f), Φ=e^{S_b}, μ_b=Z_b⁻¹ Φ² dHaar, L_b=K−2Γ_K(S_b,·). Let ω_b=osc_{p∈[-1,1]} log ψ_b(p).

The integration-by-parts identity is
⟨f,L_b g⟩_{μ_b}=Σ_{e,k}∫(X_{e,k}f)(X_{e,k}g)dμ_b.
The normalized density ratio is bounded by exp(2Nω_b), hence Haar Poincaré comparison gives
gap(L_b)≥(3/4)exp(−2Nω_b).
Consequently, for u=L_b⁻¹P_{μ_b,0}f,
||u||_{2,μ_b}≤(4/3)exp(2Nω_b)||P_{μ_b,0}f||_{2,μ_b}, and
(Σ||X_{e,k}u||²_{2,μ_b})^{1/2}≤(2/√3)exp(Nω_b)||P_{μ_b,0}f||_{2,μ_b}.

These are rigorously finite-volume but the method loses exponentially in N, so they do not establish a thermodynamic gap. For numeric checks only: the isolated central-character Hamiltonian is tridiagonal with diagonal n(n+2), subdiagonal −b/2. A 100-mode numerical truncation gives class-sector gaps 3, 3.007280310990, 3.028986327102, 3.113863811507 at b=0,0.25,0.5,1, respectively. This is not the full original-link gap, and sampled wavefunction oscillations are not certified suprema.

**Next:** seek local conditional-link/Dobrushin or direct local coercivity estimates uniform in strip length, then extend inverse control to a nonlinear analytic product algebra and prove residual polymer summability. The interacting λ=1 and continuum mass gaps remain open. Full report, executable numerical checker, log and SHA-256 manifest reside in Library /The Singular Boundary/Proof Audits.