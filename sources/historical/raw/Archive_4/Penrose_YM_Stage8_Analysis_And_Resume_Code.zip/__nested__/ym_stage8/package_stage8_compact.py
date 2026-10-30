from pathlib import Path
import hashlib,json,zipfile
root=Path(__file__).resolve().parent
files=sorted(p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts
             and not p.name.endswith('.partial.npz')
             and p.name!='SHA256_MANIFEST.json')
m={}
for p in files:
 h=hashlib.sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 m[str(p.relative_to(root))]={'sha256':h.hexdigest(),'bytes':p.stat().st_size}
(root/'SHA256_MANIFEST.json').write_text(json.dumps(m,indent=2))
out=root.parent/'Penrose_YM_Stage8_Analysis_And_Resume_Code.zip'
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,allowZip64=True) as z:
 for p in files+[root/'SHA256_MANIFEST.json']:
  if p.parent.name=='checkpoints' and p.suffix=='.npz':continue
  z.write(p,arcname=str(Path('ym_stage8')/p.relative_to(root)))
with zipfile.ZipFile(out) as z:
 assert z.testzip() is None
 mm=json.loads(z.read('ym_stage8/SHA256_MANIFEST.json'))
 for fn in z.namelist():
  if fn.endswith('SHA256_MANIFEST.json'):continue
  rr=fn.split('ym_stage8/',1)[1]
  assert hashlib.sha256(z.read(fn)).hexdigest()==mm[rr]['sha256'],rr
print('verified',out,out.stat().st_size,'bytes')
