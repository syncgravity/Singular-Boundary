# R3-IR — Gradient-resolved nested-block resolvent differences (2026-11-02)

For finite open SU(2) straight square strips, let I be a face interval and J=I∪{f} its adjacent one-face extension. Assume the previously certified dressed-reference bounds at |b|≤0.001: κ=23/144 for all block Dirichlet gaps, ||s_b'||∞≤1/24, ||∇_{e*}p_f||∞≤1/2, and one-face L² measure comparison r=13/12. Set C_f h=2Γ_{e*}(s_b(p_f),h), Q_J=L_J⁻¹P_J, and energy seminorm E_I(h)=||∇_{E(I)}h||_{L²(ν_I)}.

By the shared-link derivative and measure comparison, ||C_f h||_{L²(ν_J)}≤13/288 E_I(h) for h supported on old links. By the uniform spectral gap, E_J(Q_J g)≤κ^(−1/2)||g||₂, hence

**E_J(Q_J C_f h)≤θ E_I(h), θ=13/(24√23)≈0.1129453.**

For old-supported F, the exact previous telescoping identity Q_JF−Q_IF=Q_J C_f Q_IF gives **E_J(Q_JF−Q_IF)≤θ E_I(Q_IF)**. This is stronger in the gradient norm than the previous ≈0.707 L² resolvent-difference estimate.

**Non-iterability:** For a fixed old-supported F and expanding intervals I_j, u_j=Q_{I_j}F, d_j=u_j−u_{j−1}. The estimate bounds E(d_j) by θ E(u_{j−1}), *not* θ E(d_{j−1}). By measure consistency one gets only E(u_j)≤(1+θ)E(u_{j−1}). No θ^k decay of actual differences follows; 2θ<1 applies to abstract nested transfer maps only. A further boundary-increment/cumulant projection identity is needed.

The exact-rational script checked all constants and this non-iterability diagnosis. Full proof, verifier, log and SHA-256 manifest are in Library /The Singular Boundary/Proof Audits. Physical interacting λ=1 and continuum mass gaps remain open.