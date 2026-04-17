###Combine glob + Conditions##

from pathlib import Path

'''path = Path(".")'''

'''for file in path.rglob("*.py"):
    if file.stat().st_size > 500:
        print(file.name)
'''

###Filter by File Size

'''for file in path.rglob("*.py"):
    if file.stat().st_size > 1000:
        print("File name : ",file.name)'''


###Filter by Time (Very Important 🔥)

import time

currentTime = time.time()

'''for file in path.rglob("*.py"):
    fileAge = currentTime - file.stat().st_mtime
    if fileAge > 7 * 86400:
        print(file.name)
'''


##Combine Multiple Conditions

'''for file in path.rglob("*.py"):
    if ( file.stat().st_size > 500 and
        not file.name.startswith(".") and
        currentTime - file.stat().st_mtime > 3*86400 ):

        print("File is : ",file.name)'''


### Find Large Old Logs ###

path = Path("/Users/vivek/Downloads")

for file in path.rglob("*.[pP][dD][fF]"):
    if ( file.stat().st_size > 10 and 
        not file.name.startswith(".") and 
        currentTime - file.stat().st_mtime > 7*86400):
        print(f"{file.name} --> Old and Large Files")



