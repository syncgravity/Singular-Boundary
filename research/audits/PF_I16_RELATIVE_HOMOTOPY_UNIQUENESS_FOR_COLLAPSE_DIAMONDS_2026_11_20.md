# PF-I16: relative-homotopy uniqueness for finite collapse diamonds

Date: 2026-11-20  
Branch: `research/pf-i16-four-interval-diamond-2026-11-19`  
Status: **general relative-homotopy lemma proved; its application to the recorded finite diamonds is conditional on the recorded elementary-collapse certificates being interpreted in their standard regular-CW realization. This does not establish naturality or geometric L8.**

## 1. Why this addendum is needed

The four-support audit records 5,012 two-path relative-collapse tests. In every test, both paths begin with the same full four-support union and end at the same grandparent support union. There are 3,224 tests with the same elementary free-pair set, related by disjoint-pair swaps, and 1,788 tests with different pair sets. The latter were correctly left unresolved as *combinatorial pair-sequence comparisons*.

There is, however, a separate topological question: must the two resulting retraction maps be homotopic relative to the common grandparent subcomplex? This question has a general answer and does not require the alternating-cycle classification.

The finite certificate provenance is:
- collapse certificates and their input-hash reconciliation: workflow [44833369833](https://github.com/syncgravity/Singular-Boundary/actions/runs/44833369833);
- alternating-cycle classification: workflow [44846395728](https://github.com/syncgravity/Singular-Boundary/actions/runs/44846395728);
- collapse artifact: `14680929981`;
- alternating-cycle artifact: `14687160404`.

This addendum reuses those recorded results. It does not rerun or independently re-enumerate the 5,012 tests.

## 2. Relative-homotopy uniqueness lemma

Let (Asubseteq X) be a subcomplex, and let
[
i:A\hookrightarrow X
]
be inclusion. Suppose (r_0,r_1:X\to A) are strong deformation retractions fixing (A) pointwise. Then
[
oxed{r_0\simeq_A r_1.}
]

Here (\simeq_A) denotes homotopy through maps (X\to A) that fix every point of (A) throughout.

### Proof

Because (r_1) is a strong deformation retraction, there is a homotopy
[
H:X\times[0,1]\to X
]
such that
[
H(x,0)=x,\qquad H(x,1)=i(r_1(x)),
\qquad H(a,t)=aquad(a\in A).
]
Define
[
K(x,t)=r_0(H(x,t)).
]
Then
[
K(x,0)=r_0(x),
]
and, since (r_0\circ i=\operatorname{id}_A),
[
K(x,1)=r_0(i(r_1(x)))=r_1(x).
]
For (a\in A), (K(a,t)=r_0(a)=a). Thus (K) is a homotopy from (r_0) to (r_1) relative to (A). \(\square\)

The result is elementary but important: strict equality of collapse maps, equality of elementary pair sets, and homotopy of the resulting retractions are different assertions.

## 3. Application to the recorded four-support diamonds

For a fixed four-support witness and a fixed pair of source deletions, let:
- (X) be the full cell complex of the four-support union;
- (A) be the cell complex of the common grandparent support union;
- (r_{mn}:X\to A) be the composite collapse map from deleting (m) and then (n);
- (r_{nm}:X\to A) be the composite collapse map from deleting (n) and then (m).

The verifier constructs both paths from the same (X) to the same (A). Its elementary pairs are:
1. a free edge paired with its unique remaining incident face; or
2. a free vertex paired with its unique remaining incident edge, with no remaining incident face.

For a regular CW realization of the accepted rhombus complex, each such pair is an elementary collapse and hence gives a strong deformation retraction. Compositions of these elementary retractions are again strong deformation retractions. The lemma therefore gives
[
oxed{r_{mn}\simeq_A r_{nm}.}
]

Consequently, **conditional on the regular-CW realization of the audited incidence complex**, all 5,012 recorded two-path diamonds have relative-homotopic retraction maps, including the 1,788 cases whose deterministic elementary pair sets differ.

The 1,788 cases are not thereby converted into disjoint-swap equivalences. Their pair-set differences remain the alternating cycles classified by the separate verifier.

## 4. What this closes—and what it does not

This supplies a homotopy-existence result at the level of the two retractions for each fixed finite diamond, subject to the regular-CW realization stated above.

It does **not** establish:
- a combinatorial sequence of valid elementary-pair exchanges between the two recorded pairings;
- a canonical, local, or support-natural choice of the homotopy;
- compatibility of these homotopies with every further source restriction or third support deletion;
- equality or natural isomorphism of the oriented boundary-cycle comparison maps;
- a source-prescribed map from the abstract interval labels to the geometric matched edges;
- arbitrary connected-support L7b or geometric L8;
- the all-orders multivalued-π Hall inequality.

In particular, a homotopy relative to one grandparent (A) need not restrict to a homotopy relative to every smaller retained subcomplex (A'\subset A). That restriction/naturality issue is precisely why this lemma does not close L8.

## 5. Revised next proof task

The alternating-cycle classification remains useful, but its role is now sharper.

1. Start with the four-cell and six-cell cycle signatures.
2. For each, identify the smallest ambient regular-CW neighborhood and the two actual collapse matchings.
3. Determine whether the matching flip can be realized by a sequence of valid local elementary-collapse exchanges, or whether only the general relative homotopy is available.
4. Test the proposed local homotopy against every further retained-support restriction. The required square must commute up to a homotopy fixed on the smaller grandparent, not merely on the current (A).
5. Only after this naturality check should the eight- and twelve-cell signatures be tested for decomposition into smaller switches.

The immediate deliverable is therefore a **restriction-natural collapse homotopy lemma**, not another enumeration of the 5,012 finite diamonds.

## 6. Proof boundary

- Finite collapse-path success and common grandparent targets: CI-verified in workflow 44833369833.
- Finite alternating-cycle classification: CI-verified in workflow 44846395728.
- Relative-homotopy uniqueness of two strong deformation retractions onto the same subcomplex: proved above.
- Application to all 5,012 certificates: conditional on the standard regular-CW interpretation of the audited free-pair collapses.
- Restriction-natural homotopy, source-prescribed geometric correspondence, L7b, and geometric L8: open.
- All-orders Hall and the physical Yang–Mills continuum mass-gap gates: open.
