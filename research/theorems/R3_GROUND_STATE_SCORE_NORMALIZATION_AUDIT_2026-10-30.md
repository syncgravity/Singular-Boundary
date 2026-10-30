# Ground-state transform, marginal Fisher contraction, and score-normalization audit
Date: 2026-10-30
Status: exact identities for finite compact SU(2) link lattice; original signed-current constant requires correction; interacting scaling OPEN.

Let H=-sum_e a_e Delta_e+V, H Omega=E Omega, Omega>0, integral Omega^2 dm=1. Dirichlet Gamma_a(g,k)=sum_e a_e grad_e g dot grad_e k. On simple face f put p=Tr(U_f)/2, u=arccos p, A=sum boundary a_e. The full-angle Haar marginal is rho_H=(2/pi)sin^2 u; write probability marginal =rho_H psi(u)^2 du.

1. Exact ground-state transform: <g Omega,(H-E)k Omega>_{dm} = integral Omega^2 Gamma_a(g,k) dm, for admissible real g,k. It follows by integrating H Omega=E Omega by parts.

2. Conditional-score Ward identity: for regular u, E_{Omega^2}[Gamma_a(u,log Omega)|u]=A psi'(u)/psi(u). Proof: apply Haar integration by parts to test g(u) and Omega^2: integral Omega^2 Delta_a g=-2 integral Omega^2 Gamma_a(g,log Omega). With Delta_a g=A(g''+2 cot(u)g'), integrating the left against rho_H psi^2 gives -2A integral rho_H psi psi' g'. Cancel terms to obtain the identity. Since Gamma_a(p,log Omega)=-sin(u)Gamma_a(u,log Omega), C(p):=E_{Omega^2}[Gamma_a(p,log Omega)|p] satisfies d log psi/du=-C(cos u)/(A sin u). This is NOT the previously quoted -4 C/(A sin u), under the same definitions and unit-S3 generator. A factor 4 could arise only from a different explicitly changed definition of C or A; scaling all a_e equally does not introduce it.

3. Exact radial Fisher-energy contraction: A int rho_H |psi'|^2 du <= int Omega^2 Gamma_a(log Omega,log Omega)dm = sum_e a_e int |grad_e Omega|^2 dm. The proof applies conditional Cauchy-Schwarz to E[Gamma_a(u,log Omega)|u] and Gamma_a(u,u)=A; integrate psi^2 rho_H. Equality requires the weighted score to be a purely radial direction almost everywhere. For folded class angle the same inequality holds with the folded psi by conditional averaging; cusp at pi/2 is measure zero and regular endpoint trace needs checking.

4. Ground energy yields T_kin=E-int V Omega^2 dm; therefore R_rad=int rho_H |psi'|² <= (E-inf V)/A. This is a rigorous but potentially crude bound, and does not imply shrinking cap survival without additional quantitative control.

5. The exact ground-state transform alone provides no preferred SIGN for psi'/psi: smooth strictly positive radial wavefunctions increasing toward the equator can be realized as ground states of smooth shifted potentials. No spectral-gap lower bound for H-E has been assumed. The local incidence estimate for |X_f V| likewise does not control the conditional transverse score.

6. The published current budget normalization and any numerical constants in downstream deletion estimates must be audited before reuse. The open connected Penrose target remains a model-specific uniform one-sided bound on center-to-exterior amplitude growth, with correct normalization, or an independent relative cap-mass bound. No continuum mass-gap theorem is claimed.
