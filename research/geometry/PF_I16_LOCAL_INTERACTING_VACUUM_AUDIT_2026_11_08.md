# PF-I16 — Local coupled-vacuum estimate on authentic source rhombi

**2026-11-08; research audit, not a certified continuum theorem.** Parent: PF-I15 (finite electric gap and kinetic ambiguity), PF-I11 (actual accepted five-direction rhombus geometry). No cubic or Voronoi substitution. Full proof and reproducible finite geometry checker are in the accompanying local PF-I16 audit archive.

## PF-I16.A — Exact single-original-link kinetic estimate

Let the finite authenticated accepted complex be (G=(V,E,F)). Define an *auxiliary, explicitly chosen* Gauss-invariant SU(2) Hamiltonian
[
H=sum_{ein E}a_e(-Delta_e)+sum_{fin F}b_f(1-	frac12operatorname{Tr}U_f),quad a_e>0, b_fge0.
]
For the normalized strictly positive ground state (Omega), write (T_e=int|
abla_eOmega|^2dU). Then
[
oxed{T_ele 2a_e^{-1}sum_{f:einpartial f}b_f.}
]
**Proof.** Haar-average the squared wavefunction over a fixed original link and take its square root: (widetildeOmega(U_{
e e})=(int|Omega(u_e,U_{
e e})|^2du_e)^{1/2}). This is normalized and Gauss invariant. The conditional (L^2)-norm contraction ensures no increase of any other link gradient energy. The deleted link kinetic term becomes zero. Wilson potentials on faces not meeting (e) have unchanged expectations. Each incident face term lies between 0 and (2b_f), so its expectation changes by at most (2b_f). Ground-state minimality now gives (0le E[widetildeOmega]-E[Omega]le-a_eT_e+2sum_{f:einpartial f}b_f), proving the result. No independent-plaquette approximation is used.

Each original five-direction coordinate edge belongs to at most two elementary rhombi involving each of the other four directions, so (d_ele8). If (a_ege a_0>0), (b_fle b_0), this implies the **volume-independent** bound (T_ele16b_0/a_0). This incidence consequence is specific to elementary coordinate rhombi; it must be revisited if the model's face inventory changes.

## PF-I16.B — True coupled-vacuum center-cap upper bound

For a given original rhombus (f), define (B_f(delta)={1-	frac12mathrm{Tr}U_fledelta}), (0<deltale1). Conditional on all but any one boundary link (e), the constraint is an SU(2) cap with Haar volume (v(delta)=[	heta-sin	hetacos	heta]/pi), (	heta=arccos(1-delta)). Hölder and the standard (S^3) Sobolev inequality imply
[
oxed{
u_Omega(B_f(delta))le C_Sv(delta)^{2/3}
left(1+rac2{a_e}sum_{g:einpartial g}b_gight).}
]
Since (v(delta)sim 2^{5/2}delta^{3/2}/(3pi)), this is (O(delta)) uniformly in ambient source volume whenever the coefficient ratios are bounded. (C_S) is any valid compact (S^3) Sobolev constant, not a numerically optimized coefficient. This is an interacting-vacuum inequality, *not* a mass-gap estimate.

## PF-I16.C — What remains open

These finite Hamiltonians still require externally supplied electric coefficients, magnetic coefficients and a semigroup time. PF-I15's uniform, Fibonacci-weight and inverse-weight electric examples have different spectra on the same source complex, so the source geometry alone has not selected a unique physical kinetic scale. The local bound above does not exclude low-frequency collective excitations, does not establish any Poincaré or connected-correlation decay estimate, and does not remain automatically uniform in a refining physical scaling if (b_0/a_0) diverges. Therefore physical time/energy selection, an interacting spectral gap uniform in accepted source volume and physical regulator, continuum reconstruction, and the 4D SU(2) Yang–Mills mass gap all remain **OPEN**.

**Verification scope:** elementary 5D coordinate incidence maximum, 5-cube boundary inventory, exact SU(2) cap formula and asymptotic checked by a local Python verifier. The variational and Sobolev proofs are analytic, not computer-certified. Historical data and canonical claim-gate statuses unchanged.
