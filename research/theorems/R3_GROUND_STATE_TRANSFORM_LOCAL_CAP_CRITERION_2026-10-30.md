# Ground-state transform and conditional center-cap criterion (2026-10-30)

Scope: finite connected open SU(2) lattice, a specified positive gauge-covariant divergence-form inverse-Whitney electric quadratic form, bounded real Wilson magnetic potential, and its strictly positive normalized ground state Omega. This is a CONDITIONAL local probability theorem, not a uniform Harnack estimate or continuum mass-gap proof.

Write H=D^* K D + V, absorbing the positive overall electric coefficient into K; D_e is an adjoint-transported invariant link derivative. It obeys the scalar Leibniz rule D_e(Omega f)=Omega D_e f+f D_e Omega. Assume the smooth positive ground state satisfies H Omega=E0 Omega. Integration by parts yields the ground-state representation, for smooth gauge-invariant f:

 <Omega f,(H-E0)Omega f> = integral Omega(U)^2 [D f(U)]^* K [D f(U)] dHaar(U).

This identity is exact, nonperturbative and works with off-diagonal electric link couplings and configuration-dependent adjoint transports when the operator is the Friedrichs realization D^* K D. Its proof uses the actual divergence-form adjoints; an unordered D D expression need not obey it. The transform shows that a spectral-gap question becomes a weighted Poincare inequality with equilibrium measure Omega^2 dHaar; SPD bounds on K alone do NOT supply a uniform weighted Poincare constant.

On the open disk choose independent deleted-face holonomy u and remaining based-face coordinates Y. Write rho_Y(u)=|Omega(u,Y)|^2 / integral_SU2 |Omega(v,Y)|^2 dv. Suppose that for almost every Y,

 osc_u log |Omega(u,Y)|^2 := sup_u log|Omega(u,Y)|^2 - inf_u log|Omega(u,Y)|^2 <= A.

Then for every Haar-measurable event C subset SU2 the exact conditional comparison is e^-A Haar(C) <= integral_C rho_Y(u)du <=e^A Haar(C). Integrating over Y yields m_f(C)>=e^-A Haar(C). In particular for the SU2 double-center cap C_delta={|Tr u/2|>=1-delta},

 m_f(delta) >= e^-A c_delta >= e^-A (8/(3pi)) delta^(3/2), 0<delta<=1.

The oscillation hypothesis can be replaced by a conditional gradient hypothesis: if the left-invariant Riemannian metric on SU2 is normalized so the geodesic diameter is D_G and sup_(u,Y)|grad_u log|Omega(u,Y)|^2|<=L, then A<=D_G L. These are SU2 conditional *density* hypotheses, not consequences established by the Whitney form. The right target for refinement is a uniform bound on the conditional log-density oscillation (or a suitable local conditional Harnack inequality), rather than a global magnetic perturbation norm.

A limiting obstruction is explicit: uniform ellipticity of K and its finite-dimensional geometric condition-number bounds do not imply A uniform when V grows. For a single SU2 rotor with positive kinetic Laplacian and potential V_tau(u)=tau(1-p(u)), the ground-state density can localize as tau increases, and the log-density oscillation need not remain bounded. This is an illustrative mechanism, not a quantified claim about Penrose physical refinement.

IMPORTANT: the Whitney inverse matrix assembled on the Penrose disk and its finite coercivity are verified; a refinement-uniform conditional oscillation bound, local Harnack constant, shrinking-center cap estimate, and continuum Yang-Mills mass gap all remain OPEN.
