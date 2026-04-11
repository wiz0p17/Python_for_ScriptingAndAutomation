from pathlib import Path

'''with open("Test.txt","r") as file:
    content = file.read()
    print(content)'''

'''with open("Test.txt","r") as file:
    for line in file:
        print(line)'''

'''with open("Test.txt","r") as file:
    lines = file.readlines()

print(lines[2])


with open("Test.txt","r") as file:
    for line in file:
        if "error" in line:
            print("Error occoured : ",line)'''


## Best practice ##


file = Path("Test.txt")

with file.open("r") as f:
    print(f.read())

