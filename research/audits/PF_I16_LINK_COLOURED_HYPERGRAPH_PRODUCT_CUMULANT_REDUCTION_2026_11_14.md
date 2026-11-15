# PF-I16 product cumulants: exact link-coloured hypergraph reduction

**Date:** 2026-11-14  
**Classification:** exact finite-order algebraic identity; no all-orders activity bound is claimed.

## 1. Purpose

The row-variable factorization in Section 16 of
\`PF_I16_JOINT_SPACETIME_CLUSTER_TREE_OPEN_GATE_2026_11_13.md\`
does not directly encode cumulants of product insertions: its first row derivative is a sum of link observables. The product-cumulant audit therefore leaves a genuine bridge prerequisite.

This note makes that bridge exact by rewriting the Leonov--Shiryaev product-cumulant formula as a **link-coloured connected-hypergraph sum**. It is an algebraic reformulation of the existing product formula, not a new bound. Its value is that it groups all elementary cumulant blocks by link before any absolute-value estimate and exposes the precise connectivity constraint.

## 2. Setup

Let the reference path law be a product over links. For \(r\) insertion rows, write
\[
A_i=\prod_{e\in X_i}Y_{i,e},\qquad i=1,\ldots,r,
\]
where \(Y_{i,e}=f_{i,e}(U_e(t_i))\) is a bounded observable of the path on link \(e\). Assume, as in the PF-I16 elementary-tensor setting, that a row contains at most one factor for each link. Define
\[
I_e=\{i:e\in X_i\},\qquad
\mathfrak I=\{(i,e):e\in X_i\}.
\]
For a finite set \(S\), let \(\Pi(S)\) denote its set partitions. Let
\(\kappa_e((Y_{i,e})_{i\in B})\) be the classical joint cumulant under the one-link path law.

## 3. Exact link-coloured hypergraph identity

For each link \(e\), choose a partition \(\rho_e\in\Pi(I_e)\). Regard every block \(B\in\rho_e\) as a hyperedge on the row-vertex set \([r]\), coloured by \(e\). Let
\[
\mathcal H(\boldsymbol\rho)
=\bigl([r],\{B:B\in\rho_e,\ e\}\bigr).
\]
Singleton blocks are allowed; they do not connect distinct rows.

Then
\[
\boxed{
\kappa(A_1,\ldots,A_r)
=
\sum_{\substack{\rho_e\in\Pi(I_e)\ \forall e\\
                 \mathcal H(\boldsymbol\rho)\ {\rm connected}}}
\ \prod_e\prod_{B\in\rho_e}
\kappa_e\bigl(Y_{i,e}:i\in B\bigr).
}
\tag{H}
\]

Here a one-vertex hypergraph is connected by convention.

### Proof

Apply the Leonov--Shiryaev product-cumulant identity to the slot family
\(\mathfrak I\), with row partition
\(\mathcal R=\{\{(i,e):e\in X_i\}:1\le i\le r\}\):
\[
\kappa(A_1,\ldots,A_r)
=
\sum_{\substack{\pi\in\Pi(\mathfrak I)\\
                 \pi\vee\mathcal R=\hat 1}}
\prod_{C\in\pi}\kappa(Y_{i,e}:(i,e)\in C).
\]
Independence of the link path processes implies that an elementary joint cumulant in a block \(C\) vanishes unless all slots in \(C\) have the same link colour. Thus every contributing \(\pi\) is uniquely a family of partitions \((\rho_e)_e\) of the link-incidence sets \(I_e\). The join condition \(\pi\vee\mathcal R=\hat1\) says exactly that the resulting link-coloured hypergraph connects all insertion rows. Substitution gives (H). \(\square\)

This is the missing algebraic bridge from elementary link cumulants to cumulants of the actual product insertions. It does **not** identify those cumulants with the square-free coefficient of the old row variables \(Y_i(z_i)\).

## 4. What the one-link estimate contributes

For every block \(B\) with \(|B|\ge2\), the established one-link estimate (12.8) gives
\[
|\kappa_e(Y_{i,e}:i\in B)|
\le (2e)^{|B|}|B|!\,
e^{-\Delta_0(\max_{i\in B}t_i-\min_{i\in B}t_i)}
\prod_{i\in B}\|f_{i,e}\|_\infty.
\tag{1}
\]
For singleton blocks the factor is the one-link mean and is bounded by
\(\|f_{i,e}\|_\infty\); no temporal decay is asserted for such a block.

For each non-singleton hyperedge \(B\), its temporal factor in (1) is exactly the maximum-spanning-tree product on the complete graph over \(B\), with edge weights \(e^{-\Delta_0|t_i-t_j|}\). A connected \(\mathcal H(\boldsymbol\rho)\) therefore contains a row-spanning tree assembled from edges inside its hyperedges. Consequently the product of all non-singleton temporal factors dominates at least one connected row-tree weight. This observation is useful, but it does not yet bound the **sum over link-coloured partitions** by one common maximum-tree weight with an exponential-in-\(r\) coefficient.

## 5. An eight-link witness: cancellation is indispensable

The connected-hypergraph form also gives a sharp warning against taking absolute values term by term. Let \(r=8\), let every row have the same support \(X_i=\{1,\ldots,8\}\), and let
\[
Y_{i,e}=U_e,\qquad e=1,\ldots,8,
\]
where the \(U_e\) are independent symmetric Rademacher variables at coincident times. Then every product row is the same Rademacher variable
\[
A_i=W:=\prod_{e=1}^8U_e.
\]
Consequently the exact product cumulant is
\[
\kappa(A_1,\ldots,A_8)=\kappa_8(W)=-272.
\]

For each link colour \(e\), restrict its partition \(\rho_e\) to perfect matchings of the eight row labels. There are \(7!!=105\) such matchings, and every pair-block weight is
\(\kappa(U_e,U_e)=1\). Choose two fixed alternating perfect matchings whose union is one cycle through all eight rows. The hypergraph is then connected regardless of the choices of the remaining six link matchings. This gives at least
\[
(7!!)^6=105^6=1{,}340{,}095{,}640{,}625
\]
distinct connected LS summands, each equal to \(+1\). Therefore the absolute sum of the LS/hypergraph summands is at least \(105^6\), although their signed total is only \(-272\).

This is an exact degree-eight-support cancellation witness. It proves that **no proof based on taking absolute values of the individual connected link-partition summands can deliver the desired \(C^r r!\) growth in general**. The cancellation must be retained across different link-coloured partition families (or encoded by another exact connected representation) before estimating. It does not show that the actual product cumulant is large; this example shows the opposite.

## 6. Exact special case: tree incidence with pairwise links

Suppose the row-overlap graph is a tree, every link belongs to exactly two rows, and each graph edge is represented by exactly one link. Suppose also that every elementary factor is centered under its one-link stationary law. Then \(I_e=\{i,j\}\) for each link, and its only partitions are \(\{\{i,j\}\}\) and \(\{\{i\},\{j\}\}\). The singleton option has zero weight by centering. The hypergraph is connected only if every tree edge contributes its pair block. Hence (H) reduces exactly to
\[
\boxed{
\kappa(A_1,\ldots,A_r)
=\prod_{e:\,I_e=\{i,j\}}
\kappa_e(Y_{i,e},Y_{j,e}).
}
\tag{2}
\]
The temporal decay and constants in this special case are inherited directly from the one-link covariance estimate, with no Bell-number or spanning-tree counting loss.

The hypotheses matter: a link shared by three or more rows creates higher-cardinality hyperedges, and multiple links shared by the same pair create parallel colours. Those are precisely the general cases not covered by (2).

## 7. The remaining combinatorial/analytic gate

Identity (H) makes the obstruction precise. The next target is not to count all partitions independently. It is to sum, **for each link as one object**, the family of its coloured blocks while retaining the global connectedness constraint. A successful estimate must:

1. preserve the cancellations inside each link's full partition sum before taking absolute values;
2. use \(\sum_e|I_e|=\sum_i|X_i|\le8r\), rather than a bound depending on the number of links or on \(\max_e|I_e|\);
3. retain a single maximum-tree temporal factor for the connected row hypergraph;
4. yield a coefficient \(C^r r!\), or a time-integrated substitute that becomes at most exponential after the Feynman--Kac \(1/r!\) normalization.

The raw absolute Leonov--Shiryaev majorant still fails this growth test. The identity (H) is an exact reduction and a useful special-case closure, not the required all-orders estimate. The joint space-time/KP gate remains **OPEN**.

## 8. Reproducibility

Run:
\`\`\`bash
python research/verification/verify_pf_i16_link_coloured_hypergraph.py
\`\`\`
The checker compares (H) with directly computed product-insertion cumulants in several exact finite Rademacher models, including a two-link covariance, three- and four-row support paths, a one-link three-row case, and the eight-link cancellation witness.
