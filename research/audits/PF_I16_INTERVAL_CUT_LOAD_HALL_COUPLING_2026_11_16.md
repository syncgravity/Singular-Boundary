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


### Exact left demand on the minimal primitive path

There is also a closed formula for the left mass at the minimal primitive path
[
h^{min}_k=\begin{cases}1&k\text{ odd},\\2&k\text{ even},\end{cases}
\qquad 1\le k<n.
]
Its Dyck word is (UUD(UD)^{s-2}D). At each of the (s-1) down-steps at odd positions (3,5,\ldots,2s-1), there are exactly two currently open left endpoints to close; the final down-step has only one choice. Hence there are exactly (2^{s-1}) compatible matchings.

For each such matching, exactly one matched interval crosses every odd cut and exactly two cross every even interior cut. Every edge of the interval-overlap graph is witnessed by a common crossing cut, which therefore must be even. Each of the (s-1) even interior cuts gives a distinct pair of crossing intervals: if the same pair crossed two even cuts, it would also cross the odd cut between them, where only one interval is present. Thus the overlap graph has exactly (s-1) edges. It is connected because the Dyck path is primitive, so it is a tree and has exactly one spanning tree. Therefore
[
oxed{L(h^{min})=2^{s-1}.}
]
The corresponding right-hand exact ceiling counts observed for n=4,6,8,10 are 3,9,27,81, i.e. (3^{s-1}). That right-hand formula is not asserted here as an all-orders theorem; proving it directly, or deriving it from (EL) with a closed boundary-state recursion, would establish the pointwise Hall inequality on this one extremal path.


## General endpoint deletion: exact rooted-forest recurrence

The two-leaf identity (EL) is the first case of a more general boundary-state recursion, which handles the residual capacity vectors whose new endpoint cut has capacity 2 or larger.

For (b=(b_1,\ldots,b_{n-1})), let (A_n(b)) be the number of labeled trees with cut loads at most (b). For a nonempty set (S\subseteq\{2,\ldots,n\}), write
[
r_k(S)=|S\cap\{k+1,\ldots,n\}|,\qquad 2\le k\le n-1.
]
Let (F_{n-1}(S;d)) denote the number of spanning forests on vertices (2,\ldots,n) which have exactly (|S|) components, each containing exactly one vertex of S, and whose old cut loads satisfy (c_k(F)\le d_k) for all (2\le k\le n-1). Then
[
oxed{
A_n(b)=
\sum_{\substack{\varnothing\ne S\subseteq\{2,\ldots,n\}\\|S|\le b_1}}
F_{n-1}\bigl(S; (b_k-r_k(S))_{k=2}^{n-1}\bigr).
}
	ag{RF}
]
A term with any negative residual capacity is zero.

**Proof.** In a tree T counted by A_n(b), let S be the neighbor set of vertex 1. Its size is deg_T(1)=c_1(T)≤b_1. Deleting vertex 1 produces a forest with exactly |S| components, and each component contains exactly one vertex of S: two neighbors of 1 in the same component would create a cycle when the two incident edges are restored. Conversely, any such rooted forest becomes a unique tree when vertex 1 is joined to every root in S. At cut k≥2, the restored star edges contribute exactly r_k(S), so the forest capacity is b_k-r_k(S). This partitions all counted trees by their unique neighbor set S and proves (RF).

When b_1=1, S={p} and the forest has one component, hence is a tree; (RF) reduces to the one-leaf recurrence. Applying it at both endpoints when b_1=b_{n-1}=1 gives (EL).

The rooted-forest count in (RF) is itself a matrix-tree quantity if the cut constraints are removed: for a weighted graph on {2,...,n}, the all-minors Matrix-Tree Theorem identifies the number of forests rooted at S with the principal Laplacian minor obtained by deleting rows and columns indexed by S. The cut constraints remain the hard part; they couple the forest's components to the ordered boundary.

### Why this is the relevant next state space

After deleting the two forced endpoint leaves of a primitive capacity h, the residual first and last capacities are in {1,2}, depending on the two leaf-neighbor choices. Repeated leaf deletion alone therefore does not close: when a residual boundary capacity is 2, the endpoint may have degree 2, and deleting it creates a two-component rooted forest rather than a tree. Formula (RF) gives the exact missing state, without discarding multiplicities or assuming a false leaf condition.

A plausible induction state is consequently a rooted forest with a specified ordered boundary-root set and residual cut capacities. To prove the one-link inequality by this route, one would need (i) a tractable recursion/upper bound for the left interval-overlap spanning-tree demand in matching boundary states, and (ii) a lower bound on the corresponding right rooted-forest supply. Neither comparison is established yet. The recurrence is exact, but it is not itself a Hall inequality.


## Left-side root-interval / rooted-overlap-forest recurrence (corrected)

There is an exact counterpart to (RF) for the left demand (L_n(h)), obtained by deleting the unique matching interval incident to port 1 from each interval-overlap spanning tree.

Let (I_0=[1,p]) be that interval. The remaining matching (M') is a perfect matching of
[
V_p=\{2,\ldots,n\}\setminus\{p\}.
]
Let (H_{M'}) be its interval-overlap graph, with edges between intervals whose interiors intersect:
[
[a,b]\sim[c,d]\iff \max(a,c)<\min(b,d).
]
The root interval (I_0) overlaps exactly those remaining intervals whose left endpoint is less than p. Define the *candidate root set*
[
S_p(M')=\{I\in M':\min I<p\}\subseteq V(H_{M'}).
]
For a finite graph H and a nonempty selected root set R\subseteq V(H), write (\mathfrak F(H,R)) for the spanning forests F of H such that every component of F contains exactly one vertex of R. Write (R(H,R)=|\mathfrak F(H,R)|).

The exact recurrence is
[
\boxed{
L_n(h)=
\sum_{p=2}^{n}\
\sum_{\substack{M'\text{ perfect matching of }V_p\\
m_k(M')=h_k-\mathbf1_{k<p}\;\forall k}}
\quad
\sum_{\varnothing\ne R\subseteq S_p(M')}
R(H_{M'},R).
}
\tag{LF-corrected}
]

**Proof (bijection).** A left object is a pair ((M,\tau)), where M has load h and \tau is a spanning tree of H_M. Let I_0=[1,p] be the unique interval containing port 1. Delete the vertex I_0 from \tau. The result is a spanning forest F of H_{M'}. Let R be the set of neighbors of I_0 in \tau. Every such neighbor belongs to S_p(M'), because it must overlap [1,p]. Since \tau is a tree, each component of F contains exactly one vertex of R: it contains at least one because \tau was connected, and cannot contain two because the path between two neighbors would create a cycle after I_0 is restored. Thus F\in\mathfrak F(H_{M'},R) for the *selected* nonempty subset R\subseteq S_p(M').

Conversely, choose p, M', a nonempty subset R\subseteq S_p(M'), and a forest F\in\mathfrak F(H_{M'},R). Restore [1,p] and join its graph vertex to every vertex in R. Each added edge exists in H_M by the definition of S_p. Since each component of F has exactly one R-root, the restored graph is connected and acyclic, hence a spanning tree of H_M. These operations are inverse. The deleted interval contributes \mathbf1_{k<p} to cut k, so the residual matching load is h_k-\mathbf1_{k<p}. This proves (LF-corrected).

The selected root set is essential. It is not generally the entire candidate set S_p(M'). For example, if H_M=K_3 and I_0 is one vertex, the other two vertices both lie in S_p. The three spanning trees of K_3 correspond to selected root sets {v_1}, {v_2}, and {v_1,v_2}; fixing R=S_p would count only the last one and lose two trees. This was the defect in the earlier formula and is now corrected in both the audit and verifier.

The identity remains valid when H_{M'} is disconnected: a selected-root forest exists exactly when every connected component of H_{M'} contains at least one selected root. That is precisely what is needed for the restored graph H_M to be connected.

### Paired recursions and the remaining comparison

The right recurrence (RF) deletes a port-vertex from a port spanning tree and records a rooted forest on the remaining complete graph. The corrected left recurrence deletes the matching interval incident to port 1 and records a rooted forest on the remaining interval-overlap graph, summed over all nonempty selected subsets of its candidate root set.

The structural difference is now sharply isolated:
- right side: rooted forests in the complete graph on V_p, subject to residual port-cut capacities and a root set determined by the deleted port's actual neighbor set;
- left side: rooted forests in the sparse interval-overlap graph H_{M'}, with selected roots R ranging over nonempty subsets of S_p(M'), summed over residual matchings.

Graph inclusion H_{M'}\subseteq K_{V_p} alone still does not compare the two sides: the left root subsets and residual capacities vary with M', and the right recurrence's root set is coupled to the port-tree attachment choices. A valid Hall comparison must inject these matching-decorated rooted forests into capacity-admissible complete-graph rooted forests, or prove an aggregate Hall inequality over the selected-root states.

The verifier research/verification/verify_pf_i16_left_interval_rooted_forest_recurrence.py now sums over all nonempty selected root subsets and compares the corrected recurrence against direct spanning-tree counts for primitive loads at n=4,6,8,10. It is a finite identity check, not an all-orders Hall proof.


## Pairwise interval switch: a valid local cut domination, and why it does not yet globalize

Let two distinct matching intervals have four endpoints
\[
x_1<x_2<x_3<x_4.
\]
If their interiors intersect, their endpoint pairing is either the crossing pairing
\((x_1,x_3),(x_2,x_4)\) or the nested pairing
\((x_1,x_4),(x_2,x_3)\). In either case, the two matching intervals contribute cut-load
\[
(1,2,1)
\]
on the three consecutive cut blocks
\([x_1,x_2),[x_2,x_3),[x_3,x_4)\), respectively (with zero contribution outside \([x_1,x_4)\)). Replacing those two matching edges by the three-edge path
\[
x_1-x_2-x_3-x_4
\]
gives cut-load \((1,1,1)\) on those same blocks. Thus:

**Pairwise switch lemma.** For any overlapping pair of matching intervals, the consecutive-endpoint path on their four endpoints is a tree on those endpoints and its cut-load is coordinatewise bounded by the contribution of the two original matching intervals.

This gives a genuine local rerouting operation, including for nested intervals; it is stronger than merely choosing one connector between the two interval-vertices. It does not by itself produce a global port tree from an overlap-tree \(\tau\), because local paths belonging to different edges of \(\tau\) share interval endpoints and can force incompatible edge choices.

A minimal obstruction to the naive globalization is
\[
M=\{(1,8),(2,3),(4,5),(6,7)\},
\qquad
\tau=K_{1,3}
\]
with center \((1,8)\). The matching load is
\[
h=(1,2,1,2,1,2,1).
\]
The three pairwise paths are
\[
1-2-3-8,\qquad 1-4-5-8,\qquad 1-6-7-8.
\]
Their union is connected, but **no** spanning tree contained in this union has cut-load coordinatewise bounded by \(h\). The union has exactly nine edges:
\[
\{1,2\},\{2,3\},\{3,8\},\{1,4\},\{4,5\},\{5,8\},\{1,6\},\{6,7\},\{7,8\}.
\]
A spanning tree has seven edges, so there are only \(\binom97=36\) candidate edge subsets. Exact enumeration of these 36 subsets finds 27 spanning trees and zero whose seven cut loads are bounded by \((1,2,1,2,1,2,1)\). This is a small, fully finite obstruction to the proposed union-and-prune rule; it does not rely on a heuristic picture or on an incorrect claim that a particular edge is forced. The cut constraints at the four odd cuts each allow only one crossing edge, and the available local-path edges cannot satisfy all four constraints while connecting all eight vertices.

The obstruction is specific to this proposed local-to-global rule, not to the Hall inequality: the same load vector has ample right-side supply in the finite computations. It shows what a successful construction must add beyond pairwise switching: a global reassignment of which endpoint edges represent each overlap-tree incidence, or a nonlocal encoding of \(\tau\) that can reroute around the forced-cut bottleneck.

**Consequence for the proof plan.** The pairwise switch lemma can be used as a local exchange rule inside a future augmenting-path/Hall argument, but it is not an injection. Any such argument must track the residual cut capacity after earlier switches; treating each overlap-tree edge independently double-spends capacity in configurations such as the four-vertex star above. No all-orders Hall inequality follows from this lemma alone.


## Hall reduction at tight cuts: a common backbone / rooted-forest state

The coordinatewise Hall condition has a useful additional structure at cuts where a primitive load is minimal. Fix a primitive Dyck load \(h\), and let
\[
K(h)=\{k\in\{1,\ldots,n-1\}:h_k=1\}
=\{k_1<\cdots<k_r\}.
\]
Call these *tight cuts*. They are the cuts at which every admissible right-hand tree has exactly one crossing edge.

### Right-hand backbone lemma

If \(T\) is a spanning tree with \(c_k(T)\le h_k\), then for every \(k\in K(h)\),
\[
c_k(T)=1.
\]
Let \(e_k(T)\) be its unique crossing edge. Then every \(e_k(T)\) lies on the unique path in \(T\) from vertex 1 to vertex n, and these edges occur along that path in increasing cut order.

**Proof.** Every spanning tree has at least one edge across every nontrivial prefix cut, so the capacity one forces equality. Removing the unique crossing edge disconnects the tree into the prefix and suffix, hence that edge lies on the 1-to-n path. Along that path, the first passage from \(\{1,\ldots,k\}\) to its complement must precede the first passage across any larger prefix cut. This gives the order assertion.

The edges at distinct tight cuts are also distinct. If one edge crossed two cuts \(k<l\), deleting it would leave every vertex in the nonempty middle slab \(\{k+1,\ldots,l\}\) in one of its two components. The component containing such a vertex would still have to connect across one of the two cuts without using the deleted unique crossing edge, a contradiction.

Consequently the \(r=|K(h)|\) tight cuts force \(r\) distinct bridge edges. Deleting these \(r\) edges from \(T\) produces exactly \(r+1\) components, each confined to one of the \(r+1\) nonempty consecutive label slabs determined by \(K(h)\). Since there are \(r+1\) slabs, there is exactly one connected within-slab tree in each slab. The original right-hand tree is a chain of these slab trees joined by the unique bridge edges. Off-slab branches cannot cross a tight cut: that would create a second crossing edge there.

### Left-hand tight-cut structure

For a matching \(M\) with load \(h\), each tight cut \(k\in K(h)\) is crossed by exactly one matching interval, denoted \(I(k)\). Any two distinct intervals that overlap have a common integer cut \(t\) with both intervals active, and necessarily \(h_t\ge2\); hence their overlap occurs strictly inside one of the open blocks between consecutive tight cuts. Thus every edge of the interval-overlap graph is supported inside a single such block.

For a block \((k_j,k_{j+1})\), the intervals active at its interior cuts form a connected interval-overlap subgraph: their union covers the block, and a gap between two disjoint overlap components would leave an interior cut with no active interval. The unique intervals crossing the two boundary tight cuts, when distinct, are the natural boundary vertices of this block graph. The full overlap graph is assembled from these block graphs by identifying the boundary interval that persists across consecutive tight cuts. A spanning tree of the full overlap graph consequently restricts to rooted forests in the block graphs, with roots at the boundary intervals through which the block pieces attach. This is the multi-block analogue of the one-root recurrence (LF).

### What this does and does not establish

This identifies a shared state space for the two sides:
- right: trees inside consecutive slabs, attached along the unique edges forced at tight cuts;
- left: interval-overlap rooted forests inside the corresponding blocks, attached along the unique matching intervals forced at tight cuts.

It also explains why the minimal primitive path is unusually tractable: every cut is tight or has height two, so the backbone leaves almost no room for branching. For a general primitive path, the non-tight blocks can have substantial height and the rooted boundary state must retain the attachment locations and residual cut capacities.

The remaining Hall step is now a blockwise capacitated comparison: for each sequence of tight-cut boundary states, compare the total number of left interval-overlap rooted-forest decorations with the number of right slab-tree decorations having no larger residual cut loads. The boundary data must be retained; summing over blocks independently would lose the correlation of a matching interval or a right bridge edge that spans several consecutive tight cuts. This is a structural reduction, not yet an inequality. In particular, it does not prove the pointwise class bound \(Q(h)\ge L(h)\) or the down-set Hall inequalities.


## Peak-cover reduction of the classwise Hall inequality (2026-11-16)

The primitive-Dyck poset has a much smaller family of immediate lower covers than its full strict lower ideal. This yields a sharper sufficient inequality for the pointwise Hall condition.

For a primitive path \(h=(h_1,\ldots,h_{n-1})\), define its *lowerable peaks*
\[
P(h)=\{k: h_k>h_{k-1},\ h_k>h_{k+1},\ h_k\ge3\},
\qquad h_0=h_n=0.
\]
For each \(k\in P(h)\), let \(h^{(k)}=h-2e_k\). This is again a primitive Dyck path: at a peak its two neighbors are \(h_k-1\), and lowering the peak by two changes the two adjacent steps to down then up; positivity follows from \(h_k\ge3\).

### Cover lemma

**Lemma.** If \(g,h\) are primitive Dyck paths with \(g\le h\) and \(g\ne h\), then there is a lowerable peak \(k\in P(h)\) such that
\[
g\le h^{(k)}<h.
\]
Consequently the immediate lower covers of \(h\) are exactly the paths \(h^{(k)}\), \(k\in P(h)\), and
\[
\{g\in\mathcal P_n:g<h\}
=
\bigcup_{k\in P(h)}\{g\in\mathcal P_n:g\le h^{(k)}\}.
\]

**Proof.** At every index, primitive Dyck paths have the same parity, so
\[
d_i=(h_i-g_i)/2
\]
is a nonnegative integer. Since \(g\ne h\), some interior index has \(d_i>0\). If such an index is not a local maximum of \(h\), at least one neighboring index \(j\) has \(h_j=h_i+1\). Since both paths take unit steps, \(g_j\in\{g_i-1,g_i+1\}\), and therefore \(d_j\ge d_i>0\). Follow such an uphill neighbor. The height strictly increases at each move, so the process terminates at a local maximum \(k\) with \(d_k>0\). Then \(h_k-g_k\ge2\), and positivity of \(g_k\) gives \(h_k\ge3\). Thus \(k\in P(h)\) and \(g_k\le h_k-2\), while \(g_i\le h_i\) at every other coordinate. Hence \(g\le h^{(k)}\). This proves the lemma and the cover characterization.

### Exact ceiling-class formula

Recall
\[
A_n(b)=\#\{T\in\mathcal T(K_n):c_k(T)\le b_k\text{ for all }k\},
\]
for any integer capacity vector \(b\), with \(A_n(b)=0\) if a capacity is below 1. Let \(Q(h)\) be the number of trees whose least primitive majorant is exactly \(h\). By the cover lemma,
\[
\widehat c(T)=h
\quad\Longleftrightarrow\quad
c(T)\le h\text{ and }c_k(T)\ge h_k-1
\text{ for every }k\in P(h).
\]
Indeed, failure of the latter condition is exactly membership in one of the lower-cover events \(c(T)\le h^{(k)}\). Inclusion-exclusion over these events gives the exact formula
\[
\boxed{
Q(h)=
\sum_{S\subseteq P(h)}(-1)^{|S|}
A_n\!\left(h-2\sum_{k\in S}e_k\right).
}
\tag{PC}
\]
The capacities in the terms need not themselves be Dyck paths; \(A_n\) was defined for arbitrary capacity vectors. Formula (PC) is exact and uses only \(2^{|P(h)|}\) determinant coefficient-sums, rather than Möbius inversion over the full primitive-path ideal.

### Sharper sufficient Hall bound

The union bound applied only to the immediate lower-cover events yields
\[
Q(h)\ge A_n(h)-\sum_{k\in P(h)}A_n(h^{(k)}).
\]
Therefore the following condition is sufficient for the classwise injection, and hence for every capacitated Hall inequality:
\[
\boxed{
A_n(h)\ge L(h)+\sum_{k\in P(h)}A_n(h^{(k)})
\quad\text{for every primitive }h.
}
\tag{PC-UB}
\]
This is strictly sharper than the earlier criterion that subtracted \(A_n(g)\) for every strict lower primitive path. It is still only a sufficient condition: overlaps among the lower-cover events make (PC) potentially substantially larger than its union-bound lower estimate.

### Exact finite checks

The existing exact tree enumerations through ten ports give the following minimum margins in (PC-UB):
\[
\min_{h\in\mathcal P_n}
\left(A_n(h)-L(h)-\sum_{k\in P(h)}A_n(h^{(k)})\right).
\]

| Ports \(n\) | Primitive paths | Minimum peak-cover margin |
|---:|---:|---:|
| 4 | 1 | 1 |
| 6 | 2 | 5 |
| 8 | 5 | 19 |
| 10 | 14 | 65 |

For ten ports, the path-by-path margins in lexicographic order are:
\[
65,\ 378,\ 378,\ 2013,\ 6354,\ 378,\ 2095,\ 2013,\ 9641,\ 29951,\ 6354,\ 29951,\ 70106,\ 222113.
\]
The exact n=4,6,8 Hall verifier and n=10 C++ ceiling-class verifier now check the peak-cover lemma on the finite path poset, the exact inclusion-exclusion identity (PC), and (PC-UB), in addition to their previous Hall and union-bound checks. The Python inclusion-exclusion verifier uses the actual peak coordinates (not peak-list indices) when lowering the capacity vector.

**What remains open.** No uniform lower bound for the determinant sums \(A_n(h)\) in (PC-UB) has been proved. Thus the peak-cover lemma is an exact poset reduction and (PC-UB) is a sharper all-orders sufficient target, but neither the pointwise inequalities \(Q(h)\ge L(h)\) nor the general down-set Hall inequalities are yet established.


## Prefix-component interpretation of right cut loads

There is a useful equivalent description of the right-hand capacity constraint. For a tree T on {1,...,n}, let T[k] be the induced forest on the prefix {1,...,k}, and let \(\kappa(T[k])\) be its number of connected components. Then
\[
\boxed{c_k(T)=\kappa(T[k]).}
\]
Indeed, every component of T[k] must have at least one edge to the suffix in order for T to be connected, and it can have at most one such edge because two would create a cycle using the path in that component and the suffix. Thus the crossing edges are in bijection with the prefix components.

Equivalently, if
\[
r_j(T)=|\{i<j:\{i,j\}\in E(T)\}|
\]
is the number of earlier neighbors of vertex j, then
\[
c_k(T)=k-\sum_{j=2}^{k}r_j(T),
\]
and the cut-capacity condition is
\[
\sum_{j=2}^{k}r_j(T)\ge k-h_k
\qquad(1\le k<n).
\]
This follows by counting the edges of the induced prefix forest: it has k vertices and \(\sum_{j=2}^k r_j(T)\) edges, so its component count is their difference.

For a matching M of load h, the induced matching graph on the first k ports has exactly \((k+h_k)/2\) components: each closed pair is one component and each of the h_k currently open interval endpoints is an isolated component. Thus h_k is precisely the number of *open singleton components* in the matching prefix, while c_k(T) is the total number of components in the tree prefix.

The peak-cover characterization sharpens this interpretation: a tree in ceiling class h has at most h_k prefix components at every cut and at least h_k-1 components at every lowerable peak. The right-hand Hall supply is therefore concentrated on trees whose prefix-component count nearly saturates the Dyck capacity at each such peak.

This suggests a growth-process formulation of the Hall problem: process ports from left to right, and at vertex j attach it to r_j earlier components. The open-interval matching process creates a new singleton component at an up-step and closes one open interval at a down-step; the overlap-tree decoration must be encoded by choices of earlier components at these closing steps. The count identity above is exact, but a canonical injective encoding of all (M,\tau) into such component-merging histories has not yet been constructed.
