# R3-IR-449 — Exact shell information dissipation criterion

2026-10-30. Conditional theorem for the actual SU(2) Wilson vacuum probability measure. No physical decay rate is asserted.

Let J_r be mutual information between a fixed target cage and links outside radius r, and let D_r be its decrease when removing shell r. R3-IR-448 proves exactly J_r=J_(r+1)+D_r, with D_r nonnegative.

For J_r>0 define theta_r=D_r/J_r. Then theta_r lies in [0,1] and J_R=J_r times the product of (1-theta_k) for k=r through R-1. In particular if theta_k>=eta>0 on each intervening shell, then J_R<=J_r(1-eta)^(R-r). The cap influence energy is bounded by osc(O)^2 J_R/2, by R3-IR-448. None of this assumes Markov conditional independence.

The missing Wilson-specific hypothesis is an actual lower bound on D_r/J_r under physical refinement. Existing local heat-kernel minorization does not provide it. The mutual-information chain rule alone provides no rate: an abstract correlated remote variable may preserve information across arbitrarily many intermediate shells, only losing it at the last shell. This is a logical diagnostic, not a physical Wilson construction.

No uniform cap-survival or continuum mass-gap conclusion is established.
