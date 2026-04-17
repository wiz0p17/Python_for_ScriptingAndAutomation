## Understanding os.walk() ##

import os

'''for root ,dirs,files in os.walk("."):
    print("Currnet folder :",root)
    print("folders : ",dirs)
    print("Files : ",files)
    print("-" * 30)'''


### Access Full File Path ###

'''for root ,dirs,files in os.walk("."):
    for file in files:
        full_path = os.path.join(root,file)
        print(full_path)'''


### 📌 Find all .txt files

'''for root,dirs,files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root,file))'''

    
### 👉 Find all .log files in entire system

'''for root,dirs,files in os.walk("."):
    for file in files:
        if file.endswith(".log"):
            print("Logs : ",os.path.join(root,file))'''


## pathlib Alternative (rglob) – Cleaner Way

'''from pathlib import Path

for file in Path(".").rglob("*.txt"):
    print(file.name)'''


###When to Use What?###
'''
✅ Use os.walk:
Need folder + file structure
Advanced control
✅ Use pathlib.rglob:
Simple file searching
Cleaner code (recommended)'''


from pathlib import Path

count = 0

for file in Path(".").rglob("*.txt"):
    count += 1

print("Total number of .txt files are : ",count) 