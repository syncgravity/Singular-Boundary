# PF-I16 — Fourth-order cut interpolation and conditional four-support tree bound

**Date:** 2026-11-13  
**Status:** finite-product spatial tree theorem for the full fourth-order coefficient, uniform in graph volume under the source-incidence and (b_0/a_0\le1/50000) hypotheses. The corrected derivative-flow estimate and face-map metric pullback are established by the companion closure audit. It is a finite dressed-reference result, not an all-orders convergence theorem or a physical Yang–Mills gap.

## 1. Cut interpolation

Let \(I=\{1,2,3,4\}\) label four centered residuals at \(s=1\), with supports \(S_i\). Let \(\ell_{\rm MST}(S_1,S_2,S_3,S_4)\) be the minimum spanning-tree length in the link-overlap graph.

Let \(L\) be the longest edge in a minimum spanning tree. Removing it partitions the labels into two nonempty sets \(P,Q\), and the MST cut property gives
\[
d(S_p,S_q)\ge L\qquad(p\in P,\ q\in Q).
\tag{1.1}
\]
Set \(r=\lfloor L/2\rfloor\) and let
\[
A_r=\bigcup_{p\in P}\{e:d(e,S_p)\le r\},\qquad B_r=E\setminus A_r.
\]
Split the dressed face potential into faces internal to either side and crossing faces:
\[
\Phi=\Phi_A+\Phi_B+\Phi_\times,\qquad
\Phi_s=\Phi_A+\Phi_B+s\Phi_\times,\quad 0\le s\le1,
\]
and put \(W=2\Phi_\times\). At \(s=0\), the link product, Haar measure, generator and perturbation split across \(A_r|B_r\). The four-source ground-energy coefficient therefore vanishes:
\[
E_{1234}(0)=0.
\tag{1.2}
\]
At \(s=1\), it is the original PF-I16 fourth-order coefficient.

For each \(s\), let \(\pi_s\propto e^{2\Phi_s}dU\), let \(L_s\) be the positive reversible generator, and let \(g_s(\mathbf t)\) be the positive eigenfunction of
\[
L_s-\sum_{i\in I}t_ir_i
\]
normalized by \(\pi_s(g_s)=1\). Write \(V_{\mathbf t}=\sum_i t_ir_i\), \(N_s(\mathbf t)=\pi_s(g_s^2)\), and \(\Gamma\) for the fixed carré du champ of the product diffusion metric. The diffusion part of \(L_s\), and hence \(\Gamma\), does not depend on \(s\).

The Rayleigh quotient is
\[
E_s(\mathbf t)=
\frac{\pi_s\!\left[\Gamma(g_s,g_s)-V_{\mathbf t}g_s^2\right]}
{\pi_s(g_s^2)}.
\]
Since
\[
\partial_s\pi_s(F)=\pi_s[(W-\pi_sW)F],
\]
the Hellmann–Feynman derivative at the normalized eigenfunction gives
\[
\partial_sE_s(\mathbf t)=
\frac{\pi_s[(W-\pi_sW)
(\Gamma(g_s,g_s)-V_{\mathbf t}g_s^2-E_sg_s^2)]}
{N_s(\mathbf t)}.
\tag{1.3}
\]
The eigenvalue equation \(L_sg_s=(V_{\mathbf t}+E_s)g_s\) and the carré-du-champ identity
\[
\Gamma(g_s,g_s)=\tfrac12[-L_s(g_s^2)+2g_sL_sg_s]
\]
reduce the bracket in (1.3) to \(-\tfrac12L_s(g_s^2)\). Reversibility, \(\pi_s[L_s(g_s^2)]=0\), and integration by parts then give the exact cut-response identity
\[
\boxed{
\partial_sE_s(\mathbf t)=
-\frac{\pi_s[g_s(\mathbf t)\Gamma(W,g_s(\mathbf t))]}
{\pi_s[g_s(\mathbf t)^2]}.
}
\tag{1.4}
\]
This identity retains the complete fourth-order coefficient; it does not split or take absolute values of the three pair-partition channels.

## 2. Centered coefficient recursion along the interpolation

The fixed residuals \(r_i\) need not be centered under \(\pi_s\) for \(s<1\). Replace them, for the purpose of the eigenfunction recursion, by
\[
r_i^{(s)}=r_i-\pi_s(r_i).
\]
This changes the eigenvalue only by the linear scalar \(\sum_i t_i\pi_s(r_i)\), leaves the eigenfunction unchanged, and therefore leaves the mixed coefficient with four distinct labels unchanged. Also
\[
\|r_i^{(s)}\|_\infty\le2B_i,\qquad
D_er_i^{(s)}=D_er_i,\qquad
B_i:=\|r_i\|_\infty,\quad
M_i:=\sum_{e\in S_i}\|D_er_i\|_\infty.
\]

Expand the mean-one eigenfunction as
\[
g_s(\mathbf t)=1+\sum_{\varnothing\ne K\subseteq I}u_K^{(s)}t_K+\cdots,
\qquad \pi_s(u_K^{(s)})=0.
\]
The centered reduced-resolvent recursion is
\[
u_K^{(s)}=G_s\!\left[
\sum_{i\in K}r_i^{(s)}u_{K\setminus\{i\}}^{(s)}
+\sum_{\varnothing\ne J\subsetneq K}
E_J^{(s)}u_{K\setminus J}^{(s)}
\right],
\tag{2.1}
\]
where \(G_s=L_s^{-1}Q_s\), \(E_{\{i\}}^{(s)}=0\), and
\[
|E_J^{(s)}|
\le2\sum_{i\in J}B_i\,U_{J\setminus\{i\}}.
\tag{2.2}
\]
Here \(U_K\) will be a uniform upper bound for \(\|u_K^{(s)}\|_\infty\).

Assume the corrected pointwise derivative-flow estimate holds uniformly for every \(\Phi_s\):
\[
\|D_eG_sh\|_\infty
\le\lambda^{-1}\sum_z e^{-\mu d(e,z)}\|D_zh\|_\infty,
\qquad \mu=\log25.
\tag{2.3}
\]
The face-Hessian majorants do not increase when crossing-face terms are scaled by \(s\in[0,1]\); the same conditional Kato–Bochner comparison and \(\lambda\) therefore apply along the interpolation.

Set
\[
\gamma=\frac14\log\frac{25}{23},\qquad
S_\gamma=
1+\frac{24e^{-(\mu-\gamma)}}{1-23e^{-(\mu-\gamma)}}
=1+\frac{24}{e^{\mu-\gamma}-23}
<18.264.
\tag{2.4}
\]
The bound uses the link-overlap shell count \(24\cdot23^{n-1}\) at distance \(n\ge1\).

For nonempty \(K\), put \(S_K=\bigcup_{i\in K}S_i\) and define the weighted derivative profile
\[
\mathcal N_K^{(s)}
=\sum_e e^{\gamma d(e,S_K)}\|D_eu_K^{(s)}\|_\infty.
\]
The weighted form of (2.3), the triangle inequality for graph distance, and the product rule imply
\[
\mathcal N_K^{(s)}
\le\frac{S_\gamma}{\lambda}
\left[
\sum_{i\in K}
\left(M_iU_{K\setminus\{i\}}+2B_i\mathcal N_{K\setminus\{i\}} \right)
+\sum_{\varnothing\ne J\subsetneq K}
\mathcal E_J\mathcal N_{K\setminus J}
\right],
\tag{2.5}
\]
where \(\mathcal E_J\) bounds \(|E_J^{(s)}|\), uniformly in \(s\). Since \(u_K^{(s)}\) is centered and every link has radius-two diameter \(2\pi\),
\[
\|u_K^{(s)}\|_\infty
\le2\pi\sum_e\|D_eu_K^{(s)}\|_\infty
\le2\pi\mathcal N_K^{(s)}.
\tag{2.6}
\]
Equations (2.2), (2.5), and (2.6) form a triangular finite recursion for all nonempty \(K\subseteq I\). In particular, one may define volume-independent bounds in increasing order of \(|K|\) by
\[
\begin{gathered}
U_\varnothing=1,\quad \mathcal N_\varnothing=0,\quad
\mathcal E_{\{i\}}=0,\\
\mathcal N_{\{i\}}=\frac{S_\gamma}{\lambda}M_i,\quad
U_{\{i\}}=2\pi\mathcal N_{\{i\}},\\
\mathcal E_K=2\sum_{i\in K}B_iU_{K\setminus\{i\}},\quad
\mathcal N_K=\frac{S_\gamma}{\lambda}
\left[
\sum_{i\in K}(M_iU_{K\setminus\{i\}}+2B_i\mathcal N_{K\setminus\{i\}})
+\sum_{\varnothing\ne J\subsetneq K}
\mathcal E_J\mathcal N_{K\setminus J}
\right],\\
U_K=2\pi\mathcal N_K\qquad(|K|\ge2).
\end{gathered}
\tag{2.7}
\]
These constants depend on the four residual amplitudes and derivative sums, \(\lambda\), and \(S_\gamma\), but not on graph volume or support separation.

## 3. Denominator coefficients and the cut-layer estimate

Because \(\pi_s(u_s)=0\),
\[
N_s(\mathbf t)=\pi_s(g_s^2)
=1+\pi_s(u_s^2).
\]
For nonempty \(K\subseteq I\), its squarefree coefficient \(n_K^{(s)}\) obeys
\[
|n_K^{(s)}|
\le D_K:=
\sum_{\varnothing\ne J\subsetneq K}
U_JU_{K\setminus J},
\qquad D_{\{i\}}=0.
\]
Let \(\chi_K^{(s)}\) be the squarefree coefficients of \(N_s^{-1}\). Since \(N_sN_s^{-1}=1\),
\[
|\chi_K^{(s)}|\le\Xi_K,\qquad
\Xi_\varnothing=1,\qquad
\Xi_K=\sum_{\varnothing\ne J\subseteq K}D_J\Xi_{K\setminus J}.
\tag{3.1}
\]
This is another finite scalar recursion.

Write
\[
H_s(\mathbf t)=\pi_s[g_s\Gamma(W,g_s)].
\]
For nonempty \(K\),
\[
[t_K]H_s
=\sum_{J\subsetneq K}
\pi_s[u_J^{(s)}\Gamma(W,u_{K\setminus J}^{(s)})].
\tag{3.2}
\]
At most eight accepted faces meet any link, and each face derivative is bounded by \(2\beta_*\), so
\[
\|D_eW\|_\infty\le32\beta_*,
\qquad \beta_*:=\sup_f\beta_f.
\tag{3.3}
\]
The derivative norms in (2.3) and (3.3), the carré-du-champ norm, and the radius-two link oscillation are taken in the same normalization; compatibility with the weighted product metric remains part of the conditional face-map metric/pullback input.
The derivative of \(W\) is supported on links belonging to faces crossing \(A_r|B_r\).

For every such boundary link \(e\), the cut property and face diameter one in the link-overlap graph imply
Indeed, a crossing face contains a link in \(A_r\) and a link in \(A_r^c\), and every pair of links in that face is adjacent. A crossing-face link inside \(A_r\) must be at distance at least \(r\) from every \(P\)-side support, or its outside neighbor would also lie in \(A_r\); a crossing-face link outside \(A_r\) is at distance at least \(r+1\) from every \(P\)-side support. For any \(Q\)-side support, use the inside neighbor and the cross-cut distance lower bound \(L\) to obtain distance at least \(L-r-1\). Thus every crossing-face link is at distance at least \(\min(r,L-r-1)\ge R\) from all four supports.
\[
d(e,S_m)\ge R:=\max\!\left(0,\left\lfloor\frac L2\right\rfloor-1\right)
\qquad(m\in I).
\tag{3.4}
\]
Therefore, for every nonempty \(K\subseteq I\),
\[
\sum_{e\in\operatorname{supp}DW}
\|D_eu_K^{(s)}\|_\infty
\le e^{-\gamma R}\mathcal N_K.
\tag{3.5}
\]
Combining (3.2)–(3.5),
\[
|[t_K]H_s|
\le32\beta_*e^{-\gamma R}
\sum_{J\subsetneq K}U_J\mathcal N_{K\setminus J}.
\tag{3.6}
\]
Since \(E_s'=-H_s/N_s\), coefficient multiplication and (3.1) give
\[
|[t_I]E_s'|
\le32\beta_*e^{-\gamma R}
\sum_{K\subseteq I}
\Xi_{I\setminus K}
\sum_{J\subsetneq K}U_J\mathcal N_{K\setminus J}.
\tag{3.7}
\]
The right side is uniform in \(s\) and graph volume.

Finally,
\[
R\ge\frac L2-\frac32,\qquad
\ell_{\rm MST}\le3L.
\]
Thus
\[
e^{-\gamma R}
\le e^{3\gamma/2}
e^{-(\gamma/6)\ell_{\rm MST}}.
\tag{3.8}
\]
Using \(E_{1234}(0)=0\), integrate (3.7) from \(s=0\) to \(1\). Define the finite, volume-independent prefactor
\[
\mathcal C_{1234}
=
32\beta_*e^{3\gamma/2}
\sum_{K\subseteq I}
\Xi_{I\setminus K}
\sum_{J\subsetneq K}U_J\mathcal N_{K\setminus J}.
\tag{3.9}
\]
The four-support result is
\[
\boxed{
|E_{1234}|
\le\mathcal C_{1234}
\exp\!\left[
-\frac1{24}\log\!\frac{25}{23}\,
\ell_{\rm MST}(S_1,S_2,S_3,S_4)
\right].
}
\tag{3.10}
\]
The exponent is positive:
\[
\eta_4=\frac{\gamma}{6}
=\frac1{24}\log\frac{25}{23}>0.
\]

## 4. Scope and remaining gaps

**Derived conditionally:** the exact cut-response identity (1.4); the centered recursion and weighted derivative-profile bounds through order four; the denominator coefficient recursion; the cut-layer tail; and the full four-support MST tree estimate (3.10). Because the interpolation retains the full coefficient, no pair-partition channel is bounded separately and the disconnected cancellation is not lost.

**Finite-model hypotheses:** source-uniform incidence (d_e\le8), the allocation bounds, and (b_0/a_0\le1/50000). The face-map metric pullback and finite-product Kato–Bochner comparison are derived in the companion closure audit. The same absolute Hessian majorants hold uniformly along the interpolation. The corrected pointwise derivative-flow estimate holds uniformly for all \(\Phi_s\). The cross-face derivative bound (3.3) uses the corrected isolated-face first-derivative estimate.

**Not proved:** a uniform growth bound on \(\mathcal C_n\) as the order \(n\) increases; all-orders activity summability or a nonzero convergence radius; Dobrushin mixing of the actual interacting Wilson-vacuum measure; physical-time normalization; continuum reconstruction; or a Yang–Mills mass gap. The fixed fourth-order estimate does not close these gaps.

The proof uses no R3-IR constants and does not replace graph connectedness by reconstructed spin-support connectedness.
