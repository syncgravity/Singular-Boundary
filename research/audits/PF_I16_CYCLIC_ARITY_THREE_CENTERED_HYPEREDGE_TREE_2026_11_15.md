# PF-I16 — Centered hyperedge expansion and temporal trees for link arity at most three

**Date:** 2026-11-15  
**Status:** ESTABLISHED for finite independent-link systems in which every nontrivial link is incident to at most three distinct rows. This includes cyclic incidence hypergraphs, arbitrary overlap patterns, nonzero slot means, and parallel links. It gives an exponential-in-order support-restricted temporal-tree estimate and its normalized Feynman–Kac time-integrated form. Links incident to four or more rows remain outside the theorem.

## 1. Setup

Let (V=[R]), (R\ge2). For each independent link process e, let (I_e\subseteq V) be its row incidence, with (2\le |I_e|\le3). (A link incident to one row contributes only its mean to that row and may be removed.) Write
[
Y_{e,i}=f_{e,i}(X_e(t_i)),qquad
A_i=\prod_{e:\,i\in I_e}Y_{e,i},qquad
|Y_{e,i}|\le M_{e,i}.
\tag{1.1}
]
Link processes are independent across e, with arbitrary joint laws among the at most three slots on one link.

Set
[
\mu_{e,i}=\mathbb E Y_{e,i},\qquad Z_{e,i}=Y_{e,i}-\mu_{e,i}.
\tag{1.2}
]
For every subset (S\subseteq I_e) of size 2 or 3, define the centered link activity
[
c_e(S)=\mathbb E_e\prod_{i\in S}Z_{e,i}.
\tag{1.3}
]

## 2. Exact connected active-hyperedge identity

For a choice (mathbf S=(S_e)_{e\in E}), with
[
S_e\in\{\varnothing\}\cup\{S\subseteq I_e:|S|\in\{2,3\}},
]
let (H(mathbf S)) be the hypergraph on V whose nonempty hyperedges are the selected sets (S_e).

**Theorem.**
[
\boxed{
\kappa(A_1,\ldots,A_R)
=
\sum_{\substack{\mathbf S:\,H(\mathbf S)\text{ connected and spanning}}}
\left(\prod_{e:S_e\ne\varnothing}c_e(S_e)\right)
\left(\prod_e\prod_{i\in I_e\setminus S_e}\mu_{e,i}\right).
}
\tag{2.1}
]
Here connected and spanning means that the selected pair/triple hyperedges connect all R row vertices.

**Proof.** Expand every slot as (Y_{e,i}=\mu_{e,i}+Z_{e,i}) and use multilinearity of the joint cumulant. A term is indexed by selected endpoint subsets (S_e\subseteq I_e); its scalar coefficient is the product of means at omitted endpoints, and its row variables are
[
B_i=\prod_{e:\,i\in S_e}Z_{e,i}.
]
If (|S_e|=1), the centered slot from e occurs in exactly one row variable and is independent of every other link process. Every moment of any block containing that row therefore vanishes, so the cumulant term is zero. If a row belongs to no selected set, its B_i is the constant 1 and the cumulant is zero.

It remains that every selected S_e has size two or three and the selected hypergraph spans V. If it is disconnected, the row variables split into independent components, so their joint cumulant vanishes.

Suppose H(mathbf S) is connected and spanning. Use the moment-partition formula for (kappa(B_1,\ldots,B_R)). Consider any partition (pi) of V with at least two blocks. Connectivity implies that some selected hyperedge S_e meets at least two blocks. Since (|S_e|\in\{2,3\}), at least one block meets S_e in exactly one vertex. The moment for that block contains exactly one centered variable from link e; independence across links factors out its zero mean. Hence that partition term vanishes. The only surviving partition is the one-block partition, so
[
\kappa(B_1,\ldots,B_R)
=\mathbb E\prod_{i\in V}B_i
=\prod_{e:S_e\ne\varnothing}c_e(S_e),
]
where the last equality is independence of the link processes. Restoring omitted endpoint means and summing proves (2.1). \(\square\)

The essential combinatorial fact is specific to arity at most three: every nontrivial split of a selected pair or triple has a singleton intersection in at least one block. For a four-row hyperedge, a 2+2 split has no singleton, so this proof does not extend.

## 3. Support-restricted temporal-tree estimate

Assume each link is a stationary reversible Markov process with (L^2) gap at least (Delta_0>0). For a selected pair S={i,j},
[
|c_e(S)|\le4M_{e,i}M_{e,j}e^{-\Delta_0|t_i-t_j|}.
\tag{3.1}
]
For a selected triple S={i,j,k}, centering makes (c_e(S)) its third joint cumulant. The one-link temporal-tree estimate gives
[
|c_e(S)|
\le16M_{e,i}M_{e,j}M_{e,k}
\sum_{T\in\mathcal T(S)}
\prod_{\{a,b\}\in T}e^{-\Delta_0|t_a-t_b|}.
\tag{3.2}
]
The constants are explicit: (|Z_{e,i}|_\infty\le2M_{e,i}), the order-three cumulant coefficient is (2^{3-2}=2), and there are three spanning trees on a triple.

Let (G_s) be the simple row support graph joining any two rows that occur in a common original link support (I_e). For each connected selected configuration in (2.1), expand each triple bound (3.2) into its at most three local tree choices; pair activities contribute their unique edge. The union of these local trees is connected and spanning. Choose any spanning tree T from this union. Since every temporal edge weight is at most one, the product of all local tree weights is at most the product along T.

For each link with (|I_e|=2) there are two possible selected sets (empty or the pair); for (|I_e|=3) there are five (empty, three pairs, or the triple). Thus there are at most (5^{|E|}) selected configurations, and at most (3^{|E|}) local tree-choice combinations per configuration. The local cumulant constants are bounded by (16^{|E|}). Consequently,
[
\boxed{
|\kappa(A_1,\ldots,A_R)|
\le
240^{|E|}
\left(\prod_{e\in E}\prod_{i\in I_e}M_{e,i}\right)
\sum_{T\in\mathcal T(G_s)}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}.
}
\tag{3.3}
]
If every row has at most m incident link slots, then (2|E|\le\sum_e|I_e|\le mR), so
[
240^{|E|}\le(240^{m/2})^R.
\tag{3.4}
]
The coefficient is therefore exponential in row order, with no per-link multiplicity cap beyond the structural arity bound (|I_e|\le3).

## 4. Feynman–Kac time-integrated consequence

For every fixed row tree T,
[
\int_{[0,\mathcal T]^R}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}\,dmathbf t
\le\mathcal T(2/\Delta_0)^{R-1},
]
by successive leaf integration. Since (|\mathcal T(G_s)|\le R^{R-2}) and (R!\ge(R/e)^R), (3.3) implies
[
\frac1{R!}\int_{[0,\mathcal T]^R}
|\kappa(A_1(t_1),\ldots,A_R(t_R))|\,d\mathbf t
\le
\mathcal T\,C_{m,\Delta_0}^{R}
\prod_{e,i\in I_e}\|f_{e,i}\|_\infty,
\tag{4.1}
]
for example with (C_{m,\Delta_0}=240^{m/2}e\max(1,2/\Delta_0)). This is normalized time-integrated control for the arity-at-most-three class.

## 5. Scope and next obstruction

- Arbitrary connected cyclic pair/triple incidence hypergraphs: **ESTABLISHED**.
- Parallel pair/triple link labels: **ESTABLISHED**.
- Nonzero slot means: **ESTABLISHED** by (2.1).
- Temporal decay: pair activities use only the spectral-gap covariance estimate; triple activities use the one-link order-three temporal cumulant estimate.
- Row incidence bounded by m: yields the exponential coefficient (3.4).
- Links incident to four or more rows: **OPEN**. A selected four-slot centered link can split 2+2 across blocks without creating a singleton, so the moment-partition cancellation argument no longer applies.
- Unrestricted repeated multi-row support labels, the general cyclic hypergraph case with arity at least four, KP convergence, interacting-vacuum Poincaré, physical scale setting, and the continuum mass gap remain open.

The companion verifier checks the exact algebraic identity (2.1) with rational finite pair/triple laws over cyclic, overlapping, branching, and parallel hypergraphs. It does not verify the temporal semigroup estimates, which follow from the stated gap and one-link order-three theorem. No P0–P5 gate is promoted.
