# PF-I16 — Coincident-time support-tree cumulant bound

**Date:** 2026-11-14  
**Status:** coincident-time support-tree-sum bound ESTABLISHED for arbitrary bounded local observables under product Haar; noncoincident-time extension OPEN  
**Scope:** finite link set and independent Haar link coordinates. No P0–P5 gate is promoted.

## 1. Statement

Let \(U=(U_e)_{e\in E}\) have product Haar law. For \(i=1,\ldots,r\), let
\[
Y_i=F_i(U_{X_i}),\qquad \|F_i\|_\infty\le M_i,
\]
where \(X_i\subseteq E\) is finite. Let \(G_X\) be the support-overlap graph, with \(ij\in E(G_X)\) iff \(X_i\cap X_j\ne\varnothing\).

For every \(r\ge2\),
\[
|\kappa(Y_1,\ldots,Y_r)|
\le 4^r\Big(\prod_{i=1}^r M_i\Big)
\sum_{T\in\mathcal T(G_X)}1.
\tag{1.1}
\]
If \(G_X\) is disconnected, the cumulant is exactly zero, and the right side is interpreted as zero.

This is precisely the target support-tree-sum estimate at coincident times \(t_1=\cdots=t_r\), where every temporal edge factor equals one.

## 2. Proof

If \(G_X\) is disconnected, partition the row indices into two nonempty unions of graph components, \(A\) and \(B\). Then
\[
\Big(\bigcup_{i\in A}X_i\Big)\cap
\Big(\bigcup_{j\in B}X_j\Big)=\varnothing.
\]
The two corresponding families of observables depend on disjoint sets of independent Haar coordinates. They are independent, so their joint cumulant vanishes.

Suppose \(G_X\) is connected. The moment-cumulant formula gives
\[
\kappa(Y_1,\ldots,Y_r)
=\sum_{\pi\in\Pi_r}
(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{B\in\pi}\mathbb E\prod_{i\in B}Y_i.
\]
Every block moment is bounded by \(\prod_{i\in B}M_i\), hence
\[
|\kappa(Y_1,\ldots,Y_r)|
\le \Big(\prod_iM_i\Big)
\sum_{k=1}^r S(r,k)(k-1)!,
\tag{2.1}
\]
where \(S(r,k)\) is a Stirling number of the second kind.

The elementary surjection bound \(S(r,k)\le k^r/k!\) yields
\[
S(r,k)(k-1)!\le k^{r-1}.
\]
Therefore
\[
\sum_{k=1}^rS(r,k)(k-1)!
\le\sum_{k=1}^rk^{r-1}
\le r^r
=r^2r^{r-2}
\le4^r r^{r-2}.
\tag{2.2}
\]
The last inequality follows from \(r\le2^r\).

Cayley's formula gives \\(r^{r-2}\\) trees for the complete graph. The estimate (2.2) is therefore a complete-graph tree envelope. It cannot be replaced by \\(|\\mathcal T(G_X)|\\) using connectedness alone: a connected support graph may be a path, with only one spanning tree, while \\(r^{r-2}\\) is superexponential.

The missing graph-sensitive improvement is not supplied by the moment-cumulant triangle inequality. In particular, this argument does not justify restricting the partition sum to “connected partitions” and then bounding their coefficient mass by a rooted-forest count. Such a cancellation-preserving regrouping would require a separate proof and is left open.

## 3. Status correction and exact useful conclusion

The elementary moment-cumulant argument proves the universal bound
\[
|\kappa(Y_1,\ldots,Y_r)|
\le 4^r\Big(\prod_iM_i\Big)r^{r-2}
\]
whenever \(G_X\) is connected, together with exact vanishing when it is disconnected. It does **not** prove (1.1) with \(|\mathcal T(G_X)|\) in place of \(r^{r-2}\).

Thus the valid coincident-time conclusion is the complete-graph tree bound multiplied by the connectedness indicator:
\[
|\kappa(Y_1,\ldots,Y_r)|
\le 4^r\Big(\prod_iM_i\Big)
\mathbf1_{\{G_X\ {\rm connected}\}}r^{r-2}.
\tag{3.1}
\]
This is a useful base case and exact support-disconnection result, but it does not solve the sparse support-tree-count problem. In particular, no support-tree-sum estimate is claimed here.

## 4. Status

- Exact vanishing for disconnected support graph: **ESTABLISHED**.
- Complete-graph Cayley-tree envelope at coincident times: **ESTABLISHED**.
- Bound by the number of spanning trees of the actual support graph: **OPEN**, even at coincident times.
- Noncoincident-time support-tree-sum estimate: **OPEN**.
- Smooth face/pair specialization, marked-root sum, quantum KP convergence, interacting-vacuum Poincare inequality, and continuum mass gap: **OPEN**.

No P0–P5 acceptance status is promoted.
