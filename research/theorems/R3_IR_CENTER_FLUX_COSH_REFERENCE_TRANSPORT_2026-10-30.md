# Exact center-flux cosh transport from a single decoupled Wilson reference ensemble

Date: 2026-10-30. Claim R3-IR-399. Exact finite-volume positive Euclidean identities; no regulator-uniform cap survival proved.

Let H(t)=H0+t b(1-p_g) be the original-link SU(2) Wilson Hamiltonian with the target face f deleted, and its neighboring face g absent from H0. All other Wilson terms may remain. Let O=k_a(W_f) be a nonnegative, nonzero target-cap observable. Assume the independent center-flux involution S_g (archived FN-2) preserves H0 and O but flips p_g. This symmetry must be checked for each graph and source; O need not be invariant under a naive single-link sign flip.

At finite beta, write E0 for expectation under the positive Gauss-projected Feynman-Kac loop measure of H0, and E0^O[Y]=E0[OY]/E0[O] for its cap-biased version. Let X=b integral_0^beta p_g(U(s)) ds. Then E0[O]=alpha_a^2 by the private-link Haar property, and the path involution reverses X while keeping O fixed.

**Theorem CS-1 (exact cosh ratio).** For any real t,

F_beta(t)/F_beta(0)
= E0^O[exp(tX)]/E0[exp(tX)]
= E0^O[cosh(tX)]/E0[cosh(tX)].  (CS-1)

Proof. The scalar tb in the Wilson magnetic interaction contributes exp(-beta tb) to both numerator and denominator and cancels. The remaining perturbation weights trajectories by exp(tX). The involution S_g makes the odd sinh part vanish separately in ordinary and O-biased measures. Both cosh expectations are finite and strictly positive, since |X|<=beta b.

This equality requires no spectral gap and is nonperturbative in tb. It refers to ONE decoupled reference path ensemble rather than the series of interacting measures along 0<=t<=1.

**Corollary CS-2 (conditional comparison).** Define the ordinary and cap-biased laws of |X| at the zero-neighbor reference. If the cap-biased |X| stochastically dominates the ordinary |X| (a new independent hypothesis), then F_beta(t)>=F_beta(0) for all t>=0, since cosh(tx) is increasing for x>=0. A weaker sufficient condition for a half-Haar cap expectation is
E0^O[cosh(X)] >= (1/2) E0[cosh(X)].
This is exactly the finite-beta half-Haar condition, not an independently established estimate.

**Corollary CS-3 (curvature at zero).**
(d²/dt²) log F_beta(t) at t=0
= E0^O[X²]-E0[X²],
since the source is odd and both means vanish. This agrees with the previously proved signed variance transport.

**Vacuum limit.** At each fixed finite lattice the original positive physical ground state is simple and the finite-volume gap positive. Thus
F(1)/F(0) = lim_(beta to infinity) E0^O[cosh X]/E0[cosh X],  (CS-4)
where the ratio is taken BEFORE the limit. The two expectations generally diverge exponentially with beta; neither is separately a finite ground-state correlation. No exchange of a ratio and two individual limits is claimed.

**Important obstruction.** At physical magnetic strength b~h^-2, |X|<=beta b grows without bound as beta increases, so the cosh tilt is exponentially sensitive to rare reference paths. Positivity, center-flux parity and the private-link Haar baseline do NOT order the two |X| laws or make the numerator comparable with the denominator. The exact formula therefore does not prove Haar-order cap survival, signed current, infrared response, or a continuum mass gap. It isolates an explicit probabilistic Wilson-specific comparison at the decoupled original-link ensemble.

Dependency: archived FN-1/FN-2 and R3_IR_EVEN_COUPLING_CAP_VARIANCE_TRANSPORT_2026-10-30.md. Status: identity PROVED; nonperturbative comparison OPEN.
