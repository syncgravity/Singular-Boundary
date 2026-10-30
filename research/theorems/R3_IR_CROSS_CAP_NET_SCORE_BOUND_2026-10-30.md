# R3-IR: Cross-cap net-score bound for the completed Wilson cage

**Date:** 2026-10-30. **Status:** Exact finite-volume conditional theorem for the true deleted-target marginal; physical uniform estimate remains open.

Let the deleted-face ground-state holonomy have center-symmetric SU(2) radial density
\[
d\nu(u)=\frac2\pi\sin^2u\,\psi(u)^2du,\quad 0\le u\le\pi,\quad\psi(u)=\psi(\pi-u)>0,
\]
normalized to one. This is the genuine complete-cage target marginal, not the isolated 2D Euclidean boundary law. For \(0<a<\pi/2\), put \(m(a)=(a-\sin a\cos a)/\pi\) (the one-center Haar cap mass), and introduce the **net cross-cap log-score excursion**
\[
D_a=\sup_{0\le u\le a,\ a\le v\le\pi/2}
   [\log\psi(v)-\log\psi(u)]_+.
\]
Then
\[
\boxed{\Pr_\nu\{0\le u\le a\}\ge
\frac{m(a)}{2m(a)+e^{2D_a}(1-2m(a))}
\ge m(a)e^{-2D_a}.}\tag{CC}
\]

**Proof.** Every \(u\in[0,a]\), \(v\in[a,\pi/2]\) satisfies \(\psi(v)^2\le e^{2D_a}\psi(u)^2\). Write \(A=\int_0^a w\psi^2\), \(B=\int_a^{\pi/2}w\psi^2\), \(w=2\sin^2u/\pi\). Center symmetry gives \(A+B=1/2\). Integrating pairwise, \(B m(a)\le e^{2D_a} A (1/2-m(a))\). Solving for A yields CC. The last estimate follows because \(2m+e^{2D}(1-2m)\le e^{2D}\). QED.

For absolutely continuous \(\log\psi\), the previously used adverse signed-current budget \(T=\int_0^{\pi/2}[(\log\psi)'(u)]_+du\) controls \(D_a\le O\le T\), where \(O=\sup_{0\le u\le v\le\pi/2}[\log\psi(v)-\log\psi(u)]_+\). This is strictly weaker data: for \(\psi_n(u)=c_n e^{\varepsilon\cos(2nu)}\), reflected about \(\pi/2\), fixed \(\varepsilon>0\) and integer n, \(D_a\le2\varepsilon\) for every cap while \(T\) grows linearly in n. These smooth center-even densities are algebraic counterexamples to treating T as necessary; **they are not claimed to be actual Wilson deleted vacua**.

**Variational implication (conditional):** In any already established magnetic-deletion variational inequality using only lower survival \(F(a)\ge m(a)e^{-2T}\) at its chosen radius, one may replace T by \(D_a\) *with the same remaining hypotheses, coefficients, and constants*. Thus along the previously specified Penrose coefficient scaling, provided the original deletion bound applies and \(a_h=1/\kappa_h\) is its admitted radius,
\[
\Delta_f\le Ch^{-1}[1+\log(1/h)+D_{f,a_h}].
\]
A new sufficient condition is \(\sup_{f\in D_R}D_{f,a_h}=o(h^{-1/4})\), implying \(\sup_f\Delta_f=o(h^{-5/4})\). The hypothesis is **OPEN for the actual fully coupled Wilson vacua**. No spectral gap, center-cap half-Haar, or continuum existence is inferred.

**Next physical gate:** estimate the *net* conditional score excursion
\[
D_{f,a}=\sup_{u\le a\le v\le\pi/2}\left[-\frac4{A_f}\int_u^v\frac{J_f(\cos s)}{\sin s}\,ds\right]_+
\]
via the exact physical score Ward identity, including coupled neighbors and refinement constants. This preserves cancellations before taking the positive part; Fisher/energy bounds alone do not furnish the required estimate.
