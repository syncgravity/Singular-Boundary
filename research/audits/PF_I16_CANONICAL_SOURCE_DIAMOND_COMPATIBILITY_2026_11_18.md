# PF-I16: canonical source-level compatibility after the reverse-mark diamond

Date: 2026-11-18

Status: **exact relation criterion and next finite/theorem obligation; no canonical source-level diamond is claimed.**

## 1. Repository-grounded canonical rule

The controlling implementation is
`research/verification/verify_pf_i16_source_dependent_leaf_peeling.py`:

- `canonical_leaf(intervals, tau)` roots the overlap tree at the interval containing port 1, takes all non-root degree-one vertices, and chooses the lexicographically least interval among them.
- `parent_data(intervals, tau, leaf)` deletes the selected interval, compresses the remaining port labels, and deletes that leaf from the overlap tree.
- The canonical parent-target neighborhood is implemented by
  `candidate_outputs(parent_intervals, parent_tau, forced_last=canonical_leaf(...))`.
- The child-side multivalued-π verifier in
  `verify_pf_i16_n10_multivalued_pi_projection.py` retains a child target T for a leaf J exactly when its final-switch inverse, compressed after deleting J, belongs to that canonical parent-target neighborhood.

Thus the fiber incidence is not merely “J is a local reverse mark.” For F=(p,J),
[
T\in N(F)
\iff
J\text{ is a valid guarded reverse mark of }T
\quad\text{and}\quad
P_J(T)\in C_{\rm can}(p).
	ag{C1}
]

## 2. Exact candidate for a source-level diamond

Suppose two retained fibers F=(p,J) and G=(q,K) are incident to the same target T, and J,K are disjoint and mutually surviving in the target-side sense of the proved guarded diamond lemma.

The target-side theorem supplies a common twice-reversed target
[
U=P_K^{\,J}(P_J(T))=P_J^{\,K}(P_K(T)).
]

For this to be a **source-level** diamond over a common parent source r, the source projections must also agree:
[
K\text{ is a non-root leaf of }p,\qquad
J\text{ is a non-root leaf of }q,
]
[
\pi_K(p)=\pi_J(q)=r.
	ag{C2}
]
Here each π operation is the exact `parent_data` operation, including port compression and overlap-tree deletion. Condition (C2) says p and q are sibling source extensions of the same r. It is stronger than target-side mutual survival; the target theorem alone says nothing about matching intervals or overlap-tree source identity.

Even (C1) and (C2) do not, by themselves, state that U is in the canonical neighborhood of r. The remaining canonical diamond condition is
[
U\in C_{\rm can}(r).
	ag{C3}
]
This is the exact point that must be proved or checked. It is not enough that U is an all-orders output of r, nor that it has some valid reverse mark. The forced-last condition in the implementation is specific: the lexicographically least non-root leaf of r must be the final inserted interval in at least one construction of U.

## 3. What the target-side theorem contributes

The mutual-survival diamond lemma proves equality of the two target-side double inverses without requiring disjoint four-port supports. It therefore removes ambiguity in the target U once the two marks mutually survive.

It does not prove (C2) or (C3). In particular:

- local port-tree inverses do not identify the source matching or overlap tree;
- a valid target-side mark need not be a non-root leaf of the relevant parent overlap tree;
- even if the two parent-source projections agree, the common target U still has to satisfy the canonical forced-last condition for r.

## 4. Next exact test / proof obligation

Build the canonical source-diamond incidence table over small n:

1. enumerate source pairs p,q and candidate leaf intervals K,J;
2. retain exactly those with π_K(p)=π_J(q)=r;
3. require K=canonical_leaf(p) and J=canonical_leaf(q) as a first, sharply defined subcase; then broaden to noncanonical leaves only if justified;
4. intersect the canonical child target neighborhoods by target T;
5. retain pairs whose reverse marks are mutually surviving under the exact guarded inverse;
6. compute the common U from the proved target-side diamond and test U∈C_can(r).

The output should separate failures of source identity (C2), failures of target mutual survival, and failures of canonical membership (C3). Do not merge these into one “diamond failure” count.

A proof that (C3) holds for the relevant arbitrary source pairs would give the source-level bridge needed to use local reverse-mark diamonds in a fiber argument. A finite census alone would remain diagnostic and would not imply mixed-fiber Hall.

No all-orders Hall theorem or unconditional weighted one-link inequality is claimed.
