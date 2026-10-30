# Word-level Penrose SU(2) link/face incidence certificate — scope audit

Date: 28 October 2026. **Status: a reproducible word-level construction and verification, NOT an identification of the historical 14-face insertion.**

## Source and target

The verified `direct_cut_project.py` was extracted without modification from the supplied `Phase_III_Cut_and_Project_Recomputed.zip`. It generates an actual two-dimensional cut-and-project Penrose rhombus disk (not a 3D icosahedral Penrose complex). Our exact three-periodic-time extrusion uses each spatial rhombus word at slices `t=0,1,2` and each spatial edge `a--b` in slab `t` to form the oriented temporal plaquette

`U_(a,b,t) T_(b,t) U_(a,b,t+1)^(-1) T_(a,t)^(-1)`.

The orientation is fixed by sorting the two endpoints of the source graph's spatial edges. Every word contains four oriented links. The spatial/temporal link IDs and face IDs, together with canonical Z^5 endpoints, are included in each JSON certificate. The word-level construction is deterministic across four nested radius-5, 6.5, 8, 10 cut-and-project disks.

## Exact local staple identities

For a retained face word, cyclically rotate it so its chosen link `e` occurs first. If the link orientation is `+`, the effective quaternion staple is the *inverse* of the remaining cyclic word. If it is `-`, the effective staple is the remaining cyclic word. Denote it by `a_(f,e)` as an SU(2) product. Then the following is an **exact nonabelian identity** for every SU(2) assignment:

`d(W_f)=1- dot(U_e, a_(f,e))`.

For each pair of retained faces `f,g` meeting `e`, the script exports the *reduced noncommutative free-group word* of the pair-staple loop `a_(f,e) a_(g,e)^(-1)`. It does not commute link variables or use a Gaussian approximation. Therefore the exact star-minimum identity

`m_e= [2 sum_(f<g) d(a_(f,e) a_(g,e)^(-1))] / [n_e+|sum_f a_(f,e)|]`

can be evaluated from the exported words. The script also exports all oriented face words, the inserted-face support list, its adjustable-link set, all affected retained faces, and the local star words.

`verify_words.py` independently substitutes Haar-random unit quaternions into every exported pair-loop word and face-trace formula. For the example support it checked 77 pair-staple identities in each radius, with maximal residual at most 4.45e-16. These are numerical checks of the exact symbolically constructed expressions.

## Historical Q14 identification fails, and this is important

The conversation reports **historical** Q14 counts `|H|=36`, `|A(H)|=62`, and `|A_fill|=54` with Bianchi filling, but the original 14 canonical Z^5 endpoint-labelled face list and the corresponding 54-face noncommutative relators are **not present in the currently supplied files**. Counts alone cannot reconstruct the historical support uniquely.

To produce a fully executable word-level audit without fabricating provenance, `certificate.py` uses one explicitly declared **illustrative** support: the seven spatial edges whose midpoints are closest to the origin at radius 5, each inserted as a temporal face in both slabs 0 and 1. On every nested volume, this candidate has:

- `|Q|=14` temporal faces;
- `|H|=35` (not historical 36);
- `|A(H)|=53` (not historical 62);
- a naive single-prism peeling fails (and does **not** prove a 54-face fill or a 44-energy Bianchi bound);
- four of the inserted-support links have no incident retained faces;
- 77 distinct pair-staple loop words for the retained link stars.

These discrepancies prove **only that this illustrative candidate is not a valid reconstruction of the reported historical cavity**. They do not contradict the previously reported results for the historical cavity.

## How to certify the actual historical cavity

Place the exact historical list of 14 face labels into a JSON file in the format of `example_Q_labels.json`. Then run:

`python certificate.py --canonical-Q historical_Q_labels.json`

Follow with:

`python verify_words.py`

The exporter checks that all 14 canonical labels exist in every one of the four nested Penrose patches, emits the four radius-specific certificates, and recomputes all local star and pair-loop words. The verification tests recalculate the retained-star and affected-face incidence in every volume.

**The current script's Bianchi parser only attempts a simple prism shelling.** If the historical Q is not peelable with this scheme, that failure is not proof that it is not Bianchi-fillable: a more general conjugated face-group-word elimination or Tietze proof will be needed. In particular, the script does **not** claim that a signed cellular boundary identity is already a nonabelian based group-word identity.

## Spectral-radius implication and open problem

The raw word-level certificate supplies the necessary inputs for searching for exact inequalities of the form `m_(e(p)) <= sum_r B_(p,r) d(W_r)`. It **does not** construct such pointwise inequalities or certify `rho(B)<1`. Any proposed contraction matrix must be accompanied by its group-word inequalities and an exterior leakage audit. The thermal-excess Ward bound remains valid, but unconditional ambient-volume-uniform Gibbs suppression of the historical 54-face frustration is open.

## Files

`certificate.py`: parametric generator and exporter; `verify_words.py`: quaternion/checksum verifier; `direct_cut_project.py`: extracted source geometry; `example_Q_labels.json`: illustrative input format; `manifest.json`: four-volume SHA-256s; `certificate_radius_*.json`: words and incidence; `verification.json`: observed numerical identity errors.
