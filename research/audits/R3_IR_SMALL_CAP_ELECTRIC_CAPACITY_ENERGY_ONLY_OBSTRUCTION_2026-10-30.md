# R3-IR-426 — Small SU(2) caps have vanishing electric capacity: an energy-only no-go

2026-10-30. Rigorous variational obstruction on SU(2), not a counterexample to the actual Wilson ground state. This tests precisely what can and cannot follow from R3-IR-425's full-coupling electric-energy budget.

Fix 0<a<pi/8. Use SU(2) class angle theta in [0,pi], Haar class measure dmu=(2/pi)sin²(theta)dtheta. Let psi_a(theta) be a smooth, center-even cutoff with 0<=psi<=1, psi=0 on [0,a] and [pi-a,pi], psi=1 on [2a,pi-2a], and |psi'|<=C/a on the two transition shells. Such cutoffs may be chosen smooth as class functions by remaining constant near the poles.

Let phi_a=psi_a/||psi_a||_2. Then phi_a is a normalized smooth center-symmetric wavefunction and its cap probability exactly vanishes:
int_{B_a(I)} |phi_a|²dmu=0.
For strict positivity use phi_(a,eps)=(psi_a+eps)/||psi_a+eps||_2, eps>0. It is smooth, everywhere positive, center even, and
P_(a,eps)(B_a(I))=eps² mu(B_a(I))/||psi_a+eps||_2².
As eps->0 the ratio of cap probability to Haar cap probability tends to zero.

Its kinetic Dirichlet energy is
E_a=int_SU2 |grad phi_a|²dU
=(2/pi)/||psi_a||_2² int_0^pi sin²(theta)|psi_a'(theta)|²dtheta.
Each shell has length O(a), sin²(theta)=O(a²), and slope O(1/a), so E_a<=C_1 a for all sufficiently small a. The normalized positive variants have energy <=C_2 a uniformly in 0<eps<=1.

For any chosen positive electric coefficient a_x, multiplying by a_x gives a_x E_a=O(a_x a). Thus for every fixed budget b_g/a_x>0 and sufficiently small cap radius a, there exist smooth strictly positive normalized center-symmetric states satisfying < -Delta_x > <= b_g/a_x but having less than ANY prescribed positive fraction of the Haar cap mass.

More strongly, even a sequence of kinetic energies tending to zero as a->0 does not force half-Haar mass in the simultaneous shrinking caps. The cost of suppressing the cap is controlled by its H^1 capacity O(a), whereas its Haar mass is O(a³).

Consequences:
1. R3-IR-425's actual Wilson ground-state estimate a_x<-Delta_x><=b_g, without further structure from the Wilson eigen-equation or environment, cannot imply a regulator-uniform half-Haar cap bound.
2. Even a hypothetical strengthened energy estimate with <-Delta_x>->0 could fail to certify shrinking cap survival unless its scale is sufficiently restrictive relative to a. This construction shows energy bound of order a is compatible with eliminating cap mass. It does not prove a necessary sharp threshold for all admissible densities.
3. The constructed wavefunctions are test states on SU(2), NOT claimed to be Wilson vacuum states. Center symmetry is respected, so the obstruction survives the R3-IR-420 symmetry constraint. A Wilson-specific Harnack, conditional density, or nonperturbative signed cap comparison would be needed to go beyond an energy-only argument.

This is an exact analytic obstruction to a proof method, not a result about a continuum mass gap.
