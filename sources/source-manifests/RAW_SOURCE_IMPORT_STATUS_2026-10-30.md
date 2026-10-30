# Raw source import audit — October 30, 2026

**Scope:** The non-LFS source-only handoff `OCT11_30_ALL_ARCHIVES_GIT_READY.zip` contains 1,281 distinct UTF-8 source files. Its exact source paths and content SHA-256 are specified in `SOURCE_MANIFEST.json` inside that handoff; the handoff archive SHA-256 is `aa8a3b9c955e739578b1783e676f65e7be704925a86340099d2412cb218fde03`.

**Committed to this exact raw-source namespace and checked:** 10 files under `sources/historical/raw/`. Original Git blob SHAs checked against the ZIP contents after restoring the trailing newline in `haar_sampler.py`:
- `Archive_4/Phase_III_Cut_and_Project_Recomputed.zip/__nested__/Phase_III_CutProject_Recomputation/haar_sampler.py` — `de45afc4f815b8c1bfb74f7cd3fd124b5545e675`
- `Archive/R3_penrose_peierls_shell_2026_10_27_bundle.zip/__nested__/R3_penrose_peierls_shell_2026_10_27/analytic_constants.py` — `50c8be5304ea4688dd0478fa13a33e51db5ec815`
- `Archive_2/R3_incidence_forensic_2026_10_28.zip/__nested__/R3_incidence_forensic_2026_10_28/test_audit.py` — `c5af9d65dfa8a049262d31d0e66970d64323adba`
- `Archive_3/r3_gibbs_smallball_audit_2026-10-28.zip/__nested__/r3_gibbs_smallball_audit_2026-10-28/check.py` — `6e3c38db083f3087e7457585e27f7a0233c85ec2`
- `Archive_4/Phase_III_Cut_and_Project_Recomputed.zip/__nested__/Phase_III_CutProject_Recomputation/run_segments.py` — `9a1e7fca79dbe5849b1f4b9d37ad3cc1e1e86dcc`
- `Archive_4/Stage18_Scalar_12000_Initial_Audit.zip/__nested__/stage18_audit/compare.py` — `dc7c0fecab8fe953683a028e3216f9bbc896319a`
- `Archive/verify (4).py` — `8e56a2628c506d723e2f82784607d86d98294b97`
- `Archive_4/Penrose_YM_Stage26_Outer_First_Connected_Scalar_Campaign.zip/__nested__/stage26_outer/stage24_inner/deps_stage23/deps/stage19_complete/test_stage19_mc.py` — `1c14bb74dac1cd64c3af82d18991f5b41b8d266c`
- `Archive_4/Penrose_YM_Stage26_Outer_First_Connected_Scalar_Campaign.zip/__nested__/stage26_outer/stage24_inner/deps_stage23/deps/stage19_complete/stage19/test_target_first.py` — `71d0f5ae144082da7dced006b2d1f2c7fc4b0ce1`
- `Archive_2/R3_joint_thermal_mgf_2026_10_27_bundle.zip/__nested__/R3_joint_thermal_mgf_2026_10_27/verify_mgf.py` — `2d82929dbc56ed1896bfee1be559c40dc05d034f`

**Still outstanding in this exact namespace:** 1,271 source-only handoff entries. Some historical standalone notes are separately committed under `sources/historical/2026-10-26/` and must not be double-counted as members of the raw namespace.

**Transfer blocker:** authenticated GitHub connector accepts source text in its request but cannot directly access bytes from the local ZIP in the model's container, and the container cannot resolve `github.com` for network Git. Batch size is not the primary obstacle; transferring the actual bytes without retyping/reconstructing files is. The remaining files are not pushed. Historical research continuity requires that future import uses exact archive bytes, verifies content hashes, and never substitutes handwritten approximations for original sources.

This ledger records repository actions and limitations; it does not imply the program's mathematical proof obligations have been resolved.
