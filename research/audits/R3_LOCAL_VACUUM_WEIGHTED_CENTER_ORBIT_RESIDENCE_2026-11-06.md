# P2/T2 localized interacting-vacuum center-orbit residence audit

Date 2026-11-06. Finite cubic SU(2) theorem candidate, NOT a continuum mass-gap proof. All continuum gates OPEN.

Previous PR #87 merged as ebb6541c049f4dcc4f1f46c1712b171efd0185b8.

Assume the established finite-regulator equivariant center-stable normal coordinates around an unstable center gauge orbit O, with unstable fiber dimension m>=3, initial resident unstable width w_s<=c_hr r exp(-gamma_hr s). For the actual coupled quantum ground state Omega, previous per-link kinetic estimates imply total gradient energy <= 32 |E| / g0(h)^4. Applying the homogeneous m-dimensional Sobolev inequality in the unstable fiber, a smooth cutoff on a radius-O(r) tube, Holder on the small resident fiber, and finite-chart Jacobian comparisons yields:

nu(R_O(s,r)) <= min(1, K_hr exp(-2 gamma_hr s)(1+32 |E| r^2/g0(h)^4)).

This replaces the global density supremum of PR #87 with true interacting-vacuum H1 energy. K_hr, gamma_hr, and r are NOT uniform under refinement.

For a single-negative-link center orbit, gauge-orbit distance <=r implies each one of four negative plaquette holonomies has SU2 distance <=4r to -I. Thus 1+half-trace <=2r^2; the earlier genuine-vacuum cap theorem gives nu(R_O(s,r)) <=min(1,C r^2 (1+32/g0(h)^4)), uniform in box size but with no time-decay term.

Combine the two upper bounds. This does not control later entry to center tubes, physical renormalized curvature, infinite-volume limits, or a Yang-Mills mass gap.

Complete proof report, Python verifier, 5730 passed deterministic geometry/capacity checks, execution log and SHA-256 manifest saved to user's Library: The Singular Boundary/Proof Audits/R3_LOCAL_VACUUM_CENTER_ORBIT_RESIDENCE_2026-11-06.zip. ZIP SHA-256: 385d1c3aa91669d398123dadfa4a1ba8f102bebd9f508ce53071eb075ed50200. Pending independent review.
