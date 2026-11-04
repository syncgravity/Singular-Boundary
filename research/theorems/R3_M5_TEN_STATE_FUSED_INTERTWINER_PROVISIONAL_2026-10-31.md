# R3-IR-575 — Ten-state M5 fused-intertwiner extension: provisional Ritz result

Date: 2026-10-31.

Combined the nine two-loop spin-character product functions chi_{a/2}(U_A) chi_{b/2}(U_B), a,b=0,1,2, with the fused trace state F=(2/sqrt3)[chi_{1/2}(U_A U_B)−chi_{1/2}(U_A)chi_{1/2}(U_B)/2]. The resulting ten trial vectors are gauge invariant and numerically Haar orthonormal. The derivation retains the **full** original candidate M5 prism inverse-Whitney link matrix and rooted quaternion transport derivative form, not an independently diagonalized kinetic approximation.

An explicit 24^3 quaternion-design tensor contraction computes all 10×10 electric, Wilson p_A, Wilson p_B, and resulting Ritz matrices. The spin-character magnetic multipliers use the action-derived coefficients b_A and b_B from R3-IR-562. The Haar Gram discrepancy is at most 2.3e−15, and the previously exact fused electric coupling E_(chi_A chi_B,F)=24.65408201758688 agrees with R3-IR-574. The new ten-state **provisional** first Ritz gap is 58.5160217280032; the independently computed nine-state exact-degree gap was 58.744154660340655, a decrease of approximately 0.2281329323 under this enlargement.

A second 24-cell quadrature, independently rotated by a deterministic orthogonal 4×4 matrix, agrees with the first to 3.98e−13 on the electric matrix and 5e−14 on the gap. This supports numerical consistency but DOES NOT certify the higher-degree polynomial moments: the 24-cell rule is guaranteed exact only through degree five, while some ten-state gradient products may reach degree eight. A direct 120^3 600-cell run was attempted but exceeded the available execution time. Thus the **new ten-state Ritz matrix and gap are provisional**, not exact-form Haar contractions. This distinction must be preserved even though the lower-cutoff components are independently certified.

The ten-state basis is a nested enlargement of the nine-state two-loop basis, but it is NOT the combined 18-state three-loop basis and does not add the third disjoint Wilson loop. Convergence of full Gauss-invariant spectrum, calibrated physical h-refinement, and continuum Yang–Mills mass gap are unproved.

Execution and data stored in ChatGPT Library /The Singular Boundary/Source/: compute_m5_ten_state_fused.py, m5_ten_state_fused_24cell_provisional_2026-10-31.json, and m5_ten_state_rotated_24cell_2026-10-31.json. Follow-up: implement exact Haar moment-factorization or optimized 600-cell tensor contraction, then incorporate the fused intertwiner into the 18-state three-loop basis.
