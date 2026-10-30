R3 24-MODE PENROSE EXTERIOR SURGERY: VERIFIED FIXED-SUPPORT MATHEMATICAL AUDIT
2026-10-27

Main result: exact rank-24 exterior face-incidence quotient and an exact
noncommutative 59-pivot flat gluing of all 62 retained faces touching the
14-face insertion. Three-color 24-link Haar surgery is action nonincreasing.
The full-net surgery yields an unconditional tail with unwanted +66*lambda;
it DOES NOT prove the requested uniform C^|Q|(1+lambda)^(a|Q|) e^(-c*t)
tail, local energy theorem, R3 insertion theorem, or continuum mass gap.

From this directory:
 python classify_modes.py
 python exact_crossing_rank.py
 python crossing_no_go.py
 python optimize_basis.py
 python relative_words.py
 python word_length_audit.py
 python verify_joint_gluing.py
 python joint_surgery.py
 python theorem_certificate.py

The scripts require installed numpy and sympy. canonical links are labeled
by the direct Z5 acceptance-window Penrose source.

Key outputs:
 FORMAL_NOTE.md: proof with explicit scope
 modes_certificate.json, mode_table.csv: all 24 basis directions and colors
 relative_words_joint.json: exact Tietze pivot group words
 relative_words_joint_optimized.json: 33-crossing basis Tietze words
 joint_gluing_certificate.json: noncommuting SU2 verification
 full_action_surgery_certificate.json: 3-color full-action audit
 exact_crossing_rank.json: exact Q rational rank no-go
 theorem_certificate.json: quantitative Peierls bound with +66lambda
