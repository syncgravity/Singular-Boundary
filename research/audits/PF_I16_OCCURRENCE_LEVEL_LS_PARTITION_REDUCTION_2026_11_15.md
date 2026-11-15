# PF-I16 — Exact occurrence-level Leonov–Shiryaev reduction

**Date:** 2026-11-15  
**Status:** Exact algebraic reduction proved below. The resulting uniform decorated-tree resummation is stated as a precise remaining inequality; it is not claimed proved.

## 1. Slot and row partitions

Fix a monomial term in each of R row observables,
\[
A_i=\prod_{e\in X_i}Y_{i,e},\qquad
Y_{i,e}=f_{i,e}(X_e(t_i)).
\]
Let the slot set be
\[
\mathscr S=\{(i,e):1\le i\le R,\ e\in X_i\}.
\]
Let \(\rho\) be the partition of \(\mathscr S\) into row blocks
\(\rho_i=\{(i,e):e\in X_i\}\). For each link e, let
\(\mathscr S_e=\{(i,e)\in\mathscr S\}\).

The Leonov–Shiryaev product-cumulant formula gives
\[
\kappa(A_1,\ldots,A_R)
=
\sum_{\substack{\pi\in\Pi(\mathscr S)\\
                 \pi\vee\rho=\hat 1}}
\prod_{B\in\pi}\kappa(Y_s:s\in B).
\tag{1.1}
\]
Here \(\pi\vee\rho=\hat1\) means that the slot blocks, joined through common row labels, connect all R row labels.

The link paths \((X_e)_e\) are independent. A joint cumulant of variables from two nonempty independent subfamilies is zero. Consequently every nonzero block B in (1.1) is monochromatic in its link label. Thus (1.1) is exactly
\[
\boxed{
\kappa(A_1,\ldots,A_R)
=
\sum_{\substack{(\pi_e)_{e}\\
      (\bigvee_e\pi_e)\vee\rho=\hat1}}
\prod_e\prod_{B\in\pi_e}
\kappa_e(Y_{i,e}:i\in B),
}
\tag{1.2}
\]
where \(\pi_e\) ranges over partitions of the row set
\(I_e=\{i:e\in X_i\}\). Singleton blocks contribute expectations. Formula (1.2) preserves the original occurrence labels and is valid for unrestricted repeated support labels.

## 2. From local temporal trees to a connected row graph

For a block B of size at least two, the one-link temporal-tree theorem supplies
\[
|\kappa_e(Y_{i,e}:i\in B)|
\le
2^{|B|-2}\prod_{i\in B}\|f_{i,e}\|_\infty
\sum_{T_B\in\mathcal T(B)}
\prod_{\{i,j\}\in E(T_B)}
e^{-\Delta_0|t_i-t_j|}.
\tag{2.1}
\]
Each edge in \(T_B\) joins two rows that both use link e. Singleton blocks are bounded by their one-slot sup norm.

For any fixed tuple \((\pi_e)_e\) admitted in (1.2), choose one temporal tree for each nonsingleton block. Their union is connected on the original row labels: this is precisely the join condition in (1.2). Every edge joins rows with a common link, so the union is a connected multigraph contained in the row support-overlap graph. In particular it contains a spanning tree of that graph.

This proves the **connectivity mechanism** and identifies the admissible edge set. It does not yet prove the desired coefficient bound after summing over all link partitions and all local temporal trees.

## 3. The remaining resummation inequality

Write
\[
w_{ij}=e^{-\Delta_0|t_i-t_j|}
\quad\text{for }\{i,j\}\text{ with }X_i\cap X_j\ne\varnothing,
\]
and let \(G_X\) be the row support-overlap graph. The missing uniform estimate is a bound of the form
\[
\begin{aligned}
&\sum_{\substack{(\pi_e)_e\\
      (\bigvee_e\pi_e)\vee\rho=\hat1}}
\prod_e\prod_{B\in\pi_e}
\left[
  2^{(|B|-2)_+}
  \sum_{T_B\in\mathcal T(B)}
  \prod_{\{i,j\}\in E(T_B)}w_{ij}
\right] \\
&\hspace{2cm}\le
C^R\sum_{T\in\mathcal T(G_X)}
\prod_{\{i,j\}\in E(T)}w_{ij},
\end{aligned}
\tag{3.1}
\]
with a constant C depending only on the fixed row arity and the maximum number of **distinct support types** incident to a link (232 here), but not on the occurrence multiplicities \(|I_S|\), the number of links, or the time horizon.

The left side of (3.1) is an absolute-value majorant. A proof may need to preserve additional cancellations in (1.2), rather than bound every partition separately. In particular, the crude observation that each connected union contains some spanning tree does not suffice: the number of preimages of a row tree under the choices of link partitions and local trees must itself be controlled uniformly.

The exact factorization by support type in the repeated-insertion audit is compatible with (1.2), but does not prove (3.1). Nor does pairwise block HGR tensorization: the three-way hyperedge counterexample in the companion audit shows that pairwise subjective-HGR control cannot replace the missing higher-order estimate.

## 4. Proof ledger

Established:
- the occurrence-level Leonov–Shiryaev identity (1.1);
- vanishing of mixed-link cumulant blocks by independence;
- the monochromatic-link representation (1.2);
- the fact that local temporal trees, if inserted, form a connected row multigraph supported on common-link edges.

Still open:
- the multiplicity-uniform resummation (3.1), or a sharper signed/canceling replacement;
- the sparse support-overlap case with unrestricted repeated labels;
- KP convergence, interacting-vacuum Poincaré, physical scale setting, and the continuum mass gap.

No proof gate is promoted by this reduction.
