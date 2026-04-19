###“Smart Storage Analyzer”###

'''It should: Scan all files

Print:  total files
        total size
        largest file'''

from pathlib import Path

path = Path(".")

totalFiles = 0
totalFileSize = 0
largestFileSize = 0
largestFile = None

for file in path.rglob("*.py"):
    if file.is_file():
        totalFiles += 1

        totalFileSize += file.stat().st_size

        if file.stat().st_size > largestFileSize:
            largestFile = file
            largestFileSize = file.stat().st_size

print("Total Files = ",totalFiles)
print("Total File size = ",int(totalFileSize/1024),"MB")
print("Largest File = ",largestFile)
print("Largest File Size = ",largestFileSize/1024,"MB")