# PF-I16 continuation — Exact interacting Wilson spectral moments on authentic source rhombi

**Date:** 2026-11-08. **Status:** derived finite-operator theorem; independent one-rhombus Jacobi numerical consistency checks, **not** continuum Yang–Mills mass gap. Depends on PF-I11/PF-I15 original accepted rhombi and PF-I16 local interacting-vacuum bound. No cubic substitution. Coefficients below are explicitly **auxiliary**, not source-derived physical kinetic scales.

## Theorem: uniform local spectral weight above a strictly positive auxiliary frequency

On any finite authentic accepted PF two-complex, let
[
H=sum_e a_e(-Delta_e)+sum_f b_f(1-p_f),quad p_f=	frac12operatorname{Tr}U_f,
quad a_0le a_ele a_*,quad 0le b_fle b_0,
]
on the SU(2) Gauss-invariant Hilbert space. The link Casimir convention is (C_echi_{1/2}=	frac34chi_{1/2}). Let (Omega>0) be the finite interacting ground state, (
u=Omega^2dmu), and (T_e=int|
abla_eOmega|^2dmu).

PF-I16 established (T_ele 2a_e^{-1}sum_{g:einpartial g}b_g). Each elementary five-direction coordinate edge belongs to at most eight elementary rhombi; hence (T_ele T_*=16b_0/a_0), independently of ambient source volume.

Fix one genuine four-edge rhombus f. Set (p=p_f), (q=1-p^2), (Q=
u(q)). On **each original boundary link**, the SU(2) identities are
[
Delta_eq=	frac32-2q,qquad |
abla_eq|^2=q(1-q).
]
Integration by parts against (Omega^2) and Cauchy–Schwarz prove
[
|	frac32-2Q|le2sqrt{T_eQ(1-Q)},
quadLongrightarrowquad
oxed{Qge q_-(T_e)ge q_-(T_*)>0,}
]
with (q_-(T)=[3+2T-sqrt{T(4T+3)}]/[4(1+T)]).

Let (mu_f) be the positive excitation spectral measure of ((p-
u(p))Omega) for (H-E_0), and (A_f=sum_{einpartial f}a_e). The exact interacting ground-state Dirichlet form gives
[
oxed{m_1:=int E,dmu_f(E)=	frac14 A_fQge c:=a_0q_-(T_*)>0.}
]
Since magnetic potentials commute with p, the link-commutator identity gives
[
(H-E_0)pOmega=sum_{einpartial f}a_eigl(	frac34pOmega-2
abla_epcdot
abla_eOmegaigr).
]
Using (|p|le1), (|
abla_ep|le	frac12), and the bound on (T_e),
[
oxed{m_2:=int E^2dmu_f(E)le B^2,qquad B=a_*(3+4sqrt{T_*}).}
]
Here (m_2=|(H-E_0)pOmega|^2) exactly, since the centering constant is annihilated by (H-E_0).

Because (mu_f([0,infty))=operatorname{Var}_
u(p)le1), splitting the first moment at (c/2), then applying Cauchy–Schwarz to the high-energy part, proves
[
oxed{mu_f([c/2,infty))ge c^2/(4B^2)>0.}
]
This lower bound and auxiliary frequency threshold are independent of source volume **at fixed coefficient bounds**. Illustrative values for (a_0=a_*=b_0=1): (T_*=16), (c=0.0332145428310), threshold (c/2=0.0166072714155), and certified spectral weight (>7.6399	imes10^{-7}).

## Verification and limitations

A local 45-character SU(2) one-rhombus tridiagonal Jacobi verifier passed five coefficient cases and confirmed the first-moment identity against the exact matrix spectrum, local kinetic and gradient-mass inequalities, and the commutator second-moment bound. This is a **one-rhombus** check, not an independent exact computation of the full coupled many-rhombus vacuum. The complete Python verifier and SHA-256 manifest are supplied separately in the conversation research package `PF_I16_SPECTRAL_MOMENTS_2026_11_08.zip`.

**Crucial limitation:** positive spectral weight *above* a positive energy does **not** exclude spectral weight arbitrarily near zero. The result does not imply a uniform interacting Poincaré inequality, spectral gap, physical-time selection, refinement-uniform physical mass, OS reconstruction, or continuum Yang–Mills. Nor has boundedness of (b_0/a_0) been established along any physical coupling/refinement trajectory. All these gates remain **OPEN**. The next step must control the low-energy spectral region for the full interacting vacuum, with a source-justified normalization. No historical source data or canonical claim classifications were modified.