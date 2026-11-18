# PF-I16 source-dependent leaf-peeling audit — 2026-11-16

## Recursive source rule

For each source object (M,tau), root the overlap tree tau at the matching
interval containing port 1. Choose the lexicographically first non-root leaf
interval J. Delete J and its two endpoints, compress the remaining port labels
in order, and delete the leaf vertex from tau. This produces a parent source
p(x) on n-2 ports.

Restrict the guarded switch histories for x to parent-before-child orders in
which J is inserted last. Denote the resulting neighborhood by C_leaf(x).

For every T in C_leaf(x), the last switch can be reversed by searching pairs
u,v outside J such that the induced tree on {a,b,u,v}, where J={a,b}, is one
of the three local switch trees. Reverse the three local edges to uv, delete
a,b, and compress labels. The verifier checks that every inverse parent tree
belongs to C(p(x)), not merely that one guessed inverse does.

## Exact finite results

| Ports | Sources | Parent fibers | Leaf-last target union | Global matching |
|---:|---:|---:|---:|---:|
| 4 | 2 | 1 | 3 | 2/2 |
| 6 | 22 | 2 | 43 | 22/22 |
| 8 | 608 | 22 | 1,493 | 608/608 |

At all three orders:
- every source has a nonempty leaf-last neighborhood;
- every leaf-last output has at least one inverse;
- every inverse candidate is a valid output of the corresponding parent source;
- the full bipartite graph x~T iff T in C_leaf(x) has a matching
  saturating every source.

At eight ports, the leaf-last neighborhood is a strict subset of the full
all-orders neighborhood for 330 of 608 sources, omitting 13,385 source-target
incidences. Nevertheless its global matching still saturates all 608 sources.
This is evidence that source-dependent leaf deletion is useful; it is not an
all-orders proof.

## Why naive fiber induction fails

Parent-fiber sizes at eight ports range from 19 to 39. Matching each fiber
independently produces 397 repeated target trees across different fibers.
Also, no single parent target tree supports distinct lifts for every child
in any of the 22 fibers.

Thus the induction cannot assign one parent tree to a parent source and then
lift all its children independently. It needs a global exchange/rerouting
invariant across parent fibers.

## Uniform fractional transport still fails

Sending each source's unit mass uniformly over its distinct leaf-last outputs
has maximum target column loads:

| Ports | Maximum column load |
|---:|---:|
| 4 | 5/6 |
| 6 | 19/12 |
| 8 | 666095824449188291/186846825104503200 ~= 3.564929851372 |

So the finite source-saturating matching is genuinely using nonuniform
assignment; the uniform-neighborhood weighting is not a Hall certificate.

## Reproduction

Verifier:
research/verification/verify_pf_i16_source_dependent_leaf_peeling.py

CI:
https://github.com/syncgravity/Singular-Boundary/actions/runs/43974448818

Commit tested:
1d976e5bd1334a444fc23791d68f8076bf0aee69

The verifier reports the Hall matching as a finite exact result. It does not
assert an all-orders matching theorem. The unresolved obligation is a
constructive all-orders rerouting argument for the leaf-last relation, or a
structural characterization of its Hall neighborhoods. No Yang–Mills mass-gap
conclusion follows from these computations.


## Stronger inverse and assignment trace

The refined verifier establishes at n=4,6,8 that the inverse parent projection
is unique for every leaf-last child output: maximum inverse multiplicity is 1,
and no output has multiple parent projections. All 30,810 inverse candidates
at n=8 are valid parent-neighborhood trees (the run reports zero non-parent
inverse candidates).

Tracing the global matching through this unique projection gives:
- n=4: maximum assigned multiplicity of one (parent source, parent target)
  pair is 2; one such pair is used;
- n=6: maximum multiplicity 8; five pairs are used;
- n=8: maximum multiplicity 18; 157 pairs are used.

This identifies the recursive object more precisely: the parent assignment
must be a capacitated multiset of parent targets, not a single parent target
per parent source. The finite global child matching induces such a multiset,
but the verifier does not yet prove a general capacity bound or construct it
without solving the child matching problem.

Latest verifier commit:
378f7dc1f47a6c591000e268f87192293f97fb8e

Latest CI run:
https://github.com/syncgravity/Singular-Boundary/actions/runs/43974717402


## Structural inverse lemma

The verifier's final version no longer searches all pairs u,v. If J={a,b}
is inserted at the final step, all edges incident to a or b are among the
three local switch edges. For each of the three local trees, the union of
the neighbors of a and b, with a,b removed, is exactly the two endpoints
u,v of the old edge. Hence
\[
\{u,v\}=(N_T(a)\cup N_T(b))\setminus\{a,b\}.
\]
This recovers the old edge and the local four-vertex tree uniquely. Replacing
the local three edges by uv and deleting a,b is therefore a deterministic
inverse, not a multivalued projection.

The direct inverse verifier passed the complete n=4,6,8 CI suite:
https://github.com/syncgravity/Singular-Boundary/actions/runs/43974862779

Latest verifier commit:
c2baaaab83a29412ac5a82ef98ee962ff204db87
