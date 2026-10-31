# R3-IR — Exact neighboring Wilson-force Green–Kubo identity and low-energy tail gate

Date: 2026-10-31. Finite original-link interacting SU(2) Wilson theorem; **no uniform low-energy bound**.

Set A=H_f^-−E0≥0, Ω>0 normalized, w_a=X_(e,a)Ω and F_a=(X_(e,a)V_-)Ω. The original-link differentiated eigen-equation gives Aw_a=−F_a and w_a,F_a⊥Ω. Define the ground-state stationary reversible diffusion generator ℒ=Σ_e a_e(Δ_e+2∇_e logΩ·∇_e). For φ_a=X_(e,a)V_- define C_e(t)=Σ_a E_ν[φ_a(U0)φ_a(Ut)]=Σ_a⟨F_a,e^(−tA)F_a⟩≥0. The spectral theorem gives exactly

**S0_e=Σ_a‖X_(e,a)Ω‖²=∫_0^∞t C_e(t)dt**,

and the archived f-sum is S1_e=∫_0^∞C_e(t)dt=(3/8)Σ_{g≠f:e∈∂g}b_g E_νp_g. For any T>0 the exact positive remainder is R_e(T)=Σ_a⟨F_a,A^(−2)(I+TA)e^(−TA)F_a⟩≥0, so S0_e=∫_0^TtC_e(t)dt+R_e(T). The finite-time integral is ≤ T² C_e(0)/2; the remainder is the unresolved low-energy sector, and dropping it never proves an upper bound.

For one retained adjacent face g, C_e(0)=(b_g²/4)E_ν(1−p_g²). An **independently proved** envelope C_(e,h)(t)≤c_(e,h)(1+t/τ_(e,h))^(−q), q>2, would imply S0_(e,h)≤c_(e,h)τ_(e,h)²/((q−1)(q−2)). This is a conditional dynamical hypothesis, *not* an established Penrose Wilson mixing rate. Even an S0 bound does not yield the unweighted center current without a separate collar anti-depletion/conditional projection argument. Thus sup_f 𝔗_(f,h)=o(h^(−1/4)), covariance and continuum mass gap remain OPEN.

Independent verifier: 250 randomized positive spectra, finite-time remainder and power-law integral checks (numerical algebra diagnostic only). Proof, verifier, results and SHA256 manifest archived in Library `/The Singular Boundary/Proof Audits/R3_IR_WILSON_FORCE_GREEN_KUBO_2026-10-31.zip`. See the full report there for derivations and domain hypotheses.