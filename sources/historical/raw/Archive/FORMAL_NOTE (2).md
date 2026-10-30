# Localized gauge-fixed propagator on Penrose spacetime blocks

## Scope
Finite bounded-incidence cell complexes, including finite Penrose-rhombus spatial patches extruded in Euclidean time, with arbitrary positive spatial/temporal plaquette weights. This is a **conditional resolvent localization theorem**, not a proof of uniform coercivity, interacting polymer convergence, or the Yang–Mills mass gap.

## Discrete linearized gauge theory
Take real Lie algebra cochains `C^k(B;su(2))` with Euclidean product and cellular coboundaries `d_0`, `d_1`, so `d_1 d_0=0`. At the flat identity background, the quadratic Wilson curvature energy is `(1/2) <d_1 A, B_2 d_1 A>` (normalization of Lie algebra generators absorbed in `B_2`). With gauge-fixing parameter `xi>0` the quadratic Hessian is

`H = d_1^* B_2 d_1 + xi d_0 d_0^*`, acting on the allowed 1-cochain domain, provided the boundary conditions define compatible adjoints. A residual harmonic one-cochain lies in `ker d_1 ∩ ker d_0^*`, hence is a zero mode: simply connected topology alone does not certify the chosen boundary problem. Specify relative/Dirichlet boundary conditions or project all harmonic modes out, and certify `mu = inf spec(H)>0`.

For a small-field background `Ubar`, the actual Wilson Hessian may contain background-curvature terms and is not automatically nonnegative. Require an independent comparison `||H(Ubar)-H|| <= delta < mu` if claiming its covariance is controlled by the flat quadratic Hessian.

## Theorem: finite-range Combes–Thomas resolvent localization
Let `H` be self-adjoint on the finite one-link fluctuation space, finite-range in the link adjacency graph. Suppose `H >= mu I`, `mu>0`, and the off-diagonal row sum is bounded by

`J = sup_e sum_{g neq e} ||H_{eg}|| < infinity`, symmetric block matrices, and nonzero off-diagonal blocks occur only between adjacent sites (for radius R replace d by ceil(d/R)).

Let `G=H^{-1}` and graph distance `d(e,g)`. For any `theta>0` with `J (exp(theta)-1) <= mu/2`,

`||G_{eg}|| <= (2/mu) exp(-theta d(e,g))`.

Proof: For a fixed target g, conjugate by a diagonal exponential weight `W_e=exp(theta min(d(e,g),N))`. Schur bounds give `||WHW^{-1}-H|| <= J (exp(theta)-1)`. Neumann inversion yields `||(WHW^{-1})^{-1}|| <= 2/mu`. The weighted (e,g) block equals exp(theta d(e,g)) times G_eg. Take N>=d(e,g). This proves the bound, independently of the total number of sites.

Choose `theta = log(1+mu/(2J))`, for J>0. If J=0, all off-diagonal resolvent blocks vanish. More generally for `H+m^2 I`, replace `mu` by a lower bound of `H+m^2 I`, showing regularized localization even when massless H is singular.

## Uniformity distinction
The theorem is volume uniform *if* mu and J have uniform bounds in the selected normalization; it is not automatically cutoff uniform. In a canonical discretization of a continuum second-order elliptic operator, `J_h = O(h^-2)` while Dirichlet `mu_h ~ O(L^-2)` on a block of physical diameter L. This elementary CT bound gives lattice rate `theta_h = O(h^2/L^2)`, which does not yield useful fixed-physical-distance decay as `h->0`. More refined heat-kernel/elliptic/Davies estimates and geometrical Poincare/Sobolev controls are required for scale-sharp estimates. In the massless Gaussian reference, uniform exponential clustering as L->infinity is not expected; RG needs scale-dependent localization or boundary/block constraints, not an asserted physical mass.

## A computable Penrose-specific admission test
1. Use actual Penrose stage geometry and temporal extrusion to enumerate oriented incidence matrices `d_0,d_1`, verify `d_1 d_0=0` exactly.
2. Choose and document boundary conditions, weights and gauge fix.
3. Compute or rigorously certify the smallest singular value of `D = [sqrt(B_2) d_1; sqrt(xi) d_0^*]` on the restricted link domain: `mu=sigma_min(D)^2`.
4. Determine the maximum off-diagonal block row sum J and incidence degree; apply CT bound directly.
5. For small nonflat backgrounds, independently bound actual Hessian perturbation below mu and account for the Faddeev–Popov/gauge-fixing Jacobian. Flat cochain H is not the full non-Abelian block integration.
6. To prove a continuum-stable polymer norm, establish multi-scale covariance bounds, connected large-field region bounds, and source/reconstruction estimates. None follow from the CT inequality alone.

## Bibliography
T. Balaban, *Propagators for lattice gauge theories in a background field*, Communications in Mathematical Physics 99 (1985), 389–434, doi:10.1007/BF01240355. This work establishes background-field propagator regularity and decay in its stated setting. Its results are not here claimed to cover Penrose complexes automatically.

T. Balaban, *Spaces of regular Gauge field configurations on a lattice and gauge fixing conditions*, Communications in Mathematical Physics 99 (1985), 75–102, doi:10.1007/BF01466594.

## Proof status
Proved: exact linearized quadratic operator formulation, conditional finite-volume Combes–Thomas off-diagonal bound, computable coercivity gate. Not proved: uniform Penrose block cochain spectral inequality, uniformly coercive nonflat Wilson Hessians, scale-sharp cutoff covariance localization, residual spacetime polymer norm, R3 or R2 mass gap.
