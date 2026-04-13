import shutil
from pathlib import Path

#basic copy
#shutil.copy("Report.txt","Hello.txt")

#copy with meta data
#shutil.copy2("Report.txt","Hello.txt")

#move files 
#shutil.move("Hello.txt","/Users/vivek/Downloads/Hello.txt")


#Delete File
"""file = Path("/Users/vivek/Downloads/Hello.txt")

if file.exists():
    file.unlink()

#Delete Folder
shutil.rmtree("Hello")"""


###Combine with pathlib (Best Practice)###
'''src = Path("Test.txt")
dest = Path("/Users/vivek/Downloads/Hello.txt")

shutil.copy(src,dest)'''

###Mini Practice (DO THIS)

'''👉 Script:

Create folder backup
Copy all .txt files into it'''

source = Path(".")
backup = Path("Backup")

backup.mkdir(exist_ok=True)

for file in source.iterdir():
    if file.suffix == ".txt":
        shutil.copy(file,backup / file)
        print(file)

print("Backup completed!")



