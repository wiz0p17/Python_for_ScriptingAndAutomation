#!/usr/bin/env python3

##🎯 10. Your Assignment (🔥 Important)
"""
👉 Convert your previous tool:

“monitor.py → monitor command”

Steps:

Add shebang
Make executable
Run without python
(optional) move to /usr/local/bin"""


import subprocess
import time

def run_command(cmd,retry= 3):
    for attempt in range(retry):
        try:
            output = subprocess.run(cmd,capture_output=True,text=True,check=True)

            return output.stdout
        
        except Exception as E:
            print("An Error occoured while executing the file")
            print(E)

def main():
    return run_command(["whoami"])
    """for attempt in range(retry):
        try:
            output = subprocess.run(cmd,capture_output=True,text=True,check=True)

            return output.stdout
        
        except Exception as E:
            print("An Error occoured while executing the file")
            print(E)"""
        
if __name__ == "__main__":
    print(main())





