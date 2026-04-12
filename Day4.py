'''✅ Writing files
✅ Overwriting vs Appending
✅ Generating reports/logs'''

from pathlib import Path

'''file = Path("Test.txt")

with file.open("w") as f:
    f.write("\nHello what are you doing?")
    f.write("\nI am doing Coding in Python.")'''


### Writing Multiple Lines.

'''lines = ["Line 1\n", "Line 2\n" , "Line 3"]

with open("Test1.txt","w") as f:
    f.writelines(lines)'''


###Mini Practice (DO THIS)###

'''👉 Read file and save only errors into new file:'''

input_file = Path("Test1.txt")
output_file = Path("Errors.txt")

with input_file.open("r") as f, output_file.open("w") as out:
    for line in f:
        if "error" in line.lower():
            out.write(line)

print("Errors Saved.")