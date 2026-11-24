#!/usr/bin/env python3
"""Verify third-mark restriction naturality across all graph-5 [1,2] diamonds.

This extends the minimal four-cell audit to every graph-5 differing-pair-set
certificate/map row (64 four-cell cycles and 340 twelve-cell cycles).
"""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter
from pathlib import Path

import verify_pf_i16_four_cell_switch_restriction_naturality as base

def intersect(a, b):
    return {k: set(a[k]) & set(b[k]) for k in ("F", "E", "V")}

def cell_inventory_hash(state):
    obj = {
        "F": sorted(state["F"]),
        "E": sorted([list(e) for e in state["E"]]),
        "V": sorted([list(v) for v in state["V"]])
    }
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--collapse", required=True, type=Path)
    ap.add_argument("--diagrams", required=True, type=Path)
    ap.add_argument("--inventory", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()

    collapse, ch = base.load(args.collapse, base.EXPECTED["collapse"])
    diagrams, dh = base.load(args.diagrams, base.EXPECTED["diagrams"])
    inventory, ih = base.load(args.inventory)
    face_hash = hashlib.sha256(json.dumps(
        inventory["face_key_table"], sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    assert face_hash == base.EXPECTED["inventory_face_table"], (face_hash, base.EXPECTED["inventory_face_table"])

    fv = [base.face_vertices(x) for x in inventory["face_key_table"]]
    fe = [base.face_edges(x) for x in inventory["face_key_table"]]
    lookup = {(pi, wi): w for pi, pair in enumerate(diagrams["per_pair"])
              for wi, w in enumerate(pair["graph5_witnesses"])}

    rows = []
    cycle_counts = Counter()
    restricted_cycle_counts = Counter()
    block_counts = Counter()
    extra_counts = Counter()
    order_counts = Counter()
    prefix_swap_counts = Counter()
    intermediate_counts = Counter()
    full_prefix_exact = full_suffix_exact = 0
    crossing_free = both_replay = full_factorizations = restricted_factorizations = 0
    common_extra_equal = common_prefix_equal = common_intermediate_equal = suffix_replays = 0
    deletion3_success = 0
    witness_ids = set()

    for witness in collapse["families"]["graph5"]["witness_results"]:
        pi, wi = witness["pair_index"], witness["witness_index"]
        support_faces = lookup[(pi, wi)]["support_face_indices"]
        for perm in witness["permutation_results"]:
            pmap = perm["source_to_support_isomorphism"]
            for cert in perm["diamond_certificates"]:
                if cert["same_elementary_pair_set"] or cert["source_mark_pair"] != [1, 2]:
                    continue
                assert pmap[0] == 0 and pmap[3] == 3
                assert witness["single_deletion_certificates"][str(pmap[3])]["success"] is True
                deletion3_success += 1

                full_X = base.union(set().union(*(set(support_faces[i]) for i in range(4))), fv, fe)
                full_keep = [i for i in range(4) if i not in {pmap[1], pmap[2]}]
                full_A = base.union(set().union(*(set(support_faces[i]) for i in full_keep)), fv, fe)
                restricted_labels = [i for i in range(4) if i != pmap[3]]
                X3 = base.union(set().union(*(set(support_faces[i]) for i in restricted_labels)), fv, fe)
                B = base.union(support_faces[pmap[0]], fv, fe)

                L = base.sequence(cert["path_delete_m_then_n"])
                R = base.sequence(cert["path_delete_n_then_m"])
                assert base.replay(L, full_X, full_A, fv, fe) == full_A
                assert base.replay(R, full_X, full_A, fv, fe) == full_A
                dL, dR = set(L)-set(R), set(R)-set(L)
                D = dL | dR
                faces = {p[2] for p in D if p[0] == "FE"}
                edges = {p[1] if p[0] == "FE" else p[2] for p in D}
                vertices = {p[1] for p in D if p[0] == "EV"}
                full_sig = (len(faces), len(edges), len(vertices), len(D))
                assert full_sig in {(1, 2, 1, 4), (2, 6, 4, 12)}
                assert len(dL) == len(dR) and base.one_alternating_cycle(dL, dR)
                cycle_counts[full_sig] += 1

                # Factor the original four-support collapse paths.
                blockL, _, _, prefixL, suffixL = base.dependency_close(L, full_X, full_A, dL, fv, fe)
                blockR, _, _, prefixR, suffixR = base.dependency_close(R, full_X, full_A, dR, fv, fe)
                full_extraL, full_extraR = blockL-dL, blockR-dR
                full_midL = base.replay(prefixL, full_X, full_A, fv, fe)
                full_midR = base.replay(prefixR, full_X, full_A, fv, fe)
                assert full_extraL == full_extraR
                assert set(prefixL) == set(prefixR)
                assert full_midL is not None and full_midL == full_midR
                assert base.replay(suffixL, full_midL, full_A, fv, fe) == full_A
                assert base.replay(suffixR, full_midR, full_A, fv, fe) == full_A
                full_factorizations += 1
                common_extra_equal += 1
                common_prefix_equal += 1
                common_intermediate_equal += 1

                # Restrict the two original paths to supports 0,1,2 (delete mark 3).
                left, crossL = base.restrict_sequence(L, X3)
                right, crossR = base.restrict_sequence(R, X3)
                assert not crossL and not crossR
                crossing_free += 1
                assert base.replay(left, X3, B, fv, fe) == B
                assert base.replay(right, X3, B, fv, fe) == B
                both_replay += 1
                rdL, rdR = set(left)-set(right), set(right)-set(left)
                rD = rdL | rdR
                rfaces = {p[2] for p in rD if p[0] == "FE"}
                redges = {p[1] if p[0] == "FE" else p[2] for p in rD}
                rvertices = {p[1] for p in rD if p[0] == "EV"}
                restricted_sig = (len(rfaces), len(redges), len(rvertices), len(rD))
                assert restricted_sig == full_sig
                assert base.one_alternating_cycle(rdL, rdR)
                restricted_cycle_counts[restricted_sig] += 1

                # Factor the restricted paths independently.
                rblockL, _, _, rprefixL, rsuffixL = base.dependency_close(left, X3, B, rdL, fv, fe)
                rblockR, _, _, rprefixR, rsuffixR = base.dependency_close(right, X3, B, rdR, fv, fe)
                rextraL, rextraR = rblockL-rdL, rblockR-rdR
                rmidL = base.replay(rprefixL, X3, B, fv, fe)
                rmidR = base.replay(rprefixR, X3, B, fv, fe)
                assert rextraL == rextraR
                assert set(rprefixL) == set(rprefixR)
                assert rmidL is not None and rmidL == rmidR
                assert base.replay(rsuffixL, rmidL, B, fv, fe) == B
                assert base.replay(rsuffixR, rmidR, B, fv, fe) == B
                restricted_factorizations += 1
                suffix_replays += 1

                # Exact restriction naturality: restrict the original prefix/suffix
                # components, not just the original full path, and compare sequence-for-sequence.
                rpL, cpL = base.restrict_sequence(prefixL, X3)
                rpR, cpR = base.restrict_sequence(prefixR, X3)
                rsL, csL = base.restrict_sequence(suffixL, X3)
                rsR, csR = base.restrict_sequence(suffixR, X3)
                assert not any((cpL, cpR, csL, csR))
                restricted_mid = intersect(full_midL, X3)
                assert restricted_mid == rmidL == rmidR
                assert base.replay(rpL, X3, restricted_mid, fv, fe) == restricted_mid
                assert base.replay(rpR, X3, restricted_mid, fv, fe) == restricted_mid
                assert base.replay(rsL, restricted_mid, B, fv, fe) == B
                assert base.replay(rsR, restricted_mid, B, fv, fe) == B
                assert rpL == rprefixL and rpR == rprefixR
                assert rsL == rsuffixL and rsR == rsuffixR
                full_prefix_exact += 1
                full_suffix_exact += 1

                swaps, error = base.normalize_prefix(rprefixL, rprefixR, X3, restricted_mid, fv, fe)
                assert error is None and swaps is not None
                prefix_swap_counts[(full_sig, swaps)] += 1

                extra_orderL = [p for p in rsuffixL if p in rextraL]
                extra_orderR = [p for p in rsuffixR if p in rextraR]
                wordL = tuple(p[0] for p in extra_orderL)
                wordR = tuple(p[0] for p in extra_orderR)
                order_counts[(full_sig, len(rblockL), len(rextraL), wordL, wordR, wordL == wordR)] += 1
                block_counts[(full_sig, len(rblockL))] += 1
                extra_counts[(full_sig, len(rextraL))] += 1
                intermediate_counts[(full_sig, len(rmidL["F"]), len(rmidL["E"]), len(rmidL["V"]))] += 1
                witness_ids.add(witness["witness_id"])

                rows.append({
                    "pair_index": pi, "witness_index": wi, "witness_id": witness["witness_id"],
                    "source_mark_pair": [1, 2], "further_deleted_source_mark": 3,
                    "source_to_support_map": pmap, "restricted_support_labels": restricted_labels,
                    "full_alternating_cycle_signature": list(full_sig),
                    "restricted_alternating_cycle_signature": list(restricted_sig),
                    "no_pair_crosses_restriction_boundary": True,
                    "both_restricted_paths_replay_to_root_support": True,
                    "full_factorization_restricts_exactly": True,
                    "same_restricted_prefix_pair_set": True,
                    "same_restricted_intermediate_inventory": True,
                    "same_restricted_dependency_closed_pair_set": True,
                    "restricted_suffix_pair_count": len(rblockL),
                    "restricted_common_extra_pair_count": len(rextraL),
                    "restricted_common_extra_order_equal": wordL == wordR,
                    "restricted_common_extra_left_word": list(wordL),
                    "restricted_common_extra_right_word": list(wordR),
                    "prefix_normalizing_valid_swaps": swaps,
                    "restricted_intermediate_inventory_counts": {
                        "faces": len(rmidL["F"]), "edges": len(rmidL["E"]), "vertices": len(rmidL["V"])
                    }
                })

    assert len(rows) == 404 and len(witness_ids) == 202
    assert cycle_counts == Counter({(1, 2, 1, 4): 64, (2, 6, 4, 12): 340})
    assert restricted_cycle_counts == cycle_counts
    assert deletion3_success == crossing_free == both_replay == 404
    assert full_factorizations == restricted_factorizations == suffix_replays == 404
    assert full_prefix_exact == full_suffix_exact == 404
    assert common_extra_equal == common_prefix_equal == common_intermediate_equal == 404
    assert sum(v for k,v in order_counts.items() if k[0] == (2,6,4,12) and k[-1]) == 0
    assert sum(v for k,v in order_counts.items() if k[0] == (2,6,4,12) and not k[-1]) == 340
    assert block_counts[((2,6,4,12),8)] == 236 and block_counts[((2,6,4,12),11)] == 104
    assert extra_counts[((2,6,4,12),2)] == 236 and extra_counts[((2,6,4,12),5)] == 104

    result = {
        "schema": "PF-I16-GRAPH5-404-THIRD-MARK-RESTRICTION-NATURALITY-v1",
        "inputs": {
            "collapse_payload_sha256": ch, "diagrams_payload_sha256": dh,
            "inventory_payload_sha256": ih, "inventory_face_table_sha256": face_hash
        },
        "scope": "all graph-5 source-mark-[1,2] differing-pair-set certificates under both root-preserving maps, restricted by the third eligible source mark 3",
        "counts": {
            "certificate_map_rows": 404, "distinct_geometric_witnesses": 202,
            "four_cell_alternating_cycles": 64, "twelve_cell_alternating_cycles": 340,
            "third_mark_single_deletion_certificates_success": deletion3_success,
            "no_elementary_pair_crosses_restriction_boundary": crossing_free,
            "both_restricted_paths_replay_to_root_support": both_replay,
            "restricted_alternating_cycle_preserved": 404,
            "full_dependency_closed_factorizations_valid": full_factorizations,
            "restricted_dependency_closed_factorizations_valid": restricted_factorizations,
            "original_factorization_restricts_exactly_to_restricted_factorization_prefix": full_prefix_exact,
            "original_factorization_restricts_exactly_to_restricted_factorization_suffix": full_suffix_exact,
            "common_extra_pair_sets_agree": common_extra_equal,
            "common_prefix_pair_sets_agree": common_prefix_equal,
            "common_intermediate_inventories_agree": common_intermediate_equal,
            "both_restricted_suffixes_replay_to_root_support": suffix_replays,
            "dependency_closed_suffix_pair_counts": [
                {"cycle":list(k[0]),"pairs":k[1],"count":v} for k,v in sorted(block_counts.items())
            ],
            "common_extra_pair_counts": [
                {"cycle":list(k[0]),"pairs":k[1],"count":v} for k,v in sorted(extra_counts.items())
            ],
            "common_extra_order_templates": [
                {"cycle":list(k[0]),"suffix_pairs":k[1],"extra_pairs":k[2],
                 "left_word":list(k[3]),"right_word":list(k[4]),"order_equal":k[5],"count":v}
                for k,v in sorted(order_counts.items())
            ],
            "prefix_normalizing_valid_swap_counts": [
                {"cycle":list(k[0]),"swaps":k[1],"count":v} for k,v in sorted(prefix_swap_counts.items())
            ],
            "restricted_intermediate_inventory_counts": [
                {"cycle":list(k[0]),"faces":k[1],"edges":k[2],"vertices":k[3],"count":v}
                for k,v in sorted(intermediate_counts.items())
            ]
        },
        "conclusions": {
            "third_mark_restriction_preserves_all_404_graph5_collapse_paths": True,
            "dependency_closed_factorization_is_exactly_restriction_natural_on_all_404_rows": True,
            "larger_twelve_cell_cycles_have_two_order_sensitive_dependency_templates": True,
            "general_all_orders_restriction_naturality_proved": False,
            "geometric_L8_closed": False
        },
        "rows": rows
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["counts"], sort_keys=True))

if __name__ == "__main__":
    main()
