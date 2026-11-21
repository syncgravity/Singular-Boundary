# PF-I16: blockwise split-demand Hall reduction by first overcrowded cut

Date: 2026-11-17

## Status

**Proved reduction; finite verification at 8 and 10 ports; all-orders blockwise Hall remains open.**

This note isolates the next proof obligation after the exact parent-canonical split-demand flow. It uses the first-overcrowded-cut partition to eliminate all cross-class target collisions. The remaining problem is entirely within one cut block.

## 1. Source and target partitions

Let (n=2s). Let (K_{2s}) be the tree-overlap terminal source class. For every odd
(kin{3,5,ldots,2s-3}), let (X_k) be the sources whose first odd cut with matching load at least three is (k).

Partition target trees into (Q_{2s}), those with exactly one edge crossing every odd cut, and (Y_k), those whose first odd cut with at least two crossing edges is (k).

These are disjoint partitions:
[
X_{2s}=K_{2s}sqcupcoprod_k X_k,
qquad
mathcal T(K_{2s})=Q_{2s}sqcupcoprod_kY_k.
]
The terminal-class theorem gives Hall from (K_{2s}) into (Q_{2s}) for every order.

For a source (xin X_k), every edge of the guarded-switch relation has target first-overcrowded odd cut at least (k), by coordinatewise load domination. More strongly, the cut-preserving lifting theorem proves
[
|N_R(x)cap Y_k|ge 2^{s-2}.
	ag{1}
]
Thus every complementary source has same-block support, and every fixed parent/deleted-interval fiber has Hall when restricted to its own (Y_k). This is local support/Hall, not Hall for unions of fibers.

## 2. Split-demand quotient inside one block

For a child source (x=(M,\tau)), let (d(x)) be its number of non-root leaves. Each non-root leaf (J) determines a parent source (p=\pi_J(x)) and a fiber (F=(p,J)). Put
[
\delta(F)=\sum_{x\in F}\frac1{d(x)}.
]
As before, each source contributes total demand one across its leaf fibers.

For a fiber in block (k), let
[
N_k(F)=N_R(F)\cap Y_k,
]
where (N_R(F)) is its common parent-canonical multivalued-\(\pi\) target row.

The blockwise quotient Hall condition is
[
\boxed{
\left|\bigcup_{F\in S}N_k(F)\right|
\ge \sum_{F\in S}\delta(F)
\quad\text{for every family }S\text{ of fibers in block }k.
}
\tag{BQH_k}
]

For any source family (A\subseteq X_k), let (S(A)) be all fibers touched by its sources. Each (x\in A) contributes total split demand one to (S(A)), so
[
|A|\le\sum_{F\in S(A)}\delta(F).
]
Also (N_R(A)\cap Y_k=\bigcup_{F\in S(A)}N_k(F)). Hence (BQH_k) implies
[
|N_R(A)\cap Y_k|\ge|A|.
]
This proves Hall for the entire source block (X_k), not merely for individual fibers.

## 3. Blockwise Hall implies full Hall

Assume (BQH_k) for every odd (k), and use the already-proved terminal-class Hall theorem
[
|N_R(A_0)\cap Q_{2s}|\ge|A_0|
\quad(A_0\subseteq K_{2s}).
]

Take an arbitrary source family
[
A=A_0\sqcup\coprod_k A_k,
\quad A_0\subseteq K_{2s},\quad A_k\subseteq X_k.
]
For each block, the previous section gives at least (|A_k|) neighbors in (Y_k); the terminal theorem gives at least (|A_0|) neighbors in (Q_{2s}). Since (Q_{2s}) and the (Y_k)'s are pairwise disjoint,
[
|N_R(A)|
\ge |N_R(A_0)\cap Q_{2s}|+
\sum_k|N_R(A_k)\cap Y_k|
\ge |A_0|+\sum_k|A_k|=|A|.
]
Therefore:
[
oxed{
\left[\text{all blockwise }(BQH_k)\right]
+\left[\text{terminal-class Hall}\right]
\Longrightarrow
\left[\text{full multivalued-}\pi\text{ Hall}\right].
}
\tag{2}
]

This is a rigorous reduction. It does not assume that all edges from (X_k) land in (Y_k); it uses only the same-block subrelation, whose target classes are disjoint across (k).

## 4. Exact finite evidence for the blockwise quotient

The same-cut max-flow verifier is
`research/verification/verify_pf_i16_overcrowded_cut_split_maxflow.py`.
It constructs the intended parent-canonical rows by reversing the final switch at (J), checking membership in (C_{\rm can}(p)), and then retaining only targets whose first overloaded odd cut is the source block (k).

Successful run: [44078442710](https://github.com/syncgravity/Singular-Boundary/actions/runs/44078442710), job 134022421678, checked-out commit `74413140a5867bd8533dd0a2a8a753f9b68a1422`.

Exact job output:
- (n=8): 564 sources in (X_3), 36 in (X_5), 424 fibers, 1,458 targets in the same-cut rows, scaled demand (7,200), max flow (7,200/7,200).
- (n=10): 30,528 sources in (X_3), 1,128 in (X_5), 72 in (X_7), 21,240 fibers, 95,125 targets in the same-cut rows, scaled demand (380,736), max flow (380,736/380,736).

The scale is 12, which clears all source split-demand denominators at these orders. These exact integral flows establish (BQH_k) for every fiber subfamily in each tested block at (n=8,10). They are finite-order results. The earlier full parent-canonical quotient flow independently verifies the unrestricted (across all source blocks) quotient at (n=6,8,10).

## 5. What this does and does not solve

**Proved all orders**
- The source/target first-overcrowded-cut partitions.
- Terminal-class Hall.
- Same-block row support and the lower bound (1).
- Hall within every single fixed parent/deleted-interval fiber.
- The implication (2): blockwise quotient Hall plus terminal Hall implies full Hall.

**Verified finite orders**
- Full parent-canonical split-demand quotient Hall at (n=6,8,10).
- Same-cut blockwise split-demand quotient Hall at (n=8,10), with the exact flows above.

**Open**
- Prove (BQH_k) for arbitrary (s), every odd (k), and every fiber family (S) in that block.
- Equivalently, find an all-orders capacity-sensitive allocation within each same-cut target class.

The local lower bound (2^{s-2}) does not by itself imply (BQH_k): many different fibers can share targets. Nor does the finite max-flow success give an all-orders bound.

## 6. Next proof obligation

The next structural lemma should be cut-local and parent-recursive:

For each (k), control the union of same-cut lifts of an arbitrary family of parent/leaf fibers by the sum of their split demands. A useful proof must simultaneously account for:
1. the case where the inserted interval (J) lies entirely to one side of (k), in which the parent first-overcrowded cut is inherited after relabeling and at least two guarded lifts preserve the cut class;
2. the case where (J) crosses (k), in which at least one guarded lift enters (Y_k), but the parent source need not belong to a corresponding first-overcrowded block;
3. collisions between different (J)'s and different parent sources, which are not controlled by the fixed-fiber inverse uniqueness lemma.

The crossing case is the obstruction to a naive induction on the same (k)-block. Any all-orders proof must handle it explicitly rather than silently treating every parent as a member of (X_{k'}).

No all-orders complement Hall theorem, weighted one-link inequality, or Yang--Mills mass-gap proof is claimed here.
