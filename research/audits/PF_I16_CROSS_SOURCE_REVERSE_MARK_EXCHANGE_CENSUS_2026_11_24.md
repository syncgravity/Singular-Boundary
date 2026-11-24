# PF-I16 cross-source reverse-mark S/D incidence census

Date: 2026-11-24 UTC  
Branch: `research/pf-i16-parent-fiber-exchange-2026-11-23`  
Verifier commit: `acb786edd723042dd907b81fc6a03b82afbf4750`  
Workflow: [45362601045](https://github.com/syncgravity/Singular-Boundary/actions/runs/45362601045), conclusion **SUCCESS**  
Artifact: [14904533373](https://github.com/syncgravity/Singular-Boundary/actions/runs/45362601045/artifacts/14904533373)  
Artifact ZIP SHA-256: `e2356712d0563322651120339e35d8704a62ff169f7e7289a8be0fa9421d98aa`  
Decoded JSON SHA-256: `85c3c0551918b8e7562ebd900feda00230cf7f6ffb8efe4a3631079ccf614f56`

**Status:** exact finite cross-source S/D incidence census at (n=6,8). It exposes a large residual class of non-diamond collisions not connected by the current certified exchange graph. It is not a capacity allocation, PFEL proof, or Hall counterexample.

## 1. Question and preserved structure

The preceding projection-shifting census established source-preserving D–S–D transitions for a fixed child source (x), with the ordinary common-parent target (Uin C(r)) certified at both endpoints. The next obligation was to extend sibling-lift (S)-moves across distinct child sources in the same fixed ((p,J,P)) block, without quotienting away source identity or the split demand (1/d(x)).

A state is retained as
[
(x,J,P,T),qquad p=pi_J(x),quad P=P_J(T)in C_{\rm can}(p).
]
Here (x) is the complete child matching/overlap-tree source, (J) its eligible non-root leaf, (P) the exact compressed parent target, and (T) the child target.

The verifier constructs each block
[
B(p,J,P)={(x,J,P,T):pi_J(x)=p, P_J(T)=P}.
]
For a fixed block it independently verifies that every child source in (X(p,J)) has exactly the same set (L_J(P)) of child targets. This is the fixed-fiber Cartesian-product check.

### S-edges

Within a fixed ((p,J,P)) block, an S-edge joins incidence states when the child target changes. The audit counts both:
- same-source target-changing S-edges;
- cross-source target-changing S-edges, with (x
e x') and (T
e T').

The complete block data retain the child-source indices and the full (L_J(P)) target list, so the edge counts are reconstructible without materializing every pairwise edge.

### D-edges

A D-edge joins two states ((x,J,P,T)) and ((x,K,Q,T)) only when:
- the same source (x) has both eligible non-root leaves;
- both exact guarded inverses are valid;
- both opposite-order inverses survive;
- the two double inverses agree;
- the common double inverse (U) belongs to the **ordinary** common-parent neighborhood (C(r)).

The verifier does not require (Uin C_{\rm can}(r)). Every D-edge stores the source matching/tree, (J,K,T,P,Q), and the ordinary (U).

The S-connected blocks are contracted to block vertices; certified D-edges then define the finite S/D component graph. Cross-source collisions at a common target are classified according to whether their block endpoints lie in the same or different components of this graph.

## 2. Exact results

| Quantity | (n=6) | (n=8) |
|---|---:|---:|
| Child sources | 22 | 608 |
| Parent-leaf fibers ((p,J)) | 18 | 440 |
| Source-mark incidences | 30 | 1,050 |
| Parent-target blocks ((p,J,P)) | 45 | 3,980 |
| Full ((x,J,P,T)) incidence states | 278 | 48,879 |
| Distinct child targets | 43 | 1,493 |
| Blocks with multiple child sources | 30 | 3,358 |
| Maximum child sources in one block | 2 | 3 |
| Maximum lifts in one block | 6 | 9 |
| Same-source S-edges | 445 | 117,558 |
| Cross-source target-changing S-edges | 410 | 211,106 |
| Cross-source same-target state pairs | 119 | 41,963 |
| Certified D-diamond witnesses | 37 | 11,086 |
| D-diamond rejections | 0 | 0 |
| Non-diamond cross-source target-collision pairs | 842 | 1,161,021 |
| Such pairs connected by an S/D path | 66 | 174,828 |
| Such pairs in distinct S/D components | 776 | 986,193 |
| S/D block components | 17 | 341 |

All fixed-((p,J,P)) blocks pass the cross-source Cartesian-row check. Every D-edge has a valid ordinary common-parent witness. No D-edge was rejected after the retained common-target incidences were formed.

The component block-size histograms are:
- (n=6): ({1:9,3:2,4:2,5:2,6:2});
- (n=8): ({1:206,3:8,4:11,5:18,6:18,7:6,8:3,9:1,10:6,11:6,12:2,14:1,15:1,18:1,20:1,21:3,22:1,24:1,27:2,29:1,30:1,33:1,36:1,39:2,40:2,43:1,46:3,47:1,48:1,51:2,53:2,55:1,57:1,60:1,61:1,62:1,63:2,68:2,69:2,75:1,76:1,77:1,79:1,80:1,81:1,84:1,94:1,99:1,102:1,111:1,117:1,120:1,129:2,135:1}).

## 3. Explicit non-diamond obstruction to universal S/D connectivity

The first disconnected non-diamond collision at (n=6) is:

- Common child target:
  [
  T={(1,2),(2,3),(3,4),(4,5),(4,6)}.
  ]
- Left child source:
  [
  x_L=({(1,3),(2,5),(4,6)},{(0,1),(1,2)}),
  quad J_L=(4,6).
  ]
- Right child source:
  [
  x_R=({(1,3),(2,6),(4,5)},{(0,1),(1,2)}),
  quad J_R=(4,5).
  ]
- Both have the same parent source
  [
  p=({(1,3),(2,4)},{(0,1)})
  ]
  and the same parent target
  [
  P={(1,2),(2,3),(3,4)}.
  ]

These are distinct child sources with different deleted marks, sharing the same target and even the same ((p,P)). They are not a D-edge because D requires one common source witness with two eligible marks. The two corresponding block vertices lie in different S/D components.

The first disconnected (n=8) collision has:
- common target the path ({(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8)});
- left source intervals ((1,3),(2,5),(4,7),(6,8)), with (J_L=(6,8));
- right source intervals ((1,3),(2,5),(4,8),(6,7)), with (J_R=(6,7));
- common parent source intervals ((1,3),(2,5),(4,6)), overlap tree ((0,1),(1,2));
- common parent target the path on six ports.

Again, the sources are distinct and the deleted marks differ, while the parent source and parent target agree. The collision endpoints lie in different S/D components.

These are concrete witnesses to the non-diamond class. They do not form a Hall-deficient fiber family: no demand/capacity min-cut is computed by this audit.

## 4. What the result rules out

The proposed strong connectivity shortcut is false in the tested finite orders:

> Every shared-target collision between distinct source witnesses can be resolved by a path of fixed-((p,J,P)) sibling-lift moves and same-source deletion-diamond moves.

At (n=6), 776 of 842 non-diamond collision pairs remain in different components. At (n=8), 986,193 of 1,161,021 remain in different components.

Thus the present two-colour S/D complex is not by itself a universal exchange graph for all target collisions. The issue persists even when the two source witnesses share the same parent source and the same parent target: the deleted marks and child sources are different, so no source-certified D-edge is available.

This does **not** rule out:
- a fractional allocation across these disconnected components;
- a separate capacity-surplus estimate for non-diamond collisions;
- longer exchange primitives not generated by the current S/D edges;
- the split-demand quotient Hall inequality or source-level Hall.

## 5. Capacity interpretation and nonclaims

The fiber demand
[
delta(p,J)=sum_{xin X(p,J)}rac1{d(x)}
]
is exported exactly as a rational. Each fiber record lists its child-source indices and all parent-target blocks (Pin C_{\rm can}(p)). Each block lists its source indices and complete child lift set (L_J(P)).

The quantity obtained by summing (1/d(x)) over the sources in every ((p,J,P)) block is **duplicated across the different parent targets (P)**. It is only a pre-allocation diagnostic and must not be summed as conserved demand. A valid transport must still choose how each fiber's single (delta(p,J)) is distributed among its parent-target blocks and then among child targets, with total target load at most one.

The audit does not:
- construct such a transport;
- prove the weighted dual (\mathrm{MR}_k);
- prove PFEL, quotient Hall, all-orders multivalued-(pi) Hall, or the weighted one-link inequality;
- assign a helical phase or (mathbb Z^5) label to any reverse mark.

## 6. Reproduction and custody

Verifier: `research/verification/verify_pf_i16_cross_source_reverse_mark_exchange.py`  
Workflow: `.github/workflows/pf-i16-cross-source-reverse-mark-exchange.yml`  
Verifier blob SHA: `b1c35de9b3c7e133cb255c5aea109800721bf85d`  
Workflow blob SHA: `ab6dc9518864d8194fd38ae1d8761187795a5110`  
Successful run: [45362601045](https://github.com/syncgravity/Singular-Boundary/actions/runs/45362601045)

The artifact contains full fiber/source/parent-target/child-target records, all certified D-edge witnesses with ordinary common-parent targets, component summaries, and the first connected and disconnected non-diamond collision witnesses.

**Next proof obligation:** classify the disconnected non-diamond collision blocks and determine whether their source demands admit a separate capacity allocation or whether a genuinely new exchange primitive is required. Do not infer a Hall obstruction from disconnectedness.


## 7. Parent-sibling C-incidence refinement

A second exact pass asks whether a restricted class of non-diamond collisions can be connected without inventing a common child source.

Define a **C-incidence** between two distinct blocks
\[
B(p,J,P),\qquad B(p,K,P),\qquad J\ne K,
\]
when distinct child sources \(x\ne x'\) extend the same parent source \(p\) by the different deleted marks \(J,K\), and both incidences contain the same child target \(T\) with the same parent target \(P\). This retains both source witnesses. It is not a source deletion diamond, and it is not yet a target-changing capacity move.

The verifier adds these C-incidences to the existing S/D block graph and recomputes connectivity. The C relation is deliberately narrow: it requires the same parent source and the same parent target, not merely a shared child target.

<text></text>

| Quantity | \(n=6\) | \(n=8\) |
|---|---:|---:|
| Distinct C block-pair/target witnesses | 82 | 5,786 |
| Distinct child-source-pair witnesses | 242 | 36,142 |
| S/C/D block components | 1 | 30 |
| Largest S/C/D component | 45 blocks | 3,916 blocks |
| Non-diamond pairs connected after C | 842 | 1,156,140 |
| Non-diamond pairs still in distinct components | 0 | 4,881 |

At \(n=6\), the C-augmented graph is connected across all 45 blocks. At \(n=8\), it has one 3,916-block component, 27 components of size two, and two components of size five.

### Collision classification at \(n=8\)

The table distinguishes whether two colliding source incidences have the same parent source \(p\), the same parent target \(P\), and the same deleted interval \(J\). The last column is the number still disconnected after adding C.

| Same \(p\)? | Same \(P\)? | Same \(J\)? | Total pairs | Connected after C | Disconnected after C |
|---|---|---|---:|---:|---:|
| No | No | No | 572,501 | 569,993 | 2,508 |
| No | Yes | No | 193,500 | 192,400 | 1,100 |
| No | Yes | Yes | 329,900 | 328,707 | 1,193 |
| Yes | No | No | 28,978 | 28,898 | 80 |
| Yes | Yes | No | 36,142 | 36,142 | 0 |
| **Total** | | | **1,161,021** | **1,156,140** | **4,881** |

Thus the C relation resolves every collision in the same-parent/same-parent-target/different-mark class. It does not resolve collisions whose parent sources differ, or whose parent targets differ.

### First residual collision after S/C/D

A concrete \(n=8\) residual pair is:

\[
T=\{(1,2),(2,3),(3,4),(3,5),(3,6),(6,7),(6,8)\}.
\]

Left source:
- matching intervals \((1,4),(2,5),(3,7),(6,8)\);
- overlap tree \((0,2),(1,2),(2,3)\);
- deleted mark \(J=(2,5)\);
- parent source intervals \((1,3),(2,5),(4,6)\), parent tree \((0,1),(1,2)\);
- parent target \(P=\{(1,2),(2,3),(2,4),(4,5),(4,6)\}\).

Right source:
- matching intervals \((1,4),(2,7),(3,5),(6,8)\);
- overlap tree \((0,1),(0,2),(1,3)\);
- deleted mark \(K=(6,8)\);
- parent source intervals \((1,4),(2,6),(3,5)\), parent tree \((0,1),(0,2)\);
- parent target \(Q=\{(1,2),(2,3),(3,4),(3,5),(3,6)\}\).

The two incidences share \(T\), but \(p\ne q\) and \(P\ne Q\). They therefore have neither a D witness (no common child source), nor a C witness (no common parent source and parent target). Their block vertices remain in different S/C/D components.

This gives a concrete next structural boundary: the residual collisions require a transition that changes parent source and/or parent target, or a separate capacity estimate. It does not show a Hall deficiency.

## 8. Interpretation and next proof obligation

The finite progression is now:

1. Sibling-lift S moves within fixed \((p,J,P)\) blocks.
2. Same-source D moves witnessed by a guarded deletion diamond and ordinary common-parent target \(U\in C(r)\).
3. Cross-source C incidences between different one-leaf extensions of the same parent source, at the same parent target and child target.

This three-relation complex connects every non-diamond collision at \(n=6\), and all but 4,881 at \(n=8\). The residual class is concentrated at changes of parent source or parent target.

The next finite test should be **recursive parent projection of the 4,881 residual \(n=8\) collisions**: map each endpoint \((p,P)\) to its canonical-leaf parent incidence at order six, find shortest S/C/D paths in the order-six graph, and then test whether each such path has an actual source-preserving lift back to order eight. The parent-level path alone is not enough; every lifted step must retain the exact child source, mark, guarded inverse, and ordinary common-parent witness.

No all-orders parent-fiber exchange lemma follows from connectivity at \(n=6\) or \(n=8\). PFEL, quotient Hall, all-orders multivalued-\(\pi\) Hall, and the weighted one-link inequality remain open.

## 9. Follow-up reproduction record

The C-incidence refinement is included in verifier commit \`c6bf2c83396cad395df3b403e8795df5840b691e\` and passed in workflow [45363512929](https://github.com/syncgravity/Singular-Boundary/actions/runs/45363512929), conclusion **SUCCESS**.

Artifact: [14905217719](https://github.com/syncgravity/Singular-Boundary/actions/runs/45363512929/artifacts/14905217719)  
Artifact ZIP SHA-256: \`a36f61cf8c1e5f0c3e321767f95b774a1cdf54cd13e365703eae99ecd674a421\`  
Decoded JSON SHA-256: \`285991694ddd38ef7d75baf9d10301652d99317b112b69e3d211e7b532bbf8f1\`  
Verifier blob SHA: \`be4876be9f1c0de7d5fa766fec7c4b3c9f578fc7\`  
Workflow blob SHA: \`ab6dc9518864d8194fd38ae1d8761187795a5110\`
