# R3-IR — Three-dimensional weak-coupling threshold and continuum scaling audit (2026-11-04)

**Status:** audited conditional application of published weak-interaction stability to periodic cubic original-link SU(2) rotor lattices. This is *not* a numerical uniform gap threshold, open-boundary theorem, physical coupling z=1 result, or continuum Yang–Mills mass-gap proof. Full note, exact verifier and hashes: current conversation ZIP R3_IR_3D_QUANTITATIVE_THRESHOLD_AND_CONTINUUM_SCALING_AUDIT_2026-11-04.zip.

## Correctly normalized Yarotsky support embedding

Let each lattice vertex x hold the three outgoing SU(2) link rotors, with free on-site operator k_x and gap 3/4. For the three oriented plaquettes anchored at x, the union of original-link site supports lies in \(\Lambda_0+x\), \(\Lambda_0=\{0,e_1,e_2,e_3\}\). Write
\[
\bar H=K-\frac12\sum_p z_p\chi_1(U_{\partial p}),\qquad K=\sum_xk_x.
\]
For **periodic cubic volumes** take
\[
h_x=\frac43\sum_{y\in\Lambda_0+x}k_y,\quad
\phi_x=-\frac83\sum_{p\text{ anchored at }x}z_p\chi_1(U_{\partial p}).
\]
Each h_x has a unique product ground state **and gap at least 1 on all four sites** in its support, while \(\|\phi_x\|\le16z_{\max}\). Counting each k_x four times gives \(\sum_x(h_x+\phi_x)=(16/3)\bar H\). If \(\beta_Y(3,\Lambda_0)>0\) denotes Yarotsky 2006 Theorem 1's admissible constant in this normalized bounded-perturbation case, the symbolic sufficient homogeneous threshold is
\[
\boxed{16|z|<\beta_Y.}
\]
The theorem gives no published numerical value for this \(\beta_Y\) in its statement. **Do not report a computed numerical \(z_*\)**. The 2006 proof states its primary finite-volume result for periodic cubic volumes and translation-invariant interactions. The earlier claimed automatic extension to arbitrary open finite cubes and inhomogeneous couplings needs separately justified boundary/inhomogeneity handling. The 2022 Henheik–Teufel–Wessel local-stability paper is not itself a numerical global gap estimate.

## Physical coupling translation: regime mismatch

In the 3+1D Kogut–Susskind convention
\[
H_{\rm KS}=\frac{g_0^2}{2a}K+\frac1{g_0^2a}\sum_p[2-\chi_1(U_{\partial p})].
\]
Up to an additive constant, dividing by \(g_0^2/(2a)\) yields
\[
\bar H=K-\frac z2\sum_p\chi_1(U_{\partial p}),\qquad
\boxed{z=4/g_0^4},\quad
\boxed{\Delta E_{\rm phys}=(g_0^2/2a)\Delta\bar H}.
\]
The symbolic magnetic weak-coupling threshold becomes \(64/g_0^4<\beta_Y\), equivalent to \(g_0>(64/\beta_Y)^{1/4}\), **large bare gauge coupling**. In this convention z=1 corresponds to g_0=sqrt(2). Along the expected asymptotically free 4D continuum trajectory \(g_0(a)\to0\), so \(z(a)\to\infty\), outside every fixed small-z stability neighborhood. With one-loop \(b_0=11/(24\pi^2)\), \(g_0^{-2}\sim2b_0\log(1/a\Lambda)\) and \(z\sim16b_0^2\log^2(1/a\Lambda)\). This is a limitation of **this proof regime**, not a no-go theorem for a continuum interacting gauge theory.

## Literature, tests and next target

Yarotsky (2006), Theorem 1: https://arxiv.org/html/math-ph/0412040
Henheik–Teufel–Wessel (2022): https://link.springer.com/article/10.1007/s11005-021-01494-y
Physical Hamiltonian normalization (D'Andrea et al., Phys. Rev. D 109, 074501 (2024)): https://doi.org/10.1103/PhysRevD.109.074501
Asymptotic freedom overview: https://www.cphysics.org/article/07611.html

Exact checker passed **234,642** normalization and cubic-incidence checks; it does not verify Yarotsky's theorem. Prior open-cube simple min–max estimate remains separate and volume dependent.

Next objective: extract numerical \(\beta_Y\) by tracking cluster combinatorics *with all constants and boundaries*, while separately building a magnetic-side or renormalization-group method capable of addressing \(z\to\infty\), maintaining physical-unit gap and OS/Wightman continuum requirements.