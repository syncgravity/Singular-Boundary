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
