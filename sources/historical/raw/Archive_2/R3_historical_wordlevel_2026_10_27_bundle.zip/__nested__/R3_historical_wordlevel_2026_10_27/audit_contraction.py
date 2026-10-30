import json, numpy as np
from pathlib import Path
root=Path(__file__).resolve().parent
out={}
for vol in ['5','6_5','8','10']:
 j=json.loads((root/f'certificate_radius_{vol}.json').read_text()); A=j['A']; aset=set(A); W=j['words_all']; F=sorted(map(int,j['Bianchi_peel']['multiplicity'].keys()));
 # Assign to each retained face an incident link, minimizing the count of other retained faces at the link.
 stars={int(e):sorted({x['face'] for x in entries}) for e,entries in j['star_words'].items()}
 B=np.zeros((len(A),len(A)),dtype=int); E={};
 for i,p in enumerate(A):
  es=[e for e,s in W[p] if e in stars];
  assert es
  e=min(es,key=lambda x:(len(stars[x]),x));E[str(p)]=e
  for r in stars[e]:
   assert r in aset
   B[i,A.index(r)]=1
 assert (np.diag(B)==1).all()
 radius=float(max(abs(x) for x in np.linalg.eigvals(B)))
 fcovered=sum(p in aset for p in F)
 out[vol]={'Q':len(j['Q']),'H':len(j['H']),'A':len(A),'fill':len(F),'pairs':sum(map(len,j['pair_staple_loop_words'].values())), 'candidate_B':'elementary valid bound m_e <= sum incident retained plaquettes','B_diagonal_min':int(np.diag(B).min()),'B_row_sum_min':int(B.sum(1).min()),'B_row_sum_max':int(B.sum(1).max()),'B_spectral_radius_float':radius,'strict_contraction_ruled_out_by_diagonal':True,'fill_faces_all_in_A':fcovered==len(F)}
 (root/f'elementary_B_radius_{vol}.npz').write_bytes(b'') if False else None
 np.savez_compressed(root/f'elementary_B_radius_{vol}.npz',B=B,A=np.array(A),chosen_link=np.array([E[str(p)] for p in A]),fill=np.array(F))
(root/'contraction_audit.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
