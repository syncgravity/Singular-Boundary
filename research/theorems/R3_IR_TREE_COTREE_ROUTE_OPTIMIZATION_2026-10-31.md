# R3-IR — Optimal dual-root path lengths for planar SU(2) tree–cotree transports

Date 2026-10-31. Exact graph theorem; full Wilson metric estimate OPEN.

Let D be the planar cellulation dual graph, rooted at the exterior face *. For any dual spanning tree T, its route length ℓ_T(f) from * to f obeys ℓ_T(f)≥d_D(*,f). A breadth-first dual spanning tree achieves equality **simultaneously for all faces** and hence minimizes any coordinatewise nondecreasing function of the dual path lengths, including total and maximum length. For nonnegative weighted dual edges, a shortest-path tree gives the weighted analogue. Its primal-edge complement is a primal spanning tree by planar tree–cotree duality.

For the *separate exact rooted SU(2) chain transport model* with equal electric weights and n unchanged-link factors, the maximum positive normalized metric distortion is D_chain(n)=2n+2sqrt(n²+n), increasing in n. BFS therefore minimizes this **chain-model proxy** when dual depth is used as n. **There is no proof that the complete original-link Jacobian of the actual planar tree–cotree transport has this distortion, or that path-length minimization minimizes its metric defect.** Unchanged primal tree links can introduce cross terms, and their dependence must be computed.

Deterministic verification for 3×4, 6×5, 13×11, 20×20 rectangular disks: BFS depths equal independently computed shortest distances at every face. For 20×20, mean dual depth BFS=3.85 versus DFS=200.5, maximum BFS=10 versus DFS=400. The proxy is not a physical Wilson-vacuum observable.

Full proof and executable networkx checker/results/checksums: Library /The Singular Boundary/Proof Audits/R3_IR_TREE_COTREE_ROUTE_OPTIMIZATION_2026-10-31.zip.

Remaining: compute full Lie-coordinate Jacobians for two primal/dual tree choices on the same completed interior face; bound signed metric defect on physical Wilson ground state; prove uniform signed current, covariance and continuum Yang–Mills gap.