import os
import re
from typing import List, Dict
from pathlib import Path

folders: Dict[str, Path] = {
    "archive": Path("./archive"),
    "cvs and resumes": Path("./cvs and resumes"),
    "essays": Path("./essays"),
    "other": Path("./other"),
    "speeches": Path("./speeches")
}

pattern: re.Pattern = re.compile(r"\.(aux|fdb_latexmk|fls|log|synctex.gz|bbl|bcf|blg|out|run.xml|xdv)")

files_removed: List[Path | None]  = []

for k, v in folders.items():
    for p in v.rglob("*"):
        if pattern.search(p.name):
            os.remove(p)
            files_removed.append(p)
        
print("Files Removed")
for file in files_removed:
    print(f"\t{file}")