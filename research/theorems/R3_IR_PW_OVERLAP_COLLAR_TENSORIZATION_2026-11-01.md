# Overlap-collar intrinsic Peter–Weyl bilinear estimate (2026-11-01)

**Scope:** finite open straight SU(2) original-link face chains; a local theorem, not a connected-score convergence theorem.

Let I,J be overlapping face intervals, O=I∩J nonempty, T=I∪J and C={x∈T:dist(x,O)≤1}; let c=|C|≤|O|+2. Let H_sigma denote the product-Haar intrinsic Peter–Weyl Hilbert scale, sigma>sigma'≥0, z=exp(-2(sigma-sigma')), D=z∂_z, F_c=((1+z)/(1-z)^3)^c, G_c=(1-z)^(-c).

**Theorem.** Assuming the original-link locality (each link derivative acts on at most its two incident neighboring faces), the canonical local PW bound implies

```
||Gamma(f_I,g_J)||_{H_sigma'(T)}
 ≤ 48 c sqrt[(D²F_c)(z)(D²G_c)(z)] ||f_I||_{H_sigma(I)} ||g_J||_{H_sigma(J)}.
```

With the established free-electric centered inverse bound ||K_T^{-1}P0||≤1/3 in this scale, the coefficient 48 becomes 16 after applying K_T^{-1}P0.

**Proof.** Put E=I\C, F=J\C. They are disjoint. A common original-link derivative affecting both inputs is supported entirely within C: a link crossing the boundary of O has at most one additional face on either side. Hence Gamma acts only on C, leaving disjoint spectator variables E and F untouched. Expand f and g in respective orthonormal PW-weighted spectator bases: f=Σ_alpha e_alpha(E)f_alpha(C), g=Σ_beta g_beta(C)h_beta(F). Then Gamma(f,g)=Σ_alpha,beta e_alpha h_beta Gamma_C(f_alpha,g_beta). The spectator pairs are orthogonal in H_sigma'(T), and sigma'≤sigma. Apply the established c-face PW bilinear bound to each coefficient pair, square, sum, and factor the two squared coefficient sums. Apply centered PW inverse for the second assertion. Thus only c enters the constant, not |T|.

**Limits.** For I=J=T, c=|T|, so full-overlap radius growth is **unchanged**. Repeated self-overlaps and fully nested interactions remain in the connected recurrence. This theorem does not prove a rooted-support sum, a radius allocation, an ordinary perturbative convergence radius, convergence at lambda=1, the Penrose signed-current condition, or any continuum Yang–Mills theorem. Gevrey bounds remain formal. A sign correction in the physical original-link convention affects low-order coefficients but not this magnitude estimate.

**Prior work:** R3_IR_PW_ANALYTIC_BILINEAR_2026-11-01.md; R3_IR_PW_SUPPORT_SENSITIVE_2026-11-01.md; R3_IR_PW_RADIUS_MAJORANT_OBSTRUCTION_2026-11-01.md; R3_IR_CONNECTED_RECURRENCE_AUDIT_2026-11-01.md; and the P1 operator correction chain. The extended proof and a deterministic 4,082-pair locality audit plus 100 tensor regression checks are in the companion conversation archive R3_IR_PW_OVERLAP_COLLAR_TENSORIZATION_2026-11-01.zip. Archive preservation in GitHub/Library remains a separate verification obligation.
