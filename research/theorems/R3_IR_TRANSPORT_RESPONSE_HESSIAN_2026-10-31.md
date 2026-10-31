# R3-IR — Exact second variation of magnetic-preserving SU(2) transport

Date: 2026-10-31. Finite original-link theorem; no uniform vacuum-current estimate.

Let H=K+V_- on L²(SU(2)^E,dHaar), K=-Σ_e a_eΔ_e with positive constant link coefficients, Ω>0 the normalized ground state with HΩ=E0Ω. Let T_t be a smooth one-parameter Haar-preserving transport with V_-∘T_t=V_- and P_tF=F∘T_t a unitary group with skew-adjoint generator D. Assume adequate smooth domains. Then F(t)=⟨P_tΩ,(H-E0)P_tΩ⟩ satisfies F(0)=F'(0)=0 and

**F''(0)=2Q, Q=⟨DΩ,(H-E0)DΩ⟩=-½⟨Ω,[D,[H,D]]Ω⟩≥0.**

Because [V_-,D]=0, [H,D]=[K,D]. The outer derivative must retain all variable coefficient and transport terms. The ground-state transform gives Q=∫Ω²|∇(DΩ/Ω)|²_A dHaar. Spectrally Q=Σ_{n≥1}(E_n-E0)|⟨Ω_n,DΩ⟩|². Proof: differentiate the quadratic form, use (H-E0)Ω=0, D*=-D and integrate by parts. None of these equalities supplies an upper bound on Q or a lower bound on the transport response-sector gap.

**Non-implication:** even Q or ||DΩ||² control cannot alone imply the unweighted signed radial score integral at rare centers; see `R3_IR_FISHER_TO_SIGNED_SCORE_CAPACITY_OBSTRUCTION_2026-10-30.md`. A regulator-robust Wilson-specific anti-depletion principle remains necessary. This does not establish sup_f T_(f,h)=o(h^-1/4), full completed-cage spectrum, or any continuum mass gap. The Stage26 M55 Euclidean β coefficients have not been justified as Hamiltonian electric coefficients.

An independent 3×3 positive-ground-state matrix test with potential-invariant skew generator checks Q=1.3764704604500932, double commutator expectation -2.7529409209001847 and F(t)/t²→Q. It is **not** a simulation of the M55 Wilson vacuum. Full report, code, JSON and hash manifest: Library `/The Singular Boundary/Proof Audits/R3_IR_TRANSPORT_RESPONSE_HESSIAN_2026-10-31.zip`. Related source: `R3_IR_M55_EXACT_ELECTRIC_COMMUTATOR_2026-10-31.md`.
