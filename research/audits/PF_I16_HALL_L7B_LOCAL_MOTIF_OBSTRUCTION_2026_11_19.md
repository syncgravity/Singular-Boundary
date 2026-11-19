# PF-I16 — Local motif obstruction to the frozen L4–L5–L7b lift

Date: 19 November 2026  
Branch: `research/pf-i16-z5-incidence-lift-2026-11-18`  
Verifier: `research/scripts/verify_pf_i16_hall_l7b_local_motif_obstruction.py`  
Target domains: PF-I16 original-source accepted complex and PF-I11 completed-window core, both at Ngrid=7.

## 1. Result

For the explicit three-interval star source
\[
M=\{[1,6],[2,3],[4,5]\},\qquad
\tau=\{(I_1,I_2),(I_1,I_3)\},
\]
there is **no** face-supported interval-support triple satisfying L4, L5, and the adopted L7b open-complementary-arc condition when the frozen matched-edge assignment is
\[
\begin{aligned}
e_1 &: (0,1,0,0,0)\to(0,1,0,0,1),\\
e_2 &: (0,1,0,1,0)\to(0,1,0,1,1),\\
e_3 &: (0,1,1,0,0)\to(0,1,1,1,0).
\end{aligned}
\]
This obstruction is independent of the number of rhombi in the supports. It replaces the need for a bounded support-size or bounded root-size separator argument for this particular frozen motif.

It is **not** an obstruction to every possible incidence lift, not a Hall counterexample, and not an all-orders result.

## 2. Exact target incidence

Write
\[
m=(0,1,0,0,0),\quad
m_2=(0,1,0,1,0),\quad
m_3=(0,1,1,0,-1),\quad
v_*=(0,1,1,1,0).
\]
A rhombus key \((m;j,k)\) means the four vertices
\[
m,\quad m+e_j,\quad m+e_j+e_k,\quad m+e_k.
\]

In each target domain, the exact accepted-face incidence sets are:

| Matched edge | Its two incident accepted rhombi |
|---|---|
| \(e_1\) | \((m;0,4), (m;3,4)\) |
| \(e_2\) | \((m;3,4), (m_2;2,4)\) |
| \(e_3\) | \((m;2,3), (m_3;3,4)\) |

The decisive vertex incidences are:
- The face \(F_{20}=(m;3,4)\) contains both endpoints of \(e_1\) and both endpoints of \(e_2\).
- The other \(e_2\)-incident face \(F_{2*}=(m_2;2,4)\) contains \(v_*\).
- Both \(e_3\)-incident faces contain \(v_*\), and in particular \(v_*\) is the upper endpoint of \(e_3\).

The verifier rebuilds the two Ngrid=7 complexes and checks these exact incidence sets, rather than merely checking the displayed face labels against a hand-entered list. Population controls are PF-I16 \((V,E,F)=(1550,3017,1468)\) and PF-I11 \((1432,2761,1330)\).

## 3. Local impossibility proof

Let \(S_i\) be the face-supported interval support assigned to \(I_i\).

1. By L4, the distinguished matched edge \(e_i\) lies on the boundary of \(S_i\). Each of the three edges has exactly two incident accepted rhombi in the target. Therefore exactly one of the two listed incident rhombi belongs to the corresponding support; including both would make the matched edge an interior edge, not a boundary edge.

2. Consider the two possibilities for \(S_2\).

   **Case A: \(F_{20}\subset S_2\).** Since \(F_{20}\) contains both endpoints of \(e_1\), and \(e_1\subset S_1\), the intersection \(S_1\cap S_2\) contains both endpoints of the root's distinguished edge. But L7b requires this overlap footprint to lie strictly inside the open complementary boundary arc of \(S_1\), excluding both endpoints of \(e_1\). Contradiction.

   **Case B: \(F_{2*}\subset S_2\).** Then \(v_*\in S_2\). Since \(v_*\) is an endpoint of the distinguished edge \(e_3\), it also belongs to \(S_3\). Thus \(S_2\cap S_3\) contains \(v_*\), contradicting L5: \(I_2\) and \(I_3\) are non-overlapping leaves and their supports must be disjoint, including at vertices.

Both possible choices for the unique \(e_2\)-incident face lead to contradiction. Hence no support triple exists under these conditions, regardless of support size.

## 4. What this establishes—and what it does not

**Established:** the frozen three-edge motif cannot realize L4 + L5 + the adopted L7b open-arc requirement for this star source in either Ngrid=7 target domain. The argument is a finite-target incidence theorem with an unrestricted support-size conclusion.

**Not established:**
- impossibility for a different choice of matched edges or a different target motif;
- impossibility for every alternative L1–L3 incidence lift;
- impossibility for larger or different PF target domains;
- failure of Hall's theorem or of the all-orders multivalued-parent Hall inequality.

The earlier bounded-root relative face-separator census remains a finite diagnostic. It should not be promoted to an unrestricted separator theorem. The local two-case incidence argument above is the support-size-independent proof for the frozen motif.

## 5. Reproducibility

Run from a clean checkout with the existing PF-I16 scripts on the same branch:

```bash
python research/scripts/verify_pf_i16_hall_l7b_local_motif_obstruction.py
```

The verifier imports the existing L1–L3 target builder and L4–L5 face-key normalizer, rebuilds both target domains, checks exact incidence around \(e_1,e_2,e_3\), checks the decisive vertex inclusions, and asserts that the completed-window core's faces are contained in the original-source replay.

This record reports the committed verifier and its specified checks. It does not claim that the verifier was executed from a clean checkout in this session.
