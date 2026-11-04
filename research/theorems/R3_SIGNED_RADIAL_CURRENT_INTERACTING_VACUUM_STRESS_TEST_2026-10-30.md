# R3-IR-544 — Interacting radial-current obligation: exact SU(2) rotor stress test

Date: 2026-10-30. Scope: assessment of the pre-existing signed radial-current criterion, not proof of a Penrose or continuum mass gap.

## Source-derived conditional criterion

The prior signed-current theorem (R3-IR-289–292) defines a radial amplitude ψ_f(u) by deleted-face marginal dν_f(u)=(2/π)sin²(u)ψ_f(u)² du; its conditional Ward identity and current budget T_f yield P(C_delta)>=exp(-2T_f)c_delta. The actual Penrose refinement-uniform estimate on T_f was explicitly left OPEN. These statements should only be applied after checking the Ward identity's normalization and coarea/conditional regularity for the chosen full SU2 root-transport metric, not transferred automatically to another model.

## Exact adversarial class-rotor family

On one SU2 link, set p=Tr(U)/2∈[-1,1]. Normalized Haar p law is (2/π)sqrt(1-p²)dp. For λ>=0 set ψ_λ(p)=Z_λ^-1/2 exp(-λ p²), where Z_λ=E_Haar exp(-2λ p²). This is smooth, strictly positive, center symmetric and normalized. For the standard SU2 Laplacian Δ with Δp=-(3/4)p and Γ(p,p)=(1-p²)/4, define V_λ(p)=Δψ_λ/ψ_λ=-λ/2+2λ p²+λ²p²(1-p²). Then (-Δ+V_λ)ψ_λ=0. Ground-state transform yields nonnegative form ∫ψ_λ²|∇(f/ψ_λ)|², so ψ_λ is the unique positive ground state of the compact elliptic rotor. Each V_λ is bounded (but not uniformly bounded in λ), and is a constructed quartic class potential, NOT a Wilson-linear face term.

In radial u=acos p, log ψ_λ(u)=-λ cos²u-(1/2)log Z_λ. It increases by λ from center to equator. Its one-sided log-slope integral over [0,π/2] is exactly λ, so the corresponding positive radial score-current budget is T_λ=λ with the standard rotor kinetic normalization, and the oscillation budget O_λ=λ.

The cap C_delta={|p|>=1-delta} has exact probability ratio
P_λ(C_delta)/c_delta = (1/Z_λ)* [∫_(1-delta)^1 (2/π)sqrt(1-p²)e^-2λp² dp]/[∫_(1-delta)^1 (2/π)sqrt(1-p²) dp].
As delta→0, the ratio→e^-2λ/Z_λ. Laplace asymptotics Z_λ~sqrt(2/(π λ)) yield asymptotic ratio ~sqrt(π λ/2)e^-2λ as λ→∞. Therefore no uniform-in-λ relative lower cap coefficient follows from smoothness, positivity, center symmetry, or finite-volume spectral positivity alone. This is NOT a counterexample to the specified Wilson Penrose ground state, and the mere existence of this model does not prove failure of the old radial Ward identity.

Direct numerical check at delta=.005: λ=0 has ratio 1; λ=1 gives .203315841253; λ=5 gives .000138751953263; λ=20 gives ~3.06137456251e-17. Independently the shrinking-cap asymptotic ratios are 1, .200892541790, .000130642362498, ~2.39632089240e-17.

## What remains necessary for Penrose

The actual uniform conditional current estimate remains unproved. To turn the signed-current theorem into a relative cap estimate one must establish quantitative control of the conditional ground-state score in the *actual* many-link deleted Penrose vacuum with the selected inverse Whitney metric, preserving cross-link transport, proper coarea factors, and the physical refinement couplings. Local sector coercivity from R3-IR-528 does not itself bound the signed score budget. We should test the underlying Ward identity with the full anisotropic kinetic metric before claiming that the radial coefficient A_f is constant.

There is also an independent refinement obligation to generate actual matrices M(h) and derive coupling normalization; previous h^-2 relative scaling was only an assumption. Neither a Penrose relative cap theorem nor the continuum 3+1D Yang–Mills mass gap is proved.

Reproducer: research/scripts/validate_radial_current_countermodel.py. Text-only code in Git; no binary outputs need committing.
