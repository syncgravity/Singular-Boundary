# Residual-certified finite-Wilson localized Q response
Date: 2026-10-30
Status: exact finite-regulator a posteriori certificate criterion; NO certified Penrose computation or continuum estimate.

On a fixed finite SU(2) Wilson disk let Omega denote normalized interacting deleted ground state, p=P_f Omega, q=Q_f Omega. Let A=Q_f(H_f^--E_f^-)Q_f as a positive self-adjoint operator on the physical Q sector, with actual finite-lattice bottom lambda_Q>0. Choose retained finite Wilson approximation p_N, source s_N=-Q_f T p_N in L², and an approximate response x_N in Dom A. Define r_N=s_N-A x_N. If a rigorously VALIDATED full-operator lower bound A>=lambda_under I with lambda_under>0 is available, then
||M_delta A^-1 s_N|| <= ||M_delta x_N|| + ||r_N||/lambda_under.
Proof: exact response = x_N+A^-1r_N, cap multiplier contraction, inverse norm <=1/lambda_under.

For actual q=A^-1s, s=-Q_f T p, include source truncation error eps_N >=||Q_fT(p-p_N)||. Then
||M_delta q|| <= ||M_delta x_N|| + (||r_N||+eps_N)/lambda_under.
In conjunction with exact cap projection bound m(delta)>=[sqrt(c_delta)||p||-||M_delta q||]_+², any independently certified lower bound c_p<=||p|| gives the FULL FINITE-LATTICE CAP CERTIFICATE:
m(delta)>= [sqrt(c_delta)c_p - ||M_delta x_N|| - (||r_N||+eps_N)/lambda_under]_+².
All terms must be rigorously enclosed; positivity and physical gauge sector are assumed. If the bracket is positive this certifies an actual lower probability at that lattice, WITHOUT knowing the exact q.

An explicit possible full-operator lower enclosure uses any certified finite-volume physical excitation gap g_under<=E1-E0 and a certified c_p<=||p||: lambda_Q>=g_under ||p||²>=g_under c_p². A Galerkin finite-matrix minimum is generally an UPPER bound on the full operator's minimum by Rayleigh-Ritz, not a validated lower bound; a spectral enclosure needs an additional method such as coercive comparison / complement estimate. As the regulator h->0, a shrinking lambda_under may render residual tolerances extremely demanding. Neither spectral enclosure nor residual/source/cap estimates have been computed from the supplied Penrose Stage26 data.

Certificate thresholds at delta_h comparable h: if c_p>=c0>0 uniformly and E_h=||M_delta x_N||+(||r_N||+eps_N)/lambda_under=o(h^(3/4)), then since c_delta~h^(3/2) the cap lower bound is Haar-order. Choosing arbitrary large N(h) qualitatively does not establish E_h small, and no continuum mass gap follows without further independent continuum conditions.

Domain warning: s_N, s must belong to L² and x_N Dom A to use displayed L² residual. If only weak forms are available, use a validated energy-dual residual and matching inverse bound; do not insert its value into the L² formula without proof.
