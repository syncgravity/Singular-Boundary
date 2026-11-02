# R3-IR: One-sided spacetime localization of fourth-order centered bridge (2026-11-02)

**Conditional theorem.** For finite dressed open SU(2) strip, centered residual bond observables f1,...,f4 with ||fi||∞≤v=1/1152, |∇fi|≤G=√21·67/13824, and temporal gaps a,b,d≥0, consider the exact fourth-cumulant middle channel
T(a,b,d)=〈P_a f1, f2 Q P_b Q(f3 P_d f4)〉,
where Q removes stationary means. Assume the archived weighted L² semigroup-gradient inequality rate c=11/120 with weight ρ=6/5, spectral gap κ=23/144, and full-future conditional Poincare inequality.

**If the spatially rightmost residual bond is f1**, let S be the union of supports of f2,f3,f4 and r=d_link(T_>m,S), where m is the index of f1. Then
|T(a,b,d)|≤(v³G/√κ)(5/6)^r e^(−ca)[e^(−cb)(e^(−cd)+e^(−κd))+e^(−κ(b+d))].
By reversibility, the same estimate with time gaps reversed applies if the spatially rightmost bond is f4.

**Proof:** Set F=f3 P_d f4. Its norm is ≤v²e^(−κd), and its weighted gradient norm is ≤vG(e^(−cd)+e^(−κd)). For U=QP_bQF, ||U||₂≤v²e^(−κ(b+d)), and weighted gradient ≤vG e^(−cb)(e^(−cd)+e^(−κd)). For H=Q(f2 U), weighted gradient ≤v²G[e^(−cb)(e^(−cd)+e^(−κd))+e^(−κ(b+d))]. Apply P_a gradient contraction and exact old-prefix centering of f1, together with future conditional Poincare and weighted spatial tail. Q projections are retained; only their gradients vanish.

Time integration over three gaps yields
∫_[0,∞)^3 |T| ≤ (5/6)^r (v³G/√κ)[c^−2(c^−1+κ^−1)+c^−1 κ^−2]
≈8.982166213×10^−8(5/6)^r.

**Strict limitations:** Only temporal orderings with a spatially extremal bond at earliest/latest time are covered. Middle-position extremal bonds remain unresolved. The calculation depends on previously assumed weighted SU(2) Bochner/Poincare results; arithmetic finite-state tests do not prove those assumptions. No complete fourth-order tree clustering, fourth-order extensivity, interacting λ=1 gap, or continuum Yang–Mills mass gap follows.

Complete audit and reproducible checker, log, hashes archived in Library /The Singular Boundary/Proof Audits.