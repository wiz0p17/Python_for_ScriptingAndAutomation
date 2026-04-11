'''“Log Analyzer”

It should:

Read a file
Count total lines
Count how many lines contain "ERROR"'''


from pathlib import Path

file = Path("Test.txt")

no_of_lines = 0
count = 0
with file.open("r") as f:
    for line in f:
        no_of_lines = no_of_lines + 1
        if "error" in line.lower():
            count = count + 1
            print("Line number = ",no_of_lines," Error :",line)

print("Total number of errors :",count)
print("Total number of Lines :",no_of_lines)