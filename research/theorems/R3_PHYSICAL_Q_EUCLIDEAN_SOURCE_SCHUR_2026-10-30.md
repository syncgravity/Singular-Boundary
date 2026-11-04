# Physical Q-sector Euclidean response and exact Schur complement
Date: 2026-10-30
Status: exact finite-volume identities; NO Penrose uniform response estimate established.

Let H_f^-=T+V_- on finite physical gauge-invariant SU(2) Hilbert space, ground state Omega>0 normalized, K=H_f^--E0>=0. P is the physical conditional Haar projection on the deleted based-face holonomy, Q=I-P, and [P,V_-]=0. Write p=P Omega, q=Q Omega. Denote the Q-compressed positive self-adjoint Friedrichs operator by A=QKQ on Ran Q (do NOT confuse with the face electric coefficient A_f=sum_{e in boundary f}a_e). Assume p is in the relevant operator domain and s=-QKPp=-QTPp belongs to L². Finite-volume uniqueness and compact resolvent imply A>=lambda_Q>0 at each fixed lattice, but no uniform lower bound.

THEOREM 1: Define C(t)=<s,exp(-tA)s> for t>=0. Then C(t)>=0 and
||q||²=<s,A^-2 s>=int_0^infinity t C(t)dt.
Proof by spectral theorem and int_0^infinity t exp(-t lambda)dt=lambda^-2. Compressed semigroup exp(-t QKQ) is not generally Q exp(-tK) Q.

THEOREM 2 (exact block Schur identity): On the P block set B=PKP and C=QKP. Projected equation gives A q=-C p and Bp+C* q=0. Hence
q=-A^-1 C p
and (B-C* A^-1 C)p=0.
All statements are operator identities under domain assumptions and form identities otherwise. The negative Schur term is nonnegative as a quadratic form C* A^-1 C, but positivity alone does not imply that the Q-amplitude q is small. Since C=QTP, all P-Q coupling is electric, although B and A contain the retained magnetic potential.

THEOREM 3 (short/long-time split): for any tau>0,
||q||² = int_0^tau t C(t)dt + int_tau^infinity t C(t)dt,
0<=int_0^tau t C(t)dt <= (tau²/2)||s||²
by positivity and contraction of exp(-tA). The long-time integral is the difficult low-energy contribution. A bound on it independent of an assumed uniform physical gap is needed. The unweighted resolvent source bound ||s|| small is insufficient if A has small eigenvalues.

CAP CONSEQUENCE (conditional only): if uniformly for f in D_R at refinement h, int_0^infinity t C_{f,h}(t)dt=o(h^(3/2)), then eta=||QOmega||=o(h^(3/4)) and OT-4 yields Haar-order identity-center cap probability at radius delta~h. Combined with the separately proved exponential-tilt bound, this condition would give the logarithmic magnetic deletion comparison. This source-correlation condition is exactly equivalent to the previously open inverse-square spectral source criterion and is NOT an improvement in its quantitative strength. No continuum mass gap is claimed.

VERIFICATION NOTES: equations follow from finite-dimensional block algebra and positive self-adjoint spectral functional calculus; no Monte Carlo Stage 26 data used or modified. For strong operator claims need p in domain(K), s in L²; otherwise work in appropriate form duality and avoid unsupported semigroup formulae.
