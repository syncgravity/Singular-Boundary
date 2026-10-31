# R3-IR-545 — Correct anisotropic radial-score Ward identity

Date: 2026-10-30. This is a **general finite elliptic SU(2)-link Hamiltonian identity**. The simplified constant-A deleted-face identity recorded in earlier research must NOT be substituted without additional geometric and conditional tests.

Let X=SU(2)^E with product normalized Haar μ, and let L=div_μ(G grad) denote the diffusion generator associated to the scalar positive electric form (the negative of the nonnegative electric Hamiltonian without its scalar coupling), with carré du champ Γ(f,g)=<df,G dg>. Let the normalized smooth positive interacting ground state be Ω, ρ=Ω², and let p=p_f=Tr(U_f)/2 for a selected Wilson plaquette; p∈(-1,1). Define m(p) as the Lebesgue density of the push-forward measure p_*(ρ μ) and define conditional coefficients

a(p)=E_ρ[Γ(p,p)|p],   b(p)=E_ρ[Lp|p],   j(p)=E_ρ[Γ(p,log Ω)|p].

For each smooth compactly supported scalar test φ in (-1,1), integration by parts yields

∫ m φ b dp = -∫ m φ' a dp - 2∫ m φ j dp.

Hence, in the distributional sense (and pointwise when the conditional functions are differentiable),

**(m a)'=m(b+2j).**

Equivalently, (log m)'=(b+2j-a')/a wherever a>0. With Haar plaquette trace density w(p)=(2/π)sqrt(1-p²) and normalized radial amplitude ψ(p)=sqrt(m(p)/w(p)), the exact score equation becomes

**(log ψ)' = j/a + (1/2)[b/a - a'/a - (log w)'].**

There is generally a *geometric drift correction* in addition to the score current. A constant one-dimensional factor Γ(p,p)=κ(1-p²), Lp=-3κ p makes b/a-a'/a=(log w)', recovering (log ψ)'=j/a, but this cancellation must be PROVED for the full matrix-coupled, Wilson-transported Penrose operator; it is not a consequence of gauge invariance alone.

### Exact two-link countermodel
Let two SU2 links U,V have p=Tr(UV)/2 and independent source-left link derivatives, with positive electric link matrix K=[[1,.4],[.4,1]]. At fixed UV=iσ_z, the link gradients are -z/2 and -Ad(U^-1)z/2 for z=(0,0,1). Thus Γ(p,p)=1/2+.2[z·Ad(U^-1)z]. Choosing U=I, U=iσ_x or U=(I+iσ_x)/sqrt2 gives Γ=.7,.3,.5, **while p=0 in all cases**. This example exhibits failure of microscopic closure on p even for an SU2 gauge-related Wilson character; it does not by itself show that conditional a(p) is nonconstant in any particular many-link ground state.

### Consequence for the research agenda
The signed radial current of the previous R3-IR-289–292 work is not by itself a sufficient description unless the correction term is controlled. The appropriate one-dimensional score budget must involve the **full** s(p)=(b+2j-a')/(2a) -(log w)'/2, or independently establish the radial geometric identity b-a' = a(log w)' for the actual interacting conditional coefficients.

The 30-link original M5 Whitney matrix, original SU2 geometry, and rooted coefficient prescription still require numerical or analytical conditional calculations of a(p), b(p), j(p) at more than one regulator and magnetic coupling, with correct coarea factors. The finite-model bound does not establish refinement-uniform center-cap mass or the continuum 3+1 Yang–Mills mass gap.

Reproducer: research/scripts/audit_anisotropic_radial_ward.py. No binary artifacts committed.
