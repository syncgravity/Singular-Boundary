# Wilson-observable low-energy frame criterion for the collective deleted-face current
Date: 2026-10-30
Status: exact finite-volume overlap identity and conditional frame theorem; no uniform Penrose frame or overlap estimate proved.

Setup: H_-=T+V_- on a finite SU(2) gauge link lattice, positive real normalized ground state Omega, K=H_--E>=0, and smooth Haar-preserving dual-path action generators D_a with D_a*=-D_a. Let P_L=1_(0,L](K), v_a=D_a Omega, and L_gamma(L)=sum_a ||P_L v_a||². Let B_i be real bounded gauge-invariant multiplication observables, ideally center-even Wilson polynomials; define w_i=P_L B_i Omega.

Lemma (Wilson-current Ward overlap): <D_a Omega,B_i Omega>=-1/2 int Omega² D_a B_i dm. Proof: integrate D_a(B_i Omega²) against Haar, using divergence-free D_a. Spectrally truncated overlap <P_L v_a,w_i> is the mixed spectral measure integrated over (0,L]. This quantity is not equal to the untruncated Ward overlap in general; the latter also contains high-energy contributions.

NO-GO: By Cauchy-Schwarz, |<P_L v_a,w_i>|² <= ||P_L v_a||² ||w_i||². Thus small response for one or finitely many unspecified B_i does not bound ||P_L v_a|| from above; a nonzero vector orthogonal to all w_i is invisible. Center parity does not forbid such orthogonality.

CONDITIONAL FRAME THEOREM: Let M_L be a closed subspace of Ran P_L containing all P_L v_a. Suppose the vectors w_i=P_L B_i Omega satisfy a LOWER frame bound
alpha_L ||x||² <= sum_i |<x,w_i>|² for all x in M_L,
with alpha_L>0. Then
L_gamma(L) <= alpha_L^-1 sum_{a,i} |<P_L v_a,P_L B_i Omega>|².
Combining with exact high energy inequality gives
J_gamma <= alpha_L^-1 sum_{a,i}|mixed_{a,i}(L)|² + S_gamma/L.
Thus a sufficient (NOT established) condition for Haar-order deleted identity cap at delta~h is uniform over bulk f of [alpha_L^-1 sum_{a,i}|mixed|² + S_gamma/L]=o(h^(3/2)), with suitably chosen cutoffs, paths, and B_i. No assumption of a physical uniform gap is needed, but a uniform positive lower frame bound and small overlaps are serious additional dynamical requirements.

Finite cutoff P_L has finite rank for a finite compact elliptic H. Completeness of general bounded gauge-invariant multiplication observables against positive Omega implies that one can find a finite family spanning each finite-dimensional spectral subspace, giving some alpha_L>0 at fixed regulator. This qualitative existence provides NO uniform-in-h alpha_L and no small overlap. Restricting the family to a particular set of center-even Wilson loop polynomials requires proving its span covers the relevant symmetry sector. A single deleted-face character cannot be assumed to furnish such a frame.

No actual connected Penrose low spectral estimate, polynomial cap probability, bulk deletion theorem or continuum mass gap is proved.
