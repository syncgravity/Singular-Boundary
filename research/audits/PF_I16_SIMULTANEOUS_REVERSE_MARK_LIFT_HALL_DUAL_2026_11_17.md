# PF-I16: simultaneous reverse-mark lift allocation and its Hall dual

Date: 2026-11-17

## 1. The lift kernel is a capacitated matching problem

Fix a parent allocation alpha(p,J,P) supported on P in C_can(p). For every row
r=(p,J,P), let L(r) be the set of distinct child target trees obtained by
the admissible final guarded switches from P with J inserted last. Define
a_r=alpha(p,J,P).

A final-lift kernel beta is exactly a nonnegative matrix z indexed by rows and
child targets, with
[
z_{r,T}=a_r\,\beta(r,T),
]
such that
[
\sum_{T\in L(r)}z_{r,T}=a_r
\quad\text{and}\quad
\sum_{r:T\in L(r)}z_{r,T}\le1.
\tag{1}
]
For a zero-demand row the corresponding variables are zero. For positive
demand, beta=z/a is a probability distribution over that row's lifts.

By the capacitated bipartite max-flow/min-cut theorem, such a kernel exists
if and only if
[
\boxed{
\sum_{r\in R}a_r
\le
\left|\bigcup_{r\in R}L(r)\right|
\quad\text{for every row subfamily }R.
}
\tag{2}
]
This is the exact dual condition. It is not a pointwise reverse-mark bound.

Proof: make a source-to-row edge of capacity a_r, row-to-each-lift-target
edges of infinite capacity, and target-to-sink edges of capacity one. A
finite cut indexed by R has capacity
\sum_{r\notin R}a_r+|N(R)|. It is at least total demand precisely when
(2) holds. Max-flow/min-cut proves necessity and sufficiency.

## 2. Why reciprocal mark-counting does not solve the problem

The tempting rule
[
\beta(r,T)=1/|L(r)|
]
normalizes each row, but the resulting target load is
[
L(T)=\sum_{r:T\in L(r)}a_r/|L(r)|.
]
There is no general reason for this sum to be at most one. Dividing instead by
the number of reverse marks of T would control columns, but would generally
make the row sums smaller than a_r, destroying conservation of demand.

Thus a valid rule must solve both constraints in (1) simultaneously.

## 3. Bridge classes expose, but do not remove, the high-multiplicity case

For a target tree T and an edge uv, let A_u and A_v be the leaf sets in the
two components of T-uv. Every pair (a,b) in A_u x A_v is a raw type-3
reverse-mark candidate, with local path a-u-v-b. This gives |A_u||A_v|
candidate marks for one bridge.

The correct aggregation is therefore not a bound on the number of marks.
It is a capacity inequality for the union of their *actual lift rows*:
[
\sum_{r\in R_{uv}}a_r
\le
\left|\bigcup_{r\in R_{uv}}L(r)\right|,
\]
and, more importantly, the corresponding inequality for arbitrary mixtures
of rows from different bridges and from distance-one and distance-two mark
types. Bridge-by-bridge inequalities alone do not imply the mixed-family
inequality because lift target sets from different bridges can overlap.

## 4. What would count as a structural proof

A structural charging theorem must provide both:

1. A parent allocation alpha, recursively specified and conserving every
   fiber demand across its parent targets.
2. A proof of (2) for the resulting rows, using a combinatorial invariant
   of reverse marks and their lift sets.

One possible invariant is a rooted edge decomposition of T: charge each
type-3 mark to its central bridge and leaf-side pair, and charge types 1 and
2 to their unique local center. But to prove (2), one must show that any
collection of these marked configurations has enough distinct lifted child
trees, including when configurations share vertices, bridges, or parent
targets. No such expansion inequality has yet been established.

## 5. Logical status

Equation (2) is necessary and sufficient for a fixed alpha. It is an exact
reformulation of the remaining lift-kernel problem, not a proof that the
kernel exists. Allowing alpha itself to vary adds another allocation layer;
the combined feasibility problem is still a capacitated flow problem.

The finite n=8 and n=10 split-demand flows establish their own finite
instances. They do not establish (2) for arbitrary s, nor identify a
recursive alpha with a proof of the required mixed-row expansion.

The global cross-fiber inequality, weighted one-link inequality, and
Yang--Mills mass-gap claim remain unproved.
