# Explicit rhombus-prism incidence and nonlinear crossing-action audit (2026-10-27)

## Scope and data provenance
We constructed a **single abstract extruded quadrilateral** with eight vertices, twelve links, six faces and one cell. This is the local combinatorial type of a Penrose rhombus prism, **not** an extracted, certified whole Penrose 3D complex. `verify.py` reproduces all incidence calculations and `prism_incidence.npz` contains d1,d2,d3 as signed integer arrays.

The provided `penrose_complete_catalogue.npz` has keys `idx`, `sign`, `length`, `roots`, `distance`, `target`, `faces`, `cidx`, `csign`, `clength`, `ckind`, `F`, `graph_hash`, `threshold`, `coverage_version`; its 22,808 indexed cycles are not an explicit full 2D cell incidence system, nor does it store the signed 3D prism 3-cell boundaries. The supplied stage26 zip contains simulation arrays but not an independently certified 3D face-cell incidence map. Therefore the whole-Penrose extension is not verified.

## Integer cellular verification
The constructed matrices satisfy d1 (8x12), d2 (12x6), d3 (6x1), d1*d2=0, d2*d3=0. Ranks of d1 and d2 are 7 and 5. Each face contains four edges and the single 3-cell boundary comprises its six oriented faces (d3 all +1 in the chosen orientation). This establishes the chain property in one model cell.

## Exact nonlinear Bianchi constraints
For actual SU(2) links on an oriented prism cell, the six based face holonomies obey a conjugated ordered product identity equal to the identity. This implies for any face p, theta(W_p) <= sum_{f!=p} theta(W_f) using bi-invariant geodesic distance and transports to a common basepoint. Since d(W)=1-cos(theta) and 2 theta^2/pi^2<=d(W)<=theta^2/2, 

    d(W_p) <= (5*pi^2/4) * sum_{f!=p} d(W_f).

If five faces are flat, the sixth is necessarily flat. Repairing one face while keeping all five other face holonomies fixed is not possible unless its original holonomy was already forced to the desired value. In particular, link deformations cannot violate Bianchi; residual curvature must propagate into another face.

## General exact crossing-action bound
For any actual-link transport T with geodesic link displacement a_e(U)=dist(U_e,(TU)_e), set A_f=sum_{e in boundary f}a_e. By multiplication Lipschitzness, theta(W_f(TU))<=theta(W_f(U))+A_f. Using |sqrt(d(g))-sqrt(d(h))|<=dist(g,h)/sqrt(2),

    S_0(TU)-S_0(U) <= sum_{f retained, touched} beta_f [sqrt(2d_f(U))*A_f + A_f^2/2].

This is exact, nonlinear, local in the touched-face set, and includes spatial and temporal crossings. Bounded incidence proves the number of touched faces is O(number of modified links), but gives no cutoff-uniform O(k log lambda) bound when order-one displacements occur. In that case the bound can be O(lambda*k); suppression or cancellation requires a genuine Gibbs estimate.

## Controlled subclass and no-go
If T leaves all retained face holonomies unchanged (an invariant fiber), then S_0(TU)-S_0(U)=0 pointwise even with order-one displacements. But when Q consists of one face of a prism and its other five face holonomies are retained and preserved, Bianchi forces W_Q to remain fixed up to conjugation. Thus the one-face interior cannot generally be repaired on a crossing-free invariant fiber.

For a serial chain of independently adjustable holonomy increments g_i satisfying prod g_i=h, a geodesic assignment g_i=exp(log h/n) gives the exact restricted energy <= beta_max theta(h)^2/(2n). This extends into a prism complex only after verifying that each increment can be realized by links without extra retained-face energy. The signed incidence identities alone do not certify that lifting.

## Final audit
**Proved:** local 3D integer prism incidence and Bianchi compatibility; exact local nonlinear crossing-action estimate; no independent one-face repair while all other five faces fixed; zero-action on true invariant fibers; serial geodesic construction under separate realization conditions.
**Unproved:** full Penrose 3D incidence verification, a support-local low-action extension for arbitrary Q, nonlinear Gibbs concentration making crossing-action O(|Q| log lambda), arbitrary-support insertion free energy, R3/R2, Yang-Mills mass gap.
