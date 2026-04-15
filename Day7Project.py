##Mini Project: Downloads Organizer##

'''A script that:

Scans a folder (Downloads or any folder)
Detects file types
Creates folders automatically
Moves files into correct folders'''

from pathlib import Path
import shutil

base = Path(".")

file_types = {
    "Images": [".jpg",".jpeg",".png"],
    "Documents": [".pdf",".xlsx",".docx",".txt"],
    "Videos": [".mkv",".mp4"],
    "Archives": [".rar",".zip"]
}

totalFiles = 0
movedFiles = 0

for file in base.iterdir():
    if file.is_file() and not file.name.startswith("."):
        if file.stat().st_size == 0:
            continue

        totalFiles += 1
        moved = False

        for folderName , extensions in file_types.items():
            if file.suffix.lower() in extensions:
                targetFolder = base / folderName
                targetFolder.mkdir(exist_ok=True)

                shutil.move(file, targetFolder / file.name)
                movedFiles += 1
                moved = True

        if not moved:
            other = base / "Others"
            other.mkdir(exist_ok=True)
            shutil.move(file,other / file.name)
            movedFiles += 1

print("\nOrganizing of files is complete!!!\n")
print("Total number of files are = ",totalFiles)
print("Total number of files moved are = ",movedFiles)