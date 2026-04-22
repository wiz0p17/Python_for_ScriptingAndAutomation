##Smart File Organizer (PRO VERSION)##

'''Your script will:

Organize files by type
Skip hidden files
Skip empty files
Handle errors safely
Log all operations
Print summary'''

import logging
from pathlib import Path
import shutil

## Setting up log file

logging.basicConfig(filename="Organizer.log",level=logging.INFO,format= "%(asctime)s - %(levelname)s - %(message)s")

#Target Folder
path = Path("./test")

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Archives": [".zip", ".rar"]
}

totalFiles = 0
movedFiles = 0
skippedFiles = 0

for file in path.iterdir():
    if file.is_file() and not file.name.startswith("."):
        
        try:
            #skip empty files
            if file.stat().st_size <=0:
                skippedFiles +=1
                logging.info(f"Skipped file : {file.name}")
                continue
        
            totalFiles +=1
            moved = False

            for folderName ,extensions in FILE_TYPES.items():
                if file.suffix.lower() in extensions:
                    targetFolder = path / folderName
                    targetFolder.mkdir(exist_ok=True)
                    shutil.move(file , targetFolder / file.name)
                    logging.info(f"Moved {file} -> {targetFolder}")
                    movedFiles += 1
                    moved = True
                    break
            
            if not moved:

                other = path / "Others"
                other.mkdir(exist_ok=True)
                shutil.move(file,other / file.name)
                logging.info(f"Moved {file} -> {other}")
                movedFiles += 1
        
        except Exception as e:
            logging.error(f"An error occoured in {file} : {e}")
            skippedFiles += 1
            logging.info(f"Skipped file : {file.name}")


print("✅ Organizing Complete!")
logging.info(f"Total file processed : {totalFiles}")
logging.info(f"Total files moved : {movedFiles}")
logging.info(f"Skipped Files : {skippedFiles}")      