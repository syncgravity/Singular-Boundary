# R3–IR — Two-time weighted reference spacetime clustering (2026-11-02)

Let L_N be the finite SU(2) dressed reversible generator and P_t=e^{-tL_N}. Assume the **previously archived weighted Bochner semigroup estimate** ||∇P_t h||_(S,α,2)≤exp(−ct)||∇h||_(S,α,2), with c=11/120, α=log(6/5), for every physical original-link source set S. This assumption is *not independently verified by arithmetic tests*. Let F,G be smooth observables with link-gradient support S_F,S_G at distance d. Then

**|Cov_ν(F(X0),G(X_t))| ≤ (120/11)e^(−11t/120)(5/6)^d ||∇F||₂ ||∇G||₂.**

Proof: with Q the centered projection and R=L_N^-1 Q, the exact Poisson/Dirichlet identity is Cov(F(X0),G(Xt))=<∇F,∇R P_t QG>. Integrating the weighted gradient estimate for P_{t+s}G over s≥0 yields ||∇R P_t QG||_(S_G,α,2)≤(120/11)e^(−11t/120)||∇G||₂. Restricting the pairing to support of ∇F produces (5/6)^d. Integration yields the bound **∫₀∞|Cov|dt ≤ (14400/121)(5/6)^d ||∇F||₂||∇G||₂**.

For local residual bonds, ||∇w_j||₂≤G_w=√21·67/13824, and the two-time prefactor is (120/11)G_w²≈0.0053813347779. This is strictly about stationary dressed-reference dynamics, not cut-interpolation ground-state dynamics, not four-time connected cumulants, not fourth-order extensivity, not an interacting λ=1 gap, and not a continuum mass gap. Full detailed report, exact two-spin semigroup verifier, log and hash manifest archived in Library /The Singular Boundary/Proof Audits.