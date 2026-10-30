# R3-IR-437 — Exact conditional cap derivative and Fisher covariance control

2026-10-30. Genuine finite-volume original-link Wilson vacuum identity. This does not construct a refinement-uniform environmental flux.

Let dmu(x,y)=rho_y(x)dx dnu(y) be the strictly positive smooth ground-state measure from R3-IR-434/436. For a smooth gauge-invariant target cap observable O(x,y), set m(y)=int O(x,y)rho_y(x)dx. For any smooth environmental tangent field v(y), define the conditional score h_v(x,y)=v(y)·grad_y log rho_y(x), which has E_(rho_y)h_v=0.

Differentiate under the compact-link integral:
v·grad_y m(y)
=E_(rho_y)[v·grad_y O]+Cov_(rho_y)(O,h_v). (CD-1)

Thus the environmental variation of the conditional cap expectation splits EXACTLY into a geometric variation of the target observable and a covariance with the Wilson conditional score. For the target holonomy W_f=xL(y), the first term need not vanish: changing an environmental edge of f changes the holonomy even if the selected x is held fixed.

Cauchy-Schwarz gives the sharp pointwise certificate
|v·grad m-E_(rho_y)[v·grad O]|²
<=Var_(rho_y)(O) Var_(rho_y)(h_v). (CD-2)

After integrating y, the actual Wilson score Fisher estimate of R3-IR-436 implies
int |v·grad m-E_(rho_y)[v·grad O]|²dnu
<= [ess sup_y Var_(rho_y)(O)] 4 V_infty(v) sum_g b_g. (CD-3)
For 0<=O<=nu_cap, Var_(rho_y)(O)<=nu_cap²/4, so the RHS is at most nu_cap² V_infty(v) sum_g b_g.

This is an explicit true-ground-state bound on the score contribution to marginal cap variation, but it does not bound the geometric term E[v·grad O], the existence and norm of a marginal Poisson flux, or the potentially extensive magnetic budget. It also cannot be converted into an upper bound on Var_nu(m) without a marginal Poincare/coercivity estimate, which is precisely one of the unresolved obligations.

No signed target-cap comparison, regulator-uniform half-Haar survival, infrared gap or continuum Yang-Mills mass gap is proved.
