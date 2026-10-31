# R3-IR-596 — One-sided radial Harnack comparison from positive effective forcing

Date 2026-10-31. This is a conditional one-dimensional differential-equation lemma for the deleted-face marginal, NOT a proof that the nonlinear Penrose interacting vacuum satisfies its hypotheses with scale-uniform constants.

## Statement

Let L=π/2, ψ∈C²([0,L]) be positive and radial-center regular with ψ'(0)=0. Suppose
ψ''(u)+2 cot(u)ψ'(u)=q(u)ψ(u), 0<u≤L, where q is bounded above and Q=esssup_{[0,L]}[q(u)]_+<∞.
Define O=sup_{0≤v≤u≤L}[logψ(u)−logψ(v)]_+.
Then

**O ≤ (Q L²)/2 = (π²/8)Q.**

If a correctly normalized effective radial potential equation for the genuine face-deleted vacuum has q=(2/A_f)(W_f−λ_f), then
O_f≤(π²/(4A_f))||(W_f−λ_f)_+||_∞.
Hence the sufficient scale condition sup_f ||(W_f−λ_f)_+||_∞/A_f=o(h^(−1/4)) yields the same one-sided oscillation estimate as R3-IR-594, provided all prior spectral and marginal assumptions hold.

## Proof

For any 0≤v≤u≤L, let r∈[0,u] minimize ψ on [0,u]. If r=u then ψ(u)≤ψ(v), so the positive increment is zero. Otherwise ψ'(r)=0 (at r=0 by center regularity; interior r by Fermat). Set y(t)=ψ(r) exp[Q(t−r)²/2], r≤t≤L. Then y(r)=ψ(r), y'(r)=0 and
(y''+2cot(t)y')/y=Q+Q²(t−r)²+2Q(t−r)cot(t)≥Q≥q(t)
on [r,L] (use continuity at 0). The Volterra integral form of the radial ODE with initial derivative zero, or the first-crossing comparison theorem with positive Green kernel for (sin²t ψ')'=sin²t q(t)ψ, yields ψ(t)≤y(t) for r≤t≤L. Therefore ψ(u)/ψ(v)≤ψ(u)/ψ(r)≤exp[Q(u−r)²/2]≤exp(QL²/2). Taking log and supremum proves the theorem.

This is a **sup-norm positive-part** condition, potentially more restrictive than the previous branch's signed interval-current condition; it is an independently verifiable sufficient condition, not an asserted improvement in strength. In the R3-IR-595 synthetic radial boundary-layer family, positive effective forcing becomes large, consistent with large one-sided oscillation.

## Execution and limitations

Executable check `check_radial_forcing_harnack.py` and data `radial_forcing_harnack_check_2026-10-31.json` are persisted in Library /The Singular Boundary/Source. Tests used an analytic manufactured radial profile, not the interacting Yang–Mills deleted vacuum; numerical maxima are sampled and do not establish any independent sup-norm certificate. The actual interacting conditional potential W_f, its regularity and a scale-uniform upper bound on (W_f−λ_f)_+/A_f remain unproved; no continuum mass gap is claimed.
