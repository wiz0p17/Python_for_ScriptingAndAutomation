##Using try/except (VERY IMPORTANT 🔥)###

'''from pathlib import Path

for file in Path(".").rglob("*"):
    try:
        if file.is_file():
            print(file.stat().st_size)

    except Exception as e:
        print(f"Error with File{file}: {e}")
'''


##Handle Specific Errors (Best Practice)
'''
try:
    file.unlink()
except FileNotFoundError:
    print("File already deleted or not found")
except PermissionError:
    print("Permission Denied")
'''

##Safe Automation Pattern (IMPORTANT)

'''from pathlib import Path

for file in Path(".").rglob("*"):
    if file.is_file():
        try:
            print("Processing:", file)
            # your logic here

        except Exception as e:
            print(f"Skipping {file}: {e}")'''


##Real Production Script

from pathlib import Path
import time

path = Path(".")
currentTime = time.time()

for file in path.rglob("*.log"):
    if file.is_file():
        try:
            age = currentTime - file.stat().st_mtime

            if age > 7 * 86400:
                print("Deleting File :",file.name)
                file.unlink()
        
        except FileNotFoundError:
            print("file not found!!!")

        except PermissionError:
            print("Permission Denied!!!")


###Add error handling to your previous scripts###

for file in path.rglob("*.txt"):
    try:
        print(file.read_text())

    except Exception as e:
        print("An errror Occoured: ",e)