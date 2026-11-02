# Corrected-sign connected-score recurrence audit (2026-11-01)

**Scope:** finite open straight SU(2) original-link chain; exact formal transform and adjacent two-face quadratic inversion. The detailed audit, checker, execution log, and checksums are retained in Library /The Singular Boundary/Proof Audits/R3_IR_CONNECTED_RECURRENCE_AUDIT_2026-11-01.zip.

Take (K=-\sum_{e,\alpha}a_eD_{e,\alpha}^2), (\Gamma(f,g)=\sum_{e,\alpha}a_e(D_{e,\alpha}f)(D_{e,\alpha}g)), (H_\lambda=K+\lambda V) and positive eigenfunction (\Omega_\lambda=e^{S_\lambda}). The identity (K e^S/e^S=KS-\Gamma(S,S)) yields
[
KS_\lambda=E(\lambda)-\lambda V+\Gamma(S_\lambda,S_\lambda).
]
With (P_0S_n=0) and formal expansions (S_\lambda=\sum_{n\ge1}\lambda^nS_n), (E=\sum_{n\ge1}\lambda^nE_n),
[
KS_1=-(1-P_0)V,\quad E_1=P_0V,
]
[
KS_n=(1-P_0)\sum_{i=1}^{n-1}\Gamma(S_i,S_{n-i}),\quad
E_n=-P_0\sum_{i=1}^{n-1}\Gamma(S_i,S_{n-i})\quad(n\ge2).
]
The sign is **positive** in front of Gamma in the Poisson score recurrence. Formal coefficient identities alone do not establish analytic perturbation convergence or a connected-interval cumulant decomposition.

Previously verified adjacent-face identities (K(ab)=\frac{11}2ab+\frac12r_{AB}), (K(r_{AB})=\frac{15}2r_{AB}), and corrected (\Gamma(a,b)=\frac{ab-r_{AB}}4) give the **exact** Poisson inversion:
[
\boxed{K^{-1}\Gamma(a,b)=\frac{ab}{22}-\frac{2r_{AB}}{55}.}
]
Substitution into the quadratic block gives (K(ab/22-2r_{AB}/55)=(ab-r_{AB})/4). Two ordered cross contributions for first-order inputs (ca,cb) give (c^2(ab/11-4r_{AB}/55)). No claim is made that these constitute the full physical second-order score.

Original-link locality implies (\Gamma(f_I,g_J)=0) when there is no common original link with nontrivial derivatives; otherwise its support is contained in (I\cup J). This does not prove a connected support projection or summable all-order tree majorant, and the finite-radius loss for fully overlapping equal supports persists.

**Research verdict:** The positive-ground-state transform yields a corrected-sign formal score Poisson recurrence with explicit Haar energy counterterms. A first nontrivial adjacent-face inversion is established exactly. The transformation to connected interval coefficients, all-order majorant, interacting (\lambda=1) gap, Penrose signed-current bound, and continuum Yang–Mills mass gap remain open.
