###“Robust File Analyzer”###

'''
It should:  Scan all files
            Skip errors safely

Print:  file name
        size

Count:  processed files
        skipped files'''


from pathlib import Path

processed = 0
skipped = 0

path = Path(".")

for file in path.rglob("*"):
    if file.is_file():
        try:
            print("file name :",file.name)
            print("file size :",file.stat().st_size)
            processed += 1 

        except Exception as e:
            skipped += 1
            print("Error Occoured :",e)

print("Total Files processed : ",processed)
print("Total Files skipped : ",skipped)