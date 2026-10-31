# Endpoint stitching criterion for the physical SU(2) deleted-face current

**Date:** 2026-10-31. **Status:** exact conditional inequality, synthesizing the *existing* 2026-10-30 Harnack–Fisher annular estimate with an additional endpoint score assumption. **Not** a proof of that assumption for Wilson cages, nor a uniform current estimate. The annular portion is not new.

For a finite positive Gauss-invariant Wilson ground state, let the target face density be `q(u)=w(u)ψ(u)^2`, `w(u)=2 sin²u/π`, `s(u)=∂u logψ(u)`, `A=Σ_(e∈∂f)a_e`, and `I=A∫_0^π s(u)^2q(u)du`. The exact Ward theorem identifies the signed positive current budget as `T=∫_0^{π/2}[s(u)]_+du`. For each `0<ε<π/2`, assume the explicit two local hypotheses:

1. **Endpoint one-sided derivative:** `[s(u)]_+≤M_ε u` for all `0≤u≤ε` (with finite M_ε).
2. **Annular density floor:** `ψ(u)≥m_ε>0` for all `ε≤u≤π/2`.

Then

`T ≤ (M_ε ε²)/2 + [ (π I)/(2 A m_ε²) cot ε ]^(1/2)`.

**Proof:** integrate the endpoint inequality on `[0,ε]`. On `[ε,π/2]`, weighted Cauchy–Schwarz gives `∫|s|≤(I/A)^(1/2)[∫q^-1]^(1/2)`. Since `q≥(2/π)m_ε² sin²u`, the inverse-density integral is at most `π cot ε/(2m_ε²)`. Add the two intervals. The endpoint `s(0)=0` follows from smooth centrality at the group identity but **does not provide a regulator-uniform M_ε**; the slice eigen-equation gives its jet without sign/variation control.

A sufficient *quantified, noncircular* regulator criterion is the existence of `ε_h∈(0,π/2)` and proven independent estimates `M_(f,h,ε_h)`, `m_(f,h,ε_h)`, `I_(f,h)/A_(f,h)` such that

`sup_f [ M_(f,h,ε_h) ε_h²/2 + sqrt(π I_(f,h) cot ε_h / (2 A_(f,h) m_(f,h,ε_h)²)) ] = o(h^-1/4)`.

A weaker necessary-to-test candidate at the marginal level may use the known one-link Harnack `m_ε≥R^-1`, but existing `R∼exp(C/h)` cannot make this small. The actual missing theorem is a **quantitative local endpoint score bound plus sufficient annular anti-depletion**, or a direct signed current bound that bypasses this sufficient criterion.

**Crucial non-implication:** the prior transport-response Hessian `Q=∫Ω²|∇(DΩ/Ω)|²_A` is not identified with the marginal score Fisher `I` and gives no value for `M_ε` or `m_ε`. No assertion `Q⇒I` or `Q⇒T` is made. The 2026-10-30 SU(2) center-cap capacity obstruction shows why the weighted-to-unweighted step is not automatic. This result therefore refines the analytic *dependency*, not the physical vacuum bound.

**Evidence:** 15 deterministic `ψ_λ(u)=exp(-λ cos²u)` rotor cases (λ=0.5,1,2,4,8; ε=0.1,0.2,0.4), exact input `T=λ`, with numerical quadrature of `I/A`, passed the inequality. This tests arithmetic, not Wilson vacuum and not asymptotic sharpness. Reproducible script and JSON preserved in Library `/The Singular Boundary/Proof Audits/R3_IR_ENDPOINT_STITCHING_CRITERION_2026-10-31.zip`.

**References in repo:** `R3_IR_HARNACK_FISHER_ANNULAR_CURRENT_2026-10-30.md`, `R3_IR_FISHER_TO_SIGNED_SCORE_CAPACITY_OBSTRUCTION_2026-10-30.md`, `R3_IR_CENTER_SLICE_EIGEN_EQUATION_JET_2026-10-30.md`, `R3_IR_TRANSPORT_RESPONSE_HESSIAN_2026-10-31.md`. Remaining complete-cage signed current, connected covariance, and continuum Yang–Mills mass gap **OPEN**.