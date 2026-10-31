# R3-IR-522 — Local ground-state comparison without heat-bridge time penalty (2026-10-30)

Finite compact connected SU(2) link configuration space with scalar elliptic inverse-Whitney kinetic quadratic form, bounded unchanged magnetic background, and a selected boundary plaquette p_f=Tr(U_f)/2. Let H_b=H_0-b p_f with b>=0. Assume the switched-off H_0 has a **simple** normalized positive ground state Omega_0, energy E_0, and **interacting spectral gap** Delta_0>0 above E_0. Assume a free-edge center-flip unitary Z commutes with H_0 and anticommutes with p_f, so <Omega_0,p_f Omega_0>=0. Let Omega_b be the positive ground state of H_b.

By the variational principle E_b<=<Omega_0,H_b Omega_0>=E_0. The perturbed ground-state energy identity and p_f<=1 give
<Omega_b,(H_0-E_0)Omega_b>=E_b-E_0+b<Omega_b,p_f Omega_b> <= b.
The spectral gap of **H_0** gives
Delta_0 [1-|<Omega_0,Omega_b>|²] <= b.
Thus the pure-state trace distance is at most min(1,sqrt(b/Delta_0)). For EVERY measurable event A (in particular the double-center cap),
Prob_(Omega_b)(A) >= [Prob_(Omega_0)(A)-sqrt(b/Delta_0)]_+.
This avoids the exponential e^(-4bt) factor and all heat-bridge diagonal constants of R3-IR-520/521.

If center-flip symmetry is absent and m_0=<p_f>_0, the same argument gives the weaker bound sqrt(min(1,b(1-m_0)/Delta_0)) for b>=0, as E_b<=E_0-b m_0. The center-flip result above assumes m_0=0.

IMPORTANT: this is a **finite-volume weak relative-coupling** bound. It is useful only if b/Delta_0 is small relative to the event mass squared. Delta_0 is the INTERACTING switched-off gap (not the previously proved electric-only gap). No environment/refinement-uniform lower bound for Delta_0 has been established, and the strong-magnetic b/Delta_0 regime makes the bound vacuous. The theorem does not establish the Penrose refinement-uniform center-cap coefficient or continuum Yang–Mills mass gap. It is not a replacement for the original unresolved theorem.

Reproduction: research/scripts/validate_local_gap_state_comparison.py; tests positive two-level center-symmetric Hamiltonians for multiple b and gaps.
