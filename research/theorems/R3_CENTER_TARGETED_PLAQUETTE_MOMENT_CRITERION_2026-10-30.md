# R3-IR-505: center-targeted moment inequalities and the strong-magnetic SU2 rotor

Date: 2026-10-30. Scope: precise finite-regulator probability inequalities; a standalone SU2 rotor example. **Not a proof of local Penrose moment control or a Yang-Mills mass gap.**

Let p_f(U)=Tr U_f/2 in [-1,1] and C_delta={|p_f|>=1-delta} with 0<delta<1. On C_delta^c we have 1-p_f²>1-(1-delta)²=2delta-delta². For any normalized state psi, integrating this nonnegative inequality yields

Prob_psi(C_delta)>=max(0, 1- <1-p_f²>_psi/(2delta-delta²)).

No assumption on kinetic diagonalization, independence of plaquettes, gauge invariance of a wavefunction, or existence of a density lower bound is needed. This is the EXACT Markov/moment criterion (strictness at the boundary is irrelevant for the integral). In particular sufficient local input <1-p_f²>_Omega <= (1-c)(2delta-delta²) implies Prob_Omega(C_delta)>=c. However for the original requested shrinking-cap lower bound proportional to delta^(3/2), this criterion requires a DELTA-DEPENDENT moment estimate or another mechanism, and is usually vacuous for a fixed state as delta->0. Do not claim a uniform small-delta coefficient from an O(1) second moment bound.

Also C_delta^c is contained in {1-p_f>delta}, so Prob_psi(C_delta)>=max(0,1-<1-p_f>_psi/delta). The latter can be preferable for an identity-localized phase, but is not symmetric in center.

For the single SU2 rotor H=a(-Delta)+b(1-p), whose normalized ground state Omega satisfies b<1-p>_Omega <= E0, use the exact trial family psi_n=(1+p)^n to get E0<= 3 a n²/[4(4n+1)] +3 b/(2n+3). Then for each delta>0,

Prob_Omega(C_delta) >= max(0,1-(3 a n²/[4(4n+1)] +3 b/(2n+3))/(b delta)).

For n~sqrt(8b/a), this tends to 1 as b/a->infinity. It is consistent with the previously established divergence of osc(log Omega²): center concentration is not equivalent to full-group Harnack control.

At a=1, delta=0.1, b=10^4 gives a certified algebraic lower bound 0.894260256..., and b=10^8 gives 0.998939372... (decimals rounded). Verified with exact Fraction arithmetic in research/scripts/validate_center_targeted_moment.py.

For the interacting Penrose disk, no estimate <1-p_f²>_Omega =o(delta) or small <1-p_f>_Omega has yet been derived from the inverse-Whitney kinetic form. The local moments cannot be bounded by the total magnetic energy without a volume-dependent loss; conditional magnetic correlations still matter. No refinement-uniform shrinking center-cap estimate and no continuum Yang-Mills mass gap is established.
