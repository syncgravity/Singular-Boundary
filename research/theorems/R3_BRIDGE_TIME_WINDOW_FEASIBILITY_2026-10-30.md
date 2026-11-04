# R3-IR-521 — Midpoint bridge feasible-time criterion (2026-10-30)

For finite compact uniformly elliptic H0 and Hb=H0-bp with |p|<=1, b>0, midpoint heat bridges satisfy a ground-state event comparison

Prob_b(A) >= [exp(-4bt)(c-eps0(t))-epsb(t)]_+, c=Prob_0(A).

At regularization time s>0 the spectral error bounds are eps_i(t)<=sqrt(z_i/(1+z_i)), z_i=C_{s,i}(x) exp(-2(t-s)Delta_i), Delta_i>0. For 0<eta<c/2, errors <=eta are guaranteed at t>=t_mix=s+max(0,log(C_{s,0}(1-eta²)/eta²)/(2Delta_0),log(C_{s,b}(1-eta²)/eta²)/(2Delta_b)); terms with C=0 contribute zero. Perturbative positivity is ensured for t<t_pert=log((c-eta)/eta)/(4b). Hence t_mix<t_pert is a SUFFICIENT feasible-window criterion. Its failure is not a proof that actual event mass vanishes.

A positive two-state test with H0=[[1.7,-1],[-1,.7]], p=diag(1,-1), s=.25, x=0, event A={1}, c=.7236067977, eta=.1 gives b=.2: t_mix=1.242704505<t_pert=2.287937315 (feasible); b=.8: t_mix=1.242704505>t_pert=.571984329 (infeasible for these bounds). The test script recomputes both constants exactly up to double precision.

No Penrose refinement-uniform spectral gaps, diagonal constants, or time window have been proved; this is an explicit METHOD obstruction, not a physical counterexample. The continuum Yang–Mills mass gap remains open.
