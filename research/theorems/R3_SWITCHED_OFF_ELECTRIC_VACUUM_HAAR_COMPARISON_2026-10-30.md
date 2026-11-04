# R3-IR-514 — Switched-off Penrose ground state compared to electric Haar vacuum

Date: 2026-10-30. Finite connected 11-face OPEN disk with the gauge-covariant inverse-Whitney electric quadratic form; magnetic couplings nonnegative. This is a dynamical statement about the ACTUAL switched-off Hamiltonian, not an inference from parity alone.

Let H0=HE-sum_(j != f) b_j p_j with p_j=Tr(U_j)/2, B0=sum_(j != f)b_j. Define c=g2_squared/(2 lambda_max(M)), and T=sum_e (-Delta_e), with link fundamental Casimir 3/4. The previously verified finite electric form comparison HE>=c T gives a Poincare estimate HE>=gamma (I-|1><1|), gamma=3g2_squared/(8 lambda_max(M)). Here 1 denotes the normalized constant in product Haar L²(SU2^E). The inequality is on the whole configuration Hilbert space, hence also on the gauge-invariant subspace. All electric transports annihilate 1.

Let Omega0 be the normalized positive ground state of H0 (uniqueness follows for the scalar smooth uniformly elliptic divergence-form operator on the compact connected SU2^E). Since <1,H0 1>=0 (each elementary plaquette fundamental character has zero product Haar integral), E0<=0. The potential satisfies Vrest>=-B0. Therefore

 gamma (1-|<1,Omega0>|²) <= <Omega0,HE Omega0> <= B0.

Consequently the vector-state trace distance between normalized pure states Omega0 and 1 is sqrt(1-|<1,Omega0>|²) <= min(1,sqrt(B0/gamma)). Any event A determined by measurable link holonomies, and in particular any plaquette trace event, obeys the sharp projective-measurement contraction

 |Prob_Omega0(A)-Prob_Haar(A)| <= min(1,sqrt(B0/gamma)).

Thus for the deleted-face or switched-off face double-center event C_delta={|Tr(U_f)/2| >=1-delta}, since its product-Haar marginal is SU2 Haar,

 Prob_Omega0(C_delta) >= max(0, c_delta - sqrt(B0/gamma)),

 c_delta=(2/pi)[arccos(1-delta)-(1-delta)sqrt(2delta-delta²)].

This is an explicit, rigorously derived finite-geometry zero-local-coupling near-center MASS lower bound for the full inverse-Whitney interacting environment, not merely the parity identity. It holds without a free boundary flip, although that symmetry is useful elsewhere.

For the archived 11-face 30-link disk with g2_squared=1, lambda_max(M)=1.1046593441618966, and nine OTHER retained plaquette couplings each 3/32000, B0=0.00084375, gamma=0.3394711699872615, error sqrt(B0/gamma)=0.04985462390154264. The cap lower bound at delta=.1 is ZERO (Haar=.037386073468498655); at delta=.2 it is 0.0542334147602852 (Haar=.10408803866182784). Numerical constants are floating-point demonstrations, not certified interval results.

This is NOT a refinement-uniform result: B0 grows with volume and, in spatial dimension 2 under conventional fixed-g² scaling, each b_j typically grows as h^-2. As soon as B0/gamma ceases to be small, the bound becomes vacuous. It also does not give a zero-coupling law suitable for exponential trials uniformly in volume; it only supplies a finite-volume weak-magnetic distributional comparison. Uniform near-center estimates and the 3+1D continuum Yang-Mills mass gap remain OPEN.
