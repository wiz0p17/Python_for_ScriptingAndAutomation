"""Prints current directory
Lists all files
Counts total files"""


from pathlib import Path

path = Path(".")

print(path.cwd())

count = 0
for item in path.iterdir():
    if item.is_file():
        print(item)
        count= count+1

print("Total number of files : ", count)


