# Feshbach block response for the deleted-face Haar projection
Date: 2026-10-30
Scope: exact finite-volume identity; no uniform Penrose commutator or sector gap bound claimed.

Let H_-=T+V_- be a self-adjoint finite compact SU(2) link Hamiltonian, Omega>0 its normalized ground state and E its ground energy. K=H_--E>=0. Let P be the orthogonal Haar-average projection over the deleted based face holonomy, Q=I-P, and [V_-,P]=0 as in OT-4. Write p=P Omega and q=Q Omega. Then
QKQ q = -QKP p = -Q[T,P]Omega
as a form identity (and an operator identity whenever domain conditions hold). In particular K P Omega=[T,P]Omega, and the non-Haar q is sourced solely by electric cross-terms.

If QKQ is coercive on the Q sector, i.e. <v,Kv> >=lambda_Q||v||² for v in Ran Q with lambda_Q>0 (form domain), then
||Q Omega|| <= ||Q[T,P]Omega||/lambda_Q
whenever the right side is L2-defined. A slightly sharper statement is ||q|| <= ||QKP p||/lambda_Q. This is conditional: neither a uniform lambda_Q nor a suitably small source norm is currently established for connected Penrose refinement.

Let c_delta be the SU(2) Haar identity-cap mass. The exact projection cap estimate established in OT-4 is
m_-(delta)>= [sqrt(c_delta)*sqrt(1-eta²)-eta]_+², eta=||q||.
Therefore sufficient conditions are lambda_Q>=lambda_h>0 and ||Q[T,P]Omega||/lambda_h=o(h^(3/4)) at delta~h, uniformly in bulk f. These hypotheses are NOT proved. In particular a spectral lower bound on QKQ is not the physical mass gap: Q is a kinematic face-fiber projection and K need not reduce Q.

Further caution: the electric commutator [T,P] is generally unbounded and cannot be bounded simply by the local incidence derivative of V; appropriate operator domains and weighted form estimates are required. A finite Q-sector coercivity may exist in each finite regulator but can deteriorate as h->0. Do not infer it from the raw SU(2) orbit Poincare inequality, which concerns Haar orbit derivatives, not the Omega² ground-state transformed form.

This step is a precise resolvent/Schur-complement decomposition, not a proof of polynomial Penrose cap mass or continuum mass gap.
