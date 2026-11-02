# Second cut-strength coefficient: conditional spatial localization (2026-11-02)

Let H_t=L0+tV, where L0 is the factorized original-link cut generator, ||V||∞≤c=269/72000, gap(L0)≥κ=23/144. Set A=V−〈V〉0 and R=L0^-1 Q. For the normalized positive ground vector h_t=1+t h1+t²h2+O(t³), exactly h1=−RA, h2=RQ(A RA)−(1/2)||RA||² 1. For centered right residual bond w_k, its t² expectation coefficient is **a₂(w_k)=2〈w_k,RQ(A RA)〉+〈w_k,(RA)²〉**. Centering A is essential; the squared term records ground-state normalization.

Assume archived weighted L² and L⁴ Bochner/Poisson bounds apply to the factorized cut generator, with B=120/11, right-prefix conditional Poincaré κ=23/144, ρ=6/5, residual norm v=1/1152 and complete local cut gradient bound G=√30·15989/1728000. For a cut after face j and distant k≥j+2, let d≥max(0,k−j−2) be future-link distance from the cut-potential support. Leibniz, L² weighted resolvent, L⁴ weighted resolvent, and interpolated ||RA||₄≤4√2 c/κ give:

|a₂(w_k)|≤[2v(B/√κ)(2cBG+2cG/κ)+(v/√κ)·2(4√2 c/κ)BG]·(5/6)^d

=**0.0006259326472751424·(5/6)^d**, volume uniformly. The two components are 0.0003081347450998358 and 0.0003177979021753067. This is a *conditional coefficient* result, not all-t locality or an all-orders spatial sum. Explicit independent 4-state rational Taylor recursion yields nonzero test coefficient −3/64; arithmetic tests pass. The SU(2) weighted Bochner assumptions have not been independently proved by the checker. Fourth-order extensivity, physical interacting λ=1 gap and continuum Yang–Mills mass gap remain open.

Full proof, verification script, execution log, SHA256 manifest available in Library /The Singular Boundary/Proof Audits.