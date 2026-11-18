# PF-I16 distinct-parent source-diamond theorem: counterexample and revised proof boundary

Date: 2026-11-18

## 1. Status

The proposed distinct-parent canonical diamond assertion is **false at n=10**. The condition p != q does not repair the unrestricted canonical third-mark implication.

The n=10 diagnostic excludes p=q before counting the tested source diamonds. It finds 2,906 distinct-parent rooted-star source diamonds and 765,852 common-target incidences. All 765,852 incidences have mutually surviving guarded reverse operations and a common double inverse. Among them, the canonical common-parent leaf A is a valid guarded reverse mark in 479,412 cases and invalid in 286,440 cases. Whenever A is valid, B survives after reversing A (479,412/479,412); there are no B-survival failures conditional on A-validity.

Thus the exact failure is at the first clause of the rooted-star criterion, not at the second.

## 2. Exact source-diamond setup

Let x=(M,tau) be a child source and J,K disjoint non-root leaves. Put
[
p=\pi_J(x),\quad q=\pi_K(x),\quad r=\pi_K(p)=\pi_J(q).
]
The retained target T lies in both fiber neighborhoods, and the guarded reverse operations at J and K mutually survive. Hence there is a common double inverse
[
U=P_K(P_J(T))=P_J(P_K(T)).
]
The canonical source routes put U in the ordinary common-parent neighborhood C(r).

The proposed strengthening
[
p\ne q\quad\Longrightarrow\quad U\in C_{\rm can}(r)
	ag{DP}
]
is disproved by the witness below.

## 3. Explicit distinct-parent counterexample

The first logged failure has
[
J=(2,3),\qquad K=(4,6),
]
and distinct parent sources
[
p=\left(
((1,6),(2,4),(3,7),(5,8)),
((0,1),(0,2),(0,3))
\right),
]
[
q=\left(
((1,6),(2,3),(4,7),(5,8)),
((0,1),(0,2),(0,3))
\right).
]
They are distinct as matching/overlap-tree sources, and both delete to
[
r=\left(
((1,4),(2,5),(3,6)),
((0,1),(0,2))
\right).
]
The common parent r is a rooted star. Its non-root leaves are
[
A=(2,5),\qquad B=(3,6),
]
with A the canonical leaf. The common double inverse is
[
U=((1,2),(2,3),(3,4),(4,5),(4,6)).
]
The verifier reports that A has no exact guarded reverse record in U. Therefore U is an ordinary output of r but not in C_can(r), by the exact rooted-star criterion
[
U\in C_{\rm can}(r)
\iff
A\text{ is a guarded reverse mark of }U
\text{ and }B\text{ survives after reversing }A.
]

Both added canonical leaves in p and q attach to the root of r (attachment type (R,R)), rather than to A. Thus the earlier attachment discussion does not isolate the obstruction: even when both source extensions attach at the root and their canonical-leaf comparisons place the added leaves before A in their respective compressed orders, A need not be a reverse mark of U. The compressed-order comparisons do not control the target-side endpoint-incidence/guard condition.

The diagnostic has been patched to print the exact common child target T and the two reverse records for future counterexample readback. The completed logs currently available for the three original runs did not print T, so this audit does not invent it. The full p,q,r,U witness and the invalidity test are exact; the target T remains to be read from the patched rerun before claiming the complete five-tuple.

## 4. Finite diagnostic details

The focused verifier is
`research/verification/verify_pf_i16_n10_distinct_parent_third_mark.py`.
Its cache is keyed by parent source and target mark. It constructs both retained fiber neighborhoods from canonical parent targets and exact guarded forward lifts, intersects them, computes both inverse orders, asserts equality of the common double inverse, and verifies ordinary common-parent output membership.

Three completed successful runs produced the same census:
- [44256861362](https://github.com/syncgravity/Singular-Boundary/actions/runs/44256861362)
- [44257821334](https://github.com/syncgravity/Singular-Boundary/actions/runs/44257821334)
- [44258114237](https://github.com/syncgravity/Singular-Boundary/actions/runs/44258114237)

Their shared counts are:
- parent sources: 608; rooted-star child-parent sources: 158;
- disjoint mark pairs: 630;
- distinct-parent source diamonds: 2,906 (the 332 p=q diamonds are excluded);
- common-target incidences: 765,852;
- mutually surviving double inverses: 765,852;
- A valid: 479,412; A invalid: 286,440;
- B survives after A in all 479,412 A-valid cases; no conditional B failures.

Attachment types (p-extension attachment, q-extension attachment) across the 2,906 distinct-parent source diamonds:
[
\begin{array}{c|r}
(A,A)&632\\
(A,B)&360\\
(A,R)&640\\
(B,A)&180\\
(B,B)&84\\
(B,R)&240\\
(R,A)&280\\
(R,B)&210\\
(R,R)&280
\end{array}
]
Here A and B denote the two non-root leaves of r, and R its root.

This is a finite disproof at n=10, not an all-orders statement. It does not contradict target-side mutual-survival, the retained multivalued-pi relation, or the all-orders Hall theorem.

## 5. What remains usable

The following rooted-star implication remains supported by the exhaustive n=10 census:
[
A\text{ valid in }U
\quad\Longrightarrow\quad
B\text{ survives after reversing }A.
]
This is only finite evidence at n=10. The leaf-bubbling criterion remains a sufficient condition: if a leaf is valid at each adjacent swap and the next inserted leaf survives after its inverse, that leaf can be bubbled to the final position. The source-diamond hypotheses have not been shown to imply those swap conditions.

The distinct-parent split alone is not a valid reduction. In particular, the (R,R) attachment class already contains failures, so excluding the exceptional (A,A) attachment geometry would not suffice.

## 6. Revised proof boundary

Established:
- target-side mutual-survival yields the common double inverse U;
- source routes put U in C(r);
- the exact rooted-star canonicality criterion;
- unrestricted DP is false at n=10;
- the distinct-parent DP is also false at n=10, with explicit p,q,r,U and verified A-invalidity.

Open:
- a correct restricted local canonicality statement, if one is needed;
- an all-orders mixed-fiber Hall proof that does not rely on this false diamond implication;
- the all-orders multivalued-pi Hall theorem;
- the weighted one-link inequality unconditionally.

The global Hall argument must retain the full multivalued relation and cannot use DP to merge distinct-parent fibers. The p=q and p!=q classes both require the original Hall treatment.
