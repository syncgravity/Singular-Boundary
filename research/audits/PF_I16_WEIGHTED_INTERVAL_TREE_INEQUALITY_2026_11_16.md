# PF-I16 — Weighted interval-overlap tree inequality: one-link reduction

**Date:** 2026-11-16  
**Status:** exact reduction and finite rational regression established; general inequality remains a conjecture, not a theorem.

## 1. One-link reduction

Take ordered ports (1<\cdots<n) on one symmetric binary Markov link. Write the adjacent temporal factors
\[
x_k=e^{-\Delta_0(t_{k+1}-t_k)}\in(0,1],\qquad
r_{ij}=\prod_{k=i}^{j-1}x_k.
\]
For an even number (n=2s) of ports, a nonzero one-link matching family is a perfect matching (M). Associate to each pair ((a,b)\in M) the interval ([a,b]). Let (H_M) be the interval-overlap graph: its vertices are matched intervals, and two vertices are adjacent exactly when their interval interiors overlap. Only connected (H_M) contribute to the connected cumulant coefficient. Whitney's broken-circuit bound gives
\[
|[q]\chi_{H_M}(q)|\le\tau(H_M).
\]

The one-link weighted multiplicity problem is therefore implied by the stronger inequality
\[
\boxed{
\sum_{\substack{M\text{ perfect matching}\H_M\text{ connected}}}
\tau(H_M)\prod_{\{a,b\}\in M}r_{ab}
\;\le\;
\mathcal T_n(r):=
\sum_{T\in\mathcal T(K_n)}\prod_{\{i,j\}\in T}r_{ij}.
}
\tag{1.1}
\]
The right side is the weighted spanning-tree partition function of the complete support graph with the same temporal kernel. If true, (1.1) gives constant one at the level of the τ-majorant for a single link, substantially stronger than an exponential-in-(n) estimate.

## 2. Why the temporal tradeoff is plausible

For a connected interval family, the union of its intervals is itself an interval. If its hull is ([a,b]), then
\[
b-a\le\sum_{I\in M}|I|,
\qquad
\prod_{I\in M}r_I\le r_{ab}.
\]
Thus every connected matching family pays at least the temporal cost of spanning its full hull. This is the basic decay-versus-overlap tradeoff.

It is not by itself enough: the same hull path cannot encode the τ(H_M) different conflict spanning trees. The missing step is a multiplicity-sensitive *endpoint-tree expansion*: assign distinct support trees to the conflict trees while ensuring that the total additive support-tree cost does not exceed the sum of matched interval lengths. A natural local move is the crossing pattern
\[
a<c<b<d.
\]
The three-edge endpoint path (a-c-b-d) has total length (d-a\le(b-a)+(d-c)). This shows how an overlap can replace two crossing interval edges by a cheaper connected endpoint tree, but a global construction must coordinate these switches across all edges of a conflict tree without cycles or collisions.

## 3. Exact finite regression

Added verifier:
`research/verification/verify_pf_i16_weighted_interval_tree_inequality.py`.

It enumerates every perfect matching for (n=4,6,8,10), retains those with connected interval-overlap graph, computes τ(H_M) exactly, and compares the left side of (1.1) with the weighted complete-graph tree sum computed by an exact rational Matrix-Tree determinant. It checks four rational adjacent-gap profiles at each order (three homogeneous profiles and one inhomogeneous profile). All checks pass.

These tests support the conjecture but do not establish it for arbitrary gaps or order. The verifier intentionally uses τ(H_M), not the possibly smaller absolute chromatic coefficient, so it tests a stronger statement.

## 4. Bounded multi-link incidence: proposed lift, not yet proved

For rows (i=1,\ldots,R) with link supports (X_i) and (|X_i|\le m), each link (e) sees its own ordered port set (I_e=\{i:e\in X_i\}), matched intervals, and interval-overlap graph. A plausible route is:

1. Apply a one-link endpoint-tree expansion separately on each (I_e), preserving its temporal weights (r^e_{ij}).
2. Glue the resulting linkwise endpoint trees along shared row vertices. The union is connected precisely when the row-pair/conflict incidence structure is connected.
3. Extract a row support spanning tree. Since each row belongs to at most (m) link supports, charge any duplicated linkwise edge/cost to at most an (m)-dependent factor, rather than to the total number of links or ports.

The unresolved issue is step 2: linkwise endpoint trees must be selected *jointly* so that their union retains the quotient-tree labels needed for an injective or bounded-load encoding. Taking arbitrary linkwise trees and then deleting cycle edges proves per-configuration weight domination, but not a bound on the sum over all conflict-tree choices. The earlier unweighted quotient-tree injection does not solve this weighted compatibility problem.

## 5. Status

- Exact one-link interval-graph reduction: proved.
- Candidate inequality (1.1): conjectural.
- Finite exact rational checks through ten ports: pass.
- Bounded multi-link lift: proposed architecture only.
- Weighted multiplicity estimate (4.1), KP convergence, interacting-vacuum Poincaré inequality, physical scale setting, and Yang–Mills mass gap: open.

No proof closure or mass-gap conclusion is claimed.
