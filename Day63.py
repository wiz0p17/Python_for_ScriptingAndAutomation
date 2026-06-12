#Day 63 – argparse (Build Professional Command-Line Tools)
"""
import argparse

parser = argparse.ArgumentParser()

args = parser.parse_args()

print(args)"""


#Add Your First Argument
"""
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name")

args = parser.parse_args()

print(args.name)"""


"""
Terminal
    ↓
--name Vivek
    ↓
argparse
    ↓
args.name
    ↓
Vivek"""


"""
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name",required=True,default="Vivek")

parser.add_argument("--age",type=int)

args = parser.parse_args()

print(args.name)

print(args.age)"""

"""import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--server",required=True)

args = parser.parse_args()

print(f"Monitoring {args.server}")"""


#boolean flags
"""
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--cpu",action="store_true")

args = parser.parse_args()

print(args.cpu)"""


#real Devops example

import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument("--cpu",action="store_true")

args = parser.parse_args()

if args.cpu :
    result = subprocess.run(["uptime"],capture_output=True,text=True)

    print(f"CPU: {result.stdout}")

