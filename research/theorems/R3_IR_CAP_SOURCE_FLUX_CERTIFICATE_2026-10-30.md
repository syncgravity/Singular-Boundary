# R3-IR-433 — Source-specific flux certificate and conditional-environment decomposition

2026-10-30. Exact finite-volume physical SU(2) Wilson upper-certificate, without assuming an interacting spectral gap. No regulator-uniform cap bound is asserted.

Let mu=Omega² dHaar be the true positive full-coupling ground-state probability of R3-IR-432 and L the ground-state transformed nonnegative generator with Dirichlet form D(phi)=sum_e a_e int |grad_e phi|²dmu. Set f=O-int O dmu for a smooth gauge-invariant cap observable O.

For measurable link tangent vector fields J_e with weak weighted continuity equation
f=-mu^(-1) sum_e div_e(mu J_e),
integration by parts gives int f phi dmu=sum_e int J_e dot grad_e phi dmu. Cauchy-Schwarz implies |int f phi|²<=M(J) D(phi), with M(J)=sum_e a_e^(-1) int |J_e|² dmu. Substitution in R3-IR-432's variational dual proves

A=<f,L^(-1)f> <= M(J). (FC-1)

In fact the infimum of M(J) over admissible fluxes equals A, by taking J_e=a_e grad_e u for u=L^(-1)f (with sign set by the displayed weighted divergence). Therefore FC-1 is an exact source-specific certificate and does not require a lower bound on L for all unrelated modes.

To separate local from environmental work, select the target-neighbor shared link x and write mu(dx,dy)=rho_y(x)dx nu(dy), with rho_y>0 and int rho_y dx=1. Set m(y)=int O(x,y)rho_y(x)dx, and f_loc(x,y)=O(x,y)-m(y), f_env(y)=m(y)-int m dnu. Then f=f_loc+f_env. At each y, f_loc has zero conditional mean. Solve the weighted compact SU(2) Poisson equation
-div_x(rho_y grad_x u_y)=rho_y f_loc
with int u_y rho_y dx=0. This yields an exact local x-flux J_x=grad_x u_y with -mu^(-1)div_x(mu J_x)=f_loc and energy
M_loc=a_x^(-1)int |grad_x u_y|² dmu.
A separate global link flux K must represent f_env:
-mu^(-1) sum_e div_e(mu K_e)=f_env(y).
Then J=J_x+K satisfies the full source equation, and
A <= 2 M_loc + 2 M(K). (FC-2)
The factor two comes from |J_x+K_x|²<=2|J_x|²+2|K_x|²; if K_x=0 the energies add exactly.

Caution: solving an environmental Poisson problem relative only to the marginal nu does NOT automatically produce a valid full-configuration flux K with no x-component, because mu's conditional rho_y generally depends on y. Such a lift requires an explicit correction field. Nor does controlling M_loc alone upper-bound A.

At each finite volume strict positivity and smoothness make local and full Poisson solutions available, but their energy constants may diverge with Penrose refinement. To close R3-IR-431 one needs a family of explicit admissible fluxes with int_0^1 M_t(J_t)dt <= a0²/[8 b_g P(1)]. No such uniform bound has been established. This identifies a constructive alternative to a global spectral-gap assumption without pretending it has been achieved.

No signed cap transport, physical uniform half-Haar inequality, or continuum Yang-Mills mass gap follows.
