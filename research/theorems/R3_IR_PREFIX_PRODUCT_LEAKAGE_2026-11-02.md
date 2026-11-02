# R3-IR — Prefix-product leakage for third-order insertions (2026-11-02)

**Exact algebra.** With P_j conditional expectation onto all original links of the old prefix, w_j a bounded next-face residual and P_j w_j=0, for every u∈L²:
P_j(w_j u)=P_j[w_j(u−P_j u)] and **||P_j(w_j u)||₂≤||w_j||∞||(1−P_j)u||₂**. Also
w_j u=w_jP_j u + P_j[w_j(1−P_j)u]+(1−P_j)[w_j(1−P_j)u].
The first term is prefix-centered but need not be small in norm.

**Conditional physical-strip consequence.** Taking u=R w_i for an earlier residual i<j and using the previously certified full-strip future-link conditional Poincaré and weighted gradient Poisson estimate, with r the physical link-graph distance from future links to support(w_i),
||P_j(w_j R w_i)||₂ ≤ [1440/(1152·11√23)](5/6)^r||∇w_i||₂
≤ 0.000303838993 (5/6)^r.
This is a stronger L² *old-sector leakage* estimate than the scalar two-bond pairing.

**Unresolved centered term.** The same hypotheses do not control ||w_j P_j Rw_i|| in distance. An exact product-model example u=x, w_j=y, x,y independent centered ±1 shows (1−P_j)u=0, P_j(w_j u)=0 but ||w_jP_j u||₂=1. Thus the third-order chain <w_k,RQ(w_jRw_i)> is not yet bounded by the leakage estimate alone. A spatially connected product estimate and cancellation across the six permutations remain necessary. No interacting λ=1 or continuum mass-gap result follows.

Full detailed proof, verifier, execution log, SHA-256 manifest archived in Library /The Singular Boundary/Proof Audits.