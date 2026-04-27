##“Advanced CLI File Tool”
"""
It should:

Accept:
--path
--ext
--verbose
Print files
If verbose → show file size"""


import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Advanced CLI file tool")

parser.add_argument("--path",required=True,help="Add path to your folder")
parser.add_argument("--ext",choices=[".py",".txt",".log"],required=True,help="Choose file type")
parser.add_argument("--verbose",action="store_true",help="use if you wnat extra details")

args = parser.parse_args()

path = Path(args.path)

for file in path.rglob(f"*{args.ext}"):
    if args.verbose:

        print("File : ", file.name)
        print("Size : ",file.stat().st_size,"byte")

    else:
        print("File : ",file.name)