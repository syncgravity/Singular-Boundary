# Explicit center-flux involutions on a planar SU(2) rhombus disk

2026-10-30. Finite-graph structural proof and scope audit of archived FN-2. This is not a cap-survival theorem.

Let K be a finite connected cellulation of a topological closed disk by oriented quadrilateral faces, with all boundary edges retained as genuine dynamical SU(2) links and no externally fixed boundary link values. Define over F2 the face-edge matrix D with D_{fe}=1 iff e is in the boundary of f (orientation is irrelevant mod 2). For a selected neighbor g and distinct target f, require a vector z of edge signs satisfying D z = 1_g: the selected face has odd signed-link parity and every other face, including target, has even parity.

LEMMA (CF-G). D has full row rank F. Proof: if a row relation lambda D=0 exists, choose a face whose coefficient lambda_f=1. A planar disk has a boundary face, and a union of selected faces has a boundary edge adjacent to exactly one selected face. More algebraically, any nonempty collection of faces has an edge incident to exactly one face in the collection: take the boundary of its union in the disk, which cannot be empty. For that edge the corresponding coefficient of lambda D is 1, contradiction. Thus D is surjective F2^E -> F2^F. Therefore every single-face pattern 1_g has a preimage z.

For z choose the link-center map S_z: U_e -> (-1)^{z_e} U_e. Haar measure, each link Laplacian, and the Gauss-invariant subspace are preserved, because the central signs commute with left and right vertex gauge transformations. A face holonomy acquires sign (-1)^(D z)_f. In particular W_g -> -W_g, W_f -> W_f, and all other face Wilson fundamental traces are unchanged. With
H(t)=K_el + sum_{r != g} b_r(1-p_r) + t b_g(1-p_g)
(including b_f=0 for the target),
the exact operator identity is
S_z H(t) S_z^{-1}=H(-t)+2 t b_g.
The target central multiplier O=k_a(W_f) is invariant. Therefore physical normalized Gibbs and vacuum target-cap expectations are even in t.

This directly verifies the combinatorial center-flux premise of FN-2 for finite ordinary disk cellulations, including simultaneous other plaquette couplings. It does not by itself establish evenness for other topologies, frozen boundary link conditions, nonstandard identifications, or target observables not invariant under the face-center pattern. Those require separate verification.

The center-flux involution gives no order between the cap-biased and ordinary integrated-plaquette cosh moments and no sign of their variance difference. The full-coupling cap survival and continuum mass gap remain OPEN.

Proof note: The existence statement uses boundary edges as independent variables and the mod-two face-edge incidence; it must not be applied to a periodic torus, where the sum of all face boundaries is zero mod two.
