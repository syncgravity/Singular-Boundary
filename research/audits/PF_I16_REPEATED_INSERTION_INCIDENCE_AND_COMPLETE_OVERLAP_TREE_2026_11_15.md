# PF-I16 — Repeated-insertion incidence audit and complete-overlap temporal tree

**Date:** 2026-11-15  
**Status:** The bounded-incidence projective tree theorem is valid under its literal slot-multiplicity hypothesis. The quoted geometric value (D\le232) counts distinct face/pair support types, not repeated Feynman–Kac occurrences, and therefore does not yet give a uniform all-orders constant for the full expansion. A separate complete-overlap theorem closes the repeated-support case without any incidence cap.

## 1. The incidence distinction

The projective multi-time super-row theorem assumes, for the entire order-(r) family and counted with multiplicity,
\[
q_e=\#\{\text{one-time slots on link }e\}\le D
\quad\text{for every link }e.
\tag{1.1}
\]
The geometric inventory (8) face supports plus (224) adjacent-face-pair supports per link bounds the number of **distinct interaction support labels** incident to a link. It does not bound how often one of those labels occurs in an order-(r) Feynman–Kac tuple.

For example, repeat one fixed face insertion (v_f(t_i)) at (r) distinct row times. Each of its four boundary links occurs in at least (r) row slots:
\[
N=4r,\qquad q_e=r\quad(e\in\partial f).
\tag{1.2}
\]
Thus for (r>232), the literal hypothesis (q_e\le232) fails. Repeating a fixed face-pair insertion similarly makes the incidence of each of its shared links grow linearly in (r). The geometric count (D\le232) is therefore not, by itself, an all-orders multiplicity bound.

This does **not** invalidate the conditional projective theorem (Section 3 of its companion audit). It restricts its direct application to families satisfying (1.1), for example tuples with bounded repetition. The statement that the same (D\le232) applies uniformly to unrestricted Feynman–Kac tuples must not be used until repeated occurrences have been separately resummed or compressed.

## 2. Complete-overlap theorem: no incidence cap is needed

Let (E_0) be any finite set of links, and let
\[
Z_t=(X_e(t))_{e\in E_0}
\]
be the product of independent stationary link Markov processes. Suppose each link semigroup satisfies
\[
\|P_t^e-\Pi_e\|_{L^2_0\to L^2_0}\le e^{-\Delta_0t}.
\tag{2.1}
\]
Then the product semigroup (P_t^{E_0}=\bigotimes_{e\in E_0}P_t^e) satisfies the same gap:
\[
\boxed{
\|P_t^{E_0}-\Pi_{E_0}\|_{L^2_0(\otimes_e\mu_e)\to L^2_0(\otimes_e\mu_e)}
\le e^{-\Delta_0t}.
}
\tag{2.2}
\]

**Proof.** Decompose the product (L^2) space orthogonally into tensor sectors indexed by subsets (S\subseteq E_0): coordinates in (S) are mean-zero and coordinates outside (S) are constant. The global mean-zero subspace is the orthogonal sum over nonempty (S). On the (S)-sector, the tensor semigroup norm is at most
\[
\prod_{e\in S}e^{-\Delta_0t}\le e^{-\Delta_0t},
\]
because every nonempty sector has at least one factor and (e^{-\Delta_0t}\le1). Taking the supremum over nonempty sectors proves (2.2). No reversibility or finite-state assumption is needed.

Now suppose every row observable (F_i) is supported in the same common link set (E_0) (the functions may differ and the times may be arbitrary):
\[
A_i(t_i)=F_i(Z_{t_i}),\qquad i=1,\ldots,r.
\]
The one-link cyclic temporal-tree theorem applies to the product process (Z_t), using (2.2). Hence
\[
\boxed{
|\kappa(A_1(t_1),\ldots,A_r(t_r))|
\le2^{r-2}\prod_i\|F_i\|_\infty
\sum_{T\in\mathcal T_r}
\prod_{\{i,j\}\in E(T)}
e^{-\Delta_0|t_i-t_j|}.
}
\tag{2.3}
\]
Since all row supports are the same, their support-overlap graph is complete. Thus (2.3) is exactly the desired support-restricted tree-sum estimate for this family, with no per-link slot-incidence cap and no projective representation.

More generally, the same conclusion holds whenever the row support-overlap graph is complete: take (E_0=\bigcup_iX_i), regard each (F_i) as a bounded function on the full product state (ignoring unused coordinates), and apply the product-semigroup gap. The target graph is then (K_r).

## 3. Repeated-support moment compression: exact identity and remaining step

Write (I_S=\{i:X_i=S\}) for the occurrence set of a distinct interaction support type (S). Fix one monomial term in each projective row expansion, so that
\[
A_i(t_i)=\prod_{e\in X_i}f_{i,e}(X_e(t_i)).
\]
For each link (e), support type (S\ni e), and row subset (B\subseteq[R]), define
\[
G_{S,e}(B)=\prod_{i\in B\cap I_S}f_{i,e}(X_e(t_i)).
\tag{3.1}
\]
This is a bounded path functional on the single link path (X_e(\cdot)), and its norm is at most the product of the corresponding one-time sup norms.

For every row subset (B\subseteq[R]), independence of link paths gives the exact raw-moment factorization
\[
\boxed{
m(B):=\mathbb E\prod_{i\in B}A_i(t_i)
=\prod_e\mathbb E_e\prod_{S:\,e\in S}G_{S,e}(B).
}
\tag{3.2}
\]
The number of distinct support types (S) incident to a given link is bounded by the geometric inventory (at most 232 for the combined face/pair family), even though the occurrence sets (I_S) can be arbitrarily large. Thus each **link factor in each raw moment** is a product of at most 232 path-block functions, one per distinct support type.

This is a genuine compression of the local factor arity, but it is not yet a compression of the cumulant arguments. The original cumulant remains
\[
\boxed{
\kappa(A_1,\ldots,A_R)
=\sum_{\pi\in\Pi([R])}
(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{B\in\pi}m(B).
}
\tag{3.3}
\]
One cannot replace all occurrences of a support type by their product and take a cumulant of the resulting support-type super-rows; cumulants are not invariant under that grouping. Any valid repetition compression must preserve the full partition sum (3.3).

### Reduced one-link block-functional estimate

A useful local input would be the following. For (q\le232), let (G_1,\ldots,G_q) be bounded functions of finite (possibly interlaced and overlapping) time sets (S_1,\ldots,S_q) of one stationary link path. Prove
\[
\boxed{
|\kappa(G_1,\ldots,G_q)|
\le C_{232}\prod_{a=1}^q\|G_a\|_\infty
\sum_{T\in\mathcal T_q}
\prod_{\{a,b\}\in E(T)}
\left(
\sum_{s\in S_a,\,t\in S_b}
e^{-\Delta_0|s-t|}
\right).
}
\tag{3.4}
\]
The constant must be independent of the number of time points in each (S_a), the time horizon, and the volume. A conditional-HGR/tensorization proof is a candidate: the bridge-Doeblin estimate controls two individual time coordinates conditioned on arbitrary other time coordinates; the needed extension is to the sigma-fields generated by grouped time sets, followed by an all-orders connected-cumulant tree argument.

There is a precise tensorization theorem for the pairwise block step. Let
\[
\eta_{ab}:=
\min\left\{1,
\left\|\left(e^{-\Delta_0|s-t|}\right)_{s\in S_a,t\in S_b}
\right\|_{\ell^2(S_b)\to\ell^2(S_a)}
\right\}.
\tag{3.5}
\]
The compact-group bridge-Doeblin estimate supplies the subjective one-coordinate bound
\[
\rho_{\rm subj}(X_e(s),X_e(t)\mid\mathcal H)
\le C_0e^{-\Delta_0|s-t|}
\]
uniformly over finite conditioning sets of other time coordinates. Peyre's N-against-M maximal-correlation tensorization theorem (Theorem 3.3.1) then bounds the maximal correlation between the two block sigma-fields generated by (S_a) and (S_b), seen from the sigma-metalgebra of all their time coordinates, by the operator norm of the matrix of these pairwise subjective coefficients. In particular, up to the fixed (C_0) factor,
\[
\rho_{\rm subj}\bigl(\sigma(X_e(s):s\in S_a),\sigma(X_e(t):t\in S_b)\bigr)
\le\eta_{ab}
\le C_0\sum_{s\in S_a,t\in S_b}e^{-\Delta_0|s-t|}.
\tag{3.6}
\]
This step is a tensorization of *pairwise* conditional HGR; it is not yet a cumulant-tree theorem.

Even (3.4) is not alone sufficient. A second, **clustered partition-lattice lemma** is required: insert the exact moments (3.2) into (3.3), resum the Möbius coefficients across repeated occurrences before taking absolute values, and show that the result is a decorated tree on the original (R) occurrences. The tree must have:
- internal temporal edges joining occurrences of the same support type, with their weights retained;
- external edges joining distinct support types only when they share a link, with cross-time weights from (3.4);
- a total coefficient at most (C^R), where (C) depends on the fixed distinct-support incidence bound 232 but not on the multiplicities (|I_S|).

The exact moment identity (3.2) identifies the finite local arity; (3.4) is the proposed analytic input; the clustered partition-lattice lemma is the remaining combinatorial cancellation. Neither (3.4) nor that lemma is claimed here.

## 3. What remains open

The complete-overlap argument does not handle a connected but non-complete support graph. The product-process temporal tree may use an edge between disjoint supports, while the desired tree must use only common-link edges. The bounded-incidence projective theorem handles such sparse support graphs, but its coefficient (C_{m,D}) requires the total slot multiplicity bound (1.1).

The all-orders Feynman–Kac problem therefore has a precise remaining gap:

- **Complete support-overlap graph:** support-restricted temporal tree established by product-semigroup tensorization, including arbitrarily repeated labels.
- **Sparse support-overlap graph with bounded total slot multiplicity per link:** support-restricted tree established by the projective LS theorem.
- **Sparse support-overlap graph with unrestricted repeated interaction labels:** still open. This is the regime needed for the unrestricted Feynman–Kac cumulant sum.

A viable next step is to exploit the exact moment factorization (3.2) inside the full partition sum (3.3), proving the one-link block-functional estimate (3.4) and a clustered partition-lattice resummation. This must retain the original occurrence labels; simply replacing repeated rows by their product is invalid. The ordinary cross-split QF is not sufficient for that step by itself; it controls one cut but not an all-orders tree.

No marked-root sum, KP convergence, interacting-vacuum Poincaré inequality, physical scale-setting, or continuum mass gap is promoted. No P0–P5 gate is promoted.
