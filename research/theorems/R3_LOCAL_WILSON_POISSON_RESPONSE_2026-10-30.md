# R3-IR-553 — Local Poisson-response expansion for Wilson two-center cap

Date 2026-10-30. Exact fixed-regulator perturbative identity, plus a rigorously identified **open** localization estimate. This does not establish uniform-in-refinement control.

Let π=Ω0² μ be the unperturbed probability measure, A0=Ω0^-1(H0−E0)Ω0 the nonnegative ground-state diffusion, W=−p10 (π(W)=0 by chord-center parity), and J the edge13 center involution. Let R=A0^-1 on mean-zero L²(π), defined by the positive finite-regulator spectral gap. Choose q_b=Ω_b/Ω0 normalized by π(q_b)=1. With H_b=H0+bW and δE_b=b π(Wq_b), the eigenfunction equation is

A0 q_b + b W q_b = δE_b q_b.

For small |b| the mean-zero coefficients in q_b=1+b u1+b² u2+O(b³) satisfy
u1 = −R W,
u2 = R[W R W − π(W R W)].
Both have zero π mean; u1 is J-odd, u2 J-even. The normalized density relative to π has expansion

q_b² / π(q_b²) = 1+2b u1+b²[u1²+2u2−π(u1²)] + O(b³).

Let P_p denote π-conditional expectation at the deleted-face trace p=p0 and let t_b(p) denote the p↔−p symmetrized relative marginal. Then

**t_b(p) = 1+b² D(p)+O_{C^0}(b⁴)**

with the exact coefficient

**D(p)=P_p[u1²+2u2]−π[u1²+2u2].**

Thus, for two-center cap C_delta,
Pr_b(C_delta)/c_delta = 1+b² E_Haar[D(p)|C_delta]+O(b⁴)
where the error is uniform in cap width at each fixed compact elliptic regulator (smooth perturbation). The leading absolute relative-cap response is bounded by **||D||∞ b²**, rather than a global heat-kernel minorization. A sufficient refinement hypothesis is a uniform ||D_h||∞ plus a genuinely uniform bound on the higher even remainders in C0, or a uniform analytic neighborhood and local response norms. Merely bounding the L² spectral gap does not supply this.

The operator R is nonlocal in general. Since R W=∫₀∞ P_t W dt, proving volume-independent ||D_h||∞ requires a dynamical local-mixing/influence estimate and uniform control of P_p of these Poisson responses. The formula does not assume the conditional dynamics closes at fixed spectator links.

## Actual original M5 metric audit

Original 30×30 Whitney matrix SHA-256 d7bd716dcfa5ef640aabb824099ad614b4d64bfb781a3cbf4cc484bb8e902fbf; K=M^-1; deleted face0 edge incidence [1,4,13,0] signs [1,1,−1,−1]. Computed κ0=s^T K s/4=2.362228738429273, cross-face radial-current vector l2 norm=0.6780854027243318, and spectral operator norm of the K face-to-complement block=0.8030289533050429. This confirms nontrivial environmental coupling but is not a bound on the interacting Poisson response or on refined graphs.

## Independent regression

A 3-state reversible parity-symmetric Markov chain, A0=−[[-1,1,0],[1,−2,1],[0,1,−1]], W=diag(−1,0,1) gives u1=[1,0,−1], u2=[1/9,−2/9,1/9] and D=[5/9,−10/9,5/9]. Direct normalized lowest eigenvectors at b=.08,.04,.02,.01 yield symmetrized-density errors divided by b⁴ approaching ~1.85185. This tests perturbative coefficient algebra, not actual Penrose interacting eigensolutions.

### Next theorem obligation

Develop an actual spatial or graph-theoretic influence estimate on the resolvent R_h of the *Wilson-coupled unperturbed ground-state diffusion*, preserving nonlocal inverse-Whitney blocks and root transport. Quantify how its constants behave for computed M_h under refinement. Only after such a uniform estimate can ||D_h||∞ be certified. No continuum Yang–Mills mass gap is proved.

Executed code: research/scripts/audit_local_wilson_poisson_response.py; original binary data remains in Library.
