# R3-IR-519 — Local finite-time semigroup domination with arbitrary magnetic environment

Date: 2026-10-30. Let H0=HE+Vrest be a finite open SU2 inverse-Whitney scalar uniformly elliptic Schrödinger operator with positive Feynman–Kac kernel. Let H_b=H0-b p_f, b>=0, |p_f|<=1, with identical kinetic coefficients and all other plaquette couplings fixed.

Feynman–Kac on paths from x to y multiplies the H0 path weight by exp(b∫_0^t p_f(X_s)ds), which lies in [exp(-bt),exp(bt)]. Thus the heat kernels obey exp(-bt)k0(t;x,y)<=kb(t;x,y)<=exp(bt)k0(t;x,y). After normalizing each kernel in its endpoint variable y, its endpoint probability ν_b,t^x obeys

exp(-2bt) ν_0,t^x(A) <= ν_b,t^x(A) <= exp(2bt) ν_0,t^x(A)

for all measurable endpoint events A and t>0. No total magnetic norm B=sum_{j!=f}b_j appears: the entire environment is retained inside both kernels. The operator need not split into free-link and environment factors; off-diagonal transported Whitney derivatives are allowed. More generally for H_b=H0-bp with p∈[pmin,pmax], the normalized factor is exp(±bt(pmax-pmin)). This proof uses only scalar positivity and boundedness of the changed multiplication observable.

CAVEAT: this is a **finite-time kernel endpoint comparison**, not a ground-state measure comparison. A normalized endpoint law from e^-tH_b 1 at a fixed start approaches an expression involving the positive ground-state eigenfunction Omega_b, but not automatically Omega_b² dHaar (which is the quantum equilibrium measure). The factors exp(±2bt) degenerate as t→infinity. To make it a ground-state cap estimate would require quantitative, environment-uniform semigroup mixing or a ground-state transform argument plus a controlled change of ground state. None is given.

Independent 2-state uniformly positive-kernel regression for b=0.8, background V=diag(0.7,-0.3), and t=0.25,1,2,5 verifies both unnormalized and normalized entrywise comparisons. The tested endpoint ratios remain moderate while the bound deteriorates exponentially, illustrating looseness rather than a counterexample. The check is in research/scripts/validate_local_semigroup_perturbation.py.

The theorem is valid at every fixed finite regulator. It proves neither a refinement-uniform shrinking double-center cap coefficient nor any continuum Yang–Mills mass gap.
