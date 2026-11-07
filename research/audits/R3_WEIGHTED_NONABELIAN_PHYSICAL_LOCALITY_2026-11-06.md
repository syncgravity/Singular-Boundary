# R3 / P2–T2: Weighted nonlinear non-Abelian Wilson-flow locality at fixed physical time

**2026-11-06.** Finite original-link open cubic SU(2) theorem candidate. Independent referee review pending. **All continuum P0–P5/T0–T5 and 4D Yang–Mills mass-gap gates OPEN.** Prior growing-support audit PR #90 merged as `d5ef636ad2f8abf60ff267937580a0cef211f952`.

On a finite cubic complex of lattice spacing h, let S=Σ_p ℓ_p, ℓ_p=1−½Tr₂(U_p), and the exact classical full original-link Wilson flow dU_s/ds=−∇S(U_s). Use the product bi-invariant metric T_j=iσ_j/2. Each face has exactly four original links; each link meets at most four faces; ||∇_eℓ_p||²=ℓ_p(2−ℓ_p)/4≤ℓ_p/2. Face centers sharing a link have physical separation at most √2 h.

For any real physical-space L-Lipschitz φ, put w_p=exp(2φ(c_p)), S_w=Σ_p w_pℓ_p and w_e=max_{p∋e} w_p.

**Theorem A (exact fully non-Abelian local Caccioppoli inequality).** At every finite spatial Wilson-flow time s,
\[
\frac{d}{ds}S_w(U_s)+\frac12\sum_e w_e\|\nabla_eS(U_s)\|^2
\le 32e^{2\sqrt2Lh}L^2h^2 S_w(U_s).
\]
**Proof.** Write F_e=Σ_{p∋e}∇_eℓ_p, R_e=Σ_{p∋e}(w_e−w_p)∇_eℓ_p, and ∇_eS_w=w_eF_e−R_e. The gradient-flow chain rule gives dS_w/ds=−Σ w_e||F_e||²+Σ⟨R_e,F_e⟩. Apply Young: ⟨R_e,F_e⟩≤w_e||F_e||²/2+||R_e||²/(2w_e). Neighboring physical face centers give 0≤w_e−w_p≤2√2Lh w_e and w_e/w_p≤exp(2√2Lh). Cauchy and the incidence bound d_e≤4 imply ||R_e||²/(2w_e)≤16e^{2√2Lh}L²h² Σ_{p∋e} w_p||∇_eℓ_p||². Sum over links, using four links per face and ||∇_eℓ_p||²≤ℓ_p/2, to conclude. No linearization, common Cartan subgroup, small curvature or DΦ_s estimate. □

**Theorem B (physical-radius uniform deterministic transfer).** For τ≥0 and s=τ/h²,
\[
\boxed{S_w(\Phi_{\tau/h^2}U)\le
\exp\left(32e^{2\sqrt2Lh}L^2\tau\right)S_w(U).}
\]
With c_h=32e^{2√2Lh}L²h² one also has the weighted time-integrated force bound
\[
S_w(\Phi_sU)+\tfrac12\int_0^s e^{c_h(s-t)}\sum_e w_e\|\nabla_eS(\Phi_tU)\|^2dt
\le e^{c_hs}S_w(U).
\]
The constants are independent of the **number** of links and faces and ambient physical-box size. For L,τ fixed and h→0 they remain finite. This is a *weighted nonlinear action* estimate, not a uniform bound on the gradient of Φ_s.

**Local and interacting-quantum-vacuum corollary.** For any fixed physical set K, take φ(c)=−a dist(c,K). The weight equals one on K and decays exponentially in physical distance outside, hence
\[
\sum_{c_p\in K}\ell_p(\Phi_{\tau/h^2}U)
\le e^{32e^{2\sqrt2ah}a^2\tau}
\sum_p e^{-2a\mathrm{dist}(c_p,K)}\ell_p(U).
\]
This holds pathwise, and therefore after averaging under the **actual coupled Gauss-invariant finite-regulator quantum ground-state probability measure** Ω²dHaar. The estimate does NOT itself bound the weighted **initial** vacuum energy as h→0 and R→∞, and multiplying by the physical classical curvature normalization 8/h leaves the previously diagnosed O(g₀²h⁻⁴) insufficiency. A localized vacuum estimate or renormalized/subtracted curvature observable is still necessary. Does not provide an interacting covariance/Poincare estimate or continuum spectral gap.

**Verification and persistence:** 201 reproducible deterministic assertions passed on n=1,2,3 exact cubical incidences, randomly sampled noncommuting SU(2) links, central finite-difference Lie derivatives of each plaquette, the weighted Caccioppoli inequality **including the force term**, and both linear and distance-based physical Lipschitz profiles. The analytic derivation above is the proof; checks do not sample the quantum vacuum. Complete report, independent Python verifier, execution log, SHA-256 manifest and ZIP integrity-tested archive uploaded successfully to Library `/The Singular Boundary/Proof Audits/R3_WEIGHTED_NONABELIAN_PHYSICAL_LOCALITY_2026-11-06.zip`, SHA-256 `6d0d9294bb488b7c57add3e92c9a9cde49d8037a675ffa375be1435486ab5826`.

**Next gate:** derive a uniform **local** interacting-ground-state expectation or suitably renormalized observable on the exponentially weighted initial side, then physical-curvature tightness after positive spatial flow and separately a uniform infrared Schur/spectral estimate. No Observatory gate promoted; no public hosting modifications.