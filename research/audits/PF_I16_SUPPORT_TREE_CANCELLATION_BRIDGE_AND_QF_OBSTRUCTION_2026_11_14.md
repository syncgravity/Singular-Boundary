# PF-I16 — Support-tree cancellation bridge: what QF does and does not supply

**Date:** 2026-11-14  
**Status:** the support-temporal tree extraction and its normalized time integral are established termwise. The remaining issue is the coefficient after summing the signed slot partitions. This audit rules out one tempting shortcut: cross-split QF alone does not imply a product-over-edges support-tree cumulant bound. The independent-link Markov structure must enter more deeply.

## 1. The already established support-temporal structure

For product insertions
\[
A_i(t_i)=\prod_{e\in X_i}Y_{i,e}(t_i),
\]
the Leonov–Shiryaev expansion is indexed by linkwise partitions \(\pi_e\) whose block hyperedges connect the row set. Replacing each non-singleton block by the path through its rows in chronological order gives a connected multigraph \(H_\pi\) contained in the support-overlap graph \(G_X\). The product of one-link temporal decay factors is
\[
\prod_e\prod_{B\in\pi_e,\ |B|\ge2}
e^{-\Delta_0\operatorname{span}(B)}
=
\prod_{\{i,j\}\in E(H_\pi)_{\rm mult}}
e^{-\Delta_0|t_i-t_j|}.
\]
Selecting a spanning tree \(T_\pi\subset H_\pi\) gives
\[
\text{termwise temporal weight}
\le
\mathcal M(G_X;\mathbf t)
:=
\max_{T\in\mathcal T(G_X)}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}.
\]
The normalized time integral is already controlled:
\[
\frac1{r!\mathcal T}\int_{[0,\mathcal T]^r}
\mathcal M(G_X;\mathbf t)\,d\mathbf t
\le
e^r\left(\frac2{\Delta_0}\right)^{r-1}.
\]
Thus the temporal geometry and its integration are not the outstanding issue.

## 2. Why cross-split QF alone cannot close the tree coefficient

The established arbitrary-local-observable QF estimate controls one cut:
\[
|\operatorname{Cov}(\prod_{i\in J}A_i,\prod_{j\in K}A_j)|
\le C_r\prod_i\|A_i\|_\infty
\sum_{i\in J,j\in K}w_{ij},
\quad
w_{ij}=\mathbf1_{\{X_i\cap X_j\ne\varnothing\}}
e^{-\Delta_0|t_i-t_j|}.
\]
It is tempting to iterate this estimate and infer a cumulant bound proportional to a product of \(r-1\) edge weights. That inference is invalid without additional structure.

Here is an exact finite-dimensional obstruction to the implication from cut-QF alone. Let \(Z_1,\ldots,Z_r\in\{-1,+1\}\) have joint law
\[
\mathbb P_\varepsilon(Z=z)
=2^{-r}\left(1+\varepsilon\prod_{i=1}^r z_i\right),
\qquad 0<\varepsilon\le1.
\]
Every proper subcollection is independent and uniform. For every nontrivial split \(J\sqcup K=[r]\), the maximal covariance between bounded functions of \(Z_J\) and bounded functions of \(Z_K\) is at most \(\varepsilon\), and it equals \(\varepsilon\) for the parity functions
\[
U_J=\prod_{i\in J}Z_i,\qquad U_K=\prod_{j\in K}Z_j.
\]
But the full joint cumulant is
\[
\kappa(Z_1,\ldots,Z_r)=\mathbb E\prod_{i=1}^rZ_i=\varepsilon,
\]
because every proper mixed moment vanishes. If all cut weights are set to \(w_{ij}=\varepsilon\) on a connected graph, every cut-QF inequality holds with a constant of order one (each cut has at least one edge), whereas every spanning-tree product is \(\varepsilon^{r-1}\). Therefore no order-uniform implication
\[
\text{cut-QF}\Longrightarrow
|\kappa(Z_1,\ldots,Z_r)|
\le C^r\max_T\prod_{ij\in T}w_{ij}
\]
can hold for arbitrary joint laws.

This example is **not** a counterexample to the PF-I16 independent-link Markov model: its coordinates have a global parity interaction and are not independent base processes. It proves only that the QF estimate, viewed as an abstract cut inequality, is insufficient to perform the desired resummation.

## 3. What extra structure is available in PF-I16

The reference law is a product of independent link path laws, and each row depends on at most eight link coordinates. The useful structure is stronger than QF:

1. The global semigroup tensorizes link by link.
2. For each time gap, the product semigroup has the exact coordinate expansion
   \[
   \bigotimes_e(\Pi_e+Q^e_g)
   =
   \sum_{S\subseteq E}
   \left(\bigotimes_{e\in S}Q^e_g\right)
   \otimes
   \left(\bigotimes_{e\notin S}\Pi_e\right).
   \]
3. A nonzero term must respect which row observables actually depend on each coordinate.
4. For a fixed coordinate, the surviving Q intervals form the one-link interval forests already used in the support-temporal extraction.
5. The row-incidence bound \(\sum_e|I_e|\le8r\) limits the total number of coordinate slots, even though a single link may occur in many rows.

The next proof must retain the coordinate label through the projection expansion and perform the signed Möbius/port-completion resummation before discarding it. A global projection-tree bound forgets the coordinate label and returns trees on the complete graph. A termwise slot bound retains the label but pays the Bell-partition fiber. The general target should be a sum over support trees, not the maximum of one tree: the stronger $C^r$-times-maximum-tree target is impossible for arbitrary bounded local observables by the one-link Haar-Rademacher counterexample in [the maximum-tree obstruction audit](PF_I16_SUPPORT_TREE_MAXIMUM_BOUND_OBSTRUCTION_2026_11_14.md). The actual face/pair subclass remains a separate, undecided question.

## 4. A precise next lemma — revised to retain the support-tree sum

Let \(\mathscr F=(F_e)_e\) be a tuple of linkwise interval forests arising in the coordinate-resolved \(\Pi+Q\) expansion, with each row incident to at most eight link coordinates. Let \(\alpha(\mathscr F)\) be the **signed coefficient after all global moment-cumulant Möbius cancellations**, not the product of absolute one-link cumulant bounds. The desired estimate is
\[
\sum_{\substack{\mathscr F:\ H(\mathscr F)\ {\rm connected}\\
                 \text{fixed support-temporal tree profile}}}
|\alpha(\mathscr F)|
\le C_{\rm slot}^{\,r}
N_{G_X}(\text{profile}),
\]
where \(N_{G_X}\) counts support-overlap spanning trees with that temporal cut profile.

The parity example shows why the cut-QF inequality cannot replace this coefficient calculation. The Bell\((r)^7\) example shows why selecting a canonical tree and taking absolute values before the signed resummation cannot prove it. The coordinate-resolved product-semigroup expansion is the remaining plausible route because it preserves exactly the information lost by each shortcut.

## 5. Gate disposition

- Actual-insertion cross-split QF: **ESTABLISHED** under independent stationary link paths and the uniform one-link \(L^2\) gap.
- Termwise support-temporal spanning-tree extraction: **ESTABLISHED**.
- Exponential normalized time integral of the support-tree maximum: **ESTABLISHED**.
- Global product-process temporal tree with all labeled trees: **ESTABLISHED**.
- Cut-QF alone implies an exponential support-tree cumulant bound: **REFUTED** by the parity construction.
- Coordinate-resolved, cancellation-preserving support-tree coefficient bound: **OPEN**.
- Marked-root spatial sum, quantum KP, interacting-vacuum Poincare inequality, and continuum mass gap: **OPEN**.

No P0–P5 status is promoted.
