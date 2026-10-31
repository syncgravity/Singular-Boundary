# R3-IR-605 — Conditional Ward identity and drift-correction reconciliation
Date 2026-10-31. R3-IR-604 belongs to the prior branch's candidate rooted-electric covariance theorem; this independent Ward reconciliation is R3-IR-605. **Abstract diffusion result, not an interacting Penrose-vacuum estimate.**

The uploaded previous-branch signed-current theorem states d_u log psi_f=−4C_f(cos u)/(A_f sin u) and proposes a uniform current criterion, but its interaction-dependent estimate remains open. R3-IR-598–603 subsequently flag that the complete mixed rooted-Whitney electric operator and its divergence ordering have not been recovered.

For a symmetric Haar diffusion generator L with carré du champ Gamma and positive density rho=Omega², define a(p)=E_rho[Gamma(p,p)|p], b(p)=E_rho[Lp|p], c(p)=E_rho[Gamma(p,log Omega)|p]. Haar integration by parts gives the **exact distributional identity** (a w)'=(b+2c)w. With SU2 Haar class density w_H(p)=(2/pi)sqrt(1-p²) and w=w_H psi², one has

d_p log psi = [b+2c−a'−a(log w_H)']/(2a) = [c+delta/2]/a,

where delta=b−a'−a(log w_H)'. In u=acos p, d_u log psi=−sin u [c+delta/2]/a. **The current-only formula requires a separately proved cancellation or alternate operator-specific identity for delta.**

Independently verified analytically on a reversible two-sector toy diffusion, z=±1, sector coefficient a_z=(1−p²)(2+0.4 z p), and positive density rho_z=exp(0.8 z p). Its marginal amplitude satisfies psi∝sqrt(cosh(0.8p)), exact score at p=.5 is 0.30395916980418. The full Ward identity agrees to <3e−16 at seven points, while the naive current-only quantity 2c/a=0.36990467987885 and delta=−0.10267665432974. This is NOT a counterexample to a proven Penrose-special cancellation; it is a test of what general reversible diffusion theory alone supplies.

**Remaining obligations:** recover the actual configuration-dependent rooted adjoint electric coefficient A(U), divergence-form generator and gauge-fixed measure; derive interacting conditional a_f,b_f,c_f; verify or bound delta_f; obtain uniform signed log-score estimate and only then return to the magnetic-deletion continuum argument. None is proved here. Preserve distinction between this analytic toy, finite M5 Ritz calculations, and continuum 3+1D Yang–Mills.

Full report, executable, and data are saved in Library /The Singular Boundary/Source/ as R3_IR_604_CONDITIONAL_WARD_RECONCILIATION_2026-10-31.md, audit_variable_radial_ward_2026_10_31.py, R3_IR_604_variable_coefficient_Ward_audit.json.