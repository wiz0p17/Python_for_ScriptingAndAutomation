##📅 Day 19 – CLI Arguments with argparse

'''
✅ Accept user input via terminal
✅ Build flexible scripts with flags
✅ Create real CLI tools'''


##Basic argparse Setup

import argparse

'''
parser = argparse.ArgumentParser()

parser.add_argument("--name")

args = parser.parse_args()

print("Hello",args.name)'''

"""
parser = argparse.ArgumentParser()

parser.add_argument("--path")
parser.add_argument("--days",type=int)

args = parser.parse_args()

print("Path : ",args.path)
print("Days : ",args.days)"""



#Required Arguments
#parser.add_argument("--path",required=True)
#👉 Script will fail if not provided



##Default Values
#parser.add_argument("--days",type=int,default=7)
#👉 If user doesn’t pass → default used

'''
import argparse
import time
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("--path",required=True)
parser.add_argument("--days",type=int,default=7)

args = parser.parse_args()

path = Path(args.path)
days = args.days

currentTime = time.time()

for file in path.rglob("*.py"):
    age = currentTime - file.stat().st_mtime

    if age > days * 86400:
        print("Deleting File : ",file.name)
        #file.unlink()

print("Script Executed!!")'''



#Mini Practice

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--num1",required=True,type=int)
parser.add_argument("--num2",required=True,type=int)

args = parser.parse_args()

print("Sum = ",args.num1+ args.num2)