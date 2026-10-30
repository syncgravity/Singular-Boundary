# R3-IR-430 — Exact full-coupling Wilson plaquette response positivity, without target-cap ordering

2026-10-30. Finite original-link SU(2) Wilson Hamiltonian on a disk with dynamic boundary edges. All other neighboring and environmental plaquette couplings may be arbitrary. This theorem proves a real sign, but NOT the cap-survival sign.

Fix a plaquette g, and let H(t)=K+V_rest+t b_g(1-p_g) with b_g>0, p_g=Tr W_g/2 in [-1,1]. Let E(t) be its lowest physical eigenvalue in the actual Gauss-invariant link Hilbert space and Omega_t its unique positive normalized ground state. Define e(t)=E(t)-t b_g, the ground energy for K+V_rest-t b_g p_g.

The planar disk center-flux construction (R3-IR-402) supplies a unitary which changes the sign of p_g without changing any retained other face term. Consequently e(-t)=e(t). The Rayleigh-Ritz variational formula writes e(t)=inf_{||psi||=1}( <psi,(K+V_rest)psi>-t b_g<psi,p_g psi>), an infimum of affine functions: e(t) is concave for all real t.

The Hellmann-Feynman identity and finite-volume reduced resolvent R_t=Q_t(H(t)-E(t))^(-1)Q_t give

e'(t)=-b_g <p_g>_t,
e''(t)=-2 b_g² <Q_t p_g Omega_t,R_t Q_t p_g Omega_t> <=0.

Since e is even, e'(0)=0. Concavity makes e' nonincreasing, so for t>=0,

boxed: <p_g>_t >=0 and d/dt <p_g>_t
=2 b_g <Q_t p_g Omega_t,R_t Q_t p_g Omega_t> >=0. (PR-1)

Because Omega_t>0 almost everywhere and p_g is a nonconstant bounded function on original SU(2) links, Q_t p_g Omega_t is not identically zero. The second derivative is then strictly negative and the plaquette expectation is strictly increasing for positive b_g on every finite connected original-link disk. None of these statements assumes a regulator-uniform spectral gap.

The result controls the **source itself** under its own coupling. It does NOT compare the target-cap-biased state against the ordinary state, does not give a favorable sign for d/dt <k(W_f)>_t, and does not give the positive cap-biased cosh ordering needed for the completed-cage target. A putative inference 'positive plaquette magnetization implies cap survival' is unsupported. The same center-flux sign symmetry was used before, but the global monotone plaquette response follows rigorously from energy concavity.

All statements concern finite volumes. No regulator-uniform half-Haar cap coefficient, infrared gap, or continuum Yang-Mills mass gap follows.
