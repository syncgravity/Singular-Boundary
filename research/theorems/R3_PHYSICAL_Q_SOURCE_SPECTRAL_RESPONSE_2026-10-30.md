# Physical Q-sector source spectral inverse-square identity
Date: 2026-10-30
Status: exact finite-volume physical-sector theorem; uniform Penrose scaling OPEN.

Let H_-=T+V_- on a finite compact SU(2) link configuration space (restricted to gauge-invariant Hilbert space), with unique normalized strictly positive ground state Omega and E0. Let K=H_--E0>=0, and P the Haar conditional projector over the deleted based face holonomy, Q=I-P. Assume [P,V_-]=0, P maps physical states to physical states, and Omega belongs to domain T; write p=P Omega and q=Q Omega. Let A=QKQ as Friedrichs self-adjoint operator on Ran Q with the induced closed form, s=-QKP p=-QTP p. The exact projected equation is A q=s (in the appropriate operator/form sense).

A has strictly positive finite-volume bottom lambda_Q>0: if a unit sequence x_n in Ran Q has <x_n,Kx_n>->0, compact resolvent plus spectral gap of K above its simple vacuum implies x_n approaches span Omega; but <x_n,Omega>=<x_n,q>, and ||P Omega||>0 ensures Omega is not in Ran Q. Quantitatively, if g=E1-E0>0 is the finite-volume physical spectral gap and c=||P Omega||²>0, then for x in Ran Q, |<Omega,x>| <=||Q Omega|| ||x|| =sqrt(1-c)||x||, hence <x,Kx> >=g (||x||²-|<Omega,x>|²)>=g c ||x||². Thus lambda_Q>=g||P Omega||². This inequality is finite-volume and provides no uniform lower bound in h.

For operator source s in Ran Q, exact spectral calculus yields q=A^-1 s, and
||q||²=integral_(0,infty) lambda^-2 dmu_s(lambda),
mu_s(B)=||1_B(A)s||².
At cutoff eps>0 this is exactly
||q||²=int_(0,eps] lambda^-2 dmu_s +int_(eps,infty)lambda^-2 dmu_s
<= int_(0,eps] lambda^-2 dmu_s +eps^-2||1_(eps,infty)(A)s||².
This refines the crude low q spectral weight by a SOURCE spectral measure, without assuming a regulator-uniform gap. It DOES NOT make the low-energy negative moment small: a small total ||s|| need not suffice when A has small eigenvalues.

Projection cap estimate from OT-4:
m_f^-(delta)>=[sqrt(c_delta)*sqrt(1-eta²)-eta]_+², eta=||q||.
Thus a sufficient open condition at delta~h for Haar-order cap survival is uniform integral lambda^-2 dmu_s=o(h^(3/2)). This is a new precise response criterion, not an independently established Penrose estimate. No continuum mass gap is asserted.

Important domain caveat: QTP p may be defined only as a quadratic-form source unless smoothness and projection regularity establish s in L2. In that case all equalities involving s and the inverse should be formulated in form dual spaces. Here the operator version is explicitly conditional on s in L2.
