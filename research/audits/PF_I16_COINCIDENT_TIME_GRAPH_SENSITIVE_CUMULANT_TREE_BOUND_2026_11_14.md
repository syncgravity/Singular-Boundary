# PF-I16 — Graph-sensitive coincident-time cumulant tree bound

**Date:** 2026-11-14  
**Status:** ESTABLISHED for arbitrary bounded local observables under independent product Haar; noncoincident-time extension OPEN  
**Scope:** finite simple support-overlap graph. No P0–P5 gate is promoted.

## 1. Theorem

Let \(U=(U_e)_{e\in E}\) have independent link coordinates (in particular, product Haar). For \(i=1,\ldots,r\), let
\[
Y_i=F_i(U_{X_i}),\qquad \|F_i\|_\infty\le M_i,
\]
and let \(G=G_X\) be the support-overlap graph:
\[
ij\in E(G)\quad\Longleftrightarrow\quad X_i\cap X_j\ne\varnothing.
\]
Write \(\tau(G)\) for the number of spanning trees, with \(\tau(G)=0\) when \(G\) is disconnected. Then
\[
\boxed{\quad
|\kappa(Y_1,\ldots,Y_r)|
\le 2^{r-1}\tau(G)\prod_{i=1}^r M_i.
\quad}
\tag{1.1}
\]
This is the desired support-tree-sum estimate at coincident times: every temporal edge weight is one, so the sum over support spanning trees is exactly \(\tau(G)\).

## 2. Regroup the moment-cumulant formula by connected components

For a nonempty row set \(B\subseteq[r]\), let \(\operatorname{Comp}_G(B)\) be the connected components of the induced graph \(G[B]\), and set
\[
\mu_C=\mathbb E\prod_{i\in C}Y_i
\]
for each nonempty connected vertex set \(C\). Since distinct components of \(G[B]\) have disjoint unions of link supports, their observables are independent. Hence
\[
m(B):=\mathbb E\prod_{i\in B}Y_i
=\prod_{C\in\operatorname{Comp}_G(B)}\mu_C.
\tag{2.1}
\]

The ordinary moment-cumulant formula is
\[
\kappa(Y_1,\ldots,Y_r)
=\sum_{\pi\in\Pi_r}(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{B\in\pi}m(B).
\tag{2.2}
\]
For each \(\pi\), refine every block \(B\) into the components of \(G[B]\). The result is a partition \(\sigma\) of \([r]\) into connected vertex sets. Fix such a \(\sigma\), with \(k=|\sigma|\), and form its quotient graph \(Q_\sigma\): its vertices are the blocks of \(\sigma\), with two blocks adjacent exactly when at least one edge of \(G\) joins them.

The original partition \(\pi\) refines to \(\sigma\) in precisely this way if and only if each block of \(\pi\), viewed as a set of vertices of \(Q_\sigma\), is an independent set. Thus the \(\pi\)'s giving this fixed \(\sigma\) are exactly the proper set partitions of \(Q_\sigma\).

The chromatic polynomial has the set-partition expansion
\[
\chi_{Q}(q)=
\sum_{\rho\text{ proper partition of }V(Q)}
(q)_{|\rho|},
\qquad
(q)_j=q(q-1)\cdots(q-j+1).
\tag{2.3}
\]
The coefficient of \(q\) in \((q)_j\) is
\((-1)^{j-1}(j-1)!\). Therefore, if \(c(Q)=[q]\chi_Q(q)\), regrouping (2.2) gives the exact identity
\[
\boxed{\quad
\kappa(Y_1,\ldots,Y_r)
=\sum_{\substack{\sigma\text{ partition of }[r]\\
\text{each block of }\sigma\text{ connected in }G}}
c(Q_\sigma)\prod_{C\in\sigma}\mu_C.
\quad}
\tag{2.4}
\]

This is the cancellation-preserving step: the Möbius coefficients are summed exactly within each quotient graph before taking absolute values.

## 3. Chromatic coefficient is bounded by spanning trees

For every finite graph \(Q\),
\[
c(Q)=0\quad\text{if \(Q\) is disconnected},
\qquad
|c(Q)|\le\tau(Q)\quad\text{if \(Q\) is connected}.
\tag{3.1}
\]
Here is a short deletion-contraction proof. The claim is immediate for a single vertex. For a connected graph with an edge \(e\), use
\[
\chi_Q(q)=\chi_{Q-e}(q)-\chi_{Q/e}(q).
\]
If \(e\) is a bridge, \(Q-e\) is disconnected, so its chromatic polynomial has no linear term; hence
\(|c(Q)|=|c(Q/e)|\le\tau(Q/e)=\tau(Q)\).
If \(e\) is not a bridge, both \(Q-e\) and \(Q/e\) are connected, and
\[
|c(Q)|\le |c(Q-e)|+|c(Q/e)|
\le\tau(Q-e)+\tau(Q/e)=\tau(Q).
\]
Contractions are interpreted as multigraph contractions; parallel edges are retained for spanning-tree counting and do not change the chromatic polynomial. This proves (3.1) by induction. If \(Q\) is disconnected with at least two components, \(\chi_Q\) is divisible by \(q^2\), so \(c(Q)=0\).

## 4. Lift quotient trees and count them by cutting a spanning tree

For a connected quotient \(Q_\sigma\), choose:
- a spanning tree in each connected induced block \(G[C]\), \(C\in\sigma\);
- a spanning tree of \(Q_\sigma\);
- for each quotient-tree edge \(CD\), one actual edge of \(G\) joining \(C\) to \(D\).

The union is a spanning tree \(T\) of \(G\). Let \(L_\sigma\) be the number of such choices. Every block is connected by definition, and every quotient edge has at least one lift, so
\[
\tau(Q_\sigma)\le L_\sigma.
\tag{4.1}
\]

There is an exact bijection between all lifted choices \((\sigma,\text{internal trees},\text{quotient tree},\text{edge lifts})\) and pairs \((T,S)\), where \(T\) is a spanning tree of \(G\) and \(S\subseteq E(T)\) is the set of edges cut between blocks of \(\sigma\). Given a lifted tree and \(\sigma\), \(S\) consists of the selected inter-block edges. Conversely, given \((T,S)\), the blocks of \(\sigma\) are the components of \(T\setminus S\); the uncut edges are their internal trees, and the cut edges form the quotient tree with their actual edge lifts. Thus
\[
\sum_{\substack{\sigma\text{ connected-block partition}\\Q_\sigma\text{ connected}}}
L_\sigma
=2^{r-1}\tau(G),
\tag{4.2}
\]
because each spanning tree has \(r-1\) edges and hence \(2^{r-1}\) cut subsets.

Combining (2.4), (3.1), (4.1), (4.2), and
\(|\mu_C|\le\prod_{i\in C}M_i\), proves (1.1).

If \(G\) is disconnected, the variables split into independent nonempty families and the joint cumulant is zero, agreeing with \(\tau(G)=0\).

## 5. Scope and next extension

- The graph-sensitive tree count is now established at coincident times for arbitrary bounded local observables over independent link coordinates.
- The proof explicitly preserves the support graph and sums signed partition coefficients before taking absolute values.
- The constant \(2^{r-1}\) is an upper bound from the cut-subset count; no optimality is claimed.
- The noncoincident-time estimate with edge weights \(e^{-\Delta_0|t_i-t_j|}\) is still OPEN. The quotient-graph regrouping is algebraic and uses independence at a common time; it does not by itself retain Markov temporal contractions.
- Smooth face/pair temporal specialization, marked-root spatial summation, quantum KP convergence, interacting-vacuum Poincare inequality, and continuum mass gap remain OPEN.

No P0–P5 acceptance status is promoted.
