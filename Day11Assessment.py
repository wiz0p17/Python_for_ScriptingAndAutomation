###“Bulk File Cleaner + Organizer”###

'''It should:

Scan all folders
Delete .tmp files
Move .log files → Logs/
Rename .txt files → add prefix processed_ '''

from pathlib import Path
import shutil

base = Path(".")

logsFolder = base / "Logs"
logsFolder.mkdir(exist_ok=True)

for file in base.rglob("*"):
    if file.is_file():

        #deleting temp Files
        if file.suffix == ".tmp":
            print("Deleting files: ",file.name)
            file.unlink()
        
        #move logs files
        if file.suffix == ".log":
            shutil.move(file, logsFolder / file.name)

        if file.suffix == ".txt":
            new_name = file.parent / ("processed_" + file.name)

            file.rename(new_name)
