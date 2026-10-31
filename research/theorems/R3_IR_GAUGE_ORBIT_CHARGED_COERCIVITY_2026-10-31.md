# R3-IR — Exact local gauge-orbit coercivity of Wilson charged response

2026-10-31. **Exact finite-graph result.** It corrects the scope of the prior abstract adjoint spectral no-go: that abstract model did not impose the local electric Dirichlet-form/gauge-generator inequality obeyed by the actual original-link Wilson Hamiltonian.

## Assumptions

Finite oriented graph without loop links, original-link configuration SU(2)^E, left/right invariant orthonormal infinitesimal generators T_a=i sigma_a/2 with Casimir j(j+1). Electric kinetic operator K=sum_e a_e(-Delta_e), a_e>0 constant on each edge; magnetic potential V is smooth, gauge invariant, and bounded below. Let Omega>0 be its normalized gauge-invariant ground state, E0=inf spectrum H. Fix vertex v with incident links E(v). Let U_v(g) be its gauge unitary and Q_{v,a} its skew-adjoint Lie generators, acting by left/right link fields on the incident links. Write B_v=sum_{e incident v} a_e^{-1} (finite and positive).

## Theorem: gauge-orbit coercivity

For every smooth full-link state phi, set r=phi/Omega. The exact ground-state transform is

<phi,(H-E0)phi> = int Omega^2 sum_e a_e sum_a |X_{e,a} r|^2 dmu.

Since Omega is gauge invariant, Q_{v,a}(phi/Omega)=(Q_{v,a}phi)/Omega. As Q_{v,a} is the sum of one left/right Lie generator on each incident edge, pointwise weighted Cauchy-Schwarz gives

sum_a |Q_{v,a}r|^2 <= B_v sum_{e incident v} a_e sum_a |X_{e,a}r|^2.

Integrate against Omega^2 dmu, and use the isotypic Casimir identity -sum_a Q_{v,a}^2=j(j+1) on the spin-j sector. For each phi in that sector,

**<phi,(H-E0)phi> >= [j(j+1)/B_v] ||phi||^2.**

In particular, for the spin-one adjoint sector selected by the local Wilson force and link-score vectors,

**(H-E0)|_(v,spin1) >= delta_v = 2/B_v.**

The same bound holds on the closure of the quadratic-form domain by density. It is finite-volume and uses no assumed physical mass gap; the charged vectors are not gauge invariant. If a_e>=a_->0 and deg(v)<=d_+, then delta_v>=2a_-/d_+ independently of face count and refinement. If the electric coefficients vanish under refinement, no regulator-uniform positivity follows without further conditions.

## Wilson response implications

For a directed link e with source v, let w_a=X_{e,a}Omega and F_a=(X_{e,a}V)Omega. The exact differentiation identity (H-E0)w_a=-F_a and gauge covariance place both in spin one at v. Hence the summed Wilson force autocorrelation C_e(t)=sum_a <F_a,exp[-t(H-E0)]F_a> satisfies

**0<=C_e(t)<=C_e(0) exp[-delta_v t]**,

and the exact score norm satisfies

**S0_e=sum_a ||w_a||^2 <= S1_e/delta_v <= (3/16) B_v sum_{g: e in boundary g} b_g E[p_g] <= (3/16) B_v sum_g b_g.**

A second bound is S0_e <= C_e(0)/delta_v^2. For a deleted-face boundary link with one retained neighbor g, S1_e=(3b_g/8)E[p_g] and C_e(0)=(b_g^2/4)E[1-p_g^2]. The result **does not** control unweighted radial current or exclude rare center depletion; those remain separate analytic gates. A local gauge-charged excitation threshold is not a gauge-invariant physical mass gap.

## Necessary correction to earlier claims

The previous `R3_IR_GAUGE_CHARGED_FORCE_SELECTION_2026-10-31.md` correctly classified the force as adjoint but stated that uniform charged-sector excitation control was not derived. Its abstract two-triplet spectral countermodel remains a valid consequence of representation theory and moments **alone**, but is not compatible with fixed B_v original-link electric-form coercivity as the lower eigenvalue goes to zero. The present theorem supplies the missing additional Wilson-specific geometric input.

No numerical experiment on the M55 interacting vacuum is claimed; verification script tests SU(2) Casimir and weighted Cauchy bound independently.