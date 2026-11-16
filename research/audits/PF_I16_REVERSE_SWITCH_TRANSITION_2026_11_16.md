# Reverse switches from a fixed final tree (2026-11-16)

This note records the inverse rule for the **guarded** local-switch
relation. The corrected finite results and sourcewise degree proof are in
`PF_I16_GUARDED_SWITCH_REVALIDATION_2026_11_16.md`.

## 1. One-step inverse

Let T be a tree on V, let J={a,b} be a new matching interval, and let
e={u,w} be an edge of T overlapping J. Write the four endpoints as
x1<x2<x3<x4. Let S_j be one of

- S0={(x1,x2),(x2,x3),(x2,x4)},
- S1={(x1,x2),(x2,x3),(x3,x4)},
- S2={(x1,x3),(x2,x3),(x3,x4)}.

The guarded forward move is
[
E(U)=(E(T)\setminus\{e\})\cup E(S_j),
qquad e\notin E(S_j).
]
The guard excludes a move that immediately puts the replaced edge back.
Such an unguarded move can still produce a tree, but it is not part of the
transition relation studied here.

Define
[
\delta_U(J)=\{f\in E(U):f\cap J\ne\varnothing\}.
]
For a specified e and S_j, the inverse is
[
E(T)=\bigl(E(U)\setminus\delta_U(J)\bigr)\cup\{e\}.
]
The inverse checks are
[
e\notin E(S_j),\quad
E(S_j)\subseteq E(U),\quad
\delta_U(J)=\delta_{S_j}(J).
]
One may also check e notin E(U); this is redundant because U is a tree,
S_j is connected and contained in U, and e is not in S_j.

The first condition is the forward guard. The second verifies the entire
prescribed local tree. The third ensures that a,b have no additional
incident edges. In either guarded interleaving case, deleting a,b from
S_j leaves the two old endpoints with no edge between them. Since a,b
have no external incident edges, deleting them from U leaves exactly two
components, one containing each old endpoint. Restoring e reconnects those
components and recovers the predecessor tree exactly.

## 2. Reverse rule for a fixed final tree

For fixed source (M,tau), root tau at the matching interval containing
port 1. A reverse state consists of the current tree, the remaining
intervals, and the remaining rooted overlap tree.

At each reverse step:
1. choose a non-root leaf interval J of the remaining rooted overlap tree;
2. choose an overlapping current edge e;
3. retain only local trees S_j satisfying the three inverse checks above;
4. delete a,b and restore e.

For a genuine history, reversing in reverse chronological order satisfies
these checks. After all intervals except the root have been removed, the
tree is the root matching edge.

## 3. Reverse uniqueness at fixed insertion order

For a guarded move, every edge of S_j is incident to at least one endpoint
of J, because the old-old edge e is excluded. Thus at the last insertion,
delta_U(J)=S_j. For fixed J, the incidence set determines S_j; its support
outside J determines the two old endpoints and hence e. The predecessor
is then unique. Repeating backward proves that, for a fixed insertion
order, distinct forward histories have distinct final labeled trees.

The exact corrected finite enumeration and inverse replay counts are
recorded in
`PF_I16_GUARDED_SWITCH_REVALIDATION_2026_11_16.md`.

This inverse lemma and its finite checks do not prove the full weighted
one-link inequality or a Yang--Mills mass gap.
