"""Assemble the exact archived base and current extension; no simulation is run."""
from pathlib import Path
import argparse,urllib.request,hashlib,zipfile,shutil,json
p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=a.output.resolve();r.mkdir(parents=True,exist_ok=True)
if any(r.iterdir()):raise SystemExit('Use a NEW empty output directory')
s=Path(__file__).resolve().parent;meta=json.loads((s/'publication_manifest.json').read_text())
def digest(f):return hashlib.file_digest(f.open('rb'),'sha256').hexdigest()
for n,key,sha in [('cep_extended_validation.zip','base','base_sha256'),('CEP3_audit_extension.zip','base_audit','base_audit_sha256')]:
 f=s/n
 if not f.exists():urllib.request.urlretrieve(meta[key],f)
 assert digest(f)==meta[sha],n+' checksum mismatch'
 d=r/'simulation/archive';d.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(f) as z:z.extractall(d)
f=s/meta['asset'];assert digest(f)==meta['sha256'],'current extension checksum mismatch'
with zipfile.ZipFile(f) as z:z.extractall(r)
print('Assembled:',r)
print('Install pinned packages, then run python reproducibility/reproduce.py verify')
print('Dense derived exports can be restored separately; see README_RELEASE.md')