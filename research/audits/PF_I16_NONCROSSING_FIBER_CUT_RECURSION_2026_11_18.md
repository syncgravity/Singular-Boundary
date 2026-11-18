# PF-I16: noncrossing fiber cut recursion and crossing-boundary localization

Date: 2026-11-18

## Status

**Two all-orders cut-local lemmas proved.** They sharpen the blockwise split-demand reduction by separating a leaf fiber according to whether its deleted interval crosses the first crowded odd cut. Noncrossing fibers preserve the first crowded cut on both source and target sides and have at least two same-block lifts per canonical parent target. Crossing fibers are confined to two possible left endpoints (for cuts k>=5).

These are local structural results. They do **not** prove the blockwise quotient Hall inequality (BQH_k): collisions among different fibers (including noncrossing/noncrossing and crossing/noncrossing collisions) remain uncontrolled.

## 1. Definitions and parity

Let n=2s, let M be a perfect matching on [n], and write
m_j(M)=#{I in M: I crosses the cut j|j+1}.
For every odd j, m_j(M) is odd: the j vertices on the left are partitioned into internal matching pairs and one endpoint from each crossing interval. Hence m_j(M) is either 1,3,5,...

Let k be the first odd cut with m_k(M)>=3. Thus m_j(M)=1 for every odd j<k. Write X_k for this source block.

For a port tree T, write c_j(T) for its number of edges crossing cut j. The guarded relation has c_j(T)<=m_j(M). Let Y_k be the target class whose first odd cut with c_j(T)>=2 is k. Since T is connected, c_j(T)>=1 at every cut.

Let J=(a,b) be a non-root leaf of the chosen overlap spanning tree tau. Deleting its endpoints and order-compressing gives a parent source p=pi_J(M,tau). If J does not cross cut k, it lies wholly left (b<=k) or wholly right (a>k). The corresponding parent cut is
- k'=k-2 if J lies left of k;
- k'=k if J lies right of k.

## 2. Noncrossing source-block recursion

**Lemma 2.1 (first crowded cut is inherited).**
Suppose (M,tau) is in X_k and J is a non-root leaf interval that does not cross k. Then the parent source p lies in X_{k'}, with k' as above. The left case k=3 cannot occur.

**Proof.**

If J lies right of k, no endpoint is deleted before any cut j<=k. Thus every earlier odd parent cut j<k has matching load 1, and the parent cut k has load m_k(M)>=3. Hence the first crowded parent cut is k'=k.

Suppose J lies left of k. For k=3 this is impossible: m_3(M)>=3 requires all three ports 1,2,3 to be left endpoints of intervals crossing cut 3, leaving no two of them available as the endpoints of a matching interval J wholly in {1,2,3}. Thus k>=5 and k'=k-2>=3.

Fix an odd parent cut h<k'. The first h retained ports correspond to the first r original ports, where r=h+q and q in {0,1,2} is the number of endpoints of J among those r original ports. Since h<k-2, r<k. If q=0 or q=2, r is odd and J does not cross the original cut r. The original matching load there is 1, so the parent load at h is 1.

If q=1, then r=h+1 is even and J crosses the original cut r. The even-cut matching load m_r is even and positive, hence at least 2. The adjacent odd cuts r-1 and r+1 are both below k, so each has matching load 1. Moving a cut across one port changes matching crossing load by at most one; consequently m_r<=2 and therefore m_r=2. Deleting J removes exactly one interval crossing r, leaving parent load 1 at h.

At the parent cut k'=k-2, the corresponding original cut is k. Since J does not cross k, deleting J does not change its crossing load, which remains at least 3. Thus p has first crowded odd cut k'. QED.

## 3. Noncrossing target-block preservation

**Lemma 3.1 (cut load is preserved by a noncrossing inverse).**
Suppose J does not cross cut k and T is obtained by a valid guarded final switch at J from parent tree P. After order compression,
\[
c_{k'}(P)=c_k(T),
\]
where k'=k-2 for J left of k and k'=k for J right of k.

**Proof.**

Only the four switch endpoints can affect the cut count. Write them x_1<x_2<x_3<x_4. Alternation forces the marked pair and replaced edge to be either
\[
J=(x_1,x_3),\ e=(x_2,x_4),
\quad\text{or}\quad
J=(x_2,x_4),\ e=(x_1,x_3).
\]
The no-reinsertion guard leaves, respectively, S_1,S_2 or S_0,S_1.

If J lies left of the cut, then either all four endpoints lie left, or J=(x_1,x_3) and x_4 lies right. In the latter case e crosses the cut once, and each allowed local tree has exactly one crossing edge (the edge x_3x_4). Thus the local crossing count equals the replaced-edge crossing count.

If J lies right of the cut, then either all four endpoints lie right, or J=(x_2,x_4) and x_1 lies left. In the latter case e crosses once, and each allowed local tree has exactly one crossing edge (the edge x_1x_2). Again the local crossing count equals the replaced-edge crossing count.

All other edges are unchanged. Hence the total cut load is preserved. QED.

**Corollary 3.2 (a retained noncrossing fiber stays in the corresponding target block).**
Let x=(M,tau) be in X_k, let J be a noncrossing non-root leaf, and let T be a retained fiber target. Put p=pi_J(x) and P=P_J(T). Then p is in X_{k'}, P is in Y_{k'}, and T is in Y_k.

Indeed, Lemma 2.1 gives p in X_{k'}. Since P is in C_can(p), coordinatewise cut domination gives c_h(P)<=m_h(p)=1 at every earlier odd parent cut h<k'. Connectivity forces c_h(P)=1. Lemma 3.1 gives c_{k'}(P)=c_k(T). Since T is in Y_k, c_k(T)>=2, so P is in Y_{k'}. Conversely, for T, all earlier odd cuts h<k have m_h(M)=1 and hence c_h(T)=1, while the same cut identity gives c_k(T)=c_{k'}(P)>=2. Thus T is in Y_k.

**Corollary 3.3 (same-block row expansion).**
For a fixed noncrossing fiber F=(p,J) arising from X_k, every canonical parent target P in C_can(p) has at least two distinct guarded final-switch lifts at J; by Corollary 3.2 all of those lifts lie in Y_k. The lift sets for distinct P are disjoint by fixed-(J,T) inverse uniqueness. Consequently
\[
|N(F)\cap Y_k|\ge 2|C_{\rm can}(p)|.
\]
Using the sourcewise guarded branching bound at order n-2, this is at least 2^{s-1}.

This is a rowwise expansion statement, not a union bound for a family of fibers.

## 4. Crossing-boundary localization

**Lemma 4.1 (crossing leaf endpoints are localized).**
Suppose k>=5, x=(M,tau) is in X_k, and J=(a,b) is a non-root leaf of tau crossing cut k. Then
\[
a\in\{k-1,k\}.
\]
For k=3 the trivial bound is a in {1,2,3}.

**Proof.**

Assume instead a<=k-2. Then J crosses cut k-2. Since k-2 is odd and precedes the first crowded cut k, its matching load is exactly 1 by odd-cut parity. Thus J is the unique matching interval crossing cut k-2.

Every other interval crossing cut k must start at k-1 or k; there are only two such left endpoints. Since m_k(M)>=3, there are exactly two such intervals, say K and L. Both lie wholly to the right of cut k-2, and both overlap J. The root interval containing port 1 lies wholly to the left of cut k-2, because J is the unique interval crossing that cut.

Any matching interval not crossing cut k-2 lies wholly on one side of that cut. Therefore no overlap-graph edge joins the left-side intervals to the right-side intervals except through J. Both sides are nonempty (the root is on the left, K and L on the right), so J is an articulation vertex of the overlap graph. Every spanning tree of the overlap graph must give an articulation vertex degree at least two. This contradicts that J is a leaf of tau. Hence a>=k-1; since J crosses k, a<=k. QED.

## 5. What this does and does not close

Established for every order:

1. A noncrossing deleted leaf preserves the first crowded source block after the deterministic two-port compression.
2. The guarded inverse at a noncrossing leaf preserves the corresponding crowded target cut exactly.
3. Every retained noncrossing fiber has at least two same-block lifts per canonical parent target, with disjoint lift sets for distinct parent targets.
4. A crossing non-root leaf in X_k has left endpoint k-1 or k for k>=5.

Still open:

- BQH_k for arbitrary families of fibers.
- The capacity interaction between different noncrossing fibers, including fibers with the same parent source and different deleted intervals.
- The capacity interaction between crossing and noncrossing fibers. Lemma 4.1 reduces crossing marks to two endpoint classes, but does not make their lift neighborhoods disjoint from noncrossing rows.
- The all-orders mixed-fiber Hall theorem and the weighted one-link inequality.

In particular, the lower bound |N(F) intersect Y_k|>=2|C_can(p)| cannot be summed over fibers: different fibers can share child targets. No injective selector, fixed-parent representative, or target-disjointness conclusion is asserted.

## 6. Next proof obligation

The remaining blockwise problem can now be stated with a cleaner decomposition. For a fiber family S in X_k, split S=S_nc union S_cr according to whether J avoids or crosses k. The noncrossing fibers recursively project into the parent block X_{k'} and Y_{k'}, while crossing fibers have J left endpoint in {k-1,k} (for k>=5).

The next lemma must control the *mixed union*
\[
\left|\bigcup_{F\in S_{nc}\cup S_{cr}}N(F)\cap Y_k\right|
\ge \sum_{F\in S_{nc}\cup S_{cr}}\delta(F),
\]
including collisions between the two classes. The results above isolate the boundary fibers and prove exact cut transport for the interior fibers, but do not supply this aggregate capacity estimate.
