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


## Structural Hall reduction by the primitive-Dyck-path lattice

A matching load vector is a Dyck path: at port k the height rises when k is the left endpoint of its matched interval and falls when k is the right endpoint. Connectedness of the interval-overlap graph is equivalent to positive height at every interior cut. Thus the left types are exactly the primitive Dyck paths of semilength n/2.

The primitive Dyck paths form a meet-semilattice under coordinatewise minimum. To see this, all paths have the same parity at each fixed time. If two heights differ at time k, they differ by at least two; since each path changes by one at the next step, their pointwise minimum also changes by exactly one. Positivity and the zero endpoints are preserved. In particular, for any tree cut-load vector c that is dominated by at least one primitive path, there is a unique least primitive majorant

`\widehat c=\bigwedge\{h\in\mathcal P_n:c\le h\}`.

Let Q(h) be the number of labeled spanning trees whose least primitive majorant is h. A tree is adjacent to a left load type h exactly when `\widehat c(T)\le h`. Trees not dominated by the maximal primitive path `h^{max}_k=\min(k,n-k)` have no left neighbors and can be discarded.

Consequently the Hall graph is the order relation on one finite poset: left mass L(h), right mass Q(h), and an edge from right type u to left type h exactly when u<=h. Its capacitated Hall condition is therefore equivalent to the order-ideal inequalities

`\boxed{\sum_{h\in D}L(h)\le\sum_{h\in D}Q(h)\quad\text{for every down-set }D\subseteq\mathcal P_n.}`

Proof of equivalence: for arbitrary left subset S, its right neighborhood is the right mass on the down-closure `\downarrow S`, while `L(S)\le L(\downarrow S)`. Thus all down-set inequalities imply Hall. Conversely, taking S itself to be a down-set gives its own down-set as neighborhood, so Hall implies the inequalities.

### Stronger pointwise sufficient condition

A particularly simple sufficient condition is

`\boxed{Q(h)\ge L(h)\quad\text{for every primitive Dyck path }h.}`

If this holds, assign the L(h) left copies at h to distinct trees in the same least-majorant class h. Every such tree has cut load c(T)<=h, so this is an explicit classwise Hall coupling. Pointwise domination is stronger than the order-ideal Hall inequalities; it is a candidate theorem, not established in general.

The verifier now checks this stronger condition as well as the original exhaustive Hall test. Exact data:

| n | Primitive paths | Left L(h) values | Same-ceiling tree counts Q(h) |
|---:|---:|---|---|
| 4 | 1 | 2 | 3 |
| 6 | 2 | 4, 18 | 9, 50 |
| 8 | 5 | 8, 36, 36, 144, 384 | 27, 150, 150, 794, 2,374 |

For n=8 the paths are ordered lexicographically as in the verifier output. The pointwise inequalities hold in all these cases. This finite pattern is evidence only; no formula or all-orders lower bound for Q(h) has yet been proved.

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


### Ten-port exhaustive extension

The C++ verifier `research/verification/verify_pf_i16_interval_cut_load_hall_n10.cpp` exhausts the right-hand trees that can possibly have a left neighbor. Since every left path has first and last cut height 1, any neighboring tree must have vertices 1 and 10 as leaves. In Prüfer coordinates those two labels are absent, so it is enough to enumerate exactly `8^8 = 16,777,216` codes rather than all `10^8` labeled trees. Every such code is decoded, its nine cut loads are computed, and it is retained precisely when they lie below the maximal primitive path `(1,2,3,4,5,4,3,2,1)`. The least primitive majorant is then found by taking the coordinatewise meet of all primitive majorants.

The same C++ verifier independently enumerates all 945 perfect matchings, computes each interval-overlap spanning-tree count by an exact Bareiss Matrix-Tree determinant, and compares the left and right ceiling-class multiplicities.

Exact result:

- Connected interval matchings: 706.
- Primitive Dyck paths: 14.
- Left copies: 31,744.
- Relevant labeled trees: 442,979.
- Trees excluded because they have no left neighbor: 16,334,237.
- Pointwise `Q(h)>=L(h)` holds for all 14 paths.

In lexicographic primitive-path order, the left and right class multiplicities are:

| Primitive path h | L(h) | Q(h) |
|---|---:|---:|
| (1,2,1,2,1,2,1,2,1) | 16 | 81 |
| (1,2,1,2,1,2,3,2,1) | 72 | 450 |
| (1,2,1,2,3,2,1,2,1) | 72 | 450 |
| (1,2,1,2,3,2,3,2,1) | 288 | 2,382 |
| (1,2,1,2,3,4,3,2,1) | 768 | 7,122 |
| (1,2,3,2,1,2,1,2,1) | 72 | 450 |
| (1,2,3,2,1,2,3,2,1) | 324 | 2,500 |
| (1,2,3,2,3,2,1,2,1) | 288 | 2,382 |
| (1,2,3,2,3,2,3,2,1) | 1,116 | 12,269 |
| (1,2,3,2,3,4,3,2,1) | 2,880 | 36,194 |
| (1,2,3,4,3,2,1,2,1) | 768 | 7,122 |
| (1,2,3,4,3,2,3,2,1) | 2,880 | 36,194 |
| (1,2,3,4,3,4,3,2,1) | 7,200 | 98,270 |
| (1,2,3,4,5,4,3,2,1) | 15,000 | 237,113 |

This remains an exact finite regression, not a proof of pointwise domination for all semilengths. The C++ verifier is wired into theorem-index CI.
