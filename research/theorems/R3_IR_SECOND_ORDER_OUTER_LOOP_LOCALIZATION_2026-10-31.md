# Second-order Wilson transport: exact cut-boundary localization and finite-cage sparse response

Date: 2026-10-31. Scope: finite planar original-link SU(2), free-coupling second derivative at lambda=0.

Let Q be the exact second-order log-amplitude coefficient from the preceding Fierz-resolvent calculation. For adjacent retained faces (k,l) sharing e, define C_kl=c_k c_l a_e[3/(4 gamma_kl)+1/(4 beta_kl)] >0, and the union outer-loop trace r_kl in [-1,1]. A tree-cotree transport T preserves each retained p_k. Therefore

Q(TU)-Q(U) = sum_(k,l retained adjacent) C_kl [r_kl(TU)-r_kl(U)].

For a given T and configuration U, let S(U,T) be the original links with T(U)_e unequal to U_e. Let boundary(k union l) denote the exterior oriented boundary link set. If boundary(k union l) intersect S is empty, r_kl(TU)=r_kl(U) exactly. Consequently, with P_S={retained neighboring pairs whose exterior loop intersects S},

Q(TU)-Q(U)=sum_(k,l in P_S) C_kl delta r_kl, and |Q(TU)-Q(U)|<=2 sum_(P_S) C_kl.

This is an exact finite-volume locality result independent of the total number of retained faces, conditional on transport link-change set. It is not a uniform scaling estimate; the upper bound discards signed cancellation. Intersecting loops may still be invariant due to transport holonomy constraints.

On 3x3 cage, 9 faces, central deleted, 24 links, verified BFS/DFS tree-cotree implementations and 80 noncommuting configurations each: BFS changes 2 links, 2 potentially affected neighboring-pair loops, only 1 nonzero delta r per trial. DFS changes 5 links, 5 potentially affected loops, only 3 nonzero delta r per trial. Signed delta Q of both signs. Numerical zero tests do not establish an all-configuration identity for intersecting loops.

The formula and nonzero sample exclude universal second-order cancellation for these particular transports; not for arbitrary transports, higher orders, or physical lambda=1. Neither regulator-uniform signed current nor continuum Yang-Mills mass gap is proved.

Proof and executable numerical verification archived at /The Singular Boundary/Proof Audits/R3_IR_SECOND_ORDER_OUTER_LOOP_LOCALIZATION_2026-10-31.zip.