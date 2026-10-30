# R3-IR-438 — Constructive finite-volume environmental marginal flux via global Wilson density comparison

2026-10-30. Physical finite-volume original-link SU(2) Wilson disk. Establishes existence and an explicit (volume-dependent) energy bound for the marginal flux left open in R3-IR-437. Not refinement-uniform.

Write the complete configuration as N SU(2) original links, with product normalized Haar measure dU. The physical positive ground state Omega is gauge invariant and smooth; mu=Omega²dU. Write the electric coefficients a_e>0 and B=sum of all retained magnetic coefficients b_g. In the decomposition H=K+V, V=sum b_g(1-p_g) obeys 0<=V<=2B.

Let t>0 and let k_{a_e t} be the positive SU(2) heat kernel for each edge, with m_e(t)=min_{x,x',z}k_{a_e t}(x,z)/k_{a_e t}(x',z)>0. The bounded-potential Feynman–Kac comparison gives
exp(-2Bt)K_K(t;U,Z)<=K_H(t;U,Z)<=K_K(t;U,Z)
pointwise on product link configurations, and K_K=prod_e k_{a_e t}.
For any U,U',Z, K_K(t;U,Z)>=M_t K_K(t;U',Z), where M_t=prod_e m_e(t).
The positive vacuum eigenfunction identity implies
Omega(U)>=r_t Omega(U'), r_t=exp(-2Bt)M_t.
Therefore the full normalized density q=Omega² obeys max q/min q<=r_t^(-2). (MG-1)
This comparison uses the UNPROJECTED positive original-link kernel; the unique positive vacuum is gauge invariant. No Gauss-projected thermal trace factorization is asserted.

The Haar Poincare inequality on the product SU(2)^N with weighted electric form D_Haar(phi)=sum_e a_e int |grad_e phi|²dU has constant lambda0=(3/4)min_e a_e. Comparing q to Haar, as in R3-IR-435, gives the physical ground-state Poincare inequality
Var_mu(phi)<=r_t^(-2)lambda0^(-1) sum_e a_e int|grad_e phi|²dmu. (MG-2)
This is a valid finite-volume full Wilson coercivity estimate, very small as the volume increases.

Disintegrate mu(dx,dy)=rho_y(x)dx nu(dy), with y all environmental original links. For any smooth function phi(y) alone, its full variance equals Var_nu(phi) and its full electric form only involves environment gradients. Hence
Var_nu(phi)<=r_t^(-2)lambda0^(-1) sum_(e in env) a_e int|grad_e phi|²dnu. (MG-3)
In particular, the marginal environmental weighted Laplacian L_nu=-nu^(-1)sum_(e env) div_e(nu a_e grad_e) has positive gap >=lambda0 r_t². For the actual conditional-cap source f_env(y)=m(y)-int m dnu, solve L_nu psi=f_env with mean-zero psi. Set v_e=a_e grad_e psi. Then
-nu^(-1)sum_e div_e(nu v_e)=f_env,
and
sum_e a_e^(-1)int|v_e|²dnu
=<f_env,L_nu^(-1)f_env>_nu
<=Var_nu(m)/(lambda0 r_t²). (MG-4)

This supplies a legitimate marginal environmental flux WITH an explicit finite-volume energy bound, valid at the full Wilson coupling and with no pre-assumed interacting spectral gap. Since all spaces are compact and coefficients smooth, v has finite sup norm at fixed finite volume, permitting the exact conditional lift of R3-IR-434.

LIMITATION: r_t contains exp(-2Bt) and a product of N heat-kernel ratios. It may deteriorate extremely rapidly under Penrose refinement. Consequently MG-4 does not establish the uniform environmental flux amplitude or energy required by R3-IR-436, the half-Haar cap bound, the IR gap, or the continuum Yang-Mills mass gap.
