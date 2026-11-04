# Correction: SU(2) generator convention and current factor four
Date: 2026-10-30
Status: verified normalization correction; supersedes the factor-four allegation in R3-IR-379.

The original October 29 physical Hamiltonian uses -Delta chi_j=j(j+1)chi_j. On SU(2) this is 1/4 of the unit-round-S3 Laplacian, whose eigenvalues are 4j(j+1). Thus for A_f=sum_{e in boundary f} a_e, p_f=Tr(W_f)/2 and u=arccos p:
Gamma_a(p)=(A_f/4)(1-p^2), L_a p=-(3A_f/4)p, Gamma_a(u)=A_f/4 and L_a u=(A_f/2)cot u.

For a normalized positive ground state Omega and Haar radial density rho_0=(2/pi)sin²u, with Omega² pushforward =rho_0 psi², the exact conditional Ward identity is
E_{Omega²}[Gamma_a(u,log Omega)|u]=(A_f/4)psi'(u)/psi(u).
For C(p)=E_{Omega²}[Gamma_a(p,log Omega)|p], it follows that
d log psi/du=-4 C(cos u)/(A_f sin u).
Therefore the original October 29 factor four is correct. The October 30 note R3_GROUND_STATE_SCORE_NORMALIZATION_AUDIT_2026-10-30.md instead assumed the unit-round-S3 generator, and its assertion that the original current identity had an extra factor four is false. Scaling the generator convention without consistently scaling Gamma generated the confusion.

The exact radial fiber equation for the original Hamiltonian is -(A_f/4)rho_0^-1 (rho_0 psi')'+W psi=E psi. The Fisher contraction coefficient for this model is A_f/4. The earlier October 30 notes explicitly worked under the unit-S3 convention; their formulas in that convention are not wrong, but translating them to the physical model requires A_f -> A_f/4 in radial diffusion and the kinetic-energy budget. The folded Neumann radial spectral gap is 2 for the original generator, versus 8 for unit-round-S3, and the dimensionless Poincare inequality int|psi'|² >= 8 Var_mu(psi) remains unchanged.

This correction resolves constants, not the nonlinear Penrose conditional transverse-response estimate. The target bound and bulk deletion theorem remain open. The October 29 report's variational comparison still requires separate auditing for its probability and trial-function constants; this record does not declare those constants verified.
