import os
import re
from pathlib import Path

archive = Path("./archive")
other = Path("./other")
tex = Path("./tex")

pattern = re.compile(r"\.(aux|fdb_latexmk|fls|log|synctex.gz|bbl|bcf|blg|out|run.xml|xdv)")

for p in tex.rglob("*"):
    if pattern.search(p.name):
        print(p)