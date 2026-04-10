#import os
from pathlib import Path
#print(os.getcwd())

"""files = os.listdir()
print(files)"""

'''print(os.path.exists("os.p"))'''

'''print(os.path.isfile("Day1.py"))
print(os.path.isdir("venv"))'''

#path = Path()

'''print(path.cwd())
print(list(path.iterdir()))'''


'''file = Path("Day1.py")

print(file.exists())
print(file.is_file())'''


path = Path(".")

for item in path.iterdir():
    if item.is_file():
        print(f"File : {item}")
    else:
        print(f"Folder : {item}")
