#!/usr/bin/env python3

##👉 Refactor your monitor tool
"""
Split into:

main.py → CLI
commands.py → system logic
config.py → env variables"""

from Command import check_disk,check_cpu,check_user
import os
import argparse 
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()

parser.add_argument("--check",choices=["cpu","disk","user"],required=True)

args = parser.parse_args()

print("Hello from",os.getenv("API_KEY"))

if args.check == "cpu":
    print(check_cpu())

elif args.check == "disk":
    print(check_disk())

elif args.check == "user":
    print(check_user())
