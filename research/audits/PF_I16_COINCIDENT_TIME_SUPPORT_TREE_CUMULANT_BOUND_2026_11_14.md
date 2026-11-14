# PF-I16 — Coincident-time support-tree cumulant bound

**Date:** 2026-11-14  
**Status:** exact support-disconnection and complete-graph tree envelope ESTABLISHED; sparse support-tree count remains OPEN  
**Scope:** finite link set and independent Haar link coordinates. No P0–P5 gate is promoted.

## 1. Statement

Let \(U=(U_e)_{e\in E}\) have product Haar law. For \(i=1,\ldots,r\), let
\[
Y_i=F_i(U_{X_i}),\qquad \|F_i\|_\infty\le M_i,
\]
where \(X_i\subseteq E\) is finite. Let \(G_X\) be the support-overlap graph, with \(ij\in E(G_X)\) iff \(X_i\cap X_j\ne\varnothing\).

For every \(r\ge2\), if \(G_X\) is disconnected then
\[
\kappa(Y_1,\ldots,Y_r)=0.
\]
If \(G_X\) is connected, the universal moment-cumulant estimate is
\[
|\kappa(Y_1,\ldots,Y_r)|
\le 4^r\Big(\prod_{i=1}^r M_i\Big)r^{r-2}.
\tag{1.1}
\]
This is a complete-graph Cayley-tree envelope, not yet a bound by the number of spanning trees of the actual support graph. At coincident times all temporal edge weights equal one, so (1.1) is a useful but non-sharp baseline for the desired support-tree-sum estimate.

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

By Cayley's formula, the complete graph has \(r^{r-2}\) spanning trees. Since \(G_X\) is connected, it has at least one spanning tree, so
\[
r^{r-2}\le r^{r-2}|\mathcal T(G_X)|
\]
is not the useful direction; instead use the connected-graph bound
\[
|\mathcal T(G_X)|\ge1
\]
and (2.2) only gives \(4^r r^{r-2}\), which is **not** bounded by \(4^r|\mathcal T(G_X)|\) for a sparse graph. To obtain (1.1) with a support-tree count, use the sharper graph-sensitive cumulant estimate below.

For each partition \(\pi\), form its block-intersection graph \(K_\pi\) on the blocks of \(\pi\), joining two blocks if some support edge of \(G_X\) crosses them. If \(K_\pi\) is disconnected, the block products factor across a support cut. The standard connected-partition cancellation in the cumulant formula removes all such disconnected contributions. The surviving terms are indexed by connected partitions of \(G_X\), and their absolute coefficient sum is bounded by the rooted-forest expansion. A connected partition has a spanning tree of \(G_X\) crossing its blocks; summing over rooted forests and then forgetting roots gives the graph-sensitive bound
\[
\sum_{\pi\ {\rm connected}}(|\pi|-1)!
\le 4^r|\mathcal T(G_X)|.
\tag{2.3}
\]
For completeness, (2.3) is the only nontrivial combinatorial claim in this proof and is not established by the preceding estimates alone.

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
