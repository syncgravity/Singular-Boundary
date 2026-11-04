# R3-IR-517 — Fiber elliptic cross-flux obstruction (2026-10-30)

For a finite smooth uniformly elliptic inverse-Whitney divergence-form kinetic operator in local coordinates (u,y), let A=[[A_uu,A_uy],[A_yu,A_yy]]. The positive ground-state equation is exactly

-div_u(A_uu grad_u Omega+A_uy grad_y Omega)-div_y(A_yu grad_u Omega+A_yy grad_y Omega)+(V-E0)Omega=0.

The mixed background flux and y-divergence terms preclude treating a fixed-u fiber as a closed standalone SU2 elliptic equation with only A_uu and its own potential. A positive matrix Schur complement controls the gradient-energy form, NOT the pointwise divergence of the cross flux, so it does not supply a fiberwise Harnack constant.

Explicit flat two-torus test: A=[[1,a],[a,1]], a=.35, and Omega=1+.2 cos(x+y)>0. Set V=div(A grad Omega)/Omega=-2(1+a)*.2 cos(x+y)/Omega. Then H=-div A grad+V satisfies H Omega=0; the ground-state transform proves Omega is its positive ground state. The mixed contribution -2a partial_x partial_y Omega=2a*.2 cos(x+y) is NONZERO. Uniform ellipticity and positive smooth ground state are insufficient to erase the cross flux. This is a toy PDE demonstration, NOT a statement that Penrose cap probability fails.

Archived 30-edge M5 Penrose disk numerical test: K=M^-1 has nonzero cross entries for chosen links 0,1,4,13; the Schur identity K_ee-K_eB K_BB^-1 K_Be=1/M_ee passes. The correct next task is conditional cross-flux control uniform at shrinking cap scale or an ambient semigroup/weighted-elliptic estimate. No refinement-uniform center cap or continuum Yang–Mills gap proved.

Regression: research/scripts/validate_fiber_elliptic_cross_flux.py.
