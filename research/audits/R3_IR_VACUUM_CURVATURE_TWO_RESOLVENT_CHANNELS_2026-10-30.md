# R3-IR-412: Physical Wilson vacuum curvature has two resolvent channels

2026-10-30. Exact fixed-volume perturbation formula. The sign and full-coupling cap-survival bound remain OPEN.

Take H(t)=H0+t b(1-p) on the Gauss-invariant SU(2) original-link Hilbert space. Let Omega be its simple positive normalized vacuum at t=0, Q the orthogonal complement, R=Q(H0-E0)^(-1)Q and F=<Omega,O Omega>, with O a bounded positive target-cap multiplier. Center-flux parity gives <Omega,p Omega>=0 and F'(0)=0.

Differentiate the normalized real eigenvector with <Omega,Omega'(0)>=0. Then
Omega'(0)=b R p Omega,
Omega''(0)=2b² R Q p R p Omega - b² ||R p Omega||² Omega.

Hence the exact vacuum curvature is

F''(0)=4b² <QO Omega, R Q p R p Omega>
       +2b² <R p Omega,(O-F) R p Omega>. (VC-1)

Proof: H'(0)-E'(0)=-bp. Project the first and second derivatives of the eigenvalue equation into the excited subspace; use the second derivative of normalization for the longitudinal part. Differentiate <Omega_t,O Omega_t> twice.

This corrects an inference risk in R3-IR-409: its one-sided stationary reference vacuum three-time moment does NOT by itself equal the second derivative of the perturbed vacuum cap expectation. VC-1 also includes the source insertions on opposite sides of O and the vacuum normalization term. The preceding three-time calculation remains valid for the correlator it actually computes.

At the private-link boundary H0=a_e(-Delta_x)+H_environment, p Omega lies in the x-spin-1/2 sector, where R has operator norm at most 4/(3a_e). As the Haar average p²=1/4, ||R p Omega||<=2/(3a_e). This is a kinematical bound, not an interacting physical spectral gap.

No favorable sign for either signed channel, no full-coupling comparison and no continuum mass gap have been proved.