# R3-IR-434 — Exact conditional-density correction for environmental Wilson flux

2026-10-30. Finite-volume exact weighted-divergence construction. All statements refer to the genuine positive original-link Wilson ground-state measure, and are conditional on an explicitly supplied marginal flux. No regulator-uniform energy estimate is asserted.

Write the physical measure as dmu(x,y)=rho_y(x) dx dnu(y), with rho_y(x)>0, int rho_y dx=1. Let O(x,y) be the smooth cap observable, m(y)=int O rho_y dx, F=int m dnu, f_loc=O-m and f_env=m-F.

Suppose a smooth environmental tangent-vector flux v(y) solves the marginal divergence equation -nu^(-1)div_y(nu v)=f_env. (The divergence includes all environmental link coordinates, with their product metric.)

Naively lifting v without an x-component fails because
-mu^(-1) div_y(mu v)
=f_env - v dot grad_y log rho_y.

Set h(x,y)=v(y) dot grad_y log rho_y(x). Its conditional mean is zero:
int h rho_y dx=v dot grad_y int rho_y dx=0.

For each y solve the compact SU(2) weighted Poisson equation
-rho_y^(-1)div_x(rho_y w_y)=h(x,y).
Then the full flux K=(w_y,v) satisfies exactly
-mu^(-1)[div_x(mu w_y)+div_y(mu v)]
=h + f_env-h=f_env. (CL-1)

Independently solve -rho_y^(-1)div_x(rho_y u_y)=f_loc for the local source. The combined flux J=(u_y+w_y,v) solves -div_mu J=O-F and hence, by R3-IR-433,

A <= int [a_x^(-1)|u_y+w_y|² + sum_environment_edges a_e^(-1)|v_e|²] dmu. (CL-2)

The pointwise cancellation in CL-1 is the essential correction omitted by a naive marginal lift. All fields can be chosen suitably regular in finite volume because rho_y is smooth and strictly positive on the compact configuration manifold. Gauge-invariant averaging of an admissible flux preserves the divergence equation for gauge-invariant sources and does not increase its convex quadratic energy; thus the certificate is compatible with the physical Gauss-invariant sector.

Let lambda_x(y)>0 be the Poincare constant for conditional rho_y and let E_x(h;y)=int h² rho_y dx. By the weighted Poisson variational principle, int |w_y|² rho_y dx <= lambda_x(y)^(-1) E_x(h;y), and similarly int |u_y|² rho_y dx <= lambda_x(y)^(-1) Var_rho_y(O). Consequently

A <= 2/a_x int lambda_x(y)^(-1) [Var_rho_y(O)+Var_rho_y(v dot grad_y log rho_y)] dnu
 + sum_e(in environment) a_e^(-1)int |v_e(y)|²dnu. (CL-3)

Here the conditional score variance is a quantitative cost of lifting the environmental flux. No bound on this score, the marginal transport energy, or lambda_x(y) uniform under physical Penrose refinement is proved.

In particular the exact correction does not imply the required cap transport inequality or the continuum Yang-Mills mass gap.
