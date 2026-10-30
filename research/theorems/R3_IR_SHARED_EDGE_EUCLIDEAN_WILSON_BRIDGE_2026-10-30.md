# Exact shared-edge Euclidean Wilson bridge at a private-link coupling boundary

Date: 2026-10-30. **Status:** proven fixed-volume original-link SU(2) Wilson identity, not a full-coupling signed-response estimate.

## Setting
Take a magnetically deleted target rhombus f and its neighbor g sharing one oriented edge e. At the parameter t_g=0, no retained magnetic term depends on x=U_e. The full positive ground state and its stationary ground-state Markov process split as independent stationary Haar SU(2) Brownian motion x(s) (generator a_e Delta_x) and a stationary environment process y(s) (ground-state transform of the remaining Wilson Hamiltonian). Both the full Hamiltonian and all inserted loop observables are gauge invariant.

Choose loop decompositions at time s, with appropriate orientations,
W_f(s)=x(s)L(y(s)), W_g(s)=x(s)^{-1}M(y(s)).
This is achievable by cyclically choosing the common edge as the initial edge and changing the based orientation of one simple face. Set p_g(s)=Tr W_g(s)/2 and O_f(0)=k_a(W_f(0)), where k_a is a bounded nonnegative central function. Let
alpha_a^2 = integral_SU2 k_a(W) dW,
m_a = integral_SU2 k_a(W) Tr(W)/2 dW.
Note |m_a| <= alpha_a^2; if k_a is supported in p>=cos(a)>0, then m_a>=cos(a) alpha_a^2.

## Theorem: exact all-time shared-link bridge

For any s>=0,
E_stat[O_f(0) p_g(s) | entire environmental path y(.)]
= exp(-3 a_e s/4) m_a * p_bridge(y(0),y(s)),   (WB-1)
where
p_bridge(y0,ys)=Tr[M(ys)L(y0)]/2.
For negative time use |s| with the analogous orientation of the endpoints. The trace p_bridge is a mixed-time trace function of environmental transporters; it lies in [-1,1], and its average is gauge-invariant only after the appropriate simultaneous gauge action is specified. In particular the formula is a statement in an original-link trivialization, not an independently gauge-invariant local observable at different Euclidean times.

Proof. On the chosen shared-link orientation, the SU(2) fundamental matrix coefficient obeys Delta_x p_g(x^{-1}M)=-3p_g/4. Because x(s) is independent Haar-stationary SU(2) Brownian motion, the conditional transition gives
E_x[p_g(x(s)^{-1}M_s)|x(0),y(.)]
=exp(-3a_e s/4)p_g(x(0)^{-1}M_s).
Now substitute W=x(0)L_0, so x(0)^{-1}=L_0 W^{-1}. The inner Haar integral is
integral k_a(W) Tr(L_0 W^{-1}M_s)/2 dW.
Centrality implies integral k_a(W) W^{-1}dW=m_a I in the defining representation. Cyclicity of trace yields m_a Tr(M_s L_0)/2, proving WB-1. QED.

## Corollary: exact conditional rotor-time decay, but not an ambient mixing theorem

The absolute value of the conditional shared-link correlation is bounded by
|E_stat[O_f(0)p_g(s)|y(.)]| <= exp(-3a_e s/4) alpha_a^2. (WB-2)
This is a *private-link kinematical* decay, independent of the environment's volume or interacting physical gap. It does not imply comparable decay after t_g>0, since the original-link process then no longer factorizes.

Taking environmental expectation yields
E_stat[O_f(0)p_g(s)]
=exp(-3a_e s/4) m_a E_y[p_bridge(y0,ys)]. (WB-3)
In the deleted-target four-neighbor model, center-flux evenness of F_a(t_g), holding other parameters fixed, gives its first derivative at t_g=0 equal to zero. Equivalently the time-integrated *signed* WB-3 correlation has zero value in the corresponding physical linear-response formula. **Do not infer that the environmental mixed-time trace vanishes pointwise without an independent symmetry argument.**

## Why this advances—but does not resolve—the obligation

The selected-link portion of the mixed Euclidean cap–neighbor correlation is known exactly and has a positive exponential decay times m_a. The only possible adverse sign at the decoupled boundary lies in the *environmental mixed-time Wilson bridge*. This identifies a precise Wilson-geometric source beyond generic positive-resolvent reasoning. The formula and decay are on the hyperplane t_g=0 only. No nonperturbative bound on its continuation to t_g=1 at b_g~h^-2, or a regulator-uniform cap lower bound, is proved.

Dependencies: R3_IR_PRIVATE_LINK_ALL_TIME_DECOUPLING_2026-10-30.md, R3_IR_SIGNED_SOURCE_SPECTRAL_ALIGNMENT_OBSTRUCTION_2026-10-30.md, archived four-neighbor spin selection.
