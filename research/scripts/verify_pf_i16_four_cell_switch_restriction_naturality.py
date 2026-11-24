#!/usr/bin/env python3
"""Finite restriction-naturality audit for the PF-I16 four-cell switch.

The test restricts each of the 64 graph-5 source-mark-[1,2] collapse diamonds
to the three-support subcomplex obtained by deleting the third eligible mark
3. Every retained pair must lie wholly in the restricted subcomplex; both
restricted paths must replay to the root support and preserve the common-prefix
/ dependency-closed-switch factorization. This is a finite artifact verifier,
not an all-orders naturality theorem.
"""
from __future__ import annotations
import argparse, gzip, hashlib, itertools, json, zipfile
from collections import Counter, defaultdict
from pathlib import Path

EXPECTED = {
    "collapse": "d0d96755ceaa556759f6d5a2d0f60d0df1cd5f9805b12e5461c6d1747f6f8141",
    "diagrams": "aa2d4ae88b3d23e34007eed45858a54b7d98bfd9fa6c595b11635d04a74817ba",
    "inventory_face_table": "c20b727809eeb173ec11f584c2d60fc7afa3283e39a2dc3ccde0187703ce9ec9",
}

def load(path: Path, expected: str | None = None):
    raw = path.read_bytes()
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            assert len(names) == 1, names
            raw = z.read(names[0])
    if path.suffix == ".gz" or raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    digest = hashlib.sha256(raw).hexdigest()
    if expected is not None:
        assert digest == expected, (str(path), digest, expected)
    return json.loads(raw), digest

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def edge(a, b):
    return tuple(sorted((tuple(a), tuple(b))))

def face_vertices(row):
    m = tuple(row["lower"])
    j, k = row["directions"]
    ej = tuple(int(i == j) for i in range(5))
    ek = tuple(int(i == k) for i in range(5))
    return {m, add(m, ej), add(add(m, ej), ek), add(m, ek)}

def face_edges(row):
    v = sorted(face_vertices(row))
    return {edge(a, b) for a, b in itertools.combinations(v, 2)
            if sum(abs(x-y) for x, y in zip(a, b)) == 1}

def union(ids, fv, fe):
    F = set(ids)
    return {"F": F, "E": set().union(*(fe[i] for i in F)),
            "V": set().union(*(fv[i] for i in F))}

def sequence(path):
    out = []
    for stage in ("first_relative_collapse", "second_relative_collapse"):
        for x in path[stage]["face_edge_pairs"]:
            out.append(("FE", edge(*x["free_edge"]), int(x["removed_face"])))
        for x in path[stage]["edge_vertex_pairs"]:
            out.append(("EV", tuple(x["free_vertex"]), edge(*x["removed_edge"])))
    return out

def apply(state, pair, target, fv, fe):
    F, E, V = set(state["F"]), set(state["E"]), set(state["V"])
    if pair[0] == "FE":
        _, e, f = pair
        incident = {q for q in F if e in fe[q]}
        if e not in E or f not in F or e in target["E"] or f in target["F"] or incident != {f}:
            return None
        F.remove(f); E.remove(e)
    else:
        _, v, e = pair
        incident_edges = {q for q in E if v in q}
        incident_faces = {q for q in F if v in fv[q]}
        if v not in V or e not in E or v in target["V"] or e in target["E"] or incident_edges != {e} or incident_faces:
            return None
        E.remove(e); V.remove(v)
    return {"F": F, "E": E, "V": V}

def replay(pairs, start, target, fv, fe):
    state = {k: set(v) for k, v in start.items()}
    for pair in pairs:
        state = apply(state, pair, target, fv, fe)
        if state is None:
            return None
    return state

def pair_cells(pair):
    if pair[0] == "FE":
        return (("E", pair[1]), ("F", pair[2]))
    return (("V", pair[1]), ("E", pair[2]))

def restrict_sequence(pairs, subcomplex):
    kept, crossing = [], []
    for pair in pairs:
        cells = pair_cells(pair)
        present = []
        for kind, value in cells:
            present.append(value in subcomplex[{"F":"F", "E":"E", "V":"V"}[kind]])
        if all(present):
            kept.append(pair)
        elif any(present):
            crossing.append(pair)
    return kept, crossing

def dependency_close(pairs, start, target, initial, fv, fe):
    ordered = list(pairs)
    block = set(initial)
    swaps = 0
    absorbed = []
    while True:
        changed = False
        for j in range(len(ordered)-1):
            if ordered[j] in block and ordered[j+1] not in block:
                a, b = ordered[j], ordered[j+1]
                state = replay(ordered[:j], start, target, fv, fe)
                assert state is not None
                ab1 = apply(state, a, target, fv, fe)
                ab = apply(ab1, b, target, fv, fe) if ab1 is not None else None
                ba1 = apply(state, b, target, fv, fe)
                ba = apply(ba1, a, target, fv, fe) if ba1 is not None else None
                if ab is not None and ba is not None and ab == ba:
                    ordered[j], ordered[j+1] = b, a
                    swaps += 1
                else:
                    block.add(b)
                    absorbed.append(b)
                changed = True
                break
        if not changed:
            break
    assert replay(ordered, start, target, fv, fe) == target
    prefix = [p for p in ordered if p not in block]
    suffix = [p for p in ordered if p in block]
    assert ordered == prefix + suffix
    return block, swaps, absorbed, prefix, suffix

def normalize_prefix(left, right, start, intermediate, fv, fe):
    left, right = list(left), list(right)
    if set(left) != set(right):
        return None, ("prefix-pair-set-mismatch",)
    swaps = 0
    for i, want in enumerate(right):
        j = left.index(want, i)
        while j > i:
            a, b = left[j-1], left[j]
            state = replay(left[:j-1], start, intermediate, fv, fe)
            assert state is not None
            ab1 = apply(state, a, intermediate, fv, fe)
            ab = apply(ab1, b, intermediate, fv, fe) if ab1 is not None else None
            ba1 = apply(state, b, intermediate, fv, fe)
            ba = apply(ba1, a, intermediate, fv, fe) if ba1 is not None else None
            if ab is None or ba is None or ab != ba:
                return swaps, ("noncommuting-prefix-pair", j-1)
            left[j-1], left[j] = left[j], left[j-1]
            swaps += 1
            j -= 1
    assert left == right
    assert replay(left, start, intermediate, fv, fe) == intermediate
    return swaps, None

def one_alternating_cycle(left_diff, right_diff):
    adjacency = defaultdict(set)
    for pair in left_diff | right_diff:
        a, b = pair_cells(pair)
        adjacency[a].add(b); adjacency[b].add(a)
    if not adjacency or any(len(v) != 2 for v in adjacency.values()):
        return False
    seen, stack = set(), [next(iter(adjacency))]
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        stack.extend(adjacency[node] - seen)
    return len(seen) == len(adjacency)

def main():
    ap = argparse.ArgumentParser()
    for name in ("collapse", "diagrams", "inventory"):
        ap.add_argument("--" + name, required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()

    collapse, ch = load(args.collapse, EXPECTED["collapse"])
    diagrams, dh = load(args.diagrams, EXPECTED["diagrams"])
    inventory, ih = load(args.inventory)
    face_table_hash = hashlib.sha256(json.dumps(
        inventory["face_key_table"], sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    assert face_table_hash == EXPECTED["inventory_face_table"], (face_table_hash, EXPECTED["inventory_face_table"])

    fv = [face_vertices(x) for x in inventory["face_key_table"]]
    fe = [face_edges(x) for x in inventory["face_key_table"]]
    diagram_lookup = {(pi, wi): w for pi, pair in enumerate(diagrams["per_pair"])
                      for wi, w in enumerate(pair["graph5_witnesses"])}

    rows = []
    suffix_sizes = Counter()
    common_extra_sizes = Counter()
    extra_orders = Counter()
    prefix_swaps = Counter()
    intermediate_sizes = Counter()
    witness_ids = set()

    for witness in collapse["families"]["graph5"]["witness_results"]:
        pi, wi = witness["pair_index"], witness["witness_index"]
        support_faces = diagram_lookup[(pi, wi)]["support_face_indices"]
        for perm in witness["permutation_results"]:
            pmap = perm["source_to_support_isomorphism"]
            for cert in perm["diamond_certificates"]:
                if cert["same_elementary_pair_set"] or cert["source_mark_pair"] != [1, 2]:
                    continue
                assert pmap[0] == 0 and pmap[3] == 3
                assert witness["single_deletion_certificates"][str(pmap[3])]["success"] is True

                # Restrict source marks {1,2} and then the third eligible mark 3.
                restricted_labels = [i for i in range(4) if i != pmap[3]]
                root_label = pmap[0]
                X = union(set().union(*(set(support_faces[i]) for i in restricted_labels)), fv, fe)
                B = union(support_faces[root_label], fv, fe)

                full_left = sequence(cert["path_delete_m_then_n"])
                full_right = sequence(cert["path_delete_n_then_m"])
                left, left_crossing = restrict_sequence(full_left, X)
                right, right_crossing = restrict_sequence(full_right, X)
                assert not left_crossing and not right_crossing, (pi, wi, pmap, left_crossing, right_crossing)
                assert replay(left, X, B, fv, fe) == B, (pi, wi, "restricted-left-replay")
                assert replay(right, X, B, fv, fe) == B, (pi, wi, "restricted-right-replay")

                diff_left, diff_right = set(left)-set(right), set(right)-set(left)
                diff = diff_left | diff_right
                faces = {p[2] for p in diff if p[0] == "FE"}
                edges = {p[1] if p[0] == "FE" else p[2] for p in diff}
                vertices = {p[1] for p in diff if p[0] == "EV"}
                assert (len(faces), len(edges), len(vertices), len(diff)) == (1, 2, 1, 4)
                assert len(diff_left) == len(diff_right) == 2
                assert one_alternating_cycle(diff_left, diff_right)

                block_l, _, _, prefix_l, suffix_l = dependency_close(left, X, B, diff_left, fv, fe)
                block_r, _, _, prefix_r, suffix_r = dependency_close(right, X, B, diff_right, fv, fe)
                extra_l, extra_r = block_l-diff_left, block_r-diff_right
                assert extra_l == extra_r
                mid_l = replay(prefix_l, X, B, fv, fe)
                mid_r = replay(prefix_r, X, B, fv, fe)
                assert mid_l is not None and mid_l == mid_r
                assert replay(suffix_l, mid_l, B, fv, fe) == B
                assert replay(suffix_r, mid_r, B, fv, fe) == B
                swaps, error = normalize_prefix(prefix_l, prefix_r, X, mid_l, fv, fe)
                assert error is None and swaps is not None
                assert set(suffix_l)-set(suffix_r) == diff_left
                assert set(suffix_r)-set(suffix_l) == diff_right

                order_l = [p for p in suffix_l if p in extra_l]
                order_r = [p for p in suffix_r if p in extra_r]
                suffix_sizes[len(block_l)] += 1
                common_extra_sizes[len(extra_l)] += 1
                extra_orders[("".join(p[0] for p in order_l), "".join(p[0] for p in order_r))] += 1
                prefix_swaps[swaps] += 1
                intermediate_sizes[(len(mid_l["F"]), len(mid_l["E"]), len(mid_l["V"]))] += 1
                witness_ids.add(witness["witness_id"])
                rows.append({
                    "pair_index": pi, "witness_index": wi, "witness_id": witness["witness_id"],
                    "source_mark_pair": [1, 2], "further_deleted_source_mark": 3,
                    "source_to_support_map": pmap, "restricted_support_labels": restricted_labels,
                    "root_support_label": root_label, "no_pair_crosses_restriction": True,
                    "both_restricted_paths_replay_to_root_support": True,
                    "restricted_alternating_difference_pairs_per_side": [2, 2],
                    "one_connected_alternating_cycle": True,
                    "dependency_closed_suffix_pair_count": len(block_l),
                    "common_extra_pair_count": len(extra_l),
                    "common_extra_order_equal": order_l == order_r,
                    "common_extra_left_word": [p[0] for p in order_l],
                    "common_extra_right_word": [p[0] for p in order_r],
                    "prefix_normalizing_valid_swaps": swaps,
                    "same_prefix_pair_set": True, "same_intermediate_inventory": True,
                    "intermediate_inventory_counts": {
                        "faces": len(mid_l["F"]), "edges": len(mid_l["E"]), "vertices": len(mid_l["V"])
                    },
                    "both_local_suffixes_replay_to_root_support": True
                })

    assert len(rows) == 64 and len(witness_ids) == 32
    assert suffix_sizes == Counter({4:16, 6:8, 7:24, 10:16})
    assert common_extra_sizes == Counter({2:16, 4:8, 5:24, 8:16})
    assert sum(v for k, v in extra_orders.items() if k[0] == k[1]) == 56
    assert sum(v for k, v in extra_orders.items() if k[0] != k[1]) == 8
    assert prefix_swaps == Counter({0:40, 16:8, 24:16})
    assert sum(v for k, v in extra_orders.items() if k == ("FEEVEVEV", "EVFEEVEV")) == 4
    assert sum(v for k, v in extra_orders.items() if k == ("EVFEEVEV", "FEEVEVEV")) == 4

    result = {
        "schema": "PF-I16-FOUR-CELL-SWITCH-RESTRICTION-NATURALITY-v1",
        "inputs": {
            "collapse_payload_sha256": ch, "diagrams_payload_sha256": dh,
            "inventory_payload_sha256": ih, "inventory_face_table_sha256": face_table_hash
        },
        "scope": "64 graph-5 Ngrid=12 minimal four-cell source-mark-[1,2] certificates under both root-preserving maps, restricted by the third eligible source mark 3",
        "counts": {
            "certificate_map_rows": 64, "distinct_geometric_witnesses": 32,
            "third_mark_single_deletion_certificates_success": 64,
            "no_elementary_pair_crosses_restriction_boundary": 64,
            "restricted_left_and_right_paths_replay_to_root_support": 64,
            "restricted_symmetric_difference_is_one_four_pair_alternating_cycle": 64,
            "common_prefix_pair_sets": 64, "common_intermediate_inventories": 64,
            "prefixes_normalized_by_valid_adjacent_swaps": 64,
            "both_dependency_closed_suffixes_replay_to_root_support": 64,
            "dependency_closed_suffix_pair_counts": [{"pairs":k,"count":v} for k,v in sorted(suffix_sizes.items())],
            "common_extra_pair_counts": [{"pairs":k,"count":v} for k,v in sorted(common_extra_sizes.items())],
            "common_extra_order_equal": 56, "common_extra_order_different": 8,
            "common_extra_order_words": [{"left":k[0],"right":k[1],"count":v} for k,v in sorted(extra_orders.items())],
            "prefix_normalizing_valid_swap_counts": [{"swaps":k,"count":v} for k,v in sorted(prefix_swaps.items())],
            "restricted_intermediate_inventory_counts": [
                {"faces":k[0],"edges":k[1],"vertices":k[2],"count":v}
                for k,v in sorted(intermediate_sizes.items())
            ]
        },
        "conclusions": {
            "source_mark_3_restriction_preserves_both_collapse_paths": True,
            "restricted_paths_retain_four_pair_alternating_cycle": True,
            "restricted_paths_factor_through_a_common_prefix": True,
            "restricted_prefixes_are_related_by_valid_adjacent_commutations": True,
            "restricted_dependency_pair_sets_agree": True,
            "eight_order_sensitive_cases_remain_order_sensitive": True,
            "finite_restriction_naturality_only": True,
            "general_restriction_naturality_proved": False,
            "geometric_L8_closed": False
        },
        "rows": rows
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["counts"], sort_keys=True))

if __name__ == "__main__":
    main()
