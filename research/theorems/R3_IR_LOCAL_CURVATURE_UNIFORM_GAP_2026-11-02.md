# R3-IR — Local curvature and uniform small-coupling dressed gap (2026-11-02)

**Theorem (finite open square SU(2) strips):** Set K=−Σ_{e,k}X²_{e,k}, with quaternion/2 generators, and S_b=Σ_f s_b(p_f), s_b=log ψ_b, p_f=Re U_f; ψ_b is the positive isolated plaquette ground state. Let μ_b∝exp(2S_b)Haar, L_b=K−2Γ_K(S_b,·), q_b=||s'_b||∞+||s''_b||∞.

The product SU(2)^E has Ricci tensor Ric=(1/2)g for these generators. For a face with four distinct links, |∇p_f|²≤1, and |Hess p_f(V,V)|≤Σ_{e∈∂f}|V_e|². Each link occurs in at most two faces, so ||Hess S_b||op≤2q_b. Thus the Bakry–Émery tensor of the reversible generator −L_b=Δ+2∇S_b·∇ is Ric−2Hess S_b≥(1/2−4q_b)g.

**If q_b<1/8, gap(L_b)≥κ_b=1/2−4q_b>0, uniformly in the strip length.** In particular Var_μ f≤κ_b⁻¹Σ||Xf||²_{L²(μ)}, and ||∇L_b⁻¹P_{μ,0}f||₂≤κ_b^(−1/2)||P_{μ,0}f||₂. Since ψ_b→1 smoothly as b→0, some b_*>0 exists for which the condition holds for all |b|<b_*; this does not specify a certified numerical b_*.

A 90-character Jacobi truncation, 24-mode Chebyshev reconstruction and 2001-point derivative sample tested b=0,0.05,0.1,0.2,0.3; estimated κ values were 0.5, 0.432774, 0.364415, 0.224207, 0.079198. **These are numerical diagnostics, not rigorous suprema or certified coupling thresholds.**

The result replaces an earlier exponentially-volume-dependent comparison within the small-b region only. It does not establish an analytic algebra bound for the dressed inverse, all-orders residual polymer convergence, physical λ=1 interacting gap, or continuum Yang–Mills mass gap. Companion detailed report, verifier, log and SHA-256 manifest in Library: /The Singular Boundary/Proof Audits.