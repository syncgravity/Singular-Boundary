# Exact-profile local-switch reduction: two-star transport (2026-11-16)

## Statement

Let M be a perfect matching on ordered ports 1,...,n, let H_M be its interval-overlap graph, and let tau be any spanning tree of H_M. Root tau at the unique interval containing port 1. The all-orders local-switch construction can be restricted to the two middle-centred stars at every insertion, with no increasing-path replacement.

For every source (M,tau), every parent-before-child order, every legal choice of an overlapping current tree edge, and every sequence of the two star replacements, the final port tree T satisfies the exact identity

\[
\boxed{c(T)=m(M).}
\]

This is stronger than the previously established coordinatewise domination c(T)<=m(M).

## Proof of the local profile identity

Suppose the current tree edge is e=[u,w] and the newly inserted matching interval is J=[a,b]. The edge e is selected from a monotone parent-interval path and overlaps J. The four endpoints are distinct (matching endpoints are all distinct); write them in increasing order as x_1<x_2<x_3<x_4.

On the three cuts between consecutive x_i, the two intervals e and J have combined crossing loads (1,2,1), and their combined load is zero outside those cuts.

The two replacement stars are

\[
S_2=\{x_1x_2,x_2x_3,x_2x_4\},\qquad
S_3=\{x_1x_3,x_2x_3,x_3x_4\}.
\]

Directly counting edges crossing each of the three cuts gives (1,2,1) for each star, and zero outside. Thus replacing e by either star changes no cut-load coordinate relative to the current tree plus the newly inserted interval:
\[
c(T_{new})=c(T_{old})+\mathbf 1_J.
\]

The tree/path invariant from the all-orders local-switch construction is unchanged: deleting e splits the current tree, the three-edge star reconnects the two components and includes the two new endpoints of J, and the monotone paths can be updated along the unique star path. Induction over the s matching intervals, starting with the root interval, proves c(T)=sum_{I in M}1_I=m(M).

## Exact-class transport target

Let C_star(M,tau) be the set of distinct final port trees obtainable by all legal parent-before-child orders, all admissible overlapping-edge choices, and the two star replacements only. Then

\[
C_\star(M,\tau)\subseteq\{T:c(T)=m(M)\}.
\]

A uniform fractional transport on these sets would have column mass

\[
\sum_{(M,\tau):\ T\in C_\star(M,\tau)}
\frac{1}{|C_\star(M,\tau)|}.
\]

If this is at most one for every T, it proves the pointwise exact-class inequality L(h)<=Q(h) for every h, and hence all down-set Hall inequalities.

## Proof boundary

The exact-profile identity is an all-orders theorem. The column-mass bound for the star-only candidate relation has **not** been proved or verified here. In particular, the finite fractional certificate previously reported for the three-move relation (two stars plus the increasing path) does not automatically apply to this smaller star-only relation. This note records a valid reduction, not a proof of the weighted one-link inequality.
