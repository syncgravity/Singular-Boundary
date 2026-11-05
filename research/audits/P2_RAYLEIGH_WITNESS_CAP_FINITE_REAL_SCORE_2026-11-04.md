# P2: the Rayleigh dual witness is asymptotically insufficient; true finite-strip SU(2) score continues for all real coupling

**Research audit, 2026-11-04.** The corrected original-link finite straight-square SU(2) model in face-coordinate Peter–Weyl norms. Expanded independently executed proof/checker package and integrity-verified archive: conversation artifact \`p2_dual_cap_finite_real_2026-11-04.zip\`. **Do not confuse an upper bound on a LOWER certificate with an upper bound on the physical Schatten response.** No infinite-volume Borel summability, 4D continuum reconstruction or Yang–Mills mass gap is proved.

## P2 physical: all-width upper cap on the particular P-44/P-46 full-inverse Rayleigh LOWER witness

For even N≥4 and m≥3, let F_N be the balanced residual Gauss-twirled even-width outer intertwiner. Its separate inner input is the gauge-invariant chi_m(U_j) at each j; distinct (j,l), l=m±1, produce disjoint nonconstant PW output degree sectors. Define the *known valid lower certificate* for the full electric inverse response, omitting the global history discount exp(−κ):
\[
L_{N,m}=\sum_{j=1}^N\sum_{l=m\pm1}\frac{(l+1)^2}{4(m+1)^3}
\frac{\|Y_{j,l}\|_{S2}^2}{D_{j,l}(1+\alpha_{j,l})\|Z_{j,l}\|_{op}},
\]
where Y=T(Z) is the true physical Gauss twirl of the untwirled two-bond-collar Poisson source, D=3(N−1)+l(l+2), alpha≤1/2. A zero source contributes zero. The previous P-44 theorem proves 0≤L≤R, where R is the **true unknown complete-inverse physical Schatten response**, all in the same face-PW first-moment normalization.

**New exact all-even-width theorem**
\[
\boxed{L_{N,m}\le
\frac{5N(m+2)^4}{(m+1)^3(N-2)(3N+m^2-4)}.}\tag{1}
\]
**Proof:** P-38/P-42 exact two-bond cancellation makes Z=Z_C⊗(rank-one untouched spectators), where c=|C|≤3 and its local Hilbert dimension ≤4(l+1). Local CG compression is operator-norm contractive. The scalar Poisson source multiplier is beta_l=[3+m(m+2)−l(l+2)]/2, with beta_(m−1)=m+2, beta_(m+1)=−m. Each of at most two mixed original-link bonds contributes operator norm at most 3(l+1)/4 (the combined output and input term). Hence
\[
\|Z\|_{op}=\|Z_C\|_{op}\le|\beta_l|+\frac32(l+1)\le\frac52(m+2).
\]
The exact one-Haar Hilbert–Schmidt identity is \|Y\|2²=<Z,TZ>. Every untouched alternating spectator factor has modulus t, where t=|g_11|² is Haar-uniform on [0,1]. Cauchy–Schwarz bounds the collar overlap by \|Z_C\|2². Therefore
\[
\|Y_{j,l}\|_2^2\le\frac{\|Z_C\|_2^2}{N-c+1}
\le\frac{4(l+1)\|Z_C\|_{op}^2}{N-2}.
\]
Use the exact sector weight w_l=(l+1)²/[4(m+1)³], D≥3N+m²−4, 1+alpha≥1, l+1≤m+2, and the 2N disjoint output sectors to conclude (1). At N=m²+O(1), even:
\[
\boxed{L_{N,m}\le\frac{5}{4m}(1+O(1/m)).}\tag{2}
\]
**Logical status:** the **specific dual witness** is proven unable to certify a diverging same-grade physical response in that target regime. This is NOT an upper bound on R and NOT proof that R is bounded. The earlier ordinary-precision sweep of L close to 0.032/m lies well within this conservative ~1.25/m cap. The direct rational regression validates exact local coefficients through m=9999 and cap scaling through m=1024.

## Actual sign-sensitive SU(2) score: real-λ continuation at every fixed finite width

On the compact connected manifold M_N=SU(2)^N, use the genuine corrected original-link electric generator K_N, a nonnegative elliptic self-adjoint second-order sum of squares, and the bounded real gauge-invariant magnetic source V_N=−(1/2)Σ_j chi_1(U_j), ||V_N||∞≤N. Put H_N(λ)=K_N+λV_N, λ∈R.

The corrected electric block quadratic form satisfies K_c≥D_c/2 with D_c=Σ_i n_i(n_i+2). If D=3, the sector has one fundamental active face and K=3 exactly; otherwise D≥6 and K≥3. Thus the **free first gap is exactly 3**, independent of finite N. For each *fixed* N and every real λ, uniform ellipticity on the compact connected manifold and the positivity-improving heat kernel/Feynman–Kac guarantee a simple, strictly positive smooth ground eigenfunction ψ_(N,λ), with isolated lowest eigenvalue E0,N(λ). The bounded potential is an analytic type-A perturbation. Its isolated simple ground spectral projection, positive eigenfunction and ground energy are **locally real-analytic at every real λ**. Elliptic regularity and positivity permit a normalized log score
\[
S_N(\lambda)=\log\psi_{N,\lambda}-\int\log\psi_{N,\lambda}\,d\mu
\]
which is smooth in face variables, residual-Gauss-invariant and real-analytic along the *whole real coupling axis*. It satisfies the genuine score equation because the geometric carré du champ \(\Gamma_K(f,g)=(fKg+gKf-K(fg))/2\) obeys \(e^{-S}Ke^S=KS-\Gamma_K(S,S)\), giving the previously formal magnetic-score recursion near λ=0.

The fixed-volume interacting spectral gap is **positive** for every real λ, but generally depends on N and λ:
\[
\boxed{\Delta_N(\lambda)>0,\qquad \Delta_N(\lambda)\ge3-2N|\lambda|.}\tag{3}
\]
The second inequality follows by min–max and ||V_N||∞≤N and need not be positive for large Nλ. On each fixed N and compact real λ interval, continuity yields an N-dependent positive minimum; NO thermodynamic-uniform bound is proved.

**Exact one-face character cross-check:** the normalized-Haar class characters chi_n form an orthonormal basis, with Kchi_n=n(n+2)chi_n and chi_1chi_n=chi_(n+1)+chi_(n−1), chi_(-1)=0. Thus the actual H_1(λ) is the tridiagonal Jacobi matrix diag[n(n+2)] plus offdiagonal −λ/2. At λ=1, rigorously Δ_1(1)≥1; converged finite character cutoffs give ordinary-precision E0≈−0.081941823375 and Δ≈3.113863811504. A separate exact-rational signed score verifies 24 orders with S1=chi_1/6, S2=−chi_2/288, S3=−chi_1/648+chi_3/6480.

**The distinction from P-47 is fundamental:** Pringsheim's positive-axis Borel singularity applies to the *nonnegative scalar comparison recurrence*, not the actual signed SU(2) score. The all-real finite-volume continuation is continuation in physical λ of a *finite-volume positive ground state*; it is NOT a global positive Borel-ray theorem for the infinite strip, an OS reconstruction or a 4D continuum gap.

## Checks and next objectives

The companion archive contains the expanded complete proof; \`verify_dual_cap.py\` (19,994 exact local source inequalities and rational width/spin cap through m=1024), \`verify_finite_real.py\` (one-face tridiagonal actual H_1 eigenvalue convergence for λ=0,0.25,0.5,1,2,4,10 and exact minmax free-gap bound), \`verify_oneface_score.py\` (24 exact rational sign-sensitive SU(2) score orders), passing logs, SHA256SUMS.txt and integrity-tested ZIP.

**Next physical gate:** obtain a dual witness that probes high-rank output Schatten mass, or prove a genuine trace-norm upper estimate for R_(N,m) along N≈m². The old Hilbert–Schmidt Rayleigh witness is conclusively too weak for divergence.

**Next analytic gate:** investigate uniform-in-N continuation or an infinite-volume Borel-ray estimate for the actual sign-sensitive score; local physical real-λ analyticity for each N does not supply either.

**Scientific status: 4D continuum Yang–Mills existence and positive physical mass gap OPEN.**