# PF-I16 — Product-process tensor-gap bridge for signed product-cumulant resummation

**Date:** 2026-11-14  
**Status:** exact bridge established under the stationary independent-link Markov reference-process hypotheses; local-cumulant-only version remains open  
**Scope:** finite regulator, finite link set, stationary product reference process. This is not an interacting-vacuum or continuum result.

## 1. The key change of viewpoint

The signed Leonov–Shiryaev sum for
\[
A_i(t_i)=\prod_{e\in X_i}Y_{i,e}(t_i)
\]
need not be resummed by assigning its individual slot-partition terms to trees. In the reference-process setting, each row product is already a single bounded multiplication observable on the global product state space.

Let the finite set of links be \(E\). For each \(e\in E\), assume a stationary Markov semigroup \(P_t^e\) on \(L^2(\nu_e)\), with invariant projection \(\Pi_e\), and
\[
P_t^e=\Pi_e+Q_t^e,\qquad
\|Q_t^e\|_{2\to2}\le e^{-\Delta_e t},\qquad
\Delta_e\ge\Delta_0>0.
\tag{1.1}
\]
Assume the link processes are independent. The product state space, stationary law, and semigroup are
\[
\Omega=\prod_{e\in E}\Omega_e,\qquad
\nu=\bigotimes_{e\in E}\nu_e,\qquad
P_t=\bigotimes_{e\in E}P_t^e.
\tag{1.2}
\]

For each row \(i\), define the multiplication observable on \(\Omega\)
\[
F_i(x)=\prod_{e\in X_i}f_{i,e}(x_e),
\qquad
\|F_i\|_\infty\le\prod_{e\in X_i}\|f_{i,e}\|_\infty.
\tag{1.3}
\]
Then \(A_i(t_i)=F_i(X_{t_i})\) for the global stationary product process \(X_t\). The full product-insertion cumulant is therefore an ordinary time-ordered cumulant of bounded observables of one Markov process. The slot partitions are an algebraic expansion of that cumulant, not an additional probabilistic object that needs to be bounded termwise.

## 2. Tensorization of the spectral gap

For each link write
\[
L^2(\nu_e)=\mathbb C\mathbf1\oplus L_0^2(\nu_e).
\]
The product Hilbert space has the orthogonal decomposition
\[
L^2(\nu)=\bigoplus_{S\subseteq E}\mathcal H_S,\qquad
\mathcal H_S=
\bigotimes_{e\in S}L_0^2(\nu_e)
\otimes
\bigotimes_{e\notin S}\mathbb C\mathbf1.
\tag{2.1}
\]
The \(S=\varnothing\) summand is the constants. On a nonempty summand,
\[
P_t\big|_{\mathcal H_S}
=\bigotimes_{e\in S}Q_t^e,
\]
and hence
\[
\left\|P_t\big|_{\mathcal H_S}\right\|_{2\to2}
\le\prod_{e\in S}e^{-\Delta_e t}
\le e^{-\Delta_0t}.
\]
Taking the orthogonal direct sum over nonempty \(S\) proves
\[
\boxed{\|P_t-\Pi\|_{2\to2}\le e^{-\Delta_0t},}
\qquad \Pi=\bigotimes_e\Pi_e.
\tag{2.2}
\]
The gap is the minimum link gap, not the sum over links, and is independent of the number of links. This argument requires the stationary product structure and the linkwise \(L^2\) contraction (1.1); it does not follow from a bound on local cumulants alone.

## 3. Apply the already established projection-tree theorem globally

The all-orders interval-forest/port-completion theorem in the existing PF-I16 weighted projection-tree assignment audit, equations (7.5)–(7.8), applies to centered bounded multiplication observables of a stationary reference process satisfying (2.2). It gives, for centered \(G_1,\ldots,G_r\),
\[
\left|\kappa_0(G_1(X_{t_1}),\ldots,G_r(X_{t_r}))\right|
\le
2^r\left(\prod_i\|G_i\|_\infty\right)
\sum_{T\in\mathcal T_r}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}.
\tag{3.1}
\]
Cumulants of order \(r\ge2\) are invariant under adding constants to any argument. Set
\[
G_i=F_i-\nu(F_i).
\]
Then \(\|G_i\|_\infty\le2\|F_i\|_\infty\), so
\[
\boxed{
\left|\kappa_0(A_1(t_1),\ldots,A_r(t_r))\right|
\le
4^r\left(\prod_i\|F_i\|_\infty\right)
\sum_{T\in\mathcal T_r}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}.
}
\tag{3.2}
\]
This bound is uniform in the number of links and in the row supports. It resums the signed Leonov–Shiryaev expansion at the level of the global cumulant, before absolute values are taken. In particular, the Bell(r)^7 slot-partition fiber from the eight-identical-link example is never separately majorized.

If the support-overlap graph \(G_X\) is disconnected, the rows split into two nonempty groups depending on disjoint link-coordinate sets. The corresponding global processes are independent, so the cumulant is exactly zero. Thus the right side of (3.2) may be multiplied by
\[
\mathbf1_{\{G_X\text{ connected}\}}.
\tag{3.3}
\]
The tree sum in (3.2) is over all labeled trees, not only trees contained in \(G_X\). This is a deliberate, harmless loss for the time-integrated estimate below; it does not prove the sharper support-restricted maximum-tree estimate in the previous support-temporal audit.

## 4. Normalized time-integrated bound

For every labeled tree \(T\), root it and integrate each non-root time variable relative to its parent:
\[
\int_{[0,\mathcal T]^r}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}\,d\mathbf t
\le
\mathcal T\left(\frac2{\Delta_0}\right)^{r-1}.
\tag{4.1}
\]
Cayley's formula gives \(|\mathcal T_r|=r^{r-2}\). Combining (3.2) and (4.1),
\[
\boxed{
\frac1{r!\mathcal T}
\int_{[0,\mathcal T]^r}
|\kappa_0(A_1(t_1),\ldots,A_r(t_r))|\,d\mathbf t
\le
4^r\frac{r^{r-2}}{r!}
\left(\frac2{\Delta_0}\right)^{r-1}
\prod_i\|F_i\|_\infty.
}
\tag{4.2}
\]
Since \(r^{r-2}/r!\le e^r\) for \(r\ge2\), the right side is bounded by \(C_{\Delta_0}^r\prod_i\|F_i\|_\infty\), with a constant independent of the number of links and of \(\mathcal T\). This is the required exponential-in-order normalized temporal cumulant control for the independent-link Markov reference process.

## 5. What this resolves, and what it does not

**Resolved under (1.1)–(1.2):**
1. The global product process inherits the uniform link gap \(\Delta_0\), independently of the number of links.
2. The row products are ordinary bounded observables of that global process.
3. The signed product-cumulant / Leonov–Shiryaev sum is bounded before slot-partition absolute values, by the existing all-orders projection-tree theorem.
4. The normalized time-integrated cumulant coefficient has only exponential order growth.

**Not resolved:**
1. If the only available hypothesis is the local cumulant estimate (rather than a stationary independent-link Markov semigroup with a uniform \(L^2\) gap), this bridge is unavailable; the cancellation-preserving local-cumulant-only resummation remains open.
2. The tree sum in (3.2) is over the complete graph. A sharper support-restricted tree/fiber estimate is not proved here.
3. Spatial support summation and the joint space-time polymer/Kotecký–Preiss organization still require a separate proof.
4. The quantum connected-resolvent/tree theorem, uniform interacting Feynman–Kac convergence, interacting vacuum, P3 all-functions inequality, and four-dimensional continuum construction remain open.

This bridge does not promote any P0–P5 status. It closes only the reference-process product-cumulant time-integrability subproblem under the explicitly stated Markov tensor-gap hypotheses.
