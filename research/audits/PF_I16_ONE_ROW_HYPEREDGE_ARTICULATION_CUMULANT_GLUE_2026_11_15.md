# PF-I16 — Exact cumulant gluing at a one-row hyperedge intersection

**Date:** 2026-11-15  
**Status:** ESTABLISHED for two independent link families whose row supports cover all rows and intersect in exactly one row. The identity permits arbitrary within-link dependence and nonzero means. It yields a support-restricted temporal-tree estimate by gluing the two one-link trees at the common row. It does not cover intersections of size two or more, nor three or more link families.

## 1. Setup

Let (H_1,H_2subseteq[R]) satisfy
[
H_1cup H_2=[R],qquad H_1cap H_2={o}.
]
Let ((X_i)_{iin H_1}) be an arbitrary jointly distributed family and ((Y_j)_{jin H_2}) another arbitrary jointly distributed family, with the two families independent. Define row variables
[
A_o=X_oY_o,qquad
A_i=X_i (iin H_1setminus{o}),qquad
A_j=Y_j (jin H_2setminus{o}).
]
No variable is assumed centered, and no independence is assumed within either link family.

## 2. Exact factorization

**Theorem.**
[
oxed{
kappa(A_1,ldots,A_R)
=
kappa_1(X_i:iin H_1),
kappa_2(Y_j:jin H_2).
}
	ag{2.1}
]

**Proof.** Introduce commuting source variables (t_i) for (iin H_1setminus{o}), (s_j) for (jin H_2setminus{o}), and (u) for the articulation row. Let
[
M(u,t,s)=
mathbb Eexp!left(
sum_{iin H_1setminus{o}}t_iX_i+
sum_{jin H_2setminus{o}}s_jY_j+
uX_oY_o
ight).
]
The joint cumulant in (2.1) is the coefficient of
(uprod_{i
e o}t_iprod_{j
e o}s_j) in (log M). At (u=0), independence gives
[
M(0,t,s)=M_1(t)M_2(s).
]
Differentiate the logarithm before extracting the remaining coefficient:
[
left.partial_ulog M(u,t,s)ight|_{u=0}
=
rac{mathbb E[X_o e^{sum t_iX_i}]}
     {mathbb E[e^{sum t_iX_i}]}
cdot
rac{mathbb E[Y_o e^{sum s_jY_j}]}
     {mathbb E[e^{sum s_jY_j}]}.
	ag{2.2}
]
The first factor is
(left.partial_vlogmathbb E e^{vX_o+sum t_iX_i}ight|_{v=0});
its coefficient of (prod_{i
e o}t_i) is
(kappa_1(X_i:iin H_1)). The second factor similarly yields
(kappa_2(Y_j:jin H_2)). The two source sets are disjoint, so the coefficient factors, proving (2.1). (square)

This is an exact identity for arbitrary finite-dimensional distributions. It does not rely on a temporal gap, projective expansion, centering, or a bound on the number of observations.

## 3. Temporal-tree consequence

Now suppose (X_i=f_i(X_e(t_i))) are one-time observables on link (e), and (Y_j=g_j(X_f(t_j))) are one-time observables on an independent link (f). Assume each link satisfies the one-link Markov temporal-tree estimate
[
|kappa_e(X_i:iin H_1)|
le 2^{(|H_1|-2)_+}
prod_{iin H_1}|f_i|_\infty
sum_{T_1\in\mathcal T(H_1)}
\prod_{\{i,j\}\in E(T_1)}
e^{-\Delta_0|t_i-t_j|},
	ag{3.1}
]
and similarly for link f, with the singleton convention that its cumulant is its mean and its tree polynomial is 1.

Combining (2.1) and (3.1),
[
egin{aligned}
|kappa(A_1,ldots,A_R)|
&le
2^{(|H_1|-2)_+ + (|H_2|-2)_+}
prod_{i\in H_1}\|f_i\|_\infty
prod_{j\in H_2}\|g_j\|_\infty\
&\quad\times
\left(\sum_{T_1\in\mathcal T(H_1)}w(T_1)\right)
\left(\sum_{T_2\in\mathcal T(H_2)}w(T_2)\right).
end{aligned}
	ag{3.2}
]
Because the support sets intersect in exactly the articulation row o, the union of a tree on H1 and a tree on H2 is a spanning tree on the row support graph
(G=K_{H_1}\cup K_{H_2}), and every spanning tree of G decomposes uniquely this way. Therefore the product of tree polynomials in (3.2) is exactly
[
\sum_{T\in\mathcal T(G)}\prod_{\{i,j\}\in E(T)}w_{ij}.
	ag{3.3}
]
This proves the desired support-restricted tree bound for the two-hyperedge, one-row-intersection geometry, with an explicit exponential coefficient.

## 4. Boundary and next case

- The exact articulation factorization (2.1): **ESTABLISHED**, including nonzero means.
- The support-tree estimate (3.2)–(3.3): **ESTABLISHED** under the one-link temporal-tree hypotheses.
- Two hyperedges with intersection size at least two: **OPEN**; the shared rows no longer separate into a product of two root derivatives.
- Three or more link families: **OPEN**; iterative gluing requires controlling a nontrivial overlap-incidence tree and cannot be inferred from the two-family identity.
- Unrestricted repeated support labels in the general sparse geometry, KP convergence, interacting-vacuum Poincaré, scale setting, and the continuum mass gap remain open.

The companion verifier checks (2.1) exactly with rational finite distributions, including nonzero means and arbitrary within-link dependence, over a range of hyperedge sizes. It is a regression for the algebraic identity; the proof is the generating-function argument above.
