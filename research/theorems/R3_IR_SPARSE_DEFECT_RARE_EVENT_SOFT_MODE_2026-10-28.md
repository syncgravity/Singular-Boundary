# R3-IR — Sparse-defect rare-event spectral theorem

Research date: 2026-10-28. **Status:** exact finite interacting SU(2) Wilson-vacuum estimates; conditional (unproved hypotheses) physical soft-mode alternative. Full proofs, a genuinely interacting SU(2) character-basis verifier, execution log, and manifest are in the companion archive singular_boundary_sparse_defect_rare_event_soft_mode_2026-10-28.zip. Does **not** prove a Penrose mass gap, uniform defect rarity, or continuum field survival.

## Actual vacuum inputs

Let H=sum_e a_e(-Delta_e)+sum_f b_fd_f, d_f=1-(1/2)ReTr(W_f), 0<a_e<=a*, with four links per rhombus, link-face incidence <=2, Gauss invariance at all vertices. In a fixed physical interior region D, assume the complete collar and b_f>=beta/h². The positive, normalized physical ground state Omega defines nu=Omega² Haar, K=H-E0, Gamma(A)=sum_e a_e |grad_e A|². Previously proved regional cut comparison and exponential tilt give **uniform actual-vacuum** E_nu exp(t Z)<=M for some t>0,M>=1, where Z=h sum_D d_f.

Set r_f=(arccos p_f)²/2-d_f. Choose C1 cutoff chi=1 on [0,1], chi=0 on [2,infinity], |chi'|<=Cchi, delta=h^(3/4), signed |q_f|<=q*. Let
S=sqrt(h) sum_D q_f r_f(1-chi(d_f/delta)), G=sqrt(h) sum_D q_f r_f chi(d_f/delta), and R=S+G.
The earlier actual-vacuum good part bound is ||(G-EG)Omega||<=epsilon_h<=C_G h^(1/4).
Define E_h={max_{f in D}d_f>delta}, P=nu(E_h).

## Theorem RE-1: event-localized physical source energy

Exact global SU(2) inequalities: 0<=r_f<=c0 d_f, c0=pi²/4-1, and |grad_e r_f|²<=c3 d_f³, c3=pi⁶/1152. Because the derivative of r(1-chi) vanishes when d<=delta and r<=c2 d², |grad_e[r_f(1-chi(d_f/delta))]|²<=Cs d_f³ 1_{d_f>delta}, with Cs=(sqrt(c3)+sqrt(2)Cchi c2)², c2=pi⁴/96. Four incident links and at most two faces per link give the pointwise bounds

 **Gamma(S)<=Cgamma Z 1_Eh, Cgamma=32a* q*² Cs;**
 **|S|<=c0 q* h^(-1/2) Z 1_Eh.**

The exact nonlinear ground-state Dirichlet transform gives m1(S)=<S Omega,K S Omega>=E_nu Gamma(S).

## Theorem RE-2: entropy rare-event bound and nonlinear covariance

Let Z>=0, E exp(tZ)<=M, P=Pr(E)>0 and L=log(M/P). Conditional Jensen yields E[Z 1_E]<=(P/t)L. For r=(L+2)/t>=2/t, split E[Z² 1_E] at Z=r: below r it is <=Pr²; above r, z² e^(-tz) decreases so the tail is <= M r²e^(-tr)=e^(-2)Pr². Therefore

 E[Z² 1_E]<=(1+e^(-2))P(L+2)²/t².

Apply to the actual vacuum to obtain

 **m1(S)<=J_h:=(Cgamma/t) P log(M/P).**
 **Var_nu(S)<=[c0² q*²(1+e^(-2))/(t² h)] P[2+log(M/P)]².**

Taking centered Hilbert norms and using ||(G-EG)Omega||<=epsilon_h gives

 **sqrt(Var_nu R)<=epsilon_h+[c0 q*sqrt(1+e^(-2))/(t sqrt h)] sqrt(P)[2+log(M/P)].**

Thus if P[2+log(M/P)]²=o(h), the full fixed-support Wilson–angle difference converges to zero in interacting-vacuum norm **without** a gap assumption. Conversely, if liminf Var_nu R>=v0>0, then P[2+log(M/P)]²>=c v0 h for small h. In particular the probability of at least one defect cannot be superpolynomially small; a quantitative necessary envelope is P=Omega(h/log²(1/h)), up to constants. No assertion is made that P->0 or that Var_nu R survives.

## Theorem RE-3: soft mode without separated bands

Assume **conditionally** P_h->0 and liminf Var_nu R_h>=v0>0. Since x log(1/x)->0, J_h->0. Let r=(R-ER)Omega, s=(S-ES)Omega; ||r-s||<=epsilon_h, eventually <=sqrt(v0)/4. Then ||s||²>=9v0/16. With Lambda_h=8J_h/v0, the physical high-energy projector estimate ||P_{>Lambda}s||²<=J_h/Lambda=v0/8 gives ||P_{(0,Lambda]}s||²>=7v0/16. Transfer through r-s to obtain

 **mu_R((0,Lambda_h]) >= ((sqrt(7)-1)²/16) v0**, Lambda_h->0.
 **C_R(tau)>=exp(-tau Lambda_h)((sqrt(7)-1)²/16)v0** for every tau>=0.

The *original source* therefore detects a physical excitation with energy tending to zero, and the full physical gap obeys Delta_phys<=Lambda_h->0. This requires **no two-band, neck, or unimodality hypothesis**; it only requires rarity of at least one threshold-exceeding face and survival of the full source variance. Neither condition has been established for the refining connected Penrose system.

## Theorem RE-4: independent-gap conditional implication

If separately Delta_phys>=Delta*>0, the physical Poincare inequality and the event-localized first-moment bound give

 **sqrt(Var_nu R)<=epsilon_h+sqrt[(Cgamma/(t Delta*)) P log(M/P)].**

Thus uniform gap plus P->0 would force the full remainder to vanish. This is conditional, not a proof of a gap.

## Reproducibility and limitations

The full standalone archive contains the 8.7 KB proof manuscript, Python verifier, verification log and SHA-256 manifest. The verifier checks pointwise SU(2) inequalities, cutoffs, entropy conditional moments, and independent physical character spectral/Dirichlet identities at h=0.2 (b=5), h=0.1 (b=5), h=0.05 (b=20), and the actual 3-face 10-edge spatial Penrose seed. No Monte Carlo and no modification of historical archives. Original Stage7/26 temporal Q14, fixed-support connected defect covariance, genuine vacuum extreme-event P_h, physical mass gap, quartic resolvent and continuum remain OPEN.
