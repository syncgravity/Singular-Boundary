# Two-block full-operator Wilson spectral lower enclosure
Date: 2026-10-30
Status: exact conditional operator theorem; Penrose numerical enclosures NOT computed.

Let A=Q_f(H_f^--E_f^-)Q_f be the positive self-adjoint physical complementary-sector operator on Ran Q_f. Let Pi be orthogonal projection onto a finite Wilson trial subspace V contained in Dom A, and R=I-Pi. Suppose a>=0 and d>=0 are certified quadratic-form lower bounds Pi A Pi >=a Pi and R A R >=d R, while the off diagonal operator B=R A Pi is bounded with certified ||B||<=b. For x in V, y in V^perp, quadratic-form decomposition gives <x+y,A(x+y)> >=a||x||²+d||y||²-2b||x||||y||. The smallest eigenvalue of matrix [[a,-b],[-b,d]] gives
lambda_cert=(a+d-sqrt((a-d)²+4b²))/2.
Therefore A>=lambda_cert I. Strict positivity iff a*d>b² when a,d>0.

Domain caution: For unbounded A, the form decomposition requires V inside form domain and the complementary form domain stable under projections; choosing V in Dom A suffices for bounded off diagonal B because V is finite-dimensional and R A Pi well-defined, and R preserves form domain. Directly estimating a=smallest Galerkin eigenvalue is legitimate for the trial block but not for full A. An eigenvalue from numerical floating-point computation requires certified interval rounding to count as lower enclosure for finite A_N.

Finite-dimensional b can be bounded using verified norms of (I-Pi)A v_i on an orthonormal Wilson basis, by Hilbert-Schmidt b<=sqrt(sum_i ||(I-Pi)A v_i||²). This requires exact operator images and validated norm integrals, not merely residuals within the trial basis.

The hard input is d: a rigorous lower bound for the full orthogonal complement. Without it, the theorem cannot certify positive lambda. Potential strategies are an analytically validated high-representation Casimir inequality with controlled electric cross-terms and Wilson potential, or independent complement comparison. Such estimates have not been established for the Penrose family.

Once lambda_cert>0 is validated, insert it into the previously proved finite-Wilson cap certificate:
m_f^-(delta)>=[sqrt(c_delta)c_p-||M_delta x_N||-(||r_N||+eps_N)/lambda_cert]_+²
under the same domain assumptions and independently certified c_p, residual and source truncation enclosures. No numerical certificate or continuum theorem follows from formal existence of a,d,b.
