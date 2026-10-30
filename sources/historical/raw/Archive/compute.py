import numpy as np,itertools,opt_einsum as oe,json
z=np.load('/mnt/data/R3_looped_four_prism_2026_10_27/incidence.npz');B1,B2,B3=z['d1'],z['d2'],z['d3'];Q=list(map(int,z['seam_face_ids']))
sols=[[0,1,2,5,16,17,18,19],[6,7,8,9,11,12,14,15]]
def face_word(f):
 es=list(np.flatnonzero(B2[:,f]));st={e:int(np.flatnonzero(B1[:,e]==-1)[0]) for e in es};en={e:int(np.flatnonzero(B1[:,e]==1)[0]) for e in es};v=min(set(st.values())|set(en.values()));w=[]
 for _ in es:
  o=[(e,1,en[e]) for e in es if st[e]==v and B2[e,f]==1 and e not in [x[0] for x in w]]+[(e,-1,st[e]) for e in es if en[e]==v and B2[e,f]==-1 and e not in [x[0] for x in w]]
  assert len(o)==1,(f,v,o)
  e,s,v=o[0];w.append((e,s))
 return w
words={f:face_word(f) for f in range(20)}
sigma=np.array([np.eye(2),1j*np.array([[0,1],[1,0]]),1j*np.array([[0,-1j],[1j,0]]),1j*np.diag([1,-1])])
def moment(signs):
 mats=[sigma if s==1 else sigma.conj().transpose(0,2,1) for s in signs]
 if len(signs)==2:return sum(np.einsum('ab,cd->abcd',mats[0][a],mats[1][a]) for a in range(4))/4
 assert len(signs)==4
 arr=np.zeros((2,)*8,complex)
 for a,b,c,d in itertools.product(range(4),repeat=4):
  coef=(int(a==b and c==d)+int(a==c and b==d)+int(a==d and b==c))/24
  if coef:arr+=coef*np.einsum('ab,cd,ef,gh->abcdefgh',mats[0][a],mats[1][b],mats[2][c],mats[3][d])
 return arr
def contract(S):
 active=set(S)|set(Q);occ={e:[] for e in range(33)}
 for f in sorted(active):
  for i,(e,s) in enumerate(words[f]):occ[e].append((f,i,s))
 inds={};out=[];label=0
 for f in sorted(active):
  n=len(words[f]); ports=f in Q;seq=list(range(label,label+n+int(ports)));label+=len(seq)
  for i in range(n):inds[f,i]=(seq[i],seq[i+1] if ports else seq[(i+1)%n])
  if ports:out.extend([seq[0],seq[-1]])
 args=[]
 for e,items in occ.items():
  if not items:continue
  assert len(items) in (2,4)
  args.extend([moment([s for f,i,s in items]),list(itertools.chain.from_iterable(inds[f,i] for f,i,s in items))])
 res=oe.contract(*args,out,optimize='greedy')
 return res.transpose(0,2,4,6,1,3,5,7).reshape(16,16)
M03,M12=map(contract,sols)
SW=np.zeros((16,16),complex)
for bits in itertools.product((0,1),repeat=4):
 i=sum(bits[k]<<(3-k) for k in range(4)); bb=(bits[0],bits[1],bits[3],bits[2]);j=sum(bb[k]<<(3-k) for k in range(4));SW[i,j]=1
assert np.allclose(M03,SW/2048,atol=1e-14)
assert np.allclose(M12,np.eye(16)/4096,atol=1e-14)
assert np.isclose(np.trace(M03),1/256) and np.isclose(np.trace(M12),1/256)
M=M03+M12; eig=np.linalg.eigvalsh(M)
assert np.allclose(eig,[-1/4096]*4+[3/4096]*12)
assert np.isclose(np.trace(M/256),1/32768)
np.savez('/mnt/data/R3_four_prism_matrix_minimal_2026_10_27/matrices.npz',M_surface_03=M03,M_surface_12=M12,M_sum=M,swap_34=SW,leading_beta8_matrix=M/256)
cert={'origin':'constructed quadrilateral four-prism loop; no Penrose provenance','ports':Q,'minimal_surfaces':sols,'matrix_03':'SWAP_34/2048','matrix_12':'I_16/4096','sum_negative_eigenvalues':[-1/4096]*4,'sum_positive_eigenvalues':[3/4096]*12,'trace_each':1/256,'scalar_beta8_trace':1/32768,'leading_matrix_eigenvalues':[-1/1048576]*4+[3/1048576]*12,'basis':'oriented plaquette loop based at minimum incident vertex','scope':'open port fundamental matrix moment, not certified Fourier of gauge-fixed independent coordinates'}
with open('/mnt/data/R3_four_prism_matrix_minimal_2026_10_27/certificate.json','w') as f:json.dump(cert,f,indent=2)
print('PASS: complete exact 16x16 minimal spin contractions; eigenspectrum',eig,'trace',np.trace(M))
