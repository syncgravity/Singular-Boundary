# Two-sided conditional fiber-flux identity and adverse-current sign criterion

2026-10-30. Status: exact finite-volume theorem for the actual positive magnetic-deleted SU(2) Wilson vacuum on a finite original-link rhombus disk. This is a refinement of archived EF-1 and FES-1, not a regulator-uniform current estimate.

## Setup

With \(A=A_f>0\), positive target angular amplitude \(\Psi(u)\), and exact nonadiabatic fiber energy \(U(u)\), the archived EF-1 equation is
\[
\frac A4(\sin^2u\,\Psi'(u))'=\sin^2u\,[U(u)-E_0]\Psi(u).
\]
Write \(D=U-E_0\), \(q(u)=\sin^2u\,D(u)\Psi(u)\). For a deleted target face, the archived center-flux symmetry gives \(\Psi'(\pi/2)=0\), while smoothness gives \(\sin^2u\Psi'(u)\to0\) at zero.

## Theorem: exact two-sided flux and sign equivalence

For every \(0<u<\pi/2\),
\[
\boxed{\quad
\frac A4\sin^2u\,\Psi'(u)
=\int_0^u q(v)\,dv
=-\int_u^{\pi/2}q(v)\,dv.
\quad}\tag{TF-1}
\]
Consequently, since \(\Psi>0\),
\[
\boxed{\quad
\partial_u\log\Psi(u)>0
\iff\int_0^u q(v)\,dv>0
\iff\int_u^{\pi/2}q(v)\,dv<0.
\quad}\tag{TF-2}
\]
In particular,
\[
\boxed{\quad
\mathfrak T_f
=\frac4A\int_0^{\pi/2}
\frac{\left[\int_0^u q(v)\,dv\right]_+}
{\sin^2u\,\Psi(u)}\,du
=\frac4A\int_0^{\pi/2}
\frac{\left[-\int_u^{\pi/2}q(v)\,dv\right]_+}
{\sin^2u\,\Psi(u)}\,du.
\quad}\tag{TF-3}
\]

**Proof.** Integrate the archived divergence equation from zero to \(u\), and separately from \(u\) to \(\pi/2\). Both endpoint fluxes vanish. Division by positive \(\Psi(u)\sin^2u\) gives the two-sided logarithmic derivative. Taking positive parts and integrating proves the budget identities. QED.

## Useful sufficient sign tests

If every initial cumulative integral \(\int_0^u q\le0\), then \(\Psi'\le0\) and \(\mathfrak T_f=0\), **without assuming that D has a single crossing**. Equivalently, if every terminal tail \(\int_u^{\pi/2}q\ge0\), the same conclusion follows. The prior EF-2 single-crossing condition is one sufficient way to establish the cumulative sign condition, but it is not necessary.

More generally, a nonnegative error envelope \(\varepsilon_f(u)\) satisfying
\[
\left[\int_0^u q(v)\,dv\right]_+\le
\varepsilon_f(u)\sin^2u\,\Psi(u)
\]
gives
\[
\mathfrak T_f\le\frac4A\int_0^{\pi/2}\varepsilon_f(u)\,du.
\]
Thus the **new independent proof target** can be a one-sided cumulative signed fiber-energy bound, with no pointwise requirement on \(D_+\), no sign-crossing restriction, and no Harnack multiplier. Such an envelope has not been established for the physical completed Penrose cages.

## Why this is not the mass-gap proof

TF-1 is an exact signed cancellation but contains the unknown physical amplitude and conditional fiber energy. It does not estimate the harmful positive initial cumulative integral. The \(\sin^{-2}u\) denominator makes pointwise bounds on \(\int D_+\) insufficient near zero; fixed-volume smoothness ensures the actual expression is finite, but not uniformly bounded. The conditional state retains collective electric modes, and no regulator-uniform comparison is supplied here. The interacting R3-IR source-inserted spectral and R2 continuum gates remain independent and open.

Dependencies: R3_IR_DELETED_FACE_EXACT_FIBER_HAAR_MASS_2026-10-29.md, R3_IR_FIBER_EXCESS_HALF_INTERVAL_SUM_RULES_2026-10-30.md, and R3_IR_RICCATI_POSITIVE_FIBER_EXCESS_CURRENT_2026-10-30.md.
