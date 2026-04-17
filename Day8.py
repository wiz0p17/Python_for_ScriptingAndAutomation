###Pattern Matching (glob & fnmatch)###

'''from pathlib import Path

path = Path("/Users/vivek/Downloads")

for file in path.glob("*.pdf"):
    print(file)'''


### Recursive Search (🔥 Powerful)##

'''from pathlib import Path

path = Path("/Users/vivek/Downloads")

for file in path.rglob("*.pdf"):
    print(file)'''


##  rglob() = recursive glob


### Using fnmatch (Alternative Way)

'''import fnmatch
from pathlib import Path

for file in Path(".").iterdir():
    if fnmatch.fnmatch(file.name, "*.txt"):
        print(file)
        
###Works on file names (less used than glob)'''



###Mini Practice (DO THIS)###

##👉 Find all .log files and print them:##

'''from pathlib import Path

for file in Path(".").rglob("*.log"):
    print(file.name)'''



###Real Automation Example###

##👉 Backup only .txt files##

from pathlib import Path
import shutil

path = Path(".")

textFiles = path / "TextFilesFolder"

textFiles.mkdir(exist_ok=True)

for file in path.rglob("*.txt"):
    shutil.move(file, textFiles / file.name)

print("Backup Complete!!!")