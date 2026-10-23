"""Fast 5m-grid OpenLISEM: preserve LDD cell size and avoid closed lower boundary."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
source_file=HERE.parent/"openlisem_reference_trial"/"generate.py"
s=source_file.read_text(encoding="utf8")
assert "R=C=50" in s and "DX=2.0" in s
s=s.replace("R=C=50","R=C=20").replace("DX=2.0","DX=5.0")
selection="""variants=[
    ("Oak",5,"exponential",1),
    ("Oak",10,"exponential",1),
    ("Oak",20,"exponential",1),
    ("Miscanthus",10,"exponential",1),
    ("Oak",10,"exponential",2),
    ("Miscanthus",10,"exponential",2),
]
def save_map"""
s,n=re.subn(r"variants=\[.*?\]\ndef save_map",selection,s,flags=re.S)
assert n==1,n
namespace={"__name__":"__main__","__file__":str(source_file)}
exec(compile(s,str(source_file),"exec"),namespace)
