# R3-IR — Exact original-link cut generator and local potential (2026-11-02)

**Correct cut.** For open straight N-face SU(2) strip cut after face j, partition the *existing* 3N+1 original links into E_L=∪_{m≤j}∂f_m (3j+1 links) and E_R its complement (3(N−j) links). No shared-link duplication. Only face f_(j+1) has links on both sides. Write S=S0+s, with s=s_g(p_(j+1)) and S0=Σ_{m≠j+1}s_g(p_m). The dressed law ν0∝exp(2S0)Haar is a product ν_L⊗ν_R, and L0=−Δ−2Γ(S0,·)=L_L⊗I+I⊗L_R.

**Unitary equivalence.** If ν∝exp(2S)Haar and their normalization constants are Z,Z0, then U:L²(ν)→L²(ν0), Uf=sqrt(Z0/Z)exp(s)f, is unitary. For L=−Δ−2Γ(S,·), exact ground-state conjugation gives **ULU⁻¹=L0+Vcut**, where **Vcut=Δs+2Γ(S0,s)+Γ(s,s)**. In particular the full transformed ground vector is U1, not 1.

**Local bound.** With p=Re plaquette holonomy, Δp=−3p, Γ(p,p)=1−p², and only immediate neighboring plaquettes overlapping the cut, **||Vcut||∞≤||s_g''||∞+3||s_g'||∞+2||s_g'||∞²**. Support is inside faces j,j+1,j+2. Previous certified q_g=||s_g'||∞+||s_g''||∞≤49/576 and ||s_g'||∞≤1/24 give **||Vcut||∞≤41/192≈0.21354167**, independent of strip length. This exceeds the margin needed for a naive cut-gap minmax argument relative to κ=23/144.

**Shifted resolvent.** Let A=L0+μ, B=ULU⁻¹+μ for μ>0. The exact identity **B⁻¹−A⁻¹=−B⁻¹ Vcut A⁻¹** gives ||B⁻¹−A⁻¹||≤||Vcut||∞/μ², but has no distance decay. Centered inverses need separate ground-state projections because A and B have different ground vectors. There is no bounded-perturbation comparison by merely duplicating the shared original SU(2) link: that changes Hilbert space and measure.

**Status.** Exact finite-volume cut identity, local volume-independent potential, and shifted-resolvent identity established. Cut-localized connected fourth-order response, fourth-order extensivity, nonlinear interacting λ=1 gap and continuum Yang–Mills mass gap remain open. Independent symbolic two-dimensional diffusion, rational constant, and finite-matrix resolvent checks passed; they do not independently verify SU(2) geometry.

Full proof and SHA-256 provenance, verifier and log are in Library /The Singular Boundary/Proof Audits.