# Full Wilson Q-complement coercivity from projected electric Casimir cutoff
Date: 2026-10-30
Status: PROVED full infinite-dimensional complement lower form bound at EACH fixed regulator; positive two-block certificate and Penrose continuum bounds remain OPEN.

Let H_-=T+V_-, where T=sum_e a_e(-Delta_e) with every a_e>0 and physical SU(2) Casimir -Delta chi_j=j(j+1)chi_j. V_- >=0 pointwise for the Wilson plaquette potential. H_- is restricted to the physical gauge-invariant Hilbert space. Let E0=inf spec(H_-), K=H_--E0. Let P be deleted-face conditional Haar projection preserving the physical Hilbert space, Q=I-P, and A=QKQ as a quadratic-form compression on Ran Q. Let Pi_Lambda=1_[0,Lambda)(T) on the PHYSICAL Hilbert space, and let V_Lambda=Ran(Q Pi_Lambda), a finite-dimensional subspace of Ran Q. It consists of Q-projections of finite electric Peter-Weyl/spin-network modes, NOT necessarily of retained Wilson-only functions.

THEOREM (complete high-Casimir complement bound): If v in Ran Q intersects Dom(T^1/2) and is orthogonal in L² to V_Lambda, then for every w in Ran Pi_Lambda, <v,w>=<Qv,w>=<v,Qw>=0. Hence Pi_Lambda v=0. By the spectral theorem, <v,Tv> >= Lambda ||v||². With V_- >=0,
<v,Av>=<v,Kv>=<v,Tv>+<v,V_-v>-E0||v||² >=(Lambda-E0)||v||².
For any CERTIFIED upper bound E_up>=E0, conclude D_Lambda=(I-P_V)A(I-P_V) >= (Lambda-E_up) I in form sense on V_Lambda^⊥ intersect Ran Q. This is a lower bound for the COMPLETE complement; no false inference from a Galerkin eigenvalue is used.

Trivial certified upper bound: testing H_- on the normalized constant state gives E0<=sum_(g !=f) b_g, since Haar mean of each nontrivial simple Wilson plaquette trace is zero and T annihilates the constant. Thus d_Lambda=Lambda-sum_(g!=f)b_g is explicitly valid, though possibly extremely negative unless Lambda scales with the total magnetic coupling. Any better certified variational ground-energy upper bound improves it.

Combining with the earlier two-block criterion: choose orthonormal basis of V_Lambda, certify trial minimum a_Lambda, coupling b_Lambda=||(I-P_V)A P_V||, and use d_Lambda=Lambda-E_up. If a_Lambda*d_Lambda>b_Lambda² with a_Lambda,d_Lambda>0, full A has certified lower eigenvalue lambda_cert=[a+d-sqrt((a-d)²+4b²)]/2>0. Full off-diagonal coupling is bounded since V_Lambda finite-dimensional and Q Pi_Lambda modes are smooth (subject to smoothness of Haar projection in fixed gauge coordinates).

A key caveat: Pi_Lambda may not commute with Q; using V_Lambda=Ran(Q Pi_Lambda) is ESSENTIAL. A naive V=Ran Pi_Lambda intersect Ran Q can miss low-T directions in Q and does not ensure the same complement bound.

PRACTICAL OBSTRUCTION: The number of link-electric spin-network modes below Lambda generally grows rapidly with link count, and Lambda>E_up may require an enormous subspace. This proof supplies an analytic complement bound but neither a practical matrix construction nor favorable scaling in h. It also does not establish the trial lower eigenvalue a_Lambda or coupling b_Lambda needed for a strictly positive certified global lower bound.

No full Penrose cap certificate, uniform deleted-vacuum center cap, continuum Hamiltonian, or physical mass gap is proved.
