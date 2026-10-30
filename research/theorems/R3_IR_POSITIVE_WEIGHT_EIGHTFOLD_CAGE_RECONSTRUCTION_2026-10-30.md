# R3-IR-418 — Positive-weight exact eightfold Wilson cage reconstruction

2026-10-30. Exact finite-volume theorem on the original-link SU(2) Wilson Hamiltonian on a planar disk with free boundary. This identifies a sufficient signed derivative condition; it does not prove that condition.

Let H(t)=H_e+sum_{i=1}^4 b_i(1-t_i p_i)+other retained plaquette terms, where f is magnetically deleted and g_i are its four neighbors. Define C(t)=<Omega(t),chi_1(W_f)Omega(t)> in the unique positive normalized Gauss-invariant vacuum. All t_i lie in [0,1]. For each i, center-flux link multiplication can reverse p_i without altering other plaquette traces or W_f, and conjugates H(t) to H(t with t_i negated) up to a scalar energy shift. Thus C is even in each t_i. The finite-volume elliptic Hamiltonian has a simple vacuum for all real parameters, hence C is real analytic in a neighborhood of the compact parameter cube.

With any one neighboring coupling zero, a private link forces the target exactly Haar in the vacuum: C(t)=0 on every coordinate hyperplane t_i=0.

LEMMA. For any C2 even function f with f(0)=0, f(x)=int_0^x (x-u) f''(u)du. This is the twice-integrated fundamental theorem of calculus.

Apply the lemma successively to all four variables, using evenness and Haar vanishing on the coordinate hyperplanes. For any t_i>=0,

C(t)=int_0^{t1}...int_0^{t4} [prod_i(t_i-u_i)] (partial_1² partial_2² partial_3² partial_4² C)(u) du1..du4. (CG-1)

At full coupling t=(1,1,1,1), this is

C(1,1,1,1)=int_[0,1]^4 [prod_i(1-u_i)] D_8 C(u)du. (CG-2)

The weight is nonnegative and its integral is 1/16. Hence if D_8 C(u)>=-epsilon uniformly on the cube, then C(1)>=-epsilon/16. In particular a positive D_8 C on the cube would give C(1)>=0. These are conditional conclusions; NO such derivative bound is proved.

The last-neighbor boundary curvature from R3-IR-412 and R3-IR-416 is A(t1,t2,t3)=partial_4² C(t1,t2,t3,0). By the same reasoning, A is even in each of the first three couplings and vanishes on every coordinate hyperplane. Thus

A(1,1,1)=int_[0,1]^3 [prod_{i=1}^3(1-u_i)] D_8 C(u1,u2,u3,0)du1 du2 du3. (CG-3)

The positive triple weight has integral 1/8. This is an exact formula connecting the *complete two-channel local curvature* to the genuine eighth-order mixed response, not merely to the one-sided three-time moment.

For any bounded central target cap k, its vacuum expectation F_k(t) has Haar baseline a0 whenever any t_i=0 and is even in all t_i. Thus the same formula applies to F_k(t)-a0, with D_8 F_k in place of D_8 C. At the boundary t4=0 the spin-one filtration further gives partial_4² F_k=(a1/3) A, but that relation does not extend to arbitrary t4 because higher spin channels appear.

No global derivative sign, cap-survival lower bound or continuum Yang-Mills mass gap follows from (CG-1)–(CG-3). They make the eighth-order signed Wilson mixed response an explicit, necessary target for this positive-weight reconstruction route. Related selection rules appeared earlier in R3-IR-390; the new emphasis is an exact positive-weight nonperturbative reconstruction over the **entire coupling cube** and its restriction to the complete two-channel curvature.
