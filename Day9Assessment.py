### “Advanced File Scanner” ###

'''It should:

Ask user:
extension
minimum size
Print files matching:
extension
size condition'''

from pathlib import Path

path = Path("/Users/vivek/Downloads")

extension = input("Enter File Extension: ")
fileSize = int(input("Enter minimum file Size in bytes : "))

for file in path.rglob(f"*.{extension}"):
    if (file.stat().st_size > fileSize and
        not file.name.startswith(".")):
        print("File is: ",file.name)