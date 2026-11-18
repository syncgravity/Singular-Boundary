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

The ten-port run and log review are complete; the numerical results and the resulting counterexample are recorded in Section 8 below.

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


## 8. Completed n=10 third-mark census: canonical step fails (2026-11-18)

The two pending workflows have completed successfully:

- Focused rooted-star census, [run 44231435721](https://github.com/syncgravity/Singular-Boundary/actions/runs/44231435721), checked out `a0fb1755363382a91998a3663abd7f7163418ff5`.
- Full canonical source-diamond census, [run 44231184102](https://github.com/syncgravity/Singular-Boundary/actions/runs/44231184102), checked out `b15cabdcb82a45b124f3bbaa9c771f7e63e22a0e`.

Both jobs completed with success. The script output, rather than the CI success status alone, gives the mathematical result.

### Full n=10 source-diamond result

The full census reports:

- 608 parent sources and 630 unordered disjoint mark pairs;
- 16,636 exact sibling-source diamonds;
- 3,600,244 common-target incidences;
- all 3,600,244 incidences mutually surviving on the target side;
- 3,279,589 canonical-parent passes and **320,655 canonical-parent failures**.

The 16,636 diamonds split into 13,398 rooted-path common parents and 3,238 rooted-star common parents. The rooted-path cases have only one non-root leaf, so their canonical condition is automatic. Every one of the 320,655 failures occurs in the first nontrivial rooted-star class.

### Focused rooted-star result

The focused census reports:

- 158 child-parent sources whose common parent is a three-interval rooted star;
- 3,238 source diamonds and 858,905 common-target incidences;
- all 858,905 incidences mutually surviving;
- canonical leaf (A) is a guarded reverse mark in 538,250 incidences and is **not** a guarded reverse mark in 320,655;
- in every one of the 538,250 cases where (A) is valid, the other leaf (B) survives after reversing (A);
- there are zero failures of (B)-survival conditional on (A)-validity.

Thus the rooted-star equivalence (S) is confirmed by the finite census, but it does not rescue the proposed source-diamond implication: the obstruction is that (A) itself is not a reverse mark of (U) in 320,655 incidences. The adjacent leaf-bubbling argument cannot start in those cases.

The attachment-type counts across the 3,238 rooted-star source diamonds are:
[
egin{array}{c|rrr}
 & A & B & R\\
A & 800 & 360 & 640\\
B & 180 & 144 & 240\\
R & 280 & 210 & 384
end{array}
]
where the row records the attachment of (K) and the column the attachment of (J), with (A) the canonical leaf of the common parent, (B) its other leaf, and (R) its root.

### Explicit first counterexample

The first failure has
[
J=(2,3),\qquad K=(4,5),
]
and the two parent sources coincide:
[
p=q=
left(
((1,6),(2,3),(4,7),(5,8)),
((0,1),(0,2),(0,3))
ight).
]
The common parent is the rooted star
[
r=
left(
((1,4),(2,5),(3,6)),
((0,1),(0,2))
ight),
]
whose canonical non-root leaf is (A=(2,5)), and whose other leaf is (B=(3,6)).

The common parent target is
[
U=((1,2),(2,3),(3,4),(4,5),(4,6)).
]
It is an ordinary guarded output of (r), obtained with (B) last, but (A) is not a valid guarded reverse mark of (U). Hence (U\notin C_{\rm can}(r)), despite the two target-side reverse operations being mutually surviving and giving the same double inverse.

The full census also records the corresponding child target:
[
T=\{(1,3),(2,3),(3,5),(4,5),(5,6),(6,7),(7,8),(8,9),(8,10)\}.
]
This is a concrete finite counterexample to the source-level canonical third-mark implication as currently formulated. It does not contradict the target-side mutual-survival theorem, the multivalued-π relation, or Hall for that relation.

### Consequence and next separation

The canonical third-mark lemma in its unrestricted sibling-source form is false. It must not remain a proof obligation stated as though a proof were merely missing. The next diagnostic separates the degenerate case (p=q) from the genuinely distinct-parent case (p\ne q). The first counterexample has (p=q), so it is not yet known whether the distinct-parent restriction restores the finite n=10 implication.

A separate diagnostic script and CI workflow have been added:

- `research/verification/verify_pf_i16_n10_distinct_parent_third_mark.py`
- `.github/workflows/pf-i16-n10-distinct-parent-third-mark.yml`

Their execution result has not yet been retrieved. No claim about the (p\ne q) subcase is made here.

### Updated proof boundary

Established:
- the target-side mutual-survival diamond;
- the exact rooted-star criterion (S);
- the one-sided leaf-bubbling sufficient criterion;
- a finite n=10 counterexample to the unrestricted canonical source-level third-mark implication.

Still open:
- whether a corrected distinct-parent third-mark lemma holds;
- how the (p=q) degeneracy should be handled in the global capacity argument;
- the arbitrary-family mixed-fiber Hall inequality;
- the all-orders multivalued-π Hall theorem;
- the weighted one-link inequality unconditionally.
