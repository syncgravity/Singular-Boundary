# PF-I16: first-overcrowded-cut decomposition

Date: 2026-11-17

## 1. Exact source-side characterization

For a matching M on 2s ordered ports, let
[
m_k(M)=|{[a,b]in M:ale k<b}|.
]
At cut k, exactly k endpoints have been encountered. Each interval contributes either zero or one live endpoint, so
[
m_k(M)equiv kpmod 2.
]
If H_M is connected, every cut is crossed by at least one interval, hence m_k>=1.

If m_k<=2 at every cut, parity and connectedness force
[
m_k=1quad(k	ext{ odd}),qquad m_k=2quad(k	ext{ even}).
]
The endpoint sweep then shows H_M is a tree. Conversely, if H_M is not a tree, some cut has m_k>=3. Since even-cut loads are even, the first such cut is necessarily odd.

Thus every source is in exactly one of:
- K_{2s}, the tree-overlap sources, with no overcrowded odd cut;
- X_k, the sources whose first odd cut with m_k>=3 is k, for odd k in {3,5,...,2s-3}.

This is an exact disjoint partition of the source set.

## 2. A corresponding target partition

For any port tree T, every cut has c_k(T)>=1. Define its first overloaded odd cut to be the first odd k with c_k(T)>=2. Then the target set partitions into:
- Q_{2s}, trees with c_k=1 at every odd cut;
- Y_k, trees whose first odd cut with c_k>=2 is k.

The earlier terminal-class result identifies Q_{2s} exactly and gives |Q_{2s}|=3^(s-1).

Because every edge in the guarded-switch relation is load-dominating, if x belongs to source class X_k, then any adjacent target T has c_j(T)=1 for every odd j<k. Therefore T is either in Y_k or in some later Y_l with l>k, or in Q. The load inequality alone does not force c_k(T)>=2.

A promising stronger decomposition would show that each source in X_k can be matched into Y_k. If true for every k, the classes would be disjoint on both sides and Hall could be proved independently on each block. The exact n=10 diagnostic is testing this statement.

## 3. n=12 source census

Verifier:
`research/verification/verify_pf_i16_n12_overcrowded_cut_census.py`

Successful workflow:
[44070581000](https://github.com/syncgravity/Singular-Boundary/actions/runs/44070581000)

Exact output:
- 10,395 perfect matchings;
- 2,692,064 connected source objects;
- 32 tree-overlap sources, agreeing with 2^(6-1);
- 2,692,032 complement sources;
- first-overcrowded-cut distribution:
  - k=3: 2,628,576;
  - k=5: 61,056;
  - k=7: 2,256;
  - k=9: 144.
- maximum live-interval-depth distribution:
  - depth 2: 32;
  - depth 3: 22,464;
  - depth 4: 423,648;
  - depth 5: 1,312,800;
  - depth 6: 933,120.

All 2,692,032 complementary sources have a first overcrowded odd cut. The first-overcrowded cut is a strong stratification: 97.64% of the complement sources first become overcrowded at cut 3.

## 4. Exact parity proof

At a cut k, the number of live intervals is the number of opening endpoints among the first k ports minus the number of closing endpoints among them. Since each of the first k ports is exactly one endpoint of the matching, the parity identity is `m_k ≡ k (mod 2)`.

For a connected interval-overlap graph, m_k cannot be zero: if no interval crosses cut k, no interval on the left can overlap an interval on the right, disconnecting H_M.

If no odd cut is overcrowded, then m_k=1 at every odd cut. For an even cut k, m_k is even and is adjacent to odd cuts k-1 and k+1, each with load one; changing one endpoint changes the live count by exactly one. Hence m_k=2. This is precisely the endpoint word of the tree-overlap class.

## 5. Proof boundary and next test

The n=12 census verifies the source-side partition but does not construct a matching. The desired next lemma is a cut-preserving matching statement:
[
|N_{R_{2s}}(A)|ge |A|
quad	ext{for every }Asubseteq X_k,
]
with neighborhoods restricted to Y_k.

The first-overcrowded-cut partition verifier
`research/verification/verify_pf_i16_first_overcrowded_cut_partition_n10.py`
is being run through the n=10 multivalued-pi exchange workflow. It tests the necessary preliminary condition that every source in X_k has at least one allowed target in Y_k. Even if this passes, it is only a row-support test, not Hall on each block. If it fails, the first-overcrowded cut still gives a valid source partition but cannot be used as a same-k block decomposition without a more flexible rerouting argument.

No all-orders complement Hall theorem is claimed here.


## 6. Local cut-preserving lifting lemma

The first-overcrowded-cut partition is compatible with the final guarded switch. This gives an all-orders row-support statement, not just a finite observation.

Fix a child source x in X_k, and choose any non-root leaf interval J. Let p=pi_J(x), and let P be a canonical parent target for p. Let k' be the parent cut corresponding to child cut k.

There are two cases.

### J does not cross k

Both endpoints of J lie on the same side of k. Deleting them preserves the number of matching intervals crossing the corresponding cut, and preserves the first-overcrowded odd cut after the obvious relabeling:
- if J lies left of k, the parent first-overcrowded cut is k-2;
- if J lies right of k, it is k.

By induction, choose P in the corresponding parent target class, so c_{k'}(P)>=2. The guarded final switch replaces an admissible edge e overlapping J by a three-edge local tree. Since J lies on one side of the cut, either e also lies on that side (zero crossing edges are replaced by zero) or e crosses the cut (exactly one crossing edge is replaced by exactly one). Thus c_k is preserved. The child target remains in Y_k.

### J crosses k

Every parent port tree P has at least one edge crossing the corresponding parent cut. If an admissible crossing edge e is not contained strictly inside J, the four endpoints of e and J are either interleaved or J is nested inside e. In either case a guarded middle-centered star survives and replaces one crossing edge by two, increasing the cut crossing count by one.

If every crossing edge of P is contained strictly inside J, use the guaranteed no-reinsertion witness edge e from the connected-tree switch lemma. It is not contained inside J and cannot cross k under this assumption. Since it overlaps J, its endpoints lie on one side of k; the local switch then introduces exactly one crossing edge while leaving the existing crossing edges untouched. Again c_k increases from at least one to at least two.

Therefore there is always a guarded final switch producing a child target in Y_k.

The inverse final switch is unique for fixed J. Distinct parent targets therefore have disjoint lift sets. The parent canonical neighborhood has at least `2^(s-2)` targets. In the noncrossing case, the induction hypothesis supplies at least `2^(s-3)` parent targets in the corresponding class Y_{k'}; each has at least two guarded lifts preserving the class. This gives at least `2^(s-2)` child targets in Y_k. In the crossing case, every parent target has at least one guarded lift entering Y_k, so the full parent neighborhood gives at least `2^(s-2)` child targets. Consequently every source has at least `2^(s-2)` distinct same-class targets:
`|N_R(x) ∩ Y_k| ≥ 2^(s−2)`.

For s>=3 this is at least s-1, the maximum number of child sources in a fixed (parent,J) fiber. Thus every fixed fiber has local Hall within its matching first-overcrowded-cut block.

This proves the all-orders row-support statement: every source x in X_k has at least one neighbor in Y_k, and in fact the stated lower bound on its same-k neighborhood. It does not say that every edge out of X_k lands in Y_k; load domination only rules out target classes earlier than k. It does NOT prove Hall for arbitrary unions of different fixed-(parent,J) fibers inside X_k. Those neighborhoods can still collide, and the global capacity problem remains.

The verifier `verify_pf_i16_first_overcrowded_cut_partition_n10.py` tests the row-support statement in the actual finite n=10 multivalued-pi relation. The verifier `verify_pf_i16_overcrowded_cut_split_transport.py` tests whether split-demand uniform transport now has column loads at most one after restricting to Y_k. These are finite diagnostics of the stronger quotient condition; they do not replace the local proof above or establish the global quotient inequality.


## 7. Exhaustive n=10 same-cut row-support result

The first-overcrowded-cut partition diagnostic completed successfully in workflow [44073281842](https://github.com/syncgravity/Singular-Boundary/actions/runs/44073281842), job 134004657248.

Exact output:
- 31,744 total sources; 31,728 complement sources.
- 95,864 target trees in the multivalued-pi relation.
- Source classes: X_3 has 30,528 sources; X_5 has 1,128; X_7 has 72.
- Same-cut target support: 31,728/31,728 sources.
- No source lacked a target in its own Y_k block.
- The target incidence totals restricted to same-cut classes were 30,528 for Y_3, 22,002 for Y_5, and 4,708 for Y_7.

The source degree sums in the same-cut restricted relation were 15,625,852 (k=3), 202,364 (k=5), and 5,400 (k=7).

The diagnostic's second step (uniform split-demand transport) failed before executing its mathematics because the terminal class None was sorted with integer cut labels. The sort was corrected in commit 60a042fe9488e4686712c5059bffc16916ef1e8f. This is a reporting correction, not a failed transport result.

The exact nonuniform split-demand max-flow test is separately running in [44078442710](https://github.com/syncgravity/Singular-Boundary/actions/runs/44078442710).
