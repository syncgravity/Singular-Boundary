# PF-I16 — Exact occurrence-level Leonov–Shiryaev reduction

**Update (2026-11-15):** The local interlaced block-functional cumulant-tree obligation for the at-most-232 distinct support types on a link is now proved under the compact heat-kernel Doeblin envelope; see `PF_I16_INTERLACED_BLOCK_CUMULANT_TREE_DOEBLIN_REGENERATION_2026_11_15.md`. This supplies a port-count-uniform bound for each grouped support-type block functional. It does **not** by itself prove the multiplicity-uniform resummation of the original occurrence-level LS partition sum below: the latter still has to preserve the original occurrence partition structure and control its signed cancellations.

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

## 3. The absolute-value resummation is obstructed

The absolute-value inequality displayed below is **false in general**, not merely unproved. A two-link complete-overlap counterexample is recorded in [PF-I16 obstruction to the absolute-value LS partition resummation](PF_I16_LS_ABSOLUTE_RESUMMATION_OBSTRUCTION_2026_11_15.md). With all times coincident, one link may use the one-block partition while the second ranges over pair partitions; this gives a lower bound whose ratio to the target complete-graph tree polynomial is at least \(2^{R-2}(R-1)!!\) for even R. No fixed \(C^R\) can absorb it.

Thus the absolute-value majorant below must not be treated as a viable proof obligation. The LS identity and connectivity mechanism remain valid, but any unrestricted-repetition argument must retain cancellations between link partitions or use a different representation. The actual complete-overlap cumulant estimate remains true by the product-semigroup proof.

## 4. The remaining resummation inequality (invalid absolute majorant)

Write
\[
w_{ij}=e^{-\Delta_0|t_i-t_j|}
\quad\text{for }\{i,j\}\text{ with }X_i\cap X_j\ne\varnothing,
\]
and let \(G_X\) be the row support-overlap graph. The proposed (and now-disproved) absolute-value estimate had the form
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

The left side of (3.1) is an absolute-value majorant, and the two-link counterexample shows that it cannot be controlled by a multiplicity-uniform exponential coefficient. A viable replacement must preserve cancellations in (1.2), rather than bound every partition separately. The crude observation that each connected union contains some spanning tree does not suffice.

The exact factorization by support type in the repeated-insertion audit is compatible with (1.2), but does not prove (3.1). Nor does pairwise block HGR tensorization: the three-way hyperedge counterexample in the companion audit shows that pairwise subjective-HGR control cannot replace the missing higher-order estimate.

## 5. Proof ledger

Established:
- the occurrence-level Leonov–Shiryaev identity (1.1);
- vanishing of mixed-link cumulant blocks by independence;
- the monochromatic-link representation (1.2);
- the fact that local temporal trees, if inserted, form a connected row multigraph supported on common-link edges.

Still open:
- a signed/canceling replacement for (3.1); the absolute-value version (3.1) is disproved by the two-link counterexample;
- the sparse support-overlap case with unrestricted repeated labels;
- KP convergence, interacting-vacuum Poincaré, physical scale setting, and the continuum mass gap.

No proof gate is promoted by this reduction.
