# PF-I16: tree-overlap sources as the conjectural terminal exchange class

Date: 2026-11-17

## 1. A closed-form characterization and count

Let M be a perfect matching on ordered ports [2s], and let H_M be its
interval-intersection graph: two matching intervals are adjacent when their
open interiors intersect. Sources are restricted to connected H_M.

Define
`K_{2s} = {(M,H_M): H_M is a tree}`.
For a source in this class the overlap tree is forced: there is exactly one
spanning tree of H_M, namely H_M itself.

There is an elementary endpoint-sweep characterization of this class.

Call a port an opening endpoint if it is the smaller endpoint of its matching
interval, and a closing endpoint if it is the larger endpoint. Sweep from
left to right, and let a live interval be one whose opening endpoint has
passed but whose closing endpoint has not.

If H_M is a tree:
- at most two intervals can be live at any cut, since three live intervals
  would pairwise intersect and give a triangle;
- at least one interval is live at every cut before the final endpoint,
  since otherwise the interval-intersection graph would be disconnected.

At port 1 the first interval opens. At port 2 a second interval must open:
closing the first would leave a gap and disconnect H_M. At port 3 an interval
must close: opening a third would create a triangle. Inductively, at every
even port 2j<2s a new interval opens, and at every odd port 2j+1 (j>=1) an
interval closes. The final port 2s closes the sole remaining live interval.

Conversely, any perfect matching with this endpoint-type word has exactly one
live interval immediately before each opening at an even port. The new interval
therefore intersects exactly that one earlier interval. Each new vertex of
H_M attaches by one edge to the existing connected graph, so H_M is a tree.

Thus the tree-overlap matchings are exactly those with endpoint-type word

`open, open, close, open, close, ..., open, close, close`.

At each of the s-1 nonfinal closing ports there are exactly two live intervals
to choose from; the final closing is forced. Hence the count is exactly

`|K_{2s}| = 2^{s-1}`.

This is an all-orders theorem about the *candidate terminal class*, not yet
about the exchange graph.

## 2. Finite identification with the terminal SCC

The diagnostic
`research/verification/verify_pf_i16_terminal_class_structure.py`
prints the actual terminal SCC sources for n=4,6,8. Its exact output is
recorded in workflow
[44050793751](https://github.com/syncgravity/Singular-Boundary/actions/runs/44050793751).

At each tested order the unique sink SCC consists of exactly one source for
each matching whose overlap graph is a tree:
- n=4: 2 sources, each with one overlap edge;
- n=6: 4 sources, each with a 3-vertex overlap tree;
- n=8: 8 sources, each with a 4-vertex overlap tree.

In particular the observed sink sizes 2,4,8 are not merely a numerical
sequence: they are exactly the number of connected interval matchings whose
overlap graph is itself a tree.

## 3. Sharpened all-orders conjecture

For the multivalued-pi relation R_n, conjecture that there is a left-saturating
matching mu_n such that:
1. K_{2s} is a strongly connected component of D_{mu_n};
2. K_{2s} is the unique sink SCC;
3. K_{2s} has at least one neighbor among unmatched target trees.

By the exact matching-relative identity
`|N(A)|-|A| = |F(A)| + |N_D^+(A)|`,
these three statements imply strict Hall expansion for every nonempty source
family, and hence Hall for R_n. The load-dominating edge property would then
give the weighted one-link inequality.

The conjecture is sharper than simply predicting a sink size. The endpoint
sweep proves the size and an intrinsic description of K_{2s}; the missing
part is the exchange structure of all other sources and a recursively
constructible matching.

## 4. A finite decomposition test

The new verifier
`research/verification/verify_pf_i16_tree_overlap_terminal_decomposition.py`
tests a useful sufficient construction. Let Y(K) be the union of targets
adjacent to K. If:
- the K-to-Y(K) graph has a matching saturating K; and
- the complementary sources have a matching using only targets outside Y(K),

then the union matching makes K closed in the matching-relative digraph.
If, in addition, K is strongly connected and has a free target neighbor, it
is the unique sink SCC.

This decomposition test is stronger than merely observing that an arbitrary
maximum matching happens to have K as its sink. It tests whether the terminal
class can be separated first and the remaining matching built outside its
entire neighborhood. Its workflow is
[44051839819](https://github.com/syncgravity/Singular-Boundary/actions/runs/44051839819)
and is still queued/running at the time of this note.

## 5. Proof boundary

The endpoint-sweep count is proved for every s. The identification of K_{2s}
as the unique terminal exchange class is verified only at n=4,6,8 so far.
The n=10 matching-relative SCC computation
[44048791345](https://github.com/syncgravity/Singular-Boundary/actions/runs/44048791345)
has not yet completed. No all-orders Hall theorem, weighted one-link
inequality, or Yang--Mills mass-gap proof is claimed.
