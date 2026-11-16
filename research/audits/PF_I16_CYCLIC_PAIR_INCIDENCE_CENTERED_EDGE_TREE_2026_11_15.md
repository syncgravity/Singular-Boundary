# PF-I16 — Exact centered-edge expansion for cyclic pair-incidence supports

**Date:** 2026-11-15  
**Status:** ESTABLISHED for arbitrary finite connected multigraph link–row incidence in which every link is incident to exactly two distinct rows. This includes cyclic support graphs, arbitrary parallel links, and nonzero one-slot means. It yields a support-restricted temporal spanning-tree estimate using only one-link two-time covariance decay. Hyperedges incident to three or more rows remain outside this lemma.

## 1. Setup

Let (V=[R]), (R\ge2), and let (E) be a finite set of independent link processes. Each link label (e\in E) is incident to exactly two distinct rows, denoted (i(e),j(e)). Parallel link labels between the same row pair are allowed. The row observables are
[
A_i=\prod_{e:\,i\in\{i(e),j(e)\}}Y_{e,i},
\qquad
Y_{e,i}=f_{e,i}(X_e(t_i)).
\tag{1.1}
]
Different link processes are independent; the two endpoint observables on one link may be dependent. Assume (|Y_{e,i}|\le M_{e,i}).

Set
[
\mu_{e,i}=\mathbb E Y_{e,i},\qquad
\widetilde Y_{e,i}=Y_{e,i}-\mu_{e,i},\qquad
c_e=\mathbb E[\widetilde Y_{e,i(e)}\widetilde Y_{e,j(e)}].
\tag{1.2}
]
Let (G) be the row multigraph with one labeled edge for each link. Its underlying simple support graph is denoted (G_s).

## 2. Exact connected-subgraph identity

**Theorem.**
[
\boxed{
\kappa(A_1,\ldots,A_R)
=
\sum_{\substack{H\subseteq E:\ (V,H)\text{ connected}}}
\left(\prod_{e\in H}c_e\right)
\left(\prod_{e\notin H}
\mu_{e,i(e)}\mu_{e,j(e)}\right).
}
\tag{2.1}
]
The identity holds for arbitrary endpoint means and arbitrary within-link pair laws.

**Proof.** Expand each row product using (Y_{e,i}=\mu_{e,i}+\widetilde Y_{e,i}). By multilinearity of joint cumulants, the cumulant is a sum over choices (S_i\subseteq E(i)), where (E(i)) is the set of link labels incident to row i. The coefficient of a choice is the product of means for all omitted endpoint slots, and the row variable in that cumulant is
[
B_i=\prod_{e\in S_i}\widetilde Y_{e,i}.
]
If a link e is selected at exactly one endpoint, say i, then every joint moment involving (B_i) and any collection of other row variables contains the factor (\mathbb E\widetilde Y_{e,i}=0), because this centered link coordinate occurs nowhere else and is independent of all other link processes. The moment-partition formula therefore gives (\kappa(B_1,\ldots,B_R)=0). If some row selects no link, then (B_i=1), and the cumulant is again zero for (R\ge2).

Thus a nonzero term must select each active link at both endpoints, and the active link set H must touch every row. If H is disconnected, its row variables split into independent components, so the cumulant vanishes. Hence only connected spanning H survive.

For connected spanning H, consider a joint moment (\mathbb E\prod_{i\in C}B_i) for a nonempty proper row subset C. Since H is connected, some edge of H crosses the cut (C,V\C). Exactly one centered endpoint variable of that edge occurs in the product, so the moment is zero. The full moment factors over independent links:
[
\mathbb E\prod_{i\in V}B_i
=\prod_{e\in H}\mathbb E[
\widetilde Y_{e,i(e)}\widetilde Y_{e,j(e)}]
=\prod_{e\in H}c_e.
]
All proper nonempty subset moments vanish, so the joint cumulant of the B_i equals this full moment. The omitted endpoints contribute the product of means in (2.1). Summing the surviving choices proves the identity. \(\square\)

This is a signed connected-subgraph expansion, not the occurrence-level LS absolute majorant. It preserves the cancellation by centering each two-row link before selecting its active edge set.

## 3. Support-restricted temporal-tree bound

Assume each link has a stationary reversible semigroup with gap at least \(\Delta_0>0\). Then
[
|c_e|
=|\langle (f_{e,i}-\mu_{e,i}),P_{|t_i-t_j|}
(f_{e,j}-\mu_{e,j})\rangle|
\le
4M_{e,i}M_{e,j}e^{-\Delta_0|t_i-t_j|}.
\tag{3.1}
]
Also
[
|c_e|+|\mu_{e,i}\mu_{e,j}|
\le5M_{e,i}M_{e,j}.
\tag{3.2}
]

For every connected H in (2.1), choose one spanning tree of its underlying row graph and one link label on each tree edge. Summing over all such choices and then enlarging the non-tree edge choices gives
[
\begin{aligned}
|\kappa(A_1,\ldots,A_R)|
&\le
5^{|E|}(4m)^{R-1}
\left(\prod_{i\in V}\prod_{e\in E(i)}M_{e,i}\right)
\sum_{T\in\mathcal T(G_s)}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|},
\end{aligned}
\tag{3.3}
]
provided the row degree (counting parallel links) is at most m.

Indeed, a tree edge has at most m parallel link labels, each contributing at most the factor 4 in (3.1); all other link labels contribute at most the factor 5 in (3.2). Since every connected H contains a spanning tree, the right-hand side covers every term of (2.1), possibly more than once. The number of link labels satisfies \(|E|\le mR/2\), so
[
5^{|E|}(4m)^{R-1}
\le
\left(5^{m/2}4m\right)^R.
\tag{3.4}
]
Thus (3.3) has an exponential-in-row-order coefficient, independent of the number of temporal sample points elsewhere and without a per-link occurrence cap.

For a simple support graph (no parallel links), m may be replaced by the maximum simple degree in the tree-label factor, and the coefficient improves to \(5^{|E|}4^{R-1}\).

## 4. Scope and next obstruction

- Arbitrary cyclic pair-incidence graphs: **ESTABLISHED**.
- Parallel two-row links: **ESTABLISHED**.
- Nonzero slot means: **ESTABLISHED** by the exact expansion (2.1).
- Temporal decay: uses only the two-time link covariance gap, not higher link cumulant estimates.
- Bounded row incidence m: gives the exponential coefficient in (3.4).
- Hyperedges incident to three or more rows: **OPEN**. A centered hyperedge can cross a row cut with two or more selected endpoints on each side, so the singleton-mean cut argument used in the proof no longer forces its moment to vanish.
- Unrestricted repeated multi-row support labels, the general cyclic hypergraph case, time-integrated support summation, KP convergence, interacting-vacuum Poincaré, physical scale setting, and the continuum mass gap remain open.

The companion verifier checks (2.1) exactly over rational finite pair laws for paths, cycles, branching graphs, complete graphs, and parallel-edge examples. It verifies the finite algebraic identity; the proof and temporal estimate above are analytic. No P0–P5 gate is promoted.
