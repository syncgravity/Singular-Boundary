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

## 3. Repetition compression: the next reduced lemma

For a Feynman–Kac tuple, let (\mathscr S) be the set of distinct interaction support labels appearing among the (R) row occurrences. Group all occurrences with the same support label (S\in\mathscr S) into one support-type super-row. If (n_S) is its multiplicity, its contribution on a link (e\in S) is a bounded path functional
\[
G_{S,e}=\prod_{i:\,X_i=S} f_{i,e}(X_e(t_i)),
\qquad
\|G_{S,e}\|_\infty\le\prod_{i:\,X_i=S}\|f_{i,e}\|_\infty.
\tag{3.1}
\]
The original row monomials still factor over links after this grouping:
\[
\prod_{i:\,X_i=S}A_i
=\prod_{e\in S}G_{S,e}.
\tag{3.2}
\]
A link is now incident to at most the number of **distinct support types** containing it, which is bounded by the geometric inventory (at most 232 for the combined face/pair family). The multiplicity (n_S) is absorbed into the path functional (G_{S,e}), rather than counted as additional support-type incidence.

Applying the LS formula at the support-type level would therefore have a fixed local partition order (q_e\le232). The missing analytic input is no longer the one-time-slot cumulant estimate. It is the following block-functional estimate for a single link path.

For (q\le232), let (G_1,\ldots,G_q) be arbitrary bounded functions of finite (possibly interlaced and overlapping) time sets (S_1,\ldots,S_q) of one stationary link path. Prove
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
\tag{3.3}
\]
The constant may be extremely large because (q\le232) is fixed, but it must be independent of the number of time points in each (S_a), the time horizon, and the volume. A conditional-HGR/tensorization proof is a candidate: the bridge-Doeblin estimate controls two individual time coordinates conditioned on arbitrary other time coordinates; the needed extension is from coordinate pairs to the sigma-fields generated by the grouped time sets, followed by a connected-cumulant tree argument.

If (3.3) is proved, the support-type LS lift has only a fixed number of blocks per link. The total number of distinct support types is at most (R), and the number of links in their union is at most (8R). Thus all local partition and tree-choice multiplicities can be absorbed into (C^R), while each selected edge retains its actual shared link and its cross-time sum. This is a route to the unrestricted repeated-label Feynman–Kac tree bound. **Equation (3.3) is a precise open lemma, not a claimed result.**

## 3. What remains open

The complete-overlap argument does not handle a connected but non-complete support graph. The product-process temporal tree may use an edge between disjoint supports, while the desired tree must use only common-link edges. The bounded-incidence projective theorem handles such sparse support graphs, but its coefficient (C_{m,D}) requires the total slot multiplicity bound (1.1).

The all-orders Feynman–Kac problem therefore has a precise remaining gap:

- **Complete support-overlap graph:** support-restricted temporal tree established by product-semigroup tensorization, including arbitrarily repeated labels.
- **Sparse support-overlap graph with bounded total slot multiplicity per link:** support-restricted tree established by the projective LS theorem.
- **Sparse support-overlap graph with unrestricted repeated interaction labels:** still open. This is the regime needed for the unrestricted Feynman–Kac cumulant sum.

A viable next step is to group repeated support types while retaining their internal temporal tree, then prove a connected tree bound on the quotient support graph with constants depending on the number of distinct support types incident to each link, not on the number of repeated occurrences. The ordinary cross-split QF is not sufficient for that step by itself; it controls one cut but not an all-orders tree.

No marked-root sum, KP convergence, interacting-vacuum Poincaré inequality, physical scale-setting, or continuum mass gap is promoted. No P0–P5 gate is promoted.
