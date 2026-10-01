from pathlib import Path
import base64,gzip,hashlib,sys
root=Path(__file__).resolve().parent
parts=sorted((root/'source'/'ad_gzip_b64').glob('part_*.txt'))
if not parts: raise SystemExit('no baseline chunks')
b64=''.join(p.read_text(encoding='utf-8') for p in parts)
raw=gzip.decompress(base64.b64decode(b64))
sha=hashlib.sha256(raw).hexdigest();expected='31294f8bec9f45d6f57a01b092207aa83abc9c6126fd99dc1b58e808a7afd167'
if sha!=expected: raise SystemExit(f'baseline sha mismatch {sha} != {expected}')
out=root/'air-empire-network-ai-v2.3.0-alpha7.0-ad-complete-entrant-lifecycle-standalone.html';out.write_bytes(raw)
print(out);print(sha)