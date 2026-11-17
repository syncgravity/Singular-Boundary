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
