##Loop Through Many Files##

from pathlib import Path

'''path = Path(".")

for file in path.iterdir():
    if file.is_file():
        print(file.name)'''

##Filtering Files##

'''path = Path(".")

for file in path.iterdir():
    if file.suffix == ".txt":
        print(file.name)'''

##Multiple Types##

'''path = Path(".")

for file in path.iterdir():
    if file.suffix in [".txt",".log",".csv"]:
        print(file.name)'''


#Ignore Hidden Files#

'''path = Path(".")

for file in path.iterdir():
    if not file.name.startswith("."):
        print(file.name)'''


#File Metadata#

'''file = Path("name.txt")

print(file.stat().st_size)   #size in byte
print(file.stat().st_mtime)   #last modified date'''

#Delete files larger than a certain size:##

'''path = Path(".")

for file in path.iterdir():
    if file.is_file() and file.stat().st_size > 500:
        print(file.name)'''


### Deletes .log files older than X days ###

import time

path = Path(".")

days = 7
currnet_time = time.time()

for file in path.iterdir():
    if file.suffix == ".log":
        file_age = currnet_time - file.stat().st_mtime

        if file_age > days * 86400:
            print("Deleting File : ",file)
            file.unlink()





