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
