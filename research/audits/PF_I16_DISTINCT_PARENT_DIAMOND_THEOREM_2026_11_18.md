# PF-I16 distinct-parent source-diamond theorem: formulation and proof reduction

Date: 2026-11-18

## 1. Purpose and status

The unrestricted canonical third-mark implication is false. The explicit n=10 obstruction recorded in \`PF_I16_ALL_ORDERS_THIRD_MARK_PROOF_ATTEMPT_2026_11_18.md\` has coincident sibling parent sources \(p=q\).

This note isolates the genuinely distinct-parent case. It is a theorem target and proof reduction, not yet an all-orders theorem. The n=10 distinct-parent rooted-star verifier is running separately; no result is inferred from a queued or in-progress workflow.

## 2. Exact source-diamond setup

Let \(x=(M,\tau)\) be a child source, and let \(J,K\) be distinct, disjoint non-root leaves of its overlap tree. Write
\[
p=\pi_J(x),\qquad q=\pi_K(x),\qquad
r=\pi_K(p)=\pi_J(q).
\]
Assume \(p\ne q\).

The source-side hypotheses are:
1. \(K\) is the canonical non-root leaf of \(p\);
2. \(J\) is the canonical non-root leaf of \(q\);
3. both source deletions are valid and give the same common parent \(r\).

For a child target \(T\), assume:
1. \(T\) belongs to the retained fiber neighborhood for \((p,J)\);
2. \(T\) belongs to the retained fiber neighborhood for \((q,K)\);
3. the guarded reverse operations at \(J\) and \(K\) are mutually surviving.

Let \(P_J(T)\) and \(P_K(T)\) denote the exact guarded inverse targets. Mutual survival gives the common double inverse
\[
U=P_K(P_J(T))=P_J(P_K(T)).
\]
By the canonical-leaf hypotheses on \(p,q\), the two one-step parent targets are in the canonical neighborhoods of their respective parent sources. Reversing their final canonical marks gives \(U\in C(r)\), the ordinary (unrestricted-last-leaf) output neighborhood of \(r\).

The desired distinct-parent conclusion is the stronger statement
\[
\boxed{U\in C_{\rm can}(r).}\tag{DP}
\]
This is the distinct-parent canonical diamond assertion. It must not be conflated with target-side commutation, which only supplies the common \(U\), or with \(U\in C(r)\), which follows from either source route.

## 3. Exact reduction at the first nontrivial order

At \(n=10\), the common parent \(r\) has three matching intervals. Its rooted overlap tree is either:

- a rooted path, with exactly one non-root leaf; or
- a rooted star, with two non-root leaves \(A,B\), where \(A\) is lexicographically canonical.

For the rooted path, \(C(r)=C_{\rm can}(r)\), so (DP) is automatic.

For the rooted star, the exact rooted-star criterion already established is
\[
U\in C_{\rm can}(r)
\iff
A\text{ is a guarded reverse mark of }U
\quad\text{and}\quad
B\text{ survives after reversing }A.
\tag{S}
\]
The exhaustive unrestricted n=10 census showed that whenever \(A\) is valid, \(B\) survives after reversing \(A\). Its failures all came from \(A\) not being a reverse mark, and the explicit first failure had \(p=q\).

Thus the first distinct-parent theorem reduces to the source-to-target incidence statement:
\[
p\ne q\quad\Longrightarrow\quad
A\text{ is a valid guarded reverse mark of }U
\tag{A-DP}
\]
for every retained, mutually surviving sibling diamond over a rooted-star common parent.

This is the precise local lemma to prove or disprove. It is not yet established.

## 4. Why the attachment split matters

Let \(v_K\) be the attachment vertex in \(r\) of the added canonical leaf \(K\) in \(p=r+K\), and \(v_J\) the attachment vertex in \(r\) of \(J\) in \(q=r+J\).

If \(v_K\ne A\), then \(A\) remains a non-root leaf in \(p\); since \(K\) is canonical in \(p\), the compressed interval order places \(K\) no later than \(A\). Similarly, if \(v_J\ne A\), then \(J\) is no later than \(A\) in the separately compressed order of \(q\).

The only attachment geometry where neither source canonicality condition compares the newly added leaf against \(A\) is
\[
v_K=v_J=A.
\]
The two compressed coordinate systems are different. Therefore these inequalities cannot be compared directly across \(p\) and \(q\). The proof of (A-DP) must use the actual ordered four-port patterns, full endpoint-incidence equality, positive overlap, and the no-reinsertion guard.

The distinct-parent condition \(p\ne q\) excludes the known counterexample but does not, by itself, yet imply (A-DP).

## 5. Finite diagnostic and its scope

The diagnostic
\`research/verification/verify_pf_i16_n10_distinct_parent_third_mark.py\`
enumerates rooted-star sibling diamonds at \(n=10\), excludes \(p=q\), and separately records:
- number of distinct-parent source diamonds;
- common target incidences and mutual double-inverse survival;
- validity of canonical leaf \(A\) as a reverse mark;
- survival of \(B\) after the \(A\)-inverse;
- attachment types of the two added leaves.

The script checks the common double inverse and verifies that it is an ordinary output of the common parent. It is a finite census, not a proof for arbitrary \(n\). Its parent-output membership check is cached by common parent to avoid recomputing the full output set for every incidence.

The first run on the initial diagnostic was still in progress at run 44256861362. A cached version was committed later; its workflow run is 44257821334 and was queued at the last status check. No numerical distinct-parent conclusion is asserted in this note.

## 6. Proof obligation after the census

If the distinct-parent census has no failures, the next mathematical task is not to extrapolate from \(n=10\). Prove (A-DP) from the exact source and target constraints.

A viable proof must establish that in the exceptional attachment geometry \(v_K=v_J=A\), the two distinct source extensions impose enough endpoint-incidence constraints to force the canonical reverse pattern at \(A\). For all other attachment types, use the canonical order comparisons separately in \(p\) and \(q\), then translate them through the explicit compression maps. No step may silently identify the two compressed port orders.

If a distinct-parent counterexample occurs, record its full \((p,q,r,T,U)\) data and replace (DP) by the strongest correct restricted statement. In either case, the \(p=q\) fibers must be handled separately in the global mixed-fiber Hall proof; the known counterexample rules out absorbing them into (DP).

## 7. Proof boundary

Established:
- guarded target-side mutual-survival gives a unique common double inverse;
- the sibling source routes place that inverse in the ordinary common-parent neighborhood \(C(r)\);
- the rooted-star criterion (S);
- the finite unrestricted n=10 counterexample to the unrestricted canonical implication.

Open:
- the distinct-parent canonical diamond (DP);
- the rooted-star local lemma (A-DP);
- the all-orders mixed-fiber Hall inequality;
- the all-orders multivalued-\(\pi\) Hall theorem;
- the weighted one-link inequality unconditionally.
