# PF-I16 — Cumulant factorization on an acyclic link–row incidence hypergraph

**Date:** 2026-11-15  
**Status:** ESTABLISHED for finite families whose bipartite link–row incidence graph is a tree (or a forest, componentwise). The result allows arbitrary within-link dependence, nonzero means, and any number of links. Combining it with the one-link temporal-tree estimate gives a support-restricted tree bound with coefficient at most (2^{mR}) when each row has at most m link slots. Cyclic incidence hypergraphs, including repeated multi-link support labels, remain outside this theorem.

## 1. Setup and incidence acyclicity

Let (L) be a finite set of independent link processes. For each link e, let (H_esubseteq[R]) be the rows carrying a slot on that link, and let
[
X_{e,i}=f_{e,i}(X_e(t_i)),qquad iin H_e.
]
The row observable is
[
A_i=prod_{e:,iin H_e}X_{e,i}.
	ag{1.1}
]
Assume every row belongs to at least one link. Form the bipartite incidence graph with row vertices ([R]), link vertices L, and edge (isim e) iff (iin H_e). Assume this graph is a tree.

No independence is assumed among the variables ((X_{e,i})_{iin H_e}) on a fixed link. Independence is assumed only between distinct link processes.

## 2. Exact cumulant factorization

**Theorem.**
[
oxed{
kappa(A_1,ldots,A_R)
=
prod_{ein L}kappa_e(X_{e,i}:iin H_e).
}
	ag{2.1}
]

**Proof by leaf-link induction.** If there is one link, (2.1) is the definition of the row variables. Suppose there are at least two links. In the incidence tree, remove all row vertices of degree one. The remaining nonempty core is a tree. Choose a leaf link vertex e in this core. It has exactly one neighbor o in the core; every other row in (H_esetminus{o}) has degree one in the original incidence graph. Thus e meets the rest of the link system in exactly the one articulation row o.

Write
[
B_i=prod_{f
e e:,iin H_f}X_{f,i}
]
for rows in the remaining incidence system. For (iin H_esetminus{o}), the original row variable is (A_i=X_{e,i}); for the articulation row it is (A_o=X_{e,o}B_o); and for all other rows it is (B_i). The vector of e-link variables is independent of the entire remaining vector ((B_i)). Apply the one-row-intersection factorization theorem:
[
kappa(A_1,ldots,A_R)
=
kappa_e(X_{e,i}:iin H_e),
kappa_{m rest}(B_i:i
otin H_esetminus{o}).
]
Deleting e and its private row leaves a smaller incidence tree. Induction proves (2.1). (square)

The one-row-intersection theorem used in the induction is recorded separately in [PF-I16 exact cumulant gluing at a one-row hyperedge intersection](PF_I16_ONE_ROW_HYPEREDGE_ARTICULATION_CUMULANT_GLUE_2026_11_15.md).

## 3. Support-restricted temporal-tree estimate

Assume each link satisfies the one-link Markov temporal-tree estimate
[
|kappa_e(X_{e,i}:iin H_e)|
le
2^{(|H_e|-2)_+}
prod_{iin H_e}|f_{e,i}|_\infty
sum_{T_e\in\mathcal T(H_e)}
\prod_{\{i,j\}\in E(T_e)}
e^{-\Delta_0|t_i-t_j|},
	ag{3.1}
]
with the singleton convention that the cumulant is the mean and the tree polynomial is 1.

The union of the link cliques (K_{H_e}) is a block graph: distinct link cliques intersect only at articulation rows, and their block–cut incidence graph is a tree. Consequently, choosing one spanning tree (T_e) in each link clique gives a spanning tree of the full row support graph (G_X), and every spanning tree of (G_X) decomposes uniquely in this way. Equivalently,
[
prod_{ein L}
left(
sum_{T_e\in\mathcal T(H_e)}w(T_e)
ight)
=
sum_{T\in\mathcal T(G_X)}w(T).
	ag{3.2}
]
Combining (2.1)–(3.2) yields
[
oxed{
|kappa(A_1,ldots,A_R)|
le
2^{\sum_{e\in L}(|H_e|-2)_+}
\left(\prod_{e\in L}\prod_{i\in H_e}\|f_{e,i}\|_\infty\right)
\sum_{T\in\mathcal T(G_X)}
\prod_{\{i,j\}\in E(T)}e^{-\Delta_0|t_i-t_j|}.
}
\tag{3.3}
]
If each row has at most m link slots, then
[
sum_e |H_e|\le mR,qquad
2^{\sum_e(|H_e|-2)_+}\le2^{mR}.
	ag{3.4}
]
Thus the coefficient is exponential in R and independent of the number of observations on a link beyond the explicit row count. There is no per-link multiplicity cap D.

## 4. Scope

- Acyclic link–row incidence: **ESTABLISHED**, exact factorization (2.1).
- Temporal support-tree bound (3.3): **ESTABLISHED** under the one-link Markov temporal-tree hypothesis.
- Arbitrary within-link dependence and nonzero means: allowed.
- Cyclic incidence hypergraphs: **OPEN**. If two rows share two or more links, the incidence graph contains a cycle; this includes repeated occurrences of a multi-link support label. The factorization (2.1) is not asserted there.
- The absolute-value LS resummation obstruction remains in force; this theorem bypasses it only on acyclic incidence.
- General unrestricted sparse-support repetitions, the multi-hyperedge weighted connected-log estimate, KP convergence, interacting-vacuum Poincaré, physical scale setting, and the continuum mass gap remain open.

The companion verifier checks (2.1) exactly with rational finite distributions for several incidence trees, including chains, stars, branching, singleton link supports, and nonzero means. The analytic proof is the leaf-link induction above.
