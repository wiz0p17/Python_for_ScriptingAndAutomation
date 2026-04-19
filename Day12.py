##Get File Metadata

from pathlib import Path
import time

'''file = Path("File.txt")'''

'''stats = file.stat()

print("Size = ",stats.st_size)
print("Last modified = ",stats.st_mtime)'''


###Convert Timestamp to Human Readable

'''import time

modifiedTime = time.ctime(file.stat().st_mtime)

print("Modified Time = ",modifiedTime)'''



###Filter by File Size

'''for file in Path(".").rglob("*"):
    if file.is_file and file.stat().st_size > 1000:
        print("Large Files are = ", file.name)'''



###Filter by File Age (VERY IMPORTANT 🔥)###

'''currentTime = time.time()

for file in Path(".").rglob("*"):
    if file.is_file():
        age = currentTime - file.stat().st_mtime

        if age > 7 * 86400:
            print("Older files are : ",file.name)'''



###File Permissions (Basic Idea)##

'''file = Path("File.txt")

print(file.stat().st_mode)'''



#Real Automation Script -->  Delete old files (>7 days)

"""path = Path(".")

currentTime = time.time()

for file in path.rglob("*"):
    if file.is_file():
        age = currentTime - file.stat().st_mtime

        if age > 7 * 86400:
            print("Deleting Files : ",file.name )
            file.unlink()"""



'''Print: File name
        size
        last modified'''
import time

for file in Path(".").rglob("*.py"):
    if file.is_file():
        print("File name =",file.name)
        print("File size = ",file.stat().st_size,"Kb")
        print("Last Modified = ",time.ctime(file.stat().st_mtime))



