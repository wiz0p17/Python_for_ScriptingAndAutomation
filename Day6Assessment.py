###👉 “Smart File Organizer v2” 👈🏻###

'''It should -->>>

Scan folder
Organize files by type
Ignore hidden files
Skip empty files
Print summary:
total files processed
files moved'''

from pathlib import Path
import shutil

path = Path(".")

total = 0
moved = 0

for file in path.iterdir():
    if file.is_file and not file.name.startswith(".") and not file.stat().st_size == 0:
        total = total+1
        if file.suffix == ".txt":
            folder = path / "Text"

        elif file.suffix == ".log":
            folder = path / "Logs"

        elif file.suffix == ".jpg":
            folder = path / "Images"
        
        else:
            continue

        folder.mkdir(exist_ok=True)
        shutil.move(file,folder / file.name)
        moved = moved+1
    
print("\nYour files are organized!!\n")

print("Total files processed : ",total,"\n")
print("Total files moved : ",moved,"\n")

    
