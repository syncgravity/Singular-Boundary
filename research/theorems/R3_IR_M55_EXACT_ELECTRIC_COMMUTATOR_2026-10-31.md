# R3-IR — Exact finite-cut electric commutator and signed metric defect

Date 2026-10-31. **Exact finite-link theorem, plus M55 numerical diagnostic. Not a uniform current bound.**

On original-link X=SU(2)^E, with normalized product Haar, take H=K+V, K=-sum_i a_i X_i^2 where a_i=a_e>0 is constant on each edge's three left-invariant Lie directions, and P_g f=f∘T_g. The six-link dual transport T_g is a smooth Haar-preserving bijection that fixes all retained plaquette words and therefore V_- when the target face term is deleted. Define J_g by ∇(f∘T_g)(U)=J_g(U)^T∇f(T_gU), A=diag(a_i).

For smooth f, the **exact quadratic-form commutator** is

⟨f,(P_g* H P_g-H)f⟩ = ∫ ∇f(T_gU)^T [J_g(U) A J_g(U)^T-A] ∇f(T_gU) dμ(U).

The potential cancels exactly. All signed cross-edge terms remain. This is a form identity, **not** an operator identity without coefficient-derivative first-order drift.

For the positive normalized vacuum Ω satisfying HΩ=E0Ω on the full link-product Hilbert space, the ground-state transform proves

∫ Ω² |∇(P_gΩ/Ω)|_A²dμ = ⟨P_gΩ,(H-E0)P_gΩ⟩ = ⟨Ω,(P_g*HP_g-H)Ω⟩ ≥ 0.

No pointwise positivity of the metric defect follows. The noncentral P_g need not preserve the physical Gauss subspace; the variational identity uses the unreduced space and the positive gauge-invariant eigenfunction Ω therein.

**Historical incidence:** reconstructed Stage26 M55 spatial torus with graph SHA256 f67fc4455b37bf18f16c0a5ae90c7c3c5ccd49ca8b739fa1f5e43562b4581c21; six-edge sequence [11,15,31,28,27,23] over faces [0,8,10,19,18,15], relative to a 69-face cut. Not an infinite 3D Penrose mesh or 12-prism R3.

**Deterministic verification:** full 57×57 Lie-coordinate Jacobian, three seeded noncommuting configurations, synthetic positive electric link coefficients, link-character test observable. Chain-rule residual at most 1.02e-9, metric form residual 1.78e-15, retained face residual 2.09e-15, log Jacobian determinant residual 8.53e-10. These samples are not vacuum expectation calculations. Stage26 Euclidean beta values are not asserted to equal Hamiltonian a_e.

**OPEN:** actual Hamiltonian matching and Gauss-invariant completed-cage cut specification, vacuum expectation estimate on the signed metric defect, uniform signed current sup_f T_{f,h}=o(h^-1/4), connected covariance, continuum reconstruction and mass gap. Stage19 measurement catalogue byte identity still unresolved.

Full program and checks in Library: /The Singular Boundary/Proof Audits/M55_ELECTRIC_COMMUTATOR_2026-10-31.zip . Underlying giant incidence in prior Library reconstruction package.