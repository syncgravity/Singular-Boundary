import numpy as np,itertools,opt_einsum as oe,json
from pathlib import Path
z=np.load('/mnt/data/R3_looped_four_prism_2026_10_27/incidence.npz'); B1=z['d1'];B2=z['d2'];Q=list(map(int,z['seam_face_ids']))
r=json.loads(Path('/mnt/data/R3_four_prism_gaugefixed_2026_10_27/certificate.json').read_text());free=set(r['full_free_edges']);chords=set(r['chord_edges']);
def face_word(f):
 es=list(map(int,np.flatnonzero(B2[:,f])));st={e:int(np.flatnonzero(B1[:,e]==-1)[0]) for e in es};en={e:int(np.flatnonzero(B1[:,e]==1)[0]) for e in es};v=min(set(st.values())|set(en.values()));w=[]
 for _ in es:
  o=[(e,1,en[e]) for e in es if st[e]==v and B2[e,f]==1 and e not in [x[0] for x in w]]+[(e,-1,st[e]) for e in es if en[e]==v and B2[e,f]==-1 and e not in [x[0] for x in w]]
  assert len(o)==1
  e,s,v=o[0];w.append((e,s))
 return [p for p in w if p[0] in free]
sigma=np.array([np.eye(2),1j*np.array([[0,1],[1,0]]),1j*np.array([[0,-1j],[1j,0]]),1j*np.diag([1,-1])]);
def moment(a,b):
 A=sigma if a==1 else sigma.conj().transpose(0,2,1)
 B=sigma if b==1 else sigma.conj().transpose(0,2,1)
 return sum(np.einsum('ij,kl->ijkl',A[t],B[t]) for t in range(4))/4
sols=[[0,1,2,5,16,17,18,19],[6,7,8,9,11,12,14,15]]
def contract(S):
 words={('f',f):face_word(f) for f in S}
 words.update({('p',i):[tuple(r['gauge_fixed_face_chords'][str(f)][0])] for i,f in enumerate(Q)})
 occ={e:[] for e in free}; inds={};args=[];out=[];lab=0;scalar=1
 for key,word in words.items():
  n=len(word)
  if not n:
   assert key[0]=='f';scalar*=2;continue
  if key[0]=='f':labels=list(range(lab,lab+n));lab+=n
  else:labels=list(range(lab,lab+2));lab+=2;out.extend(labels)
  for i,(e,s) in enumerate(word):
   idx=(labels[i],labels[(i+1)%n]) if key[0]=='f' else (labels[0],labels[1])
   occ[e].append((s,idx))
 for e,items in occ.items():
  if not items:continue
  assert len(items)==2,(e,items)
  args.extend([moment(items[0][0],items[1][0]),list(items[0][1]+items[1][1])])
 result=oe.contract(*args,out,optimize='greedy')*scalar
 return result.transpose(0,2,4,6,1,3,5,7).reshape(16,16)
M1,M2=[contract(s) for s in sols];M=M1+M2
for name,x in [('S03',M1),('S12',M2),('sum',M)]:
 print(name,'trace',np.trace(x),'hermitian deviation',np.max(abs(x-x.conj().T)),'eig real',np.round(np.linalg.eigvalsh((x+x.conj().T)/2),10))
 print('nonzero entries',np.count_nonzero(abs(x)>1e-12))
print('norm diff previous:',np.max(abs(M-np.load('/mnt/data/R3_four_prism_matrix_minimal_2026_10_27/matrices.npz')['M_sum'])))
out=Path('/mnt/data/R3_four_prism_gaugefixed_2026_10_27');np.savez(out/'gaugefixed_minimal_matrices.npz',M03=M1,M12=M2,Msum=M,leading_beta8=M/256)
cert=json.loads((out/'certificate.json').read_text());cert['gaugefixed_M03_trace']=float(np.trace(M1).real);cert['gaugefixed_M12_trace']=float(np.trace(M2).real);cert['gaugefixed_eig_Msum']=np.linalg.eigvalsh((M+M.conj().T)/2).tolist();cert['gaugefixed_hermitian_deviation']=float(np.max(abs(M-M.conj().T)));(out/'certificate.json').write_text(json.dumps(cert,indent=2))
# Exact symbolic recognition of the two gauge-fixed intertwined operators.
S12=np.zeros((16,16));S34=np.zeros((16,16))
for i in range(16):
 b=[(i>>(3-k))&1 for k in range(4)];a=b.copy();a[0],a[1]=a[1],a[0];j=sum(a[k]<<(3-k) for k in range(4));S12[i,j]=1
 a=b.copy();a[2],a[3]=a[3],a[2];j=sum(a[k]<<(3-k) for k in range(4));S34[i,j]=1
omega=np.zeros(16);omega[[3,6,9,12]]=[.5,-.5,-.5,.5]
assert np.allclose(M1,S12@S34/1024,atol=1e-14)
assert np.allclose(M2,np.outer(omega,omega)/256,atol=1e-14)
assert np.allclose(np.linalg.eigvalsh(M),[-1/1024]*6+[1/1024]*9+[5/1024],atol=1e-14)
cert['exact_G03']='SWAP12 SWAP34 /1024';cert['exact_G12']='omega omega^T /256';cert['omega_components']={'0011':'+1/2','0110':'-1/2','1001':'-1/2','1100':'+1/2'};cert['eigenvalues_leading_A8']=[-1/262144]*6+[1/262144]*9+[5/262144];cert['negative_eigenvalues_small_beta']=6;cert['scalar_trace_A8']=float(np.trace(M/256).real)
(out/'certificate.json').write_text(json.dumps(cert,indent=2))
print('PASS: exact gauge-fixed M03=SWAP12 SWAP34/1024, M12=|omega><omega|/256, six negative eigenvalues')
