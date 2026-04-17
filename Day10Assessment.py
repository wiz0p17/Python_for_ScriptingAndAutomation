### “Recursive File Analyzer” ###

'''It should:

Scan all folders
Count:
total files
total size
Print summary'''

from pathlib import Path

path = Path(".")

totalFiles = 0
totalSize = 0

for file in path.rglob("*.py"):
    if file.is_file:
        totalFiles += 1
        totalSize += file.stat().st_size

print("-" * 50)
print("Total number of .py files are: ",totalFiles)
print("Total size of .py files are: ",int(totalSize/1024),"MB") 
print("-" * 50)