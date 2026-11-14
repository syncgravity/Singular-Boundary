# PF-I16 — All-orders radial character tail and full face/pair projective tensor norm

**Date:** 2026-11-14  
**Status:** the all-orders weighted character tail and a volume-uniform projective tensor bound for the actual face/pair insertions are ESTABLISHED under the recorded isolated-rotor and incidence/allocation hypotheses. The numerical projective activity majorant is improved substantially, but it still does not certify the proposed \(1/8\) criterion. Actual-insertion cross-split QF is independently ESTABLISHED under the stationary independent-link Markov \(L^2\)-gap hypotheses. No support-sensitive all-orders space-time tree, KP convergence, interacting-vacuum gap, or continuum mass gap is promoted.

## 1. Conventions and target

Let
\[
p=\cos\theta,\qquad R_\beta(p)=-\frac{q_\beta(\theta)}{\sin\theta}
=\frac{d}{dp}s_\beta(\arccos p),
\]
and use the SU(2) characters
\[
\chi_n(p)=U_n(p)=\frac{\sin((n+1)\theta)}{\sin\theta},
\qquad n=0,1,\ldots .
\]
Thus \(\chi_0=1,\ \chi_1=2p,\ \chi_2=4p^2-1\). Expand
\[
R_\beta(p)=\sum_{n\ge0}r_n(\beta)\chi_n(p).
\]
The coefficient formula already recorded in the radial audit is
\[
r_n(\beta)=\frac2\pi\int_0^\pi
\sin\theta\,R_\beta(\cos\theta)\sin((n+1)\theta)\,d\theta
=-\frac2\pi\int_0^\pi q_\beta(\theta)\sin((n+1)\theta)\,d\theta.
\tag{1.1}
\]
The goal here is a weighted \(\ell^1\) estimate strong enough to control the four-link trace expansion and the shared-link Casimir contraction in the actual pair insertion.

## 2. Character algebra and the first-order radial operator

Put
\[
L R=(1-p^2)R'(p)-3pR(p).
\]
The Chebyshev/character identities give
\[
(1-p^2)\chi_n'(p)
=p\chi_n(p)-(n+1)T_{n+1}(p),
\qquad
2T_{n+1}=\chi_{n+1}-\chi_{n-1},
\]
with \(\chi_{-1}=0\). Since \(2p\chi_n=\chi_{n+1}+\chi_{n-1}\), it follows exactly that
\[
\boxed{
L\chi_n=-\frac{n+3}{2}\chi_{n+1}
+\frac{n-1}{2}\chi_{n-1}.
}
\tag{2.1}
\]
Consequently, if \(LR=S\), then for \(m\ge1\)
\[
S_m=\frac m2r_{m+1}-\frac{m+2}{2}r_{m-1},
\tag{2.2}
\]
where subscripts denote character coefficients. The \(m=0\) coefficient of \(LR\) vanishes.

The radial equation is
\[
LR_\beta=-4\{(1-p^2)R_\beta^2+\beta p+\lambda_\beta\},
\qquad
\lambda_\beta=-\langle(1-p^2)R_\beta^2\rangle_{\rm Haar}.
\tag{2.3}
\]
The choice of \(\lambda_\beta\) is exactly the condition that the character coefficient of index zero on the right side vanish.

Solving (2.2) backwards along each parity chain and excluding the growing homogeneous solution gives
\[
\boxed{
r_{m-1}
=\sum_{k\ge0}
\frac{8m}{(m+2k)(m+2k+2)}
\,G_{m+2k},
\qquad
G=(1-p^2)R_\beta^2+\beta p+\lambda_\beta .
}
\tag{2.4}
\]
This is the all-orders coefficient-tail identity. It is not a truncation or a perturbative expansion.

## 3. Weighted character Banach algebra

For \(s\ge1\), define
\[
\|F\|_{s,\chi}
=\sum_{n\ge0}(n+1)^s|F_n|,
\qquad F=\sum_{n\ge0}F_n\chi_n.
\]
The SU(2) fusion rule is
\[
\chi_n\chi_m=\sum_{k=0}^{\min(n,m)}\chi_{n+m-2k}.
\]
Because
\[
\sum_{k=0}^{\min(n,m)}(n+m-2k+1)=(n+1)(m+1)
\]
and \(\sum x_k^s\le(\sum x_k)^s\) for \(x_k\ge0,\ s\ge1\), one has
\[
\boxed{\|FG\|_{s,\chi}\le\|F\|_{s,\chi}\|G\|_{s,\chi}.}
\tag{3.1}
\]
Also
\[
1-p^2=\frac34\chi_0-\frac14\chi_2,
\]
so
\[
\boxed{
\|(1-p^2)F\|_{s,\chi}
\le M_s\|F\|_{s,\chi},
\qquad M_s=\frac{3+3^s}{4}.
}
\tag{3.2}
\]

Define the parity-tail operator \(\mathcal K\) by the right side of (2.4), with input coefficients \(G_n\), \(n\ge1\). For each \(n\), the total coefficient sent to indices \(m-1\), \(m\le n,\ m\equiv n\pmod2\), is bounded by
\[
\frac{8}{n(n+2)}\sum_{\substack{1\le m\le n\\m\equiv n\ (2)}}m^{s+1}
\le 8n^s\le8(n+1)^s.
\]
Therefore
\[
\boxed{\|\mathcal K G\|_{s,\chi}\le8\|G\|_{s,\chi}.}
\tag{3.3}
\]
The source term is exact:
\[
\mathcal K(\beta p)=\frac43\beta\,\chi_0.
\tag{3.4}
\]

## 4. All-orders weighted character tail at PF-I16 coupling

Take \(s=4\), so \(M_4=21\). The radial equation is the fixed-point equation
\[
R=\mathcal K\{\beta p+(1-p^2)R^2\}.
\tag{4.1}
\]
On the ball \(\|R\|_{4,\chi}\le2\beta\), (3.1)–(3.3) give
\[
\|\mathcal T(R)\|_{4,\chi}
\le\frac43\beta+8\cdot21\cdot4\beta^2
=\frac43\beta+672\beta^2,
\tag{4.2}
\]
and
\[
\|\mathcal T(R)-\mathcal T(S)\|_{4,\chi}
\le 672\beta\,\|R-S\|_{4,\chi}.
\tag{4.3}
\]
The isolated-face allocation gives
\[
\beta_f=\frac{|b_f|}{A_f}\le\frac{2b_0}{a_0}
\le\frac1{25000}.
\]
At this endpoint, \(672\beta\le0.02688<1\), and
\[
\frac43\beta+672\beta^2<2\beta.
\]
Thus \(\mathcal T\) is a contraction of the closed radius-\(2\beta\) ball in the weighted character Banach algebra. It has a unique fixed point satisfying
\[
\boxed{
\sum_{n\ge0}(n+1)^4|r_n(\beta)|\le2\beta.
}
\tag{4.4}
\]
Since \(|\chi_n(p)|\le n+1\), this fixed point has \(\|R\|_\infty\le2\beta\). It solves the radial equation and lies in the same sup-norm ball as the physical regular rotor solution. The previously established \(L^\infty\) fixed-point uniqueness (contraction constant \(8\pi\beta<1\)) identifies the two solutions. Hence (4.4) is a bound for the physical radial factor, not merely for a formal coefficient solution.

In particular, the all-orders tail obeys
\[
\boxed{
\sum_{n\ge N}(n+1)^4|r_n(\beta)|\le2\beta,
\qquad
\sum_{n\ge N}|r_n(\beta)|
\le\frac{2\beta}{(N+1)^4}.
}
\tag{4.5}
\]
This closes the weighted character-tail gate needed below.

## 5. Character expansion of the dressed face gradient

Let
\[
s_\beta(\arccos p)=\sum_{n\ge0}\sigma_n(\beta)\chi_n(p).
\]
The exact derivative identity
\[
\chi_n'(p)=2\sum_{\substack{0\le m<n\\m\equiv n-1\ (2)}}(m+1)\chi_m(p)
\]
implies
\[
r_m=2(m+1)\sum_{\substack{n\ge m+1\\n-m\ {\rm odd}}}\sigma_n.
\]
Taking the difference of two successive parity tails gives
\[
\boxed{
\sigma_n=\frac{r_{n-1}}{2n}
-\frac{r_{n+1}}{2(n+2)},\qquad n\ge1.
}
\tag{5.1}
\]
The constant coefficient \(\sigma_0\) is irrelevant to the gradient.

Define
\[
C_5(\beta)=\sum_{n\ge1}(n+1)^5|\sigma_n(\beta)|.
\]
The fixed-point equation and (4.4) give the sharper decomposition
\[
\left\|R_\beta-\frac43\beta\chi_0\right\|_{4,\chi}
=\left\|\mathcal K\{(1-p^2)R_\beta^2\}\right\|_{4,\chi}
\le672\beta^2.
\]
Since the subtracted term has only character index zero, this directly gives
\[
|r_0|\le\frac43\beta+672\beta^2,\qquad
\boxed{\sum_{m\ge1}(m+1)^4|r_m|\le672\beta^2.}
\]
In particular, the nonconstant tail is \(O(\beta^2)\); it is not merely bounded by the residual \(2\beta-\frac43\beta\).
Using (5.1), separating \(n=1\), and bounding the remaining coefficient ratios,
\[
C_5(\beta)
\le16|r_0|+\frac{275}{64}
\sum_{m\ge1}(m+1)^4|r_m|
\le\frac{64}{3}\beta+\frac{1299}{64}\,672\beta^2.
\]
At \(\beta\le1/25000\), this yields the sharper rational constant
\[
\boxed{C_5(\beta)\le\frac{3281837}{150000}\,\beta
<21.879\,\beta.}
\]
Therefore
\[
\boxed{
\sum_{n\ge1}(n+1)^5|\sigma_n(\beta)|\le21.879\beta.
}
\tag{5.2}
\]
This is the weighted coefficient estimate for the actual gradient character expansion.

## 6. Exact shared-link Casimir block and pair projective norm

For spin \(j=n/2\), the face character has the four-link trace expansion
\[
\chi_n(U_1U_2U_3U_4)
=\sum_{i_0,i_1,i_2,i_3=1}^{n+1}
(\pi_j(U_1))_{i_0i_1}
(\pi_j(U_2))_{i_1i_2}
(\pi_j(U_3))_{i_2i_3}
(\pi_j(U_4))_{i_3i_0}.
\tag{6.1}
\]
There are \((n+1)^4\) rank-one link-slot terms, and every matrix coefficient has sup norm at most one.

When two face gradients share a link, their Lie-algebra indices must be contracted before taking absolute values. On spin \(j\otimes k\),
\[
\Omega_{jk}=\sum_{a=1}^3d\pi_j(T_a)\otimes d\pi_k(T_a)
\]
has exact norm
\[
\|\Omega_{jk}\|_{\rm op}
=\min(j,k)(\max(j,k)+1)
\le\frac{(n+1)(m+1)}4,
\quad j=\frac n2,\ k=\frac m2.
\tag{6.2}
\]
For fixed trace indices in (6.1), the shared-link factor is one matrix coefficient of a unitary representation tensor multiplied by \(\Omega_{jk}\); its sup norm is therefore at most \(\|\Omega_{jk}\|_{\rm op}\). The other six link factors are ordinary representation matrix coefficients with sup norm at most one. Thus the projective cost of the \((n,m)\) contracted pair mode is at most
\[
\frac14(n+1)^5(m+1)^5.
\tag{6.3}
\]
Summing with (5.2), for one shared link,
\[
\mathfrak p\!\left(
\langle\nabla s_f^{(e)},\nabla s_g^{(e)}\rangle
\right)
\le\frac14 C_5(\beta_f)C_5(\beta_g)
\le\frac{625}{4}\beta_f\beta_g.
\tag{6.4}
\]
The actual pair insertion includes the factor \(2a_e\) and at most four shared links. With the recorded allocation
\[
a_e\beta_f\beta_g\le16\,\frac{b_0^2}{a_0},
\]
we obtain
\[
\boxed{
\mathfrak p(v_{fg})\le
4\cdot2a_e\cdot\frac14 C_5(\beta_f)C_5(\beta_g)
\le\frac{10770454094569}{703125000}\,\frac{b_0^2}{a_0}
<15318\,\frac{b_0^2}{a_0}.
}
\tag{6.5}
\]
This is a full all-orders projective tensor bound for the actual pair insertion. It uses the character tail and the exact shared-link Casimir block; it is not an \(L^\infty\)-only estimate.

## 7. Face projective norm and total local activity

For the fundamental face character,
\[
p_f=\frac12\operatorname{Tr}(U_1U_2U_3U_4)
=\frac12\sum_{a,b,c,d=1}^2
(U_1)_{ab}(U_2)_{bc}(U_3)_{cd}(U_4)_{da}.
\]
This is an exact 16-term rank-one decomposition with coefficient sum \(8\). Since \(\rho_f\le32\),
\[
\boxed{\mathfrak p(v_f)\le256b_0.}
\tag{7.1}
\]
Combining (6.5) and (7.1), the per-link projective activity with support weight \(e^{|X|/8}\), at most eight face supports and 224 adjacent-face-pair supports per link, is
\[
\kappa_\pi
\le
\frac{8(256x)e^{1/2}
+224\left(\frac{10770454094569}{703125000}x^2\right)e}{3/4},
\qquad x=\frac{b_0}{a_0}\le\frac1{50000}.
\tag{7.2}
\]
Using \(\sqrt e<1.65\) and \(e<2.72\),
\[
\boxed{
\kappa_\pi
\le0.090112+0.004977568
<0.095090.
}
\tag{7.3}
\]
The pair term is reduced from the previous \(K_6^2\)-dependent projective majorant to an explicit all-orders coefficient bound. However,
\[
2\kappa_\pi<0.190180
\]
is not below \(1/8=0.125\). Thus this improved sufficient majorant still does **not** certify the proposed projective KP threshold. This is failure of the upper majorant, not a lower bound on the true projective norm and not evidence of divergence. The face-only term \(0.090112\) already prevents this particular criterion from closing.

## 8. Actual-insertion cross-split QF — separate result, now reconciled

The actual-insertion cross-split QF does not require (4.4)–(7.3). The arbitrary-local-observable link-interpolation audit proves, for bounded local multiplication observables \(F_i\) with link supports \(X_i\), every split \(I=J\sqcup K\), and stationary independent link paths with uniform one-link \(L^2\) gap \(\Delta_0\),
\[
\boxed{
\left|
\mathbb E\prod_{i\in I}F_i(X(t_i))
-\mathbb E\prod_{i\in J}F_i(X(t_i))\,
 \mathbb E\prod_{i\in K}F_i(X(t_i))
\right|
\le
2|I|\prod_i\|F_i\|_\infty
\sum_{\substack{i\in J\\j\in K}}
|X_i\cap X_j|e^{-\Delta_0|t_i-t_j|}.
}
\tag{8.1}
\]
The proof conditions on all links except one shared link. Each full local observable then becomes a bounded one-time function of that link, so no tensor-product decomposition, smoothness, or projective norm is needed. For the actual face/pair insertions, the support sizes are at most four/eight links and the overlap multiplicity is uniformly bounded. Therefore actual face/pair cross-split QF is **ESTABLISHED** under the stated reference-process hypotheses.

This QF statement is distinct from the all-orders support-sensitive cumulant tree. The global product-process tensor-gap bridge supplies an all-orders temporal tree over the complete row graph, but not a tree whose every edge is a support-overlap edge. The joint space-time tree/KP gate therefore remains open.

## 9. Gate disposition

- All-orders radial character tail \(\sum(n+1)^4|r_n|\le2\beta\): **ESTABLISHED**.
- Weighted gradient-character coefficient tail \(\sum(n+1)^5|\sigma_n|\le(3281837/150000)\beta<21.879\beta\): **ESTABLISHED**.
- Exact shared-link Casimir contraction: **ESTABLISHED**.
- Full face projective norm \(\mathfrak p(v_f)\le256b_0\): **ESTABLISHED**.
- Full pair projective norm \(\mathfrak p(v_{fg})\le15318b_0^2/a_0\): **ESTABLISHED**.
- Actual-insertion cross-split QF: **ESTABLISHED** under independent stationary link paths and uniform one-link \(L^2\) gap.
- Proposed projective \(1/8\) activity criterion: **NOT CERTIFIED**; the face-only contribution to \(\kappa_\pi\) is already \(0.090112>1/16\), before pair terms. This particular criterion cannot close without improving the face projective bound or changing the criterion/normalization.
- All-orders support-sensitive joint cumulant tree, marked-root sum, quantum KP convergence, interacting-vacuum Poincaré inequality, and continuum mass gap: **OPEN**.

No P0–P5 acceptance status is promoted.
