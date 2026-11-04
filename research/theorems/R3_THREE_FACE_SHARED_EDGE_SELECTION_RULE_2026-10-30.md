# Three-face shared-edge selection rule and electric resolvent reduction
Date: 2026-10-30
Status: exact finite-volume mixed-order selection rule; an explicitly nonzero Penrose triple remains UNVERIFIED.

Let a finite planar SU(2) link Hamiltonian T=sum_e a_e(-Delta_e) be equipped with the physical j(j+1) normalization. For two distinct retained simple faces g,k let p_g=Tr W_g/2 and p_k=Tr W_k/2, eigenvalues lambda_g=(3/4)sum_(e in boundary g) a_e and lambda_k likewise. Put L=lambda_g+lambda_k, G=p_g p_k. Let Q_f be the deleted face Haar conditional projection, fixing all retained based holonomies. Then Q_f G=0. The product diffusion rule gives
T G=L G-2 Gamma_T(p_g,p_k),
Gamma_T(F,G)=sum_e a_e <grad_e F,grad_e G>.
Since G has zero Haar mean on the physical link manifold (using independent face holonomies and product Haar), apply the inverse T_perp^-1 on orthogonal complement of constants:
T_perp^-1 G= (1/L)G+(2/L)T_perp^-1[Gamma_T(p_g,p_k)-mean(Gamma_T(p_g,p_k))].
In fact mean(Gamma_T(p_g,p_k))=0 for distinct independent faces, by self-adjointness and mean G=0, but the centered form avoids irrelevant constant bookkeeping. Applying Q_f annihilates G and constants, yielding EXACTLY
Q_f T_perp^-1(p_g p_k)=(2/L) Q_f T_perp^-1 Gamma_T(p_g,p_k).

If faces g,k do not share a primal edge, Gamma_T(p_g,p_k)=0 pointwise, hence the mixed b_g b_k coefficient of Q_f Omega^- in the prior perturbation theorem vanishes exactly. This does NOT exclude higher mixed coupling orders nor other geometries; it only rules out the specified second-order mechanism.

If g,k share a primal edge e, Gamma_T(p_g,p_k) is supported in edge derivatives associated with their shared edges; for edge-to-edge rhombi there is at most one shared primal edge. This produces a concrete contraction to evaluate. IMPORTANT: even if Gamma is nonzero, Q_f T_perp^-1 Gamma can vanish by symmetry, and no nonzero coefficient is asserted.

Evidence inventory: Uploaded Stage26 seed sweep .npz includes correlator arrays and geometric pair indices, not an explicit embedded three-face edge-incidence/spin-network contraction. Archive 4 contains an image labeled verified_penrose_patches.png with two full finite rhombus patches, but that image is not an indexed edge-incidence list and by itself does not certify the selected triple or its SU(2) electric contraction. No Penrose local triple, nonzero source, or cap probability was numerically certified.

This selection rule refines the prior three-face obligation. No continuum mass gap proved.
