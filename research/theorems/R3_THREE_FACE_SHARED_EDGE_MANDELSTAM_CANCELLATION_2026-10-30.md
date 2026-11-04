# Exact shared-edge SU(2) Mandelstam cancellation of three-face mixed deleted response
Date: 2026-10-30
Status: PROVED finite-volume second-order cancellation; no all-coupling three-face Haar theorem or Penrose continuum gap.

Consider an edge-to-edge planar rhombus disk and any two distinct retained elementary rhombi g,k. If they share an edge e, orient their face boundaries consistently so the common edge occurs with inverse orientation. Cyclically write W_g=A z and W_k=z^-1 B, where z=U_e and A,B do not contain z. The boundary word of the simple union is AB, and define p_g=Tr(Az)/2, p_k=Tr(z^-1B)/2, p_u=Tr(AB)/2. Under physical SU2 generators X_a=i sigma_a/2 and Gamma_T(F,G)=sum_edges a_e sum_a (X_e,a F)(X_e,a G), the SU2 Fierz contraction gives exactly
Gamma_T(p_g,p_k)= (a_e/4)(p_u-p_g p_k).
For nonadjacent faces Gamma_T=0. This was additionally checked by direct 2x2 matrix numerical contractions on random SU2 matrices (verification of algebra, not evidence of Penrose vacuum scaling).

All p_g,p_k,p_u are Wilson traces enclosing only retained elementary faces. In based-face coordinates with deleted f fixed by Haar averaging P_f, they depend on the retained face holonomies alone. Thus Q_f Gamma_T(p_g,p_k)=0 in BOTH adjacent and nonadjacent cases. [Strictly: this uses the standard planar identity that the trace of the union boundary is an invariant function of retained based face words, with appropriate parallel transports; if a noncanonical gauge-fixing convention is used, confirm the union trace is fixed by P_f.]

Let lambda_g=(3/4)sum_(boundary g)a_edge and similarly lambda_k. Let G=p_g p_k, L=lambda_g+lambda_k, U=p_u. The diffusion product identity T(G)=L G-2Gamma_T gives for adjacent faces
T G=(L+a_e/2)G-(a_e/2)U.
The union boundary is a simple loop with each outer edge used exactly once, so T U=lambda_u U with lambda_u=(3/4)sum_(boundary union)a_edge. Hence span{G,U} is T-invariant and contained in Ran P_f. Both functions are orthogonal to constants by independent Haar face coordinates, and T is strictly positive on this subspace. Therefore T_perp^-1 G belongs to span{G,U} and Q_f T_perp^-1 G=0. For nonadjacent faces, T G=L G and likewise Q_f T_perp^-1 G=0.

Consequently the b_g b_k mixed second-order coefficient of the deleted-face non-Haar ground-state response derived in R3_THREE_FACE_MIXED_DELETION_PERTURBATION_2026-10-30.md vanishes for ANY two retained simple planar rhombi, including adjacent ones. This supersedes the expectation in R3_THREE_FACE_SHARED_EDGE_SELECTION_RULE_2026-10-30.md that shared-edge incidence might suffice for a nonzero second-order coefficient; that older paper establishes a necessary condition but NOT sufficiency.

DO NOT INFER: this finite-dimensional closed subspace does not prove the whole retained invariant algebra is invariant under T, nor Q_f Omega^-=0 for arbitrary b_g,b_k, nor all higher perturbative orders vanish. A genuinely nonzero deleted response requires higher-order analysis or more complex Wilson combinations and explicit incidence. Existing Stage26 Monte Carlo sweep data do not directly evaluate these operator matrix elements. No polynomial cap probability or continuum mass gap proved.
