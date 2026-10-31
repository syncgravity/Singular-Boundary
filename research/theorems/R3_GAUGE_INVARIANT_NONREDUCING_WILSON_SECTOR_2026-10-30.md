# R3-IR-525 — Explicit gauge-invariant nonreducing Haar sector with Wilson-transport electric coupling

Date: 2026-10-30. This theorem is a **three-link SU(2) counterexample** to automatic local-sector reduction, not an assertion that a particular Penrose link is known to fail reduction.

Use the graph consisting of two vertices r,v, one connector edge e:r→v, a loop f at r and a loop g at v. All link variables lie in SU(2), with independent normalized Haar. The loop characters p_f=(1/2)Tr U_f and p_g=(1/2)Tr U_g are gauge invariant at their vertices. Let P_e average the connector variable U_e; this preserves gauge-invariant functions and P_e(p_f p_g)=p_f p_g.

Let X_e^a, X_f^a and X_g^a be left-invariant infinitesimal derivatives at link sources, with -Σ_a(X_j^a)^2 fundamental Casimir 3/4. Define root-frame derivatives D_e=X_e, D_f=X_f and D_g=Ad(U_e)X_g. These all transform in the same adjoint frame at r. Let K be the real positive matrix, in order (e,f,g), with ones on the diagonal, K_fg=K_gf=c, |c|<1, and every other off-diagonal entry zero. Define the positive gauge-invariant Friedrichs form t[psi]=∫Σ_{ij}K_ij D_i psi · conjugate(D_j psi) dHaar. Its self-adjoint H is D* K D. Because U_e is independent of U_f and U_g, the f,g cross differential part on smooth functions is -2c Σ_a X_f^a (Ad(U_e)X_g)^a.

Identify U=p I+i v(U)·sigma; each invariant derivative of p has magnitude components v(U)/2 (sign depends on left/right convention, but simultaneous choices yield the stated sign). For the gauge-invariant ψ=p_f p_g, the e-independent terms are linear combinations of ψ and remain P_e-invariant. The cross term has the explicit dependence

(Hψ)_cross=-(c/2) v(U_f)·Ad(U_e)v(U_g).

Since Haar(U_e) pushes to uniform SO(3), its mean is zero. Hence (I-P_e)H P_e ψ=(Hψ)_cross, and by isotropy,

||(I-P_e)H P_e ψ||²=(c²/4)(1/3)(E_Haar|v(U_f)|²)(E_Haar|v(U_g)|²)=(c²/4)(1/3)(3/4)²=3c²/64>0.

The P_e sector does NOT reduce this positive, gauge-invariant, off-diagonal transported SU(2) electric operator, even without any magnetic potential. Gauge covariance and positivity do not produce the Fourier-sector protection of R3-IR-524.

Reproduction: research/scripts/validate_nonreducing_transport_sector.py. It checks SPD and uses 150000 seeded independent Haar quaternions; at c=.3 the Monte Carlo squared norm is approximately .00422640 versus exact .00421875, with opposite nonzero cross amplitudes for connector holonomy ± rotations.

**Boundary of conclusion:** This graph has based loops and explicitly chosen K. Actual Penrose patch geometry and its rooted tree paths must be inspected to determine if the analogous off-diagonal K_fg couples links whose relative parallel transporter contains the selected boundary link. Additional accidental cancellations may occur. It is NOT a proof that the specific deleted-face projection fails reduction on the archived Penrose disk, nor a strong-magnetic cap theorem or continuum Yang–Mills mass gap.

Next obligation: construct actual M5 primal tree/root transport paths and calculate (I-P_e)H_E P_e on gauge-invariant Wilson loop functions, including all coefficients and possible cancellations.
