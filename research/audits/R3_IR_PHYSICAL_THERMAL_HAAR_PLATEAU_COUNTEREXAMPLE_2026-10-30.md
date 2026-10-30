# Physical SU(2) electric plaquette: exact finite-temperature failure of the Haar plateau

**2026-10-30. Audit / explicit counterexample, not an interacting Wilson mass-gap result.**

Consider a single oriented square plaquette with four original SU(2) links, impose Gauss invariance at every vertex, and omit its magnetic Wilson term. Let each electric link have coefficient a_e>0 and A=sum_boundary a_e. Gauge-invariant wavefunctions depend only on the conjugacy class of the holonomy W. The physical Hilbert space is L²(SU(2))^Ad, with normalized SU(2) Haar measure, and the induced electric Hamiltonian is H_phys=A(-Delta_W). Irreducible SU(2) characters chi_j(W), j=0,1/2,1,..., form an orthonormal physical eigenbasis with energies E_j=A j(j+1), since E_1/2=3A/4.

For any bounded central O(W), its **physical** heat-trace expectation is exactly

F_beta^phys(O) =
 [sum_{j=0,1/2,...} exp(-beta A j(j+1)) integral O(W) chi_j(W)^2 dW]
 /[sum_{j=0,1/2,...} exp(-beta A j(j+1))]. (PT-1)

This is a full Gauss-projected trace, not an unrestricted link heat trace. Ground state chi_0=1 gives Haar expectation in the beta-infinity limit.

**Explicit non-Haar observable.** Take O(W)=p(W)^2 with p=Tr W/2. Haar class orthogonality and Clebsch-Gordan fusion give
integral p² dW=1/4;
integral p² chi_1/2² dW=1/2.
Proof: chi_1/2=2p and chi_1/2²=chi_0+chi_1. Thus p²=chi_1/2²/4=(chi_0+chi_1)/4. The Haar integral of p² chi_1/2² is (1/4) integral (chi_0+chi_1)^2=(1/4)(1+1)=1/2.

Consequently
F_beta^phys(p²)
=1/4 +(1/4) exp(-3beta A/4)+O(exp(-2 beta A)),
as beta tends to infinity. (PT-2)
The next energy is j=1 with E_1=2A, so the remainder O(exp(-2beta A)) includes the denominator correction and j=1 contributions. In fact the j=1/2 contribution is strictly positive at every finite beta; a direct identity strengthens the conclusion:
For j=0, integral p² chi_j²=1/4, while for every j>=1/2,
integral p² chi_j²=1/2,
because chi_1/2 chi_j=chi_(j+1/2)+chi_(j-1/2), whose two character terms are orthogonal. Therefore
F_beta^phys(p²)= 1/2 - 1/[4 Z_beta],
Z_beta=sum_j exp(-beta A j(j+1)) >1. (PT-3)
In particular F_beta^phys(p²)>1/4 for every finite beta>0 and tends to 1/4 as beta tends to infinity.

**Consequence.** The statement 'a magnetically private plaquette holonomy is Haar under the physical finite-temperature trace' is false even for a single pure-electric plaquette; the unique ground-state Haar property remains correct. Gauss projection correlates link degrees of freedom at the thermal seam, and cannot be omitted from Euclidean loop calculations. This is a concrete counterexample supporting the caution in R3_IR_LAST_NEIGHBOR_HAAR_PLATEAU_AUDIT_2026-10-30.md.

For the last-neighbor cosh reference formula, always retain the actual finite-beta baseline F_beta(0), and only replace it by alpha_a² **after** taking the physical vacuum limit. This explicit example does not disprove the cap-biased cosh identity, nor imply an adverse full-coupling response; it prevents an invalid shortcut.

**Status:** exact counterexample to thermal-Haar extrapolation, not to the interacting Wilson cap-survival conjecture. The signed comparison, regulator-uniform gap and continuum Yang-Mills construction remain open.
