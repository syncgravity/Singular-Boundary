# PF-I16 four-cell alternating-cycle switch and restriction naturality

Date: 2026-11-20 UTC  
Branch: `research/pf-i16-four-interval-diamond-2026-11-19`  
Status: **conditional local switch lemma proved under an explicit regular-CW disk-neighborhood hypothesis; identification of every finite four-cell certificate with that neighborhood and extension to larger cycles remain open.**

## 1. Objective and fixed finite evidence

The source-labelled four-support audit records 5,012 successful two-path collapse diamonds. Of these, 3,224 use the same elementary free-pair set (the two orders differ only by disjoint-pair swaps), while 1,788 have different free-pair sets. The separate CI-backed alternating-cycle audit classifies every one of those 1,788 symmetric differences as one connected alternating cycle.

The smallest signature occurs in 64 graph-5 tests and has four cycle cells: one face, two edges, and one vertex. The finite census is taken from the source-labelled audit and the collapse/alternating-cycle CI artifacts; this note does not rerun those enumerations.

## 2. Minimal four-cell incidence pattern

Write the four cycle cells as
- a 2-cell (F);
- two distinct 1-cells (e_1,e_2);
- a 0-cell (v).

The two path matchings are
[
M_{12}={(F,e_1),(e_2,v)},qquad
M_{21}={(F,e_2),(e_1,v)}.
]
The alternating incidence cycle is
[
F-e_1-v-e_2-F.
]

For the local switch lemma, impose the following **explicit geometric hypothesis**: the closure of (F) is a regular closed 2-disk whose boundary is the two-edge CW circle (e_1cup e_2), with endpoints (v,w), and (w) is retained in the common target subcomplex (A). No other cell of the ambient complex meets the interior of this disk; attachments to the rest of the complex occur only through the retained boundary data. The two recorded pairings must be genuine free pairs in the stated order.

This is a hypothesis to be checked against each geometric certificate, not something implied merely by the abstract four-cycle graph.

## 3. Local switch lemma: equality of endpoint retractions

**Lemma.** Under the preceding regular-CW disk-neighborhood hypothesis, the two collapse orders
[
(F,e_1) 	ext{then} (e_2,v),
qquad
(F,e_2) 	ext{then} (e_1,v)
]
induce the same endpoint retraction on the local disk: both send the disk to the retained endpoint (w). If the rest of the ambient complex is fixed pointwise by both collapse sequences, their composite endpoint retractions (r_{12},r_{21}:X	o A) agree pointwise:
[
oxed{r_{12}=r_{21}.}
]

**Proof.** The first elementary collapse in either order removes the open 2-cell and one of its boundary 1-cells. The remaining boundary 1-cell is then paired with (v) and removed. In either order the only cell of the local closed disk left in the target is (w). Since the target of the restricted endpoint map is the singleton ({w}), both endpoint maps on the disk are the unique constant map to (w). By hypothesis the two collapse sequences act identically (as the identity) outside the local disk. They therefore agree on all of (X). (square)

The conclusion is stronger than the general relative-homotopy uniqueness lemma: in this minimal local model, the endpoint maps are equal, so the constant homotopy is already relative to every subcomplex of (A).

## 4. Restriction naturality for the minimal switch

Let (A'subseteq A) be any further retained subcomplex. If the local disk and its retained endpoint (w) survive the restriction, the same argument gives equality of the restricted endpoint maps. If the restriction removes the local disk together with the source data that generated the switch, both restricted maps are the identity on the remaining complex. Thus, **for restrictions that preserve the stated disk-neighborhood decomposition and its retained endpoint**, the switch is strictly natural: no choice of homotopy is needed.

This is not yet the unrestricted L7b/L8 naturality statement. A source restriction may alter the local incidence neighborhood, change which boundary cells are retained, or fail to preserve the two free-pair sequences. Those cases require separate verification; the abstract alternating-cycle signature alone does not decide them.

## 5. What the finite census now says

The exact smallest cycle signature is:
| Family | Cycle cells | Faces | Edges | Vertices | Tests |
|---|---:|---:|---:|---:|---:|
| Graph 5 | 4 | 1 | 2 | 1 | 64 |

The remaining signatures are larger:
| Family | Cycle cells | Faces | Edges | Vertices | Tests |
|---|---:|---:|---:|---:|---:|
| Graph 5 | 12 | 2 | 6 | 4 | 340 |
| Graph 12 | 6 | 2 | 3 | 1 | 624 |
| Graph 12 | 8 | 1 | 4 | 3 | 136 |
| Graph 12 | 8 | 2 | 4 | 2 | 624 |

The 64 four-cell tests are therefore the first target for certificate-level validation of the disk-neighborhood hypothesis. No claim is made here that all 64 already satisfy it: the currently summarized artifact gives the typed cycle census, not a separate proof that every four-cycle has the required regular-CW boundary attachments and common retained endpoint.

## 6. Relationship to the general relative-homotopy lemma

For any fixed finite diamond whose two paths are strong deformation retractions onto the same grandparent subcomplex (A), the previously recorded lemma gives (r_{12}simeq_A r_{21}). That conclusion is conditional on the regular-CW interpretation of the audited elementary collapses. The present four-cell result is a more rigid special case: if the disk-neighborhood hypothesis holds, the endpoint maps are equal, not merely homotopic.

The two arguments must not be conflated:
- general relative-homotopy uniqueness applies to all audited diamonds subject to the regular-CW interpretation;
- strict endpoint-map equality applies only to the specified minimal disk switch;
- neither by itself supplies a source-prescribed orientation-preserving boundary-cycle map for arbitrary supports.

## 7. Next proof obligations

1. Extract the actual cell labels and attaching maps for the 64 graph-5 four-cell cases from the existing collapse artifact; verify the disk-neighborhood hypothesis and the identity of the retained endpoint (w). Do not regenerate the 5,012-case census.
2. Record whether the 64 cases satisfy strict endpoint-map equality, merely relative homotopy, or neither under the certified CW realization.
3. Analyze the six-cell signature (two faces, three edges, one vertex) for a decomposition into four-cell switches. The decomposition must preserve valid free-pair order at each intermediate stage and be compatible with every retained-support restriction.
4. Only then treat the eight- and twelve-cell cycles.
5. Keep the vertex/cell-level oriented boundary-cycle comparison maps, arbitrary connected-support L7b, geometric L8, and the all-orders mixed Hall inequality as open.

## 8. Evidence boundary

- 5,012 two-path tests, 3,224 same-pair-set cases, and 1,788 differing-pair-set cases: CI-verified in workflow 44833369833.
- Single connected alternating cycle for all 1,788 differing cases and the typed signature census: CI-verified in workflow 44846395728; artifact 14687160404.
- Relative-homotopy uniqueness for two strong deformation retractions onto the same subcomplex: proved in the companion audit; its application to the finite certificates is conditional on the regular-CW realization.
- Four-cell strict endpoint-map equality: proved here **under the explicit local disk-neighborhood hypothesis**; not yet verified for all 64 finite cases.
- Geometric L8, all-orders Hall, physical continuum reconstruction and the Yang–Mills mass gap: OPEN.

## 9. Artifact-level correction: the finite four-cell pattern is a rhombus-corner switch, not the two-edge disk model

The preceding two-edge-disk lemma is mathematically valid under its stated extra hypothesis, but inspection of the actual collapse certificate shows that the hypothesis must **not** be inferred from the four-cycle signature. The concrete finite four-cell example below has two distinct residual endpoints.

Inputs inspected:
- collapse-diamond artifact 14680929981 from workflow 44833369833;
- independent diagram-lifting artifact 14681735833 from the same workflow;
- this is an artifact-level local extraction, not a replay of all 5,012 tests.

A graph-5 example is:
- witness ID: b0290fe5f0ab7536d3d0;
- witness index 3, pair index 22;
- source critical mark pair [1,2];
- permutation index 0, diamond certificate index 0;
- differing face cell F=825.

The symmetric-difference pairs are exactly
\[
(F,e_1),\ (e_2,v)\quad\text{versus}\quad(F,e_2),\ (e_1,v),
\]
where
\[
\begin{aligned}
v&=(-6,-3,5,6,-1),\\
w_1&=(-6,-2,5,6,-1),\\
w_2&=(-6,-3,5,7,-1),\\
e_1&=[v,w_1],\qquad e_2=[v,w_2].
\end{aligned}
\]
The two edges share v, but w_1≠w_2. The face is a rhombus with complementary boundary arc through
\[
z=(-6,-2,5,7,-1),\qquad P=[w_1,z]\cup[z,w_2].
\]
Thus the local boundary is the four-edge rhombus v-w_1-z-w_2-v, not a two-edge CW circle. The two collapse orders need not have the same endpoint map: one removes e_1 and then collapses e_2 against v, while the other removes e_2 and then collapses e_1 against v. The residual endpoints differ.

### Correct local target

The appropriate local candidate is a **rhombus-corner switch**. If the complementary two-edge arc P is retained during the local comparison, both collapse orders are strong deformation retractions of the rhombus onto P. Relative-homotopy uniqueness then gives a homotopy relative to P, but not pointwise equality of endpoint maps.

If a common subsequent collapse q:P→A takes P to the final grandparent A, composing the local homotopy with q gives a homotopy relative to A, provided q fixes A pointwise. This is a local factorization criterion, not yet a certificate-level theorem: the exported collapse artifact records the final target cell digest, not the complete final target cell inventory needed to verify that P is retained or that a common suffix q exists in the required form.

### Revised conclusion and next test

- The two-edge-disk strict-equality lemma remains a valid abstract special case but is **not the geometry of the inspected Penrose four-cell certificate**.
- The actual minimal geometric pattern is a rhombus-corner switch with distinct residual endpoints w_1,w_2.
- Relative homotopy is available from the general uniqueness lemma when both full paths are regular-CW strong deformation retractions onto the same grandparent A. The local rhombus picture identifies a possible witness for that homotopy; it does not supply restriction naturality.
- The next proof task is to extract, for all 64 graph-5 four-cell cases, the complementary arc P, the actual common grandparent cell inventory A, and the common collapse suffix (if any). Then test every further retained-support restriction for preservation of the relative pair (P,A). Do not count the two-edge-disk argument as a solution to these cases.

This correction supersedes any reading of Sections 2–4 as identifying the actual finite four-cell certificates with the two-edge disk model.