# PF-I16: direct mixed-fiber Hall after the retained-grandparent counterexample

Date: 2026-11-18

## Status

**The retained-grandparent sibling-rerouting lemma is disproved at the first four-interval common parent. The all-orders multivalued-\(\pi\) Hall theorem remains open.**

The corrected twelve-port census is complete:
- Workflow: [44369690167](https://github.com/syncgravity/Singular-Boundary/actions/runs/44369690167)
- Checked-out commit: \`fad52bc96dc0d6385d03f4cc57b1057fca2aa03a\`
- Verifier: \`research/verification/verify_pf_i16_retained_grandparent_exact_census.py\`
- Fixed common parent: the four-interval source \(R\) in Section 2.

The fast exact-route controls passed, and the full enumeration completed successfully. Its result is a finite counterexample to a proposed local rerouting lemma, not a counterexample to Hall.

## 1. The all-orders theorem we still need

For a source \(x=(M,\tau)\), let \(L_0(\tau)\) be its non-root leaves. For \(J\in L_0(\tau)\), write \(p=\pi_J(x)\). A target \(T\) is retained through \(J\) exactly when:
1. \(J\) is a valid guarded reverse mark of \(T\);
2. the unique inverse projection \(P_J(T)\) belongs to \(C_{\rm can}(p)\).

For a fiber \(F=(p,J)\), let \(N(F)\) be its common retained child-target row and put
\[
d(x)=|L_0(\tau_x)|,\qquad
\delta(F)=\sum_{x\in F}\frac1{d(x)}.
\]
Every source contributes total demand one across its leaf fibers.

The exact quotient Hall target is
\[
\boxed{
\left|\bigcup_{F\in S}N(F)\right|
\ge \sum_{F\in S}\delta(F)
\quad\text{for every finite fiber family }S.
}
\tag{QH}
\]
This condition implies source-level Hall for the multivalued-\(\pi\) relation. The proof is the split-demand argument: for any source family \(A\), take all fibers touched by its leaves; their total demand is at least \(|A|\), and their row union is exactly the source neighborhood.

After the first-overcrowded-cut partition, it is enough to prove the blockwise form
\[
\boxed{
\left|\bigcup_{F\in S}N_k(F)\right|
\ge \sum_{F\in S}\delta(F),
\qquad N_k(F)=N(F)\cap Y_k,
}
\tag{BQH_k}
\]
for every odd cut block \(k\) and every fiber family \(S\) in that block. The terminal class is already handled, and the target blocks \(Q_{2s},Y_3,Y_5,\ldots\) are disjoint. Thus all blockwise inequalities imply full Hall.

This remains the central all-orders theorem. No sibling-diamond compatibility lemma is logically required by this reduction.

## 2. Completed exact census: the proposed grandparent rerouting fails

The fixed common parent is
\[
R=\left(
((1,4),(2,5),(3,7),(6,8)),
((0,1),(0,2),(2,3))
\right).
\]
Its non-root leaves are \(A=(2,5)\) and \(B=(6,8)\).

The corrected verifier enumerates all ten-port parent sources deleting canonically to \(R\), reconstructs the common twelve-port child matching and overlap tree, checks both exact parent projections, intersects the exact retained fiber rows, computes the common double inverse, and tests the actual retained condition \(U\in N_\pi(R)\).

Exact output:
- ten-port parent sources: 31,744;
- parent sources deleting canonically to \(R\): 42;
- candidate pairs with the same lifted matching: 1,506;
- exact sibling-source diamonds: 1,506;
- same-parent diamonds \(p=q\): 88;
- distinct-parent diamonds \(p\ne q\): 1,418;
- common-target incidences: 796,012;
- mutually surviving double inverses: 796,012;
- nonmutual common targets: 0;
- common inverses retained in \(N_\pi(R)\): 547,376;
- common inverses not retained in \(N_\pi(R)\): **248,636**.

The first unretained witness has
\[
J=(2,3),\qquad K=(4,5),\qquad p=q,
\]
where
\[
p=q=\left(
((1,6),(2,3),(4,7),(5,9),(8,10)),
((0,1),(0,2),(0,3),(3,4))
\right).
\]
The reconstructed child source is
\[
x=\left(
((1,8),(2,3),(4,5),(6,9),(7,11),(10,12)),
((0,1),(0,2),(0,3),(0,4),(4,5))
\right).
\]
The common child target and double inverse are
\[
T=\{(1,2),(2,3),(2,5),(4,5),(5,6),(6,7),(6,8),
(7,9),(9,10),(10,11),(10,12)\},
\]
\[
U=\{(1,2),(2,3),(2,4),(3,5),(5,6),(6,7),(6,8)\}.
\]
The exact reverse-mark checker finds no leaf \(L\in L_0(\tau_R)\) for which \(L\) reverses \(U\) and \(P_L(U)\in C_{\rm can}(\pi_L(R))\).

The witness has \(p=q\). Thus the proposed sibling rerouting fails even without distinct-parent complications. The full census also shows that the failure is not a rare exception within this fixed parent: 248,636 of 796,012 mutually surviving common-target incidences fail the grandparent retained test.

### Verifier validity

The replacement verifier corrects all identified defects in the previous diagnostic:
- exact \`local_records\`, \`inverse\`, and \`relabel_tree\` enforce the no-reinsertion guard and full endpoint-incidence condition;
- p=q is included;
- the two lifted parent matchings must agree;
- the union of lifted overlap-tree edges must be a tree;
- J and K must be non-root leaves;
- deleting J and K must recover p and q exactly;
- the two target inverse orders must agree.

It also passed controls for the known rooted-star retained reroute, the eight-port universal-coverage miss, and all 241 ordinary six-port source-target incidences.

The earlier run 44366065796 is superseded for proof purposes: it omitted the no-reinsertion guard, skipped p=q, and did not certify a common child source. Its output is not used in the conclusion above.

## 3. What this counterexample does not say

It does **not** refute:
- the multivalued-\(\pi\) source-target relation;
- the all-orders Hall theorem;
- the split-demand quotient inequality (QH) or blockwise inequality (BQH_k);
- the noncrossing cut recursion;
- the crossing-leaf localization theorem;
- the weighted one-link inequality.

The counterexample only refutes the proposed proof shortcut that a pair of sibling retained fibers can always be merged through a retained common-grandparent target. The two fibers can share a child target and have mutually surviving inverse operations while their common double inverse is not in the grandparent retained row.

Accordingly, no proof may sum or identify sibling fibers by assuming \(U\in N_\pi(R)\). Any use of a common inverse must keep track of the original target capacity and all its competing reverse marks.

## 4. Exact local formula for split demand

There is a useful source-side expression for \(\delta(p,J)\).

Let \(p=(M',\tau')\) be a parent source with at least two matching intervals. Let
- \(d=d(p)\) be the number of non-root leaves of \(\tau'\);
- \(a(p,J)\) be the number of non-root leaves \(I\) of \(\tau'\) whose intervals overlap \(J\);
- \(b(p,J)\) be the number of root or internal vertices \(I\) of \(\tau'\) whose intervals overlap \(J\).

Every child source \(x\) in the fiber \(F=(p,J)\) is obtained by adjoining \(J\) to the matching and adjoining exactly one tree edge \(J I\) to \(\tau'\), for an overlap-neighbor \(I\). These are all the possible child sources in the fiber.

If \(I\) is a non-root leaf of \(\tau'\), adding \(J I\) removes \(I\) from the leaf set and adds \(J\), so \(d(x)=d\). If \(I\) is root or internal, the old non-root leaves remain and \(J\) is added, so \(d(x)=d+1\). Therefore
\[
\boxed{
\delta(p,J)=\frac{a(p,J)}{d(p)}
+\frac{b(p,J)}{d(p)+1}.
}
\tag{D}
\]
For the one-interval parent base case, there is only the root attachment and \(\delta=1\).

This formula is exact, not an estimate. It replaces a sum over child sources by local data of the parent overlap tree and the interval \(J\). It may be useful in a cut-local capacity proof, because the demand depends only on which overlap-neighbors of \(J\) are leaves versus internal/root vertices.

For each fixed parent target \(P\in C_{\rm can}(p)\), the child lifts at fixed \(J\) are disjoint from the lifts of every other parent target \(P'\), by fixed-\(J\) inverse uniqueness. Thus the remaining collisions are precisely between different deleted intervals and/or different parent sources, not between two parent targets in the same fixed fiber.

## 5. Direct mixed-Hall formulation

The exact weighted dual of (QH) is
\[
\boxed{
\sum_F\delta(F)z_F
\le
\sum_T\max_{F:T\in N(F)}z_F
\quad\text{for every }z_F\ge0,
}
\tag{MR}
\]
with an empty maximum equal to zero. The blockwise version restricts \(F\) to one \(X_k\) block and \(T\) to \(Y_k\).

This is equivalent to (QH), by layer-cake decomposition of nonnegative weights into threshold sets. It is the right formulation for a proof that handles collisions: a target contributes only the maximum weight of its eligible reverse-mark fibers, not one unit for every incident fiber.

The direct proof problem is now:

> Establish (MR) for every nonnegative weight system on fibers in every cut block, using the noncrossing parent recursion and the crossing-leaf boundary localization, without identifying different fibers through a common retained grandparent.

A proof may construct a fractional allocation \(\lambda_{F,T}\ge0\) with
\[
\sum_{T\in N_k(F)}\lambda_{F,T}=\delta(F),
\qquad
\sum_{F:T\in N_k(F)}\lambda_{F,T}\le1.
\]
But the allocation must be genuinely nonuniform or otherwise account for target competition. The earlier uniform row allocation is already overloaded at ten ports; it cannot be revived by a cosmetic change of notation.

## 6. Current all-orders structural input

The following are proved for all orders and remain available:

1. Odd matching-cut loads are odd; the first crowded odd cut partitions the complementary source class.
2. The terminal class has Hall into \(Q_{2s}\).
3. Noncrossing deleted leaves preserve the first crowded source block after compression.
4. A guarded inverse at a noncrossing leaf preserves the corresponding target cut load exactly.
5. Each fixed noncrossing fiber has at least two same-block lifts per canonical parent target, disjoint for distinct parent targets.
6. For \(k\ge5\), a crossing non-root leaf in \(X_k\) starts at \(k-1\) or \(k\).
7. The full Hall theorem follows from (BQH_k) for all odd \(k\).

Finite exact split-demand flows at \(n=6,8,10\), blockwise flows at \(n=8,10\), and crossing-only flows at \(n=8,10\) remain evidence only. They do not establish the arbitrary-family union inequality.

## 7. Revised proof program

The proof effort should now stay on the direct mixed cut-block inequality, in this order:

1. **Use the demand formula (D).** Express every fiber weight using the number of overlapping parent leaves and internal/root vertices. Separate the two crossing endpoint classes \(a=k-1\) and \(a=k\), and all noncrossing fibers.
2. **Keep target capacity at the child level.** For each \(T\in Y_k\), its eligible fibers are exactly its valid guarded reverse marks together with parent-source canonicality. Do not replace this set by a single selected mark, and do not merge two marks through a grandparent unless the actual retained condition is checked.
3. **Prove a weighted reverse-mark inequality.** Establish (MR), perhaps by a canonical allocation on the reverse-mark set of each target combined with the noncrossing parent recursion. A target's capacity is one, irrespective of how many reverse marks it supports.
4. **Handle mixed boundary/interior families simultaneously.** Crossing-only finite flows do not control collisions with noncrossing fibers. The proof must treat the two endpoint classes and the interior fibers in one inequality.
5. **Only then invoke the block decomposition** to obtain full multivalued-\(\pi\) Hall and the weighted one-link inequality.

No new workflow is warranted by the grandparent counterexample alone. It disproves a proposed local lemma but does not provide a new numerical test of (BQH_k). The next computation should be selected only after a concrete candidate allocation or a sharper dual inequality is specified.

## 8. Final theorem boundary

**Proved:** the local cut lemmas, the terminal-class Hall theorem, the reduction from blockwise Hall to full Hall, the exact split-demand quotient formulation, and the exact demand formula (D).

**Disproved:** the proposed sibling-source retained-grandparent rerouting lemma at the fixed four-interval parent \(R\).

**Finite evidence:** exact split-demand Hall at \(n=6,8,10\); blockwise at \(n=8,10\); crossing-only at \(n=8,10\); exact sibling-grandparent failure census at twelve ports.

**Open:** (BQH_k) for arbitrary fiber families, hence all-orders multivalued-\(\pi\) Hall and the unconditional weighted one-link inequality.

No Yang--Mills mass-gap conclusion is claimed.
