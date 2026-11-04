# R3-IR-597 — Weighted-integral positive radial forcing controls one-sided log oscillation

Date 2026-10-31. This is an abstract radial comparison theorem, continuing the previous branch's signed-current problem, not a proof of the interacting Penrose deleted-vacuum bound.

## Theorem
Let L=π/2. Assume ψ>0, ψ is C² on [0,L], ψ'(0)=0, and ψ''+2cot(u)ψ'=qψ on (0,L), with q measurable and integrable enough for the displayed bound. Set O=sup_{0≤v≤u≤L}[logψ(u)-logψ(v)]_+. Then

**O≤∫_0^L(L-s)[q(s)]_+ ds**.

## Proof
Write z=ψ'/ψ. On every interval where z>0, z'=q-z²-2cot(u)z≤[q]_+ because cot(u)≥0. Each connected component (a,b) of {z>0} has z(a)=0 (center regularity when a=0), hence z(t)≤∫_a^t[q(s)]_+ds. For any [v,u], its positive log increment is no larger than the integral of z_+ over [0,L]. Partition the open set {z>0} into its component intervals, integrate and exchange order: ∫_a^b z(t)dt≤∫_a^b(b-s)[q(s)]_+ds≤∫_a^b(L-s)[q(s)]_+ds. Sum over disjoint components. This proves the bound. In particular, O≤(L²/2)||q_+||∞, recovering R3-IR-596.

If the earlier effective radial fiber equation **is independently verified** for the true nonlinear face-deleted ground state with q=(2/A_f)(W_f−λ_f), then O_f≤(2/A_f)∫_0^(π/2)(π/2−s)[W_f(s)−λ_f]_+ds. Thus a uniform bound on the weighted positive forcing divided by A_f of order o(h^-1/4) suffices for the previous branch's conditional O requirement. The weighted-integral criterion is weaker than the L∞ criterion, but need not be weaker than the signed interval-current criterion because it still discards cancellations.

## Checks and limitations
Deterministic numerical integration on synthetic positive center-symmetric radial capacities from R3-IR-595 verifies the inequality. At N=8,16,32,64,128 the weighted bound is approximately 207.47, 849.34, 3770.69, 19467.17, 129222.03, whereas the older bound using sup q is approximately 5571.54, 55594.94, 734914.28, 14810326.45, 554680938.77. These are test functions and do not approximate the true Penrose ground state. The numerical tests do not replace the analytic inequality.

**Open obligation:** identify or rigorously derive q or conditional score of the actual Gauss-invariant face-deleted vacuum and prove a regulator-uniform weighted forcing or signed-score bound. This theorem does not prove any Yang-Mills continuum mass gap.

Executable: ChatGPT Library /The Singular Boundary/Source/prove_integrated_radial_forcing_2026_10_31.py. Data: /The Singular Boundary/Source/integrated_radial_positive_forcing_2026-10-31.json.
