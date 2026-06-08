#day 61 code
"""
Why Do Cloud Engineers Use It?

Real examples:

Check disk usage
Check memory usage
Restart services
Take backups
Execute shell scripts
Gather system information

Most automation tools use this concept."""


import subprocess

subprocess.run(["pwd"])
"""
subprocess.run(["ls"])"""

"""Python
   ↓
subprocess.run()
   ↓
Linux Command
   ↓
Result"""

#Capture Output
"""
Normally output goes to terminal.

Let's store it in a variable."""

import subprocess

result = subprocess.run(["pwd"],capture_output=True,text=True)

print(result.stdout)


#Get Current User

import subprocess

result = subprocess.run(["whoami"],capture_output=True,text=True)

print(result.stdout)


#Check Disk Usage

result = subprocess.run(["df","-h"],capture_output=True,text=True)

print(result.stdout)

#Check Memory Usage

import subprocess
"""
result = subprocess.run(["free","-m"],capture_output=True,text=True)

print(result.stdout)"""

#Check return Code

print(result.returncode)


#Mini Project

import subprocess
try:
    commands = [["pwd"],["whoami"],["date"]]

    for command in commands:
        result = subprocess.run(command,capture_output=True,text=True)

    
        print(result.stdout)
except Exception as e:
    print("An error orroured:",e)