# PF-I16: all-orders third-mark lemma — proof reduction and base-order correction

Date: 2026-11-18

Status: **proof reduction established; all-orders third-mark lemma remains open.** This note corrects the evidentiary interpretation of the earlier n=6/n=8 source-diamond census and records the next structural obligation without promoting finite evidence to a theorem.

## 1. Exact setup

Let x be a child source whose overlap tree has two distinct non-root leaves J,K. Let
\[
p=\pi_J(x),\qquad q=\pi_K(x),\qquad
r=\pi_K(p)=\pi_J(q).
\]
The source-diamond hypotheses under study are:

- J and K are disjoint matching intervals and leaves of the child overlap tree;
- K is the canonical leaf of p;
- J is the canonical leaf of q;
- a target T lies in both retained fiber neighborhoods through J and K;
- J and K are mutually surviving guarded reverse marks of T.

The target-side theorem then gives a common double inverse U. Because the K inverse of P_J(T) is the canonical last insertion of p, U is an ordinary output of r. Likewise from q. The unresolved point is whether U can be generated with the canonical leaf of r last.

Write C(r) for all guarded outputs of r and C_can(r) for those with its canonical non-root leaf inserted last.

## 2. Correction: why n=6 and n=8 do not test nontrivial C3

At n=6, r has one matching interval and no non-root leaf.

At n=8, r has two matching intervals. Its overlap tree is a single edge rooted at the interval containing port 1, so there is exactly one non-root leaf. Therefore
\[
C(r)=C_{\rm can}(r)
\]
at both orders.

The earlier census counts (8 sibling-source diamonds / 37 common target incidences at n=6; 274 / 7,884 at n=8) remain valid checks of source identity, exact fiber construction, guarded mutual survival, and equality of the two target-side double inverses. But the C3 membership result is automatic after establishing U in C(r). The additional n=8 checks of the unique leaf and its parent projection are useful verifier consistency checks, not an independent test of canonical choice.

The first possible nontrivial case is n=10, where r has three matching intervals:
- if its rooted overlap tree is a path, it still has one non-root leaf and C3 is automatic;
- if its rooted overlap tree is a star rooted at its center, it has two non-root leaves and canonical choice matters.

## 3. Exact reduction in the rooted-star case

Suppose r has root R and two non-root leaves A,B, with A lexicographically smaller than B. Then C_can(r) is the subset of C(r) whose histories end in A.

If U has a history ending in A, it is canonical. Otherwise a history ends in B, so B is a valid guarded reverse mark of U. Deleting A from r leaves the two-interval rooted path source r-A, whose only non-root leaf is B. Consequently its full output set is exactly the set of targets on which B is a valid guarded reverse mark. Hence, for a history of U ending in B,
\[
U\in C_{\rm can}(r)
\iff
A\text{ is valid in }U
\quad\text{and}\quad
B\text{ is valid in }P_A(U).
\tag{S}
\]

This is one-sided survival of B through the A inverse. It does not require A to survive after the B inverse. If both directions survive, the target-side mutual-survival diamond gives the stronger commutation statement, but that is not needed for (S).

Thus the first nontrivial all-orders case reduces to a precise local third-mark obligation: the canonical leaf A must be a reverse mark of U, and the other leaf B must survive after reversing A.

## 4. Source-side attachment case split

In the rooted-star source r, let v_K be the vertex of r to which the child leaf K is attached in p=r+K, and v_J the vertex to which J is attached in q=r+J.

If v_K is not A, then A remains a non-root leaf in p. Since K is canonical in p, K is lexicographically no later than A in p's compressed interval order. Similarly, if v_J is not A, then J is no later than A in q's compressed interval order.

Therefore the only attachment geometry in which neither source canonicality condition compares the added leaf with A is
\[
v_K=v_J=A.
\]
This is an exact source-tree case split. The p and q coordinate systems are separately compressed, so it does not imply a comparison between K and J, and it does not yet imply any target-side reverse-mark incidence at A.

The remaining proof must combine this source attachment information with the exact ordered four-port patterns, full endpoint-incidence equality, positive overlap, and no-reinsertion guard. A purely interval-order comparison is insufficient.

## 5. Leaf-bubbling lemma: a sufficient all-orders criterion

Let L be a non-root leaf of a source overlap tree, and let
\[
\sigma=(I_1,\ldots,I_s)
\]
be a parent-before-child insertion history producing U. Since L has no descendants, moving it rightward across later intervals preserves the source partial order.

Consider an adjacent segment in the history where L is followed by K, and let V be the target immediately after K is inserted. Assume:

1. L is a valid guarded reverse mark of V;
2. K remains a valid guarded reverse mark of P_L(V).

Then
\[
V\xrightarrow{P_L}P_L(V)\xrightarrow{P_K}W
\]
is a valid inverse sequence. Reversing these two steps constructs V in the order K then L:
\[
W\xrightarrow{K}P_L(V)\xrightarrow{L}V.
\]
Thus the adjacent insertions can be swapped without changing their terminal target. Repeating such swaps moves L to the final position, proving U in C_can(r).

This proof uses one-sided survival of the later mark after the earlier mark is reversed. It does not need the full mutual-survival diamond, although that stronger theorem applies when both directions survive.

The lemma is only a sufficient criterion. The current source-diamond hypotheses have not yet been shown to provide the required chain of one-sided survivals.

## 6. Exact next obligations

For arbitrary r, derive from the sibling-source hypotheses either:

- the direct third-mark statement \(L\) valid in U and \(P_L(U)\in C(r-L)\); or
- a leaf-bubbling sequence of adjacent one-sided survivals that moves L to the end of a valid construction history.

For n=10, focus first on the rooted-star case. The verifier has been extended to record the attachment types of J and K relative to A, B, and R, and to count separately:
- A valid as a reverse mark of U;
- B surviving after the A inverse;
- canonical parent-output membership.

The ten-port run is not yet accepted as evidence until its workflow completes and its logs are read back. No numerical result from an in-progress run is asserted here.

## 7. Proof boundary

Established:
- the target-side mutual-survival diamond for every finite port tree;
- the source projection identity in the finite n=6/n=8 census;
- the exact C4 forced-last characterization;
- the rooted-star equivalence (S);
- the one-sided adjacent leaf-bubbling criterion.

Not established:
- that the sibling-source hypotheses force (S) at n=10;
- an all-orders source-level third-mark lemma;
- an arbitrary-family mixed-fiber Hall inequality;
- the all-orders multivalued-\(\pi\) Hall theorem;
- the weighted one-link inequality unconditionally.
