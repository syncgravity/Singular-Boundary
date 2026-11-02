# Independent centered-defect operator audit — 2026-11-02

For L>=0, Γ(F,G)=1/2(F LG+G LF−L(FG)) positive. D_t(F,G)=P_t(FG)−P_tF·P_tG=2∫₀ᵗP_sΓ(P_(t−s)F,P_(t−s)G)ds. Q commutes with P_s, and crucially Q acts on the **whole** carré-du-champ product.

Under spectral gap κ=23/144 and weighted L4 semigroup gradient decay c=11/120, rho=6/5, two-sided graph weights plus L4×L4→L2 yield ||Γ(P_uF,P_uG)||₂≤(5/6)^D exp(−2cu)||∇F||₄||∇G||₄, with no link-count factor. Thus ||QD_t||₂≤(1440/17)(5/6)^D[exp(−23t/144)−exp(−11t/60)]||∇F||₄||∇G||₄ and ∫dt||QD_t||₂≤(17280/253)(5/6)^D||∇F||₄||∇G||₄.

The stationary scalar component can fail to decay: in the two-spin simultaneous-flip model ΠD_t(X,X)=1−exp(−6t), QD_t(X,X)=0. An independently scripted four-state semigroup and Γ quadrature confirmed signs, factor of two, Q placement and the earlier 3/64 spin-product value. The initial test had an incorrect 4t exponent for X; corrected to 6t before final passing run. Weighted SU(2) Bochner and gap estimates are inherited analytic conditions; no fourth-order, interacting λ=1, or continuum mass-gap theorem is newly proved.

Full detailed report, executable Python verifier, final passing log and SHA256 are archived in Library /The Singular Boundary/Proof Audits.