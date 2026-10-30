# Quantitative cavity compatibility: exact counterexample and corrected sufficient criterion

Date: 2026-10-26. Scope: finite SU(2) Wilson plaquette complexes, normalized Haar measure, and the cavity exterior distribution. No Yang–Mills mass gap is asserted.

## 1. Definitions
For an internal link set I, size m, delete incident plaquette interactions to form S_out(v), Z_cav, and cavity exterior probability rho_I(dv)=exp[-S_out(v)]dv/Z_cav. Define S_I(u;v), E_I(v)=min_u S_I(u;v), Z_I(v)=∫exp[-S_I(u;v)]du, and a_I=E_rho Z_I=Z_full/Z_cav. Insertion free energy is F_I=-log a_I.

## 2. Exact counterexample to an exp(-O(m)) low-frustration event
Take two oriented plaquettes p1,p2 that share exactly one link e; all their other links are private (this is a finite bounded-incidence SU(2) gauge complex). Set I={e}, m=1, beta_{p1}=beta_{p2}=lambda, and no additional interactions. Deleting both incident plaquette interactions makes the cavity measure product Haar on every exterior link. Each plaquette staple q_i(v) is independently Haar distributed in SU(2)~S^3. The incident action of the core link u is S_I(u;v)=2lambda-lambda u·(q_1+q_2), where the sign convention can be chosen by orientation and quaternion identification. Therefore E_I=F_e=2lambda-lambda|q_1+q_2|.

Write q_1^{-1}q_2 as an SU(2) element of geodesic angle theta∈[0,pi]. Then |q_1+q_2|=2cos(theta/2), so E_I=2lambda[1-cos(theta/2)]. Under independent Haar staples theta has density (2/pi)sin^2 theta dtheta. For fixed A>0, L=A(1+log lambda), and 0<L<2lambda, set theta_max=2 arccos(1-L/(2lambda)). Then

rho_I(E_I≤L)=(2/pi)∫_0^{theta_max}sin²theta dtheta = (theta_max - sin(theta_max)cos(theta_max))/pi.

As lambda→∞, theta_max~2 sqrt(L/lambda) and
rho_I(E_I≤L)~(16/(3pi))(L/lambda)^(3/2)→0.

Hence no positive, lambda-independent lower bound exp(-C m)=exp(-C) exists on this compatible-extension event, for any fixed constants A,C, even though the geometry has bounded incidence. This example does not by itself disprove the property on the specially constrained interior supports of a particular Penrose spacetime complex; it refutes any inference from bounded incidence and gauge covariance alone.

The full partition function has exact factorization by integrating one private link per plaquette: Z_full=q(lambda)^2 where q(lambda)=exp(-lambda)z(lambda), z(lambda)=2 I_1(lambda)/lambda. The cavity partition is 1. Since q(lambda)~sqrt(2/pi)lambda^(-3/2),
F_I=-log Z_full=3 log lambda-log(2/pi)+o(1).
Thus logarithmic insertion free energy holds exactly even though rho_I(E_I≤A log lambda) vanishes polynomially. The previously proposed exp(-O(m)) event is sufficient but unnecessarily strong, and is not valid in general.

## 3. Corrected polynomial compatible-extension criterion
A local-minimizer Haar-ball argument yields constants c_0,C_0 (depending on bounded incidence, coupling ratios) for lambda≥1:
Z_I(v)≥c_0^m lambda^(-3m/2)exp[-E_I(v)-C_0 m].
If a cavity event B_I satisfies
rho_I(B_I)≥exp[-a m(1+log lambda)]
and sup_{v∈B_I}E_I(v)≤b m(1+log lambda),
then
F_I≤(a+b+3/2)m log lambda+(a+b+C_0-log c_0)m
(up to choices of constants). This suffices for the previously derived full-Wilson contour estimate, provided m≤K|X| and all incident beta≥c_-lambda:
mu_full(d_p>lambda^-1/2 for all p∈X) ≤ exp[-c_-sqrt(lambda)|X|+F_I], hence ≤exp[-c sqrt(lambda)|X|] at large lambda.
The polynomial-probability criterion is compatible with the two-plaquette exact example, whereas the exp[-O(m)] condition is not.

## 4. Independence from desired free-energy bound
The criterion is noncircular *if* B_I is constructed and its cavity probability is independently bounded by direct integration of S_out. Simply defining B_I={E_I≤...} and citing F_I to show its probability would be circular. For arbitrary interior thin Penrose supports, constructing such a B_I with only O(m) controllable exterior degrees of freedom and O(m log lambda) exterior action surcharge has not been proved. A local gauge collar can have external plaquettes costing O(lambda m) when repaired. Consequently neither the polynomial compatibility-event estimate nor the arbitrary-thin-support logarithmic insertion bound is currently established for Penrose spacetime.

## 5. Research conclusion
The exact two-plaquette calculation falsifies the *specific* exp(-O(m)) compatibility-event conjecture in the general bounded-incidence class. It simultaneously proves that small insertion free energy can be dominated by polynomially rare compatible exterior configurations. A sound Penrose proof should aim at exp[-O(m log lambda)] probability for a compatible, low-action exterior event (or a direct relative partition-function comparison), not exp[-O(m)] probability. R3 and continuum R2 mass gap remain open.
