# R3-IR-561 — Dissertation-constrained 3D Penrose-prism plaquette-incidence audit (2026-10-31)

## Primary-source check: Sharpe dissertation v10.7

The user-supplied archive `Sharpe_dissertation_v10.7.tar.gz` includes `delivery/dissertation/the_singular_boundary.pdf` (23 pages, draft dated March 8, 2026). Chapter 2 §2.1–2.2 discusses Penrose tiling, five pentagrid families, and the projected geometric construction. Chapter 3 §3.1–3.4 (printed pp. 9–10) describes the C5 decomposition of R5 into physical and perpendicular planes, the extra compact direction `u=Re(z2)`, and explicitly compares the *coupled Z5 Laplacian* with a **separable product** `L_Pen ⊗ I_u + I_Pen ⊗ L_u`. Section 3.4 states that their spectral dimension effects differ. The dissertation **does not define** an extruded quadrilateral Whitney 3D-prism edge mass, SU(2) gauge links, 3D Wilson plaquette incidence, or an action-derived 3+1D Yang–Mills Hamiltonian. Consequently the prismatic construction in R3-IR-560 and below is an **alternative candidate** inspired by the independent Penrose physical-plane geometry; it is not established as the author's original coupled Z5 construction.

## Full candidate prism Wilson cell incidence

On each recovered `Approximant(M)` (M=5,7,9,11,13,15), take the radius-two edge-adjacent face neighborhood of face 0 as before. Denote its face, edge and vertex sets F,E,V. Make two horizontal link layers E_bottom and E_top, and one vertical link for every base vertex V. The elementary *Wilson plaquettes* comprise:

1. One bottom plaquette for each face in F.
2. One top plaquette for each face in F.
3. One vertical rectangle joining the bottom and top copies of every edge in E. For oriented base edge e:u→v its boundary link cycle is e_bottom, vertical(v), reverse(e_top), reverse(vertical(u)).

Thus the number of links is 2|E|+|V| and the number of Wilson plaquettes is 2|F|+|E|. These are elementary 4-link closed cycles; the full 3D oriented chain-complex boundary operator, Gauss law and Yang–Mills action have **not** been validated by this combinatorial enumeration alone.

A rooted spanning tree is constructed with (|V|−1) bottom links, including exactly three of the deleted face's four edges and excluding selected chord e, plus **all** |V| vertical links. It has 2|V|−1 edges and connects the two-layer graph. It uses zero top horizontal edges, so the selected bottom chord stays non-tree; all tree root transporters are independent of that bottom chord.

For the selected bottom chord, the count is **exactly three** incident plaquettes: the deleted bottom f0, one other retained bottom face, and the vertical side rectangle of the chord. After deleting f0, there are **two** retained Wilson couplings involving the chord. The top horizontal f0 does **not** contain the *bottom* chord; it contains its distinct top-layer copy. This explicitly corrects any mistaken four-retained-plaquette count. The protected-link theorem R3-IR-556 requires replacing the single adjacent Wilson forcing b by the total chord-dependent bounded multiplication forcing; a safe crude bound is |b_bottom|+|b_vertical| (assuming each Wilson character has sup norm ≤1). The resulting ratio is rho=8 M_ee(|b_bottom|+|b_vertical|)/(3g2²) under the *same chosen kinetic normalization*, and the full proof still requires all its operator hypotheses.

| M | Base faces | 3D links | Wilson plaquettes | Tree links | Incident target plaquettes | Retained target couplings |
|---:|---:|---:|---:|---:|---:|---:|
|5|14|98|65|47|3|2|
|7|14|95|64|45|3|2|
|9|14|98|65|47|3|2|
|11|14|95|64|45|3|2|
|13|14|95|64|45|3|2|
|15|14|95|64|45|3|2|

These counts were computed from original `penrose_faces` incidences on each approximant, not inferred from a schematic prism. At M5,M7,M11,M13, the selected base chord ID is 1; at M9,M15 it is 0. The retained neighboring horizontal face is f2 or f1, respectively. No attempt is made to equate numeric edge identifiers across approximants.

## Durability and limits

Executed original-code reproducer `construct_prism_plaquettes.py` and complete per-approximant JSON `prism_plaquette_incidence_2026-10-31.json` are in ChatGPT Library `/The Singular Boundary/Source/`. Original dissertation archive is preserved there. This report is text-only Git. The earlier six candidate 3D mass matrices are also in Library. These geometry checks do **not** establish that the product prisms reproduce the dissertation's coupled Z5 Laplacian, nor do they calibrate 3D gauge couplings, prove refinement-uniform sector gaps or the continuum Yang–Mills mass gap.

**Next obligation:** construct the 3D coboundary/Bianchi consistency checks and full Wilson action/canonical Hamiltonian with correct kinetic-magnetic units and gauge-invariant Gauss-law sector, then measure the **two-interaction** protected chord ratio under justified physical scaling. Also investigate a directly coupled Z5-derived 3D complex if the goal is mathematical fidelity to dissertation §3.4 rather than a separable extruded model.
