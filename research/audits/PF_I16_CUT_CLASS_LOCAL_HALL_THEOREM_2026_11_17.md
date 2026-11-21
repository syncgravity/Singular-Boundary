# PF-I16: same-first-overcrowded-cut local Hall theorem

Date: 2026-11-17

## Definitions

For a source \(x=(M,\tau)\) on \(2s\) ports, write
\[
m_k(M)=|\{[a,b]\in M:a\le k<b\}|.
\]
Because the overlap graph \(H_M\) is connected, \(m_k\ge1\) at every cut. Also \(m_k\equiv k\pmod2\).

Let \(K_{2s}\) be the tree-overlap source class. Every source outside \(K_{2s}\) has a unique first odd cut
\[
k(x)=\min\{k\in\{1,3,\ldots,2s-3\}:m_k(M)\ge3\}.
\]
Write \(X_k=\{x:k(x)=k\}\).

For a port tree \(T\), put
\[
c_k(T)=|\{ab\in E(T):a\le k<b\}|,
\]
and let its first overloaded odd cut be the first odd \(k\) with \(c_k(T)\ge2\). Write \(Y_k\) for this target class and \(Q_{2s}\) for the trees with \(c_k(T)=1\) at every odd cut.

Let \(R_{2s}\) be the multivalued-\(\pi\) guarded-switch relation: a child target is retained when some non-root leaf interval \(J\) is inserted last and its inverse parent target belongs to the canonical leaf-last neighborhood of the parent source.

## Theorem

For every \(s\ge3\), every source \(x\in X_k\) has at least
\[
\boxed{|N_{R_{2s}}(x)\cap Y_k|\ge 2^{s-2}.}
\tag{L}
\]

Consequently, for every fixed parent/deleted-interval fiber
\[
F(p,J)=\{x:\pi_J(x)=p\},
\]
the restricted bipartite graph from \(F(p,J)\) to \(Y_k\) satisfies Hall, where \(k\) is the common first-overcrowded cut of the sources in the fiber.

## Proof

We use induction on \(s\). The canonical parent neighborhood of every source on \(2(s-1)\) ports has at least \(2^{s-2}\) distinct targets, by the guarded-switch witness lemma. For a fixed deleted interval \(J\), inverse final switching is unique, so lifts of distinct parent targets are disjoint.

The key local observation is how a final switch changes the crossing count at a fixed cut \(k\).

**Case A: \(J\) does not cross \(k\).** Its endpoints lie on one side of the cut. Any admissible old edge \(e\) overlapping \(J\) either lies on that same side or crosses \(k\). In the first case the local four-vertex switch changes no crossing edge at \(k\). In the second case the four endpoints split \(3+1\) across the cut, so every connected local tree has exactly one crossing edge; the old crossing edge is replaced by exactly one crossing edge. Thus \(c_k\) is preserved.

Deleting \(J\) and compressing the labels preserves the matching crossing count at the corresponding cut. If \(J\) lies left of \(k\), the parent cut is \(k-2\); if \(J\) lies right of \(k\), it is \(k\). The parent source therefore lies in \(X_{k-2}\) or \(X_k\), respectively. By induction, at least \(2^{s-3}\) canonical parent targets have crossing count at least two at that parent cut. Each has at least two guarded final-switch lifts, and both preserve the cut count. Distinct parent targets have disjoint lifts. Hence there are at least
\[
2\cdot2^{s-3}=2^{s-2}
\]
child targets in \(Y_k\).

**Case B: \(J\) crosses \(k\).** The parent cut corresponding to \(k\) is \(k-1\), and every parent port tree \(P\) has at least one edge crossing that cut.

If \(P\) has a crossing edge \(e\) not contained strictly inside \(J\), then \(e\) overlaps \(J\). The endpoint order is either interleaving or \(J\) is nested inside \(e\). In either case, one of the guarded middle-centered stars survives and replaces one crossing edge by two, so the child crossing count at \(k\) is at least two.

If every crossing edge of \(P\) is contained strictly inside \(J\), take the guaranteed no-reinsertion witness edge \(e\) from the connected-tree switch lemma. It overlaps \(J\) but is not contained inside \(J\); under this case assumption it cannot cross \(k\), so it lies entirely on one side. The four endpoints split \(3+1\), and the local switch introduces exactly one crossing edge while leaving all existing crossing edges untouched. Since \(P\) already had at least one crossing edge, the child has at least two.

Thus every canonical parent target has at least one guarded final-switch lift in \(Y_k\). Distinct parent targets have disjoint lifts, and there are at least \(2^{s-2}\) parent targets. This proves (L) in the crossing case.

**Base case \(s=3\).** The only possible first-overcrowded cut is \(k=3\). Since there are only three matching intervals, all three cross this cut. Hence every non-root leaf \(J\) crosses \(k\), and Case B gives at least one child lift for each of the at least two canonical parent targets on four ports. Thus (L) holds with lower bound two.

This completes the induction.

Finally, a fixed fiber \(F(p,J)\) has at most \(s-1\) sources, since the new interval \(J\) can be attached to at most the \(s-1\) parent intervals in the overlap tree. All sources in this fiber have the same matching (the parent matching plus J) and hence the same first-overcrowded cut. They also have the same leaf-last target neighborhood: their parent overlap tree is identical, and the parent-before-child switch history followed by insertion of J depends only on the parent source, J, and the current parent port tree—not on which parent interval is the unique overlap-tree neighbor of J. Therefore (L) gives
\[
|N(F(p,J))\cap Y_k|\ge2^{s-2}\ge s-1\ge|F(p,J)|
\]
for \(s\ge3\). Hall holds on each individual fixed fiber.

## What this does not prove

Different \((p,J)\) fibers can share targets. Hall for each fiber separately does not imply Hall for an arbitrary union of fibers. The remaining global task is to prove a capacity-sensitive Hall inequality for unions of fibers, for example the split-demand quotient condition. This theorem supplies the exact local expansion and same-cut support needed for that reduction, but it does not yet establish the full complement matching or the weighted one-link inequality.
