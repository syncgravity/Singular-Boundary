# PF-I16: corrected target-side reverse-mark classification and mixed-mark structure

Date: 2026-11-17

> **Correction to the earlier version of this audit:** the distance-three
> leaf-pair case below is NOT a valid reverse mark for the implemented
> inverse. The old edge {u,v} must be absent from the induced local
> four-vertex tree. If it is already one of its three edges, adding it back
> after deleting the local tree does not restore the required edge count;
> the verifier's len(parent)==n-3 assertion rejects it. In particular,
> the double-star cross-bridge leaf-pair family is not a family of valid
> reverse marks. The previous claim that it proves unbounded valid-mark
> multiplicity is withdrawn.

## 1. Exact validity conditions

For a proposed inserted interval J={a,b} in a target tree T, put
\[
S_T(a,b)=(N_T(a)\cup N_T(b))\setminus\{a,b\}.
\]
The implemented inverse first requires |S_T(a,b)|=2, say S={u,v};
the induced four-vertex tree on {a,b,u,v} must be one of LOCAL_TREES;
and the old edge uv must be absent from that induced tree. The last condition
is essential: the inverse removes the three local edges and adds uv, so the
edge count rises by one only if uv was not already present.

For a tree on n vertices, this gives a parent tree with n-3 edges after
removing a,b. The inverse parent is unique for each valid J:
\[
P_J(T)=\bigl(T-E(T[\{a,b,u,v\}])\bigr)\cup\{uv\}.
\]
This is unique conditional on J; it says nothing by itself about collisions
between different J.

## 2. Correct classification of raw candidates

Assume |S_T(a,b)|=2 and the induced four-vertex graph is connected. Before
the old-edge exclusion, the tree-distance cases are:

- dist(a,b)=1 and deg(a)+deg(b)=4;
- dist(a,b)=2 and deg(a)+deg(b)=3;
- dist(a,b)=3 and a,b are both leaves.

The third case has local path a-u-v-b, so uv is already an edge of the
induced local tree. It is therefore rejected by the old-edge exclusion.
Consequently every valid reverse mark is of one of the first two types:

**Type I — adjacent endpoints.**
The endpoint degrees are (1,3) or (2,2). In the (1,3) case the induced
local tree is a three-star; in the (2,2) case it is a four-vertex path.
The old edge joins the two external neighbors and is absent from the local
tree.

**Type II — distance-two endpoints.**
One endpoint is a leaf and the other has degree two. The induced local tree
is a four-vertex path; the old edge joins the middle vertex to the external
neighbor of the degree-two endpoint and is absent from the local tree.

Proof of the distance classification: if dist=1, the external-neighbor
sets are disjoint and have total size deg(a)+deg(b)-2. If dist=2, they
intersect in the middle vertex and their union has size deg(a)+deg(b)-1.
If dist=3, they are disjoint, and connectedness forces the middle edge uv,
which is exactly the forbidden old edge. At distance at least four, the
induced four-set cannot be connected.

## 3. Port order makes the surviving type-II pattern rigid

For type II, write the target path as l-u-d-v, where l is the leaf, d is
the degree-two endpoint, and u is the middle vertex. The allowed local path
is the increasing path on the four sorted ports. Since the interval endpoints
are the two marked vertices, there are exactly two possible order patterns:

- l < u < d < v, with J=(l,d)=(x1,x3);
- v < d < u < l, with J=(d,l)=(x2,x4).

In the first pattern, the path edges are lu, ud, dv and the absent old edge
is uv. In the second, the path edges in increasing order are vd, du, ul
and the absent old edge is vu. In either case the old edge joins the two
unmarked vertices and is absent from the local path. These are mirror
orientations; neither may be discarded. The inverse removes the three
path edges and restores uv.

Type-I marks are similarly rigid: in a star pattern, J is the adjacent
leaf/center pair at one end of the sorted four-set; in the path pattern,
J is the middle edge (x2,x3).

Type-I marks are likewise local: either a leaf/degree-three adjacent pair
in one of the two star patterns, or the middle edge of an increasing
four-path with degree pair (2,2).

This is a useful reduction: the mixed-mark problem is not a generic
four-vertex-tree problem. It is a problem about ordered leaf/degree-two
configurations plus the two type-I configurations, subject also to the
no-reinsertion guard and canonical-parent membership.

## 4. Why the corrected classification still does not prove mixed expansion

The rejected distance-three case removes the earlier double-star
counterexample, but type-II configurations can still have high raw
multiplicity around one vertex u: many leaves a<u and many degree-two
vertices b>u with other neighbors v>b yield candidate pairs (a,b).
The matching/overlap-tree constraints and the canonical-parent condition
may sharply thin these candidates, but no uniform bound has been proved.

For rows r=(p,J,P), with demand a_r and lift set L(r), the exact mixed
expansion statement remains
\[
\sum_{r\in R}a_r\le
\left|\bigcup_{r\in R}L(r)\right|
\quad\text{for every mixed row family }R.
\]
The classification above supplies a structural description of which J can
occur in a common target T. It does not establish this inequality: one must
still control overlaps among the lift sets arising from distinct type-I
and type-II marks, including marks sharing u, sharing an endpoint, or
arising from different parent sources.

## 5. Precise next lemma to prove

A plausible intermediate statement is an **ordered-center expansion lemma**.
Fix a target T and a center u. Let
\[
A_u=\{a<u: a\text{ is a leaf adjacent to }u\},\qquad
B_u=\{b>u: b\text{ has degree }2,\ N_T(b)=\{u,v_b\},\ v_b>b\}.
\]
Every type-II mark centered at u lies in A_u x B_u, before the
additional guard and parent-neighborhood restrictions.

The required lemma cannot merely bound |A_u||B_u|. It must show that for
any weighted selection of the corresponding parent rows, the union of their
admissible final lifts has capacity at least the total selected demand.
It must also remain true after adjoining type-I rows and rows centered at
other vertices. That mixed version is precisely the unresolved expansion
problem; no proof is claimed here.
