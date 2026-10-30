exec(open('/mnt/data/stage18_audit/analyze.py').read().split("results={'integrity'")[0])
for kind in ['square','penrose']:
 old=np.concatenate([np.load(f'/mnt/data/{kind}_nt20_seed{s}.npz')['observables_scalar'] for s in seeds]);new=np.concatenate([X[kind,s] for s in seeds]);
 print(kind,'old',old.shape,'new',new.shape,'oldC',np.round(corr(old)[2:5,:3]*1e7,3),'newC',np.round(corr(new)[2:5,:3]*1e7,3))
 v=new.reshape(-1,12);r=np.corrcoef(v,rowvar=False)
 for i in [9,10,11]:print('new level12 channel',i,'closest original level6',np.max(abs(r[i,6:9])), 'r',np.round(r[i,6:9],5))
