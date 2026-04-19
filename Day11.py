from pathlib import Path

'''for file in Path(".").rglob("*"):
    if file.is_file():
        print(file.name)'''


#Rename file in Bulk

'''for file in Path(".").rglob("*.txt"):
    new_file = file.parent / ("new_" + file.name)
    print(file.parent)'''


##Delete Files

'''for file in Path(".").rglob("*.tmp"):
    print("Deleting file: ",file.name)
    file.unlink()'''


##Move Files from Nested Folders

import shutil

'''destination = Path("All_text_files")
destination.mkdir(exist_ok=True)

for file in Path(".").rglob("*.txt"):
    shutil.move(file,destination / file.name)'''


### Modify File Content (Powerful)##

#Example: Replace text in all .txt files#

'''for file in Path(".").rglob("*.txt"):
    content = file.read_text()

    updated = content.replace("ERROR","")

    file.write_text(updated)'''


###Mini Practice (DO THIS)###

##👉 Add prefix old_ to all .log files:##


for file in Path(".").rglob("*.log"):
    file.rename(file.parent / ("Old_" + file.name))



