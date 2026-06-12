#Assignment (Cloud Engineer Version)
"""
Build:

Health Checker

Arguments:

--cpu
--memory
--disk

Example:

python health.py --cpu

Output:

Checking CPU Usage
python health.py --memory

Output:

Checking Memory Usage"""

import argparse 
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument("--cpu",action="store_true")

parser.add_argument("--memory",action="store_true")

parser.add_argument("--disk",action="store_true")

args = parser.parse_args()

if args.cpu:
    result = subprocess.run(["uptime"],capture_output=True, text=True)

    print(f"CPU: {result.stdout}")

if args.memory:
    result = subprocess.run(["free","-h"],capture_output=True, text=True)

    print(f"Memory: {result.stdout}")

if args.disk:
    result = subprocess.run(["df","-h"],capture_output=True, text=True)

    print(f"Disk: {result.stdout}")