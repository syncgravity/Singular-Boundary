# PF-I16: Multivalued parent projection as an all-orders Hall route

Date: 2026-11-16/17

## Status

This note isolates the strongest recursive relation currently supported by the finite computations. It is a proof program, not an all-orders proof.

## Source and target objects

A source is (x=(M,\tau)), where (M) is a perfect matching of the ordered ports and \(\tau\) is a spanning tree of its interval-overlap graph. A target is a labelled port-spanning tree.

For every non-root leaf interval \(\ell\) of \(\tau\), delete \(\ell\) and its two endpoints, then relabel the remaining ports in order. This gives a parent source \(\pi_\ell(x)\) on two fewer ports.

Fix the canonical leaf rule already used by the source-dependent leaf-peeling verifier. Write \(C_{\rm can}(p)\) for the set of parent port trees produced by guarded local switches with the canonical leaf of parent source \(p\) inserted last.

For each child source \(x\), define the multivalued parent-restricted child neighborhood
\[
R_n(x)=\bigcup_{\ell\in L_0(\tau)}
\{T:\ T\text{ is an }\ell\text{-last guarded output of }x,
\quad \pi_\ell(T)\in C_{\rm can}(\pi_\ell(x))\}.
\]
Here \(\pi_\ell(T)\) is obtained by inverting the final local switch and deleting the endpoints of \(\ell\). The inverse is unique for a fixed final leaf.

Every retained target has cut-load vector coordinatewise bounded by the source matching load, because every guarded local switch has that property and the final inverse is a legal switch history.

## The exact induction target

The desired statement is the Hall condition
\[
|N_{R_n}(A)|\ge |A|\qquad
( A\subseteq X_n),
\tag{H\(_n^\pi\)}
\]
where \(X_n\) is the set of all sources on \(n\) ports.

If \((H_n^\pi)\) holds for every even \(n\), then the weighted one-link inequality follows: for every source subset (in particular every down-set in the cut-load poset), its distinct representative targets have load no larger than the source loads. The usual down-set Hall reduction then gives the coefficientwise weighted inequality.

## Why the projection must be multivalued

A fixed canonical child leaf is too restrictive. At ten ports, restricting each child to its canonical leaf and requiring the parent projection to lie in the canonical eight-port parent neighborhood leaves a graph with 31,744 sources and a Hall deficiency of 92. The alternating-reachability witness has 264 child sources and 172 neighbors, arranged as four sources in each of 66 parent fibers.

Allowing every non-root leaf \(\ell\) as a possible parent projection repairs this finite obstruction while retaining a strict restriction of the all-orders graph.

## Verified finite instance: ten ports

Verifier: `research/verification/verify_pf_i16_n10_multivalued_pi_projection.py`

Workflow run: https://github.com/syncgravity/Singular-Boundary/actions/runs/44021572817

The successful run reports:

- 31,744 child sources and 608 distinct parent sources;
- 1–4 available non-root leaves per source;
- 31,815,129 raw leaf incidences;
- 20,592,849 unique all-orders source-target incidences;
- 15,834,241 unique incidences in \(R_{10}\), i.e. 76.891940% of the all-orders graph;
- no isolated source; restricted degrees 16–3,304;
- 95,864 target trees;
- a matching saturating all 31,744 sources;
- empty alternating Hall-deficiency witness.

The matching uses all 608 parent sources. A parent-source/parent-target pair may support multiple distinct child lifts (observed multiplicity 1–43), so a proof cannot assume injectivity after projection. The child-level matching is genuinely global.

## The missing theorem: a capacity-sensitive lifting lemma

The finite result suggests the following formulation. For a child family \(A\), each pair \((p,P)\), with \(p\) a parent source and \(P\in C_{\rm can}(p)\), has a set of child lifts
\[
\mathcal L_A(p,P)=
\{(x,T):x\in A,\ \exists\ell\in L_0(\tau_x),\pi_\ell(x)=p,\ \pi_\ell(T)=P,\ T\in R_n(x)\}.
\]
The difficulty is that a child target can have witnesses through more than one leaf, and different parent pairs can lift to the same child target. Therefore simple counting of parent pairs or independent matching within each parent fiber is insufficient.

A viable proof needs a global exchange/capacity principle that turns the parent neighborhoods and the local switch alternatives into distinct child targets for an arbitrary family \(A\). In particular it must handle:
1. overlap between the lift sets from different leaves of the same source;
2. collisions between different parent fibers;
3. simultaneous collisions, not merely one challenger at a time;
4. preservation of the load-domination condition under every reroute.

One promising route is a matching-relative Hall argument at the child level. Given a maximum matching, a deficient set is characterized by its alternating-reachable closure. The parent projections should constrain the outgoing boundary of such a set. The n=8 proof succeeded by excluding small Hall slack via a sink-SCC boundary census. The next mathematical task is to identify an analogous projection-compatible boundary invariant for arbitrary even \(n\), rather than extrapolating the finite SCC counts.

## Proof boundary

The ten-port matching is a finite verified computation. It does not establish \((H_n^\pi)\) for arbitrary \(n\), does not prove the weighted inequality, and does not establish a Yang–Mills mass gap. The all-orders burden is precisely the capacity-sensitive lifting/exchange lemma above.

## New structural lemma: expansion inside a fixed (parent, deleted interval) fiber

Fix a parent source \(p\) and a possible deleted interval \(J\). Consider all child sources \(x\) satisfying \(\pi_J(x)=p\). Such a child is obtained by adjoining \(J\) to the parent matching and adjoining exactly one overlap edge \(e=(J,I)\) to the parent overlap tree. Consequently
\[
|X(p,J)|\le s-1
\]
when the child has \(s\) matching intervals: there are at most \(s-1\) choices for the parent interval \(I\).

For a fixed \(J\), the inverse final switch is rigid: from a child target \(T\), the two neighbors outside \(J\) recover the replaced edge, and deleting the local four-vertex tree and restoring that edge recovers a unique parent port tree \(P\). Therefore the lift sets of two distinct parent targets \(P\) are disjoint when \(J\) is fixed.

Moreover, for every \(P\in C_{\rm can}(p)\), insertion of \(J\) has at least two guarded local switch outcomes. The connected-tree witness argument applies to the connected port tree \(P\): if a port lies strictly inside \(J\), follow its path to port 1 and take the first edge leaving the interior; otherwise the parent interval adjacent to \(J\) contains \(J\), and the path between that interval's endpoints has an edge spanning \(J\). The no-reinsertion guard leaves at least two local patterns. Thus, writing \(L_J(P)\) for the final-switch lifts,
\[
|L_J(P)|\ge 2,
\qquad
L_J(P)\cap L_J(P')=\varnothing\quad(P\ne P').
\]
It follows that
\[
|N_{R_n}(X(p,J))|
\ge 2|C_{\rm can}(p)|
\ge 2\cdot 2^{s-2}
=2^{s-1}
\ge s-1
\ge |X(p,J)|.
\]
So Hall holds on every single fixed-\((p,J)\) fiber, with substantial local slack.

This isolates the remaining obstruction sharply: it is not a shortage of lifts within one fixed parent/deleted-interval fiber. It is collision between lift sets belonging to different deleted intervals \(J\), and potentially different parent sources, where the same child port tree can have distinct inverse projections. An all-orders proof should exploit the switch relation between these different projections to exchange/reroute representatives globally.

The inequality above is a local Hall statement. It does not imply global Hall for a union of different \((p,J)\) fibers, because their target neighborhoods can overlap.

## Quotient reduction: a sufficient split-demand Hall test

For fixed \((p,J)\), all child sources in \(X(p,J)\) have the same restricted target neighborhood \(N(p,J)\). This follows because the parent-before-child switch history has \(J\) last: the preceding history depends only on the parent source, and the final allowed local switch depends on the current port tree and \(J\), not on which parent interval is the unique overlap-tree neighbor of \(J\). The finite verifier checks this row equality.

A child source can have several non-root leaves and therefore belongs to several \((p,J)\) fibers. Consequently the stronger weighted condition with demand \(|X(p,J)|\) is sufficient but is not equivalent to source-level Hall: it can count one child source more than once.

The correct quotient demand splits each source's unit mass evenly among its available leaves. If \(d(x)=|L_0(\tau_x)|\), define
\[
\delta(p,J)=\sum_{x\in X(p,J)}\frac1{d(x)}.
\]
Then every source contributes total demand exactly one:
\[
\sum_{(p,J):x\in X(p,J)}\frac1{d(x)}=1.
\]
For any source family \(A\), let \(S(A)\) be the set of fibers touched by at least one source in \(A\). Every leaf-fiber of every \(x\in A\) lies in \(S(A)\), so
\[
|A|\le\sum_{(p,J)\in S(A)}\delta(p,J).
\]
Thus the following weighted quotient inequality is a sufficient Hall criterion:
\[
\boxed{
\left|\bigcup_{(p,J)\in S}N(p,J)\right|
\ge\sum_{(p,J)\in S}\delta(p,J)
\quad\text{for every set of fibers }S.
}
\tag{QH\(_n^{\rm split}\)}
\]

A particularly concrete sufficient condition is the uniform row transport
\[
\lambda_{(p,J),T}=
\begin{cases}
\delta(p,J)/|N(p,J)|,&T\in N(p,J),\\
0,&T\notin N(p,J).
\end{cases}
\]
If every target column has load
\[
\sum_{(p,J):T\in N(p,J)}
\frac{\delta(p,J)}{|N(p,J)|}\le1,
\]
then summing the transport over any fiber set proves \((QH_n^{\rm split})\), and hence the original source-level Hall condition.

The verifier `verify_pf_i16_fixed_parent_leaf_fiber_expansion.py` now computes these demands exactly as rational numbers and reports exact target loads and overload counts. A maximum column load at most one proves Hall for that finite order. A load above one only disproves this uniform transport; it does not disprove Hall or a nonuniform fractional transport.

The all-orders task is to prove the split-demand quotient inequality, perhaps by constructing a nonuniform transport or a matching-relative alternating-boundary argument. This quotient formulation is a sufficient reduction, not an equivalence.

## From a Hall matching to the weighted one-link inequality

Let \(X_n\) be the source objects \((M,\tau)\), each carrying load vector \(m(M)\), and let \(Y_n\) be all labelled port-spanning trees, each carrying cut-load vector \(c(T)\). Every edge in the guarded-switch relation satisfies
\[
c(T)\le m(M)\quad\text{coordinatewise}.
\]

If the split-demand transport has all target-column loads at most one, then it is a fractional matching saturating every source. Since the bipartite incidence matrix is integral (equivalently, by the max-flow/min-cut theorem for bipartite graphs), a source-saturating integral matching exists. The same conclusion follows directly if one verifies a matching certificate.

Now let \(D\) be any down-set in the coordinatewise load poset. Every source with \(m(M)\in D\) is matched to a distinct target with \(c(T)\le m(M)\), hence \(c(T)\in D\). Therefore
\[
\#\{(M,\tau):m(M)\in D\}
\le
\#\{T:c(T)\in D\}.
\tag{D}
\]

For \(0\le x_k\le1\), the weight
\[
f(h)=\prod_{k=1}^{n-1}x_k^{h_k}
\]
is antitone in the coordinatewise order. On a finite poset, every nonnegative antitone function is a nonnegative linear combination of indicators of its superlevel down-sets (equivalently, use the layer-cake identity \(f(h)=\int_0^\infty\mathbf 1_{\{f(h)\ge t\}}\,dt\)). Applying (D) to each such down-set and integrating yields
\[
\sum_{(M,\tau)}\prod_{k=1}^{n-1}x_k^{m_k(M)}
\le
\sum_{T\in\mathcal T(K_n)}\prod_{k=1}^{n-1}x_k^{c_k(T)}.
\]
Since each matching \(M\) occurs with exactly \(\tau(H_M)\) overlap-tree choices \(\tau\), the left side is precisely the weighted one-link expression in (1).

Thus the split-demand column test is not merely a numerical surrogate: a successful all-orders bound would imply the desired weighted inequality exactly. The present computations only test this route at finite orders; no all-orders column bound has yet been established.


## Independently checked n=10 matching certificate (2026-11-17)

The multivalued-pi workflow now emits and independently checks an explicit matching certificate:
[workflow 44031284003](https://github.com/syncgravity/Singular-Boundary/actions/runs/44031284003),
[artifact 14309344057](https://github.com/syncgravity/Singular-Boundary/actions/runs/44031284003/artifacts/14309344057).
The independent checker reports `PASS: explicit n=10 multivalued-pi matching certificate`.

The certificate gives one selected non-root leaf and one projected parent target for each of the 31,744 child sources. It verifies that each selected child target is in the retained relation and that all 31,744 child targets are distinct. Thus the finite relation is Hall-saturating with an explicit, independently replayable witness.

The selected assignment can be viewed as a nonuniform integral allocation to parent-leaf fibers. Each child source chooses exactly one of its available leaf fibers; the selected child target is routed through that fiber. In the certificate:
- 16,176 parent-leaf fibers receive positive selected demand;
- selected demand per occupied fiber is 1–4 (histogram 1: 6,353; 2: 5,400; 3: 3,101; 4: 1,322);
- 608 distinct parent sources are represented, with 12–98 child sources per parent source;
- 10,179 distinct assigned (parent source, projected parent target) pairs occur, with pair multiplicity 1–43.

This explains how the finite matching avoids the overloaded columns of the uniform split-demand transport: it chooses the leaf and child target jointly, instead of distributing every source uniformly over all its leaves. Parent projection is emphatically not injective; repeated parent pairs are allowed and are resolved by distinct child lifts.

This is a finite certificate, not an all-orders construction. The matching algorithm still solves the full finite child graph. The all-orders problem is to prove a structural nonuniform allocation/augmenting theorem that chooses one leaf and one lift per source while keeping child targets distinct, for every even order. See `PF_I16_N10_MULTIVALUED_PI_MATCHING_CERTIFICATE_2026_11_17.md` for the certificate audit and exact counts.


## New reduction: first-overcrowded-cut blocks and all-orders local Hall

The complement of K_{2s} partitions by the first odd cut k with matching load m_k>=3. Write X_k for this source block. Port trees partition similarly into Q_{2s} (all odd cut loads equal one) and Y_k (first odd cut with c_k>=2).

The exact parity argument is:
- m_k is odd at odd cuts and even at even cuts;
- connectedness gives m_k>=1 at every cut;
- if no odd cut has load at least three, then all odd loads are one and all even loads are two, which is exactly K_{2s}.

A new all-orders theorem is recorded in
`research/audits/PF_I16_CUT_CLASS_LOCAL_HALL_THEOREM_2026_11_17.md`:

For every source x in X_k,
[
|N_{R_{2s}}(x)cap Y_k|ge 2^{s-2}.
]
The proof is by induction on s and a cut-preserving final-switch lemma. If the deleted leaf interval J is on one side of k, the parent source remains in the corresponding first-overcrowded-cut class, and every admissible final switch preserves c_k. If J crosses k, a guarded local switch can always increase the crossing count from at least one to at least two. Distinct parent targets have disjoint lifts for fixed J.

Every fixed (parent,J) fiber has at most s-1 child sources and a common target row, so its restricted graph into Y_k satisfies Hall individually:
[
|N(F(p,J))cap Y_k|ge 2^{s-2}ge s-1ge |F(p,J)|.
]

This does not yet prove Hall for unions of different fibers inside X_k. Their target neighborhoods can overlap. The next sufficient test is the split-demand quotient transport restricted to each first-overcrowded-cut block. Its exact finite diagnostic is
`research/verification/verify_pf_i16_overcrowded_cut_split_transport.py`.
The n=12 source-profile census is
[44070581000](https://github.com/syncgravity/Singular-Boundary/actions/runs/44070581000); it found 2,692,064 connected sources, of which 32 are in K_12, and first-overcrowded-cut counts 2,628,576 (k=3), 61,056 (k=5), 2,256 (k=7), and 144 (k=9).

The finite n=10 same-cut row-support and split-demand transport diagnostics are running in
[44073281842](https://github.com/syncgravity/Singular-Boundary/actions/runs/44073281842). These computations test the quotient criterion; they do not replace the all-orders local theorem and cannot establish the global quotient inequality by themselves.


## Canonical third-mark obligation: corrected base-order boundary and leaf-bubbling reduction (2026-11-18)

The source-diamond census through eight target ports is useful for checking the exact source projections and target-side inverses, but its C3 conclusion is automatic once the common double inverse is known to be an output of the common parent source:

- At target order n=6, the common parent source r has one matching interval and no non-root leaf.
- At target order n=8, r has two matching intervals. Its overlap tree has exactly one non-root leaf, so the full output set C(r) equals the canonical-leaf-last set C_can(r).

Thus the 7,884 n=8 C3 passes do not test a nontrivial canonical choice. The first order at which C3 can distinguish canonical from noncanonical last leaves is n=10, when r has three matching intervals. For a rooted path, there is still only one non-root leaf and C3 is automatic. The first genuine case is a rooted star, with two non-root leaves.

### Exact rooted-star reduction

Let r have root interval R and non-root leaves A,B, with A lexicographically smaller than B. Then C_can(r) is the set of outputs of r whose last inserted interval is A.

If U in C(r) has a construction ending in A, then U is already in C_can(r). Otherwise its two-interval insertion history ends in B, so B is a valid guarded reverse mark of U. Since r^- = r-A has only one non-root leaf B, its full output set is exactly the set of targets for which B is a valid guarded reverse mark. Therefore, in this nontrivial rooted-star case,
\[
U\in C_{\rm can}(r)
\iff
\bigl[A\text{ is a valid guarded reverse mark of }U\bigr]
\ \text{and}\
\bigl[B\text{ remains a valid guarded reverse mark of }P_A(U)\bigr],
\]
provided the chosen history of U ends in B.

This is a one-sided survival criterion. It is not necessary to assume that A also survives after reversing B. If both directions survive, the proved target-side mutual-survival diamond additionally identifies the two double inverses.

### Source attachment constraint in the first nontrivial case

In the rooted-star case, let v_K be the attachment vertex in r of the child-source leaf K (the canonical leaf of p=r+K), and v_J the attachment vertex of J (the canonical leaf of q=r+J). If v_K is not A, then A remains a non-root leaf in p; canonicality of K in p forces K to precede A in p's lexicographic interval order. Similarly, if v_J is not A, canonicality of J in q forces J to precede A in q's interval order.

Consequently, the only attachment geometry in which neither canonicality condition compares the new leaf against A is
\[
v_K=v_J=A.
\]
This is a necessary case split, not a proof of the target-side third-mark conclusion. The p and q interval orders are separately compressed; no direct comparison between K and J across those two coordinate systems is implied.

### Leaf-bubbling criterion

Let L be any non-root leaf of a source overlap tree, and let
\[
\sigma=(I_1,\ldots,I_s)
\]
be a parent-before-child insertion history producing a target U. Because L is a leaf, it has no descendants. Hence moving L to the right across later intervals preserves the source partial order.

For an adjacent segment in the history where L is followed by K, let V be the target immediately after inserting K. Suppose:

1. L is a valid guarded reverse mark of V; and
2. K remains a valid guarded reverse mark of P_L(V).

Then the two-step inverse
\[
V\xrightarrow{P_L}P_L(V)\xrightarrow{P_K}W
\]
is valid. Reversing these two steps gives a valid construction
\[
W\xrightarrow{K}P_L(V)\xrightarrow{L}V.
\]
Thus the adjacent insertions can be swapped without changing their terminal target. Repeating this swap moves L to the final position. Consequently U belongs to C_can(r).

This is a rigorous sufficient criterion for canonicalization. It uses only one-sided survival at each adjacent swap; the stronger mutual-survival theorem is available when both directions hold.

### Remaining all-orders third-mark burden

For a source diamond (p,J),(q,K) over common parent r, the hypotheses provide two canonical parent histories and a common double inverse U in C(r). They do not yet provide the adjacent one-sided survival chain needed to move the canonical leaf L of r to the end of a history for U.

The all-orders proof must derive one of the following, not assume it:

1. directly, that L is a valid reverse mark of U and P_L(U) belongs to C(r-L); or
2. a leaf-bubbling chain of one-sided adjacent survivals that reorders a construction of U so that L is last.

The first nontrivial rooted-star case at n=10 is being instrumented by the canonical source-diamond verifier to separate:
- rooted path versus rooted star parent sources;
- attachment vertices v_K,v_J relative to the canonical leaf A, the other leaf B, and the root;
- validity of A as a reverse mark of U;
- survival of B after reversing A, equivalently P_A(U) in C(r-A).

The n=6/n=8 finite C3 counts are retained as source/target consistency checks, not as evidence for the nontrivial all-orders third-mark lemma. No all-orders third-mark or Hall theorem is claimed here.


## Current proof boundary after the exact twelve-port retained-grandparent census (2026-11-18)

The proposed sibling-source retained-grandparent rerouting is now **disproved** at the first four-interval common parent. The corrected exact census is recorded in
\`PF_I16_DIRECT_MIXED_HALL_AFTER_RETAINED_DIAMOND_COUNTEREXAMPLE_2026_11_18.md\`
and workflow [44369690167](https://github.com/syncgravity/Singular-Boundary/actions/runs/44369690167).

The census reconstructs genuine twelve-port sibling sources, includes both p=q and p!=q, and uses the exact no-reinsertion reverse guard. It finds 796,012 mutually surviving common-target incidences at the fixed parent R, of which 248,636 have a common double inverse outside the actual retained grandparent neighborhood N_pi(R). The first witness has p=q. Thus no all-orders proof may rely on merging sibling fibers through a retained common-grandparent target.

This does not refute the child-level Hall theorem or the split-demand quotient inequality. The proof target remains the direct arbitrary-family inequality (QH), or equivalently its first-overcrowded-cut blockwise form (BQH_k). The all-orders noncrossing recursion, target cut preservation, and crossing-leaf localization remain valid and independent of the disproved rerouting lemma.

A further exact source-side identity is now available. For a fiber F=(p,J), lift the parent intervals to the child port line. If d(p) is the number of non-root leaves of p, a(p,J) is the number of overlapping non-root-leaf parent intervals, and b(p,J) is the number of overlapping root/internal parent intervals, then
\[
\delta(p,J)=\frac{a(p,J)}{d(p)}+\frac{b(p,J)}{d(p)+1},
\]
with the one-interval parent base case \delta=1. This follows by enumerating the possible single attachment edge from the new leaf J to an overlap-neighbor in the parent tree.

The next proof obligation is therefore not a third-mark or grandparent-compatibility lemma. It is a capacity-sensitive proof of the weighted reverse-mark inequality
\[
\sum_F\delta(F)z_F
\le
\sum_T\max_{F:T\in N(F)}z_F
\qquad(z_F\ge0),
\]
within each cut block. The proof must account for mixed crossing/noncrossing fibers and preserve unit capacity at each child target. The previous uniform row allocation is overloaded at n=10, and the fixed-grandparent reroute is false. No new workflow should be launched until a new allocation or dual inequality is specified and its finite predictions are clear.

The all-orders Hall theorem, weighted one-link inequality, and any Yang--Mills mass-gap claim remain open.


## New direct capacity criterion: reciprocal reverse-mark degrees (2026-11-18)

A sufficient condition for the mixed Hall dual is now isolated in
`PF_I16_RECIPROCAL_REVERSE_MARK_DEGREE_CRITERION_2026_11_18.md`.

For a target (T) in cut block (Y_k), let (r_k(T)) be the number of **all** eligible fibers (F=(p,J)) in that block for which (T\in N_k(F)). Then the fiberwise bound
[
\delta(F)\le \sum_{T\in N_k(F)}\frac1{r_k(T)}
\tag{RD}
]
implies blockwise Hall. Indeed, for arbitrary (z_F\ge0),
[
\max_{F:T\in N_k(F)}z_F
\ge \frac1{r_k(T)}\sum_{F:T\in N_k(F)}z_F.
]
Summing over targets gives the mixed weighted dual (MR) immediately. Equivalently, each target splits its unit capacity equally among every eligible reverse-mark fiber; if each fiber receives at least its demand, trim the excess.

This is genuinely different from the failed uniform row allocation: shares are target-dependent and penalize high-collision targets. The reciprocal degree must count crossing and noncrossing fibers together. Restricted degrees are invalid for this test.

The next finite test, if implemented, is exact rational evaluation of
[
q(F)-\delta(F)=\sum_{T\in N_k(F)}1/r_k(T)-\delta(F)
]
for every fiber in each block. A negative fiber rejects this sufficient criterion at that order only; it does not refute Hall. No finite test has yet been run, and (RD) is not claimed as an all-orders theorem.


## Exact reciprocal-degree diagnostic: eight-port obstruction (2026-11-18)

The equal reciprocal target split criterion (RD), recorded in
`PF_I16_RECIPROCAL_REVERSE_MARK_DEGREE_CRITERION_2026_11_18.md`, has now been tested exactly at n=8. It fails for 98 of 424 fibers:
- cut 3: 90 negative fibers among 382; 1,356 targets; 17,100 fiber-target incidences;
- cut 5: 8 negative fibers among 42; 102 targets; 1,047 incidences.

The minimum exact slacks are
[
\min_{F\in X_3}(q(F)-\delta(F))=-169259/95760,
\qquad
\min_{F\in X_5}(q(F)-\delta(F))=-451/420.
]
The first cut-3 witness has (J=(2,8)), three child sources, eight retained targets, (q=22261/95760), and (delta=2). Its target reverse degrees range from 28 to 48.

Yet the aggregate reciprocal capacity surplus is (792) in cut 3 and (66) in cut 5, exactly target count minus total split demand. The failure is local concentration, not aggregate shortage. Thus equal reciprocal splitting is rejected, while a nonuniform allocation and mixed Hall remain open.

Audit: `PF_I16_RECIPROCAL_REVERSE_MARK_DEGREE_N8_OBSTRUCTION_2026_11_18.md`.
The continued n=8/n=10 workflow is [44392154434](https://github.com/syncgravity/Singular-Boundary/actions/runs/44392154434); its n=10 outcome is pending. The earlier run [44392067165](https://github.com/syncgravity/Singular-Boundary/actions/runs/44392067165) stopped after n=8 because the original harness incorrectly asserted that the sufficient criterion should pass; that harness has been corrected.
