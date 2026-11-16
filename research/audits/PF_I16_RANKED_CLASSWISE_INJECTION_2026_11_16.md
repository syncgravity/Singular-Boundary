# PF-I16 ranked classwise injection: explicit conditional construction (2026-11-16)

## Purpose and status

This note makes the finite-poset Hall reduction into a deterministic, fully specified injection **conditional on** the strict-lower-ideal union-bound (UB). It is a genuine algorithm for producing and inverting the port tree once the required cardinality inequality is known. It is not a structural all-orders proof of (UB), and it does not close the one-link weighted inequality.

The distinction matters: a ranking construction is not a substitute for proving that every ceiling class contains enough trees. It does, however, isolate the only remaining numerical input and removes any ambiguity about how the injection is realized after that input is proved.

## Objects and canonical orders

Fix n=2s and a primitive Dyck path h.

A left object of type h is a pair (M,tau), where:
- M is a perfect matching of the ordered ports with connected interval-overlap graph H_M and cut-load m(M)=h;
- tau is a labeled spanning tree of H_M.

Its total number is exactly L(h).

Use the following canonical total order on left objects:
1. Encode M by its partner word (p_1,...,p_n), where p_i is the unique port matched to i; order these words lexicographically.
2. For a fixed M, encode tau by the lexicographically ordered list of its unordered vertex-pairs, with interval vertices ordered by their left endpoints; order these lists lexicographically.

A right object of type h is a labeled spanning tree T of K_n whose least primitive majorant satisfies widehat c(T)=h. Its total number is Q(h).

Use the canonical total order on right objects given by the lexicographic order of their Prüfer words (with the standard smallest-leaf decoding convention).

Let
L_h[1],...,L_h[L(h)] and R_h[1],...,R_h[Q(h)] denote these ordered lists.

## The ranked injection

If Q(h)>=L(h) for every primitive h, define
[
oxed{\quad \iota(M,\tau)=R_h[k]\quad}
]
where h=m(M) and k is the rank of (M,tau) in the left list L_h.

This is a deterministic injection:
- **Cut-load domination:** by definition of the least primitive majorant, every T in R_h has c(T)<=h=m(M).
- **Injectivity within a type:** distinct left objects have distinct ranks k, hence distinct right trees.
- **Injectivity across types:** the least primitive majorant of T is unique, so right classes R_h are disjoint.
- **Explicit inverse on the image:** given T, compute c(T), then its least primitive majorant h; compute its Prüfer rank k within R_h; return L_h[k].

Thus this is not merely an existence statement from Hall: it is an explicit rank/unrank algorithm, with finite enumeration as its implementation.

## A cumulative-count criterion that guarantees the injection

Let
[
A(h)=\#\{T:c(T)\le h\}=\sum_{g\le h}Q(g).
]
Since Q(g)<=A(g),
[
Q(h)=A(h)-\sum_{g<h}Q(g)
\ge A(h)-\sum_{g<h}A(g).
]
Therefore it is sufficient that
[
\boxed{A(h)\ge L(h)+\sum_{g<h}A(g)\qquad(\mathrm{UB})}
]
for every primitive h.

The weighted Matrix-Tree identity computes A(h) exactly:
[
A(h)=\sum_{u\le h}[x^u]\det(\mathcal L_n(x)^{(n)}),
\qquad
w_{ij}(x)=\prod_{k=i}^{j-1}x_k.
]
So a proof of (UB) supplies the missing cardinality bound and the ranked injection immediately follows.

## Verified finite range

The repository's exact checks establish pointwise Q(h)>=L(h), and the stronger (UB), for n=4,6,8,10. The n=10 C++ exhaustive verifier enumerates all 8^8 Prüfer words that can have a left neighbor, all 945 perfect matchings, and exact interval-overlap tree counts. The associated CI run completed successfully:
https://github.com/syncgravity/Singular-Boundary/actions/runs/43809756875

These are finite exact checks only. The rank construction is executable at each fixed n, but no uniform proof of (UB), Q(h)>=L(h), or the original weighted inequality is known.

## What the structural construction still needs

The next mathematical task is no longer to guess how to decode an injection. It is to prove (UB) by a uniform comparison of:
- the cumulative number A(h) of labeled port trees whose cut-load lies below h; and
- the interval-overlap tree demand L(h), together with the strict-lower cumulative counts.

A useful proof would likely need a direct family of trees counted by A(h), organized so that its members can be separated into disjoint rank blocks for all strict lower paths and at least L(h) additional trees of exact ceiling h. The current endpoint-doubling map does not provide such a family and is ruled out by the recorded eight-port cut obstruction.

No all-orders injection or Yang-Mills mass-gap proof is claimed.
