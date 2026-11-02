# All-orders cut-strength weighted-gradient majorant — 2026-11-02

**Conditional theorem:** For the finite open SU(2) square strip with the physical original-link cut, let H(t)=L0+tVcut with a=2||Vcut||∞≤269/36000, κ=23/144, and ||∇Vcut||∞≤G=√30·15989/1728000 on a fixed cut-local source S. Assume the archived *cut-reference* weighted L4 Poisson-gradient bound B=120/11, interpolated L4 centered resolvent C4=2√2/κ, conditional right-prefix Poincaré, and exact centering of right bonds w_k. These analytic assumptions are not independently proved by the arithmetic checker.

Normalize the positive eigenvector by mean one, φ(t)=1+Σ_n≥1 t^n f_n, not ||φ||₂=1. For A=Vcut−〈Vcut〉, R=L0^-1 Q, define e_n=〈A f_(n−1)〉, e1=0 and

f_n=−R[A f_(n−1)−Σ_(m=2)^(n−1)e_m f_(n−m)].

The L2 coefficient-majorant M solves M=z(1+M+M²), z=at/κ. The L4 amplitude-majorant is H=C4 a t/[1−C4 a t(1+M)], and weighted L4 gradient-majorant is D=B G t(1+H)/[1−B a t(1+M)]. All denominators are positive throughout t∈[0,1]. At t=1: M=0.049197424555885896, H=0.15365300988559435 and D=0.6974777376801158.

For a right residual bond k≥j+2 across cut after face j, μ_t(w_k)=〈w_k φ²〉/〈φ²〉, the denominator is ≥1, and exact right-prefix centering plus the spatially weighted L4 Leibniz inequality yields

**sup_(0≤t≤1)|μ_t(w_k)| ≤ 0.003495428301864162 (5/6)^max(0,k−j−2).**

This controls *all* cut-strength powers collectively, conditional on the weighted L4 analytic inputs, and removes the distance-independent nonlinear cut-remainder obstruction for one distant residual bond. It does **not** prove four-point connected energy clustering, fourth-order extensivity, interacting λ=1 gap, or continuum Yang–Mills mass gap.

Complete detailed mathematical report, independent finite-state recursion checker, log, and SHA-256 manifest archived in Library /The Singular Boundary/Proof Audits.