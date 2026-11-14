# PF-I16 — Product-cumulant support-temporal tree extraction and fiber obstruction

**Date:** 2026-11-14  
**Status:** exact termwise support-temporal tree extraction established; cancellation-preserving slot-partition summation remains OPEN  
**Scope:** finite-regulator product insertions under independent link path laws. No P0–P5 gate is promoted.

## 1. Product-cumulant slot formula

Let
\[
A_i(t_i)=\prod_{e\in X_i}Y_{i,e}(t_i),\qquad i\in[r],
\]
where the link path processes are independent. Write \(I_e=\{i:e\in X_i\}\). The Leonov–Shiryaev product-cumulant formula sums over one set partition \(\pi_e\in\Pi(I_e)\) for each link:
\[
\kappa(A_1,\ldots,A_r)
=
\sum_{\substack{(\pi_e)_e\\
\bigvee_e\pi_e\vee\sigma=1}}
\prod_e\prod_{B\in\pi_e}
\kappa_e(Y_{i,e}:i\in B).
\tag{1.1}
\]
Here \(\sigma\) is the partition into insertion rows; equivalently, the join condition says that the row hypergraph whose hyperedges are the blocks \(B\in\pi_e\) is connected. Singleton blocks are retained.

Assume the one-link temporal estimate
\[
|\kappa_e(Y_{i,e}:i\in B)|
\le a_e(B)\,
e^{-\Delta\,\operatorname{span}_t(B)}
\prod_{i\in B}\|Y_{i,e}\|_\infty,
\qquad |B|\ge2,
\tag{1.2}
\]
where \(\operatorname{span}_t(B)=\max_{i\in B}t_i-\min_{i\in B}t_i\). Singleton blocks have no decay factor.

## 2. Every connected slot-partition term contains a support-temporal spanning tree

For each non-singleton block \(B\in\pi_e\), order its row labels by their times, breaking ties by row label:
\[
i_1,\ldots,i_k,\qquad t_{i_1}\le\cdots\le t_{i_k}.
\]
Replace the hyperedge \(B\) by its temporal path
\[
P_e(B)=\{\{i_1,i_2\},\ldots,\{i_{k-1},i_k\}\}.
\]
Every edge of this path belongs to the insertion support-overlap graph
\[
G_X:\quad i\sim j\iff X_i\cap X_j\ne\varnothing,
\]
because all rows in \(B\) contain the same link \(e\). Its total time length is exactly
\[
\sum_{\{i,j\}\in P_e(B)}|t_i-t_j|
=\operatorname{span}_t(B).
\tag{2.1}
\]

Let \(H_\pi\) be the multigraph obtained by taking the union of all these paths over all links and all non-singleton blocks. Replacing each hyperedge by a path preserves its connected components. Thus the join condition in (1.1) implies that \(H_\pi\) is connected on \([r]\). Select any spanning tree \(T_\pi\subseteq H_\pi\). Since every edge weight is at most one,
\[
\begin{aligned}
\prod_e\prod_{\substack{B\in\pi_e\\|B|\ge2}}
e^{-\Delta\operatorname{span}_t(B)}
&=
\prod_{\{i,j\}\in E(H_\pi)_{\rm mult}}
e^{-\Delta|t_i-t_j|}\\
&\le
\prod_{\{i,j\}\in T_\pi}e^{-\Delta|t_i-t_j|}\\
&\le
\mathcal M(G_X;\mathbf t),
\end{aligned}
\tag{2.2}
\]
where
\[
\mathcal M(G_X;\mathbf t)
=
\max_{T\in\mathcal T(G_X)}
\prod_{\{i,j\}\in T}e^{-\Delta|t_i-t_j|}
=
\exp\!\left[-\Delta\min_{T\in\mathcal T(G_X)}
\sum_{\{i,j\}\in T}|t_i-t_j|\right].
\tag{2.3}
\]
The last maximum is over spanning trees of the support-overlap graph. If that graph is disconnected, the product cumulant vanishes by independence.

**Conclusion:** every individual connected Leonov–Shiryaev summand carries the same support-sensitive maximum-spanning-tree temporal factor. No independent spatial tree and temporal tree are multiplied. The spatial and temporal edges are literally the same edges: consecutive rows in a local link-cumulant block.

## 3. Consequence for normalized time integration

Since \(\mathcal M\le\sum_{T\in\mathcal T(G_X)}\prod_{ij\in T}e^{-\Delta|t_i-t_j|}\), root each tree and integrate leaves:
\[
\int_{[0,\mathcal T]^r}
\prod_{\{i,j\}\in T}e^{-\Delta|t_i-t_j|}\,d\mathbf t
\le
\mathcal T\left(\frac2\Delta\right)^{r-1}.
\]
Using \(|\mathcal T(G_X)|\le r^{r-2}\),
\[
\boxed{
\frac1{r!\mathcal T}\int_{[0,\mathcal T]^r}
\mathcal M(G_X;\mathbf t)\,d\mathbf t
\le
\frac{r^{r-2}}{r!}\left(\frac2\Delta\right)^{r-1}
\le
e^r\left(\frac2\Delta\right)^{r-1}.
}
\tag{3.1}
\]
Therefore a cancellation-preserving pointwise estimate
\[
|\kappa(A_1(t_1),\ldots,A_r(t_r))|
\le C_{\rm slot}^{\,r}
\left(\prod_i\|A_i\|_\infty\right)
\mathcal M(G_X;\mathbf t)
\tag{3.2}
\]
would immediately give an exponential-in-\(r\) normalized Feynman–Kac time-integrated bound. The time integration and the single \(1/r!\) normalization are not the obstruction once (3.2) is available.

## 4. Why the obvious tree map cannot prove (3.2)

The map \((\pi_e)_e\mapsto T_\pi\) has no bounded fiber if it simply selects a canonical tree from the union paths.

Take eight links with identical incidence set \(I_e=[r]\), so every row uses exactly eight links and the source-incidence constraint is saturated:
\[
\sum_e|I_e|=8r.
\]
Fix \(\pi_1=\{[r]\}\), the one-block partition on the first link. This single block already connects all rows. Each of the other seven link partitions can be chosen arbitrarily in \(\Pi([r])\), and the full tuple always satisfies the connected-join condition. If the canonical tree selector gives priority to link 1, all these
\[
\mathrm{Bell}(r)^7
\]
distinct connected slot-partition tuples map to the same temporal path tree from link 1.

Thus termwise tree extraction is exact, but a naive injection into trees loses an unbounded, in fact superexponential, fiber. This is the same cancellation obstruction exposed by the degree-eight Rademacher witness: the large absolute slot-partition family must be resummed with its signs before taking absolute values.

## 5. Exact status and next lemma

**Established**
1. The row-hypergraph connectedness condition in the product-cumulant formula implies connectedness of the union of temporal paths generated by its local blocks.
2. Every connected slot-partition summand is bounded by the same maximum-spanning-tree product on the actual support-overlap graph.
3. The normalized time integral of that maximum-tree factor has only exponential growth, as in (3.1).
4. The naive canonical tree map has Bell\((r)^7\) fibers in an allowed eight-link incidence pattern.

**Still open**
The signed sum in (1.1) must be reorganized before absolute values so that the resulting coefficient after factoring out \(\mathcal M(G_X;\mathbf t)\) is bounded by \(C_{\rm slot}^r\), uniformly over all support families with
\[
\sum_e|I_e|\le8r.
\]
The one-link factorial bound and an absolute Leonov–Shiryaev majorant do not provide this: the latter contains at least \((2e)^{8r}(r!)^8\) in the maximally overlapping example.

The next mathematical target is a **tree-rooted Leonov–Shiryaev resummation**: group all slot partitions that induce the same connected support-temporal tree, perform the linkwise Möbius/cumulant sums inside each fiber while preserving their signs, and prove that the resummed fiber coefficient is at most \(C^r\). If this fails, produce an explicit bounded-link counterexample to that proposed fiber estimate. No all-orders WDG estimate, Feynman–Kac convergence, P3 inequality, or physical mass gap is claimed.
