# Location-uniform one-link Wilson generating functions and frustration bottleneck
Date: 2026-10-27

## Set-up
Finite SU(2) Wilson link model with nonnegative plaquette couplings β_p, simple plaquette boundaries (each incident link appears once in a face word). Fix a link e and condition on other links. Write S_e(u)=B_e-k_e·u, with u a unit quaternion, B_e=Σ_{p∋e}β_p, and k_e=Σ_{p∋e}β_p q_{ep}, where each q_ep is a unit quaternion obtained from the oriented staple, with conventions arranged so β_p d_p=β_p(1-q_ep·u).

Set κ=|k|, F=B-κ≥0, and T=κ-k·u (when κ=0 T=0). Then S_e=F+T. Conditional heat bath π_k(du)=e^{k·u} Haar(du)/z(κ), z(s)=2I_1(s)/s, z(0)=1. For every 0<t<1,
  E[e^{tT}|others]=e^{tκ} z((1-t)κ)/z(κ) ≤ C_t,
with C_t finite, independent of κ and geometry. Indeed h(s)=e^{-s}z(s) satisfies a(1+s)^(-3/2)≤h(s)≤b(1+s)^(-3/2), so ratio h((1-t)κ)/h(κ) ≤(b/a)(1-t)^(-3/2). For κ=0 formula equals 1.

Because all incident plaquette energies are nonnegative, β_p d_p≤S_e=F+T for each p∋e. Therefore
  E_{ρ0} exp(tβ_p d_p) ≤ C_t E_{ρ0} exp(tF_e)
 and
  ρ0(β_p d_p≥s, F_e≤f)≤C_t exp(-t(s-f)).
These hold for every retained p adjacent to an integrated link e, in arbitrary finite Wilson cavities, including nonperiodic spacetime geometries. They do not imply a bound on E exp(tF_e).

## Exact coupling-dilution identity
For a prescribed retained face p, 
 E_{ρ0} exp(tβ_p d_p) = Z(β_p -> (1-t)β_p)/Z(β_p),
where all other couplings stay unchanged. Thus a uniform bound on this face's generating function is precisely a uniform local proportional-dilution free-energy comparison. This identity does not prove that comparison.

## Aligned versus opposed staples
If two incident equal-weight staples align, q1=q2, then κ=2β and F=0, and the conditional energy fluctuations are O(1). If they oppose, q1=-q2, then κ=0 and F=2β; conditional u is Haar. In that case a specified plaquette has conditional E[d_p]=1 and conditional E[e^{tβ d_p}]≥ e^{tβ} (by Jensen), so no exterior-uniform O(logβ) energy estimate holds. This does not disprove an *unconditional* uniform Gibbs estimate, because the exterior opposition event may be rare; its probability is exactly the missing dynamical input.

## Support-local statement
For a prescribed set X of retained faces, choose incident links e(p). A union-bound argument gives for any thresholds s_p and f_p:
  ρ0(∃p∈X: β_p d_p≥s_p, F_{e(p)}≤f_p) ≤ C_t Σ_{p∈X}e^{-t(s_p-f_p)}.
For simultaneous large defects or joint MGFs, shared links obstruct multiplication of one-link conditional bounds; no independence is claimed.

## Open target
Establish for a nonperiodic Penrose prism cavity a bound on the distribution of F_e or a coupled support-local frustration cost, uniformly under arbitrary deleted face supports, independent of an assumed insertion partition-function ratio. Only after this can the above one-link reduction yield the required absolute thin-support tail and a cutoff-uniform R3 contour estimate. The continuum Yang-Mills mass gap is not proved.
