# R3-IR — Spectator-tilt entropy identity (2026-10-31)

Finite-volume exact original-link SU(2) identity. Let Ω>0 be the deleted-face Wilson ground state, with starts (x,z),(x',z) differing only on S. Fix heat time t>0. Let Z be free spectator diffusion and B_x(y;Z)>0 the Feynman–Kac changed-link bridge factor at common endpoint y after separating spectator-only V0 from incident V1. Form normalized reference measure π0 on (Z,y) with density proportional to e^(−∫V0(Z)) B_x'(y;Z) Ω(y,Z_t), relative to spectator free path law and Haar y. Put L=log(B_x/B_x') and πλ=e^(λL)π0/Eπ0 e^(λL).

**ST-1 exact:** Ω(x,z)/Ω(x',z)=Eπ0 e^L.

**ST-2 exact:** log[Ω(x,z)/Ω(x',z)]=Eπ0 L+∫_0^1(1−λ)Var_πλ(L)dλ = Eπ0 L + D_KL(π0||π1). Thus a signed conditional bridge mean alone does not control the full ground-state ratio. Spectator-only V0 cancels from L at fixed paths but **remains in the posterior π0**.

**Conditional criterion:** if |Eπ0 L|≤m_h and sup_λ Var_πλ(L)≤v_h for every pair of orbit starts, then |log Ω(x,z)/Ω(x',z)|≤m_h+v_h/2 and log orbit-density ratio R_z≤2m_h+v_h. Neither condition is currently proved at Wilson refinement scale.

**Counterexample:** L=±a each with probability 1/2, E L=0 but log E e^L=log cosh(a), arbitrarily large.

Numerical verification: 5000 random finite positive-measure tests; maximal quadrature error 2.49e−14, zero negative KL violations. Full theorem, verifier, JSON results, SHA256 manifest: Library `/The Singular Boundary/Proof Audits/R3_IR_SPECTATOR_TILT_ENTROPY_IDENTITY_2026-10-31.zip`. Refinement-uniform signed current, covariance and continuum Yang–Mills gap remain OPEN.