# Independent one-sided spatial-tail pairing audit — 2026-11-02

For original-link finite SU(2) strip, let P_m denote left-prefix conditional expectation and T_{>m} the complementary future original links. Under the conditional Poincare inequality ||(I-P_m)H||²_2 <= kappa^(-1) sum_(e in T>m)||grad_e H||²_2 with kappa=23/144 and exact centering P_m w_m=0, ||w_m||₂<=v=1/1152, an arbitrary smooth H obeys
**|<w_m,H>| <= (v/sqrt(kappa)) (5/6)^r ||grad H||_{S,log(6/5),2}**, r=dist_link(T_{>m},S).
This follows directly by orthogonal projection, Cauchy–Schwarz, conditional Poincare and the deterministic spatial weight comparison; no prefix-gradient commutator or compact support of H is required. The mirror bound uses the independently derived right-prefix projection.

For bond supports S_k=E_k union E_(k+1), the **exact future-to-source link distance** when m>k is d(T_{>m},S_k)=m−k, distinct from the entire-bond support distance max(0,m−k−2). Source union for other bonds gives r=m−max{k<m}. We checked 26,488 reflection and filtration distances for N=2..44 and rational weighted-gradient inequalities.

Substituting weighted L2 and L4 semigroup assumptions reproduces the previously reported endpoint triple-integral coefficient 8.98216621302897e-8 and middle-time coefficient 4.49667708861093e-7, each multiplied by (5/6)^r. These time factors require separate semigroup analytic hypotheses and do not follow from the tail pairing alone. This is a narrow exact conditional implication, not a full SU(2) Poincare theorem, fourth-order extensive energy proof without conditions, interacting lambda=1 gap, or continuum Yang–Mills mass gap.

Full detailed mathematical audit and executable exact verifier, log, SHA256 are in the project Proof Audits Library.