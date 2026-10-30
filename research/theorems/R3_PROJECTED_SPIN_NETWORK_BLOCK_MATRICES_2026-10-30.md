# Exact projected spin-network Gram, Galerkin and coupling matrices
Date: 2026-10-30
Status: proved finite-block algebra; no evaluated Penrose enclosures or continuum mass gap.

At each fixed finite SU(2) disk use original-link physical electric operator T=sum_e a_e(-Delta_e) and its orthonormal gauge-invariant spin-network eigenbasis psi_i for all T-eigenvalues below cutoff Lambda. Let P_f be the exact deleted-face Haar conditional projection, Q_f=I-P_f. Set u_i=Q_f psi_i, projected finite trial space V=span{u_i}, and A=Q_f(H_f^--E0)Q_f on physical Ran Q. The projected u_i are not necessarily orthogonal or linearly independent.

Define G_ij=<u_i,u_j>=<psi_i,Q_f psi_j>; H_ij=<u_i,A u_j>=<u_i,(H_f^--E0)u_j>; S_ij=<A u_i,A u_j>. Each is a finite Gram/energy/operator-image matrix, provided u_i in Dom(A) (smooth finite-volume projections). Exact matrix elements in a link spin-network basis can in principle be expressed through SU(2) Haar integrals, Clebsch-Gordan contractions and Wilson loop trace multiplication, but no explicit Penrose recoupling coefficients were calculated in this note.

On the positive-rank part G>0, choose a coefficient isometry C with C* G C=I (e.g. certified inverse-square-root of the nonzero Gram eigenspace) and put Hhat=C*H C, Shat=C*S C. The trial minimum is a=lambda_min(Hhat), equivalently smallest finite generalized eigenvalue Hc=aGc for non-null directions.

Let W: C^r -> Ran Q map orthonormal coefficients to trial vectors Wz=sum_i u_i (Cz)_i. Then W*W=I, Hhat=W*A W, Shat=W*A²W (the latter interpreted as norm of operator images), and the off-diagonal coupling B=(I-WW*)A W. Exactly
B*B = Shat - Hhat² >=0,
hence b²=||B||²=lambda_max(Shat-Hhat²).
This is a direct rigorous algebraic identity. The residual matrix must be positive semidefinite in exact arithmetic; significant negative eigenvalues in computed intervals indicate inconsistent approximations. Need rigorous interval enclosures of G,H,S and a robust Gram rank certification.

The constant ground energy E0 enters H and S. If only E0 in a rigorous interval [E_low,E_up], one must propagate this interval through operator images and the trial matrix, not silently use a floating-point approximate eigenvalue. The complement bound d=Lambda-E_up proven previously is valid. Together with verified a,b and a*d>b², the two-block bound gives a positive full-operator Q lower enclosure. None has been numerically certified for supplied Stage26 Penrose data.

No polynomial cap probability, continuum limit, or mass gap asserted.
