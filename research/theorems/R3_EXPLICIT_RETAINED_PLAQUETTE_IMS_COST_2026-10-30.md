# Exact retained plaquette cutoff electric geometry on Penrose rhombus disks
Date: 2026-10-30
Status: proved finite-link-local geometric estimates; physical Q source response and uniform cap probability still OPEN.

Let T=sum_e a_e(-Delta_e) on finite SU(2) link manifold, with physical -Delta chi_j=j(j+1)chi_j. Let g != f be a retained simple rhombus plaquette, W_g its product word and p_g=(1/2)Tr W_g. Set A_g=sum_{e in boundary g}a_e. The pointwise chain rule and SU(2) Casimir normalization give Gamma_T(p_g)=A_g(1-p_g²)/4. (For any incident link, other link factors move the SU(2) translation of the word but do not affect the gradient norm of its trace; nonincident links contribute zero.) Thus for smooth scalar phi, chi=phi(p_g), Gamma_T(chi)=A_g(1-p_g²)|phi'(p_g)|²/4 exactly. Chi is gauge invariant and a function of retained holonomy only, hence commutes with P_f and Q_f.

For chi_rho=phi((1-p_g)/rho) where phi' is supported at t in [c,C] with 0<c<C, and |phi'|<=L, the exact expression becomes Gamma_T(chi_rho)=[A_g/(4rho²)]|phi'((1-p_g)/rho)|²(1-p_g²). On its transition region 1-p_g<=C rho, 1-p_g²<=(2C rho), so ||Gamma_T(chi_rho)||_infty<=A_g C L²/(2rho). This uses only the four boundary edges of g and is independent of the length ell of any dual path transporting W_f. If A_g=O(1), then kinetic transition cost O(rho^-1). For nonshrinking rho the bound is O(1).

For a smooth function F(p_{g1},...,p_{gm}) of retained plaquette traces in a planar edge-to-edge disk, each edge belongs to at most two selected faces, and |sum_{g:e in boundary g} partial_g F grad_e p_g|² <= 2 sum_{g:e in boundary g}|partial_g F|² |grad_e p_g|². Thus Gamma_T(F)<= (1/2) sum_{g in selected} A_g (1-p_g²)|partial_g F|² pointwise. This bound counts selected faces but does not incur the deleted face dual path length; if many retained faces are chosen, their number and weight appear explicitly.

Substitute into fiber-compatible IMS identity for v=q=Q_f Omega:
a_f[chi q]=Re<chi² q,s>+int Gamma_T(chi)|q|².
The explicit geometric bound does NOT by itself bound s=-QTP_f Omega, ||chi q||, or the cap-localized norm ||M_delta q||, and rho^-1 growth may be problematic. No claim that a local cutoff automatically localizes q in deleted-holonomy cap.

No refinement uniform Penrose vacuum dynamics, deletion energy scaling, or continuum mass gap proved.
