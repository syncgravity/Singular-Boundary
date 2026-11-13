# PF-I16 — Dobrushin control of the dressed third-order tree coefficient

**Date:** 2026-11-13  
**Status:** conditional finite-product spatial tree estimate for the complete six-permutation third-order coefficient. The new Dobrushin influence estimate is derived from the corrected single-face first-derivative bound and universal incidence inventory. The final tree estimate additionally uses the corrected pointwise derivative-flow theorem, which remains conditional on the refined face-pullback and finite-product Kato–Bochner comparison. This is not a theorem for the actual interacting Wilson vacuum, an all-orders activity theorem, a physical-time theorem, or a Yang–Mills mass-gap result.

## 1. Direct cumulant representation

Let
\[
d\nu_\Phi=Z_\Phi^{-1}e^{2\Phi}dU,\qquad
\Phi=\sum_f s_f(H_f),
\]
on the finite accepted-link product \(M=\prod_{e\in E}\mathrm{SU}(2)_e\). Let \(L_\Phi\) be the positive reversible generator, \(G=L_\Phi^{-1}Q\), and let \(r_i\) be centered residuals supported on \(S_i\). Put
\[
u_i=Gr_i,\qquad
A_{i,b}=\|D_br_i\|_\infty,\qquad
M_i=\sum_{b\in S_i}A_{i,b},\qquad
B_i=\|r_i\|_\infty.
\]
All \(u_i\) are centered. Self-adjointness and the centering projection give the exact identity
\[
T_{ijk}:=\nu_\Phi[r_iGQ(r_jGr_k)]
=\nu_\Phi[u_i r_j u_k]
=\operatorname{cum}_{3,\nu_\Phi}(u_i,r_j,u_k).
\tag{1.1}
\]
Thus each ordered term in the six-permutation coefficient is already a third cumulant. This route estimates the full ordered term directly; it does not discard or estimate away the conditional boundary mean in the alternative conditional decomposition.

The required derivative-flow input is
\[
\|D_eu_i\|_\infty
\le \lambda^{-1}\sum_{b\in S_i}e^{-\mu d(e,b)}A_{i,b},
\qquad \mu=\log25,
\tag{1.2}
\]
together with the local oscillation consequence
\[
\|u_i\|_\infty\le \frac{26\pi}{\lambda}M_i.
\tag{1.3}
\]
These are conditional PF-I16 inputs, as recorded in the corrected reversible-flow theorem.

## 2. Dobrushin influence matrix for the dressed reference measure

Treat original links as sites, with single-site conditional law
\[
\nu_{\Phi,e}(dU_e\mid\eta)
=Z_e(\eta)^{-1}
\exp\!\left(2\sum_{f:e\in\partial f}s_f(H_f(U_e,\eta))\right)dU_e.
\]
Let \(n_{ez}\) be the number of accepted faces containing both links \(e,z\), and define the Dobrushin influence coefficient
\[
C_{ez}=\sup_{\eta,\eta':\,\eta_w=\eta'_w\ (w\ne z)}
\|\nu_{\Phi,e}(\cdot\mid\eta)-\nu_{\Phi,e}(\cdot\mid\eta')\|_{\rm TV},
\qquad C_{ee}=0.
\]
Only faces containing both \(e,z\) contribute.

Assume the corrected isolated-face derivative estimate
\[
\|D_zs_f(H_f)\|_\infty\le2\beta_f,\qquad
\beta_*:=\sup_f\beta_f\le\frac{2b_0}{a_0}.
\tag{2.1}
\]
If two outside configurations differ only at \(z\), the radius-two \(\mathrm{SU}(2)\) diameter \(2\pi\) gives, for each shared face,
\[
\sup_{U_e}|2s_f(H_f(U_e,\eta))-2s_f(H_f(U_e,\eta'))|
\le8\pi\beta_*.
\]
The oscillation in \(U_e\) of this log-density difference is therefore at most \(16\pi\beta_*\). The elementary density-ratio inequality
\[
\|\rho-\rho'\|_{\rm TV}\le\tanh\!\left(\frac{\operatorname{osc}\log(d\rho/d\rho')}{4}\right)
\]
then yields
\[
C_{ez}\le n_{ez}\tanh(4\pi\beta_*).
\tag{2.2}
\]
The universal incidence inventory has at most eight accepted faces at each link, with three other links per face. Hence
\[
\sum_z n_{ez}\le24.
\tag{2.3}
\]

At the corrected weak-coupling threshold \(b_0/a_0\le1/50000\), (2.1) gives \(\beta_*\le1/25000\). For the weighted matrix norm
\[
\|C\|_\mu:=\sup_e\sum_z C_{ez}e^{\mu d(e,z)},\qquad \mu=\log25,
\]
(2.2)–(2.3) imply
\[
\|C\|_{\log25}
\le600\tanh(4\pi\beta_*)
\le\frac{12\pi}{125}
<\frac{264}{875}<1.
\tag{2.4}
\]
The second inequality uses \(\tanh x\le x\), and the strict rational bound uses \(\pi<22/7\).

Consequently the Dobrushin resolvent
\[
\mathsf D=(I-C)^{-1}=\sum_{n\ge0}C^n
\]
is well-defined and has weighted norm
\[
\|\mathsf D\|_{\log25}\le\frac1{1-\|C\|_{\log25}}
<\frac{875}{611}=:D_*.
\]
In particular,
\[
\boxed{\mathsf D_{ez}\le D_*e^{-(\log25)d(e,z)}.}
\tag{2.5}
\]
This is a mixing estimate for the finite-volume **dressed reference measure** \(\nu_\Phi\). It is not a Dobrushin estimate for the true interacting Wilson-vacuum measure.

## 3. Föllmer covariance inequality and pair convolutions

For a finite product Gibbs measure satisfying the Dobrushin condition, the Föllmer covariance estimate states that bounded observables \(F,H\) satisfy
\[
|\operatorname{Cov}_{\nu_\Phi}(F,H)|
\le\frac14\sum_{e,z}\delta_eF\,\mathsf D_{ez}\,\delta_zH,
\tag{3.1}
\]
where \(\delta_eF\) is the full oscillation of \(F\) in link \(e\). We use the standard finite-volume form of this estimate (Föllmer, *A covariance estimate for Gibbs measures*, J. Funct. Anal. 46 (1982), 387–395, DOI 10.1016/0022-1236(82)90053-2).

The link diameter and (1.2) imply
\[
\delta_eu_i\le\frac{2\pi}{\lambda}
\sum_{b\in S_i}e^{-\mu d(e,b)}A_{i,b},
\qquad
\delta_er_j\le2\pi\,\mathbf1_{e\in S_j}A_{j,e}.
\tag{3.2}
\]
Write \(K_\mu(e,z)=e^{-\mu d(e,z)}\), and define
\[
\mathcal I(F,H)=\sum_{e,z}K_\mu(e,z)\delta_eF\,\delta_zH.
\]
The previously established shell-convolution estimates give
\[
P_2(a,c):=\sum_eK_\mu(a,e)K_\mu(e,c)
\le C_1e^{-\nu d(a,c)},\quad
C_1<25.511,\quad \nu=\frac12\log\frac{25}{23},
\tag{3.3}
\]
and
\[
P_3(a,c):=\sum_{e,z}K_\mu(a,e)K_\mu(e,z)K_\mu(z,c)
\le C_3e^{-\gamma d(a,c)},\quad
C_3<465.933,\quad \gamma=\frac14\log\frac{25}{23}.
\tag{3.4}
\]
Here \(C_3=C_1C_2\), with the conservative previously verified \(C_2<18.264\). No exponent is assumed to survive convolution unchanged.

Substitution of (3.2) into (3.3)–(3.4) yields
\[
\boxed{
\mathcal I(u_i,r_j)
\le\frac{4\pi^2C_1}{\lambda}M_iM_j
e^{-\nu d(S_i,S_j)},
}
\tag{3.5}
\]
and
\[
\boxed{
\mathcal I(u_i,u_k)
\le\frac{4\pi^2C_3}{\lambda^2}M_iM_k
e^{-\gamma d(S_i,S_k)}.
}
\tag{3.6}
\]
By (2.5), the right side of (3.1) is bounded by \(D_*/4\) times the corresponding \(\mathcal I\).

## 4. Three-cumulant tree estimate

For centered \(F_1,F_2,F_3\),
\[
\operatorname{cum}_3(F_1,F_2,F_3)
=\operatorname{Cov}(F_a,F_bF_c)
\]
for any choice of singleton label \(a\). The product oscillation satisfies
\[
\delta_z(F_bF_c)
\le\|F_b\|_\infty\delta_zF_c
+\|F_c\|_\infty\delta_zF_b.
\]
Therefore, for any singleton choice,
\[
|\operatorname{cum}_3(F_a,F_b,F_c)|
\le\frac{D_*}{4}
\left[
\|F_b\|_\infty\mathcal I(F_a,F_c)
+\|F_c\|_\infty\mathcal I(F_a,F_b)
\right].
\tag{4.1}
\]

Let \(\ell_{\rm MST}(S_i,S_j,S_k)\) be the length of a minimum spanning tree on the three support sets, using the link-overlap graph distance. Let \(L\) be the longer of its two edges. Removing that edge isolates one of the three support labels; by the cut property of a minimum spanning tree, both distances from the isolated support to the other two are at least \(L\). Also
\[
\ell_{\rm MST}\le2L.
\tag{4.2}
\]

Apply (4.1) with the isolated observable as the singleton.

* If the isolated observable is \(r_j\), use (1.3) and (3.5) twice. The result is at most
  \[
  \frac{52D_*\pi^3C_1}{\lambda^2}
  M_iM_jM_k\,e^{-\nu L}.
  \]
* If the isolated observable is \(u_i\) or \(u_k\), use (3.5) for the residual-resolvent pair and (3.6) for the resolvent-resolvent pair. Since both cross-cut distances are at least \(L\), the result is at most
  \[
  \frac{D_*}{\lambda^2}
  \left(\pi^2C_3B_jM_iM_k
  +26\pi^3C_1M_iM_jM_k\right)e^{-\gamma L}.
  \]

Since \(\nu>\gamma\), all cases are covered by the common estimate
\[
|T_{ijk}|
\le\frac{D_*}{\lambda^2}
\left(\pi^2C_3B_jM_iM_k
+52\pi^3C_1M_iM_jM_k\right)e^{-\gamma L}.
\]
Using (4.2), \(\eta=\gamma/2=\frac18\log(25/23)\), and the conservative rational bounds
\[
D_*<\frac{875}{611},\quad
C_1<25.511,\quad C_3<465.933,\quad \pi<\frac{22}{7},
\]
gives
\[
\boxed{
|T_{ijk}|
\le\frac{e^{-\eta\ell_{\rm MST}(S_i,S_j,S_k)}}{\lambda^2}
\left(
6591\,B_jM_iM_k
+58976\,M_iM_jM_k
\right).
}
\tag{4.3}
\]
This is a volume-independent connected tree estimate for each ordered third-order term, conditional on the PF-I16 derivative-flow input and the corrected isolated-face derivative bound.

## 5. Six-permutation coefficient

The exact third-order coefficient is
\[
E_{123}=-\sum_{\sigma\in S_3}T_{\sigma(1)\sigma(2)\sigma(3)}.
\]
Because \(T_{ijk}=\nu_\Phi[u_i r_j u_k]\) is symmetric under \(i\leftrightarrow k\), the six terms group exactly as twice the three choices of middle label. Summing (4.3) gives
\[
\boxed{
|E_{123}|
\le\frac{e^{-\eta\ell_{\rm MST}(S_1,S_2,S_3)}}{\lambda^2}
\left[
13182\sum_{j=1}^3B_jM_iM_k
+353856\,M_1M_2M_3
\right],
}
\tag{5.1}
\]
where in the first sum \(\{i,k\}=\{1,2,3\}\setminus\{j\}\), and
\[
\eta=\frac18\log\frac{25}{23}>0.
\]
The constants are intentionally conservative and are verified by the accompanying exact-rational arithmetic checker.

## 6. Scope and remaining gates

**Derived conditionally:** the finite-volume Dobrushin influence bound (2.4)–(2.5) for the dressed reference measure; the Föllmer-covariance reduction; the pair-convolution estimates (3.5)–(3.6); the connected three-support tree estimate (4.3); and the complete six-permutation estimate (5.1).

**Still conditional:** the corrected PF-I16 pointwise derivative-flow estimate and its face-pullback / finite-product Kato–Bochner hypotheses. The result is not an unconditional physical theorem.

**Not proved:** Dobrushin mixing for the actual interacting Wilson-vacuum measure; the boundary-cumulant subroute \(\operatorname{cum}_3(q_j,m_i,m_k)\) considered in the alternative conditional decomposition (that subroute is bypassed, not closed); fourth-order spatial partition cancellation; all-orders activity summability; source physical kinetic/time normalization; continuum reconstruction; or a Yang–Mills mass gap.

The new route does not delete disconnected minimal spin-support channels and imports no R3 constants. It bounds each ordered PF-I16 third cumulant directly under \(\nu_\Phi\), rather than assuming that the separate boundary-cumulant decomposition has a tree bound.

## References

1. H. Föllmer, “A covariance estimate for Gibbs measures,” *Journal of Functional Analysis* 46 (1982), 387–395. DOI: 10.1016/0022-1236(82)90053-2.
2. F. Coppini and W. M. Ruszel, “Gaussian fluctuations of differential observables of stationary lattice fields,” arXiv:2610.04452 (2026), Proposition 5.6. Its Dobrushin cut argument is related context; the finite-product oscillation-profile estimate above is derived for the PF-I16 link measure and is not imported as a black-box theorem.
