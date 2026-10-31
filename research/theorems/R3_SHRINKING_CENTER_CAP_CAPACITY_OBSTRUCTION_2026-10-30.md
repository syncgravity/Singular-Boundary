# R3-IR-516: vanishing double-center cap mass despite vanishing SU(2) electric energy

Date 2026-10-30. An explicit capacity obstruction to upgrading the fiberwise Haar comparison R3-IR-515 to a universal relative shrinking-center estimate using only a small link Dirichlet energy. This is a Hilbert-space counterexample, **not** a counterexample involving actual Penrose ground states.

Write U=cos(theta)I+i sin(theta)n·sigma with theta∈[0,pi]. Class Haar density is (2/pi)sin²(theta)dtheta; in the normalization -Delta chi_(1/2)=(3/4)chi_(1/2), radial Dirichlet energy is (1/4)∫|psi'(theta)|²dHaar. The double-center cap of width delta_r=1-cos(r) consists of theta≤r and theta≥pi-r. For 0<r<pi/4 define h_r(theta)=0 when d(theta)=min(theta,pi-theta)≤r, = (d-r)/r when r<d<2r, and =1 for d≥2r. Let psi_r=h_r/||h_r||_2. Then psi_r is a normalized nonnegative H1 wavefunction supported entirely OUTSIDE both center caps, so Prob_psi_r(C_delta_r)=0. The squared norm tends to 1; and its electric energy equals

E_r=[1/(pi r² ||h_r||²)] * ∫_r^(2r) sin²(theta) dtheta

= [1/(pi r² ||h_r||²)]* [r/2-(sin(4r)-sin(2r))/4], which is asymptotic to (7/(3pi)) r as r→0. This is O(sqrt(delta_r)); the SU2 double-center Haar probability is c_delta=(2/pi)[r-sin(r)cos(r)]~4r³/(3pi)=O(delta_r^(3/2)). Smooth compactly supported radial approximations to h_r can be made with a slightly enlarged zero neighborhood and the same energy order. This disproves a purported general implication 'E_e(psi)→0 implies a positive relative Haar cap coefficient for arbitrarily shrinking caps'. In particular any general energy-based estimate for relative cap mass must incorporate a cap-scale condition stronger than the mere E_e=o(1), or additional structural PDE information on ground states.

Numerically at r=0.25,0.125,0.0625,0.03125,0.015625, the normalized electric energies are approximately 0.18131555,0.09193313,0.04628327,0.02319150,0.01160263. All constructed cap probabilities equal zero. Reproduction research/scripts/validate_cap_capacity_obstruction.py.

This does not rule out a cap estimate from positive ground-state elliptic regularity with coefficients controlled appropriately at shrinking scales. Crucially, no physical Penrose ground-state estimate, refinement-uniform cap, or continuum Yang-Mills mass gap follows.
