# Reverse switches from a fixed final tree (2026-11-16)

## 1. One-step inverse

Let \(V\) be the current port set, let \(T\) be a tree on \(V\), and let
\(J=\{a,b\}\) be a matching interval whose endpoints are not in \(V\).
Choose a current tree edge \(e=\{u,w\}\) whose interval overlaps \(J\);
the four endpoints are distinct. Write them in increasing order as
\(p<q<r<s\).

Let \(S_0,S_1,S_2\) be the three allowed local switch trees on these four
ordered endpoints: the star centered at \(q\), the increasing path, and
the star centered at \(r\). A forward step is
\[
E(T^+)=(E(T)\setminus\{e\})\cup E(S_j).
\]
Here the two new vertices are \(a,b\), and all other vertices and all
other tree edges are unchanged.

For a tree \(U\), write
\[
\delta_U(\{a,b\})=\{f\in E(U): f\cap\{a,b\}\ne\varnothing\}.
\]
The exact inverse transition is
\[
\boxed{
E(T^-)=
\bigl(E(U)\setminus\delta_U(\{a,b\})\bigr)\cup\{e\},
\qquad U=T^+.
}
\tag{R}
\]
The inverse is legal precisely when
\[
e\notin E(S_j),\qquad
e\notin E(U),\qquad
E(S_j)\subseteq E(U),\qquad
\delta_U(\{a,b\})=\delta_{S_j}(\{a,b\}).
\tag{R-inc}
\]
The first condition is essential: otherwise the forward operation can
reinsert the edge it supposedly replaced, and the edge count need not be
that of a tree. The additional condition \(e\notin E(U)\) is also
necessary: the replaced edge must actually be absent from the current tree
when it is restored. Without it, the set-union formula can fail to add an
edge and cannot recover the predecessor edge set. The second ensures that the entire prescribed local switch
tree is present, including a possible edge between the two old endpoints.
The third says that the two new endpoints have no incident edges beyond
those prescribed by the local switch. Under these conditions, (R) recovers
the previous tree exactly: it deletes the two new vertices, removes their
local incidences, and restores the replaced edge. It is not the operation
of deleting all three local edges while retaining all four endpoints.

**Why the four conditions are necessary.** At the instant \(J\) is inserted, \(a,b\)
are new, so every edge incident to either endpoint is one of the local
switch edges. The complete local tree is inserted. For the last insertion
in a history, no later step can have attached an edge to either endpoint.
The replaced edge was deleted and is not one of the inserted local edges;
thus all four conditions hold when reversing a genuine history in reverse
chronological order.

**Why it is sufficient.** The current tree contains the complete local
switch tree, and its incidences at \(a,b\) are exactly the prescribed
ones. Removing those incidences and restoring \(e\) recovers the old edge
set exactly. Consequently the result is a tree on
\(V\setminus\{a,b\}\), with one fewer edge than vertices.

## 2. Reverse transition rule for a fixed final tree

Fix a source matching \(M\) and its overlap spanning tree \(\tau\), rooted
at the matching interval containing port 1. A reverse state consists of:
- a current tree \(U\) on the endpoints of the intervals not yet removed;
- the remaining rooted subtree of \(\tau\);
- the remaining matching intervals.

A reverse move is:

1. Choose a non-root leaf interval \(J=(a,b)\) of the remaining rooted
   overlap tree. This is exactly an interval that could have been last in a
   parent-before-child insertion order.
2. Choose a current edge \(e=(u,w)\) whose interval overlaps \(J\).
3. For each of the three local trees \(S_j\), form its labeled copy on
   \(\{u,w,a,b\}\). Keep the choice only if both conditions in (R-inc)
   hold in \(U\).
4. Apply (R), remove \(J\) and its leaf from \(\tau\), and continue.

When only the root interval remains, the current tree must be its single
edge. Reversing a complete forward history always follows this rule.

This gives a reverse-search characterization of the ancestry fiber over a
fixed final tree \(T_*\): start with \(U=T_*\) and enumerate all legal
reverse branches. A branch records the source matching, overlap tree, and
reverse history. Distinct branches can still coalesce to the same source
\((M,\tau)\) and final tree; therefore the desired column counts each
source-target pair only once.

## 3. What this does not yet prove

For a fixed \(T_*\), the exact weighted column remains
\[
W(T_*)=
\sum_{(M,\tau):\,T_*\in C(M,\tau)}
\frac{1}{|C(M,\tau)|}.
\]
The reverse rule identifies the admissible last-step predecessors and gives
a finite reverse recursion. It does not by itself bound this sum: one still
needs a sourcewise quotient of reverse branches and an all-orders estimate
for the resulting weighted source set. Counting reverse histories without
collapsing repeated branches from the same source would overcount.

The ancestry verifier
research/verification/verify_pf_i16_switch_ancestry_quotient.py
has been extended with reverse_history, which checks all three conditions in
(R-inc), performs (R), and verifies the tree invariant at every reverse
step for every enumerated history. It is configured for four and six ports.
Both forward enumerators now discard a proposed local replacement when
the selected old edge reappears in the three-edge local tree; the ancestry
reverse checker also asserts this exclusion. This tightens the admissible
transition relation. The previously reported finite degree and column
figures were produced before this guard was added and must be revalidated
against the corrected relation. The updated verifiers have not yet been
executed in this work session; no corrected finite pass result is claimed.

The displayed inverse condition (R-inc) is the four-condition version;
the earlier prose-only mention of e's absence is not a separate optional
guard.

This is a precise inverse-transition lemma and search rule, not a proof of
the weighted one-link inequality or of a Yang--Mills mass gap.


## 4. Corrected valid-choice count

For overlapping intervals, the endpoints of the old edge and the new
interval alternate in the sorted four-point order. Thus the old edge is
either the (1,3) or (2,4) diagonal. Inspecting the three allowed local trees,
exactly one contains that diagonal; the other two are valid. Therefore,
for every currently available overlapping edge, there are exactly two
valid local replacements after the no-reinsertion guard.

At every insertion, the maintained path joining the endpoints of the
parent interval contains an edge overlapping the child interval. To see
this, if the intervals interleave as p<a<q<b, the p-to-q path crosses the
cut at a; if a<p<b<q, the p-to-q path crosses the cut at b. The crossing
edge overlaps the child interval. Consequently every current state has at
least two valid next transitions.

For a fixed parent-before-child order with s-1 non-root intervals, the
number of forward histories is therefore at least 2^(s-1). This is a
history lower bound, not yet a lower bound for the number of distinct
terminal trees: histories may coalesce across different orders (and that
quotient must be counted sourcewise).

The inverse test now explicitly checks e is absent from U before restoring
it. This condition is necessary for exact edge-set recovery and follows
for a genuine reverse-chronological history after all later insertions
have first been undone.


## 5. Distinct-output lower bound from reverse uniqueness

Fix one parent-before-child insertion order. At a step inserting J, the
old edge e and J interleave. If e is the (1,3) pair, the two valid local
trees are S0 and S1; if e is the (2,4) pair, they are S1 and S2. In either
case every edge of the valid local tree is incident to at least one of the
two new endpoints. The three-edge local tree is therefore exactly the
incidence set delta_U(J) at the instant it is the last insertion.

For a fixed J and final tree U, a valid reverse step is unique: delta_U(J)
is the local tree S; its support outside J gives the two old endpoints,
hence determines e. The predecessor is then uniquely
(U minus the incidences at J) union {e}. Inducting backward along the fixed
insertion order shows that two different forward histories with that same
order cannot end at the same labeled tree.

There are at least two valid choices at every current state, by the
parent-path crossing argument in Section 4. Thus one fixed insertion order
has at least 2^(s-1) histories, and reverse uniqueness makes their terminal
trees distinct. Consequently every source has at least 2^(s-1) distinct
outputs under the guarded relation. This replaces the former, invalid
3^(s-1) degree floor.

The finite verifier now asserts this corrected floor and checks at every
enumerated state that the number of next transitions is at least twice the
number of current states. These are executable checks; corrected finite
column figures remain pending execution.
