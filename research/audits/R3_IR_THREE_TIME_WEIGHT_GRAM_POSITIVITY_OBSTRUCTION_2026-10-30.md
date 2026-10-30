# R3-IR-411 — Indefinite time-weight obstruction in the exact Wilson three-time cap bridge

2026-10-30. Exact finite-dimensional algebraic obstruction extracted from genuine original-link SU(2) Wilson three-time identity R3-IR-409. This does not imply the full physical cap response is negative.

At zero coupling of the selected last neighboring plaquette, R3-IR-409 gives for positive source times s,t

Cov(O(0),p_g(s)p_g(t)) = (a1/12) w_a(s,t) E_y[K(A_s,A_t)],

where a=a_e>0, w_a(s,t)=exp(-2a min(s,t)-(3a/4)|s-t|), and K(A,B)=4p(A)p(B)-p(A^{-1}B). A_s is the mixed-time environmental transporter. R3-IR-410 proved K(A,B)=3 a0 b0-a_vec dot b_vec for the unit-quaternion components of A,B, so the spatial part of K has an adverse signature.

THEOREM (TW-1). The scalar time-weight w_a is not a positive semidefinite kernel on two or more distinct positive time points. Indeed, for 0<=s<t,

w_a(s,s)=exp(-2as), w_a(t,t)=exp(-2at),
w_a(s,t)=exp(-2as-(3a/4)(t-s)).

Its 2 by 2 principal determinant is

w_a(s,s) w_a(t,t)-w_a(s,t)^2
=exp(-4as)[exp(-2a(t-s))-exp(-(3a/2)(t-s))] < 0.

Thus any attempt to infer a sign of the time-integrated environmental bridge by representing this scalar w_a as a positive Gram or covariance kernel is invalid. Its failure is strict for every a>0 and every distinct pair s<t, independent of volume, lattice geometry or environmental Wilson couplings.

A useful diagnostic is the normalized two-time matrix correlation
w_a(s,t)/sqrt(w_a(s,s)w_a(t,t))=exp(a(t-s)/4)>1,
which cannot occur for a positive semidefinite covariance kernel.

The reason this does not contradict positivity of the underlying physical Euclidean process is that w_a multiplies a **cap-connected mixed three-time response**, not a positive two-point covariance. The cap insertion subtracts the uncapped spin-zero contribution and leaves a signed spin-one transport channel. Neither w_a nor K is required to be positive separately.

At coincident times the identity reduces to the physical two-face spin-one perimeter loop, whose sign was left open in R3-IR-407. TW-1 provides no sign verdict for its interacting vacuum expectation and no failure of the target cap survival conjecture; it excludes only a shortcut based on Gram positivity of w_a.

STATUS: proved elementary obstruction. Required remaining estimate must exploit genuine dynamical information on environmental loop correlations jointly with w_a and K. No nonperturbative full-coupling comparison, regulator-uniform Haar cap bound or continuum Yang–Mills gap is established.
