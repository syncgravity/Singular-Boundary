# R3-IR-520 — Midpoint heat bridges converge quantitatively to interacting ground-state probability

Date: 2026-10-30. Assume a finite connected compact SU(2)^E configuration manifold, a scalar smooth uniformly elliptic self-adjoint inverse-Whitney divergence-form kinetic operator, and bounded real magnetic multiplication potential. The heat kernel k_t(x,y)>0 is symmetric. Let E0 be its simple lowest eigenvalue and Omega>0 its L2-normalized ground state. Put Delta=E1-E0>0 (FINITE graph only).

For fixed x and t>0 define the normalized MIDPOINT BRIDGE
nu_(t,x)(dy)= k_t(x,y)^2 / k_(2t)(x,x) dHaar(y).
The semigroup law normalizes it. Expanding k_t(x,.) in an eigenbasis, its principal component is a_t Omega(.) with a_t=e^(-tE0) Omega(x); the orthogonal remainder has squared norm R_t²=sum_(n>=1) e^(-2t E_n)|phi_n(x)|². For fixed s>0 and t>=s, the spectral gap gives
R_t²/a_t² <= e^(-2(t-s)Delta) C_s(x),
C_s(x)=[e^(2sE0) k_(2s)(x,x)/Omega(x)²]-1.
The L2-normalized vector k_t(x,.)/sqrt(k_(2t)(x,x)) has overlap with Omega of squared size >=1/(1+z), z=e^(-2(t-s)Delta)C_s(x). Pure-state measurement contraction then yields, for any measurable event A,
|nu_(t,x)(A)-Prob_Omega(A)|<=sqrt(z/(1+z)).
This convergence is for the ACTUAL squared ground-state probability; the ordinary normalized endpoint heat kernel instead converges to Omega(y)/integral Omega and must not be confused with it.

For H_b=H_0-b p_f, b>=0, |p_f|<=1, a fixed full inverse-Whitney kinetic operator and arbitrary unchanged background magnetic potential, Feynman-Kac gives e^(-bt)k_t^0<=k_t^b<=e^(bt)k_t^0. The TWO half-bridges numerator and the 2t denominator together give
e^(-4bt)nu^0_(t,x)(A)<=nu^b_(t,x)(A)<=e^(4bt)nu^0_(t,x)(A).
Combine the previous spectral errors eps_i(t,x)=sqrt(z_i/(1+z_i)) to get the actual ground-state event bound:
Prob_(Omega_b)(A)>= [e^(-4bt)(Prob_(Omega_0)(A)-eps_0(t,x))-eps_b(t,x)]_+.
This is a rigorous FINITE-graph local perturbation statement, not a refinement-uniform comparison; the factor e^(-4bt) worsens with time while eps_i requires a spectral gap and controls of C_s(x). The result does not supply environment-independent constants. Strong magnetic refinement, shrinking double-center caps and continuum Yang–Mills mass gap remain OPEN.

Regression: research/scripts/validate_midpoint_heat_bridge.py, a positive 2-state model with t=.25,1,2,5. This checks exact matrix bridge normalization, gap spectral TV error and e^(±4bt) domination; it does NOT calculate Penrose heat-kernel constants.
