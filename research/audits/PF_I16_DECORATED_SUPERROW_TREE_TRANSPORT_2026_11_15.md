# PF-I16 — Decorated-tree transport through recursive super-row elimination

**Date:** 2026-11-15  
**Status:** The decorated connectivity step is ESTABLISHED as a combinatorial lemma once internal trees are carried in a weighted projective expansion. The unweighted projective norm in the preceding multi-time super-row audit does not, by itself, record those internal temporal bonds; the recursive-lift sentence there must be read with the decoration below. This audit supplies the missing bookkeeping and a finite regression. It does not improve the numerical KP constant or close the continuum mass gap.

## 1. The bookkeeping gap

The projective monomial theorem bounds a cumulant of current rows by a tree on those current-row labels. In a recursive conditional-cumulant argument, however, a current super-row can represent a cluster of original insertion labels. A tree on the super-row labels is not yet a tree on the original labels unless each super-row carries its previously generated internal tree.

The ordinary projective norm
\[
\mathfrak p(F_C)=\int \prod_{\alpha\in S_C(\omega)}
\|f_{C,\alpha,\omega}\|_\infty\,d|\nu_C|(\omega)
\]
does not encode the temporal weights of such an internal tree. Therefore the last paragraph of Section 4 of the companion audit cannot be justified by that norm alone. The correct object is a *decorated projective expansion*.

## 2. Decorated projective rows

Let the original insertion labels be \(L=[R]\). At an intermediate stage let
\(\mathcal C=\{C_1,\ldots,C_k\}\) be a partition of \(L\) into current clusters. A term in the expansion of the current super-row indexed by \(C_a\) consists of:

1. a monomial in one-time link factors
\[
M_a(\omega)=\prod_{\alpha\in S_a(\omega)}
f_{a,\alpha,\omega}(X_{e(a,\alpha)}(s_{a,\alpha})),
\]
with every slot tagged by its original label \(\ell(\alpha)\in C_a\); and
2. a tree \(\tau_a\) on the original labels in \(C_a\), whose edges each retain the original common-link port pair that generated that edge.

Write
\[
w(u,v)=e^{-\Delta_0|s_u-s_v|}\in[0,1]
\]
for the weight of a tagged original port pair. Define the decorated projective norm
\[
\mathfrak p_{\rm dec}(F_{C_a})
:=
\int
\left(\prod_{\alpha\in S_a(\omega)}
\|f_{a,\alpha,\omega}\|_\infty\right)
\left(\prod_{\{u,v\}\in E(\tau_a(\omega))}
w(u,v)\right)
d|\nu_a|(\omega).
\tag{2.1}
\]
The tree is empty for a singleton cluster, so initially
\(\mathfrak p_{\rm dec}(F_{\{i\}})=\mathfrak p(F_i)\).
The slot budgets are measured on original labels:
\[
N=\sum_a |S_a|\le mR,\qquad
q_e=|\{\alpha:e(a,\alpha)=e\}|\le D.
\tag{2.2}
\]

## 3. Decorated LS tree lemma

**Lemma.** Suppose each current cluster \(C_a\) has a decorated projective expansion as above, and (2.2) holds uniformly on its expansion support. Then, under the one-link cumulant estimate (2.6) of the companion audit,
\[
\boxed{
|\kappa(F_{C_1},\ldots,F_{C_k})|
\le C_{m,D}^{R}
\left(\prod_{a=1}^k\mathfrak p_{\rm dec}(F_{C_a})\right)
\sum_{T\in\mathcal T_{\rm orig}}
\prod_{\{u,v\}\in T}w(u,v),
}
\tag{3.1}
\]
where \(C_{m,D}=(K_D^*)^m\), and \(\mathcal T_{\rm orig}\) is the set of spanning trees on \(L\) whose edges are tagged by an original common-link port pair. If no such tree exists, the sum is zero.

**Proof.** First fix one monomial/decorated term from each projective expansion. Apply the Leonov–Shiryaev formula to the current monomial rows. Every nonzero slot partition \(\pi\) satisfies the join condition with the partition of slots into current clusters. Each block of \(\pi\) lies on one link. For each block choose the chronological maximum-weight tree supplied by (2.6). The union of these slot trees, projected to current-cluster labels and with loops removed, is connected by the LS join condition.

A connected graph on the current clusters contains a spanning tree. Choose one. Every selected edge comes from two slots on a common link, and hence is tagged by their original labels \(u\in C_a\), \(v\in C_b\). Add these selected cross-cluster edges to the internal trees \(\tau_a\). The result is connected on all original labels. It has
\[
\sum_a(|C_a|-1)+(k-1)=R-1
\]
edges, so it is a spanning tree on \(L\).

All weights lie in \([0,1]\). Removing loops and unselected edges from the union of block trees can only increase the product. Thus the product of the block maximum-tree weights, multiplied by the internal decoration weights, is bounded by the weight of the constructed original spanning tree, and hence by the sum in (3.1).

Finally, the absolute LS partition coefficients factor by link. Dropping the global join restriction gives
\[
\sum_{\pi\ {\rm admissible}}\prod_{B\in\pi}b_{|B|}
\le\prod_e K_{q_e}
\le(K_D^*)^N\le C_{m,D}^{R}.
\]
Integrating the fixed-term estimate against the total-variation measures gives (3.1). \(\square\)

The key point is that the internal tree is part of the *termwise projective decoration*, not merely a property asserted after taking the ordinary projective norm.

## 4. Closure under one-link conditional-cumulant elimination

Suppose a selected link \(e\) is shared by current clusters \(C_a\). For a fixed choice of decorated monomial terms, the law of total cumulance partitions the incident current clusters into blocks \(B\). For each block, the conditional cumulant over the \(e\)-path is a cumulant of products of the \(e\)-slots carried by the clusters in \(B\), multiplied by all their other-link factors and their inherited scalar decorations.

Apply the LS product formula *inside this one-link cumulant*. Its join condition connects the current clusters in \(B\). The one-link estimate (2.6) supplies temporal trees on its slot blocks. Project their union to the current clusters, select a spanning tree on \(B\), and add the inherited internal trees of the clusters in \(B\). This gives a tree on \(\bigcup_{a\in B}C_a\), which is the decoration of the new conditional-cumulant super-row.

Singleton blocks add no new edge and retain their old decoration. Thus every branch of the conditional-cumulant expansion remains in the decorated class. The outer cumulant is then taken over these newly decorated super-rows and the nonincident rows.

For an explicit recursive coefficient, the law-of-total-cumulance partition at a link of incidence \(q\le D\) contributes at most \(\mathrm{Bell}(q)\) branches. The inner LS partition sum is bounded by \(K_q\). Since each original link is eliminated at most once and the number of links in the original support is at most \(mR\), the conservative recursive overhead is bounded by
\[
\left[
B_D^*\widehat K_D
\right]^{mR},
\qquad
B_D^*:=\max_{1\le q\le D}\mathrm{Bell}(q),
\quad
\widehat K_D:=\max_{1\le q\le D}K_q=D!.
\tag{4.1}
\]
This is finite and exponential in \(R\), but is generally much larger than the direct one-shot LS constant \(C_{m,D}^{R}\). The two maxima are kept separate because the number of current clusters incident to a link and the number of original time slots on that link need not be equal. The direct decorated LS lemma (3.1) does not pay the extra Bell factor; (4.1) is only a safe bound for the explicit recursive law-of-total-cumulance implementation.

The argument requires that each original insertion have at most \(m\) one-time link slots, that each link's total original slot incidence is at most \(D\), and that no recursion step duplicates or discards an original slot. These are exactly the port-conservation hypotheses; they must be checked for the chosen insertion inventory.

## 5. What is and is not certified

- The one-shot decorated LS tree lemma (3.1): **ESTABLISHED** under the one-link cumulant estimate and the stated decorated projective hypotheses.
- Connectivity of the union of internal cluster trees and the outer LS tree: **ESTABLISHED**; the edge count is exactly \(R-1\).
- Closure of the decorated class under a single conditional-cumulant elimination: **ESTABLISHED** at the termwise expansion level described in Section 4.
- A recursive coefficient bounded by (4.1): **ESTABLISHED**, but intentionally conservative and not numerically useful for KP at present.
- The unweighted norm \(\mathfrak p(F_C)\) alone does not carry internal temporal decay. Any use of the recursive lift must use \(\mathfrak p_{\rm dec}\), or an equivalent tree-labelled measure.
- Arbitrary bounded path-functionals without projective one-time-slot expansions remain outside this result.
- Marked-root summation, numerical KP convergence, interacting-vacuum Poincare inequality, physical scale-setting, and the continuum mass gap remain **OPEN**.

No P0–P5 gate is promoted.

## 6. Finite regression

The companion verifier enumerates small local set partitions, checks the LS join condition, projects chronological block trees to current clusters, and verifies that adjoining a spanning tree of cluster decorations produces a connected graph with exactly \(R-1\) edges on the original labels. This is a combinatorial regression only; it does not verify the analytic one-link cumulant estimate, projective expansion, or KP convergence.
