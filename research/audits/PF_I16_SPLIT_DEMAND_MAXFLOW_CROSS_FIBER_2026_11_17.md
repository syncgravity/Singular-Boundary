# PF-I16: exact split-demand max-flow formulation for cross-fiber collisions

Date: 2026-11-17

## 1. Why uniform spreading was too restrictive

For each source x, let L_0(x) be its non-root leaves and d(x)=|L_0(x)|. Every source is represented in each fixed (parent,J) fiber corresponding to one of these leaves. To avoid double-counting sources, assign x the split demand 1/d(x) in each such fiber:
\[
\delta(p,J)=\sum_{x\in F(p,J)}\frac1{d(x)}.
\]
The sum of all fiber demands is exactly the number of complement sources.

The earlier uniform transport sent each fiber's demand equally to all targets in its row. A column overload only says that this particular symmetric allocation fails. It does not imply the weighted quotient Hall condition fails, because the flow may be rerouted nonuniformly.

## 2. Exact capacitated-flow equivalence

Fix a first-overcrowded-cut block k. Construct a network:
- source node \(\sigma\);
- one node for each nonempty fixed fiber \(F(p,J)\subseteq X_k\);
- one node for each target in the same-cut neighborhood of at least one such fiber;
- sink node \(\omega\).

Add capacities:
\[
\sigma\to F(p,J):\delta(p,J),\qquad
F(p,J)\to T:+\infty\quad(T\in N(F(p,J))\cap Y_k),
\]
\[
T\to\omega:1.
\]

A flow saturating every edge out of \(\sigma\) is exactly a feasible split-demand transport. By max-flow/min-cut, this exists iff
\[
\left|\bigcup_{(p,J)\in S}
(N(F(p,J))\cap Y_k)\right|
\ge\sum_{(p,J)\in S}\delta(p,J)
\]
for every fiber subfamily S in that cut block.

For n=8 and n=10, every d(x) divides 12. Multiplying capacities by 12 makes the network integral:
\[
c(\sigma,F)=\sum_{x\in F}\frac{12}{d(x)},\quad
c(F,T)=c(\sigma,F),\quad c(T,\omega)=12.
\]
Thus an ordinary integer max-flow computation exactly decides the split-demand quotient condition at these orders; no floating-point tolerance is involved.

## 3. Verifier

research/verification/verify_pf_i16_overcrowded_cut_split_maxflow.py

The verifier constructs same-cut fiber neighborhoods from the guarded-switch relation, uses exact integer capacities, and runs Dinic max flow. On failure, the residual source-side min cut reports:
- number of reachable fibers;
- number of their neighboring targets;
- total scaled demand;
- available scaled target capacity;
- deficiency;
- distribution of the witness fibers across first-overcrowded cuts.

The workflow is:
https://github.com/syncgravity/Singular-Boundary/actions/workflows/pf-i16-overcrowded-cut-split-maxflow.yml

The first execution failed immediately due only to sorting a None key (the terminal class) alongside integer cut labels. That output occurred before any graph construction. The ordering bug was corrected in commit 74413140a5867bd8533dd0a2a8a753f9b68a1422; the corrected run is
https://github.com/syncgravity/Singular-Boundary/actions/runs/44078442710

## 4. Proof boundary

A successful split-demand flow would prove a sufficient quotient Hall condition and hence source-level Hall for the multivalued-pi relation at that finite order. It would not by itself prove the condition for arbitrary s.

A failed flow would give a genuine obstruction to this equal-leaf split-demand reduction, not necessarily a Hall obstruction in the original source-target graph: source demand may be allocated nonuniformly among its leaf representations, and the original graph can have an integral matching even when this particular quotient flow fails.

No global all-orders cross-fiber theorem is claimed by this formulation alone.
