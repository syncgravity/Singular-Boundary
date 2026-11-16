# Reverse switches from a fixed final tree (2026-11-16)

## 1. One-step inverse

Let (V) be the current port set, let (T) be a tree on (V), and let
(J=\{a,b\}\) be a matching interval whose endpoints are not in (V).
Choose a current tree edge (e=\{u,w\}\) whose interval overlaps (J);
the four endpoints are distinct. Write them in increasing order as
(p<q<r<s).

Let (S_0,S_1,S_2) be the three allowed local switch trees on these four
ordered endpoints: the star centered at (q), the increasing path, and
the star centered at (r). A forward step is
[
T^+=(T\setminus\{e\})\cup S_j.
]
Here the two new vertices are (a,b), and all other vertices and all
other tree edges are unchanged.

For a tree (U), write
[
\delta_U(\{a,b\})=\{f\in E(U): f\cap\{a,b\}\ne\varnothing\}.
]
The exact inverse transition is
[
\boxed{
T^-=
\bigl(E(U)\setminus\delta_U(\{a,b\})\bigr)\cup\{e\},
\qquad U=T^+.
}
	ag{R}
]
The inverse is legal precisely when
[
\delta_U(\{a,b\})
=
\delta_{S_j}(\{a,b\}).
\tag{R-inc}
]
In particular, the two new endpoints have no incident edges beyond the
local switch edges. Under (R-inc), (R) is exactly the previous tree (T):
it deletes the two new vertices, removes their local incidences, and restores
the replaced edge. It is not the operation of deleting all three local
edges while retaining all four endpoints.

**Why (R-inc) is necessary.** At the instant (J) is inserted, (a,b)
are new, so every edge incident to either endpoint is one of the local
switch edges. For the last insertion in a history, no later step can have
attached an edge to either endpoint. Thus (R-inc) holds when reversing a
genuine history in reverse chronological order.

**Why it is sufficient.** The current tree is the forward image of a tree
under the specified local replacement. Removing the complete incident
stars of (a,b), then restoring (e), recovers the old edge set exactly.
Consequently the result is a tree on (V\setminus\{a,b\}), with one fewer
edge than vertices.

## 2. Reverse transition rule for a fixed final tree

Fix a source matching (M) and its overlap spanning tree \(\tau\), rooted
at the matching interval containing port 1. A reverse state consists of:
- a current tree (U) on the endpoints of the intervals not yet removed;
- the remaining rooted subtree of \(\tau\);
- the remaining matching intervals.

A reverse move is:

1. Choose a non-root leaf interval (J=(a,b)) of the remaining rooted
   overlap tree. This is exactly an interval that could have been last in a
   parent-before-child insertion order.
2. Choose a current edge (e=(u,w)) whose interval overlaps (J).
3. For each of the three local trees (S_j), form its labeled copy on
   ({u,w,a,b}). Keep the choice only if its incident edges at (a,b)
   equal the complete incident edges of (a,b) in (U), as in (R-inc).
4. Apply (R), remove (J) and its leaf from \(\tau\), and continue.

When only the root interval remains, the current tree must be its single
edge. Reversing a complete forward history always follows this rule.

This gives a reverse-search characterization of the ancestry fiber over a
fixed final tree (T_*): start with (U=T_*) and enumerate all legal
reverse branches. A branch records the source matching, overlap tree, and
reverse history. Distinct branches can still coalesce to the same source
((M,\tau)) and final tree; therefore the desired column counts each
source-target pair only once.

## 3. What this does not yet prove

For a fixed (T_*), the exact weighted column remains
[
W(T_*)=
\sum_{(M,\tau):\,T_*\in C(M,\tau)}
\frac{1}{|C(M,\tau)|}.
]
The reverse rule identifies the admissible last-step predecessors and gives
a finite reverse recursion. It does not by itself bound this sum: one still
needs a sourcewise quotient of reverse branches and an all-orders estimate
for the resulting weighted source set. Counting reverse histories without
collapsing repeated branches from the same source would overcount.

The ancestry verifier
`research/verification/verify_pf_i16_switch_ancestry_quotient.py`
has been extended with `reverse_history`, which checks (R-inc), performs
(R), and verifies the tree invariant at every reverse step for every
enumerated history. It is configured for four and six ports. The updated
verifier has not yet been executed in this work session; no new finite
pass result is claimed here.

This is a precise inverse-transition lemma and search rule, not a proof of
the weighted one-link inequality or of a Yang--Mills mass gap.
