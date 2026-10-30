# The Singular Boundary — Poincaré constants and the continuum gate

**26 October 2026. Status: unconditional finite-volume inequality, conditional uniform criterion, no nonperturbative continuum mass-gap proof.**

## Scope
A finite connected spatial graph G with E edges and pure SU(2) gauge fields, compact configuration space X=SU(2)^E with normalized product Haar measure h. Work on the gauge-invariant subspace. Electric coefficients a_e>0 and bounded real gauge-invariant potential B. The quadratic-form Hamiltonian is H=sum_e a_e(-Delta_e)+B. The Laplace-Beltrami convention has first nonzero SU(2) eigenvalue 3/4.

## Proposition 1 (finite-volume ground state)
For the full configuration space, H has compact resolvent and a unique strictly positive ground state Psi (regularity and positivity follow from ellipticity and positivity improving of the heat semigroup). Gauge covariance makes Psi gauge invariant. Set rho=Psi^2 (Psi normalized in L2(h)), dnu=rho dh. There are finite positive m=min_X rho and M=max_X rho.

## Proposition 2 (unconditional explicit-in-density Poincaré comparison)
For all gauge-invariant H1 functions f,

 Var_nu(f) <= (4/3)(M/m) sum_e int |grad_e f|^2 dnu.

Consequently

 gap(H|physical) >= (3/4) min_e(a_e) (m/M).

Proof. Var_nu(f)=inf_c int(f-c)^2 rho dh <= M inf_c int(f-c)^2 dh = M Var_h(f). Product Haar tensorization and the SU(2) Laplacian gap give Var_h(f)<= (4/3)sum_e int |grad_e f|^2 dh <=(4/3m)sum_e int |grad_e f|^2 dnu. Combine with the exact ground-state transform (integration by parts). This applies at arbitrary couplings, but m/M generally depends on volume and cutoff.

## Proposition 3 (what would establish uniform gap)
Any volume- and cutoff-independent K such that Var_nu(f)<= K sum_e a_e int |grad_e f|^2 dnu for all gauge-invariant f centered in nu yields gap >=1/K. Conversely the optimal K equals the inverse gap. Thus the statement itself is equivalent to the target and must not be assumed as proof.

A sufficient but generally unrealistically strong condition is sup_{G,a}(M_{G,a}/m_{G,a})/a_*(a) < infinity, where a_*=min_e a_e in common physical units. This is a sufficient uniform bound, not a demonstrated property of Wilson ground states. More refined block/conditional criteria can improve on global density comparison but also require independent proofs of their hypotheses.

## Boundaries
The propositions hold for any finite graph (open, periodic, etc.) with connected compact configuration space and strictly positive electric coefficients, provided the gauge projection and action are defined consistently. They do not yield constants uniform over those choices. A change of topology can change vacuum-orthogonal sectors and near-low-energy states; the boundary-uniform problem is separate.

## Continuum scaling
For conventional 2+1D Hamiltonian conventions, electric coefficients scale approximately as g3^2 while magnetic coefficients scale as 1/(g3^2 a^2), up to geometric factors and time normalization. Their ratio grows as a^{-2}, so a fixed weak-magnetic threshold cannot be continued to a->0 by that theorem. In a continuum theorem, transfer times and energy units must be matched, and one needs a uniform lower bound in physical units *and* convergence/reconstruction of the limiting quantum theory. The density ratio bound does not establish either.

## Literature and applicability
- D. A. Yarotsky, J. Math. Phys. 45 (2004) 2134–2152, DOI 10.1063/1.1705718: perturbative stability of gapped product reference systems under weak bounded finite-range perturbations.
- J. Henheik, S. Teufel, T. Wessel, Lett. Math. Phys. 112, 9 (2022), DOI 10.1007/s11005-021-01494-y: locally gapped/weakly interacting systems; permits inhomogeneous local terms; local stability result should not be conflated with an unconditional gap for arbitrary perturbations.

## Consequences for the program
1. The SU(2) product Haar spectral gap and exact ground-state transform give an unconditional finite-volume lower bound, with an uncontrolled density ratio.
2. Fixed-scale Penrose finite local complexity is helpful for applying sufficiently-weak-interaction stability results, but does not force a uniform Poincaré constant at the continuum coupling.
3. The C5 family covariance transports existing spectral estimates between equivalent weighted complexes; it cannot create a missing scale-independent lower bound.
4. Paper 3's J structure or helical sampling cannot replace a dynamical inequality. No further gauge simulations are required for these mathematical statements.
5. **Unresolved theorem:** establish volume-uniform ground-state mixing (or another physical Hamiltonian spectral inequality) over the nonperturbative scaling trajectory, with stated boundary sectors and physical normalization. No existing argument in this memorandum proves it.