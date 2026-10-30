# R3-IR-453 — Auditable bottleneck computation and stage-26 source limitation

2026-10-30. Algorithmic consequence of R3-IR-452, and direct inspection of the user-supplied stage-26 archives. No Penrose numerical R_star is asserted.

Let the planar disk dual graph have a vertex for each bounded face plus one exterior vertex. For each original link e record its incident bounded face(s), and its integer distance d(e,S0) from the deleted target cage in the chosen original-link metric. Let w(e*)=d(e,S0) be the weight of the corresponding dual edge. The conditional center symmetry bottleneck of R3-IR-452 is

R_star=min_(dual paths P:f to exterior) max_(e* in P) w(e*).

For an integer threshold R, retain only dual edges with weights <=R. Then f is connected to the exterior if and only if R>=R_star. Hence R_star equals the smallest threshold at which union-find connects target and exterior, obtained by sorting dual edges by nondecreasing weight. Equivalently, a minimax Dijkstra recursion computes R_star with candidate distance max(current,w(e*)) and takes minima over paths. The minimizing route is an explicit certificate Dz=1_f, and an edge-cut in the sublevel graph at R_star-1 certifies its minimality.

SOURCE AUDIT. Inspected supplied penrose_seed101_stage26.zip and penrose_seed101_stage26_full.zip. The sample outer_00010080.npz contains sweep/chain_seed/offset, direct_timeslice, direct_product, conditional, conditional_onepoint, pair_counts, timing, and source/catalogue hashes, but no primal link endpoints, face-edge incidence, target-face index, boundary flags, or explicit link-distance matrix. The latest.json records simulation metadata and catalogue_sha256, but the catalogue content is not embedded in either inspected archive. The supplied dissertation .tar.gz lists PDF deliverables rather than a machine-readable mesh catalogue. Therefore the available artifacts do not determine R_star for this stage; a numeric claim would be fabricated. Other stage archives may share this format; they are not asserted to have been individually exhaustively examined here.

To obtain stage-specific R_star, provide: (1) original link table with unique ID and endpoints, (2) each face's ordered edge IDs and target face ID, (3) identification of boundary links, and (4) a specified link-distance convention. Those inputs suffice to reproduce the above algorithm and the explicit dual path/blocked-threshold certificate. The table alone does not establish any physical Wilson cap mixing estimate.

The dual-geometric bottleneck remains exact; no numerical Penrose threshold, regulator-uniform cap survival, infrared spectral estimate or continuum Yang-Mills mass gap has been proved.
