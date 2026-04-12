###Log Report Generator ###

'''It should:

Read a file
Count:
total lines
error lines
Write a report into report.txt'''

from pathlib import Path

inputFile = Path("Test1.txt")
outputFile = Path("Report.txt")

totalLines = 0
totalErrors = 0

with inputFile.open("r") as f,outputFile.open("w") as out:
    totalLines = totalLines + 1
    for line in f:
        if "error" in line.lower():
            totalErrors = totalErrors + 1
            out.write(line)

with outputFile.open("r") as f:
    for line in f:
        print(line)