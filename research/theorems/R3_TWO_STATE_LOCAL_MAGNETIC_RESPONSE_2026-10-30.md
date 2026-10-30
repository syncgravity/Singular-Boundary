# R3-IR-511: two-dimensional Rayleigh–Ritz lower bound for boundary plaquette magnetization

Date 2026-10-30. Setup: finite interacting inverse-Whitney SU2 Hamiltonian H(b)=H(0)-b p_f, b>=0, with a plaquette f having a unique free link whose central flip Z satisfies ZH(0)Z=H(0), Zp_f Z=-p_f. Assume H(0) has a unique normalized positive ground state Omega0. Its center parity is even, so <p_f>_0=<p_f³>_0=0.

Define v0=<p_f²>_0>0 and s0=<p_f Omega0,(H(0)-E(0))p_f Omega0> >0; s0 is finite by elliptic regularity and the local carré-du-champ identity. Use the orthonormal trial vectors Omega0 and p_f Omega0/sqrt(v0). Compression of H(b)-E(0) to their span is EXACTLY the symmetric matrix [[0,-b sqrt(v0)],[-b sqrt(v0),s0/v0]]. The (negative) smaller Ritz eigenvalue gives

E(0)-E(b) >= [sqrt((s0/v0)^2+4b²v0)-s0/v0]/2.

E is concave, hence for a simple analytic ground state m(b)=-E'(b)>=[E(0)-E(b)]/b. Therefore

m(b)>= 2 b v0 / [sqrt((s0/v0)^2+4b²v0)+s0/v0].

The local electric Dirichlet sum rule supplies s0<=C_f q0=C_f(1-v0), where C_f=(g2²/2)lambda_max(K_ff), as the zero-coupling mean vanishes. Replacing s0/v0 by C_f(1-v0)/v0 weakens the right side but leaves an explicit coupling/geometric/zero-coupling-variance inequality. The magnetization bound also yields q(b)=<1-p_f²>_b <=2[1-m(b)], since 1-p²<=(2)(1-p), and a corresponding fixed-delta cap bound by Markov; these consequences are usually weak unless the magnetization bound is near one.

Limits: for fixed v0 and s0, the estimate approaches sqrt(v0) as b grows, NOT one. In the standalone Haar rotor v0=1/4, so the large-b magnetization lower estimate tends to 1/2 although actual rotor localizes near +I. A uniform zero-coupling variance lower bound itself is UNPROVED for the Penrose environment. Thus this is a rigorous finite-volume, nonperturbative localized variational result but NOT the desired refinement-uniform double-center cap or continuum Yang-Mills mass gap.

The two-state formula is verified independently for exact 2x2 reflected Hamiltonians, and the SU2 Haar rotor zero-coupling data pass the test in research/scripts/validate_two_state_center_response.py.
