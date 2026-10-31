# Exact electric shear of a local Wilson-preserving nonabelian dual transport

Date: 2026-10-31. Finite SU(2) theorem; full Penrose current estimate OPEN.

Consider a neighboring plaquette word `x z y` and a fixed `g ∈ SU(2)`. The map `x'=xg`, `z'=z`, `y'=z^{-1}g^{-1}zy` preserves the plaquette word exactly: `x'z'y'=xzy`. For the left-invariant variation `z(t)=exp(tX)z`, with original x,y fixed, the induced cross-link tangent has norm `|| d_z y'(X) ||=||(Ad_g-I)X||`, in the bi-invariant su(2) metric. Differentiate `z(t)^-1 g^-1 z(t) y`; conjugations used to left-trivialize the output tangent are isometries, yielding this norm identity.

If `Ad_g` rotates by angle θ∈[0,π], the sharp cross-link operator norm is `2|sin(θ/2)|`. The restricted input tangent along z has total output norm squared `||X||²+||(Ad_g-I)X||²`, with maximal stretch `sqrt(1+4sin²(θ/2))`. For central g, Ad_g=I and the electric shear vanishes. This does not give the operator norm of the full Jacobian for arbitrary simultaneous variations and does not establish cancellations or bounds along an entire dual path. Nor does it imply any regulator-uniform current estimate.

The proof refines the qualitative OT-3 local electric nonisometry result in `singular_boundary_deleted_face_orbit_transport_2026-10-29`. Its SO(3) adjoint finite-difference diagnostic tested six angles and 64 random noncommuting configurations per angle (max discrepancy below 7×10^-11). Exact tests, JSON and SHA-256 evidence: Library `/The Singular Boundary/Proof Audits/SB_WILSON_ELECTRIC_SHEAR_2026-10-31.zip`. The full production spanning-tree coefficient audit and signed true-vacuum bound `sup_f T_(f,h)=o(h^-1/4)` remain OPEN. No continuum mass-gap proof follows.
