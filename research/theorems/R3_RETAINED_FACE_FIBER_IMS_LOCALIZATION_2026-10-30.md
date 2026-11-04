# Fiber-adapted IMS localization in retained plaquette coordinates
Date: 2026-10-30
Status: PROVED finite-volume differential-form identities; uniform Penrose cutoff and source estimates OPEN.

Use gauge-fixed based-face coordinates (u,Y) with u=W_f in SU(2), Y retained based face holonomies. Haar measure factorizes. P averages in u, Q=I-P. Deleted potential V_-(Y) commutes with P and with multiplication by a retained-coordinate cutoff chi(Y). Require chi real, smooth, gauge-invariant under simultaneous conjugation, so the multiplication operator acts on physical gauge-invariant functions; [Q,chi]=0.

Let K=H_--E0=T+V_--E0, T=sum_e a_e(-Delta_e) under physical generator convention, and let a[v]=<v,QKQv>=<v,Kv> for v in Ran Q and form domain. Define Gamma_T(chi)=sum_e a_e |grad_e chi|² on original link space; this is coordinate-independent despite expressing chi in based-face coordinates.

For smooth v in Ran Q, integration by parts / Leibniz gives
a[chi v]=Re<chi² v,QKQ v>+int Gamma_T(chi)|v|² dm.
For the exact non-Haar vacuum q=Q Omega, with A=QKQ, source s=-QTP Omega, this specializes to
a[chi q]=Re<chi² q,s>+int Gamma_T(chi)|q|² dm.
These are exact quadratic-form identities assuming sufficient domain regularity; form-duality formulation is available otherwise. They do not imply smallness of q; the source term may have either sign, and cutoff energy can grow with refinement.

A more general identity holds for any real gauge invariant chi(Y), regardless of its support or geometry. The key fact is that chi commutes with the fiber Haar projection, unlike a cap indicator M_delta(u). Thus retained-coordinate IMS localization preserves Ran Q. A partition of unity sum_i chi_i²=1 of such cutoffs gives sum_i a[chi_i v]=a[v]+int sum_i Gamma_T(chi_i)|v|² dm, provided the sum is finite and regular.

For centered face u cap M_delta, [Q,M_delta] is generally nonzero; never apply the retained-coordinate IMS formula with chi=M_delta.

Remaining obligations: construct cutoffs chi(Y) with provably controlled sum_e a_e|grad_e chi|² for actual Penrose dual-path face coordinate transformation; obtain uniform local bound on electric source -QTP Omega; combine with a noncircular sector coercivity or direct cap comparison. No polynomial Penrose cap bound, deletion scaling, or continuum mass gap proved.
