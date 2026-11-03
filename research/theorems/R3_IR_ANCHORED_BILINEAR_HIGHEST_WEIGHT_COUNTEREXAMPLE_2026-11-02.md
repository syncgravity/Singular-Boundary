# Exact highest-weight counterexample to unrestricted same-weight anchored Wigner bilinearity (2026-11-02)

**THEOREM (conditional on the archived SU(2) original-link open-strip full matrix-coefficient operator model).** For any finite analytic radius σ≥0 and support exponent κ, the centered Poisson bilinear map B(F,G)=K^(-1)QΓ_K(F,G) is NOT a bounded map A_(σ,κ)×A_(σ,κ) → A_(σ,κ) on arbitrary anchored Wigner polymer families. This does not assert any obstruction for gauge-invariant physical observables or the Yang–Mills mass gap.

**Explicit exact-rational construction.** On T=[1,t], t≥3, use the unnormalized highest-weight Wigner coefficients u(U)^n=D^(n)_(++)(U), where u(U)=U_11. For a multidegree n, h_n=∏u(U_i)^(n_i) is an exact eigenfunction of the archived electric operator with eigenvalue E(n)=Σ_i n_i(n_i+2)−(1/2)Σ_i n_i n_(i+1). This uses the diagonal C_i eigenvalue n_i n_(i+1)/4; ladder terms vanish at highest weights.

Let F_T=e^(−κt−σt)∏_(i=1)^t u(U_i) and G_{ {j} }=e^(−κ−σm)u(U_j)^m for every j in T, all other polymer components zero. Both anchored norms equal exactly 1 for any t,m. The product in each insertion is the single highest-weight Wigner coefficient with degree m+1 at site j and 1 elsewhere, and outputs from distinct j have distinct degree vectors.

By 2Γ_K(f,g)=fKg+gKf−K(fg), on interior insertion sites Γ_K(F_T,G_j) has unnormalized coefficient −m/2 and output electric eigenvalue (5t+1)/2+m²+3m; at the two endpoints coefficient −3m/4 and eigenvalue (5t+1)/2+m²+7m/2. Projection Q changes none. There is no analytic-radius reduction. Therefore the exact anchored output norm is

**||B(F,G)||_(Aσ,κ)=e^(−κ)[(t−2)m/(5t+1+2m²+6m)+3m/(5t+1+2m²+7m)].**

Taking t=m², m→∞, yields the asymptotic **e^(−κ)m/7 → ∞**, disproving unrestricted same-weight bilinearity in this Banach space at every fixed σ,κ.

This is consistent with the prior band-limited extensive singleton theorem: it allowed its constant to depend on the degree cap m. Indeed at fixed m with t→∞ the exact output ratio approaches e^(−κ)m/5, requiring at least a linear degree-dependent constant for this test family.

**Consequences:** The desired unrestricted anchored same-radius/same-support-weight fixed-point algebra is impossible with these norm definitions. A valid next objective requires a degree-moment tame estimate, additional regularity, support-exponent loss, or a restricted (possibly physical gauge-invariant) observable space. The previously established touching-support endpoint theorem and the bounded fixed-cutoff singleton action are not contradicted. No interacting λ=1 spectral gap or continuum 4D Yang–Mills mass gap is proved.

Complete mathematical proof, exact-rational verifier, execution log, and SHA-256 checksums: The Singular Boundary / Proof Audits Library.