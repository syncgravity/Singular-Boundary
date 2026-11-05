# P2 — Dimension-free induced Schatten-1 electric contraction and second-time thermodynamic kernel regularity

**Private research audit, 2026-11-04.** Corrected original-link SU(2) finite open straight strip, balanced residual Gauss-twirled high-spin singleton source, *unchanged* independent-face PW nuclear norm. Complete expanded proof, three executed independent scripts, logs, SHA-256 manifest and verified archive preserved in Library under \`The Singular Boundary/Proof Audits/p2_s1_contractivity_2026-11-04.zip\`, with expanded report \`P2_SCHATTEN1_CONTRACTION_AND_SECOND_TIME_REGULARITY_2026-11-04.md\`. **No full physical high-spin response asymptotic, efficient complete Schur-Gram evaluation at N≈m², interacting infinite-volume automorphism or 4D Yang–Mills mass-gap theorem is claimed.**

## P-67. Trace-ideal bond estimate removes exponential Fourier-dimension loss

In a physical output tuple \(\mathbf c=(1,\ldots,1,\ell,1,\ldots,1)\), \(\ell=m\pm1\), the *actual corrected original-link electric* PW coefficient superoperator is
\[
K_{\mathbf c}(X)=D_{\mathbf c} X+H_{\mathbf c}(X),\quad D_{\mathbf c}=\sum_i n_i(n_i+2),\quad
H_{\mathbf c}(X)=-2\sum_{i=1}^{N-1}\sum_{a=1}^3 J_i^a X J_{i+1}^a.
\]
The spin generators on the two tensor ends have \(\sum_a(J_i^a)^2=j_i(j_i+1)I\), \(j_i=n_i/2\), in their appropriate left/right actions. For **any trace-class matrix X**, expanding X into rank-one singular-value terms and applying Cauchy–Schwarz to the two arrays of \(J_i^a u\) and \(J_{i+1}^a v\) proves
\[
\boxed{\left\|-2\sum_a J_i^a X J_{i+1}^a\right\|_1
\le2\sqrt{j_i(j_i+1)j_{i+1}(j_{i+1}+1)}\,\|X\|_1.}\tag{1}
\]
Thus the *same* sector bond-count bound that previously controlled the HS action **also bounds the induced S1→S1 map**, with no \(\sqrt{d_\mathbf c}\) conversion:
\[
\eta_{\rm int,\ell}=
\frac{3(N-3)+2\sqrt{3\ell(\ell+2)}}{2D_\ell},\quad
\eta_{\rm end,\ell}=
\frac{3(N-2)+\sqrt{3\ell(\ell+2)}}{2D_\ell},\quad
D_\ell=3(N-1)+\ell(\ell+2).
\]
The certified ratios are <1/2. Therefore the **complete actual corrected K inverse** admits a trace-norm convergent Neumann expansion with dimension-free error:
\[
\boxed{\|K^{-1}Y-D_\ell^{-1}\sum_{p=0}^{q}(-H/D_\ell)^pY\|_1
\le\frac{\|Y\|_1}{D_\ell}\frac{\eta_{j,\ell}^{q+1}}{1-\eta_{j,\ell}}.}\tag{2}
\]
This is a genuine induced trace-ideal result, NOT the Chebyshev spectral S2 tail from P-65. A Chebyshev polynomial's uniform Hilbert-space spectral error should **not** be used for S1 contraction without a separate proof.

The *actual Gauss-invariant physical source* P-56 rank estimate and P-44/P-63 source HS bound give
\[
\mathrm{rank}(Y_{j,\ell})\le r_{N,m,\ell}:=13(m+1)\left\lfloor\frac{(N+\ell+1)^2}{4}\right\rfloor,\qquad
\|Y_{j,\ell}\|_1\le \sqrt{r_{N,m,\ell}}\,
\frac52(m+2)\sqrt{\frac{m+1}{N+1}}.
\]
Sum (2) with the **existing** disjoint physical first-moment Fourier weights \(w_\ell=(\ell+1)^2/[4(m+1)^3]\). The full extensive true physical response R and q-depth approximation R[q] satisfy
\[
\boxed{|R_{N,m}-R_{N,m}^{[q]}|\le
\sum_{\ell=m\pm1}\frac{w_\ell\sqrt{r_{N,m,\ell}}H_{N,m}}{D_\ell}
\left[2\frac{\eta_{\rm end,\ell}^{q+1}}{1-\eta_{\rm end,\ell}}
+(N-2)\frac{\eta_{\rm int,\ell}^{q+1}}{1-\eta_{\rm int,\ell}}\right],}\tag{3}
\]
\(H_{N,m}=\frac52(m+2)\sqrt{(m+1)/(N+1)}\). Equation (3) has **polynomial**, not exponential, width/spin prefactors. It also gives a conservative **true physical upper bound** by replacing \(q+1\) with 0 in the geometric numerator and treating the q-depth approximation as zero. Along even N=m²+O(1), this yields
\[
\boxed{R_{N,m}\le(\sqrt{13}/4+o(1))m^2,}\tag{4}
\]
in the explicitly stated undiscounted first-moment norm, not a uniform same-grade closure statement. The corresponding q-depth envelope is
\[
\boxed{\Delta_q^{S1}\le(\sqrt{13}/4+o(1))m^2(3/8)^{q+1},\quad N=m^2+O(1).}\tag{5}
\]
A **sufficient, NOT necessary** absolute-error \(\epsilon>0\) inverse depth is therefore
\[
\boxed{q_{\rm sufficient}=\frac{2\log m+\log(1/\epsilon)+O(1)}{\log(8/3)}
=O(\log m+\log(1/\epsilon)).}\tag{6}
\]
This sharply supersedes the old P-63 Neumann O(N) and P-65 Chebyshev O(N) *sufficient* bounds, whose exponential dimension conversion was avoidable. It does **not prove polynomial computation of the complete inverse**: the existing raw corrected-source q-term rank expansion is \([3(N-1)]^{O(q)}\), which at q=O(log m) can be quasi-polynomial. The high-spin nuclear norm's actual growth/decay remains unresolved.

**Regression, ε=10⁻⁶:** formula (3) gives sufficient q for (m,N)=(3,10):18, (4,16):19, (6,36):19, (10,100):20, (20,400):20, (40,1600):21, (80,6400):23, (160,25600):24, (300,90000):25, (1000,1000000):28. The last cases evaluate the **analytic bound only**, not million-face Fourier matrices. Independently, 64 complex test matrices over actual spin-link actions pass (1), and both *true corrected Gauss-invariant N=2,m=3 CG physical source channels* l=2,4 pass (2) through q=12 when compared with independently solved dense K inverses. Numerical values are ordinary precision, while the displayed operator inequalities are analytic.

## P-68. Second-order time regularity of the P-64/P-66 protected positive-frequency correlations

P-64 constructs subsequential *matrix-positive*, nonnegative-frequency excitation measures \(\mu_\infty^{F,G}\) for bounded local Casimir-projection observables F,G. Put \(L_F=2|\lambda||W_F|\|F\|\), \(L_G=2|\lambda||W_G|\|G\|\). The uniform second moments, weak limiting lower semicontinuity, and the Cauchy–Schwarz inequality for the corresponding positive matrix spectral measure give
\[
\boxed{\int_0^\infty E^2\,|d\mu_\infty^{F,G}(E)|\le L_F L_G.}\tag{7}
\]
Thus for \(C_\infty^{F,G}(t)=\int_0^\infty e^{-itE}d\mu_\infty^{F,G}(E)\), differentiation under the integral is valid **twice**: \(C_\infty\in C^2(\mathbb R)\), and \(\sup_t|C_\infty''(t)|\le L_F L_G\).

Using the **actual first-frequency interacting local commutator identity** from P-66,
\[
C_\infty^{F,G}(0)=\omega_\infty(F^*G),\qquad
C_\infty'^{F,G}(0)=-i\omega_\infty(F^*\delta_{\rm loc}(G)),\quad
\delta_{\rm loc}(G)=\lambda[V_{W_G},G],
\]
and \(|e^{-itE}-1+itE|\le(tE)^2/2\), we get the *uniform thermodynamic second-order time-error certificate*
\[
\boxed{\big|C_\infty^{F,G}(t)-\omega_\infty(F^*G)
+it\,\omega_\infty(F^*\delta_{\rm loc}(G))\big|
\le\tfrac12t^2 L_F L_G.}\tag{8}
\]
This **does not identify the second derivative** with a second interacting local commutator (which need not be bounded or within the protected algebra). It **does not construct** one interacting infinite-volume automorphism, an invariant core, unique vacuum, clustering, uniform positive gap, positive-axis Borel sum or 4D continuum mass gap. Genuine one-face SU(2) Jacobi tests across four real couplings and three Fourier cutoffs pass the cross-second-moment and Taylor estimates.

## Next gates

**Physical:** apply the now logarithmic sufficient q-depth to actual N≈m² corrected source tensor coefficients and P-60 exact Wigner projected Grams, compressing the quasi-polynomial q-term rank or proving the nuclear asymptotic by another method. **Dynamical:** build an invariant gauge-compatible energy-regularized infinite-volume algebra with generator; P-68 proves only \(C^2\) protected temporal kernels, not such dynamics. **Continuum 4D Yang–Mills existence and positive mass gap: OPEN.**