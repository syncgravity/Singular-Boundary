# PF-I16: canonical source-diamond incidence census

Date: 2026-11-18

Status: **exact finite source-level compatibility verified through eight ports; the all-orders canonical source-diamond lemma remains unproved.**

Verifier: \`research/verification/verify_pf_i16_canonical_source_diamond.py\`.

## 1. Question tested

The target-side guarded mutual-survival theorem proves that two disjoint marks J,K commute when each remains a valid guarded reverse mark after the other inverse. That theorem does not identify the source objects or show that the common twice-reversed target is canonical for their common parent source.

This census tests the missing source-level conditions without replacing them by target-only shorthand.

Let n be the target port count. Let p and q be source objects on n-2 ports. Let J,K be disjoint two-port marks in [n]. Write K_p for K compressed after deleting J, and J_q for J compressed after deleting K. The source-diamond conditions are:

1. K_p is the canonical non-root leaf interval of p.
2. J_q is the canonical non-root leaf interval of q.
3. The exact parent-source projections agree:
   \[
   r=\pi_{K_p}(p)=\pi_{J_q}(q),
   \]
   including matching intervals, overlap-tree edges, and port compression.

For a parent source p and target mark J, the fiber neighborhood is computed exactly as
\[
N(p,J)=\{T:\ J\text{ is a valid guarded reverse mark of }T,\
P_J(T)\in C_{\rm can}(p)\}.
\]
The verifier constructs this set by lifting every canonical parent target through every overlapping old edge and each admissible local switch pattern. It then independently rechecks the full guarded inverse conditions and verifies that reversing J recovers the chosen parent target exactly.

For every common target
\[
T\in N(p,J)\cap N(q,K),
\]
the verifier checks whether K survives the J-inverse and J survives the K-inverse, recomputes both second inverse witnesses, and compares the resulting common target U. Finally it tests
\[
U\in C_{\rm can}(r).
\tag{C3}
\]

## 2. Exact results

| Target ports n | Parent sources p,q | Disjoint mark pairs (J,K) | Exact source diamonds (C2) | Common target incidences | Mutual survivors | C3 passes | C3 failures |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 6 | 2 | 45 | 8 | 37 | 37 | 37 | 0 |
| 8 | 22 | 210 | 274 | 7,884 | 7,884 | 7,884 | 0 |

Support geometry among the mutually surviving common incidences:

| n | (four-port support intersection, |e_J∩K|, |e_K∩J|) | Count |
|---:|---:|---:|
| 6 | (2,1,1) | 37 |
| 8 | (0,0,0) | 535 |
| 8 | (1,0,0) | 4,854 |
| 8 | (2,1,1) | 2,495 |

Thus the source-level C3 condition survives all tested incidences, including disjoint four-port supports and both overlapping-support geometries. The target-side double inverses agree in every mutually surviving case, as required by the general target-side theorem.

The census counts incidences (source diamond, target T), not merely distinct target trees. The same target can occur in more than one source-diamond incidence.

## 3. Verifier construction and independence boundaries

The verifier uses the repository's exact canonical leaf rule and exact source projection \`parent_data\`:

- root the overlap tree at the matching interval containing port 1;
- choose the lexicographically least non-root leaf interval;
- delete that interval and its endpoints;
- compress the remaining port labels in order and delete the leaf vertex.

It constructs canonical parent neighborhoods using the existing \`candidate_outputs(..., forced_last=canonical_leaf(...))\` implementation. The target lift enumerates each old edge that has positive interval overlap with J and all three local switch patterns that do not reinsert the old edge. Every generated target is then passed through the separate guarded inverse checker, which verifies exact induced four-port pattern, full incidence at J, no reinsertion, and positive interval overlap.

The source-pair census independently checks C2 by exact equality of the projected source tuples. It does not infer source identity from a common target.

The target-side inverse checker and source-generation code are existing repository components, so this is an exact cross-check between the forward lift and the guarded inverse, not a wholly independent reimplementation of the entire relation. The new source-pair enumeration, fiber-neighborhood construction, and C2/C3 tests are specific to this audit.

## 4. Verifier corrections retained in the trajectory

Two initial verifier defects were caught before accepting the census:

1. The first lift check passed one-based port labels to the target-only inverse checker, whose API is zero-based. This produced a false “no inverse” assertion. The conversion boundary was made explicit and the recovered parent target was compared after consistent relabeling.
2. The next run compared a \`frozenset\` tree representation against the tuple-of-edges representation returned by \`candidate_outputs\`. This made every C3 comparison falsely fail even though the underlying edge sets agreed. The common parent target is now normalized to the canonical tuple representation before the C3 membership test.

Neither failed run is evidence of a mathematical counterexample. The pinned expected counts apply only to the corrected verifier.

## 5. What is and is not established

Established:

- exact source sibling identity C2 for every counted incidence;
- exact construction and guarded inverse validation of both fiber neighborhoods;
- mutual target-side survival for every common target in the tested census;
- equality of the two target-side double inverses;
- C3 membership of every common double inverse for n=6 and n=8.

Not established:

- an all-orders proof of C2-to-C3;
- that arbitrary families of fibers can be organized into compatible source diamonds;
- a target-capacity or weighted mixed-fiber Hall inequality;
- the all-orders multivalued-pi Hall theorem;
- the weighted one-link inequality unconditionally.

## 6. Next proof obligation

The finite pattern suggests a source-level canonical-diamond lemma:

> If p and q are sibling one-leaf extensions of r, with the inserted leaves K_p and J_q canonical in p and q respectively, and a target T lies in both exact fiber neighborhoods through disjoint marks J,K that mutually survive, then the common double inverse U lies in C_can(r).

The next proof attempt should not extrapolate from the table. It should expose the role of the lexicographic canonical leaf L of r. A useful exact reduction is to test whether L is itself a guarded reverse mark of U and whether its inverse parent target belongs to the full neighborhood of the source obtained by deleting L from r. Those two conditions are equivalent to C3 by the forced-last definition. The proof must derive them from the two sibling histories and the exact ordered-endpoint/no-reinsertion guard, not assume them.

No all-orders Hall theorem or unconditional weighted one-link inequality is claimed.
