# PF-I16 weighted interval cut-load Hall coupling: exact finite audit (2026-11-16)

## Status

The coordinatewise cut-load coupling proposed for the one-link weighted interval-tree inequality passes an exact capacitated Hall test for 4, 6, and 8 ordered ports. This is a finite regression result, not an all-orders theorem. The coupling is sufficient for the weighted inequality, not known to be necessary.

## Definitions

Let n=2s, and let M be a perfect matching of {1,...,n}. Its interval-overlap graph H_M has one vertex for each matched interval [a,b], with an edge when the open interiors intersect. Retain only connected H_M, and let

m_k(M)=#{(a,b) in M: a<=k<b}, 1<=k<n.

For each matching M, put tau(H_M) copies of its vector m(M) into a left multiset. Thus the left multiplicity of a load vector v is

L(v)=sum_{M:H_M connected, m(M)=v} tau(H_M).

For a labeled spanning tree T of K_n, define

c_k(T)=#{ {i,j} in T: i<=k<j }.

Put one copy of c(T) into the right multiset. Its load-vector multiplicity is

R(u)=#{T in T(K_n): c(T)=u}.

A matching of left copies to distinct right trees with c(T)<=m(M) coordinatewise would imply the polynomial comparison, because x_k in [0,1] gives

prod_k x_k^{c_k(T)} >= prod_k x_k^{m_k(M)}.


## Structural reduction: the left types are primitive Dyck paths

Write h_0=0, h_k=m_k(M) for 1<=k<n, and h_n=0. At port k, the height changes by +1 if k is the smaller endpoint of its matched pair and by -1 if it is the larger endpoint. Hence h is a Dyck path of semilength s. The interval-overlap graph is connected exactly when no intermediate cut is empty, i.e. h_k>=1 for every 1<=k<n. Thus the left load-vector types are precisely the primitive (irreducible) Dyck paths of semilength s; there are Catalan_{s-1} such types.

For a fixed primitive Dyck path h, its unweighted number of compatible perfect matchings is
`prod_{down steps D} height_before(D)`,
because each down step closes one of the currently open left endpoints. The actual Hall demand L(h) is the sum of tau(H_M) over these matchings, so it is a weighted refinement of this simple product.

As an exploratory left-side extension, exact enumeration at n=10 finds 706 connected matchings, 14 primitive-Dyck load types, and total left multiplicity 31,744. This is not an n=10 Hall test: the verifier deliberately stops at n=8 because direct Prüfer enumeration of all 10^8 labeled trees is not a reasonable CI regression.

This Dyck-path identification narrows the all-orders problem: prove the Hall inequalities for primitive Dyck-path types against the cut-load distribution of labeled trees. It does not yet provide those inequalities.

## Exact Hall criterion

Compress the bipartite graph by load-vector types. A left type v is adjacent to a right type u exactly when u<=v coordinatewise. For every nonempty set S of left load types, Hall's capacitated condition is

sum_{v in S} L(v) <= sum_{u in union_{v in S}{u:u<=v}} R(u).

The verifier checks every nonempty subset of the (small) set of left load types, and counts all labeled spanning trees on the right by Prüfer codes. All multiplicities and Hall slacks are integers. The interval-overlap spanning-tree multiplicities are computed by the exact Matrix-Tree determinant using fraction-free Bareiss elimination.

## Results

| Ports n | Connected matchings | Left copies | Left load types | Labeled trees | Right load types | Minimum Hall slack |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 2 | 2 | 1 | 16 | 13 | 1 |
| 6 | 10 | 22 | 2 | 1,296 | 383 | 5 |
| 8 | 74 | 608 | 5 | 262,144 | 15,165 | 19 |

The left multiplicities at eight ports are:

- (1,2,1,2,1,2,1) -> 8
- (1,2,1,2,3,2,1) -> 36
- (1,2,3,2,1,2,1) -> 36
- (1,2,3,2,3,2,1) -> 144
- (1,2,3,4,3,2,1) -> 384

The positive minimum Hall slack means every subset of left load types has enough right-neighborhood capacity in these finite cases.

## Reproduction

Run:

    python research/verification/verify_pf_i16_interval_cut_load_hall.py

The verifier is standard-library-only and exhaustively checks n=4,6,8. The n=8 right side enumerates all 8^6=262,144 Prüfer codes.

## What remains open

1. Prove the capacitated Hall inequalities for arbitrary even n, preferably by a structural description of the downward neighborhoods of the left load vectors.
2. Alternatively, construct the matching directly, assigning each of the tau(H_M) copies of every connected interval matching to a distinct labeled spanning tree with no larger cut load.
3. If this coupling is established, it proves the weighted one-link tau(H_M)-majorant. It still does not by itself solve the multi-link gluing/multiplicity problem or close the Yang-Mills mass-gap argument.

No all-orders coupling, weighted interval-tree inequality, or mass-gap proof is claimed here.
