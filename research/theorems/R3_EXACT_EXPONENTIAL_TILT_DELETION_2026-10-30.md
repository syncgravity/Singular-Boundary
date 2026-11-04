# Exact exponential-tilt magnetic-deletion comparison
Date: 2026-10-30
Status: finite-volume theorem PROVED; polynomial deleted-vacuum cap probability OPEN.

Let H_-=sum_e a_e(-Delta_e)+V_- on a finite compact SU(2) link product, with physical convention -Delta chi_j=j(j+1)chi_j, and H_+=H_-+b_f d_f, d_f=1-p_f, p_f=Tr W_f/2. Assume simple face word, A_f=sum_{boundary f}a_e, D_f=A_f/4. Let Omega_->0 normalized, E_-, and nu the full-angle u=arccos p_f distribution under Omega_-² Haar. For g(u), exact variational comparison is Delta=E_+-E_- <= [D_f int|g'|² dnu+b_f int d_f g² dnu]/int g² dnu.

THEOREM. Put t=sqrt(2 b_f/D_f)>0 and m(delta)=nu{d_f<=delta}. For every 0<delta<=2 with m(delta)>0,
Delta <= sqrt(2D_f b_f)[log(1/m(delta))+t delta].
If 1/t<=2, set delta=1/t:
Delta <= sqrt(A_f b_f/2)[1+log(1/m(1/t))].

PROOF. Choose g=exp(-t d_f/2). Then g'=-(t/2) sin(u)g, |g'|²=(t²/4)sin²(u)g²<=(t²/2)d_f g². By D_f t²/2=b_f, kinetic term<=b_f int d_f g², so Delta<=2b_f E_t[d_f], where dnu_t=exp(-t d_f)dnu/Z(t), Z(t)=int exp(-t d_f)dnu. Relative entropy KL(nu_t||nu)=-t E_t[d_f]-log Z(t)>=0 gives E_t[d_f]<=-log Z(t)/t. Also Z(t)>=exp(-t delta)m(delta). Hence E_t[d_f]<=delta+log(1/m(delta))/t. Multiply 2b_f and use 2b_f/t=sqrt(2D_fb_f). QED.

Scaling: if A_f=O(1), b_f=O(h^-2), then t=Theta(h^-1), delta=Theta(h). If m_f(delta)>=c h^s for constants c,s>0 uniformly, then Delta_f=O(h^-1 log(1/h)). A uniform identity-cap polynomial lower bound is NOT YET PROVED for the actual connected Penrose ground state. The exponential Harnack lower bound m>=h^(3/2)exp(-C/h) only gives Delta=O(h^-2).

Under an independently established center-symmetry and cross-region amplitude K(delta) bound for the FOLDED center-distance marginal, the folded union cap mass is >= e^-2K m_H; center symmetry gives identity-cap mass =half union cap, while Haar identity cap is half folded Haar. Therefore identity cap m>=e^-2K m_H,one(delta), with m_H,one(delta)=[arccos(1-delta)-(1-delta)sqrt(2delta-delta²)]/pi. Hence Delta <=sqrt(A_f b_f/2)[1+2K(delta)+log(1/m_H,one(delta))] at delta=1/t (provided symmetry is actually verified for the Hamiltonian). In particular K=o(h^-1/4) gives Delta=o(h^-5/4) under A~1,b~h^-2 (plus logarithms), but NOT O(h^-1 polylog) unless K=O(log1/h). This is conditional and must not be conflated with the bulk theorem.

This is independently derived, not a proof of interacting continuum mass gap. No existing simulation records modified.
