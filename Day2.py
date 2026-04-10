from pathlib import Path

path = Path("/Users/vivek/Downloads")

'''count = 0
for file in path.iterdir():
    if file.is_file():
        print(f"File :{file}")
        count = count + 1

print("Total number of files are : ",count)'''

file = path / "NewFile.txt"

print(file)

#file.touch()

Path("parent/child").mkdir(parents=True, exist_ok=True)

