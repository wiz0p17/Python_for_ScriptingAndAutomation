##📅 Day 20 – Advanced argparse (Flags, Booleans, Help)

'''
From your roadmap :

✅ Add flags like --verbose
✅ Boolean arguments
✅ Improve help messages
✅ Make scripts user-friendly'''

'''import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--verbose",action="store_true")

args = parser.parse_args()

if args.verbose:
    print("Verbose Mode On")'''



##Multiple Flags Example

'''parser.add_argument("--delete",action="store_true")
parser.add_argument("--dry-run",action="store_true")'''



## Add Help Messages
'''
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--path",help="Path to scan files")

args = parser.parse_args()

print(args.path)'''




##Add Choices (Controlled Input)

'''import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("--type",choices=["txt","py","log"])

args = parser.parse_args()

path = Path(".")

for file in path.rglob(f"*.{args.type}"):
    if file.is_file and not file.name.startswith("."):
        print(file.name)'''



###Real Automation Script (Pro Level)

'''import time
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Cleaner Tool")

parser.add_argument("--path",required=True,help="Path of the folder")
parser.add_argument("--days",type=int,default=7,help="Delete files older than days")
parser.add_argument("--dryrun",action="store_true",help="Test case to delete files")

args = parser.parse_args()

path = Path(args.path)

currentTime = time.time()

for file in path.rglob("*.py"):
    if file.is_file() and not file.name.startswith("."):

        age = currentTime - file.stat().st_mtime

        if args.dryrun:
            if age > args.days * 86400:
                print("deleting files : ",file.name)

            else:
                print("")'''



##Mini Practice (DO THIS)
        
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name",required=True)
parser.add_argument("--verbose",action="store_true")

args = parser.parse_args()

if args.verbose:
    print("Running in verbose mode")

print("Hello",args.name)