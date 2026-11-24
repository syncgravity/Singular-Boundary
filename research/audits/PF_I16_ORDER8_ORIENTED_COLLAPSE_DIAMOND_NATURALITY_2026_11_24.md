# PF-I16 order-eight oriented boundaries and collapse-diamond naturality

Date: 2026-11-24 UTC  
Branch: `research/pf-i16-four-interval-diamond-2026-11-19`  
Status: **finite local verifier passes on the current immutable order-eight artifacts; clean GitHub Actions replay is pending.** The result covers the graph-5 and graph-12 four-support candidate families, not all 490 order-eight source diamonds and not geometric L8.

## 1. Purpose

The previous source-labelled audit retained all 15 labelled intersections for each four-support witness, relative-deletion booleans, anchored footprint words, and the source parent deletion diamonds. The present audit strengthens that record in two ways:

1. Reconstruct each oriented boundary cycle directly from the accepted rhombus faces, anchored at the directed matched edge, rather than trusting the stored boundary-cycle field.
2. Construct explicit elementary relative-collapse sequences along both orders of each source critical pair, compare their pair sets, and factor every differing-pair case into a common prefix and dependency-closed local suffixes.

The source-side deletion theorem and the target-side geometric comparison remain distinct. In particular, the order-eight source exporter provides interval endpoints and overlap trees, but no source-prescribed ℤ^5 displacement or oriented boundary word.

## 2. Pinned inputs

- Independent four-support diagram JSON SHA-256: `aa2d4ae88b3d23e34007eed45858a54b7d98bfd9fa6c595b11635d04a74817ba`.
- Accepted-face inventory face-key-table SHA-256: `c20b727809eeb173ec11f584c2d60fc7afa3283e39a2dc3ccde0187703ce9ec9`.
- Source audit schema: `PF-I16-SOURCE-LABELLED-FOUR-SUPPORT-RESTRICTION-AUDIT-v1`.
- Source order: (n=8), with 608 canonical source records.

The verifier imports the repository's canonical order-eight source exporter and geometric cell/collapse primitives. It independently reconstructs the boundary cycles, intersection contents, and elementary collapse paths.

## 3. Exact oriented-boundary reconstruction

For each of the 996 retained four-support witnesses, the verifier:

- Builds the support complex from its accepted rhombus face indices.
- Counts face incidences of each edge and extracts the one-face boundary.
- Checks that the boundary is a single 2-regular cycle.
- Starts the cycle at the directed matched edge, lower endpoint to upper endpoint.
- Compares the complete vertex sequence and open complementary arc with the stored certificate.
- Independently reconstructs each neighboring support's boundary footprint and its position in the oriented open arc.
- Rechecks every footprint-meeting relation.

Results:

| Check | Count |
|---|---:|
| Four-support witnesses | 996 |
| Independently reconstructed anchored oriented cycles | 3,984 / 3,984 |
| Open complementary arcs | 3,984 / 3,984 |
| Ordered multi-footprint words | 3,984 / 3,984 |
| Labelled intersection entries recomputed, including empty entries | 14,940 / 14,940 |
| Relative single-support deletion-collapse checks | 3,984 / 3,984 |

The boundary-footprint word census over the 3,984 support boundaries is:

| Number of footprints | Support boundaries |
|---:|---:|
| 1 | 514 |
| 2 | 1,478 |
| 3 | 1,992 |

Thus the finite order-eight candidate family has genuine multi-footprint data, not just one distinguished footprint per boundary.

## 4. Source-side order-eight deletion diamonds

The canonical source exporter generates 608 order-eight records and 490 pairs of simultaneous eligible non-root leaf deletions. The verifier independently composes endpoint compression in both orders and compares the final parent intervals, parent tree, and original-to-final port map.

All 490 / 490 source-side diamonds commute.

The current geometric four-support inventory represents only two overlap-graph families:

- Graph 5: 12 source records and 20 source critical pairs.
- Graph 12: 48 source records and 24 source critical pairs.

Therefore 44 of the 490 source diamonds are represented by the present four-support geometry; the other 446 belong to other order-eight overlap-graph families and remain without a geometric lift in this audit.

Across the 996 witnesses, the 60 represented source records, and both root-preserving graph maps, the verifier checks:

| Check | Count |
|---|---:|
| Source/witness/map rows | 58,608 |
| Parent port-order restriction checks | 98,192 |
| Source-diamond geometric lift instances | 43,696 |
| Distinct source critical pairs represented geometrically | 44 |

Both root-preserving graph maps remain admissible. This audit does not select a unique source-to-target labeling.

## 5. Elementary relative-collapse paths

For each represented source critical pair, the verifier constructs both paths:
[
U_4 searrow U_3^{(-m)} searrow U_2^{(-m,-n)},qquad
U_4 searrow U_3^{(-n)} searrow U_2^{(-m,-n)}.
]

Each elementary pair is checked at the moment it is applied:
- an FE pair removes a free edge and its unique incident face, neither in the retained target;
- an EV pair removes a free vertex and its unique incident edge, with no remaining incident face.

Both paths replay to the same retained two-support complex in all 43,696 source-map diamond instances.

The collapse-path comparison gives:

| Comparison | Instances |
|---|---:|
| Same elementary-pair set | 25,472 |
| Same pair set, normalized by valid adjacent collapse commutations | 25,472 |
| Different elementary-pair sets | 18,224 |
| Different pair sets forming one connected alternating cycle | 18,224 |

The alternating-cycle sizes are:

| Alternating-cycle cells | Instances |
|---:|---:|
| 4 | 256 |
| 6 | 7,488 |
| 8 | 9,120 |
| 12 | 1,360 |

The source-graph split is informative:

| Source graph family | Same pair set | Different pair set | Alternating-cycle types |
|---|---:|---:|---|
| Graph 5 | 18,944 | 1,616 | 256 four-cell; 1,360 twelve-cell |
| Graph 12 | 6,528 | 16,608 | 7,488 six-cell; 9,120 eight-cell |

No differing-pair case in this finite family decomposes into multiple alternating components.

## 6. Dependency-closed local switch factorization

For each of the 18,224 differing-pair instances, the verifier starts with the alternating-difference pairs and closes the local block under failed adjacent commutations. It then checks:

- The two paths have the same prefix pair set.
- The prefixes reach the same intermediate cell inventory.
- The common prefixes normalize to the same ordered sequence by valid adjacent collapse commutations.
- The two dependency-closed suffixes have the same additional-pair set.
- Both suffixes replay from the common intermediate complex to the same retained two-support target.

All 18,224 instances pass these checks.

Dependency-closed suffix sizes:

| Suffix pairs | Instances |
|---:|---:|
| 4 | 1,696 |
| 5 | 8,064 |
| 6 | 32 |
| 7 | 1,680 |
| 8 | 3,824 |
| 10 | 1,360 |
| 11 | 1,568 |

Common additional-pair counts:

| Additional pairs | Instances |
|---:|---:|
| 0 | 1,632 |
| 1 | 2,160 |
| 2 | 6,912 |
| 4 | 4,496 |
| 5 | 512 |
| 6 | 1,296 |
| 7 | 1,152 |
| 8 | 64 |

The order of common additional pairs agrees in 12,800 instances and is order-sensitive in 5,424. The latter are not failed replays: both local suffixes remain valid and have the same additional-pair set. They identify larger local switch templates that cannot be reduced to adjacent swaps alone.

## 7. Interpretation

This advances the geometric L8 program in three concrete ways:

1. It independently authenticates the complete oriented boundary cycles and multi-footprint words for all 996 current four-support candidates.
2. It upgrades the 44 represented source critical pairs from relative-collapse booleans to explicit two-order elementary collapse paths.
3. It shows that every differing-pair collapse diamond in this represented family has a single alternating-cycle discrepancy and a valid dependency-closed common-prefix/local-suffix factorization.

It does **not** close geometric L8. In particular:

- 446 of the 490 order-eight source diamonds belong to other overlap-graph families and are not geometrically lifted here.
- Both root-preserving graph maps remain possible.
- The source does not prescribe a unique ℤ^5 edge displacement or oriented boundary word.
- A finite factorization of collapse sequences is not yet a natural homotopy or equality of collapse maps.
- No all-orders local switch lemma, all-orders accepted-face confluence theorem, or all-orders PF-I16 Hall inequality follows.

## 8. Reproduction

Verifier:

`research/scripts/verify_pf_i16_order8_oriented_collapse_diamond_naturality.py`

The CI step consumes the generated order-eight diagram JSON, accepted-face inventory, and source-labelled restriction audit. It emits row-level witness/pair path digests and the complete finite census above. The current branch workflow is the clean-checkout reproducibility gate; its conclusion is pending at the time of this record.
