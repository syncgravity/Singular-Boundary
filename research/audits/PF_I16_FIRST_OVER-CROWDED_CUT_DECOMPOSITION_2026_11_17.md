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

At a cut k, the number of live intervals is the number of opening endpoints among the first k ports minus the number of closing endpoints among them. Since each of the first k ports is exactly one endpoint of the matching,
[
m_kequiv kpmod 2.
]
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
