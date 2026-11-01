# R3-IR — Spectator-conditioned local Wilson Harnack bound

Date 2026-10-31. Exact finite-volume theorem; no regulator-uniform claim.

Let H=-Σ_e a_e Δ_e+V on X=SU(2)^E, with a_e>0, continuous bounded real V, and positive normalized ground state Ω. For S⊆E and x=(x_S,z), x'=(x'_S,z) sharing all spectator link values, define Δ_S V=sup_z(sup_u V(u,z)−inf_u V(u,z)). Let R(s)=max k_s / min k_s for positive SU(2) heat kernel. Then for all t>0,

**Ω(x)/Ω(x') ≤ exp(t Δ_S V) ∏_(e∈S) R(a_e t).**

**Proof.** Condition the product-Brownian bridge in Feynman–Kac on the entire common spectator bridge Z_[0,t]. For every fixed spectator path, the changed-link bridge Feynman–Kac factor lies between exp[−∫sup_u V(u,Z_s)ds] and exp[−∫inf_u V(u,Z_s)ds]. These factors are the same for both initial changed-link configurations, so the ratio of conditional kernels is bounded by exp(t Δ_S V) times the ratio of the free changed-link heat kernels. Compare the latter by ∏R, integrate the identical positive spectator bridge measure, and then integrate against Ω(y)>0 in the ground-state semigroup identity. No global potential-oscillation factor remains.

For the deleted-face Wilson V_-=Σ_(k≠f)b_k(1-p_k), **Δ_S V_-≤2Σ_(k≠f,∂k∩S≠∅)b_k**. Plaquettes disjoint from S cancel exactly. If a target holonomy transport T_g changes only links in S, then its actual Wilson vacuum orbit-density ratio satisfies **R_z≤inf_(t>0)e^(2t Δ_S V_-)∏_(e∈S)R(a_e t)^2**. The set of changed links is not the potentially larger full electric-Jacobian dependency support.

Verification: 6039 finite positive-kernel conditional-bridge sandwich checks, zero violations; these are algebraic checks, not an interacting Wilson vacuum measurement. Proof and results in Library Proof Audits archive R3_IR_LOCAL_WILSON_HARNACK_2026-10-31.zip. Remaining open: refinement uniformity when |S| and b_k scale, weighted orbit anti-depletion, signed current, connected covariance, continuum Yang–Mills gap.