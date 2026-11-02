# Exact original-link strip geometry and conditional third-order summability — 2026-11-02

For N open straight square SU(2) faces f_m, each original-link face support is E(f_m)={v_m,v_(m+1),t_m,b_m}; there are 3N+1 links. The residual bond j has seven-link support S_j=E(f_j)∪E(f_(j+1)). Future links beyond prefix through face k are T_>k=E\(∪_(m≤k) E(f_m)). For **j<k**, in the link-adjacency graph where links are adjacent precisely when they bound a common plaquette, the exact distance is

**d_link(S_j,T_>k)=k−j**.

This follows from the one-column-per-graph-step lower bound, attained by the vertical-link chain ending at the next top horizontal link. Exact independent BFS checks passed in 9,880 cases for N=3,...,40, including strip reflection.

Conditionally on the preceding analytic weighted L4 and Bochner estimates, every mixed third ground-energy derivative for distinct i<j<k has bound **|E_ijk|≤C3 (5/6)^max(j−i,k−j)** by choosing the right/left extremal bond and reflection; for two labels i<j, |E_iij|,|E_ijj|≤C3(5/6)^(j−i). Here C3=6.3733515498068958e−5. For all equal, |E_iii|≤1/6500352.

The **unordered-configuration** sums are ≤55(N−1) for distinct triples and ≤5(N−1) for pairs, by exact geometric series Σ_(a,b≥1) q^max(a,b)=q(1+q)/(1−q)^2=55 and Σ_(d≥1)q^d=5 for q=5/6.

**Multiplicity correction:** E_ijk itself already sums the six resolvent orderings, but the third derivative of the **single-parameter all-bond** ground energy H_N(t)=L_N+tΣw_j sums all ordered bond labels. Each distinct unordered triple enters six times; each distinct pair enters six (3+3) times. Therefore

**|E_N'''(0)|≤(N−1)[360 C3+1/6500352]≈0.02294421941713(N−1).**

This is a conditional **third-order reference-point extensivity** theorem, not all-order convergence or a nonzero-t interacting spectral-gap theorem. Full detailed graph proof, exact-rational verification script, log and SHA256 manifest reside in Library /The Singular Boundary/Proof Audits. Interacting lambda=1 and continuum Yang–Mills mass gaps remain open.