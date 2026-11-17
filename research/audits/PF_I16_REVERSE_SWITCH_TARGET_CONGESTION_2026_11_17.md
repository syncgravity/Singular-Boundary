# PF-I16: reverse-switch target congestion decomposition

Date: 2026-11-17

## 1. Unique inverse for a marked inserted interval

Let T be a port tree on [n], and let J={a,b} be the interval inserted in the final guarded switch. In each of the three local switch trees, every edge incident to a or b is local, and the union of the neighbors of a and b outside J is exactly the two endpoints u,v of the replaced parent edge.

Therefore, if T is a valid final-switch output marked by J, the pair {u,v} is uniquely recovered from T and J. The parent tree is uniquely

\[
P_J(T)=\bigl(T\setminus E(T[\{a,b,u,v\}])\bigr)\cup\{uv\},
\]

provided the induced four-vertex tree is one of the allowed local patterns and the no-reinsertion guard holds. Otherwise J is not a valid reverse mark for T.

Proof: the only edges of T incident to either newly inserted endpoint belong to the final local three-edge tree. The union of their external neighbors is exactly the old edge's two endpoints. The final switch changes no edge outside those four vertices. Replacing the induced local tree by uv therefore recovers the unique parent tree. This is the same inverse uniqueness used in the leaf-last verifier, now expressed as a target-side statement.

## 2. Exact factorization of target congestion

Write C_can(p) for the canonical leaf-last parent neighborhood of parent source p. For a fixed fiber F=(p,J), its target row is common to every child source in F. The reverse-switch uniqueness lemma gives the exact equivalence

\[
T\in N(F)\quad\Longleftrightarrow\quad
J\in\mathcal J(T),\quad P_J(T)\in C_{\rm can}(p),
\]

where \mathcal J(T) is the set of valid reverse marks J for T (with the cut-class restriction imposed separately).

Consequently, for any fiber-to-target charge lambda, the target load is exactly

\[
L(T)=\sum_{J\in\mathcal J(T)}
\sum_{p:\,P_J(T)\in C_{\rm can}(p)}
\lambda((p,J),T).
\tag{RC}
\]

This separates the collisions into two levels:

1. **Parent-source collisions at fixed J:** several parent sources p can have the same parent target P_J(T) in their canonical neighborhoods.
2. **Marked-interval collisions:** distinct intervals J can reverse T to distinct parent trees P_J(T).

There is no third source of multiplicity: for fixed (T,J), the parent target is unique. Thus all target congestion is visible in (RC), without enumerating switch histories.

## 3. A sufficient target-side congestion criterion

A recursive charge can be factored into a parent-source/marked-interval allocation alpha(p,J,P) and a final-lift kernel beta(p,J,P,T), supported only when P=P_J(T), with

\[
\sum_{P\in C_{\rm can}(p)}\alpha(p,J,P)=\delta(p,J),
\qquad
\sum_{T:\,P_J(T)=P}\beta(p,J,P,T)=1.
\]

Then

\[
\lambda((p,J),T)=\alpha(p,J,P_J(T))\,\beta(p,J,P_J(T),T),
\]

and (RC) becomes

\[
L(T)=\sum_{J\in\mathcal J(T)}
\sum_{p:\,P_J(T)\in C_{\rm can}(p)}
\alpha(p,J,P_J(T))\beta(p,J,P_J(T),T).
\]

A sufficient congestion theorem would bound the inner sum for each reverse mark J by a number rho(T,J) with

\[
\sum_{J\in\mathcal J(T)}\rho(T,J)\le1.
\tag{TC}
\]

This is a sharper target than bounding the number of histories: history multiplicity has already been quotiented out, and (TC) concerns only distinct marked-interval inverses.

## 4. Why inverse uniqueness alone does not close the estimate

The number of valid reverse marks is not bounded by a constant independent of n. For example, take a double-star tree with adjacent hubs u,v, with r leaves at u and q leaves at v. Every pair (a,b) with a a leaf at u and b a leaf at v gives a valid four-vertex path a-u-v-b, and hence a distinct possible marked interval J={a,b} at the level of the reverse local pattern. There are rq such pairs.

Thus the unique-inverse lemma removes ambiguity for fixed J but cannot by itself control the sum over J in (RC). A proof must use the matching/overlap-tree restrictions and the canonical parent-neighborhood condition to show that the corresponding alpha-beta contributions satisfy (TC). A bound based only on the degree or number of edges of T cannot suffice.

## 5. The precise remaining parent-collision estimate

For each parent source p and marked interval J, the split demand is

\[
\delta(p,J)=\sum_{v\in A(p,J)}\frac1{d_v},
\]

where A(p,J) is the set of parent overlap-tree vertices to which J can be attached and d_v is the number of non-root leaves in the resulting child overlap tree.

The reverse-switch reduction shows that the required target congestion estimate can be pursued in two stages:

- construct alpha distributing delta(p,J) over P in C_can(p);
- prove that after final-lift distribution beta, the sum in (RC) is at most one for every T.

The local same-cut theorem proves each fiber has at least 2^{s-2} outputs, but does not provide either the parent-source collision allocation alpha or the aggregate marked-interval estimate (TC).

## 6. Status

This is an exact structural reduction of target congestion to unique marked-interval inverses and a two-level allocation. It is not yet a proof of (TC), and no all-orders cross-fiber Hall theorem is claimed. The finite n=8 and n=10 max-flow certificates remain valid independent evidence.