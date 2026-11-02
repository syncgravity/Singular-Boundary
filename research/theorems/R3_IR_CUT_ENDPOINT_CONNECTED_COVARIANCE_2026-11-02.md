# Cut endpoint connected covariance via exact bridge normalization — 2026-11-02

With a cut after face j in the physical open SU(2) strip, ν0=ν_L⊗ν_R is the factorized cut dressed measure and W(x,y)=ψ_g(p_(j+1)(x,y))² is the only crossing-face weight. Integrating right fresh links in reverse face order yields **Z(x)=∫W(x,y)dν_R(y)=Z constant**. Therefore the full dressed reference measure ν=Wν0/Z has **exact old-link marginal ν_L**, and for left A(x), right B(y):

Cov_ν(A,B)=Z⁻¹ E_νL[(A−ν_L A) Cov_νR(W_x,B)].

Assuming the previously archived weighted Bochner resolvent theorem on the cut-right generator (factor ρ=5/6, gradient constant 120/11), original-link graph distance r from the three cut-face new right links to support(B), and certified 24/25≤ψ_g≤26/25, ||s'_g||∞≤1/24, one has ||∇_R W_x||₂≤169/1250 and Z≥(24/25)². The covariance representation and Dirichlet integration by parts give

**|Cov_ν(A,B)|≤(845/528)(5/6)^r ||A−ν_L A||₂ ||∇_R B||₂**.

This is a conditional dressed-reference **endpoint** connected covariance theorem, not a spatially weighted reduced resolvent bound for H_t throughout t∈[0,1], nor a physical interacting-vacuum clustering theorem. Endpoint old-link expectations are invariant, giving ∫₀¹ μ'_t(A)dt=0 for old-link A. A rational product-spin check with right correlation c and bridge W=1+a xy yields exact Cov(x,z)=ac and unchanged left marginal. Full report, test script, log and SHA-256 manifest archived in Library /The Singular Boundary/Proof Audits. Fourth-order extensivity, interacting λ=1 and continuum Yang–Mills mass gaps remain open.