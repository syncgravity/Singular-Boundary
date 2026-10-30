# Addendum — rigorous short-time mixed-response control and its limits

**Date:** 2026-10-29. **Status:** exact finite SU(2) Hamiltonian spectral-calculus theorem, not a solution of the connected deleted-face cap estimate.

Let K=H_f^--E>=0 on a finite compact SU(2) link product with unique physical ground state Ω. Put v=QOΩ and w=QWΩ for real, smooth, gauge-invariant multiplication observables. For t>=0 write C(t)=Re<v,e^{-tK}w>, and moments m_s(O)=<v,K^s v>, m_s(W)=<w,K^s w>. For t>=0:

**A1. Exact initial slope:** C'(0)=-M_1(O,W), with M_1=E_{Ω²} Γ(O,W). For adjacent Wilson plaquettes the six-edge skein gives the exact expression in PROOF_REPORT.md.

**A2. Gap-free first-order time certificate:**

    |C(t)-C(0)| <= t sqrt(m_1(O)m_1(W)).

Proof: C'(s)=-Re<K^{1/2}v,e^{-sK}K^{1/2}w> and ||e^{-sK}||<=1. Integrate s from 0 to t.

**A3. Gap-free second-order time certificate:** for smooth bounded O,W with finite m_3(O),m_1(W),

    |C(t)-C(0)+t M_1| <= (t²/2) sqrt(m_3(O)m_1(W)).

Proof: C''(s)=Re<K^{3/2}v,e^{-sK}K^{1/2}w> and C(t)=C(0)+tC'(0)+int_0^t(t-s)C''(s)ds. For SU(2) smooth magnetic potentials on compact finite link products, smooth OΩ and WΩ lie in all polynomial domains at fixed finite volume.

**A4. Long-time limitation:** neither A2 nor A3 bounds integral_0^∞ C(t)dt without a decay, signed-cancellation, or spectral-overlap estimate on the long-time interval. Indeed the exact center-even positive diffusion countermodel in PROOF_REPORT.md has M_1=0 and M_-1=1/(24 epsilon)-1/27 -> infinity. A2-A3 remain valid while its slow relaxation time diverges.

**Remaining Wilson-specific obligation:** at full retained magnetic coupling, bound the signed integral of C_{cap,neighbor}(t) in the actual connected asymmetric Penrose deleted vacuum, or prove the polynomial center-cap probability directly. Nothing in A1-A3 assumes or proves the desired regulator-uniform physical gap.
