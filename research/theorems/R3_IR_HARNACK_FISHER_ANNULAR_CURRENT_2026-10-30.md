# Harnack–Fisher annular signed-score bound and endpoint obstruction

**2026-10-30 | R3-IR | status:** exact finite-volume corollary for the true positive physical SU(2) Wilson vacuum, any target cage, with an explicitly nonuniform constant. This is **not** a uniform center-current theorem or a continuum gap. **Dependencies:** the pre-existing 2026-10-29 \`R3_IR_DELETED_FACE_LOCAL_HEAT_HARNACK_2026-10-29.md\` (LH-1/LH-2), and 2026-10-30 \`R3_IR_TARGET_SCORE_FISHER_CONTRACTION_2026-10-30.md\` (S1–S3). This note makes no claim that either input is new.

## Setup

Take a simple target Wilson face \(f\) with original boundary-link kinetic sum \(A_f=\sum_{e\in\partial f}a_e>0\), positive Gauss-invariant ground state \(\Omega\), and its target class angle \(u\in[0,\pi]\). The angular density under \(\nu=\Omega^2d\mu\) is
\[
q_f(u)=w(u)\psi_f(u)^2,\qquad w(u)=\frac{2}{\pi}\sin^2u,
\]
where \(\psi_f(u)>0\) is the square root of the target-class density relative to Haar. Its exact signed radial score is
\[
s_f(u)=\partial_u\log\psi_f(u)=-\frac{4J_f(\cos u)}{A_f\sin u}.
\]
Set the marginal Fisher energy \(I_f=A_f\int_0^\pi s_f(u)^2q_f(u)\,du\). By the existing exact score contraction (S3),
\[
I_f\le4\,\mathbb E_\nu T_f,\qquad
T_f=\sum_{e\in\partial f}a_e|\nabla_e\log\Omega|^2.
\]
Let \(R_e(t)=\exp(tB_e) M_{a_et}/m_{a_et}\) be the **volume-independent one-link** constant from LH-1, for any selected edge \(e\in\partial f\) and \(t>0\); take any finite \(R\ge R_e(t)\). The existing LH-2 implies \(R^{-2}\le\psi_f(u)^2\le R^2\) almost everywhere.

## New explicit annular inequality

For every \(0<\alpha<\beta\le\pi/2\),
\[
\boxed{
\int_\alpha^\beta [s_f(u)]_+\,du
\le\int_\alpha^\beta |s_f(u)|\,du
\le R\sqrt{\frac{I_f}{A_f}}\,
\left[\frac{\pi}{2}\big(\cot\alpha-\cot\beta\big)\right]^{1/2}.
}\tag{HF-1}
\]
In particular,
\[
\boxed{
\int_\alpha^\beta [s_f(u)]_+\,du
\le2R\sqrt{\frac{\mathbb E_\nu T_f}{A_f}}\,
\left[\frac{\pi}{2}\big(\cot\alpha-\cot\beta\big)\right]^{1/2}.
}\tag{HF-2}
\]
Optimizing the independent edge and time in \(R_e(t)\) is permitted. These bounds use only the local incident magnetic strength \(B_e=2\sum_{g:e\in\partial g}b_g\) and the local physical electric score expectation, not the full total magnetic volume.

**Proof.** Weighted Cauchy–Schwarz on the interval gives
\[
\int_\alpha^\beta |s_f|du
\le\bigg(\int_\alpha^\beta s_f^2q_fdu\bigg)^{1/2}
\bigg(\int_\alpha^\beta q_f^{-1}du\bigg)^{1/2}.
\]
The first factor is at most \((I_f/A_f)^{1/2}\). LH-2 supplies \(q_f(u)\ge R^{-2}w(u)\), so the second factor is at most
\[
R\left(\frac\pi2\int_\alpha^\beta\csc^2u\,du\right)^{1/2}
=R\left[\frac\pi2(\cot\alpha-\cot\beta)\right]^{1/2}.
\]
This gives HF-1, and S3 gives HF-2. QED.

## Precise endpoint and scaling obstruction

The multiplier diverges at \(\alpha\downarrow0\), since \(\cot\alpha\sim1/\alpha\). The center-current budget is an **unweighted** integral down to \(u=0\), so HF-1/HF-2 do not bound the complete budget. Moreover, in strong-field scaling \(b_g\asymp h^{-2}\), the earlier optimized LH bound only gives \(R\lesssim\exp(C/h)\); HF-2 is accordingly much weaker than \(o(h^{-1/4})\). These are failures of uniformity, not errors in the inequality.

The smooth positive class-amplitude cap-capacity counterexample of \`R3_IR_FISHER_TO_SIGNED_SCORE_CAPACITY_OBSTRUCTION_2026-10-30.md\` shows why this endpoint failure is not cured by a small Fisher energy alone. The actual interacting eigenfunction equation could enforce more, but it must yield either a **scale-uniform bound on a conditional target-density floor together with endpoint regularity**, or a **direct one-sided differential/current estimate**. A mere pointwise oscillation bound is also insufficient to bound total positive variation when the score changes sign many times.

## What to prove next, without circularity

Seek a true-ground-state radial differential inequality or localized semigroup comparison for the conditional target fiber that controls the sign/variation of \(\partial_u\log\psi_f\) on the entire center cap, including \(u=0\), with a Penrose-uniform sub-\(h^{-1/4}\) bound. A candidate estimate must be explicit in \(h\), original-link coefficients, collar size and boundary conditions and must not assume the desired spectral gap. This is separate from the source-inserted R3-IR low-energy gate.
