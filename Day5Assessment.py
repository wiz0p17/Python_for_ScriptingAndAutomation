###Your Assignment (Important 🔥)###

'''👉 Build this:

“Downloads Organizer (Basic Version)”

It should:

Scan a folder
Move:
.txt → TextFiles/
.jpg → Images/
.pdf → PDFs/'''

from pathlib import Path
import shutil

base = Path(".")

for file in base.iterdir():
    if file.is_file():
        if file.suffix == ".txt":
            folder = base / "TextFiles"
        elif file.suffix == ".jpg":
            folder = base / "Images"
        elif file.suffix == ".pdf":
            folder = base / "PDFs"
        else:
            continue

        folder.mkdir(exist_ok=True)
        shutil.move(file, folder / file.name)

print("Files organized!")