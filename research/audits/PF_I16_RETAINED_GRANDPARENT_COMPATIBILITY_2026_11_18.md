# PF-I16: retained grandparent compatibility is weaker than canonical third-mark

Date: 2026-11-18

## Status

**Logical correction and a proved low-order retained-diamond lemma.** The earlier third-mark program demanded that a common double inverse U belong to C_can(r), where r is the common parent source. That is stronger than the actual multivalued-pi relation requires. The actual row condition is
\[
U\in N_\pi(r)
\iff
\exists L\in L_0(\tau_r):
\quad L\text{ is a valid guarded reverse mark of }U,
\quad P_L(U)\in C_{\rm can}(\pi_L(r)).
\tag{RG}
\]
Thus the relevant compatibility question is whether U belongs to the retained multivalued-pi neighborhood of r, not whether the canonical leaf of r itself is the final reverse mark.

For sources with at most three matching intervals, every ordinary guarded output is retained. This proves the relevant grandparent compatibility for the first nontrivial source-diamond order. It does not establish the corresponding statement for four or more matching intervals.

## 1. Exact distinction between the two conditions

Let r=(M,tau) be a source and C(r) its ordinary guarded output neighborhood. The canonical leaf-last neighborhood C_can(r) requires the lexicographically canonical non-root leaf of tau to be inserted last.

The retained multivalued-pi neighborhood is instead
\[
N_\pi(r)=
\bigcup_{L\in L_0(\tau)}
\{U:
L\text{ is a valid guarded reverse mark of }U,P_L(U)\in C_{\rm can}(\pi_L(r))\}.
\]
The deleted leaf L is allowed to be any non-root leaf. Only the *parent target* must be canonical for the parent source.

The inclusion N_pi(r) subseteq C(r) is immediate by forgetting the parent-canonical filter. No general inclusion between C_can(r) and N_pi(r) is asserted: C_can(r) fixes the final leaf of r but does not require the preceding parent target to be canonical, whereas N_pi(r) allows any leaf but imposes that parent-canonical condition.

The distinction matters in the rooted-star counterexamples. There, the common inverse U is not in C_can(r), because the canonical leaf A is not a valid reverse mark. But U has an ordinary history with the other leaf B last. Deleting B leaves a two-interval parent source, whose unique non-root leaf is automatically canonical. Hence U is in N_pi(r) despite not being in C_can(r).

So the counterexamples to the unrestricted and distinct-parent canonical diamond assertions do **not** disprove retained grandparent compatibility at that order.

## 2. Two-step canonical-suffix characterization

For any U in C(r), choose a guarded construction history
\[
\sigma=(I_1,\ldots,I_{t-1})
\]
in a parent-before-child order, where t is the number of matching intervals and the root interval is not inserted. Let L=I_{t-1} be its final inserted leaf. Reversing the last switch gives P_L(U), an ordinary output of the parent source r_L=pi_L(r).

The target U belongs to N_pi(r) exactly when there exists at least one such history (not necessarily the initially chosen one) whose last two inserted intervals are K,L, with K the canonical non-root leaf of r_L. Equivalently,
\[
U\in N_\pi(r)
\iff
\text{some valid history of U ends in }(K,L)
\text{ with }K=\operatorname{canleaf}(r_L).
\tag{2S}
\]
For the base case r_L with one matching interval, the parent target is the unique two-port tree and the canonical condition is interpreted in the usual base-case sense.

This is the exact "two-step canonical suffix" condition. It is weaker than requiring the canonical leaf of r itself to be the final insertion.

## 3. Theorem for sources with at most three matching intervals

**Theorem 3.1.** If r has at most three matching intervals, then
\[
N_\pi(r)=C(r).
\]

**Proof.**

The inclusion N_pi(r) subseteq C(r) is part of the definition.

If r has one matching interval, it is the terminal base source.

If r has two matching intervals, its rooted overlap tree has exactly one non-root leaf L. Every ordinary output is constructed by inserting L last. The parent source has one matching interval, so the parent target is the unique base target and is canonical. Thus every U in C(r) belongs to N_pi(r).

If r has three matching intervals, every ordinary construction history ends with one of the non-root leaves L of its rooted overlap tree. Delete L. The parent source r_L has exactly two matching intervals, whose overlap spanning tree is a single edge rooted at the interval containing port 1. It has exactly one non-root leaf. Therefore every ordinary output of r_L is automatically in C_can(r_L). The inverse of the final guarded switch at L is precisely the preceding target in the chosen history, so it belongs to C_can(r_L). Hence U belongs to N_pi(r). QED.

No assumption that the final leaf L is the canonical leaf of r is used.

## 4. Consequence for the n=10 sibling-source diamonds

In the sibling-source setup
\[
p=\pi_J(x),\quad q=\pi_K(x),\quad
r=\pi_K(p)=\pi_J(q),
\]
the common double inverse U is an ordinary output of r by the two source routes.

For a ten-port child source x, r has three matching intervals (six ports). Theorem 3.1 therefore gives
\[
U\in N_\pi(r)
\]
regardless of whether U belongs to C_can(r), and regardless of whether p=q.

This is the correct retained-relation statement at the first nontrivial sibling-diamond order. The n=10 canonical third-mark failures do not obstruct it.

## 5. What remains open at the next order

For a source r with four matching intervals, deleting a final leaf L leaves a three-interval parent source. Its canonical neighborhood can be a strict subset of its ordinary neighborhood: the rooted-star third-mark counterexamples already occur at that parent order. Thus the proof of Theorem 3.1 does not extend by the same one-line argument.

The next candidate theorem is the **retained grandparent diamond**:

> Under the exact sibling-source, retained-fiber, and mutually surviving hypotheses, the common double inverse U belongs to N_pi(r), without requiring U in C_can(r).

The first genuinely new test is when r has four matching intervals (eight ports), corresponding to a twelve-port child source. The necessary test is not merely whether U is an ordinary output of r; it is whether at least one valid final leaf L has parent projection P_L(U) in C_can(r_L).

A finite counterexample to this retained condition would invalidate this proposed rerouting primitive. A finite pass would be evidence only, not an all-orders proof.

## 6. Proof boundary

Established:

- The canonical third-mark condition U in C_can(r) is stronger than the actual retained multivalued-pi row condition.
- The exact retained condition is (RG), equivalently the two-step canonical suffix criterion (2S).
- N_pi(r)=C(r) for sources with at most three matching intervals.
- Hence the common inverse in every ten-port sibling-source diamond is retained at its six-port common parent, even in the explicit p!=q canonical-diamond counterexample.

Open:

- Retained grandparent compatibility for common parents with four or more matching intervals.
- Whether sibling-source hypotheses imply the two-step canonical suffix at those orders.
- How any retained grandparent diamond can be assembled into the mixed-fiber Hall inequality for arbitrary fiber families.

The all-orders mixed-fiber Hall theorem and the weighted one-link inequality remain open. No canonical third-mark claim is revived.
