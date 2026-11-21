# PF-I16: ordered reverse-mark templates for crossing fibers

Date: 2026-11-17

## Status

**Proved all orders.** This is a necessary-pattern lemma combining the first-overcrowded-cut localization with the corrected inverse-mark classification. It is not a capacity-one or Hall theorem.

## Setup

Let \(x=(M,\tau)\in X_k\), with \(k\ge5\) its first overcrowded odd cut. Let \(J=[a,b]\) be a non-root leaf interval of \(\tau\) crossing \(k\). By the crossing-localization lemma,
\[
a\in\{k-1,k\}.
\tag{1}
\]

Suppose \(T\in Y_k\) is a target obtained from this fiber by a valid guarded final switch at \(J\). Write the four local ports in increasing order as
\[
x_1<x_2<x_3<x_4.
\]
The reverse-mark classification says that \(J\) is one of the following five rank pairs:
\[
\boxed{(x_1,x_2),\ (x_1,x_3),\ (x_2,x_3),\ (x_2,x_4),\ (x_3,x_4).}
\tag{2}
\]
The pair \((x_1,x_4)\) is impossible.

## Proof of the five-pair list

For Type I adjacent endpoints:
- in the star centered at \(x_2\), the marked pair is \((x_1,x_2)\) or \((x_2,x_4)\);
- in the star centered at \(x_3\), it is \((x_1,x_3)\) or \((x_3,x_4)\);
- in the increasing path \(x_1-x_2-x_3-x_4\), it is the middle pair \((x_2,x_3)\).

For Type II distance-two endpoints, the two permitted mirror orientations give \((x_1,x_3)\) and \((x_2,x_4)\). These add no new rank pairs. The distance-three leaf/leaf pattern is excluded because the old edge is already present in the local path.

This proves (2).

## Crossing specialization

Since \(a\) is the smaller endpoint of \(J\), (2) implies that \(a\) is one of \(x_1,x_2,x_3\). Combining this with (1), every valid crossing reverse mark in \(Y_k\) has one of these forms:

- lower endpoint \(k-1\), with local rank 1, 2, or 3;
- lower endpoint \(k\), with local rank 1, 2, or 3.

Thus the crossing contribution is not an arbitrary four-port configuration: it is supported on ten ordered endpoint/rank templates (five rank pairs for each of the two possible lower endpoints), with the additional order inequalities forced by the chosen pair.

More explicitly, if \(a=k-1\), the other three local ports are distributed among
\[
(-\infty,k-1),\quad(k-1,b),\quad(b,\infty)
\]
according to whether \(a\) has rank 1, 2, or 3; the same statement holds with \(k\) in place of \(k-1\). Since all ports are integers, these are finite order-position cases, not a bound on the number of possible choices of the other ports.

## What this eliminates, and what it does not

The local inverse has no hidden history multiplicity: for fixed \((T,J)\), the parent target is unique. Equations (1) and (2) therefore reduce crossing target collisions to collisions among the two lower-endpoint classes and the five local rank-pair templates.

However, this does **not** bound how many different values of the other three local ports can occur around one target, nor how their parent sources' canonical neighborhoods overlap. In particular, it does not prove
\[
\sum_{F:\,T\in N_k(F)}\delta(F)\le1,
\]
and it does not prove BQH by itself.

## Next exact test

The next useful finite diagnostic is to enumerate, for each target \(T\in Y_k\), all incident crossing fibers and label each incidence by:
1. lower endpoint class \(a=k-1\) or \(a=k\);
2. Type I star, Type I path, or Type II;
3. rank pair in (2);
4. inverse parent target \(P_J(T)\);
5. parent-source multiplicity \(\{p:P_J(T)\in C_{\rm can}(p)\}\).

The resulting incidence table can distinguish collisions caused by the two lower-endpoint classes from collisions within one local template. It is diagnostic only; an all-orders proof still requires a weighted expansion estimate for arbitrary mixed fiber families.
