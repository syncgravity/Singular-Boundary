# R3-IR-547 — Finite-regulator multiplicative cap bound via projected ground-state amplitude

Date 2026-10-30. This is a **finite-dimensional conditional theorem**, not a uniform Yang–Mills result.

Let X=SU(2)^E with normalized product Haar μ, p=Tr(W_f)/2 for a **fundamental face** in a fixed rooted transport tree. Assume a positive self-adjoint electric diffusion operator -L with divergence-free first-order generators, smooth SPD inverse-Whitney coefficients, and exact radial closure Lφ(p)=κ[(1-p²)φ''(p)-3pφ'(p)] for κ>0. Let H=-L+V on X with bounded real multiplication potential V, smooth unique normalized positive ground state Ω, HΩ=EΩ, ∫Ω²dμ=1. Let w(p)=2/π sqrt(1-p²) and denote the normalized Haar conditional expectation P onto functions of p. Since L is symmetric and the radial subspace is invariant, P L=L_rad P on smooth functions.

Write q(p)=PΩ(p)>0 and F(p)=P(VΩ)(p), so
 -κ[(1-p²)q''-3pq']+v_eff(p)q=Eq, with v_eff=F/q ∈[inf V,sup V] pointwise. This *effective potential* involves the Ω-weighted **Haar-fiber** average, not the Ω²-conditionals in the radial Ward identity R3-IR-545.

Let K_t(p,p') be the positive kernel of exp(t L_rad) relative to w(p')dp', and let 0<m_t≤K_t≤M_t<∞ on [-1,1]². By Feynman–Kac and the eigenfunction identity q=e^{tE} exp(t[L_rad-v_eff])q,
  q(p)/q(p') ≤ exp(t osc(V)) M_t/m_t =: R_t.
Set I=∫Ωdμ=∫q(p)w(p)dp. Since q_max≤R_t q_min and ∫q w=I, q(p)≥I/R_t.
By conditional Jensen, P(Ω²)(p)≥(PΩ(p))²=q(p)². Therefore for ANY measurable p-event A,
  Pr_{Ω²μ}(A) ≥ I² exp(-2t osc V) (m_t/M_t)² μ_Haar(A).
In particular this applies to both-center caps C_delta for every delta>0. The factor I is strictly positive at any finite compact regulator. It need not be bounded below under refinement; nor need osc V. This method supplies a **finite-model multiplicative** cap certificate but NOT the required uniform coefficient.

## Certified elementary SU2 radial-kernel constants

For radial diffusion κ[(1-p²)∂p²-3p∂p], the orthonormal SU2 characters U_n(p) (Chebyshev of second kind) obey L_rad U_n=-κ n(n+2)U_n and |U_n(p)|≤n+1. Hence K_t(p,p')=Σ_n≥0 exp[-κ n(n+2)t] U_n(p)U_n(p'). Define S_t=Σ_n≥1 (n+1)² exp[-κ n(n+2)t]. Whenever S_t<1, 1-S_t≤K_t≤1+S_t, yielding explicit certificate
  Pr(C_delta)/c_delta ≥ I² exp[-2t osc V] [(1-S_t)/(1+S_t)]².

For original archived M5 inverse Whitney κ0=2.362228738429273 (without an additional overall g²/2 factor; scale diffusion time consistently otherwise), Python double-precision evaluations give:
t=.3 S=.508690467095, coefficient (excluding I and V) .106049857511;
t=.5 S=.116375275865, coefficient .626491666984;
t=1 S=.003344710433, coefficient .986710207953.
These are easily made rigorous by elementary exponential series upper bounds or interval arithmetic; presented floating-point values are diagnostic, while the inequalities with exact infinite S_t are mathematical.

## Nonuniformity stress test

Even spectator degrees of freedom with no influence on the observed face can shrink I: for normalized independent positive rotor factors ψλ(p)=Zλ^-1/2 exp(-λp²), I_single=Z_(λ/2)/sqrt(Zλ). At λ=5, I_single≈.808531; for 30 independent factors I²=(I_single)^60≈2.896e-6, although the *marginal on a separate untouched Haar face can remain exactly Haar*. This proves that the I² factor of the new certificate is an artifact of a global amplitude projection and can deteriorate solely with spectator volume.

## Open issue

Need a conditional heat-kernel comparison bypassing global I or a volume-independent local logarithmic score estimate; must also bound effective potential oscillation locally, not via whole-graph osc V. Exact closure alone does not prove refinement uniformity, nor the 3+1 dimensional Yang–Mills mass gap.

Reproducer: research/scripts/audit_fundamental_radial_heat_kernel_bound.py; script also in ChatGPT Library /The Singular Boundary/Source. All binary data remain Library-only.
