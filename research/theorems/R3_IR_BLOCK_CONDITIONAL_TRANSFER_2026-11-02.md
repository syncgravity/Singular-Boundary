# R3-IR — Conditional block resolvent and one-step boundary transfer

Date 2026-11-02. This is a uniform finite-block Hilbert-space theorem, **not** a projective Fourier inverse or convergent polymer expansion.

For a straight square SU(2) strip interval I, define S_I=sum over I of s_b(p_f), the positive reference measure mu_I proportional to exp(2 S_I) Haar, and L_I=K_I−2 Gamma(S_I,.). For |b|<=0.001 the certified local curvature theorem yields gap(L_I)>=kappa=23/144 uniformly in interval length.

On extra spectator links L_I has a nonconstant kernel of spectator functions, so the correct projection is the **conditional** projection P_I F=F−E_muI[F | spectators]. The fiberwise inverse Q_I=L_I^{-1} P_I obeys ||Q_I F||_2<=kappa^{-1}||P_I F||_2 and ||grad_I Q_I F||_2<=kappa^{-1/2}||P_I F||_2.

For one exterior neighboring face f, exactly one link e* is shared. With |s'_b|<=1/24 and |grad_e* p_f|<=1/2, the boundary insertion B_f|I F=2 Gamma_e*(s_b(p_f),Q_I F) obeys ||B_f|I F||_{L2(mu_I times Haar spectators)}<=1/sqrt(92)||P_I F||_2. The one-face normalized measure change has L2 norm-comparison factor <=13/12, hence ||B_f|I F||_{L2(mu_{I+f})}<=(13/12)/sqrt(92)||P_I F||_2. All constants independent of |I|. Two boundary directions maximum.

**Limit:** Conditional centering changes at each extension. The bounds do not establish compositions, connected influence decay, any Banach/projective Fourier closure, the physical interacting lambda=1 gap, or the continuum mass gap. Detailed proof, exact-rational verification, log, and hash manifest are in Library /The Singular Boundary/Proof Audits.