###“Smart File Finder”###

'''It should:

Ask user for extension (like .txt)
Find all matching files
Print:
file name
size'''


from pathlib import Path


print
userInput = input("Enter file Type: example .txt , .py etc. : ")

print("Your File type is : ",userInput)


for file in Path(".").rglob(f"*{userInput}"):
    print(f"\nFile name : {file.name} , size : {file.stat().st_size/1024} mb")