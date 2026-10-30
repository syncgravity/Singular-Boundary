# Optimized center-collar splitting criterion for completed-cage signed current

**2026-10-30 | R3-IR | Classification:** exact quantitative **conditional criterion** for the physical finite-volume completed-cage Wilson vacuum; mathematical optimization only, not a proof of the missing regulator-uniform hypotheses.

## Inputs (already established in prior Git theorems)

For each h and target f let \(\psi_{f,h}\) denote the positive target class amplitude, and
\[
\mathfrak T_{f,h}=\int_0^{\pi/2}[\partial_u\log\psi_{f,h}(\cos u)]_+du.
\]
For a collar \(0\le u\le a_0\le\pi/2\), assume an explicit bound
\[
M_{f,h}:=\sup_{\cos a_0\le p\le1}|\partial_p\log\psi_{f,h}(p)|<\infty.
\]
It is finite at every fixed h by previously proved smooth endpoint regularity, but **no useful uniform estimate is known**.

The previously established Harnack–Fisher annular theorem supplies, for any \(0<a\le a_0\),
\[
\mathfrak T_{f,h}\le M_{f,h}(1-\cos a)
+R_{f,h}\sqrt{\frac{\pi I_{f,h}}{2A_f}\cot a}.
\tag{1}
\]
Here \(R_{f,h}\) is the old one-link Harnack ratio and \(I_{f,h}\) the marginal Fisher energy, with \(I_{f,h}\le4\mathbb E T_f\).

## Optimized quantitative criterion

Choose \(a_0\le\pi/4\) and set
\[
B_{f,h}=R_{f,h}\sqrt{\frac{\pi I_{f,h}}{2A_f}}.
\]
Using \(1-\cos a\le a^2/2\) and \(\cot a\le 1/a\) for \(0<a\le\pi/4\) gives the rigorous inequality
\[
\boxed{\quad
\mathfrak T_{f,h}
\le \inf_{0<a\le a_0}\left\{\frac12 M_{f,h}a^2+B_{f,h}a^{-1/2}\right\}.
\quad}\tag{2}
\]
If \(M_{f,h}>0\) and
\[
a_*=\left(\frac{B_{f,h}}{2M_{f,h}}\right)^{2/5}\le a_0,
\]
then elementary differentiation gives
\[
\boxed{\quad
\mathfrak T_{f,h}\le
\left(2^{-9/5}+2^{1/5}\right)
M_{f,h}^{1/5}B_{f,h}^{4/5}.
\quad}\tag{3}
\]
The coefficient can equivalently be written \(5\,2^{-9/5}\). **Check:** derivative of \(M a^2/2+B a^{-1/2}\) is \(Ma-(B/2)a^{-3/2}\), yielding \(a_*^{5/2}=B/(2M)\). Substitution gives \(2^{-9/5}+2^{1/5}=5\,2^{-9/5}\).

If \(a_*>a_0\), the valid bound is the unoptimized endpoint expression \(M a_0^2/2+B a_0^{-1/2}\). If \(M=0\), the score is identically zero on the collar, and (2) is minimized at \(a=a_0\). If \(I=0\), the entire marginal log score vanishes, so the current is zero.

## Exact conditional scaling target

In the interior-optimizer case, a **sufficient, not established**, regulator-uniform condition for the original bulk-current gate is
\[
\boxed{\quad
\sup_{f\in D_R}M_{f,h}^{1/5}
R_{f,h}^{4/5}
\left(\frac{I_{f,h}}{A_f}\right)^{2/5}
=o(h^{-1/4}).
\quad}\tag{4}
\]
Uniform applicability also requires \(a_*(f,h)\le a_0\), or else separate control of the boundary expression. Taking fifth powers, the sufficient product condition may be expressed as
\[
\sup_{f\in D_R}
M_{f,h}R_{f,h}^4
\left(\frac{I_{f,h}}{A_f}\right)^2
=o(h^{-5/4}).
\tag{5}
\]
The currently available Harnack estimate permits \(R_{f,h}\) as large as \(\exp(C/h)\), so (4) does **not** follow from existing results even with polynomial bounds on the remaining factors. No assumed spectral gap may be inserted to force (4).

## Mathematical interpretation

The center singularity in the prior annular upper estimate is resolved for each fixed lattice by regularity, and the split can be optimized exactly. This converts a vague request for 'better endpoint control' into a verifiable joint one-sided derivative / cap-density / score-energy sufficient condition. It neither shows that the condition holds nor addresses the separate R3-IR source-observability spectral requirement.

**Next independent theorem:** obtain a completed-cage center-collar derivative or one-sided score estimate from the *true* Wilson eigen-equation with subexponential (preferably polynomial) local Harnack-type constants, or avoid the Harnack factor entirely through signed cancellation. A valid result must identify all dependence on h, geometry, coupling and ambient volume.

## Source and status notes

Depends on R3_IR_TRUE_VACUUM_CENTER_ENDPOINT_REGULARITY_2026-10-30.md (endpoint smoothness), R3_IR_HARNACK_FISHER_ANNULAR_CURRENT_2026-10-30.md (annular current), R3_IR_TARGET_SCORE_FISHER_CONTRACTION_2026-10-30.md (weighted Fisher). It introduces only optimization and a conditional sufficient bound; it does not independently verify every archived proof package.
