# Two exact half-fiber energy sum rules for the magnetic-deleted SU(2) Wilson vacuum

**2026-10-30 | R3-IR | Status:** exact finite-volume consequence of the pre-existing EF-1 fiber equation, the center parity of the *magnetic-deleted* Hamiltonian, and smooth endpoint regularity. This is **not** a volume-uniform current estimate, a mass-gap theorem, or an independent estimate on the fiber potential.

## Inputs and parity scope

In a finite simply connected original-link SU(2) rhombus disk, consider the physical positive ground state of the Hamiltonian with the *target magnetic term omitted*. By the archived exact nonlinear fiber equation (EF-1), the positive normalized angular amplitude \(\Psi(u)\), \(0\le u\le\pi\), satisfies
\[
-\frac{A}{4}\big(\Psi''+2\cot u\,\Psi'\big)+U(u)\Psi=E_0\Psi,\qquad A=A_f>0,
\]
with \(U(u)=U_f(\cos u)\). The archived center-flux involution of the deleted-face model gives \(\Psi(\pi-u)=\Psi(u)\), hence \(\Psi'(\pi/2)=0\); endpoint smoothness gives \(\Psi'(0)=0\). Define
\[
D(u)=U(u)-E_0,\quad s(u)=\partial_u\log\Psi(u),\quad w(u)=\frac2\pi\sin^2u.
\]
For a smooth finite-volume Wilson vacuum all relevant radial derivatives are regular; the algebra below can also be understood weakly and by approximation.

**Important:** Center parity is not asserted for a Hamiltonian in which the *target magnetic term is retained*. Nor is the deleted-face center-flux involution silently assumed for arbitrary Wilson observables.

## Theorem (FES-1): physical-amplitude-weighted excess vanishes

The exact differential equation in divergence form is
\[
\frac{A}{4}\big(\sin^2u\,\Psi'(u)\big)'
=\sin^2u\,D(u)\Psi(u).
\]
Integrating from \(0\) to \(\pi/2\), using the endpoint and midpoint flux conditions, proves
\[
\boxed{\int_0^{\pi/2}w(u)D(u)\Psi(u)\,du=0.}\tag{FES-1}
\]

Thus the positive and negative parts of the exact excess energy **cancel after weighting by \(\Psi\)**. In particular, if \(D\ge0\) almost everywhere on the half interval, FES-1 and \(\Psi>0\) imply \(D=0\) almost everywhere there. The analogous statement holds for \(D\le0\).

## Theorem (FES-2): unweighted excess is a nonnegative score quadratic form

The exact Riccati identity derived previously is
\[
s'+2\cot u\,s+s^2=\frac4A D.
\]
Multiply by \(\sin^2u\) and integrate over the half interval:
\[
\int_0^{\pi/2}\sin^2u\,D(u)\,du
=\frac A4\int_0^{\pi/2}\sin^2u\,s(u)^2\,du,
\]
because \(\sin^2u\,s(u)=0\) at both ends. Hence
\[
\boxed{\int_0^{\pi/2}w(u)D(u)\,du
=\frac A4\int_0^{\pi/2}w(u)s(u)^2\,du\ge0.}\tag{FES-2}
\]
Equality holds exactly when \(s=0\) almost everywhere, in which case \(\Psi\) is constant and the fiber equation forces \(D=0\) almost everywhere.

Subtracting FES-1 from FES-2 gives the exact covariance-like balance
\[
\boxed{
\int_0^{\pi/2}w(u)D(u)\,[1-\Psi(u)]\,du
=\frac A4\int_0^{\pi/2}w(u)s(u)^2\,du.
}\tag{FES-3}
\]
No probability normalization of \(w\Psi\) is assumed; these are precisely the unnormalized half-interval weights indicated.

## Exact positive/negative energy implication

Write \(D=D_+-D_-\), with both parts nonnegative. FES-1 yields
\[
\int_0^{\pi/2} w\,D_+\,\Psi
=\int_0^{\pi/2} w\,D_-\,\Psi.
\tag{FES-4}
\]
This identifies an indispensable cancellation in the nonlinear conditional fiber energy. It does **not** bound the Haar-weighted positive part \(\int \sin u\cos u\,D_+du\) in the previously derived Riccati current inequality, because the weights \(\Psi w\) and \(\sin u\cos u\) differ sharply near the center. Without an independent lower amplitude or sign/shape estimate, FES-1–FES-4 cannot provide the required Penrose-uniform estimate.

## What the result changes

1. It prevents treating \(U-E_0\) as an everywhere-positive local energy cost in the deleted physical ground state: unless the radial amplitude is flat, the excess has both signs, by FES-1.
2. It gives an exact *signed cancellation* and *nonnegative quadratic score* identity without assuming a mass gap, Gaussian approximation, Harnack ratio or low-energy spectral decay.
3. It does not resolve whether the **positive** excess concentrates on a shrinking center layer. Such concentration is invisible to these two moment identities and is the remaining mathematical obstruction to deducing the current gate.
4. A substantive next theorem must control how the true nonadiabatic \(U_f\) varies across the center collar (or prove a one-sided cumulative weighted flux bound) from original-link magnetic geometry and electric dynamics, with Penrose-uniform constants.

**Source dependencies:** archived \`research/theorems/R3_IR_DELETED_FACE_EXACT_FIBER_HAAR_MASS_2026-10-29.md\` (EF-1 and deleted-face parity), \`research/theorems/R3_IR_RICCATI_POSITIVE_FIBER_EXCESS_CURRENT_2026-10-30.md\` (Riccati current bound), and fixed-volume endpoint regularity. The derivation is exact but is **not** independently certified by an executable numerical verifier.
