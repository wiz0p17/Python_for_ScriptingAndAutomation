##“CLI File Scanner”

'''
It should:

Take:
--path
--ext
Print all matching files'''


import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("--path",required=True)
parser.add_argument("--ext",required=True)

args = parser.parse_args()

path = Path(args.path)
extension = args.ext

count = 0

for file in path.rglob(f"*.{extension}"):
    count += 1
    print(file.name)

print("Count = ",count)