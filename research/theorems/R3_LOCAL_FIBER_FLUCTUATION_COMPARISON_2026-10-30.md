# R3-IR-550 — Local fiber-fluctuation comparison without global amplitude normalization

**Scope:** exact finite-regulator theorem and a sufficient *conditional* refinement criterion. This does not prove uniform bounds for the physical Penrose Wilson vacuum.

Let the fundamental-face trace be p, normalized Haar conditional expectation P, and positive normalized ground-state amplitude Ω, HΩ=EΩ. Define

q(p)=PΩ(p),  s(p)=P(Ω²)(p),  r(p)=s(p)/q(p)²≥1.

The ground-state radial marginal relative to Haar is **s(p)=q(p)² r(p)**; normalization ∫s(p)w(p)dp=1. Here r is the squared coefficient-of-variation factor, not a radial current; its oscillation rather than absolute value governs the comparison.

The exact identity yields for any p,p' with positive conditional quantities

log[s(p)/s(p')]=2 log[q(p)/q(p')]+log[r(p)/r(p')].

Consequently, if Bq=osc_p log q<∞ and Br=osc_p log r<∞, then

**Pr_Ω²(A)≥exp(-2Bq-Br) Pr_Haar(A)**

for *every* radial measurable event A, including arbitrarily shrinking center caps. Proof: max s/min s≤exp(2Bq+Br); since ∫s w=1, min s≥exp(-2Bq-Br). This **removes the global L1 ground-state factor I²** from R3-IR-547. A uniform bound on Bq and Br suffices for a refinement-uniform multiplicative cap coefficient, but has not been established for the interacting Penrose Hamiltonian.

### Effective radial potential controls Bq

Under R3-IR-546 exact fundamental-cycle closure and the self-adjoint radial projection identity, q solves

-L_rad q+v_eff(p)q=E q,
v_eff(p)=P(VΩ)(p)/PΩ(p).

Let K_t^κ be the strictly positive, continuous SU2 radial heat kernel, bounded 0<m_t≤K_t≤M_t. Its Feynman–Kac representation gives

q(p)/q(p')≤exp[t osc(v_eff)] (M_t/m_t),

hence **Bq≤t osc(v_eff)+log(M_t/m_t)**.

Combining,

**Pr_Ω²(A)/Pr_Haar(A)≥exp[-2t osc(v_eff)](m_t/M_t)² exp[-Br].**

This is a finite-volume exact result, and is independent of I. Unlike the crude R3-IR-547 oscillation osc(V), only the radial oscillation of the Ω-weighted *effective potential* appears. An additive spectator potential independent of p can contribute a constant to v_eff; its oscillation therefore vanishes. The fluctuation factor Br still needs independent control for *interacting* spectators. No one-dimensional fixed-spectator Schrödinger reduction is assumed: the full kinetic mixed derivatives are retained within the projected equation and r.

For the original M5 radial κ=2.362228738429273, the n≥1 SU2 character kernel series satisfies S_t=Σ(n+1)² exp[-κn(n+2)t], and if S_t<1, (m_t/M_t)≥(1-S_t)/(1+S_t). Thus a completely explicit sufficient certificate is
exp[-2t osc(v_eff)] [(1-S_t)/(1+S_t)]² exp[-Br].

### Noninteracting spectator invariance

If Ω(p,y)=f(p)g(y) normalized, then q(p)=f(p) E_Haar g, r(p)=E_Haar g²/(E_Haar g)², independent of p. Thus Br=0 regardless of number of spectator links or how small ∫Ωdμ becomes. This repairs the artificial spectator penalty of R3-IR-547.

### Coupled two-rotor numerical test

For Ω(p,y) proportional to exp[-λp²-ηy²+τpy], with normalized independent SU2 Haar trace laws for p and y and (λ,η,τ)=(.7,.9,.5), 96-node Gauss-Jacobi integration and a 301-point p-grid gave Bq=0.6750825954, Br=0.03029613647, a direct local certificate exp(-2Bq-Br)=0.2514625198; directly normalized min relative marginal density approximately 0.3540. For τ=0, λ=.7, varying η through 0,1,5,20 leaves Br numerically zero and the certificate exp(-1.4)=0.24659696394 unchanged, including with arbitrarily concentrated spectator factor.

### Remaining physical obligation

To obtain a **refinement-uniform Penrose cap**, show for the *actual* Wilson-coupled Ω_h that (i) osc_p v_eff,h divided by the local diffusion time scale κ_h is controlled and (ii) osc_p log r_h is controlled (or a signed one-sided replacement). Neither follows merely from the elementary global potential bounds or ground-state kinetic energy. In particular, no uniform refinement matrices/couplings or interacting ground states were available for this turn. Nothing here proves a continuum 3+1 Yang–Mills mass gap.

Code: research/scripts/audit_local_fiber_oscillation.py; also archived as raw source in ChatGPT Library /The Singular Boundary/Source. No binary files committed to Git.
