# PF-I16 — Product-semigroup cumulant bound and the support-localization gap

**Date:** 2026-11-16  
**Status:** exponential all-orders complete-temporal tree bound established by tensorization; support-restricted temporal tree remains open.

## 1. Product-process reduction

Let \((X_e(t))_{e\in E}\) be independent stationary link Markov processes with invariant laws \(\mu_e\) and semigroups \(P_t^e\). Assume the uniform linkwise \(L^2\) contraction
\[
\|P_t^e-\Pi_e\|_{L^2_0(\mu_e)\to L^2_0(\mu_e)}
\le e^{-\Delta_0t}.
\]
Form the product process
\[
Z(t)=(X_e(t))_{e\in E},\qquad
\mu=\bigotimes_{e\in E}\mu_e,\qquad
P_t=\bigotimes_{e\in E}P_t^e.
\]

The product semigroup has the same \(L^2\) gap:
\[
\boxed{\|P_t-\Pi\|_{L^2_0(\mu)\to L^2_0(\mu)}
\le e^{-\Delta_0t}.}
\tag{1.1}
\]
Indeed,
\[
L^2(\mu)=\bigoplus_{S\subseteq E}
\bigotimes_{e\in S}L^2_0(\mu_e)
\otimes\bigotimes_{e\notin S}\mathbb C1.
\]
On each nonconstant tensor sector \(S\ne\varnothing\), the product semigroup norm is at most
\[
\prod_{e\in S}e^{-\Delta_0t}
=e^{-|S|\Delta_0t}\le e^{-\Delta_0t}.
\]
This argument is valid for nonreversible link semigroups as well, provided the stated operator-norm contractions hold.

Every row monomial
\[
A_i(t_i)=\prod_{e\in X_i}f_{i,e}(X_e(t_i))
\]
is a single-time observable \(F_i(Z(t_i))\) of this product process, with
\[
\|F_i\|_\infty\le\prod_{e\in X_i}\|f_{i,e}\|_\infty.
\]
Consequently, the existing one-link Markov cumulant-tree theorem applied to \(Z\) yields the complete-temporal-tree estimate
\[
|\kappa(A_1(t_1),\ldots,A_R(t_R))|
\le 2^{R-2}\prod_i\|F_i\|_\infty
\sum_{T\in\mathcal T_R}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|},
\qquad R\ge2.
\tag{1.2}
\]
This is exponential in cumulant order and has no dependence on the number of links or on repeated support types. It is a genuine improvement over the superexponential coefficient in the global regeneration bound—but its tree is not yet spatially support-restricted.

## 2. Exact support factorization

Let
\[
G_X=([R],\{\{i,j\}:X_i\cap X_j\ne\varnothing\}).
\]
If \(G_X\) is disconnected, rows in distinct connected components depend on disjoint sets of independent link paths. Their sigma-fields are independent, so
\[
\kappa(A_1,\ldots,A_R)=0.
\tag{2.1}
\]
Thus the full cumulant has both a complete temporal-tree bound (1.2) and exact vanishing when the support graph is disconnected.

What does **not** follow is the desired bound with the temporal weights restricted to edges of \(G_X\). The complete temporal tree can use a short temporal edge between two rows that share no link. Connectivity of \(G_X\) does not make that edge replaceable by a support edge without losing temporal decay.

## 3. Three-row exact diagnostic

Take two independent stationary two-state chains \(U_e,U_f\), each with correlation
\[
\mathbb E[U_e(s)U_e(t)]=e^{-\Delta_0|t-s|},\qquad
\mathbb E[U_f(s)U_f(t)]=e^{-\Delta_0|t-s|},
\]
and set
\[
t_1=0,\quad t_2=100/\Delta_0,\quad t_3=50/\Delta_0,
\]
\[
X_1=\{e\},\quad X_2=\{e,f\},\quad X_3=\{f\},
\]
\[
A_1=U_e(t_1),\quad A_2=U_e(t_2)U_f(t_2),\quad
A_3=U_f(t_3).
\]
All three row observables are centered, and their pair covariances vanish. Therefore their third cumulant is their joint moment:
\[
\kappa(A_1,A_2,A_3)
=\mathbb E[U_e(t_1)U_e(t_2)]
 \mathbb E[U_f(t_2)U_f(t_3)]
=e^{-150}.
\]
The support graph is the path \(1-2-3\), so its only support spanning tree has weight
\[
e^{-100}e^{-50}=e^{-150}.
\]
But the complete temporal graph has the alternative tree with edges \(1-3\) and \(2-3\), whose weight is
\[
e^{-50}e^{-50}=e^{-100}.
\]
Hence the complete-tree majorant is strictly weaker by an arbitrarily large factor as the time gaps are scaled. The complete-tree theorem cannot simply be relabeled as a support-tree theorem.

This example is not a counterexample to the desired support-restricted estimate: the exact cumulant has precisely the support-tree decay. It isolates the missing step—retaining the coordinate label of each temporal bridge.

## 4. Relation to weighted dependency-graph product stability

Féray's weighted-dependency-graph product stability theorem (Proposition 5.11 in *Weighted dependency graphs*, arXiv:1605.03836) applies to monomials of bounded degree, but its resulting constants \(D_{m,R}\) depend on \(m,R\) and the original cumulant constants. The proof explicitly sums Leonov–Shiryaev multiset partitions. It therefore supplies an ordinary weighted dependency graph, not the uniform exponential-in-\(R\) coefficient required here.

Féray also records that uniform weighted dependency graphs are not stable under products in general (HDR, Section 3.3.5). This does not rule out a stronger theorem for the present independent-link Markov structure, but it prevents treating product stability as an automatic solution.

References:
- V. Féray, *Weighted dependency graphs*, Electronic Journal of Probability 23 (2018), paper 93, arXiv:1605.03836, Proposition 5.11.
- V. Féray, *On random combinatorial structures: partitions, permutations and asymptotic normality*, HDR (2021), Section 3.3.5, especially the warning following Definition 3.19.

## 5. New sharply stated target

The remaining one-time monomial problem is now isolated as a coordinate-resolved Markov cumulant inequality:
\[
\boxed{
|\kappa(A_1(t_1),\ldots,A_R(t_R))|
\le C^R\prod_i\prod_{e\in X_i}\|f_{i,e}\|_\infty
\sum_{T\in\mathcal T(G_X)}
\prod_{\{i,j\}\in T}e^{-\Delta_*|t_i-t_j|}.
}
\tag{5.1}
\]
The constant must be independent of \(R\), the number of links, and all repeated support-type multiplicities, with only the fixed row-incidence bound \(m=\sup_i|X_i|\) entering \(C=C(m)\) (and the uniform link semigroup constants).

The product-semigroup argument proves the same statement with \(\mathcal T_R\), the complete graph, in place of \(\mathcal T(G_X)\). Exact support factorization proves zero when \(G_X\) is disconnected. The missing theorem is the interpolation between these facts: every edge in the cumulant tree must be assigned to a common link coordinate, while the signed LS cancellations remain intact.

A promising analytic formulation is a coordinate-resolved forest interpolation for the product generator
\[
\mathcal L=\sum_{e\in E}\mathcal L_e,
\]
in which a bridge created by \(\mathcal L_e\) can join only row ports carrying coordinate \(e\). A global-gap estimate discards this color and is therefore insufficient.

## 6. Proof boundary

Established:
- product-semigroup \(L^2\)-gap tensorization (1.1);
- exponential complete-temporal-tree estimate (1.2), by the existing one-link Markov cumulant theorem;
- exact support-component factorization (2.1);
- the explicit three-row diagnostic showing why (1.2) does not imply (5.1).

Open:
- coordinate-resolved forest interpolation / support-restricted bound (5.1);
- time-integrated spatial summation and KP convergence;
- interacting-vacuum Poincaré inequality, physical scale setting, and continuum mass gap.

No P0–P5 gate is promoted.
