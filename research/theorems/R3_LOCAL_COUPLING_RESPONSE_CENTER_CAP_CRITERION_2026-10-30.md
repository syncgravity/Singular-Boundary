# R3-IR-506: local magnetic-coupling energy response controls center-cap moments (2026-10-30)

Let H(b)=A-b p_f with A self-adjoint semibounded, independent of b, and bounded self-adjoint plaquette multiplication p_f in [-1,1]. Define E(b)=inf spec H(b), F(b)=E(b)+b=inf spec (A+b(1-p_f)). F is concave, nondecreasing, and 2-Lipschitz in b (in fact 0<=1-p_f<=2). For a normalized ground state Omega_b, variational comparison at b-s yields F(b-s)<=F(b)-s<1-p_f>_Omega_b, hence

<1-p_f>_Omega_b <= [F(b)-F(b-s)]/s

for all s>0 within the parameter domain, WITHOUT requiring ground-state uniqueness or differentiability. At differentiability F'(b)=<1-p_f>_Omega_b (Hellmann-Feynman), and the backward secant is an upper bound by concavity. In case of degeneracy, the inequality applies to EVERY normalized ground state.

Pointwise 1-p_f²=(1-p_f)(1+p_f)<=2(1-p_f). For C_delta={|p_f|>=1-delta} and 0<delta<1, the cap Markov bound gives

Prob_Omega_b(C_delta)>=max(0,1-2[F(b)-F(b-s)]/[s(2delta-delta²)]).

The formula is a LOCAL COUPLING finite-difference criterion holding for the full inverse-Whitney gauge-covariant Hamiltonian, provided all kinetic geometry and the remaining magnetic couplings are held fixed while b varies. Note the response F(b)-F(b-s) still encodes the ENTIRE environment; a refinement-uniform bound for this finite difference is NOT proved. For delta->0 the criterion is usually vacuous unless the secant vanishes with delta; it is not a uniform delta^(3/2) cap theorem.

For an elementary boundary face with a unique free boundary link e, if the electric kinetic operator is built from adjoint parallel transports, the link-center flip U_e -> -U_e leaves its electric quadratic form invariant: Haar measure and left/right invariant electric derivatives commute with center flips, and adjoint parallel transports are center-blind. The flip changes the sign of p_f and no other plaquette trace. Hence H(-b)=Z_e H(b) Z_e^-1, so E(-b)=E(b). This symmetry requires the specific free boundary link and center-blind electric construction, and does not imply the local response bound is uniform in b or volume.

A counterexample to a stronger inference from concavity alone: the two-level H(b)=a(I-sigma_x)+b(I-sigma_z) has E(b)=a+b-sqrt(a²+b²), F(b)=E(b) when writing the potential as b(1-sigma_z); its response 1-b/sqrt(a²+b²) can range from near one to near zero as a/b varies. Concavity and electric positivity alone do not control the response across physical scaling.

Crucial remaining work: derive an absolute, volume/refinement-uniform upper bound on the local energy increment [F(b)-F(b-s)]/s in the relevant delta regime, or use a complementary mechanism not demanding this moment criterion. Neither a center-cap theorem nor a 3+1D continuum Yang-Mills mass gap is proved.
