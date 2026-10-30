# The Singular Boundary: Independent local response audit
26 October 2026

## Scope
A local finite-time dynamical bound can be proved from the on-site electric Hamiltonian and bounded finite-support magnetic Wilson terms at fixed lattice cutoff. A uniform boundary-response estimate for the interacting ground state, at arbitrary couplings or along the continuum scaling trajectory, does not follow from these premises and is not proved here.

## Hamiltonian
On finite Penrose rhombus patches, use H = sum_e a_e(-Delta_e) + sum_f b_f(1 - (1/2)ReTr U_f) acting on tensor-product link L2(SU(2)) and its Gauss-invariant subspace. Assume b_f bounded at the fixed cutoff, each rhombus has four edges, and each edge borders at most two rhombi.

## Proposition (finite-time locality)
For bounded local observables A_X and B_Y with disjoint support, the Heisenberg commutator has a Lieb-Robinson-type bound
||[tau_t(A_X),B_Y]|| <= C |X| ||A_X|| ||B_Y|| exp(-mu (d(X,Y) - v|t|)).
Constants may depend on the fixed-cutoff bound sup_f ||V_f||, local incidence and the chosen interaction-graph metric, but do not depend on the total number of vertices.

### Proof mechanism
Factor out the tensor-product on-link electric dynamics. Though its generators are unbounded, it preserves individual link supports and norms. In the interaction picture, the magnetic terms remain norm-bounded and supported on four edges. Iterated Duhamel expansion shows only chains of overlapping face supports connecting X to Y contribute. Their number grows at most exponentially in chain length because the interaction graph has bounded degree, while time integrals supply n! in the denominator. Sum over paths to obtain the stated finite-speed bound.

### Limitations
This bound holds for real-time observable commutators. It does not imply spatial mixing of the interacting ground-state probability density. Finite propagation speed is compatible with critical or degenerate systems. On the conventional 2+1D continuum trajectory, magnetic couplings scale like 1/(g_3^2 a^2); this crude microscopic locality estimate has no controlled cutoff-uniform physical propagation velocity, and its decay constants do not certify continuum equilibrium clustering.

## Exact local response identity and missing step
For a differentiable, nondegenerate gapped finite-volume ground state of H(s)=H+sV_Y, the ground-state derivative for local A_X can be written using reduced resolvent R_s=Q_s(H(s)-E_0(s))^{-1}Q_s:
d/ds <A_X>_s = -2 Re <Omega_s, A_X R_s (V_Y-<V_Y>_s) Omega_s>.
This is an identity, not a bound uniform in volume or cutoff: bounding the reduced resolvent or its localized matrix elements is the missing input. The same caveat applies to imaginary-time integrated connected correlations.

## Counterexample to inferring ground-state mixing from locality
Local finite-range Hamiltonians can exhibit finite-speed propagation while being gapless or having long-range-ordered ground states. Thus finite-time commutator locality alone cannot establish a ground-state Poincare constant or boundary-response decay.

## Research tests, no new Monte Carlo required
1. Derive a rigorously controlled, renormalized block estimate for local ground-state response that does not assume the spectral gap.
2. Specify boundary perturbations, gauge constraints, physical block scale ell, and energy normalization.
3. Prove constants uniform over Penrose exhaustions at fixed cutoff before attempting a->0.
4. Distinguish the local-gap response theory from a lower bound for the entire vacuum-orthogonal spectrum.

## Relevant literature
- Henheik, Teufel, Wessel (2022), Local stability of ground states in locally gapped and weakly interacting quantum spin systems, Letters in Mathematical Physics 112:9. https://doi.org/10.1007/s11005-021-01494-y
- Henheik and Wessel (2026), Response Theory for Locally Gapped Systems, Journal of Statistical Physics 193:151. https://link.springer.com/article/10.1007/s10955-026-03703-1
