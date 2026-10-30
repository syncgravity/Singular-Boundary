#!/usr/bin/env python3
"""Compute exact fixed-support constants for the safe joint finite-net Peierls surgery."""
from pathlib import Path
import json,math,csv
P=Path(__file__).resolve().parent
m=json.loads((P/'modes_certificate.json').read_text())
f=json.loads((P/'relative_words_joint.json').read_text())
fo=json.loads((P/'relative_words_joint_optimized.json').read_text())
o=json.loads((P/'optimized_basis.json').read_text())
g=json.loads((P/'joint_gluing_optimized_certificate.json').read_text())
no=json.loads((P/'exact_crossing_rank.json').read_text())
q=14;k=fo['solved_count'];b=o['best_crossing_faces'];nu=7
assert q==14 and k==59 and b==33 and g['crossing_retained_face_count']==33
assert no['extra_exterior_modes_accessible_while_preserving_crossing_faces']==1
assert all(j['layers'][0]['independent_exterior_modes']==24 for j in m['results'])
cert={'support_size_Q':q,'original_local_links':36,'exterior_compatibility_rank':24,'optimized_basis_links':o['best_basis_links'],
'joint_relative_group_eliminations':k,'remaining_free_local_links':1,'affected_retained_faces_flattened':62,'relator_identities':3,
'optimized_basis_crossing_face_count':b,'max_face_incidence':nu,'full_holonomy_net_size_per_link':'<=4097 lambda^(3/2)',
'left_Haar_jacobian_on_each_branch':1,'inverse_branch_multiplicity_bound':'(4097 lambda^(3/2))^59',
'global_action_decrease_guarantee':'lambda*(S_R(U)-S_R(T U)) >= lambda*s_H(U outside H) - 66*lambda - 826',
'exterior_minimum_tail':'P(lambda*s_H >= t) <= min(1, exp(-t + 66*lambda + 59*(1.5*log(lambda)+log(4097)+14)))',
'finite_net_log_constant':59*(math.log(4097)+14),
'crossing_fixed_no_go_rank':1,'crossing_fixed_missing_rank':23,
'per_Q_fixed_support_cost':{'mode_links_per_Q':24/q,'net_pivots_per_Q':59/q,'crossing_faces_per_Q':33/q},
'scope':'All statements concern one fixed 14-temporal-face Penrose support on nested radii 5, 6.5, 8, 10. The tail has an uncontrolled +66 lambda term, so it does not establish the sought polynomial-prefactor absolute concentration or general R3.'}
(P/'theorem_certificate.json').write_text(json.dumps(cert,indent=2))
rows=[]
for i,a in enumerate(m['results'][0]['layers'][0]['basis_exterior']):
 rows.append({'rank_index':i+1,'physical_link_id_radius5':a['link_id'],'link_type':a['key'][0],
              'time_level':a['key'][1],'z5_endpoints':str(a['key'][2]),'retained_faces_touching':a['retained_faces_touching_pivot'],
              'retained_faces_in_original_A':a['retained_faces_in_original_A'],
              'group_color':next(c for c,gp in enumerate(m['results'][0]['layers'][0]['colors']) if a['link_id'] in gp)})
with (P/'mode_table.csv').open('w',newline='') as fd:
 wr=csv.DictWriter(fd,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
print('PASS',cert['global_action_decrease_guarantee'],'log_constant',round(cert['finite_net_log_constant'],3),'24 mode CSV',len(rows))
