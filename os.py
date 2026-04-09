import os

files = os.listdir(".")
print(files)

os.rename("Python Basics","CHL")


'''with open("test.txt","a") as file:
    file.write("\nPython is a programming language")'''


with open("test.txt","r") as file:
    print(file.read())


'''
"r" → read
"w" → overwrite
"a" → append'''

