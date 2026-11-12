# PF-I16 — Infrared spectral gate: bounded kinetic energy does not force a gap

**2026-11-08 · source-faithful mathematical audit, NOT a Yang–Mills mass-gap theorem.**
The full derivation, executable checker, output and checksums are in the Library archive `/The Singular Boundary/Proof Audits/PF_I16_INFRARED_GATE_2026_11_08.zip` and its accompanying complete Markdown report. Geometry: a genuine four-edge accepted PF-I11 rhombus with the original SU(2) link action, no 3D cubic/Voronoi conversion.

## Exact local countermodel

Let `p=Tr(U_f)/2` for one accepted simple source rhombus. SU(2) Haar pushforward has density `(2/pi)*sqrt(1-p^2) dp`, `E_Haar(p^2)=1/4`. Choose `0<eps<=1`, `Z=1/4+eps^2`, and the smooth strictly positive normalized gauge-invariant wavefunction
[
Omega_epsilon=sqrt{p^2+epsilon^2}/sqrt Z.
]
For each of the four original boundary links `e`, `|grad_e p|^2=(1-p^2)/4` and thus
[
T_e=int|
abla_eOmega_epsilon|^2dmu
=rac1{4Z}intrac{p^2(1-p^2)}{p^2+epsilon^2}dmule1.
]
For the weighted ground-state measure `dnu=Omega^2 dmu`, put `g=p/sqrt(p^2+eps^2)`. Then
[

u(g)=0,quad operatorname{Var}_
u(g)=1/(4Z)=1/(1+4epsilon^2).
]
For positive original-link electric coefficients `a_e`, let `A_f=sum_{e in boundary f}a_e`. The Dirichlet energy obeys
[
mathcal E_
u(g,g)=rac{A_fepsilon^4}{4Z}
intrac{1-p^2}{(p^2+epsilon^2)^2}dmu
le rac{A_fepsilon}{4Z},
]
because the class Haar density is at most `2/pi` and the real-line integral of `(x^2+eps^2)^(-2)` is `pi/(2eps^3)`. Therefore
[
oxed{Delta_
ule A_fepsilon	o0,qquad T_ele1.}
]
With unit electric coefficients the upper bound is `4 eps`. This is an explicit obstruction to concluding a Poincaré gap *from local kinetic information alone*.

## Exact auxiliary interacting Hamiltonian

For the original-link electric operator `K=sum_e a_e(-Delta_e)` and the chosen rhombus, define
[
V_epsilon(p)=rac{A_fepsilon^2}{4}
left[rac{3}{p^2+epsilon^2}+
rac{1-p^2}{(p^2+epsilon^2)^2}ight]ge0.
]
Using `Delta_e F(p)=[(1-p^2)F''(p)-3pF'(p)]/4` on every rhombus boundary edge gives
[
(K+V_epsilon)Omega_epsilon=(3A_f/4)Omega_epsilon.
]
The strictly positive eigenfunction is the true nondegenerate finite-system ground state by the ground-state transform. Its excitation gap is at most `A_f eps`.

**Strict qualification:** `V_eps` is NOT the fixed-coefficient Wilson potential `sum_f b_f(1-p_f)`. Although smooth and bounded for each epsilon, its maximum grows as `epsilon^(-2)`. This countermodel does not refute the possibility of a uniform gap for the actual bounded-coupling PF Wilson model; it specifically refutes a kinetic-bound-only proof strategy.

## Finite-band corollary from the earlier PF-I16 moments

For the authentic-source *bounded Wilson* family, prior PF-I16 inequalities give spectral first moment `m1>=c`, second moment `m2<=B^2`, and mass `m0<=1`, where
[
T_*=16b_0/a_0,quad
c=a_0rac{3+2T_*-sqrt{T_*(4T_*+3)}}{4(1+T_*)},
quad B=a_*(3+4sqrt{T_*}).
]
Splitting the first moment at `c/2` and bounding the upper tail by the second moment proves the **additional** band theorem
[
oxed{mu_f([c/2,,4B^2/c])ge 3c^2/(16B^2)>0.}
]
This detects definite excitation weight in a finite *auxiliary* energy band, not a spectral gap: low-energy additional weight remains possible.

## Conditional sufficient path; two missing estimates

If the **true** interacting Wilson-vacuum measures obey (i) approximate tensorization `Var_nu(F)<=C_AT sum_e E Var_{nu_e}(F|rest)` and (ii) uniform one-link logarithmic-vacuum oscillation `osc_{u_e}log Omega<=L`, then conditional SU(2) Poincaré with Haar first eigenvalue `3/4` yields
[
oxed{Delta_Gge (3a_0/4C_{m AT})e^{-2L}.}
]
Neither hypothesis has been proved for the genuine coupled PF Wilson vacuum. In particular, a local `H^1` bound on Omega is not an `L^infty` score/oscillation bound. A physical gap also requires a source-determined kinetic/time normalization and continuum limit.

## Provenance and verification

Companion local Python checker executes six exact-class-Haar numerical quadratures, verifies `T_e<=1`, the Rayleigh bound, smooth potential nonnegativity and direct eigenfunction substitution. The full analytic proof is in the archived report; numerical tests do not certify a uniform physical theorem. No source archives, canonical claim IDs or Observatory proof gates have been modified. Physical interacting infrared exclusion, dynamical J/clock selection, continuum and Yang–Mills mass gap remain **OPEN**.
