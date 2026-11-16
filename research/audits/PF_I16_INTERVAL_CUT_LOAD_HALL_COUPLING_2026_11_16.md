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


## Exact determinant / order-ideal formulation

There is an exact way to compute every right-hand Hall capacity without enumerating Prüfer codes. For (1\le i<j\le n), put
[
w_{ij}(x)=\prod_{k=i}^{j-1}x_k,
\qquad w_{ji}=w_{ij}.
]
Let (\mathcal L_n(x)) be the weighted Laplacian of the complete graph on the ordered ports, with off-diagonal entries (-w_{ij}(x)) and diagonal entries (\sum_{j\ne i}w_{ij}(x)). By the weighted Matrix-Tree Theorem,
[
\Phi_n(x_1,\ldots,x_{n-1})
=\det\bigl(\mathcal L_n(x)^{(n)}\bigr)
=\sum_{T\in\mathcal T(K_n)}\prod_{k=1}^{n-1}x_k^{c_k(T)}.
]
Thus, for a primitive path (h), define the cumulative tree count
[
A(h)=\#\{T:c(T)\le h\}
=\sum_{u\le h}[x^u]\Phi_n(x).
]
The ceiling-class counts are the poset Möbius inversion of these cumulative counts:
[
A(h)=\sum_{g\le h}Q(g),
\qquad
Q(h)=\sum_{g\le h}\mu(g,h)A(g),
]
where the order is coordinatewise on primitive Dyck paths and \(\mu\) is its incidence-algebra Möbius function. This identity is exact; it does not establish the desired lower bound on (Q).

There is also an exact formula for the supply of an arbitrary down-set (D). Let \(\operatorname{Max}(D)\) be its maximal paths and let \(\wedge S\) denote their coordinatewise meet. Since
[
\{T:c(T)\le h_1,\ldots,c(T)\le h_r\}
=\{T:c(T)\le h_1\wedge\cdots\wedge h_r\},
]
finite inclusion-exclusion gives
[
\boxed{
\sum_{h\in D}Q(h)
=
\sum_{\varnothing\ne S\subseteq\operatorname{Max}(D)}
(-1)^{|S|+1}A(\wedge S).
}
]
The meet remains primitive and belongs to (D), so every term is defined. Equivalently, the all-orders Hall problem is the family of determinant-count inequalities
[
\sum_{h\in D}L(h)
\le
\sum_{\varnothing\ne S\subseteq\operatorname{Max}(D)}
(-1)^{|S|+1}
\sum_{u\le\wedge S}[x^u]\Phi_n(x).
]
This is a finite, explicit algebraic criterion for each (n) and each down-set. It exposes the remaining challenge as a lower bound on a union of bounded-cutwidth tree classes against the interval-overlap spanning-tree demand. No inequality between these two sides has yet been proved uniformly in (n).

### Status of this refinement

- The determinant identity follows directly from weighted Matrix-Tree.
- The Möbius inversion follows from the definition of the least primitive majorant.
- The down-set inclusion-exclusion formula follows from the meet property and ordinary finite inclusion-exclusion.
- These are exact reformulations, not an all-orders Hall proof. In particular, cancellation in the inclusion-exclusion sum prevents replacing the union count by the sum of the individual (A(h)) without an additional argument.


## A sharper sufficient condition from the cumulative tree counts

The determinant formula gives a useful lower bound on each exact ceiling class without evaluating inclusion-exclusion. Recall

`A(h)=\sum_{g\le h}Q(g)`, hence
`Q(h)=A(h)-\sum_{g<h}Q(g)`.

Since every `Q(g)\le A(g)`, we obtain the rigorous estimate

```
Q(h) >= A(h) - sum_{g<h} A(g).
```

Consequently the following *strict-lower-ideal union-bound criterion* is sufficient for the desired pointwise coupling:

```
A(h) >= L(h) + sum_{g<h} A(g)       for every primitive h.       (UB)
```

This is not equivalent to pointwise domination and is stronger: it replaces the union of all lower principal tree classes by the sum of their sizes, allowing arbitrary overlap. Its advantage is that it reduces the exact-class problem to cumulative determinant counts only. No Möbius inversion or cancellation estimate is needed once (UB) is established.

The finite data through ten ports satisfy (UB). For compactness, the table reports the minimum margin
`A(h)-L(h)-sum_{g<h}A(g)` over all primitive paths at each size:

| n | number of primitive paths | minimum (UB) margin |
|---:|---:|---:|
| 4 | 1 | 1 |
| 6 | 2 | 5 |
| 8 | 5 | 19 |
| 10 | 14 | 65 |

At n=10, the margins path-by-path in lexicographic order are:
`65, 378, 378, 1932, 5211, 378, 2014, 1932, 7967, 18070, 5211, 18070, 16291, 39738`.
The corresponding cumulative counts `A(h)` are:
`81, 531, 531, 3363, 10485, 531, 3481, 3363, 20964, 64280, 10485, 64280, 205866, 442979`.

This identifies a concrete all-orders target:

```
det(L_n(x)^(n)) coefficient-sum below h
    >= L(h) + sum_{g<h} coefficient-sum below g.
```

A proof of this determinant-growth inequality would imply `Q(h)>=L(h)` by the displayed estimate, then the classwise injection, then all Hall inequalities, then the weighted one-link interval-tree inequality.

**Current status:** (UB) has only been checked at n=4,6,8,10. The key unresolved step is a uniform lower bound on the cumulative tree count `A(h)` relative to all strict lower paths and the interval-overlap demand. In particular, the positive finite margins do not yet yield a recurrence or an all-orders estimate. No closure is claimed.


## Injection attempt: rooted endpoint-doubling and its obstruction

A natural way to turn a spanning tree \(\tau\) of the interval-overlap graph into a tree on the \(2s\) ports is to root \(\tau\), retain the matched edge of the root interval, and, for each parent-child edge of \(\tau\), replace the child's matched edge by two endpoint links: left endpoint to left endpoint and right endpoint to right endpoint. The edge count is exactly
\[
1+2(s-1)=2s-1,
\]
and the resulting graph is a tree: it is two copies of the rooted \(\tau\)-tree joined by the root matched edge.

This construction is **not cut-load preserving**. The smallest transparent obstruction is the four-interval star on eight ports:
\[
M=\{(1,8),(2,3),(4,5),(6,7)\}.
\]
Its overlap graph is \(K_{1,3}\), so \(\tau=1\), and its matching cut-load is
\[
h=(1,2,1,2,1,2,1).
\]
Root at \((1,8)\). The endpoint-doubling tree has edges
\[
(1,8),(1,2),(8,3),(1,4),(8,5),(1,6),(8,7).
\]
At the cut between ports 3 and 4, six of these edges cross, whereas \(h_3=1\). Thus its cut-load is 6, exceeding the permitted load by 5.

This is not a minor choice-of-root issue: the long root interval is the only active matching interval at that cut, while endpoint doubling routes several child endpoints across it. Any successful injection must use a different port-tree encoding—one that reroutes/replaces edges so that every cut is charged at most once per active interval, while retaining enough information to recover both \(M\) and the overlap-tree copy.

The failed construction is recorded to prevent it being reused as a proof. It does not disprove the desired injection or the Hall inequality.


## Endpoint-leaf recurrence and complementary cut swap (2026-11-16 continuation)

This section records a further exact decomposition of the right-hand cumulative counts. It is independent of Prüfer-code enumeration.

For an arbitrary integer capacity vector b=(b_1,...,b_{n-1}), write
`A_n(b)=#{T in T(K_n): c_k(T)<=b_k for every k}`.
Set A_n(b)=0 if any b_k<1. If b_1=b_{n-1}=1, every admissible tree has vertices 1 and n as leaves. Let p in {2,...,n-1} be the neighbor of 1 and q in {2,...,n-1} the neighbor of n. Removing those leaves gives a unique tree T' on {2,...,n-1}. For its cut after old vertex k, the two deleted edges contribute respectively 1_{p>k} and 1_{q<=k}. Therefore, with
[
b^{p,q}_j=b_{j+1}-\mathbf1_{p>j+1}-\mathbf1_{q\le j+1},
qquad 1\le j\le n-3,
]
there is the exact recurrence
[
oxed{
A_n(b)=\sum_{p=2}^{n-1}\sum_{q=2}^{n-1} A_{n-2}(b^{p,q}).
}
	ag{EL}
]
Here the interior labels are relabeled in increasing order. A term with any capacity below 1 is zero. The identity is bijective: each tree has a unique ordered pair (p,q), and conversely any interior tree counted by A_{n-2}(b^{p,q}) becomes a unique admissible n-vertex tree after adjoining leaves 1 and n at p and q.

For a primitive Dyck path h, the hypotheses b_1=b_{n-1}=1 hold. Thus (EL) is an exact recursion for the determinant-derived cumulative count A(h), with no Möbius inversion. Its nonzero attachment pairs are precisely those satisfying, at every interior cut k,
[
h_k-\mathbf1_{p>k}-\mathbf1_{q\le k}\ge1.
]
Equivalently: at a height-1 cut neither leaf edge may cross; at a height-2 cut both may not cross; at a height-at-least-3 cut there is no further restriction.

As a check, for the minimal primitive path h_k=1 for odd k and 2 for even k, the only nonzero pairs are p in {2,3} and q in {n-2,n-1}. The exact recurrence terms obtained by exhaustive smaller-tree counts are:
- n=6: 2, 4, 1, 2; sum 9.
- n=8: 6, 12, 3, 6; sum 27.
- n=10: 18, 36, 9, 18; sum 81.

These agree with the minimal-ceiling class counts in the Prüfer verifier. They suggest a small boundary-state recursion for this extremal path, but the four terms are not yet evaluated by a proved closed recurrence for all n.

### A cut-complement identity relevant to an injection

Suppose a matching contains two distinct outer intervals [1,p] and [q,n] with q<p, so these two intervals overlap. Their contribution to its cut-load at k is
[
m^{outer}_k=\mathbf1_{k<p}+\mathbf1_{k\ge q}.
]
Instead attach the two tree leaves by edges {1,q} and {p,n}. Their contribution is
[
c^{leaf}_k=\mathbf1_{k<q}+\mathbf1_{k\ge p}.
]
A direct three-region check gives
[
m^{outer}_k-c^{leaf}_k=
\begin{cases}
2,&q\le k<p,\\
0,&k<q\text{ or }k\ge p.
\end{cases}
]
Thus this swap never increases any cut load and saves two units throughout the overlap region. It is exactly the type of complementary attachment pattern that the endpoint-leaf recurrence permits.

This is only a local cut identity. It does **not** yet define an injection from (M, spanning tree of H_M) to a port tree: the remaining interval-overlap tree must still be encoded into a tree on the interior ports, and connected matchings need not have their two endpoint intervals overlapping as a pair when other intervals bridge them. The outstanding task is to construct that interior encoding, or a more general boundary-state recursion that handles the bridged case, while preserving injectivity and the cut budget.

**Status:** (EL) and the cut-complement identity are proved. They give a new recursive representation of the right-hand supply and a concrete local edge-swap mechanism. They do not prove Q(h)>=L(h), the weighted one-link inequality, or the Yang--Mills mass gap.
