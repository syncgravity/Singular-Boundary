# R3-IR-452 — Exact exterior-radius threshold for target center symmetry

2026-10-30. Graph-theoretic consequence of R3-IR-451, for arbitrary finite planar disk original-link cellulations. No Penrose-specific numerical depth is asserted.

Let f be the deleted target face, S0 its original boundary links, and d(e,S0) a fixed integer graph distance from links to S0. In the exterior-martingale construction R3-IR-447, condition on Y_r={e:d(e,S0)>=r}. Let P range over dual paths from f to the exterior vertex and define the bottleneck radius
R_star=min_P max_(e dual to an edge in P) d(e,S0).
The finite graph contains at least one such path.

THEOREM. A target-only link-center-flip symmetry preserving the full Hamiltonian and fixing all conditioned links Y_r exists if and only if r>R_star. Proof: R3-IR-451 says such a symmetry exists precisely when an f-to-exterior dual path avoids Y_r. Avoiding Y_r means every selected original link has distance <r. This is equivalent to max distance along some path <r, or R_star<r.

Consequently, for every center-odd target function O_odd, if r>R_star then E_mu[O_odd|Y_r]=0 exactly. For r<=R_star, none of the target-flipping ORIGINAL-LINK CENTER TRANSFORMATIONS considered in R3-IR-451 fixes Y_r. This does not prove the conditional expectation nonzero, since other cancellations may exist.

If every boundary link has distance at least d_boundary from S0, then R_star>=d_boundary. Hence for radii r<=d_boundary the simple center-flux symmetry cannot eliminate conditional half-spin contributions. This is a graph-geometric obstruction, independent of magnetic and electric coefficients.

The theorem is exact for each finite planar disk. For a particular Penrose stage, evaluating R_star requires its actual link adjacency and dual-face incidence; no numerical R_star or uniform refinement scaling is asserted without that computation. When r>R_star, only the center-odd conditional component is forced to zero; the center-even cap component can retain exterior influence.

No distance-decay estimate for the center-even influence, regulator-uniform cap survival, infrared spectral gap, or continuum Yang-Mills mass gap follows.
