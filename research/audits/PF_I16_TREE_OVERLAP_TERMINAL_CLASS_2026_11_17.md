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
entire neighborhood. Its exact successful workflow is
[44051839819](https://github.com/syncgravity/Singular-Boundary/actions/runs/44051839819).
It passes at n=4,6,8:

| n | all sources | |K_n| | all targets | |N(K_n)| | complement matching |
|---:|---:|---:|---:|---:|---:|
| 4 | 2 | 2 | 3 | 3 | 0/0 |
| 6 | 22 | 4 | 43 | 9 | 18/18 |
| 8 | 608 | 8 | 1,493 | 27 | 600/600 |

At each order, K_n itself has a saturating matching into N(K_n), and the
complementary sources have a saturating matching using only targets outside
N(K_n). Their union is therefore a full source-saturating matching with no
exchange arc from K_n to an outside source. The computed full exchange
digraph has respectively 1, 2, and 4 SCCs; its unique sink is exactly K_n,
with 1, 5, and 19 free target neighbors. K_n is strongly connected at all
three orders.

This is a stronger finite result than merely observing that a maximum
matching happens to have K_n as its sink: it verifies the *separable
matching* construction directly.

## 5. Proof boundary

The endpoint-sweep count is proved for every s. The identification of K_{2s}
as the unique terminal exchange class is verified only at n=4,6,8 so far.
The n=10 matching-relative SCC computation
[44048791345](https://github.com/syncgravity/Singular-Boundary/actions/runs/44048791345)
has not yet completed. No all-orders Hall theorem, weighted one-link
inequality, or Yang--Mills mass-gap proof is claimed.


## 6. The matching-load boundary profile and its target class

Every source in K_{2s} has the same matching load
[
h_k^*=
\begin{cases}
1,&k\text{ odd},\\
2,&k\text{ even}.
\end{cases}
]
This is exactly the live-interval pattern in the endpoint-sweep proof.

Define the target class
[
Q_{2s}=\{T\in\mathcal T(K_{2s}):c_k(T)\le h_k^*\text{ for every }k\}.
]
Since a spanning tree crosses every cut at least once, its odd-cut loads in Q are
exactly one.

There is a second all-orders count:
[
|Q_{2s}|=3^{s-1}.
]
To see this, take the unique path P in T from port 1 to port 2s. At every odd
cut P must use the unique crossing edge. Any edge not on P therefore cannot
cross an odd cut; its endpoints must lie in one adjacent pair
({2j,2j+1}). At least one vertex of each such pair lies on P, and there
are exactly three possibilities:
1. both vertices lie on P and are joined by their pair edge;
2. only 2j lies on P, with 2j+1 attached as a leaf;
3. only 2j+1 lies on P, with 2j attached as a leaf.

These independent three-state choices determine P and all off-path edges,
and every sequence of choices gives a tree in Q. Hence |Q|=3^(s-1).

Because every edge of R_n is load-dominating, every neighbor of K_{2s} lies
in Q_{2s}. Thus
[
N_{R_n}(K_{2s})\subseteq Q_{2s}.
]
The finite computations give equality at n=4,6,8: the respective target
neighborhood sizes are 3,9,27, exactly 3^(s-1). The K-only neighborhood
census, including n=10, is running as
[44052220966](https://github.com/syncgravity/Singular-Boundary/actions/runs/44052220966).

## 7. Hall on the terminal class is already an all-orders consequence

For any x in K_{2s}, choose any non-root leaf interval J of its overlap tree.
Deleting J leaves a parent source in K_{2s-2}. The canonical parent
neighborhood has at least 2^(s-2) distinct targets by the guarded-switch
witness lemma. For each such parent target, insertion of J has at least two
guarded local lifts; the inverse final switch is unique for fixed J, so lifts
of distinct parent targets are disjoint. All these lifts belong to R_n(x).
Therefore
[
|R_n(x)|\ge 2\cdot2^{s-2}=2^{s-1}=|K_{2s}|.
]
For every nonempty A subset K_{2s}, choose x in A. Then
[
|N_{R_n}(A)|\ge|R_n(x)|\ge|K_{2s}|\ge|A|.
]
So Hall holds on the entire terminal class K_{2s} for every s, without a
matching computation.

This is an important reduction: the unresolved part is entirely the
complement. The separable finite matching test asks for a matching of
(X_{2s}\setminus K_{2s}) into (Y_{2s}\setminus Q_{2s}). It succeeds at
n=4,6,8, with complement sizes 0,18,600 respectively. Proving this
complement Hall statement (or a suitable recursive replacement for it) is
now the central remaining combinatorial task.
