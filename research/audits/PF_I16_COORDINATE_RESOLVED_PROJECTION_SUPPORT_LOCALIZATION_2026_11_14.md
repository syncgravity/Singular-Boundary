# PF-I16 — Coordinate-resolved projection intervals and support-edge localization

**Date:** 2026-11-14  
**Status:** coordinatewise interval localization is ESTABLISHED; cancellation-preserving support-tree coefficient bound remains OPEN  
**Scope:** finite link set, independent stationary link Markov semigroups with a uniform mean-zero L2 gap. No P0–P5 gate is promoted.

## 1. Purpose

The global product-process projection-tree estimate forgets which link carries each temporal contraction. The Leonov–Shiryaev expansion remembers link labels but loses cancellation when its slot partitions are bounded term by term. This audit isolates the exact operator-level localization available between those two descriptions.

Let
\[
\mathcal H=\bigotimes_{e\in E}L^2(\nu_e),\qquad
P_t=\bigotimes_{e\in E}P_t^e,\qquad
P_t^e=\Pi_e+Q_t^e,
\]
where \(Q_t^e\Pi_e=\Pi_eQ_t^e=0\), \(Q_s^eQ_t^e=Q_{s+t}^e\), and
\[
\|Q_t^e\|_{2\to2}\le e^{-\Delta_0t}.
\]
A row \(i\) is multiplication by a bounded local observable \(F_i\), supported on \(X_i\subseteq E\). Write \(M_i\) for this multiplication operator.

## 2. Tensor expansion of one global Q interval

For every \(t>0\),
\[
P_t-\Pi
=\sum_{\varnothing\ne S\subseteq E}
R_{S,t},\qquad
R_{S,t}=
\bigotimes_{e\in S}Q_t^e
\otimes\bigotimes_{e\notin S}\Pi_e,
\tag{2.1}
\]
where \(\Pi=\bigotimes_e\Pi_e\). Thus every global Q interval carries a nonempty set of active link coordinates.

Fix one coordinate \(e\) and an ordered-time operator word arising from the projection expansion. Mark each temporal gap on which the selected tensor term contains \(Q^e\). At a row \(i\) with \(e\notin X_i\), the coordinate-\(e\) part of \(M_i\) is the identity, so it commutes with \(Q^e\). Consecutive active gaps separated only by such rows therefore contract exactly:
\[
Q^e_{s_2-s_1}\,I\,Q^e_{s_3-s_2}
=Q^e_{s_3-s_1}.
\tag{2.2}
\]
A row in \(I_e:=\{i:e\in X_i\}\) is the only kind of row at which this contraction can be interrupted.

At the two ends of the stationary operator word, a run of active \(Q^e\)'s with no incident row at one endpoint vanishes, since
\[
Q_t^e\mathbf1=0,\qquad (Q_t^e)^*\mathbf1=0.
\tag{2.3}
\]
Consequently, after contracting across rows that do not use \(e\), every nonzero active coordinate run has endpoints among the \(e\)-incident rows. If it crosses no intervening \(e\)-incident row, it produces one factor
\[
Q^e_{|t_i-t_j|},\qquad i,j\in I_e.
\]
If it crosses intervening \(e\)-incident rows, it breaks into successive such intervals. In either case, every resulting temporal edge joins two rows sharing the link \(e\).

**Support-localization lemma.** Every nonzero coordinate-resolved projection word can be reduced, link by link, to temporal Q intervals whose endpoint pairs are edges of the support-overlap graph
\[
G_X:\quad \{i,j\}\in E(G_X)\iff X_i\cap X_j\ne\varnothing.
\tag{2.4}
\]
Each retained interval \((i,j)\) carries the contraction
\[
\|Q^e_{|t_i-t_j|}\|_{2\to2}
\le e^{-\Delta_0|t_i-t_j|}.
\tag{2.5}
\]

The statement is operator-level: it uses the fact that a row not involving \(e\) acts as the identity in coordinate \(e\). It does not assume a tensor-product factorization of the row observable across its incident links.

## 3. Connectedness and the support-tree weight

In the linkwise Leonov–Shiryaev formula, a summand is indexed by partitions \(\pi_e\) of the incident row set \(I_e\), subject to the connected-join condition. Replace every non-singleton block \(B\in\pi_e\) by its increasing temporal path through the rows of \(B\). Every edge of this path is supported by \(e\), and the union over all links is connected by the join condition.

Let \(H\) be this connected support multigraph, with one temporal edge for each retained local interval. Its contraction weight is
\[
W(H;\mathbf t)=
\prod_{\{i,j\}\in E(H)_{\rm mult}}
e^{-\Delta_0|t_i-t_j|}.
\]
For any spanning tree \(T\subseteq H\), all edge weights lie in \([0,1]\), hence
\[
W(H;\mathbf t)
\le
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}
\le
\sum_{T\in\mathcal T(G_X)}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}.
\tag{3.1}
\]
Thus the desired support-tree-sum weight is already the correct termwise temporal majorant once the linkwise connected structure has been retained.

This is consistent with the previously established support-temporal extraction audit. The new point here is the operator explanation for why a Q contraction can be localized to a shared-link pair: inactive coordinates commute through rows and telescope, while the stationary boundary kills runs with no incident endpoint.

## 4. The remaining coefficient problem is not solved by localization

Equation (3.1) bounds the temporal weight of an individual connected link-partition term. It does not bound the signed sum of all such terms.

For a fixed support tree \(T\), many different tuples \((\pi_e)_e\) can generate connected multigraphs containing \(T\). In the eight-identical-link incidence pattern, fixing one link to have its one-block partition leaves \(\mathrm{Bell}(r)^7\) arbitrary choices on the other seven links, all still satisfying the connected-join condition. Taking absolute values before summing the linkwise Möbius coefficients therefore gives a superexponential fiber.

The global projection-tree theorem avoids that fiber by summing the signed moment-cumulant coefficients first, but its port-completion injection does not retain the coordinate labels needed to ensure that every completed tree edge belongs to \(G_X\). Coordinate localization and global cancellation are both available; a proof that combines them with a controlled fiber is not yet available.

In particular, the following tempting inference is invalid:
\[
\text{each term has a support-tree weight}
\quad\Longrightarrow\quad
|\text{signed sum}|\le C^r\sum_{T\in\mathcal T(G_X)}W(T).
\]
The missing step is precisely the cancellation-preserving coefficient estimate.

## 5. Exact next lemma

A sufficient next result would be a **coordinate-preserving port-completion inequality**. Group the signed projection expansion by its link-labelled interval forest \(H\), and prove that its total absolute grouped coefficient assigned to any support tree \(T\) is at most
\[
C^{\,r+\sum_e |I_e|/r\cdot 0}
\]
with a universal \(C\); under the actual face/pair incidence constraint \(|X_i|\le8\), the target can equivalently be written \(C_8^r\). The notation emphasizes that the bound must not contain a Bell-number or \(r^{cr}\) fiber.

A successful construction must satisfy all three conditions:

1. **Coordinate preservation:** every final tree edge is witnessed by a common link of its endpoints.
2. **Cut-profile preservation:** the sum of temporal edge lengths is not increased, so the product of exponential contractions is not weakened.
3. **Controlled decoding:** the original signed interval data and its link labels can be recovered from the final tree plus at most \(C_8^r\) decorations.

The existing port-completion proof supplies conditions 2 and 3 after forgetting link labels; the support-localization lemma supplies condition 1 before completion. Their compatible combination is the outstanding combinatorial step.

## 6. Status

- Tensor decomposition (2.1): **ESTABLISHED**.
- Commutation/telescoping across rows outside a link support: **ESTABLISHED**.
- Localization of nonzero temporal Q intervals to shared-link row pairs: **ESTABLISHED**.
- Connected support-temporal termwise tree majorant: **ESTABLISHED**.
- Cancellation-preserving, coordinate-labelled coefficient bound by a support-tree sum: **OPEN**.
- Actual smooth face/pair specialization of the stronger single-maximum-tree bound: **UNDECIDED**.
- Marked-root spatial summation, quantum KP convergence, interacting-vacuum Poincare inequality, and continuum mass gap: **OPEN**.

No P0–P5 acceptance status is promoted.
